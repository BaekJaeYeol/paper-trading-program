import tempfile
import unittest
from datetime import date,timedelta
from pathlib import Path
from unittest.mock import Mock,patch
from types import SimpleNamespace
from stockbot.broker import AlpacaPaper
from stockbot.sessions import describe
from stockbot.cadence import Cadence
from stockbot.cli import cycle,load_config
from test_bot import FakeBroker
ROOT=Path(__file__).resolve().parents[1]

def calendar(first='2026-10-02',last='2026-10-12',closed=(),early=()):
    start=date.fromisoformat(first);end=date.fromisoformat(last)
    return [{'date':str(start+timedelta(days=i)),'open':'09:30','close':'13:00' if str(start+timedelta(days=i)) in early else '16:00'} for i in range((end-start).days+1) if (start+timedelta(days=i)).weekday()<5 and str(start+timedelta(days=i)) not in closed]

class SessionTests(unittest.TestCase):
    def session(self,stamp,opened=False,cal=None):return describe({'timestamp':stamp,'is_open':opened},calendar() if cal is None else cal)
    def test_regular_pre_post_and_overnight_are_distinct(self):
        for stamp,opened,code in [('2026-10-05T12:00:00Z',False,'pre'),('2026-10-05T14:00:00Z',True,'regular'),('2026-10-05T21:00:00Z',False,'post'),('2026-10-06T01:00:00Z',False,'overnight_unverified')]:
            result=self.session(stamp,opened);self.assertEqual(result['code'],code)
            self.assertEqual(result['new_orders_allowed'],code=='regular');self.assertFalse(result['extended_orders_enabled'])
    def test_weekend_and_sunday_evening_not_24_7_market(self):
        self.assertEqual(self.session('2026-10-03T15:00:00Z')['code'],'closed')
        self.assertEqual(self.session('2026-10-04T23:59:59Z')['code'],'closed')
        self.assertEqual(self.session('2026-10-05T00:00:00Z')['code'],'overnight_unverified')
        self.assertEqual(self.session('2026-10-03T00:00:00Z')['code'],'closed')
    def test_holiday_eve_no_overnight_window(self):
        cal=calendar(closed=('2026-10-05',))
        self.assertEqual(self.session('2026-10-05T01:00:00Z',cal=cal)['code'],'closed')
        self.assertEqual(self.session('2026-10-05T15:00:00Z',cal=cal)['code'],'closed')
    def test_early_close_does_not_assume_after_hours_schedule(self):
        cal=calendar(early=('2026-10-05',))
        self.assertEqual(self.session('2026-10-05T18:00:00Z',cal=cal)['code'],'early_close_wait')
    def test_dst_conversion_next_open_in_kst(self):
        summer=self.session('2026-10-04T15:00:00Z')
        winter=self.session('2026-11-01T15:00:00Z',cal=calendar('2026-10-30','2026-11-06'))
        self.assertIn('T22:30:00+09:00',summer['next_regular_open_kst'])
        self.assertIn('T23:30:00+09:00',winter['next_regular_open_kst'])
    def test_clock_mismatch_and_missing_calendar_do_not_authorize_order(self):
        self.assertEqual(self.session('2026-10-05T14:00:00Z',False)['code'],'clock_mismatch')
        self.assertFalse(self.session('2026-10-05T14:00:00Z',True,[])['new_orders_allowed'])
        with self.assertRaises(ValueError):self.session('2026-10-05T14:00:00')
    def test_pre_and_post_engine_make_no_account_or_order_calls(self):
        with tempfile.TemporaryDirectory() as d:
            config=load_config(ROOT/'config.json');config['state_dir']=d
            for stamp in ('2026-10-05T12:00:00Z','2026-10-05T21:00:00Z','2026-10-06T01:00:00Z'):
                broker=Mock()
                def request(path,params=None,body=None):
                    if path=='/v2/clock':return {'timestamp':stamp,'is_open':False}
                    if path=='/v2/calendar':return calendar()
                    raise AssertionError('No account/quote/order activity outside regular bracket scope')
                broker.request.side_effect=request
                result=cycle(config,True,broker)
                self.assertEqual(result['status'],'market_closed');self.assertEqual(result['next_poll_seconds'],60)
                broker.quote.assert_not_called();broker.bars.assert_not_called()
                self.assertFalse(Path(d,'orders.sqlite').exists())
    def test_regular_to_waiting_and_back_rebases_without_backlog(self):
        c=Cadence(300,0);c.claim(0);c.set_interval(60);c.complete(10)
        self.assertEqual(c.next_due,60)
        self.assertTrue(c.claim(60));c.set_interval(300);c.complete(70)
        self.assertEqual(c.next_due,360)
    def test_close_between_quote_and_post_prevents_submission(self):
        with tempfile.TemporaryDirectory() as d:
            config=load_config(ROOT/'config.json');config.update(state_dir=d,symbols=['AAPL']);broker=FakeBroker();old=broker.request;clocks=[]
            def request(path,params=None,body=None):
                if path=='/v2/clock':
                    clocks.append(1)
                    return {'timestamp':'2026-10-05T14:00:00Z','is_open':True} if len(clocks)<3 else {'timestamp':'2026-10-05T21:00:00Z','is_open':False}
                return old(path,params,body)
            broker.request=request;result=cycle(config,True,broker)
            self.assertEqual(result['status'],'market_closed');self.assertEqual(broker.sent,[])
    def test_quote_that_ages_before_post_is_not_submitted(self):
        with tempfile.TemporaryDirectory() as d:
            config=load_config(ROOT/'config.json');config.update(state_dir=d,symbols=['AAPL']);broker=FakeBroker();old=broker.request;clocks=[]
            def request(path,params=None,body=None):
                if path=='/v2/clock':
                    clocks.append(1);return {'timestamp':'2026-10-05T14:00:00Z' if len(clocks)<3 else '2026-10-05T14:03:00Z','is_open':True}
                return old(path,params,body)
            broker.request=request;cycle(config,True,broker);self.assertEqual(broker.sent,[])
    def test_regular_engine_preserves_bracket_not_extended_flag(self):
        with tempfile.TemporaryDirectory() as d:
            config=load_config(ROOT/'config.json');config.update(state_dir=d,symbols=['AAPL']);broker=FakeBroker()
            result=cycle(config,True,broker)
            self.assertEqual(result['market_session']['code'],'regular');self.assertEqual(len(broker.sent),1)
            self.assertNotIn('extended_hours',broker.sent[0]);self.assertEqual(broker.sent[0]['order_class'],'bracket')

class DailyLookupBoundsTests(unittest.TestCase):
    def broker(self,responses):
        b=AlpacaPaper.__new__(AlpacaPaper);b.request=Mock(side_effect=responses);return b
    def test_repeated_token_cannot_loop_forever(self):
        b=self.broker([{'bars':[],'next_page_token':'repeat'}]*2)
        with self.assertRaises(RuntimeError):b.bars('AAPL','2026-01-01','2026-10-01','iex')
        self.assertEqual(b.request.call_count,2)
    def test_unique_tokens_still_have_page_cap(self):
        b=self.broker([{'bars':[],'next_page_token':str(i)} for i in range(11)])
        with self.assertRaises(RuntimeError):b.bars('AAPL','2026-01-01','2026-10-01','iex')
        self.assertEqual(b.request.call_count,10)
    def test_time_budget_stops_after_current_request(self):
        clock=[0];b=self.broker([])
        def request(*args,**kw):clock[0]=61;return {'bars':[],'next_page_token':'next'}
        b.request=Mock(side_effect=request)
        with patch('stockbot.broker.time',SimpleNamespace(monotonic=lambda:clock[0])):
            with self.assertRaises(RuntimeError):b.bars('AAPL','2026-01-01','2026-10-01','iex')
        self.assertEqual(b.request.call_count,1)
