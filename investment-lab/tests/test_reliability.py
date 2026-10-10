import sys,unittest,datetime as dt
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from reliability import session_bounds,freshness,advance_v2,next_schedule
class Reliability(unittest.TestCase):
    def rows(self,volume=1):
        return [(f'2026-10-09T{h}+00:00',100.,101.,99.,100.,volume) for h in ('13:30:00','13:45:00','14:00:00')]
    def test_calendar(self):
        self.assertIsNone(session_bounds('2026-07-03'))
        self.assertEqual(dt.datetime.fromtimestamp(session_bounds('2026-11-27')[1],dt.timezone.utc).hour,18)
        self.assertEqual(dt.datetime.fromtimestamp(session_bounds('2026-11-02')[0],dt.timezone.utc).hour,14)
    def test_partial_and_duplicate(self):
        rows=self.rows();a=advance_v2(None,rows[:1],[1],0)
        b=advance_v2(a,rows,[1,1,1],2000000000)
        self.assertEqual(b['events'][0]['status'],'partial')
        self.assertAlmostEqual(b['events'][0]['quantity'],.01)
        self.assertTrue(b['events'][0]['remainder_expired'])
        self.assertEqual(advance_v2(b,rows,[1,1,1],2000000001),b)
        altered=list(rows);altered[1]=(*rows[1][:5],1000000)
        changed=advance_v2(a,altered,[1,1,1],2000000000)
        self.assertEqual(changed['events'][0],b['events'][0])
    def test_zero_and_revision(self):
        rows=self.rows(0);a=advance_v2(None,rows[:1],[1],0)
        b=advance_v2(a,rows,[1,1,1],0)
        self.assertEqual(b['events'][0]['status'],'unfilled');self.assertEqual(b['cash'],10000)
        changed=list(rows);changed[0]=(*rows[0][:4],101.,0)
        with self.assertRaises(ValueError):advance_v2(a,changed,[1,1,1],0)
        self.assertEqual(a['cash'],10000)
    def test_freshness_and_schedule(self):
        now=dt.datetime.fromisoformat('2026-10-10T12:00:00+00:00').timestamp()
        rows=[('2026-10-09T19:45:00+00:00',1,1,1,1,1)]
        self.assertFalse(freshness(rows,now)['stale'])
        self.assertTrue(freshness(self.rows(),now)['stale'])
        self.assertTrue(next_schedule(now).startswith('2026-10-12'))
if __name__=='__main__':unittest.main()
