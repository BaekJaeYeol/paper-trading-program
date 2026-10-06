import tempfile
import unittest
from decimal import Decimal as D
from stockbot.recovery import Coordinator, Order

class Fake:
    def __init__(self): self.orders={};self.count=0;self.timeout=False;self.cancels=[]
    def find_order(self,cid): return self.orders.get(cid)
    def submit(self,r,cid):
        self.count+=1
        order=Order(cid,'broker-1',r['symbol'],D(str(r['qty'])),D('0'),'accepted')
        self.orders[cid]=order
        if self.timeout: raise TimeoutError()
        return order
    def account_snapshot(self): return {'complete':True,'account_id':'fake','as_of':'2026-10-05T14:00:00Z','positions':[],'open_orders':[]}
    def cancel(self,bid): self.cancels.append(bid)

class RecoveryTests(unittest.TestCase):
    def test_partial_restart_and_duplicates(self):
        with tempfile.TemporaryDirectory() as root:
            b=Fake();c=Coordinator(root,b);c.synchronize()
            c.submit('one',{'symbol':'AAPL','qty':10})
            c.submit('one',{'symbol':'AAPL','qty':10})
            self.assertEqual(b.count,1)
            b.orders['one']=Order('one','broker-1','AAPL',D(10),D(3),'partially_filled')
            c=Coordinator(root,b)
            self.assertTrue(c.synchronize()['ready'])
            self.assertEqual(c.intent('one')[3],'3')
            b.orders['one']=Order('one','broker-1','AAPL',D(10),D(10),'filled')
            c.synchronize();self.assertEqual(c.intent('one')[1],'filled')
    def test_timeout_then_found(self):
        with tempfile.TemporaryDirectory() as root:
            b=Fake();b.timeout=True;c=Coordinator(root,b);c.synchronize()
            with self.assertRaises(RuntimeError): c.submit('one',{'symbol':'AAPL','qty':10})
            self.assertTrue(c.synchronize()['ready'])
            c.submit('one',{'symbol':'AAPL','qty':10});self.assertEqual(b.count,1)
    def test_missing_blocks_all_new_orders(self):
        with tempfile.TemporaryDirectory() as root:
            b=Fake();b.timeout=True;c=Coordinator(root,b);c.synchronize()
            with self.assertRaises(RuntimeError): c.submit('one',{'symbol':'AAPL','qty':10})
            b.orders.clear();self.assertFalse(c.synchronize()['ready'])
            with self.assertRaises(RuntimeError): c.submit('two',{'symbol':'MSFT','qty':1})
    def test_halt_only_managed_and_cancel_not_final(self):
        with tempfile.TemporaryDirectory() as root:
            b=Fake();c=Coordinator(root,b);c.synchronize();c.submit('one',{'symbol':'AAPL','qty':10})
            self.assertEqual(c.halt(True)[0]['status'],'cancel_requested')
            self.assertEqual(b.cancels,['broker-1'])
            self.assertEqual(c.intent('one')[1],'accepted')
            with self.assertRaises(RuntimeError): c.submit('two',{'symbol':'AAPL','qty':1})
    def test_payload_change_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            b=Fake();c=Coordinator(root,b);c.synchronize();c.submit('one',{'symbol':'AAPL','qty':10})
            with self.assertRaises(ValueError): c.submit('one',{'symbol':'AAPL','qty':11})
