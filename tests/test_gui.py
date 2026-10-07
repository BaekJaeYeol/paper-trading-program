import queue
import tempfile
import time
import unittest
from pathlib import Path
from stockbot.gui import Dashboard, account_view

class FakeAccount:
    def __init__(self, count=1): self.count=count; self.requests=[]
    def request(self,path,params=None):
        self.requests.append((path,params))
        if path=='/v2/account':
            return {'id':'private-id','equity':'1000','cash':'200','buying_power':'400','last_equity':'950'}
        if path=='/v2/clock': return {'is_open':False}
        if path=='/v2/positions': return [{'symbol':'AAPL','qty':'2','avg_entry_price':'100','current_price':'120','unrealized_pl':'40','account_id':'private-id'}]
        if path=='/v2/orders': return [{'symbol':'AAPL','side':'buy','qty':'1','filled_qty':'0','limit_price':'100','status':'new','secret':'hidden'}]*self.count
        raise AssertionError(path)

class GUIBehaviorTests(unittest.TestCase):
    def test_snapshot_read_only_and_excludes_private_fields(self):
        b=FakeAccount();result=account_view(b)
        self.assertEqual(result['daily_pnl'],50)
        self.assertFalse(result['market_open'])
        self.assertNotIn('private-id',str(result))
        self.assertNotIn('hidden',str(result))
        self.assertEqual([r[0] for r in b.requests],['/v2/account','/v2/clock','/v2/positions','/v2/orders'])
    def test_truncated_orders_rejected(self):
        with self.assertRaises(ValueError): account_view(FakeAccount(500))
    def test_worker_does_not_emit_exception_secret(self):
        d=Dashboard.__new__(Dashboard)
        d.busy=False;d.events=queue.Queue();d.actions=[]
        class Status:
            def set(self,*args): pass
        d.status=Status()
        class Selector:
            def configure(self, **kwargs): pass
        d.selector=Selector()
        def fail(): raise RuntimeError('super-secret-key')
        self.assertTrue(d.work('account',fail))
        result=d.events.get(timeout=2)
        self.assertEqual(result,('account',None,True))
        self.assertFalse(d.work('account',fail))
    def test_stop_creates_stop_and_cancels_repeat(self):
        d=Dashboard.__new__(Dashboard)
        d.running=True;d.timer='timer-id';d.write=lambda text:None
        class Root:
            def after_cancel(self,handle): self.cancelled=handle
        class Status:
            def set(self,value): self.value=value
        d.root=Root();d.status=Status()
        d.busy=False
        class Selector:
            def configure(self, **kwargs): pass
        d.selector=Selector()
        with tempfile.TemporaryDirectory() as temp:
            d.config={'state_dir':str(Path(temp)/'state')}
            d.stop()
            self.assertTrue((Path(temp)/'state/STOP').exists())
            self.assertFalse(d.running)
            self.assertIsNone(d.timer)
            self.assertEqual(d.root.cancelled,'timer-id')
