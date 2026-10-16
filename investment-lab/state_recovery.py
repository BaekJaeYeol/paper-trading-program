"""Conservative recovery for local research snapshots; no broker operations."""
import argparse
from contextlib import contextmanager, closing
import json
import hashlib
import math
import os
from pathlib import Path
import shutil
import sqlite3
import tempfile
import uuid


@contextmanager
def state_lock(state):
    """OS lock is released on process death; never delete a possibly active lock."""
    state=Path(state).resolve()
    state.parent.mkdir(parents=True,exist_ok=True)
    path=state.with_name('.'+state.name+'.lock')
    with path.open('a+b') as handle:
        handle.seek(0,2)
        if handle.tell()==0:
            handle.write(b'0');handle.flush()
        handle.seek(0)
        try:
            if os.name=='nt':
                import msvcrt
                msvcrt.locking(handle.fileno(),msvcrt.LK_NBLCK,1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
        except OSError as exc:
            raise RuntimeError('이미 실행 중입니다. 같은 상태 폴더의 중복 실행을 중단하세요.') from exc
        try:
            yield
        finally:
            handle.seek(0)
            if os.name=='nt':
                msvcrt.locking(handle.fileno(),msvcrt.LK_UNLCK,1)
            else:
                fcntl.flock(handle.fileno(),fcntl.LOCK_UN)


def atomic_json(path,value):
    path=Path(path)
    temporary=None
    try:
        with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=path.parent,
                                         prefix='.'+path.name+'.',suffix='.tmp',delete=False) as handle:
            temporary=Path(handle.name)
            json.dump(value,handle,ensure_ascii=False,indent=2,allow_nan=False)
            handle.flush();os.fsync(handle.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def validate_snapshot(folder):
    from operational_audit import validate_account
    folder=Path(folder)
    bars=json.loads((folder/'bars.json').read_text(encoding='utf-8'))
    accounts=json.loads((folder/'accounts.json').read_text(encoding='utf-8'))
    v2=json.loads((folder/'accounts-v2.json').read_text(encoding='utf-8'))
    if not bars or not isinstance(accounts,dict) or not accounts or not isinstance(v2,dict) or not v2:
        raise ValueError('복구 스냅샷의 필수 데이터가 비어 있습니다')
    last=bars[-1]
    for account in v2.values():
        validate_account(account)
        if account['last_date']!=last[0] or abs(account['mark']-last[4])>1e-6:
            raise ValueError('복구 스냅샷 v2 기준 봉 불일치')
    for name,account in accounts.items():
        if account['last_date']!=last[0] or not all(isinstance(account[k],(int,float)) and math.isfinite(account[k]) and account[k]>=0 for k in ('cash','qty','equity')):
            raise ValueError('복구 스냅샷 v1 계좌 오류')
        if not math.isclose(account['cash']+account['qty']*last[4],account['equity'],abs_tol=.01,rel_tol=1e-9):
            raise ValueError('복구 스냅샷 v1 평가액 불일치')
        path=folder/'accounts'/(hashlib.sha256(name.encode()).hexdigest()[:16]+'.sqlite')
        with closing(sqlite3.connect(path.resolve().as_uri()+'?mode=ro',uri=True)) as db:
            if db.execute('PRAGMA quick_check').fetchone()[0]!='ok':
                raise ValueError('복구 스냅샷 SQLite 무결성 오류')
            saved=db.execute('SELECT cash,qty,last_date,mark FROM account WHERE id=1').fetchone()
            if saved is None or saved[2]!=last[0] or abs(saved[3]-last[4])>1e-6 or not all(math.isclose(saved[i],account[k],rel_tol=1e-9,abs_tol=.000001) for i,k in enumerate(('cash','qty'))):
                raise ValueError('복구 스냅샷 SQLite·계좌 요약 불일치')


def recover_snapshot(destination):
    """Caller holds state lock. Restore only an unambiguous validated backup."""
    destination=Path(destination)
    backup=destination.with_name(destination.name+'.backup')
    pending=destination.with_name(destination.name+'.pending')
    actions=[]
    if not destination.exists() and not backup.exists() and pending.exists():
        raise ValueError('미완료 저장만 남았습니다. 새 계좌 생성 중단; 장애 복구 안내를 확인하세요.')
    if backup.exists():
        if not destination.exists():
            validate_snapshot(backup)
            backup.rename(destination)
            actions.append('검증된 교체 전 백업 복구')
        else:
            # Both exist after a crash following successful rename: keep current,
            # preserve the old backup separately; never guess if current is bad.
            validate_snapshot(destination)
            actions.append('현재 스냅샷 검증; 이전 백업 별도 보존')
    for leftover in (backup,pending):
        if leftover.exists():
            archive=destination.parent/'recovery-archives'
            archive.mkdir(exist_ok=True)
            leftover.rename(archive/(leftover.name+'.'+uuid.uuid4().hex))
            actions.append(leftover.suffix+'를 복구 보관함으로 이동')
    return actions


def ensure_space(state,symbol):
    folder=Path(state)/symbol
    size=sum(p.stat().st_size for p in folder.rglob('*') if p.is_file()) if folder.exists() else 0
    required=64*1024*1024+2*size
    if shutil.disk_usage(state).free<required:
        raise OSError('디스크 여유 공간 부족: 계좌 갱신 중단. 복구 보관함을 백업한 뒤 공간을 확보하세요.')


def main():
    parser=argparse.ArgumentParser(description='기본은 읽기 전용 진단. 계좌 초기화·실주문 없음.')
    parser.add_argument('--state',required=True)
    parser.add_argument('--recover',action='store_true',help='단독 실행 잠금 후 명확한 교체 중단 상태만 복구')
    args=parser.parse_args()
    state=Path(args.state).resolve()
    if not state.is_dir():
        parser.error('기존 상태 폴더를 지정하세요. 새 계좌를 만들지 않습니다.')
    symbols=sorted({p.name.removesuffix('.backup').removesuffix('.pending') for p in state.iterdir()
                    if p.is_dir() and (p.name.endswith(('.backup','.pending')) or (p/'accounts-v2.json').exists())})
    result={}
    def check():
        for symbol in symbols:
            try:
                actions=recover_snapshot(state/symbol) if args.recover else []
                validate_snapshot(state/symbol)
                result[symbol]={'status':'ok','actions':actions}
            except Exception as exc:
                result[symbol]={'status':'error','message':str(exc)}
    if args.recover:
        with state_lock(state):check()
    else:
        check()
    for name,kind in (('status.json',dict),('operations-history.json',list)):
        path=state/name
        if path.exists():
            try:
                if not isinstance(json.loads(path.read_text(encoding='utf-8')),kind):
                    raise ValueError('운영 보고서 형식 불일치')
                result[name]={'status':'ok'}
            except Exception as exc:
                result[name]={'status':'error','message':str(exc)+'; 계좌를 초기화하지 말고 마지막 정상 저장본을 확인하세요.'}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return int(any(info['status']=='error' for info in result.values()))


if __name__=='__main__':raise SystemExit(main())
