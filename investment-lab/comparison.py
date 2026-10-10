"""Chronological, common-capital comparisons; matched exposure is retrospective."""
import math

def simulate(rows,signals,start,end,cost,initial_weight=None):
    cash=1.;qty=0.;peak=1.;drawdown=0.;exposure=[];turnover=0.
    for i in range(start,end):
        o,c=rows[i][1],rows[i][4];equity=cash+qty*o
        target=signals[i-1] if initial_weight is None else initial_weight
        if initial_weight is None or i==start:
            wanted=equity*target/o-qty
            if wanted>0:
                fill=min(wanted,cash/(o*(1+cost)));cash-=fill*o*(1+cost);qty+=fill
            else:
                fill=min(-wanted,qty);cash+=fill*o*(1-cost);qty-=fill
            turnover+=fill*o/equity
        exposure.append(qty*o/(cash+qty*o))
        equity=cash+qty*c;peak=max(peak,equity);drawdown=max(drawdown,1-equity/peak)
    equity=cash+qty*rows[end-1][4]*(1-cost)
    drawdown=max(drawdown,1-equity/peak)
    return dict(return_=equity-1,max_drawdown=drawdown,average_exposure=sum(exposure)/len(exposure),turnover=turnover)

def compare(rows,signals,start,end,cost=.0021):
    if not 1<=start<end<=len(rows) or len(signals)!=len(rows):raise ValueError('Invalid comparison range')
    if not math.isfinite(cost) or not 0<=cost<.1:raise ValueError('Invalid costs')
    if any(not math.isfinite(s) or not 0<=s<=1 for s in signals):raise ValueError('Invalid exposure')
    gross=simulate(rows,signals,start,end,0)
    net=simulate(rows,signals,start,end,cost)
    lo,hi=0.,1.
    # Match actual average invested fraction with a one-time buy and cash sleeve.
    for _ in range(35):
        mid=(lo+hi)/2
        if simulate(rows,signals,start,end,cost,mid)['average_exposure']<net['average_exposure']:lo=mid
        else:hi=mid
    allocation=(lo+hi)/2
    matched=simulate(rows,signals,start,end,cost,allocation)
    full=simulate(rows,signals,start,end,cost,1.)
    return dict(start=rows[start][0],end=rows[end-1][0],bars=end-start,one_way_cost=cost,
                strategy_gross=gross,strategy_net=net,buy_hold_net=full,matched_buy_hold_net=matched,
                matched_initial_allocation=allocation,cost_drag=gross['return_']-net['return_'],
                excess_over_matched=net['return_']-matched['return_'],
                drawdown_reduction_from_cash=full['max_drawdown']-matched['max_drawdown'],
                drawdown_reduction_beyond_cash=matched['max_drawdown']-net['max_drawdown'],
                limitation='사후 평균 노출을 맞춘 설명용 비교. 현금 이자 0, 소수점 매매, 시가 가정, 유동성 제한 없음. v2 실제 기록 성과와 다름.')

def report(rows,candidates):
    # Fixed candidates, no ranking/automatic selection; last quarter held out.
    start=27;split=start+(len(rows)-start)*3//4
    if split>=len(rows):raise ValueError('Not enough bars')
    return dict(model='common-capital-research-v1',selection='none',
                results={name:{'development':compare(rows,sig,start,split),'holdout':compare(rows,sig,split,len(rows))}
                         for name,sig in candidates.items()})
