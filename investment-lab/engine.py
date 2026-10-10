"""Daily, long-only research harness. Signals at close, fills at next open."""
import argparse, csv, json, math, statistics
from datetime import date
from pathlib import Path

def load(path):
    rows=[]
    with open(path, encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            date.fromisoformat(r['date'])
            rows.append((r['date'],*[float(r[k]) for k in ('open','high','low','close','volume')]))
    if len(rows)<252: raise ValueError('At least 252 daily rows required')
    if any(a[0]>=b[0] for a,b in zip(rows,rows[1:])): raise ValueError('Dates must be unique and ascending')
    for _,o,h,l,c,v in rows:
        if not all(math.isfinite(x) for x in (o,h,l,c,v)) or min(o,h,l,c)<=0 or v<0 or l>min(o,c) or h<max(o,c) or l>h:
            raise ValueError('Invalid OHLCV')
    return rows

def signals(rows):
    close=[r[4] for r in rows]; out={k:[] for k in ('trend','momentum','breakout','reversion','volume_filter')}
    for i,c in enumerate(close):
        if i<60:
            for x in out.values(): x.append(0.)
            continue
        mean20=statistics.mean(close[i-19:i+1]); sd=statistics.pstdev(close[i-19:i+1])
        avgvol=statistics.mean(r[5] for r in rows[i-30:i])
        values=(mean20>statistics.mean(close[i-59:i+1]),c>close[i-60],c>max(close[i-20:i]),sd>0 and c<mean20-sd,
                avgvol>0 and rows[i][5]/avgvol>=3 and c/close[i-21]-1<=.03)
        for k,v in zip(out,values): out[k].append(float(v))
    return out

def evaluate(rows,s,start,end,cost):
    # Each fold starts flat. Prior-close target rebalanced at today's open.
    equity=peak=1.; dd=turnover=0.; weight=0.; returns=[]
    for i in range(start,end):
        old=equity
        overnight=rows[i][1]/rows[i-1][4]-1
        equity*=1+weight*overnight
        weight=weight*(1+overnight)/(1+weight*overnight)
        target=s[i-1]; change=abs(target-weight)
        equity*=1-change*cost; turnover+=change
        dayret=rows[i][4]/rows[i][1]-1
        equity*=1+target*dayret
        weight=target*(1+dayret)/(1+target*dayret)
        if i==end-1:
            equity*=1-weight*cost; turnover+=weight; weight=0.
        returns.append(equity/old-1); peak=max(peak,equity); dd=max(dd,1-equity/peak)
    sd=statistics.stdev(returns) if len(returns)>1 else 0
    return {'return':equity-1,'max_drawdown':dd,'sharpe_rf0':statistics.mean(returns)/sd*math.sqrt(252) if sd else 0,
            'turnover':turnover,'days':len(returns)}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--csv',required=True); p.add_argument('--out',default='results'); p.add_argument('--fee',type=float,default=.001); p.add_argument('--slippage',type=float,default=.001); a=p.parse_args()
    if min(a.fee,a.slippage)<0 or not math.isfinite(a.fee+a.slippage) or a.fee+a.slippage>=.1: p.error('Invalid costs')
    rows=load(a.csv); sig=signals(rows); start=61; usable=len(rows)-start; b=start+usable//2; c=start+usable*3//4
    folds={'development':(start,b),'validation':(b,c),'holdout':(c,len(rows))}; costs=a.fee+a.slippage
    candidates={'cash':[0.]*len(rows),'buy_hold':[1.]*len(rows),**sig}
    # Candidate pairs predefined, not mined from holdout. AND and equal capital sleeves.
    keys=list(sig)
    for j,x in enumerate(keys):
        for y in keys[j+1:]:
            candidates[x+' AND '+y]=[min(u,v) for u,v in zip(sig[x],sig[y])]
            candidates[x+' + '+y]=[(u+v)/2 for u,v in zip(sig[x],sig[y])]
    validation={k:evaluate(rows,s,b,c,costs) for k,s in candidates.items()}
    eligible=[k for k in candidates if k not in ('cash','buy_hold') and validation[k]['turnover']>0]
    selected=max(eligible,key=lambda k:validation[k]['sharpe_rf0']) if eligible else 'cash'
    results=[]
    for fold,(lo,hi) in folds.items():
        names=candidates if fold!='holdout' else ['cash','buy_hold',selected]
        for k in names:
            results.append({'fold':fold,'strategy':k,**evaluate(rows,candidates[k],lo,hi,costs)})
    out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
    with (out/'metrics.csv').open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=list(results[0])); w.writeheader(); w.writerows(results)
    report={'input':str(Path(a.csv).resolve()),'selection_rule':'validation Sharpe, nonzero turnover; fixed candidate set','selected':selected,
            'one_way_cost':costs,'fold_dates':{k:[rows[l][0],rows[h-1][0]] for k,(l,h) in folds.items()},'holdout':[r for r in results if r['fold']=='holdout'],
            'limitations':['single asset','fractional exposure','no dividends unless reflected in consistently adjusted OHLC','no liquidity or partial fills','no statistical significance claim','repeated holdout reuse invalidates final test']}
    (out/'summary.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
