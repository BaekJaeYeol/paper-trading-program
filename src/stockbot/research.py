"""Offline, fixed-candidate chronological comparison. Never promotes settings."""
import hashlib
import json
import math
from .core import backtest,size

def trend(history):
    if len(history)<60:return False
    closes=[b.close for b in history[-60:]]
    return closes[-1]>=sum(closes[-20:])/20>sum(closes)/60 and closes[-1]/history[-22].close-1>=-.10

def calm_trend(history):
    if not trend(history):return False
    ranges=[max(history[i].high-history[i].low,abs(history[i].high-history[i-1].close),abs(history[i].low-history[i-1].close)) for i in range(len(history)-14,len(history))]
    return sum(ranges)/14/history[-1].close<=.05

def candidates(config):
    return [('baseline',dict(config),None),('trend_guard',dict(config),trend),
            ('trend_volume_2',dict(config,volume_ratio=2.0),trend),
            ('trend_volume_4',dict(config,volume_ratio=4.0),trend),
            ('trend_volatility_guard',dict(config),calm_trend)]

def metrics(result):
    return {k:result[k] for k in ('total_return','max_drawdown','closed_trades','win_rate','profit_factor','estimated_costs','exposure_days','evaluation_days')}

def holding(bars,start,cash,fee,slippage,sell_tax,fraction):
    first=bars[start].open;entry=first*(1+slippage)
    qty=size(cash,cash,entry*(1+fee),fraction)
    remainder=cash-qty*entry*(1+fee);peak=cash;dd=0
    for i in range(start,len(bars)):
        value=remainder+qty*bars[i].close
        if i==len(bars)-1:value=remainder+qty*bars[i].close*(1-slippage)*(1-fee-sell_tax)
        if not math.isfinite(value):raise ValueError('Non-finite benchmark result')
        peak=max(peak,value);dd=max(dd,1-value/peak)
    return {'total_return':value/cash-1,'max_drawdown':dd,'allocation_fraction':fraction}

def compare(bars,config,*,cash=10000.,fee=.001,slippage=.001,sell_tax=0.):
    if not 300<=len(bars)<=5000:raise ValueError('Strategy research requires 300 to 5000 ordered daily bars')
    if any(a.day>=b.day for a,b in zip(bars,bars[1:])):raise ValueError('Unique ascending daily dates required')
    n=len(bars);train_end=n*3//5;validation_end=n*4//5
    boundaries=[('train',60,train_end),('validation',train_end,validation_end),('test',validation_end,n)]
    rows=[]
    for name,c,guard in candidates(config):
        row={'name':name,'volume_ratio':c['volume_ratio']}
        for label,start,end in boundaries:
            row[label]=metrics(backtest(bars[:end],c,cash,fee,slippage,sell_tax=sell_tax,entry_filter=guard,start_index=start,liquidate_end=True))
        rows.append(row)
    # Selection uses training results only. Validation/test never enter this key.
    eligible=[r for r in rows if r['train']['closed_trades']>=5]
    selected=max(eligible,key=lambda r:r['train']['total_return']-r['train']['max_drawdown']) if eligible else None
    evidence='insufficient_training_trades'
    if selected:
        evidence='research_only_unverified_market_data' if min(selected['validation']['closed_trades'],selected['test']['closed_trades'])>=3 else 'insufficient_holdout_trades'
    identity=hashlib.sha256(json.dumps([[str(b.day),b.open,b.high,b.low,b.close,b.volume] for b in bars],separators=(',',':')).encode()).hexdigest()
    benchmarks={}
    for label,start,end in boundaries:
        segment=bars[:end]
        benchmarks[label]={'cash_return':0.,'matched_allocation_hold':holding(segment,start,cash,fee,slippage,sell_tax,config['max_position_fraction']),
                           'full_allocation_hold':holding(segment,start,cash,fee,slippage,sell_tax,1.)}
    return {'schema':'strategy-research-v1','data_provenance':'unverified_csv','data_sha256':identity,'bars':n,
            'capital_price_units':cash,'cost_assumptions':{'fee_each_side':fee,'slippage_each_side':slippage,'sell_tax':sell_tax},
            'periods':{label:{'from':str(bars[start].day),'to':str(bars[end-1].day),'bars':end-start} for label,start,end in boundaries},
            'selection_rule':'training net return minus drawdown; minimum 5 closed trades; ties preserve candidate order',
            'selected_on_training':selected['name'] if selected else None,'evidence_status':evidence,
            'automatic_promotion':False,'rows':rows,'benchmarks':benchmarks,
            'limitations':['Single asset daily next-open approximation; not an intraday limit/bracket execution replica.',
                           'Each period starts flat with fresh capital and pays forced end-liquidation costs.',
                           'No data provenance, split/dividend adjustment, delisted-universe or tax correctness verified.',
                           'No real-market improvement established; selected candidate is never applied automatically.']}
