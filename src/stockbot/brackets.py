"""Read-only bracket linkage and managed-symbol quantity checks. Never sells."""
from datetime import datetime,timezone
from decimal import Decimal
import json
from zoneinfo import ZoneInfo
from .ui_safety import ORDER_STATES
from . import review_cases as review

FINAL={'filled','canceled','rejected','expired'}

def number(value):
    n=Decimal(str(value))
    if not n.is_finite() or n<0:raise ValueError('Invalid bracket quantity/price')
    return n

def initialize(db):
    db.execute('''CREATE TABLE IF NOT EXISTS paper_legs(
        parent TEXT NOT NULL,role TEXT NOT NULL,broker_id TEXT NOT NULL UNIQUE,
        symbol TEXT NOT NULL,qty TEXT NOT NULL,filled TEXT NOT NULL,status TEXT NOT NULL,
        price TEXT NOT NULL,checked_at TEXT NOT NULL,PRIMARY KEY(parent,role))''')

def save_legs(db,cid,payload,root):
    initialize(db)
    legs=root.get('legs')
    old={r[0]:r[1:] for r in db.execute('SELECT role,broker_id,qty,filled,status FROM paper_legs WHERE parent=?',(cid,))}
    if legs is None:legs=[]
    if not isinstance(legs,list) or len(legs)>2:raise ValueError('Invalid bracket graph')
    parent_qty=number(root['qty']);parent_filled=number(root['filled_qty'])
    if not legs:
        if old or parent_filled==parent_qty:raise ValueError('Bracket legs missing')
        return
    parsed={};ids=set()
    for leg in legs:
        kind=leg.get('type');role={'limit':'take_profit','stop':'stop_loss'}.get(kind)
        if role is None or role in parsed:raise ValueError('Unexpected bracket role')
        bid=leg.get('id');status=leg.get('status')
        if not isinstance(bid,str) or not bid or bid==root['id'] or bid in ids:raise ValueError('Duplicate bracket identity')
        owner=db.execute('SELECT parent FROM paper_legs WHERE broker_id=?',(bid,)).fetchone()
        if owner and owner[0]!=cid:raise ValueError('Child belongs to another parent')
        ids.add(bid)
        if leg.get('symbol')!=payload['symbol'] or leg.get('side')!='sell':raise ValueError('Child symbol/side mismatch')
        if status in ('replaced','pending_replace') or leg.get('replaced_by') or leg.get('replaces'):raise review.ReviewRequired('order_replaced','원래 자식 주문',status)
        if leg.get('time_in_force')!=payload['time_in_force'] or status not in ORDER_STATES:raise ValueError('Unsupported child change')
        if leg.get('legs'):raise ValueError('Unexpected descendant orders')
        qty=number(leg.get('qty'));filled=number(leg.get('filled_qty'))
        if not 0<qty<=parent_qty or filled>qty:raise ValueError('Child quantity mismatch')
        if status=='filled' and filled!=qty:raise ValueError('Child filled mismatch')
        if status=='partially_filled' and not 0<filled<qty:raise ValueError('Invalid partial child')
        key='limit_price' if role=='take_profit' else 'stop_price'
        price=number(leg.get(key))
        if price!=number(payload[role][key]):raise review.ReviewRequired('price_changed',payload[role][key],leg.get(key))
        if role in old:
            before=old[role]
            if before[0]!=bid:raise review.ReviewRequired('identity_changed',before[0],bid)
            if filled<number(before[2]):raise review.ReviewRequired('fill_regressed',before[2],str(filled))
            if before[3] in FINAL and status!=before[3]:raise review.ReviewRequired('fill_regressed',before[3],status)
        parsed[role]=(bid,str(qty),str(filled),status,str(price))
    if set(parsed)!={'take_profit','stop_loss'}:raise ValueError('Incomplete bracket pair')
    if sum(number(r[2]) for r in parsed.values())>parent_filled:raise ValueError('Exit fills exceed entry fills')
    # Validate the entire graph before persisting either leg.
    now=datetime.now(ZoneInfo('Asia/Seoul')).isoformat()
    for role,(bid,qty,filled,status,price) in parsed.items():
        before=old.get(role)
        if not before or before!=(bid,qty,filled,status):
            db.execute('INSERT INTO paper_events(client_id,kind,status,filled,checked_at) VALUES (?,?,?,?,?)',(cid+'/'+role,role,status,filled,now))
        db.execute('INSERT OR REPLACE INTO paper_legs VALUES (?,?,?,?,?,?,?,?,?)',(cid,role,bid,payload['symbol'],qty,filled,status,price,now))

def inventory(db,positions,legacy=0):
    expected={};verified=True
    for cid,raw,status,filled,outcome in db.execute('''SELECT r.client_id,r.payload,c.status,c.filled,c.outcome FROM paper_requests r LEFT JOIN paper_checks c ON r.client_id=c.client_id'''):
        p=json.loads(raw);symbol=p['symbol']
        if outcome!='confirmed':verified=False;continue
        exits=sum(number(r[0]) for r in db.execute('SELECT filled FROM paper_legs WHERE parent=?',(cid,)))
        remaining=number(filled)-exits
        if remaining<0:verified=False
        expected[symbol]=expected.get(symbol,Decimal(0))+remaining
    actual={}
    for p in positions:
        symbol=p['symbol']
        if symbol in actual:raise ValueError('Duplicate position symbol')
        n=Decimal(str(p['qty']))
        if not n.is_finite():raise ValueError('Invalid position quantity')
        actual[symbol]=n
    rows=[{'symbol':s,'expected':str(q),'actual':str(actual.get(s,Decimal(0))),'matched':q==actual.get(s,Decimal(0))} for s,q in sorted(expected.items())]
    for row in rows:
        target='position:'+row['symbol']
        if row['matched']:review.resolve_transient(db,target)
        else:review.note(db,target,'position_mismatch',row['expected'],row['actual'])
    review_blocked=review.blocking(db)
    ready=verified and not legacy and all(r['matched'] for r in rows) and not review_blocked
    result={'ready':ready,'rows':rows,'scope':'verified_bot_symbols','legacy_unverified':legacy,
            'reason':'일치' if ready else ('주문 기록 미확인' if not verified or legacy else ('보유 수량 불일치' if any(not r['matched'] for r in rows) else '수동 검토 필요')),
            'checked_at':datetime.now(timezone.utc).isoformat()}
    db.execute("INSERT OR REPLACE INTO paper_meta VALUES ('inventory_gate',?)",(json.dumps(result),));db.commit()
    return result

def enforce_entry(db,positions):
    if review.blocking(db):raise RuntimeError('Active review cases block entry')
    row=db.execute("SELECT value FROM paper_meta WHERE key='inventory_gate'").fetchone()
    if not row:return # No historical managed orders before the first entry.
    gate=json.loads(row[0])
    if not gate.get('ready'):raise RuntimeError('Inventory reconciliation required before entry')
    actual={p['symbol']:Decimal(str(p['qty'])) for p in positions}
    if any(not n.is_finite() for n in actual.values()):raise ValueError('Invalid holdings')
    if any(Decimal(r['expected'])!=actual.get(r['symbol'],Decimal(0)) for r in gate['rows']):raise RuntimeError('Holdings changed after reconciliation')

def leg_history(db):
    return [{'client_id':cid+'/'+role,'symbol':symbol,'qty':qty,'filled_qty':filled,
             'remaining_qty':str(number(qty)-number(filled)),
             'status':('익절 · ' if role=='take_profit' else '손절 · ')+ORDER_STATES.get(status,'미확인'),
             'checked_at':checked} for cid,role,symbol,qty,filled,status,checked in db.execute('SELECT parent,role,symbol,qty,filled,status,checked_at FROM paper_legs ORDER BY checked_at DESC LIMIT 200')]
