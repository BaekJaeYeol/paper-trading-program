"""Export only selected results to a user-selected Drive desktop folder.
A successful local write is never proof of cloud delivery.
"""
import hashlib, json, os, uuid
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
                if not dest.exists() or dest.read_bytes()!=data:atomic_write(dest,data)
                item.unlink()
            return f'동기화 폴더 저장 완료 ({len(pending)}건) · 클라우드 업로드 미확인'
        except OSError:
            return f'폴더 저장 대기 ({len(list(outbox.glob("*.json")))}건) · Drive 연결 확인 후 재시도'
