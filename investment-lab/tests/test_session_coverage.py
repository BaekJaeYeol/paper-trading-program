import datetime as dt
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from operational_audit import cadence_summary
from reliability import session_bounds

class CoverageTests(unittest.TestCase):
    def history(self,day='2026-10-15'):
        opening,closing=session_bounds(day)
        return [{'checked_utc':dt.datetime.fromtimestamp(t,dt.timezone.utc).isoformat()}
                for t in range(int(opening)+1320,int(closing)+421,900)]
    def test_full_day_and_duplicate(self):
        h=self.history()
        r=cadence_summary(h+h,'2026-10-15T21:00:00+00:00',session_bounds)
        self.assertEqual((r['due_slots'],r['recorded_slots'],r['pending_slots']),(26,26,0))
        self.assertEqual(r['missing_slots_utc'],[])
    def test_late_start_exposes_seven_missing_slots(self):
        h=self.history()[7:]
        r=cadence_summary(h,'2026-10-15T21:00:00+00:00',session_bounds)
        self.assertEqual(r['recorded_slots'],19)
        self.assertEqual(len(r['missing_slots_utc']),7)
        self.assertIn('주의',r['summary'])
    def test_grace_and_future_not_missing(self):
        r=cadence_summary([],'2026-10-15T13:53:00+00:00',session_bounds)
        self.assertEqual((r['due_slots'],r['pending_slots']),(0,26))
        h=[{'checked_utc':'2026-10-15T13:53:59+00:00'}]
        r=cadence_summary(h,'2026-10-15T13:54:00+00:00',session_bounds)
        self.assertEqual(r['recorded_slots'],1)
    def test_early_close_weekend_and_dst(self):
        h=self.history('2026-11-27')
        r=cadence_summary(h,'2026-11-28T20:00:00+00:00',session_bounds)
        self.assertEqual(r['session_date'],'2026-11-27')
        self.assertEqual(r['due_slots'],14)
        self.assertEqual(r['missing_slots_utc'],[])
        self.assertTrue(h[0]['checked_utc'].endswith('14:52:00+00:00'))
    def test_preopen_uses_previous_trading_day(self):
        r=cadence_summary(self.history(),'2026-10-16T12:00:00+00:00',session_bounds)
        self.assertEqual(r['session_date'],'2026-10-15')
        self.assertEqual(r['missing_slots_utc'],[])
