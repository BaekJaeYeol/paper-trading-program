import csv, datetime as dt, hashlib, json, re
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from zoneinfo import ZoneInfo
from engine import load

def symbol_name(symbol):
    symbol=symbol.strip().upper()
    if not re.fullmatch(r'[A-Z][A-Z0-9.-]{0,14}',symbol): raise ValueError('종목 코드를 확인하세요. 예: SPY, AAPL')
    return symbol

def download(symbol, destination, years=5):
    symbol=symbol_name(symbol)
    url=f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={years}y&interval=1d'
    req=Request(url,headers={'User-Agent':'Mozilla/5.0 InvestmentLab/0.1'})
    try:
        with urlopen(req,timeout=25) as r: payload=json.load(r)
    except HTTPError as e: raise RuntimeError(f'시세 다운로드 HTTP {e.code}. 나중에 다시 시도하거나 CSV를 가져오세요.') from None
    except (URLError,TimeoutError): raise RuntimeError('시세 서버 연결 실패. CSV 가져오기를 사용할 수 있습니다.') from None
    result=payload.get('chart',{}).get('result')
    if not result: raise ValueError('시세 응답에 데이터가 없습니다')
    item=result[0]; quote=item['indicators']['quote'][0]
    # Yahoo OHLC split-adjusted; volume is provider convention. No dividend adjustment.
    today=dt.datetime.now(ZoneInfo('America/New_York')).date()
    records=[]
    for i,t in enumerate(item.get('timestamp',[])):
        day=dt.datetime.fromtimestamp(t,ZoneInfo('America/New_York')).date()
        if day>=today: continue # exclude current session even after close, conservative
        vals=[quote[k][i] for k in ('open','high','low','close','volume')]
        if any(v is None for v in vals): continue
        records.append([day.isoformat(),*vals])
    destination=Path(destination); destination.parent.mkdir(parents=True,exist_ok=True)
    temp=destination.with_suffix('.tmp')
    with temp.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['date','open','high','low','close','volume']);w.writerows(records)
    try: load(temp)
    except Exception:
        temp.unlink(missing_ok=True);raise
    temp.replace(destination)
    metadata={'source':'Yahoo chart API','symbol':symbol,'collected_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
              'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),'rows':len(records),
              'adjustment':'provider OHLC, split convention; dividend excluded','real_market_data':True}
    destination.with_suffix('.metadata.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    return destination
