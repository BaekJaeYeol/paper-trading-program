import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from stockbot.core import Bar, signal, size, backtest
from stockbot.cli import cycle, load_config

ROOT = Path(__file__).resolve().parents[1]

class FakeBroker:
    def __init__(self, fail=False):
        self.sent=[];self.fail=fail
    def request(self,path,params=None,body=None):
        if path=='/v2/clock': return {'is_open':True,'timestamp':'2026-10-05T14:00:00Z'}
        if path=='/v2/calendar': return [{'date':'2026-10-02'}]
        if path=='/v2/account': return {'status':'ACTIVE','equity':'10000','last_equity':'10000','buying_power':'10000'}
        if path in ('/v2/positions','/v2/orders') and body is None: return []
        if body:
            self.sent.append(body)
            if self.fail: raise TimeoutError()
            return {'id':'test'}
        raise AssertionError(path)
    def bars(self,*args):
        end=date(2026,10,2)
        return [{'t':f'{end-timedelta(days=30-i)}T04:00:00Z','o':100,'h':101,'l':99,'c':100,'v':3000 if i==30 else 1000} for i in range(31)]
    def quote(self,*args): return {'t':'2026-10-05T14:00:00Z','bp':99.99,'ap':100}

class Tests(unittest.TestCase):
    def bars(self):
        return [Bar(date(2026,1,1)+timedelta(days=i),100,101,99,100,3000 if i==30 else 1000) for i in range(31)]
    def test_threshold_excludes_current_volume(self):
        self.assertEqual(signal(self.bars())['volume_ratio'],3)
    def test_insufficient(self): self.assertIsNone(signal(self.bars()[:30]))
    def test_size(self):
        self.assertEqual(size(10000,200,100,.05),2)
        self.assertEqual(size(10000,200,float('nan'),.05),0)
    def test_invalid(self):
        with self.assertRaises(ValueError): Bar(date.today(),100,90,99,100,1)
    def test_next_open_and_stop_first(self):
        c=load_config(ROOT/'config.json')
        bars=self.bars()+[Bar(date(2026,2,1),100,120,90,100,1000)]
        r=backtest(bars,c)
        self.assertEqual(len(r['trades']),2)
        self.assertEqual(r['trades'][0]['date'],'2026-02-01')
        self.assertLess(r['trades'][1]['price'],95)
    def test_dry_run_duplicate_and_unknown(self):
        for fail in (False,True):
            with tempfile.TemporaryDirectory() as temp:
                c=load_config(ROOT/'config.json');c['symbols']=['AAPL'];c['state_dir']=temp
                b=FakeBroker(fail)
                self.assertEqual(len(cycle(c,False,b)['orders']),1)
                self.assertEqual(len(b.sent),0)
                if fail:
                    with self.assertRaises(RuntimeError): cycle(c,True,b)
                else: cycle(c,True,b)
                cycle(c,True,b)
                self.assertEqual(len(b.sent),1)
    def test_daily_loss_and_stale_quote(self):
        with tempfile.TemporaryDirectory() as temp:
            c=load_config(ROOT/'config.json');c['symbols']=['AAPL'];c['state_dir']=temp
            class LossBroker(FakeBroker):
                def request(self,path,params=None,body=None):
                    r=super().request(path,params,body)
                    if path=='/v2/account': r['equity']='9700'
                    return r
            self.assertEqual(cycle(c,True,LossBroker())['status'],'daily_loss_limit')
            class StaleBroker(FakeBroker):
                def quote(self,*args): return {'t':'2026-10-05T13:00:00Z','bp':99.99,'ap':100}
            b=StaleBroker()
            self.assertEqual(cycle(c,True,b)['orders'],[])
            self.assertEqual(b.sent,[])
    def test_concurrent_cycle_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            c=load_config(ROOT/'config.json');c['state_dir']=temp
            Path(temp,'cycle.lock').mkdir()
            with self.assertRaises(RuntimeError): cycle(c,True,FakeBroker())
    def test_kill_switch(self):
        with tempfile.TemporaryDirectory() as temp:
            c=load_config(ROOT/'config.json');c['state_dir']=temp
            Path(temp,'STOP').touch()
            self.assertEqual(cycle(c,True,FakeBroker())['status'],'halted')

if __name__=='__main__': unittest.main()
