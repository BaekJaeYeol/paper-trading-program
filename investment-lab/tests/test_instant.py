import datetime,time,tempfile,unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from engine import load
from paper import Paper
from data import validate_quote
from zoneinfo import ZoneInfo
class InstantTests(unittest.TestCase):
    def setUp(self):
        rows=load(Path(__file__).resolve().parents[1]/'demo_synthetic.csv');end=datetime.datetime.now(ZoneInfo('America/New_York')).date()-datetime.timedelta(days=1)
        self.rows=[((end-datetime.timedelta(days=len(rows)-1-i)).isoformat(),*r[1:]) for i,r in enumerate(rows)]
    def quote(self):return {'symbol':'SPY','currency':'USD','price':100.,'timestamp':time.time(),'session':'pre','source':'fixture'}
    def test_entry_once_and_following_daily_bar(self):
        with tempfile.TemporaryDirectory() as d:
            p=Paper(Path(d)/'p.sqlite');p.start(self.rows,'buy_hold','real_download')
            q=self.quote();s=p.enter_now(self.rows,q,'SPY');self.assertGreater(s['qty'],0)
            self.assertEqual(s['ledger'][0][2],'buy');qty=s['qty']
            self.assertEqual(p.enter_now(self.rows,q,'SPY')['qty'],qty)
            self.assertEqual(Paper(p.path).enter_now(self.rows,q,'SPY')['qty'],qty)
            day=datetime.datetime.fromtimestamp(q['timestamp'],ZoneInfo('America/New_York')).date()
            rows=self.rows+[(day.isoformat(),100,102,99,101,1000)]
            s=p.advance(rows);self.assertEqual(s['qty'],qty);self.assertEqual(len(s['ledger']),1)
            self.assertEqual(s['last_date'],day.isoformat());self.assertFalse(s['config']['instant_pending'])
            tomorrow=day+datetime.timedelta(days=1)
            rows.append((tomorrow.isoformat(),101,103,100,102,1000))
            s=p.advance(rows);self.assertEqual(len(s['ledger']),2)
    def test_zero_signal_and_invalid_quote_no_fill(self):
        with tempfile.TemporaryDirectory() as d:
            p=Paper(Path(d)/'p.sqlite');p.start(self.rows,'cash','real_download')
            q=self.quote();q['timestamp']-=1201
            with self.assertRaises(ValueError):p.enter_now(self.rows,q,'SPY')
            self.assertEqual(p.snapshot()['ledger'],[])
            s=p.enter_now(self.rows,self.quote(),'SPY');self.assertEqual(s['qty'],0);self.assertEqual(s['ledger'][0][2],'hold')
    def test_quote_checks(self):
        for changes in [{'currency':'KRW'},{'session':None},{'price':float('nan')},{'symbol':'AAPL'},{'timestamp':time.time()+30}]:
            q=self.quote();q.update(changes)
            with self.assertRaises(ValueError):validate_quote(q,'SPY')
