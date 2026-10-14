"""Validate saved paper state and retain a bounded operational audit."""
import math
import json
from pathlib import Path

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
    temporary=path.with_suffix('.tmp')
    temporary.write_text(json.dumps(history[-200:],ensure_ascii=False,indent=2),encoding='utf-8')
    temporary.replace(path)
    status['duration_seconds']=entry['duration_seconds']
