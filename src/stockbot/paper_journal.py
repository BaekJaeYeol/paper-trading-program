"""Durable journal and GET-only reconciliation for legacy Alpaca paper orders."""
from contextlib import closing
from datetime import datetime
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path
import sqlite3
import time
from zoneinfo import ZoneInfo
from . import brackets
from .ui_safety import ORDER_STATES,order_row,unresolved_attempts

TERMINAL={'filled','canceled','rejected','expired','replaced'}
PROBLEMS={'missing':'조회 결과 없음','lookup_failed':'조회 실패','mismatch':'주문 정보 불일치','legacy':'이전 형식 · 수동 대조 필요','awaiting_check':'브로커 상태 확인 전','take_profit':'익절 자식 주문','stop_loss':'손절 자식 주문','pending':'주문 요청 기록','response_lost':'주문 응답 미확인'}

def fingerprint(account):
    identity=account.get('id')
    if not isinstance(identity,str) or not identity.strip():raise ValueError('Account identity missing')
    return hashlib.sha256(('alpaca-paper:'+identity).encode()).hexdigest()


def account_snapshot(broker):
    """Read-only snapshot. Never return credentials or account identifiers."""
    started=time.monotonic()
    account = broker.request('/v2/account')
    clock = broker.request('/v2/clock')
    positions = broker.request('/v2/positions')
    orders = broker.request('/v2/orders', {'status': 'open', 'limit': 500, 'nested': 'false'})
    if len(orders) >= 500:
        raise ValueError('Order snapshot may be truncated')
    for order in orders:order_row(order)
    if any(not math.isfinite(float(account[k])) for k in ('equity','cash','buying_power','last_equity')):raise ValueError('Invalid account amounts')
    return {'received_at':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
            'request_seconds':time.monotonic()-started,
            'received_monotonic':time.monotonic(),
            'account_fingerprint':fingerprint(account),
            'can_trade':account.get('status')=='ACTIVE' and not account.get('trading_blocked') and not account.get('account_blocked'),
            'equity': float(account['equity']), 'cash': float(account['cash']),
            'buying_power': float(account['buying_power']),
            'daily_pnl': float(account['equity']) - float(account['last_equity']),
            'market_open': clock['is_open'],
            'positions': [{k: p.get(k, '') for k in
                           ('symbol', 'qty', 'avg_entry_price', 'current_price', 'unrealized_pl')}
                          for p in positions],
            'orders': [{k: o.get(k, '') for k in
                        ('symbol', 'side', 'qty', 'filled_qty', 'limit_price', 'status')}
                       for o in orders]}


def initialize(db):
    db.executescript('''
    CREATE TABLE IF NOT EXISTS attempts(id TEXT PRIMARY KEY,status TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS paper_requests(client_id TEXT PRIMARY KEY,payload TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS paper_meta(key TEXT PRIMARY KEY,value TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS paper_checks(client_id TEXT PRIMARY KEY,broker_id TEXT,status TEXT NOT NULL,filled TEXT NOT NULL,checked_at TEXT NOT NULL,outcome TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS paper_events(seq INTEGER PRIMARY KEY AUTOINCREMENT,client_id TEXT NOT NULL,kind TEXT NOT NULL,status TEXT NOT NULL,filled TEXT NOT NULL,checked_at TEXT NOT NULL);
    ''')
    brackets.initialize(db)

def bind_account(db,identity):
    if not isinstance(identity,str) or len(identity)!=64:raise ValueError('Invalid account fingerprint')
    row=db.execute("SELECT value FROM paper_meta WHERE key='account'").fetchone()
    if row and row[0]!=identity:raise ValueError('State directory belongs to another paper account')
    db.execute("INSERT OR IGNORE INTO paper_meta VALUES ('account',?)",(identity,))

def intent(db,cid,payload):
    db.execute("INSERT INTO attempts(id,status) VALUES (?,'pending')",(cid,))
    db.execute('INSERT INTO paper_requests VALUES (?,?)',(cid,json.dumps(payload,sort_keys=True,allow_nan=False)))
    save_check(db,cid,None,'pending','0','pending')

def save_check(db,cid,bid,status,filled,outcome):
    now=datetime.now(ZoneInfo('Asia/Seoul')).isoformat()
    old=db.execute('SELECT broker_id,status,filled,outcome FROM paper_checks WHERE client_id=?',(cid,)).fetchone()
    values=(bid,status,str(filled),outcome)
    if old!=values:
        db.execute('INSERT INTO paper_events(client_id,kind,status,filled,checked_at) VALUES (?,?,?,?,?)',(cid,outcome,status,str(filled),now))
    db.execute('INSERT OR REPLACE INTO paper_checks VALUES (?,?,?,?,?,?)',(cid,bid,status,str(filled),now,outcome))

def submitted(db,cid,response):
    bid=response.get('id') if isinstance(response,dict) else None
    if not isinstance(bid,str) or not bid or len(bid)>128:raise ValueError('Missing broker order identity')
    if response.get('client_order_id',cid)!=cid:raise ValueError('Submission identity mismatch')
    save_check(db,cid,bid,'submitted','0','awaiting_check')
    db.execute("UPDATE attempts SET status='submitted' WHERE id=?",(cid,))

def amount(value):
    n=Decimal(str(value))
    if not n.is_finite() or n<0:raise ValueError('Invalid quantity or price')
    return n

def validate_order(cid,payload,order,old):
    if not isinstance(order,dict) or order.get('client_order_id')!=cid:raise ValueError('Client identity mismatch')
    bid=order.get('id')
    if not isinstance(bid,str) or not bid or len(bid)>128:raise ValueError('Broker identity missing')
    for key in ('symbol','side','type','order_class','time_in_force'):
        if order.get(key)!=payload.get(key):raise ValueError('Order fields changed')
    qty=amount(order.get('qty'));filled=amount(order.get('filled_qty'))
    if qty<=0 or qty!=amount(payload['qty']) or filled>qty:raise ValueError('Order size mismatch')
    if amount(order.get('limit_price'))!=amount(payload['limit_price']):raise ValueError('Limit changed')
    status=order.get('status')
    if status not in ORDER_STATES:raise ValueError('Unknown broker state')
    if status=='filled' and filled!=qty:raise ValueError('Incomplete filled order')
    if status=='partially_filled' and not 0<filled<qty:raise ValueError('Invalid partial fill')
    if old:
        if old[0] and bid!=old[0]:raise ValueError('Broker identity changed')
        if filled<amount(old[2]):raise ValueError('Cumulative fill decreased')
        if old[1] in TERMINAL and status!=old[1]:raise ValueError('Terminal status changed')
    return bid,status,str(filled)

def problem(db,cid,reason,old):
    db.execute("UPDATE attempts SET status='unknown' WHERE id=?",(cid,))
    save_check(db,cid,old[0] if old else None,old[1] if old else 'unknown',old[2] if old else '0',reason)

def history(db):
    rows=[]
    for cid,payload,status,filled,when,outcome,attempt in db.execute('''
        SELECT a.id,r.payload,c.status,c.filled,c.checked_at,c.outcome,a.status
        FROM attempts a LEFT JOIN paper_requests r ON r.client_id=a.id
        LEFT JOIN paper_checks c ON c.client_id=a.id ORDER BY a.rowid DESC LIMIT 200'''):
        p=json.loads(payload) if payload else {}
        qty=p.get('qty');filled=filled or '0'
        label=ORDER_STATES.get(status,'미확인') if outcome=='confirmed' else PROBLEMS.get(outcome or 'legacy','미확인')
        remaining=str(amount(qty)-amount(filled)) if qty is not None else '—'
        rows.append({'client_id':cid,'symbol':p.get('symbol','—'),'qty':qty or '—','filled_qty':filled,'remaining_qty':remaining,'status':label,'checked_at':when or '미확인'})
    events=[{'client_id':cid,'kind':PROBLEMS.get(kind,'브로커 확인'),'status':ORDER_STATES.get(status,{'pending':'요청 기록','submitted':'접수 응답 수신','unknown':'미확인'}.get(status,'미확인')),'filled_qty':filled,'checked_at':when} for cid,kind,status,filled,when in db.execute('SELECT client_id,kind,status,filled,checked_at FROM paper_events ORDER BY seq DESC LIMIT 200')]
    return rows,events

def submission_uncertain(db,cid):
    old=db.execute('SELECT broker_id,status,filled,outcome FROM paper_checks WHERE client_id=?',(cid,)).fetchone()
    problem(db,cid,'response_lost',old)

def reconcile_snapshot(c,broker,reader):
    """No submit/cancel/STOP removal; unknown absence never authorizes replay."""
    root=Path(c['state_dir']);root.mkdir(parents=True,exist_ok=True);lock=root/'cycle.lock'
    try:lock.mkdir()
    except FileExistsError:raise RuntimeError('Another cycle or stale lock requires review') from None
    try:
        cancel=c.get('_reconcile_cancel')
        def interrupted():
            if cancel is not None and cancel.is_set():raise RuntimeError('Reconciliation interrupted')
        interrupted()
        data=reader(broker)
        interrupted()
        if data.get('request_seconds',float('inf'))>60:raise ValueError('Snapshot delayed')
        with closing(sqlite3.connect(root/'orders.sqlite',timeout=5)) as db:
            initialize(db);db.execute('BEGIN IMMEDIATE');bind_account(db,data.get('account_fingerprint'))
            db.execute("INSERT OR REPLACE INTO paper_meta VALUES ('inventory_gate',?)",(json.dumps({'ready':False,'rows':[],'reason':'대조 중'}),));db.commit()
            rows=db.execute('SELECT a.id,a.status,r.payload FROM attempts a LEFT JOIN paper_requests r ON r.client_id=a.id ORDER BY a.rowid').fetchall()
            checked=0;legacy=0
            for cid,state,raw in rows:
                interrupted()
                if not raw:
                    legacy+=1
                    continue
                old=db.execute('SELECT broker_id,status,filled,outcome FROM paper_checks WHERE client_id=?',(cid,)).fetchone()
                try:order=broker.find_order(cid)
                except Exception:
                    problem(db,cid,'lookup_failed',old);db.commit();continue
                if order is None:
                    problem(db,cid,'missing',old);db.commit();continue
                try:
                    payload=json.loads(raw)
                    bid,status,filled=validate_order(cid,payload,order,old)
                    order=broker.bracket_order(bid)
                    if not isinstance(order,dict) or order.get('id')!=bid:raise ValueError('Nested parent identity mismatch')
                    bid,status,filled=validate_order(cid,payload,order,old)
                    brackets.save_legs(db,cid,payload,order)
                except Exception:
                    problem(db,cid,'mismatch',old);db.commit();continue
                save_check(db,cid,bid,status,filled,'confirmed')
                db.execute("UPDATE attempts SET status='confirmed' WHERE id=?",(cid,));db.commit();checked+=1
            # Refresh balances/open orders AFTER order lookups; do not derive balances from fills.
            if rows:
                final=reader(broker)
                interrupted()
                if final.get('account_fingerprint')!=data.get('account_fingerprint') or final.get('request_seconds',float('inf'))>60:raise ValueError('Snapshot changed account or delayed')
                data=final
            if time.monotonic()-data.get('received_monotonic',time.monotonic())>60:raise ValueError('Snapshot stale')
            data['inventory']=brackets.inventory(db,data['positions'],legacy)
            data['order_history'],data['order_events']=history(db)
            data['order_history']=sorted(data['order_history']+brackets.leg_history(db),key=lambda r:r['checked_at'] if r['checked_at']!='미확인' else '',reverse=True)[:200]
            data['reconciliation']={'checked':checked,'unresolved':len(unresolved_attempts(root)),'legacy':legacy,'read_only':True}
            return data
    finally:lock.rmdir()
