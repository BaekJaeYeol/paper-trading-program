import copy
import sqlite3
import threading
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import patch,Mock
import test_paper_journal
from stockbot.paper_journal import reconcile_snapshot,account_snapshot
from stockbot import brackets
from stockbot.gui import Dashboard

class ReviewRecoveryTests(unittest.TestCase):
    setUp=test_paper_journal.JournalTests.setUp
    submit=test_paper_journal.JournalTests.submit
    check=test_paper_journal.JournalTests.check
    def prepare(self):
        self.cid=self.submit();self.root=self.b.orders[self.cid];self.original=copy.deepcopy(self.root)
        self.root['limit_price']='999';data=self.check()
        self.case=next(c for c in data['review']['cases'] if c['code']=='price_changed')
        self.selection=(self.case['target'],self.case['code'],self.case['version'])
        self.root.clear();self.root.update(copy.deepcopy(self.original));self.root['status']='canceled'
        for leg in self.root['legs']:leg['status']='canceled'
        Path(self.temp.name,'STOP').touch()
    def recover(self,reader=account_snapshot,selection=None):
        return reconcile_snapshot(self.c,self.b,reader,resolve_case=selection or self.selection)
    def audit(self):
        with closing(sqlite3.connect(Path(self.temp.name)/'orders.sqlite')) as db:
            return db.execute('SELECT code,basis FROM paper_review_resolutions').fetchall()
    def test_closed_flat_original_recovery_keeps_stop_and_audit(self):
        self.prepare();data=self.recover()
        self.assertTrue(data['review_resolution']['resolved']);self.assertTrue(data['inventory']['ready'])
        self.assertFalse(data['review']['cases'][0]['active']);self.assertEqual(len(self.audit()),1)
        self.assertTrue(Path(self.temp.name,'STOP').is_file());self.assertEqual(len(self.b.sent),1)
        with self.assertRaises(RuntimeError):self.recover()
        self.assertEqual(len(self.audit()),1)
    def test_requires_stop_before_any_broker_read(self):
        self.prepare();Path(self.temp.name,'STOP').unlink();reader=Mock()
        with self.assertRaises(RuntimeError):self.recover(reader)
        reader.assert_not_called();self.assertEqual(self.audit(),[])
    def test_open_root_or_held_child_cannot_clear(self):
        self.prepare();self.root['status']='new'
        with self.assertRaises(RuntimeError):self.recover()
        self.root['status']='canceled';self.root['legs'][0]['status']='held'
        with self.assertRaises(RuntimeError):self.recover()
        self.assertEqual(self.audit(),[])
    def test_nonflat_holdings_cannot_clear(self):
        self.prepare();self.root.update(status='filled',filled_qty=self.root['qty'])
        with self.assertRaises(RuntimeError):self.recover()
        self.assertEqual(self.audit(),[])
    def test_changed_case_token_and_still_wrong_price_cannot_clear(self):
        self.prepare();self.root['limit_price']='999'
        with self.assertRaises(RuntimeError):self.recover()
        self.root['limit_price']=self.original['limit_price']
        with self.assertRaises(RuntimeError):self.recover()
        self.assertEqual(self.audit(),[])
    def test_unsupported_replacement_cannot_be_resolved(self):
        self.prepare();self.root['replaced_by']='another';data=self.check()
        case=next(c for c in data['review']['cases'] if c['code']=='order_replaced')
        self.assertFalse(case['recovery_supported']);self.root.pop('replaced_by')
        with self.assertRaises(RuntimeError):self.recover(selection=(case['target'],case['code'],case['version']))
        self.assertEqual(self.audit(),[])
    def test_other_cases_remain_blocking(self):
        self.prepare();self.root['replaced_by']='another';self.check();self.root.pop('replaced_by')
        data=self.recover();self.assertFalse(data['inventory']['ready'])
        self.assertTrue(any(c['code']=='order_replaced' and c['active'] for c in data['review']['cases']))
    def test_account_switch_and_lookup_failure_do_not_clear(self):
        self.prepare();self.b.account_id='other'
        with self.assertRaises(ValueError):self.recover()
        self.b.account_id='offline-paper';self.b.lookup_error=True
        with self.assertRaises(RuntimeError):self.recover()
        self.assertEqual(self.audit(),[])
    def test_stop_removed_or_cancellation_during_reads_does_not_clear(self):
        self.prepare();event=threading.Event();self.c['_reconcile_cancel']=event
        def reader(b):
            data=account_snapshot(b);event.set();return data
        with self.assertRaises(RuntimeError):self.recover(reader)
        event.clear()
        def remove_stop(b):
            data=account_snapshot(b);Path(self.temp.name,'STOP').unlink(missing_ok=True);return data
        with self.assertRaises(RuntimeError):self.recover(remove_stop)
        self.assertEqual(self.audit(),[])
    def test_resolution_and_audit_rollback_together_on_gate_failure(self):
        self.prepare();original=brackets.inventory;calls=[]
        def inventory(*args,**kwargs):
            calls.append(1)
            if len(calls)==2:raise RuntimeError('simulated gate persistence failure')
            return original(*args,**kwargs)
        with patch('stockbot.paper_journal.brackets.inventory',side_effect=inventory):
            with self.assertRaises(RuntimeError):self.recover()
        self.assertEqual(self.audit(),[])
        self.assertTrue(next(c for c in self.check()['review']['cases'] if c['code']=='price_changed')['active'])
    def test_delayed_full_reconciliation_does_not_clear(self):
        self.prepare()
        # account_snapshot has its own timings; isolate the reconciliation module clock.
        snapshot=dict(account_snapshot(self.b),received_monotonic=61)
        with patch('stockbot.paper_journal.time',Mock(monotonic=Mock(side_effect=[0]+[61]*20))):
            with self.assertRaises(RuntimeError):self.recover(lambda b:copy.deepcopy(snapshot))
        self.assertEqual(self.audit(),[])
    def test_gui_cancel_never_starts_recovery(self):
        self.prepare();app=Dashboard.__new__(Dashboard);app.busy=False;app.running=False;app.config=self.c;app.root=Mock()
        app.market=Mock();app.market.get.return_value='미국';table=Mock();table.selection.return_value=['row']
        app.tables={'review':table};app.review_items={'row':self.case};app.work=Mock()
        with patch('stockbot.gui.messagebox.askyesno',return_value=False):app.recover_review()
        app.work.assert_not_called();self.assertEqual(self.audit(),[])
