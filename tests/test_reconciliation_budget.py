import copy
import io
import json
import sqlite3
import threading
import unittest
from contextlib import closing,redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock,patch
import test_paper_journal
import test_ui_safety
from stockbot import paper_journal as journal,cli
from stockbot.power import SleepGuard,ES_CONTINUOUS

class BudgetTests(unittest.TestCase):
    setUp=test_paper_journal.JournalTests.setUp
    submit=test_paper_journal.JournalTests.submit
    check=test_paper_journal.JournalTests.check
    def gate(self):
        with closing(sqlite3.connect(Path(self.temp.name)/'orders.sqlite')) as db:
            return json.loads(db.execute("SELECT value FROM paper_meta WHERE key='inventory_gate'").fetchone()[0])
    def clock(self,value):return patch.object(journal,'time',SimpleNamespace(monotonic=lambda:value[0]))
    def test_first_slow_snapshot_revokes_previous_success_gate(self):
        self.submit();self.assertTrue(self.check()['inventory']['ready']);clock=[0]
        def reader(b):
            data=journal.account_snapshot(b);clock[0]=61;return data
        with self.clock(clock):
            with self.assertRaises(journal.ReconciliationTimeout):journal.reconcile_snapshot(self.c,self.b,reader)
        self.assertFalse(self.gate()['ready']);self.assertFalse(Path(self.temp.name,'cycle.lock').exists());self.assertEqual(len(self.b.sent),1)
    def test_long_nested_lookup_does_not_publish_partial_leg_updates(self):
        cid=self.submit();self.check();clock=[0];original=self.b.bracket_order
        self.b.orders[cid]['legs'][0]['status']='new'
        def nested(bid):result=original(bid);clock[0]=61;return result
        self.b.bracket_order=nested
        with self.clock(clock):
            with self.assertRaises(journal.ReconciliationTimeout):self.check()
        with closing(sqlite3.connect(Path(self.temp.name)/'orders.sqlite')) as db:
            self.assertEqual(db.execute("SELECT status FROM paper_legs WHERE role='take_profit'").fetchone()[0],'held')
        self.assertFalse(self.gate()['ready'])
    def test_no_extra_lookup_after_budget_expires(self):
        self.submit();self.check();clock=[0];calls=[];original=self.b.find_order
        def find(cid):calls.append(cid);result=original(cid);clock[0]=60;return result
        self.b.find_order=find;self.b.bracket_order=Mock()
        with self.clock(clock):
            with self.assertRaises(journal.ReconciliationTimeout):self.check()
        self.assertEqual(len(calls),1);self.b.bracket_order.assert_not_called()
    def test_initial_read_failure_and_cancellation_revoke_gate(self):
        self.submit();self.check()
        with self.assertRaises(OSError):journal.reconcile_snapshot(self.c,self.b,Mock(side_effect=OSError('private')))
        self.assertFalse(self.gate()['ready']);self.check()
        event=threading.Event();event.set();self.c['_reconcile_cancel']=event
        with self.assertRaises(RuntimeError):self.check()
        self.assertFalse(self.gate()['ready'])
    def test_expiration_before_final_commit_rolls_back_review_resolution(self):
        cid=self.submit();root=self.b.orders[cid];original=copy.deepcopy(root)
        root['limit_price']='999';data=self.check();case=next(c for c in data['review']['cases'] if c['code']=='price_changed')
        root.clear();root.update(original);root['status']='canceled'
        for leg in root['legs']:leg['status']='canceled'
        Path(self.temp.name,'STOP').touch();clock=[0];history=journal.history
        def delayed(db):result=history(db);clock[0]=61;return result
        with self.clock(clock),patch.object(journal,'history',side_effect=delayed):
            with self.assertRaises(journal.ReconciliationTimeout):journal.reconcile_snapshot(self.c,self.b,journal.account_snapshot,resolve_case=(cid,case['code'],case['version']))
        with closing(sqlite3.connect(Path(self.temp.name)/'orders.sqlite')) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM paper_review_resolutions').fetchone()[0],0)
            self.assertEqual(db.execute("SELECT active FROM paper_review_cases WHERE code='price_changed'").fetchone()[0],1)
        self.assertFalse(self.gate()['ready'])
    def test_success_reports_total_elapsed_and_can_revalidate_after_failure(self):
        self.submit();clock=[0]
        def reader(b):
            result=journal.account_snapshot(b);clock[0]+=10;result['received_monotonic']=clock[0];return result
        with self.clock(clock):data=journal.reconcile_snapshot(self.c,self.b,reader)
        self.assertEqual(data['reconciliation']['elapsed_seconds'],20);self.assertTrue(data['inventory']['ready'])
    def test_gui_timeout_message_stops_and_releases_without_exception_text(self):
        app=test_ui_safety.SafetyTests().fake_dashboard(self.temp.name);app.running=True
        guard=SleepGuard(platform='win32',native=Mock(return_value=ES_CONTINUOUS));guard.acquire();app.sleep_guard=guard
        def fail():raise journal.ReconciliationTimeout('SECRET_TEXT')
        app.work('trade',fail);event=app.events.get(timeout=2);self.assertEqual(event,('trade',None,'reconciliation_timeout'))
        app.events.put(event);app.poll()
        self.assertFalse(app.running);self.assertFalse(guard.active);self.assertIn('60초',app.order_notice.get());self.assertNotIn('SECRET_TEXT',app.status.get())
    def test_cli_timeout_exits_instead_of_scheduling_retry(self):
        guard=SleepGuard(platform='win32',native=Mock(return_value=ES_CONTINUOUS));orders=Mock()
        with patch.object(cli,'SleepGuard',return_value=guard),patch.object(cli,'load_config',return_value=self.c),patch.object(cli,'AlpacaPaper'),patch.object(cli,'cycle',orders),patch.object(journal,'reconcile_snapshot',side_effect=journal.ReconciliationTimeout('fixed')),patch('sys.argv',['stockbot','run','--execute-paper']),redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit):cli.main()
        orders.assert_not_called();self.assertFalse(guard.active)
