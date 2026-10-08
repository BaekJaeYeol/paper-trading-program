"""Local next-open forward simulation, never sends broker orders."""
import json, sqlite3, math
from contextlib import contextmanager
from pathlib import Path
from research import candidates

class Paper:
    def __init__(self,path):
        self.path=Path(path);self.path.parent.mkdir(parents=True,exist_ok=True)
        with self.connect() as db:
            db.executescript('CREATE TABLE IF NOT EXISTS account(id INTEGER PRIMARY KEY CHECK(id=1),config TEXT,cash REAL,qty REAL,last_date TEXT,mark REAL); CREATE TABLE IF NOT EXISTS ledger(day TEXT PRIMARY KEY,signal REAL,side TEXT,qty REAL,price REAL,cost REAL,equity REAL);')
    @contextmanager
    def connect(self):
        db=sqlite3.connect(self.path,timeout=10)
        try:
            with db:
                yield db
        finally:
            db.close()
    def start(self,rows,strategy,source,fee=.001,slippage=.001,cash=10000):
        if strategy not in candidates(rows): raise ValueError('Unknown strategy')
        if source!='real_download': raise ValueError('모의 운영은 실제 다운로드 데이터에서만 시작할 수 있습니다')
        config={'strategy':strategy,'source':source,'fee':fee,'slippage':slippage,'started_after':rows[-1][0], 'reference':rows[-1][4]}
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            if db.execute('SELECT id FROM account').fetchone(): raise ValueError('기존 모의계좌가 있습니다. 별도 폴더에서 새 실험을 시작하세요.')
            db.execute('INSERT INTO account VALUES(1,?,?,?,?,?)',(json.dumps(config),cash,0.,rows[-1][0],rows[-1][4]))
        return self.snapshot()
    def enter_now(self,rows,quote,symbol):
        """Once per account: rebalance using last completed bar and a fresh quote."""
        from data import validate_quote
        from zoneinfo import ZoneInfo
        import datetime
        validate_quote(quote,symbol)
        day=datetime.datetime.fromtimestamp(quote['timestamp'],ZoneInfo('America/New_York')).date().isoformat()
        if (datetime.date.fromisoformat(day)-datetime.date.fromisoformat(rows[-1][0])).days>7:raise ValueError('신호용 일봉이 7일 이상 오래됐습니다. 실제 데이터를 다시 수집하세요.')
        if rows[-1][0]>=day:raise ValueError('완료 일봉과 현재 가격의 날짜 순서를 확인하세요')
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            raw=db.execute('SELECT config,cash,qty,last_date,mark FROM account').fetchone()
            if not raw:raise ValueError('먼저 계좌를 시작하세요')
            config,cash,qty,last,mark=raw;config=json.loads(config)
            if config.get('instant_entry_done'):return self.snapshot()
            if last!=rows[-1][0] or abs(rows[-1][4]/mark-1)>1e-6:raise ValueError('계좌 기준 일봉이 다릅니다. 먼저 기존 계좌 갱신이 필요합니다.')
            target=candidates(rows)[config['strategy']][-1];price=quote['price'];equity=cash+qty*price
            delta=equity*target/price-qty;cost=0.;side='hold'
            if delta>1e-8:
                price*=1+config['slippage'];delta=min(delta,cash/(price*(1+config['fee'])))
                cost=delta*price*config['fee'];cash-=delta*price+cost;qty+=delta;side='buy'
            elif delta< -1e-8:
                price*=1-config['slippage'];delta=-min(-delta,qty)
                cost=-delta*price*config['fee'];cash+=-delta*price-cost;qty+=delta;side='sell'
            else:delta=0.
            config.update(instant_entry_done=True,instant_day=day,instant_pending=True,instant_anchor=mark,instant_quote=quote,instant_signal_date=rows[-1][0],instant_signal=target,instant_side=side)
            db.execute('INSERT INTO ledger VALUES(?,?,?,?,?,?,?)',(day,target,side,abs(delta),price,cost,cash+qty*quote['price']))
            db.execute('UPDATE account SET config=?,cash=?,qty=?,mark=? WHERE id=1',(json.dumps(config),max(cash,0),max(qty,0),quote['price']))
        return self.snapshot()
    def advance(self,rows,stopped=False):
        if stopped: return self.snapshot()
        ss=candidates(rows)
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            account=db.execute('SELECT config,cash,qty,last_date,mark FROM account').fetchone()
            if not account: raise ValueError('먼저 모의계좌를 시작하세요')
            config,cash,qty,last,mark=account;config=json.loads(config)
            # refuse missing anchor, changed split scale, or conflicting historical revisions
            anchor=next((r for r in rows if r[0]==last),None)
            if not anchor or abs(anchor[4]/(config['instant_anchor'] if config.get('instant_pending') else mark)-1)>1e-6: raise ValueError('기준 일봉이 변경되었습니다. 분할/데이터 수정 확인이 필요합니다')
            for i,r in enumerate(rows):
                if r[0]<=last: continue
                if config.get('instant_pending') and r[0]<=config['instant_day']:
                    if r[0]==config['instant_day']:
                        last=r[0];mark=r[4];config['instant_pending']=False
                        db.execute('UPDATE ledger SET equity=? WHERE day=?',(cash+qty*mark,last))
                    continue
                if config.get('instant_pending'):
                    raise ValueError('즉시 체결일 일봉이 누락되었습니다. 계좌 처리를 중단합니다.')
                if i==0: raise ValueError('Missing prior bar')
                target=ss[config['strategy']][i-1]; equity=cash+qty*r[1]
                # Solve buy cash including fee; no shorts or leverage.
                buyprice=r[1]*(1+config['slippage']);sellprice=r[1]*(1-config['slippage'])
                targetqty=equity*target/r[1]
                delta=targetqty-qty;side='hold';cost=0.;price=r[1]
                if delta>1e-8:
                    delta=min(delta,cash/(buyprice*(1+config['fee'])));price=buyprice;side='buy';cost=delta*price*config['fee'];cash-=delta*price+cost;qty+=delta
                elif delta< -1e-8:
                    amount=min(-delta,qty);price=sellprice;side='sell';cost=amount*price*config['fee'];cash+=amount*price-cost;qty-=amount;delta=-amount
                if cash< -1e-6 or qty< -1e-6 or not math.isfinite(cash+qty): raise ValueError('Invalid balance')
                cash=max(cash,0.);qty=max(qty,0.);last=r[0];mark=r[4]
                db.execute('INSERT INTO ledger VALUES(?,?,?,?,?,?,?)',(last,target,side,abs(delta),price,cost,cash+qty*mark))
            db.execute('UPDATE account SET config=?,cash=?,qty=?,last_date=?,mark=? WHERE id=1',(json.dumps(config),cash,qty,last,mark))
        return self.snapshot()
    def snapshot(self, full=False):
        with self.connect() as db:
            row=db.execute('SELECT config,cash,qty,last_date,mark FROM account').fetchone()
            records=db.execute('SELECT * FROM ledger ORDER BY day DESC'+('' if full else ' LIMIT 100')).fetchall()
            trade=db.execute("SELECT * FROM ledger WHERE side IN ('buy','sell') ORDER BY day DESC LIMIT 1").fetchone()
        if not row: return {'active':False,'ledger':[]}
        config,cash,qty,last,mark=row
        return {'active':True,'config':json.loads(config),'cash':cash,'qty':qty,'last_date':last,'equity':cash+qty*mark,'ledger':records,'latest_trade':trade}
