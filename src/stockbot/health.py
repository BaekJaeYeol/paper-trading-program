"""Bounded local reconciliation events. Fixed codes only; never exception text."""
from contextlib import closing
from datetime import datetime
from pathlib import Path
import sqlite3
from zoneinfo import ZoneInfo

STATES={
 'timeout':('전체 대조 시간 초과','계좌·주문을 다시 대조하고 명시적으로 재개하세요.'),
 'cancelled':('대조 취소','STOP과 증권사 주문 상태를 확인한 뒤 다시 대조하세요.'),
 'failed':('대조 실패','연결·계좌·DB 상태를 확인한 뒤 다시 대조하세요.'),
 'blocked':('대조 완료 · 진입 차단','계좌 권한·차단 상세·미확인 주문·보유 수량을 확인하세요.'),
 'recovered':('대조 복구 · 자동 재개 아님','대조에 통과했습니다. 자동매매 재개는 별도 확인이 필요합니다.'),
}

def initialize(db):
    db.execute('''CREATE TABLE IF NOT EXISTS paper_system_events(
        seq INTEGER PRIMARY KEY AUTOINCREMENT,code TEXT NOT NULL,
        first_seen TEXT NOT NULL,last_seen TEXT NOT NULL,occurrences INTEGER NOT NULL)''')

def record(db,code):
    if code not in STATES:raise ValueError('Unknown system event code')
    now=datetime.now(ZoneInfo('Asia/Seoul')).isoformat()
    last=db.execute('SELECT seq,code FROM paper_system_events ORDER BY seq DESC LIMIT 1').fetchone()
    if last and last[1]==code:
        db.execute('UPDATE paper_system_events SET last_seen=?,occurrences=MIN(occurrences+1,1000000000) WHERE seq=?',(now,last[0]))
    else:db.execute('INSERT INTO paper_system_events(code,first_seen,last_seen,occurrences) VALUES (?,?,?,1)',(code,now,now))
    db.execute('DELETE FROM paper_system_events WHERE seq NOT IN (SELECT seq FROM paper_system_events ORDER BY seq DESC LIMIT 200)')

def result(db,ready):
    if not ready:record(db,'blocked');return
    last=db.execute('SELECT code FROM paper_system_events ORDER BY seq DESC LIMIT 1').fetchone()
    if last and last[0]!='recovered':record(db,'recovered')

def stamp(value):
    try:
        dt=datetime.fromisoformat(value)
        if dt.tzinfo is None:return '미확인'
        return dt.astimezone(ZoneInfo('Asia/Seoul')).isoformat()
    except (ValueError,TypeError,OverflowError):return '미확인'

def history(db):
    events=[]
    for code,first,last,count in db.execute('SELECT code,first_seen,last_seen,occurrences FROM paper_system_events ORDER BY seq DESC LIMIT 50'):
        code=code if code in STATES else 'failed';title,action=STATES[code]
        events.append({'code':code,'title':title,'next_action':action,'first_seen':stamp(first),'last_seen':stamp(last),'occurrences':count if type(count) is int and 0<count<=1000000000 else 1})
    return {'available':True,'events':events,'display_limit':50,'retention_limit':200}

def load(directory):
    path=Path(directory)/'orders.sqlite'
    if not path.exists():return {'available':True,'events':[]}
    try:
        with closing(sqlite3.connect(path.resolve().as_uri()+'?mode=ro',uri=True,timeout=.05)) as db:
            if not db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='paper_system_events'").fetchone():return {'available':True,'events':[]}
            return history(db)
    except (OSError,sqlite3.Error):return {'available':False,'events':[]}

def summary(data):
    events=data.get('events',[])
    return {'available':data.get('available') is True,'display_limit':50,
            'latest_code':events[0]['code'] if events and events[0].get('code') in STATES else None,
            'displayed_event_groups':len(events),
            'counts_in_displayed_groups':{code:sum(e.get('occurrences',0) for e in events if e.get('code')==code and type(e.get('occurrences')) is int and 0<e['occurrences']<=1000000000) for code in STATES}}
