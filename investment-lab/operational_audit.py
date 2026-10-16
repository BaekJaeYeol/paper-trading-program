"""Validate saved paper state and retain a bounded operational audit."""
import math
import json
from pathlib import Path
from state_recovery import atomic_json

def validate_account(account):
    for key in ('cash','qty','mark','equity','initial'):
        value=account.get(key)
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:
            raise ValueError('계좌 무결성 오류: '+key)
    if account['initial']<=0 or account['mark']<=0:
        raise ValueError('계좌 무결성 오류: 초기 자금·가격')
    expected=account['cash']+account['qty']*account['mark']
    if not math.isclose(expected,account['equity'],rel_tol=1e-9,abs_tol=.01):
        raise ValueError('계좌 무결성 오류: 현금·보유 수량·평가액 불일치')
    for key in ('fee','slippage','half_spread','participation'):
        value=account.get(key)
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or not 0<=value<=1:
            raise ValueError('계좌 무결성 오류: '+key)
    risk=account.get('risk',{})
    if risk:
        if not isinstance(risk.get('halted'),bool):
            raise ValueError('계좌 무결성 오류: 중단 상태')
        for key in ('peak','day_equity'):
            value=risk.get(key)
            if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<=0:
                raise ValueError('계좌 무결성 오류: '+key)
        for key in ('daily_limit','drawdown_limit'):
            value=risk.get(key)
            if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or not 0<value<1:
                raise ValueError('계좌 무결성 오류: '+key)

def record_run(state,status,previous,duration):
    for symbol,info in status['symbols'].items():
        old=previous.get('symbols',{}).get(symbol,{})
        info['consecutive_errors']=(old.get('consecutive_errors',0)+1) if info['status']=='error' else 0
        info['recovered']=info['status']=='ok' and old.get('status')=='error'
    entry={'checked_utc':status['checked_utc'],'duration_seconds':round(duration,2),
           'symbols':{symbol:{key:info.get(key) for key in ('status','message','consecutive_errors','recovered','new_bars','new_trades')} for symbol,info in status['symbols'].items()}}
    path=Path(state)/'operations-history.json'
    history=json.loads(path.read_text(encoding='utf-8')) if path.exists() else []
    # Same run timestamp replaces its entry rather than duplicating it.
    history=[item for item in history if item['checked_utc']!=entry['checked_utc']]
    history.append(entry)
    atomic_json(path,history[-200:])
    status['duration_seconds']=entry['duration_seconds']

def cadence_summary(history,checked_utc,session_bounds):
    """Audit recorded polls, not broker fills; allow two minutes of runner jitter."""
    import datetime as dt
    from zoneinfo import ZoneInfo
    now=dt.datetime.fromisoformat(checked_utc).timestamp()
    day=dt.datetime.fromtimestamp(now,ZoneInfo('America/New_York')).date()
    for offset in range(14):
        bounds=session_bounds(day-dt.timedelta(days=offset))
        if bounds and bounds[0]<=now:
            break
    else:
        return {'summary':'주기 검증: 최근 거래일을 확인할 수 없습니다'}
    opening,closing=bounds
    stamps=sorted({dt.datetime.fromisoformat(item['checked_utc']).timestamp() for item in history})
    expected=list(range(int(opening)+1320,int(closing)+421,900))
    due=[slot for slot in expected if slot+120<=now]
    missing=[dt.datetime.fromtimestamp(slot,dt.timezone.utc).isoformat()
             for slot in due if not any(slot<=stamp<=slot+120 for stamp in stamps)]
    first=next((stamp for stamp in stamps if opening<=stamp<=closing+1800),None)
    summary=f"완료 봉 확인 주기: 기록 {len(due)-len(missing)}/{len(due)}회 · 기록 없는 예정 {len(missing)}회 · 아직 판정 전 {len(expected)-len(due)}회"
    if missing:
        summary+=' · 주의: 예약 시작 지연 또는 실행·저장 누락을 확인하세요.'
    return {'session_date':str(dt.datetime.fromtimestamp(opening,dt.timezone.utc).date()),
            'due_slots':len(due),'recorded_slots':len(due)-len(missing),
            'missing_slots_utc':missing,'pending_slots':len(expected)-len(due),
            'first_record_utc':dt.datetime.fromtimestamp(first,dt.timezone.utc).isoformat() if first is not None else None,
            'summary':summary,
            'note':'각 정규장 완료 봉의 종료 7분 후를 목표로 2분 이내 실행 기록을 검사합니다. 기록 존재는 종목 성공·체결을 보장하지 않습니다. 최근 200회 이력 기준이며 예약 지연을 방지하는 기능은 아닙니다.'}
