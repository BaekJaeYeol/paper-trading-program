from contextlib import closing
import copy
import sqlite3
import tempfile
import unittest
from pathlib import Path
from stockbot.cli import cycle,load_config
from stockbot.paper_journal import reconcile_snapshot,account_snapshot
from stockbot.ui_safety import resume_snapshot
from test_paper_journal import TrackingBroker
ROOT=Path(__file__).resolve().parents[1]

class BracketTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.c=load_config(ROOT/'config.json');self.c.update(state_dir=self.temp.name,symbols=['AAPL'])
        self.b=TrackingBroker();cycle(self.c,True,self.b)
        self.cid=next(iter(self.b.orders));self.root=self.b.orders[self.cid]
        self.qty=int(self.root['qty'])
    def check(self):return reconcile_snapshot(self.c,self.b,account_snapshot)
    def fill_parent(self):self.root.update(status='filled',filled_qty=str(self.qty))
    def test_tracks_two_exit_legs_and_managed_inventory(self):
        self.fill_parent();data=self.check()
        self.assertTrue(data['inventory']['ready'])
        self.assertEqual(data['inventory']['rows'][0]['expected'],str(self.qty))
        self.assertEqual(len(data['order_history']),3)
        self.assertTrue(any('익절' in r['status'] for r in data['order_history']))
        self.assertTrue(any('손절' in r['status'] for r in data['order_history']))
        self.assertEqual(len(self.b.sent),1)
    def test_partial_take_profit_and_adjusted_stop_quantity(self):
        self.fill_parent();tp,sl=self.root['legs']
        tp.update(status='partially_filled',filled_qty='2');sl.update(qty=str(self.qty-2),status='new')
        data=self.check();self.assertTrue(data['inventory']['ready'])
        self.assertEqual(data['inventory']['rows'][0]['expected'],str(self.qty-2))
        sl.update(status='filled',filled_qty=str(self.qty-2));tp['status']='canceled'
        data=self.check();self.assertTrue(data['inventory']['ready']);self.assertEqual(data['inventory']['rows'][0]['expected'],'0')
    def test_missing_legs_after_full_entry_blocks_resume(self):
        self.fill_parent();self.root['legs']=[];data=self.check()
        self.assertFalse(data['inventory']['ready']);self.assertEqual(data['reconciliation']['unresolved'],1)
        with self.assertRaises(RuntimeError):resume_snapshot(self.c,self.b,account_snapshot)
    def test_parent_remains_filled_but_later_exit_is_refreshed(self):
        self.fill_parent();self.check()
        self.root['legs'][0].update(status='filled',filled_qty=str(self.qty));self.root['legs'][1]['status']='canceled'
        data=self.check();self.assertEqual(data['inventory']['rows'][0]['expected'],'0');self.assertTrue(data['inventory']['ready'])
    def test_child_identity_disappearance_and_quantity_regression(self):
        self.fill_parent();self.root['legs'][0].update(status='partially_filled',filled_qty='2');self.check()
        self.root['legs'][0]['filled_qty']='1';self.assertEqual(self.check()['reconciliation']['unresolved'],1)
        self.root['legs'][0]['filled_qty']='2';self.root['legs'][0]['id']='another-id'
        self.assertEqual(self.check()['reconciliation']['unresolved'],1)
    def test_double_exit_overfill_is_blocked_atomically(self):
        self.fill_parent()
        for leg in self.root['legs']:leg.update(status='filled',filled_qty=str(self.qty))
        data=self.check();self.assertFalse(data['inventory']['ready'])
        with closing(sqlite3.connect(Path(self.temp.name)/'orders.sqlite')) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM paper_legs').fetchone()[0],0)
    def test_duplicate_or_foreign_child_rejected(self):
        original=copy.deepcopy(self.root['legs']);self.fill_parent()
        self.root['legs'][1]['id']=self.root['legs'][0]['id'];self.assertEqual(self.check()['reconciliation']['unresolved'],1)
        self.root['legs']=original;self.root['legs'][0]['symbol']='MSFT'
        self.assertEqual(self.check()['reconciliation']['unresolved'],1)
    def test_actual_position_mismatch_blocks_new_entry_without_liquidation(self):
        self.fill_parent();old=self.b.request
        def request(path,params=None,body=None):
            result=old(path,params,body)
            if path=='/v2/positions':result[0]['qty']=str(self.qty+1)
            return result
        self.b.request=request;data=self.check();self.assertFalse(data['inventory']['ready'])
        self.assertFalse(data['inventory']['rows'][0]['matched'])
        self.c['symbols']=['MSFT']
        with self.assertRaises(RuntimeError):cycle(self.c,True,self.b)
        self.assertEqual(len(self.b.sent),1)
    def test_unrelated_manual_holding_is_not_owned_or_sold(self):
        self.fill_parent();old=self.b.request
        def request(path,params=None,body=None):
            result=old(path,params,body)
            if path=='/v2/positions':result.append({'symbol':'MANUAL','qty':'7','avg_entry_price':'10','current_price':'10','unrealized_pl':'0'})
            return result
        self.b.request=request;data=self.check();self.assertTrue(data['inventory']['ready'])
        self.assertEqual([r['symbol'] for r in data['inventory']['rows']],['AAPL']);self.assertEqual(len(self.b.sent),1)
    def test_stop_is_unchanged_on_both_match_and_mismatch(self):
        Path(self.temp.name,'STOP').touch();self.fill_parent();self.check()
        self.root['legs']=[];self.check()
        self.assertTrue(Path(self.temp.name,'STOP').exists());self.assertEqual(len(self.b.sent),1)
