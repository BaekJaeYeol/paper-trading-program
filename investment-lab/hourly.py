"""Unattended daily-bar paper research. No broker or user credentials."""
import argparse
import datetime
import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from data import download
from engine import load
from validation import Fleet, batch_validate


def tick(state, symbols=('SPY','QQQ','IWM','DIA'), downloader=download):
    state=Path(state);state.mkdir(parents=True,exist_ok=True)
    status={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'symbols':{},'real_orders':False}
    for symbol in symbols:
        try:
            with tempfile.TemporaryDirectory() as temp:
                stage=Path(temp)/symbol
                previous=state/symbol
                if previous.exists():shutil.copytree(previous,stage)
                else:stage.mkdir()
                path=downloader(symbol,stage/'data.csv')
                rows=load(path)
                accounts=Fleet(stage/'fleet').update(symbol,rows)
                digest=hashlib.sha256(Path(path).read_bytes()).hexdigest()
                old=stage/'digest.txt'
                if not old.exists() or old.read_text()!=digest:
                    batch_validate({symbol:path},stage/'research','real_download')
                    old.write_text(digest)
                (stage/'accounts.json').write_text(json.dumps(accounts,ensure_ascii=False,indent=2),encoding='utf-8')
                # Each symbol is staged independently; errors preserve its previous accounts.
                if previous.exists():shutil.rmtree(previous)
                shutil.copytree(stage,previous)
                status['symbols'][symbol]={'status':'ok','last_completed_bar':rows[-1][0],'accounts':len(accounts)}
        except Exception as exc:
            status['symbols'][symbol]={'status':'error','message':str(exc)}
    (state/'status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(status,ensure_ascii=False))
    return status

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--state',required=True);a=p.parse_args()
    status=tick(a.state)
    if any(s['status']=='error' for s in status['symbols'].values()):raise SystemExit(1)
