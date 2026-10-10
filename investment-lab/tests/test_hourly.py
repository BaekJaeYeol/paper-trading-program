import sys,tempfile,unittest,csv,datetime
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from hourly import tick
ROOT=Path(__file__).resolve().parents[1]
class HourlyTests(unittest.TestCase):
    def test_repeat_and_failure_preserve_state(self):
        def fixture(symbol,path):
            with open(path,'w',newline='') as f:
                w=csv.writer(f);w.writerow(['date','open','high','low','close','volume'])
                for i in range(377):
                    price=100+i*.1
                    w.writerow([(datetime.date(2020,1,1)+datetime.timedelta(days=i)).isoformat(),price,price+1,price-1,price,1000])
            return path
        with tempfile.TemporaryDirectory() as d:
            tick(d,['SPY'],fixture)
            dbs={p.name:p.read_bytes() for p in Path(d).rglob('*.sqlite')}
            tick(d,['SPY'],fixture)
            self.assertEqual(dbs,{p.name:p.read_bytes() for p in Path(d).rglob('*.sqlite')})
            def fail(symbol,path):raise RuntimeError('network failure')
            result=tick(d,['SPY'],fail)
            self.assertEqual(result['symbols']['SPY']['status'],'error')
            self.assertEqual(dbs,{p.name:p.read_bytes() for p in Path(d).rglob('*.sqlite')})
