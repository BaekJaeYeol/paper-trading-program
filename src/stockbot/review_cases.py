"""Explicit review reasons. No order writes, corporate-action guesses or overrides."""
from datetime import datetime
from decimal import Decimal
import hashlib
import json
from zoneinfo import ZoneInfo

GUIDANCE={
 'order_replaced':('정정·교체 주문 확인 필요','증권사에서 이전/새 주문 ID·정정 시각·체결 내역을 대조하세요. 새 주문을 자동 추적하거나 승인하지 않습니다.'),
 'quantity_changed':('원래 주문 수량과 다름','주문 원문과 증권사 내역을 대조하세요. 수동 정정·기업행위 등 원인은 미확정이며 수량을 자동 보정하지 않습니다.'),
 'price_changed':('원래 주문 가격과 다름','지정가·손절가와 정정 이력을 확인하세요. 가격을 자동 수정하거나 재제출하지 않습니다.'),
 'identity_changed':('연결 주문 ID가 바뀜','부모·자식 주문과 이전/새 ID를 증권사에서 확인하세요. 다른 주문으로 임의 연결하지 않습니다.'),
 'fields_changed':('종목·방향·주문 조건 변경','원래 요청과 종목·방향·주문 유형·기간을 대조하세요. 지원하지 않는 변경은 별도 검토가 필요합니다.'),
 'fill_regressed':('누적 체결 또는 종료 상태 변경','체결 정정·취소·조회 지연 가능성을 증권사 체결 내역으로 확인하세요. 과거 체결을 임의로 덮어쓰지 않습니다.'),
 'position_mismatch':('보유 수량 불일치 · 원인 미확정','증권사 잔고·체결·기업행위 공지를 대조하세요. 수동 매매·분할·이체·조회 시점 차이를 수량만으로 확정하지 않습니다.'),
 'lookup_failed':('주문 조회 실패','네트워크·인증·API 상태를 확인하고 읽기 대조를 다시 실행하세요. 주문을 재전송하지 마세요.'),
 'missing':('주문 조회 결과 없음','미접수로 단정하지 말고 증권사에서 주문 키와 체결 내역을 확인하세요. 자동 재전송하지 않습니다.'),
 'mismatch':('주문 정보 미확인','증권사 원문과 저장된 주문을 확인하세요. 현재 정보로 주문 상태를 승인할 수 없습니다.'),
 'response_lost':('주문 응답 미확인','접수 여부를 읽기 대조로 먼저 확인하세요. 같은 주문을 다시 보내지 마세요.'),
}

class ReviewRequired(ValueError):
    def __init__(self,code,expected='—',observed='—'):
        self.code=code if code in GUIDANCE else 'mismatch'
        self.expected=expected;self.observed=observed
        super().__init__(self.code)

def display(value):
    # Only explicitly selected scalar evidence is accepted; never exception/response bodies.
    if isinstance(value,(str,int,Decimal)):
        return ''.join(ch for ch in str(value) if ch.isprintable())[:120]
    return '미확인'

RECOVERABLE={'price_changed','fields_changed'}

def version(row):
    return hashlib.sha256(json.dumps(list(row),ensure_ascii=False).encode()).hexdigest()

def initialize(db):
    db.execute('''CREATE TABLE IF NOT EXISTS paper_review_cases(
        target TEXT NOT NULL,code TEXT NOT NULL,expected TEXT NOT NULL,observed TEXT NOT NULL,
        first_seen TEXT NOT NULL,last_seen TEXT NOT NULL,occurrences INTEGER NOT NULL,
        active INTEGER NOT NULL,sticky INTEGER NOT NULL,PRIMARY KEY(target,code))''')
    db.execute('''CREATE TABLE IF NOT EXISTS paper_review_resolutions(
        seq INTEGER PRIMARY KEY AUTOINCREMENT,target TEXT NOT NULL,code TEXT NOT NULL,
        case_version TEXT NOT NULL,resolved_at TEXT NOT NULL,basis TEXT NOT NULL)''')

def note(db,target,code,expected='—',observed='—',sticky=False):
    code=code if code in GUIDANCE else 'mismatch';now=datetime.now(ZoneInfo('Asia/Seoul')).isoformat()
    old=db.execute('SELECT expected,observed,occurrences,active,sticky FROM paper_review_cases WHERE target=? AND code=?',(target,code)).fetchone()
    expected,observed=display(expected),display(observed)
    if old:
        occurrences=old[2]+(0 if old[0:2]==(expected,observed) and old[3] else 1)
        db.execute('UPDATE paper_review_cases SET expected=?,observed=?,last_seen=?,occurrences=?,active=1,sticky=? WHERE target=? AND code=?',(expected,observed,now,occurrences,int(sticky or old[4]),target,code))
    else:db.execute('INSERT INTO paper_review_cases VALUES (?,?,?,?,?,?,1,1,?)',(target,code,expected,observed,now,now,int(sticky)))

def resolve_transient(db,target):
    db.execute('UPDATE paper_review_cases SET active=0 WHERE target=? AND sticky=0',(target,))

def blocking(db):return db.execute('SELECT COUNT(*) FROM paper_review_cases WHERE active=1').fetchone()[0]

def snapshot(db):
    cases=[]
    for target,code,expected,observed,first,last,count,active,sticky in db.execute('SELECT * FROM paper_review_cases ORDER BY active DESC,last_seen DESC LIMIT 200'):
        title,action=GUIDANCE.get(code,GUIDANCE['mismatch'])
        cases.append({'target':target,'code':code,'title':title,'expected':expected,'observed':observed,'first_seen':first,'last_seen':last,'occurrences':count,'active':bool(active),'manual_review_required':bool(sticky),'next_action':action,'version':version((target,code,expected,observed,first,last,count,active,sticky)),'recovery_supported':bool(active and sticky and code in RECOVERABLE)})
    return {'cases':cases,'blocking':blocking(db),'scope':'read_only_guidance','override_available':False}


def resolve_verified(db,selection,data,*,stopped):
    """Called under cycle.lock after fresh full reconciliation. No broker/STOP writes."""
    if not stopped or data.get('can_trade') is not True:raise RuntimeError('Recovery requires STOP and active paper account')
    if data['reconciliation']['unresolved'] or data['reconciliation']['legacy'] or data['orders']:raise RuntimeError('Orders remain unverified or open')
    inv=data['inventory']
    if any(not r['matched'] or Decimal(r['expected'])!=0 or Decimal(r['actual'])!=0 for r in inv['rows']):raise RuntimeError('Managed holdings must be flat and matched')
    # All saved roots and children must be terminal; no bracket protection is bypassed.
    terminal={'filled','canceled','expired','rejected'}
    roots=db.execute('SELECT client_id,status,outcome FROM paper_checks').fetchall()
    if not roots or any(status not in terminal or outcome!='confirmed' for _,status,outcome in roots):raise RuntimeError('Root orders not closed')
    if any(status not in terminal for (status,) in db.execute('SELECT status FROM paper_legs')):raise RuntimeError('Child orders not closed')
    target,code,token=selection
    row=db.execute('SELECT * FROM paper_review_cases WHERE target=? AND code=?',(target,code)).fetchone()
    if not row or not row[7] or not row[8] or code not in RECOVERABLE or version(row)!=token:raise RuntimeError('Case changed or unsupported')
    if target not in {r[0] for r in roots}:raise RuntimeError('Unknown target')
    now=datetime.now(ZoneInfo('Asia/Seoul')).isoformat()
    db.execute('INSERT INTO paper_review_resolutions(target,code,case_version,resolved_at,basis) VALUES (?,?,?,?,?)',(target,code,token,now,'original_conditions_verified_closed_flat'))
    db.execute('UPDATE paper_review_cases SET active=0 WHERE target=? AND code=?',(target,code))
    check=db.execute('SELECT status,filled FROM paper_checks WHERE client_id=?',(target,)).fetchone()
    db.execute('INSERT INTO paper_events(client_id,kind,status,filled,checked_at) VALUES (?,?,?,?,?)',(target,'review_resolved',check[0],check[1],now))
    return {'resolved':True,'code':code,'automatic_resume':False,'stop_unchanged':True}
