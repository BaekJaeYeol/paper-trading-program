"""Monotonic start-to-start cadence. Missed slots are skipped, never replayed."""
import math

class Cadence:
    def __init__(self,interval,now):
        if not math.isfinite(interval) or interval<=0 or not math.isfinite(now):raise ValueError('Invalid cadence')
        self.interval=interval;self.next_due=now;self.skipped=0
        self.last_started=None;self.last_duration=None;self.in_flight=False

    def claim(self,now):
        if self.in_flight or now<self.next_due:return False
        missed=max(0,math.floor((now-self.next_due)/self.interval))
        self.skipped+=missed;self.next_due+=(missed+1)*self.interval
        self.last_started=now;self.in_flight=True
        return True

    def complete(self,now):
        if not self.in_flight:return
        self.last_duration=max(0,now-self.last_started);self.in_flight=False
        # Avoid a near-immediate second cycle after a late callback/long operation.
        earliest=now+min(30,self.interval)
        if self.next_due<earliest:
            missed=math.ceil((earliest-self.next_due)/self.interval)
            self.skipped+=missed;self.next_due+=missed*self.interval

    def delay(self,now):return max(0,self.next_due-now)
