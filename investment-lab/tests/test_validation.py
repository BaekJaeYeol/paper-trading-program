import tempfile
import unittest
from pathlib import Path
from engine import load
from validation import walk_forward, batch_validate, Fleet

ROOT=Path(__file__).resolve().parents[1]

class ValidationTests(unittest.TestCase):
    def test_selection_does_not_see_future(self):
        rows=load(ROOT/'demo_synthetic.csv')
        first=walk_forward(rows)
        boundary=313
        altered=list(rows)
        for i in range(boundary,len(rows)):
            r=rows[i];altered[i]=(r[0],*(x*2 for x in r[1:5]),r[5])
        second=walk_forward(altered)
        self.assertEqual([r['strategy'] for r in first if r['test_start']==rows[boundary][0] and r['selected']],
                         [r['strategy'] for r in second if r['test_start']==rows[boundary][0] and r['selected']])
        starts=sorted(set(r['test_start'] for r in first))
        self.assertEqual(len(first),len(starts)*27)
        for row in first:self.assertLess(row['train_end'],row['test_start'])
    def test_fleet_restart_and_isolation(self):
        rows=load(ROOT/'demo_synthetic.csv')
        with tempfile.TemporaryDirectory() as d:
            fleet=Fleet(d);fleet.update('SPY',rows[:-1]);one=fleet.update('SPY',rows);two=Fleet(d).update('SPY',rows)
            self.assertEqual(one,two)
            self.assertEqual(len(one),27)
            self.assertEqual(one['cash']['qty'],0)
            self.assertGreater(one['buy_hold']['qty'],0)
    def test_partial_failure(self):
        with tempfile.TemporaryDirectory() as d:
            report=batch_validate({'demo':ROOT/'demo_synthetic.csv','bad':Path(d)/'missing'},d,'synthetic')
            self.assertTrue(report['results']);self.assertIn('bad',report['errors']);self.assertFalse(report['live_ready'])

class LifecycleTests(unittest.TestCase):
    def test_stop_blocks_delayed_callback(self):
        from app import App
        from unittest.mock import Mock
        app=App.__new__(App)
        app.root=Mock();app.lab_info=Mock();app.status=Mock()
        app.running=True;app.timer=None;app.fleet_timer='pending'
        app.fleet_running=True;app.fleet_generation=1
        app.stop()
        app.show_fleet('SPY',{},1)
        app.fleet_auto()
        app.root.after.assert_not_called()
        app.root.after_cancel.assert_called_once_with('pending')
    def test_download_error_saved(self):
        import json
        with tempfile.TemporaryDirectory() as d:
            batch_validate({},d,'real_download',errors={'SPY':'download failed'})
            self.assertEqual(json.loads((Path(d)/'validation.json').read_text())['errors']['SPY'],'download failed')
