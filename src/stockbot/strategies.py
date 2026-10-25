"""Shared past-only entry filters. Paper experiments, not proven return improvements."""
LABELS={'baseline':'기존 거래량 신호','trend_guard':'추세·급락 제한','trend_volatility_guard':'추세·변동성 제한'}

def decision(history,strategy):
    if strategy not in LABELS:raise ValueError('Unknown entry strategy')
    result={'strategy':strategy,'allowed':True,'reason':'baseline'}
    if strategy=='baseline':return result
    if len(history)<60:return dict(result,allowed=False,reason='insufficient_history')
    if any(a.day>=b.day for a,b in zip(history,history[1:])):raise ValueError('Unsorted strategy history')
    closes=[b.close for b in history[-60:]];ma20=sum(closes[-20:])/20;ma60=sum(closes)/60
    ret=closes[-1]/history[-22].close-1
    result.update(sma20=ma20,sma60=ma60,return_21d=ret,reason='trend_passed')
    if ret<-.10:return dict(result,allowed=False,reason='sharp_decline')
    if not closes[-1]>=ma20>ma60:return dict(result,allowed=False,reason='trend_not_met')
    if strategy=='trend_volatility_guard':
        tr=[max(history[i].high-history[i].low,abs(history[i].high-history[i-1].close),abs(history[i].low-history[i-1].close)) for i in range(len(history)-14,len(history))]
        ratio=sum(tr)/14/closes[-1];result['atr_fraction']=ratio
        if ratio>.05:return dict(result,allowed=False,reason='volatility_high')
    return result

def trend(history):return decision(history,'trend_guard')['allowed']
def calm_trend(history):return decision(history,'trend_volatility_guard')['allowed']
def configured_filter(config):
    strategy=config.get('entry_strategy','baseline')
    if strategy not in LABELS:raise ValueError('Unknown entry strategy')
    return {'baseline':None,'trend_guard':trend,'trend_volatility_guard':calm_trend}[strategy]
