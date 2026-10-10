"""Calendar checks, isolated v2 paper fills and a readable operational report."""
import datetime as dt
import json
from pathlib import Path
import exchange_calendars as xcals

UTC=dt.timezone.utc
CAL=xcals.get_calendar('XNYS')

def session_bounds(day):
    label=str(day)
    if not CAL.is_session(label):return None
    return CAL.session_open(label).timestamp(),CAL.session_close(label).timestamp()

def freshness(rows,now):
    expected=None;opened=False
    day=dt.datetime.fromtimestamp(now,UTC).date()
    for offset in range(15):
        bounds=session_bounds(day-dt.timedelta(days=offset))
        if not bounds:continue
        start,end=bounds
        opened=opened or start<=now<end
        count=int((min(now,end)-start)//900)
        if count>0:
            expected=start+(count-1)*900;break
    last=dt.datetime.fromisoformat(rows[-1][0]).timestamp()
    # Allow 20 minutes publication delay after the expected bar has completed.
    stale=expected is not None and last<expected and now>=expected+900+1200
    return dict(market='장중' if opened else '장 마감·휴장',data='데이터 지연' if stale else '최신 완료 봉 확인',
                stale=stale,expected_bar_utc=dt.datetime.fromtimestamp(expected,UTC).isoformat() if expected else None)

def next_schedule(now):
    t=dt.datetime.fromtimestamp(now,UTC).replace(second=0,microsecond=0)+dt.timedelta(minutes=1)
    for _ in range(4*24*60):
        if t.weekday()<5 and t.minute in (7,22,37,52):return t.isoformat()
        t+=dt.timedelta(minutes=1)

def advance_v2(account,rows,signals,now,blocked=False):
    """One-bar IOC proxy: prior volume cap; remainder expires, never a real order."""
    if account is None:
        return dict(cash=10000.,qty=0.,equity=10000.,initial=10000.,last_date=rows[-1][0],mark=rows[-1][4],
                    model='v2-prior-volume-IOC',events=[],fee=.001,slippage=.001,half_spread=.0001,participation=.01)
    account=json.loads(json.dumps(account))
    anchor=next((i for i,r in enumerate(rows) if r[0]==account['last_date']),None)
    if anchor is None or abs(rows[anchor][4]-account['mark'])>1e-6:
        raise ValueError('v2 기준 봉 누락 또는 가격 수정: 계좌 보존')
    for i in range(anchor+1,len(rows)):
        stamp,o,h,l,c,v=rows[i];prior=rows[i-1]
        ta=dt.datetime.fromisoformat(prior[0]);tb=dt.datetime.fromisoformat(stamp)
        if ta.date()==tb.date() and (tb-ta).total_seconds()!=900:raise ValueError('v2 봉 누락')
        target=float(signals[i-1]);cash=account['cash'];qty=account['qty']
        risk=account.setdefault('risk',dict(halted=False,reason='',peak=account['equity'],day=None,day_equity=account['equity'],daily_limit=.03,drawdown_limit=.10))
        day=tb.astimezone(__import__('zoneinfo').ZoneInfo('America/New_York')).date().isoformat()
        if risk['day']!=day:risk.update(day=day,day_equity=account['equity'])
        marked=cash+qty*o;risk['peak']=max(risk['peak'],marked)
        if marked<=risk['day_equity']*(1-risk['daily_limit']) or marked<=risk['peak']*(1-risk['drawdown_limit']):risk.update(halted=True,reason='손실 한도')
        if blocked:risk.update(halted=True,reason='사용자 비상 중단')
        wanted=0. if risk['halted'] else (cash+qty*o)*target/o-qty
        side='buy' if wanted>1e-8 else 'sell' if wanted< -1e-8 else 'hold'
        adjustment=account['slippage']+account['half_spread']
        price=o*(1+adjustment if side=='buy' else 1-adjustment if side=='sell' else 1)
        requested=abs(wanted);cap=prior[5]*account['participation']
        quantity=min(requested,cap,cash/(price*(1+account['fee'])) if side=='buy' else qty if side=='sell' else 0.)
        fee=quantity*price*account['fee']
        if side=='buy':cash-=quantity*price+fee;qty+=quantity
        elif side=='sell':cash+=quantity*price-fee;qty-=quantity
        remaining=max(0.,requested-quantity)
        status='hold' if side=='hold' else 'unfilled' if quantity<=1e-8 else 'partial' if remaining>1e-8 else 'filled'
        account.update(cash=max(0.,cash),qty=max(0.,qty),mark=c,equity=cash+qty*c,last_date=stamp)
        risk['peak']=max(risk['peak'],account['equity'])
        if account['equity']<=risk['day_equity']*(1-risk['daily_limit']) or account['equity']<=risk['peak']*(1-risk['drawdown_limit']):risk.update(halted=True,reason='손실 한도')
        account['events'].append(dict(bar=stamp,signal_bar=prior[0],side=side,status=status,requested=requested,
            quantity=quantity,remaining=remaining,remainder_expired=remaining>1e-8,price=price,fee=fee,target=target,
            risk_halted=risk['halted'],risk_reason=risk['reason'],reason=f'직전 완료 봉 목표 비중 {target:.0%}; 다음 봉 시가 가정',
            recorded_utc=dt.datetime.fromtimestamp(now,UTC).isoformat(),
            booking_delay_seconds=max(0.,now-tb.timestamp()),retrospective=True,
            capacity_source='직전 봉 거래량의 1%; 실제 호가·체결 보장 없음'))
    return account

def update_v2(stage,rows,signals,now,blocked=False):
    path=Path(stage)/'accounts-v2.json'
    old=json.loads(path.read_text()) if path.exists() else {}
    result={name:advance_v2(old.get(name),rows,sig,now,blocked) for name,sig in signals.items()}
    if blocked:
        for account in result.values():
            risk=account.setdefault('risk',dict(peak=account['equity'],day=None,day_equity=account['equity'],daily_limit=.03,drawdown_limit=.10))
            risk.update(halted=True,reason='사용자 비상 중단')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')

def dashboard(state,status):
    lines=['# 모의투자 운영 현황','',f"최근 확인: {status['checked_utc']} (UTC)",
           f"다음 예약: {next_schedule(dt.datetime.fromisoformat(status['checked_utc']).timestamp())} (UTC, 실행 지연 가능)",'',
           '실제 주문 없음. v1 기존 계좌와 v2 새 계좌의 시작일이 다르므로 수익률을 직접 우열 비교하지 마세요.',
           'v2는 다음 봉 시가에 비용·스프레드·직전 거래량 제한을 적용한 가상 체결입니다. 미체결 잔량은 만료됩니다.','',
           '| 종목 | 상태 | 최근 성공 UTC | 마지막 완료 봉 UTC | 이번 새 봉 |',
           '|---|---|---|---|---|']
    for symbol,s in status['symbols'].items():
        lines.append(f"| {symbol} | {s.get('message',s.get('detail',''))} | {s.get('last_success_utc','-')} | {s.get('last_completed_bar_start_utc','-')} | {s.get('new_bars',0)} |")
    if status.get('emergency_stop'):lines+=['','**사용자 비상 중단 활성: v2 신규 매매 차단. 보유분 자동 청산 없음.**']
    lines+=['','[공정 비교·복구 검증 설명](https://github.com/BaekJaeYeol/paper-trading-program/blob/main/investment-lab/docs/comparison-orders.md)',
            '', 'v2 신규 주문 제한: 일중 손실 3%, 최고 평가액 대비 낙폭 10%. 중단은 지속되며 자동 청산하지 않습니다. v1은 원래 비교용 계좌로 유지합니다.']
    for symbol in status['symbols']:
        lines+=['',f'## {symbol} 계좌','', '| 모델 | 전략 | 평가액 USD | 손익 USD | 최근 매매·이유 |','|---|---|---:|---:|---|']
        for filename,model in [('accounts.json','v1'),('accounts-v2.json','v2')]:
            p=Path(state)/symbol/filename
            if not p.exists():continue
            for name,a in json.loads(p.read_text()).items():
                events=a.get('events',[])
                trade=next((e for e in (reversed(events) if model=='v2' else events) if e['side']!='hold'),{})
                risk=a.get('risk',{})
                detail=('중단: '+risk.get('reason','')+' / ') if risk.get('halted') else ''
                detail+=f"{trade.get('side','대기')} / {trade.get('status','')} / {trade.get('reason','새 신호 대기')}"
                lines.append(f"| {model} | {name} | {a['equity']:.2f} | {a['equity']-10000:.2f} | {detail} |")
        comparison=Path(state)/symbol/'comparison.json'
        if comparison.exists():
            lines+=['','### 같은 기간의 비용·노출 비교 (사후 연구)','', '| 전략 | 비용 전 | 비용 후 | 100% 보유 | 같은 평균 노출 보유 | 평균 노출 |','|---|---:|---:|---:|---:|---:|']
            for name,folds in json.loads(comparison.read_text())['results'].items():
                r=folds['holdout']
                lines.append(f"| {name} | {r['strategy_gross']['return_']:.2%} | {r['strategy_net']['return_']:.2%} | {r['buy_hold_net']['return_']:.2%} | {r['matched_buy_hold_net']['return_']:.2%} | {r['strategy_net']['average_exposure']:.2%} |")
            lines+=['','동일 구간·초기 자금, 종료 시 청산 비용 포함. 노출 맞춤은 사후 설명용이며 v2 실제 계좌 성과가 아닙니다.',f'[낙폭 분해·비용 영향·전체 구간]({symbol}/comparison.json)']
        lines+=['',f'[v1 전체 기록]({symbol}/accounts.json) · [v2 전체 기록]({symbol}/accounts-v2.json)']
    (Path(state)/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

    from dashboard_ui import render_dashboard
    render_dashboard(state, status, next_schedule(dt.datetime.fromisoformat(status['checked_utc']).timestamp()))
