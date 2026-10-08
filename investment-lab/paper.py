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
            if not anchor or abs(anchor[4]/mark-1)>1e-6: raise ValueError('기준 일봉이 변경되었습니다. 분할/데이터 수정 확인이 필요합니다')
            for i,r in enumerate(rows):
                if r[0]<=last: continue
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
            db.execute('UPDATE account SET cash=?,qty=?,last_date=?,mark=? WHERE id=1',(cash,qty,last,mark))
        return self.snapshot()
    def snapshot(self):
        with self.connect() as db:
            row=db.execute('SELECT config,cash,qty,last_date,mark FROM account').fetchone()
            records=db.execute('SELECT * FROM ledger ORDER BY day DESC LIMIT 100').fetchall()
        if not row: return {'active':False,'ledger':[]}
        config,cash,qty,last,mark=row
        return {'active':True,'config':json.loads(config),'cash':cash,'qty':qty,'last_date':last,'equity':cash+qty*mark,'ledger':records}
