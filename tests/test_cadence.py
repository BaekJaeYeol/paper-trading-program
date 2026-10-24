import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import Mock,patch
from stockbot.cadence import Cadence
from stockbot.gui import Dashboard
from stockbot import cli
import test_ui_safety

class CadenceTests(unittest.TestCase):
    def test_first_cycle_immediate_and_work_time_does_not_add_to_interval(self):
        c=Cadence(300,100);self.assertTrue(c.claim(100));c.complete(140)
        self.assertEqual(c.next_due,400);self.assertEqual(c.delay(140),260)
        self.assertEqual(c.last_duration,40);self.assertEqual(c.skipped,0)
    def test_early_or_overlapping_claim_is_rejected(self):
        c=Cadence(300,0);self.assertFalse(c.claim(-1));self.assertTrue(c.claim(0))
        self.assertFalse(c.claim(1000));c.complete(40);self.assertFalse(c.claim(299))
    def test_long_work_skips_slots_without_burst(self):
        c=Cadence(300,0);c.claim(0);c.complete(950)
        self.assertEqual(c.next_due,1200);self.assertEqual(c.skipped,3)
        self.assertFalse(c.claim(951));self.assertTrue(c.claim(1200))
    def test_late_wakeup_executes_one_current_slot(self):
        c=Cadence(300,0);self.assertTrue(c.claim(3600));self.assertEqual(c.skipped,12)
        self.assertFalse(c.claim(3601));c.complete(3610)
        self.assertEqual(c.next_due,3900);self.assertEqual(c.skipped,12)
    def test_near_boundary_completion_has_at_least_30_seconds_rest(self):
        c=Cadence(300,0);c.claim(299);c.complete(299)
        self.assertEqual(c.next_due,600);self.assertEqual(c.skipped,1)
        c=Cadence(300,0);c.claim(0);c.complete(270)
        self.assertEqual(c.next_due,300);self.assertEqual(c.skipped,0)
    def test_invalid_interval(self):
        for interval in (0,-1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):Cadence(interval,0)
    def test_gui_early_callback_and_busy_retry_do_not_claim(self):
        app=Dashboard.__new__(Dashboard);app.running=True;app.root=Mock();app.root.after.return_value='timer';app.timer=None
        app.cadence=Cadence(300,300);app.work=Mock();app.busy=True
        with patch('stockbot.gui.time.monotonic',return_value=100):app.trade()
        self.assertIsNone(app.cadence.last_started);app.work.assert_not_called()
        app.busy=False
        with patch('stockbot.gui.time.monotonic',return_value=100):app.trade()
        app.work.assert_not_called();self.assertEqual(app.root.after.call_args.args[0],200000)
    def test_gui_stop_cancels_timer_and_stale_callback_cannot_trade(self):
        with tempfile.TemporaryDirectory() as d:
            app=test_ui_safety.SafetyTests().fake_dashboard(d);app.cadence=Cadence(300,0);app.running=True
            app.work=Mock();app.timer='scheduled';app.stop();app.trade()
            app.work.assert_not_called();self.assertFalse(app.running);self.assertTrue(Path(d,'STOP').exists())
    def test_cli_uses_start_cadence_and_skips_long_cycle(self):
        clock={'now':0};starts=[];sleeps=[]
        def cycle(*args):
            starts.append(clock['now'])
            if len(starts)==3:raise KeyboardInterrupt
            clock['now']+=40 if len(starts)==1 else 640
            return {'status':'ok','orders':[]}
        def sleep(delay):sleeps.append(delay);clock['now']+=delay
        fake_time=Mock(monotonic=lambda:clock['now'],sleep=sleep)
        snapshot={'reconciliation':{'unresolved':0},'inventory':{'ready':True}}
        with patch.object(cli,'time',fake_time),patch.object(cli,'load_config',return_value={}),patch.object(cli,'AlpacaPaper'),patch.object(cli,'cycle',side_effect=cycle),patch('stockbot.paper_journal.reconcile_snapshot',return_value=snapshot),patch('sys.argv',['stockbot','run','--execute-paper','--interval','300']),redirect_stdout(io.StringIO()):
            with self.assertRaises(KeyboardInterrupt):cli.main()
        self.assertEqual(starts,[0,300,1200]);self.assertEqual(sleeps,[260,260])
