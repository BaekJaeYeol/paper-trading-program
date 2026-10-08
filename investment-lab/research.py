import hashlib, json, csv, shutil
from pathlib import Path
from engine import load, signals, evaluate

def candidates(rows):
    sig=signals(rows); out={'cash':[0.]*len(rows),'buy_hold':[1.]*len(rows),**sig}
    keys=list(sig)
    for j,x in enumerate(keys):
        for y in keys[j+1:]:
            out[x+' AND '+y]=[min(a,b) for a,b in zip(sig[x],sig[y])]
            out[x+' + '+y]=[(a+b)/2 for a,b in zip(sig[x],sig[y])]
    return out

def run(path,outdir,source,fee=.001,slippage=.001):
    rows=load(path); ss=candidates(rows); start=61; n=len(rows)-start;b=start+n//2;c=start+n*3//4
    cost=fee+slippage; results=[]
    for fold,lo,hi in [('development',start,b),('validation',b,c)]:
        for name,s in ss.items(): results.append({'fold':fold,'strategy':name,**evaluate(rows,s,lo,hi,cost)})
    choices=[r for r in results if r['fold']=='validation' and r['strategy'] not in ('cash','buy_hold') and r['turnover']>=4]
    selected=max(choices,key=lambda r:r['sharpe_rf0'])['strategy'] if choices else 'cash'
    for name in dict.fromkeys(['cash','buy_hold',selected]):
        m=evaluate(rows,ss[name],c,len(rows),cost)
        m2=evaluate(rows,ss[name],c,len(rows),2*cost)
        results.append({'fold':'holdout','strategy':name,**m})
        results.append({'fold':'holdout_double_cost','strategy':name,**m2})
    summary={'source':source,'data_sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'first_date':rows[0][0],'last_date':rows[-1][0],
        'selected':selected,'fee':fee,'slippage':slippage,'selection':'validation Sharpe with turnover >=4; no holdout selection',
        'holdout_start':rows[c][0],'status':'백테스트 완료' if source=='real_download' else 'CSV 검증 완료 (출처 미확인)' if source=='imported_csv' else '과거 공개 표본 검증' if source=='historical_github_sample' else '합성 데모',
        'live_ready':False,'results':results}
    outdir=Path(outdir);outdir.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(path,outdir/'input_snapshot.csv')
    with (outdir/'metrics.csv').open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
    (outdir/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    return summary
