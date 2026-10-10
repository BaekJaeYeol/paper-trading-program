"""15-minute regular-session simulated trading. Never sends broker orders."""
import argparse
import datetime as dt
import hashlib
import json
import math
import shutil
import statistics
import tempfile
import time
from pathlib import Path
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo
from data import symbol_name
from engine import evaluate
from paper import Paper
from comparison import report as comparison_report
from reliability import session_bounds, freshness, update_v2, dashboard

NY=ZoneInfo('America/New_York')
INTERVAL=900


def decode_bars(raw, symbol, now=None):
    now=time.time() if now is None else now
    result=raw.get('chart',{}).get('result')
    if not result:raise ValueError('15분봉 응답에 데이터가 없습니다')
    item=result[0];meta=item.get('meta',{})
    if meta.get('currency')!='USD' or meta.get('symbol')!=symbol or meta.get('exchangeTimezoneName')!='America/New_York':
        raise ValueError('종목·통화·거래소 시간대를 확인할 수 없습니다')
    quote=item['indicators']['quote'][0];rows=[]
    for i,t in enumerate(item.get('timestamp',[])):
        local=dt.datetime.fromtimestamp(t,NY)
        minute=local.hour*60+local.minute
        # Only complete regular-session bars; omit incomplete/current or partial close bars.
        bounds=session_bounds(local.date())
        if not bounds or t<bounds[0] or t+INTERVAL>bounds[1] or (t-bounds[0])%INTERVAL or t+INTERVAL>now:continue
        vals=[quote[k][i] for k in ('open','high','low','close','volume')]
        if any(v is None for v in vals):continue
        o,h,l,c,v=map(float,vals)
        if not all(math.isfinite(x) for x in (o,h,l,c,v)) or min(o,h,l,c)<=0 or v<0 or l>min(o,c) or h<max(o,c) or l>h:
            raise ValueError('Invalid 15-minute OHLCV')
        stamp=dt.datetime.fromtimestamp(t,dt.timezone.utc).isoformat()
        rows.append((stamp,o,h,l,c,v))
    if len(rows)<100:raise ValueError('완료된 정규장 15분봉이 최소 100개 필요합니다')
    if any(a[0]>=b[0] for a,b in zip(rows,rows[1:])):raise ValueError('15분봉 시각 중복/순서 오류')
    return rows


def download_bars(symbol, now=None):
    symbol=symbol_name(symbol)
    req=Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=60d&interval=15m&includePrePost=false',headers={'User-Agent':'Mozilla/5.0 InvestmentLab/0.2'})
    with urlopen(req,timeout=30) as response:raw=json.load(response)
    return decode_bars(raw,symbol,now)


def intraday_candidates(rows):
    closes=[r[4] for r in rows]
    sig={k:[] for k in ('trend_8_26','momentum_26','breakout_8','reversion_12','volume_26')}
    for i,c in enumerate(closes):
        if i<26:
            for s in sig.values():s.append(0.)
            continue
        mean=statistics.mean(closes[i-11:i+1]);sd=statistics.pstdev(closes[i-11:i+1])
        vol=statistics.mean(r[5] for r in rows[i-26:i])
        values=(statistics.mean(closes[i-7:i+1])>statistics.mean(closes[i-25:i+1]),
                c>closes[i-26],c>max(closes[i-8:i]),sd>0 and c<mean-sd,
                vol>0 and rows[i][5]>=vol*2 and c/closes[i-26]-1<=.01)
        for s,value in zip(sig.values(),values):s.append(float(value))
    out={'cash':[0.]*len(rows),'buy_hold':[1.]*len(rows),**sig}
    keys=list(sig)
    for i,x in enumerate(keys):
        for y in keys[i+1:]:
            out[x+' AND '+y]=[min(a,b) for a,b in zip(sig[x],sig[y])]
            out[x+' + '+y]=[(a+b)/2 for a,b in zip(sig[x],sig[y])]
    return out


def historical_report(rows):
    ss=intraday_candidates(rows);results=[]
    # Fixed candidates, exploratory chronological tests; no automatic winner selection.
    train=260;test=130
    for lo in range(27+train,len(rows)-test+1,test):
        for name,sig in ss.items():
            normal=evaluate(rows,sig,lo,lo+test,.002)
            doubled=evaluate(rows,sig,lo,lo+test,.004)
            # Daily Sharpe annualization would be misleading for intraday returns.
            normal.pop('sharpe_rf0');normal['bars']=normal.pop('days')
            results.append(dict(strategy=name,test_start=rows[lo][0],test_end=rows[lo+test-1][0],
                                double_cost_return=doubled['return'],**normal))
    return dict(interval='15m',source='Yahoo chart API',selection='none; fixed candidates; exploratory only',
                one_way_fee=.001,one_way_slippage=.001,results=results,live_ready=False)


def publish_directory(stage, destination):
    """Copy first, then swap with rollback; persisted git state is previous recovery point."""
    destination=Path(destination)
    pending=destination.with_name(destination.name+'.pending')
    backup=destination.with_name(destination.name+'.backup')
    if pending.exists():shutil.rmtree(pending)
    shutil.copytree(stage,pending)
    if backup.exists():raise ValueError('이전 계좌 백업 복구를 확인하세요')
    if destination.exists():destination.rename(backup)
    try:pending.rename(destination)
    except Exception:
        if backup.exists():backup.rename(destination)
        raise
    if backup.exists():shutil.rmtree(backup)


def tick(state, symbols=('SPY','QQQ','IWM','DIA'), downloader=download_bars, now=None):
    state=Path(state);state.mkdir(parents=True,exist_ok=True)
    old_status=json.loads((state/'status.json').read_text()) if (state/'status.json').exists() else {'symbols':{}}
    now=time.time() if now is None else now
    status=dict(checked_utc=dt.datetime.fromtimestamp(now,dt.timezone.utc).isoformat(),interval='15m',real_orders=False,symbols={})
    blocked=(state/'emergency-stop.json').exists()
    status['emergency_stop']=blocked
    for symbol in symbols:
        try:
            rows=downloader(symbol);ss=intraday_candidates(rows)
            now=dt.datetime.fromisoformat(status['checked_utc']).timestamp()
            health=freshness(rows,now)
            if health['stale']:raise ValueError('데이터 지연: 계좌 갱신 중단, 이전 기록 유지')
            with tempfile.TemporaryDirectory() as temp:
                stage=Path(temp)/symbol;previous=state/symbol
                if previous.exists():shutil.copytree(previous,stage)
                else:stage.mkdir()
                accounts={};new_bars=0;trades=0
                for name in ss:
                    key=hashlib.sha256(name.encode()).hexdigest()[:16]
                    paper=Paper(stage/'accounts'/(key+'.sqlite'),intraday_candidates)
                    old=paper.snapshot(full=True)
                    if not old['active']:snap=paper.start(rows,name,'real_download')
                    else:
                        # Missing regular bars inside a session cannot be filled retrospectively.
                        future=[r for r in rows if r[0]>=old['last_date']]
                        for a,b in zip(future,future[1:]):
                            ta=dt.datetime.fromisoformat(a[0]);tb=dt.datetime.fromisoformat(b[0])
                            if ta.astimezone(NY).date()==tb.astimezone(NY).date() and (tb-ta).total_seconds()!=INTERVAL:
                                raise ValueError('정규장 봉 누락: 계좌 갱신을 중단합니다')
                        snap=paper.advance(rows);snap=paper.snapshot(full=True)
                        new_bars=max(new_bars,sum(r[0]>old['last_date'] for r in rows))
                        trades+=sum(r[0]>old['last_date'] and r[2]!='hold' for r in snap['ledger'])
                    # Persist exact prior-bar signal and simulated fill details.
                    by_stamp={r[0]:i for i,r in enumerate(rows)}
                    events=[]
                    for stamp,signal,side,qty,price,fee,equity in snap['ledger']:
                        index=by_stamp.get(stamp)
                        signal_at=rows[index-1][0] if index is not None and index>0 else None
                        events.append(dict(fill_bar_start_utc=stamp,signal_bar_start_utc=signal_at,
                                           strategy=name,target_weight=signal,side=side,quantity=qty,
                                           simulated_fill_price=price,fee=fee,equity=equity,
                                           reason=f'{name}: prior completed bar target {signal:.0%}; next bar open simulation'))
                    accounts[name]={k:snap[k] for k in ('cash','qty','equity','last_date','config')}
                    accounts[name]['events']=events
                digest=hashlib.sha256(json.dumps(rows).encode()).hexdigest()
                if not (stage/'digest.txt').exists() or (stage/'digest.txt').read_text()!=digest:
                    (stage/'research.json').write_text(json.dumps(historical_report(rows),ensure_ascii=False,indent=2),encoding='utf-8')
                    (stage/'digest.txt').write_text(digest)
                (stage/'bars.json').write_text(json.dumps(rows),encoding='utf-8')
                (stage/'accounts.json').write_text(json.dumps(accounts,ensure_ascii=False,indent=2),encoding='utf-8')
                if not (stage/'comparison.json').exists() or (stage/'comparison-digest.txt').read_text()!=digest:
                    (stage/'comparison.json').write_text(json.dumps(comparison_report(rows,ss),ensure_ascii=False,indent=2),encoding='utf-8')
                    (stage/'comparison-digest.txt').write_text(digest)
                update_v2(stage,rows,ss,now,blocked)
                publish_directory(stage,previous)
                status['symbols'][symbol]=dict(status='ok',last_completed_bar_start_utc=rows[-1][0],
                                               accounts=len(accounts),new_bars=new_bars,new_trades=trades,
                                               last_success_utc=status['checked_utc'],health=health,
                                               detail='new accounts waiting for next completed bar' if not old['active'] else 'updated' if new_bars else '새 데이터 없음 / '+health['market'])
        except Exception as exc:status['symbols'][symbol]=dict(status='error',message=str(exc),last_success_utc=old_status['symbols'].get(symbol,{}).get('last_success_utc'))
    (state/'status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8')
    dashboard(state,status)
    print(json.dumps(status,ensure_ascii=False))
    return status

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--state',required=True);parser.add_argument('--halt',action='store_true');args=parser.parse_args()
    if args.halt:
        Path(args.state).mkdir(parents=True,exist_ok=True)
        (Path(args.state)/'emergency-stop.json').write_text(json.dumps({'halted':True,'reason':'user request','utc':dt.datetime.now(dt.timezone.utc).isoformat()}))
    result=tick(args.state)
    if any(r['status']=='error' for r in result['symbols'].values()):raise SystemExit(1)
