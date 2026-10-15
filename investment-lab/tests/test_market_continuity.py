import datetime as dt
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from market_continuity import validate_continuity

def stamp(text):return dt.datetime.fromisoformat(text).timestamp()
def bounds(day):
 if day.weekday()>4:return None
 opening=stamp(str(day)+'T13:30:00+00:00')
 return opening,opening+1800
def rows(*values):return [(v,100,100,100,100,1000) for v in values]

class ContinuityTests(unittest.TestCase):
 def test_weekend_is_not_a_gap(self):
  r=rows('2026-10-09T13:45:00+00:00','2026-10-12T13:30:00+00:00','2026-10-12T13:45:00+00:00')
  validate_continuity(r,r[0][0],bounds)
 def test_missing_next_session_open(self):
  r=rows('2026-10-09T13:45:00+00:00','2026-10-12T13:45:00+00:00')
  with self.assertRaisesRegex(ValueError,'2026-10-12T13:30'):validate_continuity(r,r[0][0],bounds)
 def test_missing_prior_session_close(self):
  r=rows('2026-10-09T13:30:00+00:00','2026-10-12T13:30:00+00:00')
  with self.assertRaisesRegex(ValueError,'2026-10-09T13:45'):validate_continuity(r,r[0][0],bounds)
 def test_missing_whole_trading_day(self):
  r=rows('2026-10-12T13:45:00+00:00','2026-10-14T13:30:00+00:00')
  with self.assertRaisesRegex(ValueError,'2026-10-13'):validate_continuity(r,r[0][0],bounds)
 def test_holiday_and_early_close(self):
  r=rows('2026-10-12T13:30:00+00:00','2026-10-14T13:30:00+00:00')
  def calendar(day):
   if str(day)=='2026-10-13':return None
   value=bounds(day)
   return value[0],value[0]+900
  validate_continuity(r,r[0][0],calendar)
 def test_missing_anchor(self):
  r=rows('2026-10-12T13:45:00+00:00')
  with self.assertRaisesRegex(ValueError,'기준 봉 누락'):validate_continuity(r,'2026-10-12T13:30:00+00:00',bounds)
