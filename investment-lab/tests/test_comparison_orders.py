import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from comparison import compare
from orders import Controller,MockBroker
from reliability import advance_v2
class ComparisonTests(unittest.TestCase):
    def rows(self):return [(str(i),p,p,p,p,10000) for i,p in enumerate([100,105,90,95,110,100])]
    def test_constant_weight_and_cost(self):
        r=compare(self.rows(),[.5]*6,1,6)
        self.assertAlmostEqual(r['strategy_net']['average_exposure'],r['matched_buy_hold_net']['average_exposure'],places=8)
        self.assertGreater(r['cost_drag'],0)
        self.assertGreater(r['drawdown_reduction_from_cash'],0)
    def test_cash_and_full(self):
        r=compare(self.rows(),[0]*6,1,6)
        self.assertEqual(r['strategy_net']['return_'],0)
        self.assertAlmostEqual(r['matched_buy_hold_net']['return_'],0,places=8)
        r=compare(self.rows(),[1]*6,1,6)
        self.assertAlmostEqual(r['strategy_net']['return_'],r['buy_hold_net']['return_'])
    def test_future_invariance(self):
        r=compare(self.rows(),[.5]*6,1,4)
        rows=self.rows();rows[-1]=('5',999,999,999,999,1)
        self.assertEqual(r,compare(rows,[.5]*6,1,4))
class OrderTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.b=MockBroker(self.root/'broker.sqlite');self.c=Controller(self.root/'controller.sqlite',self.b)
    def tearDown(self):self.c.db.close();self.b.db.close();self.temp.cleanup()
    def test_lost_reply_restart_no_duplicate(self):
        self.b.lose_reply=True;o=self.c.submit('SPY:strategy:bar1','buy',10,100,'2026-10-09')
        self.assertEqual(o['status'],'unknown')
        self.c.db.close();self.c=Controller(self.root/'controller.sqlite',self.b)
        self.assertTrue(self.c.reconcile());self.assertEqual(self.c.intents()[0]['status'],'accepted')
        again=self.c.submit('SPY:strategy:bar1','buy',10,100,'2026-10-09')
        self.assertEqual(again['status'],'accepted');self.assertEqual(len(self.c.intents()),1)
        with self.assertRaises(ValueError):self.c.submit('different','buy',1,100,'2026-10-09')
    def test_partial_and_cancel(self):
        o=self.c.submit('a','buy',10,100,'2026-10-09');self.b.fill(o['id'],3)
        self.assertTrue(self.c.reconcile());self.assertEqual(self.c.intents()[0]['status'],'partial')
        result=self.c.emergency_stop();self.assertTrue(result['cancellation_confirmed'])
        self.assertEqual(self.c.intents()[0]['status'],'canceled');self.assertEqual(self.b.balance(),(9700,3))
        with self.assertRaises(ValueError):self.c.submit('b','sell',3,100,'2026-10-09')
    def test_cancel_failure_stays_halted(self):
        self.c.submit('a','buy',1,100,'2026-10-09');self.b.fail_cancel=True
        self.assertFalse(self.c.emergency_stop()['cancellation_confirmed']);self.assertTrue(self.c.control()['halted'])
    def test_balance_mismatch(self):
        self.b.db.execute('UPDATE balance SET cash=9999');self.b.db.commit()
        self.assertFalse(self.c.reconcile());self.assertTrue(self.c.control()['halted'])
    def test_risk_and_conflict(self):
        o=self.c.submit('a','buy',100,100,'2026-10-09');self.b.fill(o['id'],100)
        self.assertFalse(self.c.gate(96,'2026-10-09'));self.assertTrue(self.c.control()['halted'])
        with self.assertRaises(ValueError):self.c.submit('a','buy',10,100,'2026-10-09')
    def test_v2_loss_limit(self):
        rows=[(f'2026-10-09T{h}+00:00',p,p,p,p,1e6) for h,p in [('13:30:00',100),('13:45:00',100),('14:00:00',95),('14:15:00',100)]]
        a=advance_v2(None,rows[:1],[1],0);a=advance_v2(a,rows,[1]*4,0)
        self.assertTrue(a['risk']['halted']);self.assertEqual(a['events'][-1]['quantity'],0)
if __name__=='__main__':unittest.main()
