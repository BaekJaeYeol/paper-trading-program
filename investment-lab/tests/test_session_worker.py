import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from session_worker import next_poll,run_session

class SessionTests(unittest.TestCase):
 def run_fake(self,start=420,window=(0,20000),duration=1850,once=False,stop_at=None):
  now=[float(start)];ticks=[];saves=[];refreshes=[]
  def tick():
   ticks.append(now[0]);now[0]+=20
   return {'symbols':{'SPY':{'status':'ok'}}}
  def save():saves.append(now[0])
  def refresh():refreshes.append(now[0])
  def sleep(seconds):now[0]+=seconds
  result=run_session(tick,save,refresh,lambda _:window,max_seconds=duration,once=once,
                     clock=lambda:now[0],sleep=sleep,stopped=lambda:stop_at is not None and now[0]>=stop_at)
  return result,ticks,saves,now[0]
 def test_next_slot(self):
  self.assertEqual(next_poll(420),1320)
  self.assertEqual(next_poll(1319),1320)
 def test_900_seconds_without_collection_drift(self):
  result,ticks,saves,end=self.run_fake()
  self.assertEqual(ticks,[420,1320,2220]);self.assertEqual(len(saves),3)
  self.assertEqual(result,(0,3));self.assertEqual(end,2270)
 def test_holiday_and_close_skip(self):
  self.assertEqual(self.run_fake(window=None)[1],[])
  self.assertEqual(self.run_fake(start=30000,window=(0,100))[1],[])
 def test_once_preserves_manual_execution(self):
  self.assertEqual(len(self.run_fake(window=None,once=True)[1]),1)
 def test_emergency_stop_observed_during_wait(self):
  result,ticks,saves,end=self.run_fake(stop_at=500)
  self.assertEqual(len(ticks),2);self.assertEqual(len(saves),2)
  self.assertLess(end,1320)
 def test_persistence_failure_stops_session(self):
  def fail():raise RuntimeError('disk/push failure')
  with self.assertRaises(RuntimeError):
   run_session(lambda:{'symbols':{}},fail,lambda:None,lambda _:(0,1),once=True)
if __name__=='__main__':unittest.main()
