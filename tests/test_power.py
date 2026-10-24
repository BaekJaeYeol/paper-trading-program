import io
import sys
import tempfile
import threading
import time
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import Mock,patch
from stockbot.power import SleepGuard,ES_CONTINUOUS,ES_SYSTEM_REQUIRED
from stockbot import cli
import test_ui_safety

class PowerTests(unittest.TestCase):
    def test_flags_and_previous_thread_state_restored(self):
        native=Mock(side_effect=[ES_CONTINUOUS|2,ES_CONTINUOUS|ES_SYSTEM_REQUIRED])
        g=SleepGuard(platform='win32',native=native)
        self.assertTrue(g.acquire());self.assertTrue(g.acquire());self.assertTrue(g.active)
        self.assertEqual(native.call_count,1);self.assertTrue(g.release());self.assertTrue(g.release())
        self.assertEqual([c.args[0] for c in native.call_args_list],[ES_CONTINUOUS|ES_SYSTEM_REQUIRED,ES_CONTINUOUS|2])
        self.assertFalse(g.active)
    def test_acquire_failure_does_not_claim_active(self):
        for native in (Mock(return_value=0),Mock(side_effect=OSError('SECRET'))):
            g=SleepGuard(platform='win32',native=native)
            self.assertFalse(g.acquire());self.assertFalse(g.active);self.assertTrue(g.release())
            self.assertNotIn('SECRET',g.label());self.assertEqual(g.error,'acquire')
    def test_release_failure_retains_truth_and_can_retry(self):
        g=SleepGuard(platform='win32',native=Mock(side_effect=[ES_CONTINUOUS,0,ES_CONTINUOUS]))
        self.assertTrue(g.acquire());self.assertFalse(g.release());self.assertTrue(g.active)
        self.assertIn('해제 실패',g.label());self.assertTrue(g.release());self.assertFalse(g.active)
    def test_cross_thread_release_is_rejected_without_native_call(self):
        native=Mock(return_value=ES_CONTINUOUS);g=SleepGuard(platform='win32',native=native);g.acquire()
        results=[];thread=threading.Thread(target=lambda:results.append(g.release()));thread.start();thread.join()
        self.assertEqual(results,[False]);self.assertEqual(native.call_count,1);self.assertTrue(g.active);g.release()
    def test_non_windows_no_native_calls_or_false_active_claim(self):
        native=Mock();g=SleepGuard(platform='linux',native=native)
        self.assertTrue(g.acquire());self.assertTrue(g.release());self.assertFalse(g.active)
        self.assertIn('미지원',g.label());native.assert_not_called()
    def test_gui_failure_keeps_stop_and_never_trades(self):
        with tempfile.TemporaryDirectory() as d:
            app=test_ui_safety.SafetyTests().fake_dashboard(d);app.sleep_guard=Mock();app.sleep_guard.acquire.return_value=False
            app.resume_pending=True;app.trade=Mock();Path(d,'STOP').touch()
            with patch('stockbot.gui.messagebox.askyesno',return_value=True):app.finish_resume({'received_monotonic':time.monotonic()})
            app.trade.assert_not_called();self.assertFalse(app.running);self.assertTrue(Path(d,'STOP').exists())
            self.assertIn('절전 방지 요청 실패',app.status.get())
    def test_gui_pause_defers_release_until_worker_finishes(self):
        with tempfile.TemporaryDirectory() as d:
            app=test_ui_safety.SafetyTests().fake_dashboard(d);g=SleepGuard(platform='win32',native=Mock(return_value=ES_CONTINUOUS));g.acquire();app.sleep_guard=g
            app.busy=True;app.running=True;app.pause();self.assertTrue(g.active)
            app.events.put(('account',None,True));app.poll();self.assertFalse(g.active)
    def test_gui_stop_unlink_failure_releases_request(self):
        with tempfile.TemporaryDirectory() as d:
            app=test_ui_safety.SafetyTests().fake_dashboard(d);g=SleepGuard(platform='win32',native=Mock(return_value=ES_CONTINUOUS));app.sleep_guard=g
            app.resume_pending=True;app.trade=Mock();Path(d,'STOP').touch()
            with patch('stockbot.gui.messagebox.askyesno',return_value=True),patch.object(Path,'unlink',side_effect=PermissionError):
                app.finish_resume({'received_monotonic':time.monotonic()})
            self.assertFalse(g.active);self.assertTrue(Path(d,'STOP').exists());app.trade.assert_not_called()
    def invoke_cli(self,d,g,cycle):
        with patch.object(cli,'SleepGuard',return_value=g),patch.object(cli,'load_config',return_value={'state_dir':d}),patch.object(cli,'AlpacaPaper'),patch.object(cli,'cycle',side_effect=cycle) as orders,patch('stockbot.paper_journal.reconcile_snapshot',return_value={'reconciliation':{'unresolved':0},'inventory':{'ready':True}}),patch('sys.argv',['stockbot','run','--execute-paper']),redirect_stdout(io.StringIO()):
            with self.assertRaises((KeyboardInterrupt,SystemExit)):cli.main()
        return orders
    def test_cli_failure_blocks_before_cycle_and_releases_on_interrupt(self):
        with tempfile.TemporaryDirectory() as d:
            g=SleepGuard(platform='win32',native=Mock(return_value=0));orders=self.invoke_cli(d,g,KeyboardInterrupt())
            orders.assert_not_called()
            g=SleepGuard(platform='win32',native=Mock(return_value=ES_CONTINUOUS));self.invoke_cli(d,g,KeyboardInterrupt())
            self.assertFalse(g.active);self.assertEqual(g.native.call_count,2)
    def test_cli_existing_stop_does_not_acquire(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d,'STOP').touch();native=Mock();g=SleepGuard(platform='win32',native=native)
            orders=self.invoke_cli(d,g,KeyboardInterrupt());orders.assert_not_called();native.assert_not_called()
    def test_cli_wait_detects_external_stop_within_poll_interval(self):
        with tempfile.TemporaryDirectory() as d:
            clock={'now':0};delays=[]
            def sleep(delay):clock['now']+=delay;delays.append(delay);Path(d,'STOP').touch()
            with patch.object(cli,'time',Mock(monotonic=lambda:clock['now'],sleep=sleep)):
                with self.assertRaises(SystemExit):cli.wait_for_run({'state_dir':d},300)
            self.assertEqual(delays,[5])
    @unittest.skipUnless(sys.platform=='win32','Real Windows API required')
    def test_real_windows_thread_request_and_restore(self):
        g=SleepGuard();self.assertTrue(g.acquire())
        try:
            # Observe and immediately restore this test thread's actual execution state.
            previous=g.native(ES_CONTINUOUS)
            self.assertTrue(previous & ES_SYSTEM_REQUIRED)
            self.assertTrue(g.native(previous|ES_CONTINUOUS))
        finally:self.assertTrue(g.release())
        previous=g.native(ES_CONTINUOUS)
        try:self.assertEqual(previous,g.previous|ES_CONTINUOUS)
        finally:g.native(previous|ES_CONTINUOUS)
