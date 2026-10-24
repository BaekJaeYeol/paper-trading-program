import queue
import sqlite3
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import patch
from stockbot.cli import cycle,load_config
from stockbot.gui import Dashboard,account_view
from stockbot.ui_safety import order_row,unresolved_attempts,resume_snapshot
from test_bot import FakeBroker
from test_gui import FakeAccount
ROOT=Path(__file__).resolve().parents[1]
class Var:
    def __init__(self,v=''):self.value=v
    def set(self,v):self.value=v
    def get(self):return self.value
class Selector:
    def configure(self,**kwargs):pass
class Root:
    def after(self,*args):return 'timer'
    def after_cancel(self,*args):pass

class SafetyTests(unittest.TestCase):
    def test_partial_and_cancel_states_are_distinct(self):
        base={'symbol':'AAPL','side':'buy','qty':'10','filled_qty':'3','limit_price':'100','status':'partially_filled'}
        row=order_row(base);self.assertEqual(row[4],'7');self.assertEqual(row[-1],'부분 체결')
        self.assertEqual(order_row(dict(base,status='pending_cancel'))[-1],'취소 요청 중')
        self.assertEqual(order_row(dict(base,status='canceled'))[-1],'취소 완료')
        self.assertIn('미확인',order_row(dict(base,status='arbitrary-secret'))[-1])
        self.assertNotIn('arbitrary-secret',str(order_row(dict(base,status='arbitrary-secret'))))
    def test_invalid_order_cannot_reach_gui(self):
        for filled in ['11','-1','NaN','Infinity']:
            with self.assertRaises(ValueError):order_row({'qty':'10','filled_qty':filled})
        b=FakeAccount();old=b.request
        def request(path,params=None):
            r=old(path,params)
            if path=='/v2/orders':r[0]['filled_qty']='NaN'
            return r
        b.request=request
        with self.assertRaises(ValueError):account_view(b)
    def test_unknown_blocks_other_symbols_and_resume(self):
        with tempfile.TemporaryDirectory() as tmp:
            c=load_config(ROOT/'config.json');c.update(state_dir=tmp,symbols=['AAPL'])
            b=FakeBroker(True)
            with self.assertRaises(RuntimeError):cycle(c,True,b)
            c['symbols']=['MSFT']
            with self.assertRaises(RuntimeError):cycle(c,True,b)
            self.assertEqual(len(b.sent),1)
            from stockbot.paper_journal import fingerprint
            snapshot={'can_trade':True,'request_seconds':1,'account_fingerprint':fingerprint({'id':'offline-paper'}),'orders':[]}
            with self.assertRaises(RuntimeError):resume_snapshot(c,b,lambda b:snapshot)
            self.assertEqual(len(unresolved_attempts(tmp)),1)
            self.assertFalse(Path(tmp,'cycle.lock').exists())
    def test_memory_stop_blocks_even_without_stop_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            e=threading.Event();e.set();c=load_config(ROOT/'config.json');c.update(state_dir=tmp,_stop_event=e)
            b=FakeBroker();self.assertEqual(cycle(c,True,b)['status'],'halted');self.assertEqual(b.sent,[])
    def test_resume_read_only_and_leaves_stop(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp,'STOP').touch();b=FakeAccount();old=b.request
            def request(path,params=None):
                r=old(path,params)
                if path=='/v2/account':r['status']='ACTIVE'
                return r
            b.request=request
            r=resume_snapshot({'state_dir':tmp},b,account_view)
            self.assertTrue(r['can_trade']);self.assertTrue(Path(tmp,'STOP').exists())
            self.assertFalse(Path(tmp,'cycle.lock').exists())
    def test_resume_rejects_delay_and_incomplete_permissions(self):
        with tempfile.TemporaryDirectory() as tmp:
            for data in [{'can_trade':False,'request_seconds':1,'orders':[]},{'can_trade':True,'request_seconds':61,'orders':[]}]:
                with self.assertRaises(ValueError):resume_snapshot({'state_dir':tmp},None,lambda b:data)
    def fake_dashboard(self,tmp):
        d=Dashboard.__new__(Dashboard);d.config={'state_dir':tmp};d.busy=False;d.running=False;d.timer=None;d.closed=False
        d.root=Root();d.selector=Selector();d.market=Var('미국 · Alpaca');d.status=Var();d.context=Var();d.freshness=Var()
        d.stop_event=threading.Event();d.resume_pending=False;d.stop_failed=False;d.account_error=False
        d.last_account_time=time.monotonic()-61;d.last_account_label='2026-10-24T20:00:00+09:00'
        d.actions=[];d.events=queue.Queue();d.values={};d.fill=lambda *args:None;d.order_notice=Var();d.write=lambda *args:None
        return d
    def test_late_account_response_cannot_overwrite_stop(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=self.fake_dashboard(tmp);d.stop()
            d.events.put(('account',account_view(FakeAccount()),None));d.poll()
            self.assertIn('비상 중단',d.status.get());self.assertFalse(d.running)
            self.assertTrue(d.stop_event.is_set())
    def test_stale_indicator_and_stop_write_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=self.fake_dashboard(tmp);d.update_safety_display();self.assertIn('오래된',d.freshness.get())
            with patch.object(Path,'touch',side_effect=PermissionError()):d.stop()
            self.assertIn('기록 실패',d.status.get());self.assertTrue(d.stop_event.is_set())
            self.assertFalse(Path(tmp,'STOP').exists())
    def test_stop_during_resume_prevents_restart(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=self.fake_dashboard(tmp);d.resume_pending=True;d.stop()
            d.finish_resume({'received_at':'test'})
            self.assertFalse(d.running);self.assertTrue(Path(tmp,'STOP').exists())

    def test_delayed_resume_response_is_not_used(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=self.fake_dashboard(tmp);d.resume_pending=True
            d.finish_resume({'received_at':'test','received_monotonic':time.monotonic()-61})
            self.assertFalse(d.running);self.assertIn('재개 차단',d.order_notice.get())
