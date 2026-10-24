import sqlite3
import tempfile
import threading
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import Mock,patch
from stockbot import health,paper_journal as journal
from stockbot.gui import Dashboard
import test_paper_journal

class HealthStoreTests(unittest.TestCase):
    def setUp(self):
        self.db=sqlite3.connect(':memory:');self.addCleanup(self.db.close);health.initialize(self.db)
    def test_consecutive_state_groups_and_recovery_transition(self):
        for _ in range(3):health.record(self.db,'timeout')
        health.result(self.db,False);health.result(self.db,True);health.result(self.db,True)
        data=health.history(self.db)
        self.assertEqual([e['code'] for e in data['events']],['recovered','blocked','timeout'])
        self.assertEqual(data['events'][2]['occurrences'],3)
        self.assertIn('자동 재개',data['events'][0]['title'])
    def test_first_success_does_not_invent_prior_incident(self):
        health.result(self.db,True);self.assertEqual(health.history(self.db)['events'],[])
    def test_group_retention_and_display_limit(self):
        for i in range(240):health.record(self.db,'timeout' if i%2 else 'failed')
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM paper_system_events').fetchone()[0],200)
        self.assertEqual(len(health.history(self.db)['events']),50)
    def test_unknown_code_and_malformed_timestamp_not_echoed(self):
        with self.assertRaises(ValueError):health.record(self.db,'SECRET_EXCEPTION')
        self.db.execute("INSERT INTO paper_system_events(code,first_seen,last_seen,occurrences) VALUES ('SECRET_CODE','SECRET_KEY','SECRET_BODY',-5)")
        data=health.history(self.db);self.assertNotIn('SECRET',str(data));self.assertEqual(data['events'][0]['occurrences'],1)
        self.assertEqual(data['events'][0]['last_seen'],'미확인')
    def test_read_only_load_missing_legacy_and_corrupt_files(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertTrue(health.load(d)['available']);self.assertFalse(Path(d,'orders.sqlite').exists())
            p=Path(d,'orders.sqlite');p.write_bytes(b'bad SQLite SECRET')
            self.assertFalse(health.load(d)['available']);self.assertEqual(p.read_bytes(),b'bad SQLite SECRET')
            p.unlink()
            with closing(sqlite3.connect(p)) as db:db.execute('CREATE TABLE legacy(id)');db.commit()
            self.assertEqual(health.load(d)['events'],[])
    def test_locked_read_is_unavailable_and_does_not_modify(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d,'orders.sqlite')
            with closing(sqlite3.connect(p)) as db:
                health.initialize(db);health.record(db,'timeout');db.commit();db.execute('BEGIN EXCLUSIVE')
                self.assertFalse(health.load(d)['available']);db.rollback()
            self.assertEqual(health.load(d)['events'][0]['code'],'timeout')
    def test_events_rollback_with_final_transaction(self):
        health.record(self.db,'failed');self.db.commit();health.result(self.db,True);self.db.rollback()
        self.assertEqual(health.history(self.db)['events'][0]['code'],'failed')
    def test_summary_contains_only_fixed_codes_and_counts(self):
        health.record(self.db,'failed');summary=health.summary(health.history(self.db))
        self.assertEqual(summary['latest_code'],'failed');self.assertEqual(summary['counts_in_displayed_groups']['failed'],1)
        self.assertNotIn('first_seen',str(summary))

class HealthIntegrationTests(unittest.TestCase):
    setUp=test_paper_journal.JournalTests.setUp
    check=test_paper_journal.JournalTests.check
    def test_persist_timeout_and_recovery_across_connections(self):
        for _ in range(2):
            with self.assertRaises(journal.ReconciliationTimeout):journal.reconcile_snapshot(self.c,self.b,Mock(side_effect=journal.ReconciliationTimeout('SECRET_TOKEN')))
        data=health.load(self.temp.name)
        self.assertEqual(data['events'][0]['occurrences'],2);self.assertNotIn('SECRET',str(data))
        self.assertEqual(self.check()['system_health']['events'][0]['code'],'recovered')
        self.assertEqual(health.load(self.temp.name)['events'][1]['code'],'timeout');self.assertEqual(len(self.b.sent),0)
    def test_cancel_and_unknown_failure_are_distinct_fixed_codes(self):
        event=threading.Event();event.set();self.c['_reconcile_cancel']=event
        with self.assertRaises(journal.ReconciliationCancelled):self.check()
        self.assertEqual(health.load(self.temp.name)['events'][0]['code'],'cancelled');event.clear()
        with self.assertRaises(OSError):journal.reconcile_snapshot(self.c,self.b,Mock(side_effect=OSError('SECRET')))
        self.assertEqual(health.load(self.temp.name)['events'][0]['code'],'failed')
    def test_health_detail_does_not_change_execution_or_call_broker(self):
        with self.assertRaises(OSError):journal.reconcile_snapshot(self.c,self.b,Mock(side_effect=OSError()))
        app=Dashboard.__new__(Dashboard);app.root=Mock();app.running=False;app.health_items={'row':health.load(self.temp.name)['events'][0]}
        table=Mock();table.selection.return_value=['row'];app.tables={'health':table}
        with patch('stockbot.gui.messagebox.showinfo') as info:self.assertEqual(app.show_health_detail(),'break')
        self.assertIn('상태는 바뀌지 않습니다',info.call_args.args[1]);self.assertFalse(app.running);self.assertEqual(len(self.b.sent),0)
