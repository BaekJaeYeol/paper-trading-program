"""Read-only, bounded Alpaca daily-history research. No account/order/state writes."""
from datetime import date,datetime,timedelta
import re
import time
from zoneinfo import ZoneInfo
from .core import Bar
from .research import compare

NY=ZoneInfo('America/New_York')
class HistoricalDataError(RuntimeError):pass

def symbol_value(value):
    if not isinstance(value,str) or not re.fullmatch(r'[A-Z][A-Z0-9.]{0,9}',value):raise ValueError('Invalid US symbol')
    return value

def aware(value):
    if not isinstance(value,str):raise HistoricalDataError('Missing market timestamp')
    try:dt=datetime.fromisoformat(value.replace('Z','+00:00'))
    except ValueError:raise HistoricalDataError('Invalid market timestamp') from None
    if dt.tzinfo is None:raise HistoricalDataError('Timezone required')
    return dt

def fetch_compare(broker,symbol,config,*,cancel=None,cash=10000.,fee=.001,slippage=.001,sell_tax=0.):
    symbol=symbol_value(symbol);started=time.monotonic()
    def check():
        if cancel is not None and cancel.is_set():raise HistoricalDataError('Historical research cancelled')
        if time.monotonic()-started>=60:raise HistoricalDataError('Historical research time limit exceeded')
    def get(path,params=None,*,data=False):
        check()
        try:result=broker.request(path,params,data=data) if data else broker.request(path,params)
        except Exception:raise HistoricalDataError('Historical GET failed; check paper keys, feed access and network') from None
        check();return result
    clock=get('/v2/clock')
    if not isinstance(clock,dict):raise HistoricalDataError('Invalid market clock')
    now=aware(clock.get('timestamp')).astimezone(NY)
    end=now.date()-timedelta(days=1);start=end-timedelta(days=1096)
    calendar=get('/v2/calendar',{'start':start.isoformat(),'end':end.isoformat()})
    if not isinstance(calendar,list) or not calendar or len(calendar)>5000:raise HistoricalDataError('Invalid market calendar')
    try:sessions=[date.fromisoformat(row['date']) for row in calendar]
    except (KeyError,TypeError,ValueError):raise HistoricalDataError('Invalid calendar dates') from None
    if any(not start<=d<=end for d in sessions) or any(a>=b for a,b in zip(sessions,sessions[1:])):raise HistoricalDataError('Calendar must be unique, ascending and in range')
    last=sessions[-1];bars=[];token=None;seen=set();excluded=0;pages=0
    for _ in range(10):
        params={'timeframe':'1Day','start':start.isoformat(),'end':(last+timedelta(days=1)).isoformat(),'feed':'iex','adjustment':'split','limit':1000,'sort':'asc'}
        if token is not None:params['page_token']=token
        page=get(f'/v2/stocks/{symbol}/bars',params,data=True);pages+=1
        if not isinstance(page,dict) or page.get('symbol',symbol)!=symbol or not isinstance(page.get('bars'),list):raise HistoricalDataError('Invalid historical page')
        for row in page['bars']:
            try:
                day=aware(row['t']).astimezone(NY).date()
                if not start<=day<=last:excluded+=1;continue
                bar=Bar(day,*(float(row[k]) for k in ('o','h','l','c','v')))
            except (KeyError,TypeError,ValueError,OverflowError):raise HistoricalDataError('Invalid daily OHLCV') from None
            if bars and bar.day<=bars[-1].day:raise HistoricalDataError('Duplicate or unsorted daily history')
            bars.append(bar)
            if len(bars)>5000:raise HistoricalDataError('Too many daily bars')
        token=page.get('next_page_token')
        if token is None or token=='':break
        if not isinstance(token,str) or len(token)>2048 or token in seen:raise HistoricalDataError('Invalid or repeated page token')
        seen.add(token)
    else:raise HistoricalDataError('Historical page limit exceeded')
    if len(bars)<300 or bars[-1].day!=last:raise HistoricalDataError('At least 300 bars through the last completed session required')
    expected=[d for d in sessions if d>=bars[0].day]
    if [b.day for b in bars]!=expected:raise HistoricalDataError('Historical coverage has missing or non-session dates')
    check()
    report=compare(bars,config,cash=cash,fee=fee,slippage=slippage,sell_tax=sell_tax)
    check()
    report['data_provenance']='alpaca_iex_split_only'
    report['source_data']={'provider':'Alpaca','symbol':symbol,'feed':'iex','adjustment':'split','dividends_included':False,
        'requested_from':start.isoformat(),'actual_from':str(bars[0].day),'last_completed_session':str(last),
        'pages':pages,'excluded_out_of_range':excluded,'calendar_coverage_checked':True,'read_only':True}
    return report
