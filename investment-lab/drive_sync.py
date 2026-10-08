"""Export only selected results to a user-selected Drive desktop folder.
A successful local write is never proof of cloud delivery.
"""
import datetime, hashlib, json, os, re, uuid, zipfile
from zoneinfo import ZoneInfo
from pathlib import Path

REPORT_KEYS=('source','data_sha256','first_date','last_date','selected','fee','slippage','selection','holdout_start','status','live_ready','results')

def payload(report=None, account=None, symbol=None):
    result={'schema_version':1,'symbol':symbol,'cloud_upload_verified':False}
    if report is not None: result['research']={k:report[k] for k in REPORT_KEYS if k in report}
    if account and account.get('active'):
        result['paper']={k:account[k] for k in ('cash','qty','last_date','equity','ledger')}
        result['paper']['config']={k:account['config'][k] for k in ('strategy','source','fee','slippage','started_after')}
    return result

def atomic_write(path,data):
    temp=path.with_name(path.name+'.'+uuid.uuid4().hex+'.tmp')
    try:
        temp.write_bytes(data);os.replace(temp,path)
    finally:
        temp.unlink(missing_ok=True)

def compact(folder):
    """Keep latest per symbol/source and verified monthly archives of all snapshots."""
    groups={}
    for item in folder.glob('investment-lab-*.json'):
        if not re.fullmatch(r'investment-lab-[0-9a-f]{64}\.json',item.name):continue
        data=item.read_bytes()
        if hashlib.sha256(data).hexdigest()!=item.stem.removeprefix('investment-lab-'):
            raise ValueError('결과 파일 해시가 다릅니다. 원본을 유지합니다.')
        value=json.loads(data)
        month=datetime.datetime.fromtimestamp(item.stat().st_mtime,ZoneInfo('Asia/Seoul')).strftime('%Y-%m')
        groups.setdefault(month,[]).append((item,data,value,item.stat().st_mtime))
    for month,items in groups.items():
        archive=folder/f'investment-lab-history-{month}.zip'
        existing={}
        if archive.exists():
            with zipfile.ZipFile(archive) as z:
                if z.testzip() is not None:raise ValueError('기존 월별 보관 파일을 확인하세요.')
                existing={name:z.read(name) for name in z.namelist()}
        updated=dict(existing)
        for item,data,_,_ in items:
            if item.name in updated and updated[item.name]!=data:raise ValueError('보관 파일 충돌: 원본 유지')
            updated[item.name]=data
        if updated!=existing:
            temp=archive.with_name(archive.name+'.'+uuid.uuid4().hex+'.tmp')
            try:
                with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as z:
                    for name,data in updated.items():z.writestr(name,data)
                with zipfile.ZipFile(temp) as z:
                    if z.testzip() is not None or any(z.read(name)!=data for name,data in updated.items()):
                        raise ValueError('압축 검증 실패: 원본 유지')
                os.replace(temp,archive)
            finally:temp.unlink(missing_ok=True)
        for item,data,value,mtime in sorted(items,key=lambda x:x[3]):
            stream=json.dumps([value.get('symbol'),value.get('research',{}).get('source'),bool(value.get('paper'))],ensure_ascii=False)
            latest=folder/('investment-lab-latest-'+hashlib.sha256(stream.encode()).hexdigest()[:16]+'.json')
            if not latest.exists() or mtime>=latest.stat().st_mtime:
                atomic_write(latest,data);os.utime(latest,(mtime,mtime))
            item.unlink()

class DriveSync:
    def __init__(self,work):
        self.work=Path(work);self.config_path=self.work/'drive_settings.json'
        self.settings={'enabled':False,'folder':''}
        if self.config_path.exists():
            try:self.settings.update(json.loads(self.config_path.read_text(encoding='utf-8')))
            except (ValueError,OSError):pass
    def configure(self,folder,enabled):
        p=Path(folder).expanduser().resolve() if folder else None
        if enabled and (p is None or not p.is_dir()):raise ValueError('기존 Google Drive 동기화 폴더를 선택하세요.')
        if enabled and (p==self.work.resolve() or self.work.resolve() in p.parents):raise ValueError('workspace 외부의 Drive 폴더를 선택하세요.')
        self.settings={'enabled':bool(enabled),'folder':str(p) if p else ''}
        self.work.mkdir(parents=True,exist_ok=True)
        atomic_write(self.config_path,json.dumps(self.settings,ensure_ascii=False).encode('utf-8'))
    def export(self,value=None):
        if not self.settings['enabled']:return '자동 저장 꺼짐'
        outbox=self.work/'drive_outbox';outbox.mkdir(parents=True,exist_ok=True)
        if value is not None:
            data=json.dumps(value,ensure_ascii=False,indent=2,sort_keys=True,allow_nan=False).encode('utf-8')
            name='investment-lab-'+hashlib.sha256(data).hexdigest()+'.json'
            atomic_write(outbox/name,data)
        folder=Path(self.settings['folder'])
        pending=list(outbox.glob('investment-lab-*.json'))
        try:
            # Never recreate a disappeared mount or silently redirect to another folder.
            if not folder.is_dir():raise OSError('동기화 폴더를 사용할 수 없습니다')
            for item in pending:
                data=item.read_bytes();dest=folder/item.name
                if not dest.exists() or dest.read_bytes()!=data:
                    atomic_write(dest,data);os.utime(dest,(item.stat().st_mtime,item.stat().st_mtime))
                item.unlink()
            compact(folder)
            return f'최신 결과 · 월별 보관 완료 ({len(pending)}건) · 클라우드 업로드 미확인'
        except (OSError,ValueError,zipfile.BadZipFile):
            return f'폴더 저장 대기 ({len(list(outbox.glob("*.json")))}건) · Drive 연결 또는 보관 파일 확인 후 재시도'
