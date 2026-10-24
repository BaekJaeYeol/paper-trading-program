import json
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import Mock,patch
from stockbot import diagnostics
from stockbot.gui import Dashboard

class DiagnosticTests(unittest.TestCase):
    def sample(self):
        return {'account_fingerprint':'SECRET_ACCOUNT','api_key':'SECRET_KEY','orders':[{'id':'SECRET_ORDER'}],
                'reconciliation':{'checked':3,'unresolved':1,'legacy':0},
                'inventory':{'ready':False,'rows':[{'symbol':'SECRET_SYMBOL','expected':'SECRET_VALUE','matched':False}]},
                'review':{'blocking':1,'cases':[{'code':'order_replaced','active':True,'target':'SECRET_TARGET','expected':'SECRET_ORIGINAL','next_action':'SECRET_TEXT'}]}}
    def build(self,**kwargs):return diagnostics.build(self.sample(),age_seconds=kwargs.get('age',0),read_failed=kwargs.get('failed',False),stopped=True,running=False)
    def test_allowlist_excludes_sensitive_nested_data(self):
        report=self.build();self.assertNotIn('SECRET',json.dumps(report));self.assertEqual(report['review']['active_total'],1)
        self.assertEqual(report['review']['reasons'][0]['code'],'order_replaced')
        self.assertFalse(report['live_orders_enabled'])
    def test_stale_threshold_and_failure(self):
        self.assertFalse(self.build(age=59)['stale']);self.assertTrue(self.build(age=60)['stale'])
        self.assertTrue(self.build(failed=True)['stale']);self.assertTrue(self.build(age=None)['stale'])
    def test_invalid_counts_do_not_echo_strings(self):
        s=self.sample();s['reconciliation']['checked']='SECRET';s['review']['blocking']=True
        report=diagnostics.build(s,age_seconds=0,read_failed=False,stopped=False,running=False)
        self.assertIsNone(report['reconciliation']['checked']);self.assertIsNone(report['review']['active_total'])
    def test_atomic_failure_preserves_existing_file_and_cleans_temporary(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'report.json';path.write_text('original')
            with patch('stockbot.diagnostics.os.replace',side_effect=PermissionError):
                with self.assertRaises(OSError):diagnostics.write_report(path,self.build())
            self.assertEqual(path.read_text(),'original');self.assertEqual(list(Path(d).iterdir()),[path])
    def app(self,d):
        app=Dashboard.__new__(Dashboard);app.root=Mock();app.busy=False;app.running=False;app.account_error=True
        app.path=Path(d)/'config.json';app.config={'state_dir':str(Path(d)/'state')}
        Path(app.config['state_dir']).mkdir();Path(app.config['state_dir'],'STOP').touch()
        app.stop_event=threading.Event();app.diagnostic_snapshot=self.build();app.diagnostic_time=time.monotonic()-70
        return app
    def test_export_uses_cached_data_keeps_stop_and_marks_stale(self):
        with tempfile.TemporaryDirectory() as d:
            app=self.app(d);path=Path(d)/'export.json'
            with patch('stockbot.gui.filedialog.asksaveasfilename',return_value=str(path)),patch('stockbot.gui.messagebox.showinfo'):
                app.export_diagnostics()
            report=json.loads(path.read_text());self.assertTrue(report['stale']);self.assertTrue(report['stop_requested'])
            self.assertTrue(Path(d,'state','STOP').exists());self.assertFalse(app.running)
    def test_cancel_and_protected_paths_do_not_write(self):
        with tempfile.TemporaryDirectory() as d:
            app=self.app(d)
            for target in ('',str(app.path),str(Path(d)/'state'/'report.json'),str(Path(d)/'bad.sqlite')):
                with patch('stockbot.gui.filedialog.asksaveasfilename',return_value=target),patch('stockbot.gui.diagnostics.write_report') as write,patch('stockbot.gui.messagebox.showerror'):
                    app.export_diagnostics();write.assert_not_called()
    def test_no_snapshot_or_busy_never_opens_save_dialog(self):
        with tempfile.TemporaryDirectory() as d:
            app=self.app(d)
            for busy,snapshot in ((True,app.diagnostic_snapshot),(False,None)):
                app.busy=busy;app.diagnostic_snapshot=snapshot
                with patch('stockbot.gui.filedialog.asksaveasfilename') as choose,patch('stockbot.gui.messagebox.showinfo'):
                    app.export_diagnostics();choose.assert_not_called()
