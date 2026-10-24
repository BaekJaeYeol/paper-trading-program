import copy
import io
import json
import os
import sqlite3
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from stockbot.broker import AlpacaPaper,AlpacaHTTPError
from stockbot.cli import cycle,load_config
from stockbot.paper_journal import account_snapshot,reconcile_snapshot,fingerprint
from stockbot.ui_safety import resume_snapshot,unresolved_attempts
from test_bot import FakeBroker
ROOT=Path(__file__).resolve().parents[1]

class TrackingBroker(FakeBroker):
    def __init__(self):
        super().__init__();self.orders={};self.lookups=[];self.fail_after_accept=False;self.lookup_error=False;self.account_id='offline-paper'
    def request(self,path,params=None,body=None):
        if path=='/v2/orders:by_client_order_id':
            self.lookups.append(params['client_order_id'])
            if self.lookup_error:raise TimeoutError('do-not-log-secret')
            if params['client_order_id'] not in self.orders:raise AlpacaHTTPError(404)
            return copy.deepcopy(self.orders[params['client_order_id']])
        if path=='/v2/orders' and body is not None:
            self.sent.append(copy.deepcopy(body));bid='broker-'+str(len(self.sent));cid=body['client_order_id']
            order={**body,'id':bid,'filled_qty':'0','status':'new'};self.orders[cid]=order
            if self.fail_after_accept:raise TimeoutError('accepted but response lost')
            return copy.deepcopy(order)
        if path=='/v2/orders' and body is None:
            return [copy.deepcopy(o) for o in self.orders.values() if o['status'] not in ('filled','canceled','rejected','expired','replaced')]
        if path=='/v2/positions':
            return [{'symbol':o['symbol'],'qty':o['filled_qty'],'avg_entry_price':o['limit_price'],'current_price':o['limit_price'],'unrealized_pl':'0'} for o in self.orders.values() if float(o['filled_qty'])>0]
        r=super().request(path,params,body)
        if path=='/v2/account':r.update(id=self.account_id,cash='8000')
        return r
    def find_order(self,cid):return AlpacaPaper.find_order(self,cid)

class JournalTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.c=load_config(ROOT/'config.json');self.c.update(state_dir=self.temp.name,symbols=['AAPL'])
        self.b=TrackingBroker()
    def check(self):return reconcile_snapshot(self.c,self.b,account_snapshot)
    def submit(self):
        cycle(self.c,True,self.b)
        return next(iter(self.b.orders))
    def test_timeout_found_after_restart_and_never_reposted(self):
        self.b.fail_after_accept=True
        with self.assertRaises(RuntimeError):cycle(self.c,True,self.b)
        self.assertEqual(len(unresolved_attempts(self.temp.name)),1)
        self.b.fail_after_accept=False
        cid=next(iter(self.b.orders));self.b.orders[cid].update(status='partially_filled',filled_qty='1')
        Path(self.temp.name,'STOP').touch()
        data=self.check()
        self.assertEqual(data['reconciliation']['unresolved'],0)
        self.assertEqual(data['order_history'][0]['status'],'부분 체결')
        self.assertTrue(Path(self.temp.name,'STOP').exists());self.assertEqual(len(self.b.sent),1)
        # Resume check itself never removes STOP or posts.
        resume_snapshot(self.c,self.b,account_snapshot)
        Path(self.temp.name,'STOP').unlink();cycle(self.c,True,self.b)
        self.assertEqual(len(self.b.sent),1)
        self.assertIn('주문 응답 미확인',[e['kind'] for e in data['order_events']])
    def test_missing_order_stays_unknown_without_resubmit(self):
        cid=self.submit();self.b.orders.clear()
        data=self.check();self.assertEqual(data['reconciliation']['unresolved'],1)
        self.assertEqual(data['order_history'][0]['status'],'조회 결과 없음')
        self.c['symbols']=['MSFT']
        with self.assertRaises(RuntimeError):cycle(self.c,True,self.b)
        self.assertEqual(len(self.b.sent),1)
    def test_read_timeout_stays_unknown_and_redacts_exception(self):
        self.submit();self.b.lookup_error=True
        data=self.check();self.assertEqual(data['reconciliation']['unresolved'],1)
        self.assertNotIn('do-not-log-secret',str(data))
        with self.assertRaises(RuntimeError):resume_snapshot(self.c,self.b,account_snapshot)
    def test_account_swap_blocked_before_lookup_or_new_post(self):
        self.submit();self.b.account_id='another-account'
        with self.assertRaises(ValueError):self.check()
        self.assertEqual(self.b.lookups,[])
        self.c['symbols']=['MSFT']
        with self.assertRaises(ValueError):cycle(self.c,True,self.b)
        self.assertEqual(len(self.b.sent),1)
    def test_order_mismatch_is_not_confirmed(self):
        mutations=[{'symbol':'MSFT'},{'qty':'999'},{'side':'sell'},{'client_order_id':'wrong'},{'id':'wrong'},{'limit_price':'999'},{'status':'unknown-new-status'}]
        cid=self.submit();original=copy.deepcopy(self.b.orders[cid])
        for mutation in mutations:
            self.b.orders[cid]={**original,**mutation}
            data=self.check();self.assertEqual(data['reconciliation']['unresolved'],1,mutation)
            self.assertIn('불일치',data['order_history'][0]['status'])
        self.assertEqual(len(self.b.sent),1)
    def test_invalid_snapshot_blocks_resume_without_post(self):
        cid=self.submit();self.b.orders[cid]['filled_qty']='NaN'
        with self.assertRaises(ValueError):resume_snapshot(self.c,self.b,account_snapshot)
        self.assertEqual(len(self.b.sent),1)
    def test_partial_fills_monotonic_and_final_cancellation(self):
        cid=self.submit();self.b.orders[cid].update(status='partially_filled',filled_qty='2')
        self.check();self.b.orders[cid]['filled_qty']='1'
        self.assertEqual(self.check()['reconciliation']['unresolved'],1)
        self.b.orders[cid].update(status='pending_cancel',filled_qty='2')
        self.assertEqual(self.check()['order_history'][0]['status'],'취소 요청 중')
        self.b.orders[cid]['status']='canceled';data=self.check()
        self.assertEqual(data['order_history'][0]['filled_qty'],'2')
        self.assertEqual(data['order_history'][0]['status'],'취소 완료')
        before=len(self.b.lookups);self.check();self.assertEqual(len(self.b.lookups),before)
    def test_repeated_unchanged_query_does_not_duplicate_event(self):
        self.submit();one=self.check();two=self.check()
        self.assertEqual(len(one['order_events']),len(two['order_events']))
    def test_legacy_unknown_cannot_be_auto_resolved(self):
        path=Path(self.temp.name,'orders.sqlite')
        with sqlite3.connect(path) as db:
            db.execute('CREATE TABLE attempts(id TEXT PRIMARY KEY,status TEXT NOT NULL)');db.execute("INSERT INTO attempts VALUES ('legacy','unknown')")
        data=self.check();self.assertEqual(data['reconciliation']['legacy'],1)
        self.assertEqual(data['reconciliation']['unresolved'],1);self.assertEqual(self.b.lookups,[])
    def test_lock_prevents_parallel_reconciliation(self):
        Path(self.temp.name,'cycle.lock').mkdir()
        with self.assertRaises(RuntimeError):self.check()
    def test_filled_requires_full_quantity(self):
        cid=self.submit();self.b.orders[cid].update(status='filled',filled_qty='1')
        self.assertEqual(self.check()['reconciliation']['unresolved'],1)
    def test_atomic_payload_precedes_network(self):
        self.b.fail_after_accept=True
        with self.assertRaises(RuntimeError):cycle(self.c,True,self.b)
        with sqlite3.connect(Path(self.temp.name,'orders.sqlite')) as db:
            rows=db.execute('SELECT a.status,r.payload FROM attempts a JOIN paper_requests r ON a.id=r.client_id').fetchall()
        self.assertEqual(len(rows),1);self.assertEqual(rows[0][0],'unknown')
        self.assertEqual(json.loads(rows[0][1])['symbol'],'AAPL')

    def test_final_fill_and_read_only_events(self):
        cid=self.submit();self.b.orders[cid].update(status='filled',filled_qty=self.b.orders[cid]['qty'])
        data=self.check();self.assertEqual(data['order_history'][0]['remaining_qty'],'0')
        self.assertEqual(data['order_history'][0]['status'],'체결 완료')
        self.assertTrue(data['order_events'][0]['checked_at'].endswith('+09:00'))
        self.assertEqual(len(self.b.sent),1)
    def test_interrupted_reconciliation_keeps_unknown(self):
        self.b.fail_after_accept=True
        with self.assertRaises(RuntimeError):cycle(self.c,True,self.b)
        cancel=threading.Event();self.c['_reconcile_cancel']=cancel
        def reader(b):
            data=account_snapshot(b);cancel.set();return data
        with self.assertRaises(RuntimeError):reconcile_snapshot(self.c,self.b,reader)
        self.assertEqual(len(unresolved_attempts(self.temp.name)),1);self.assertEqual(self.b.lookups,[])
        self.assertFalse(Path(self.temp.name,'cycle.lock').exists())

class LookupTests(unittest.TestCase):
    def test_lookup_404_and_other_failures_are_distinct(self):
        with patch.dict(os.environ,{'APCA_API_KEY_ID':'fake','APCA_API_SECRET_KEY':'fake'}):b=AlpacaPaper()
        for code in (404,401,429):
            with patch('stockbot.broker.urlopen',side_effect=HTTPError('https://paper-api.alpaca.markets',code,'error',{},None)):
                if code==404:self.assertIsNone(b.find_order('client & id'))
                else:
                    with self.assertRaises(AlpacaHTTPError):b.find_order('client & id')
    def test_lookup_uses_only_get_and_escaped_query(self):
        seen=[]
        def open_request(req,timeout):
            seen.append(req);return io.BytesIO(b'{"id":"fake"}')
        with patch.dict(os.environ,{'APCA_API_KEY_ID':'fake','APCA_API_SECRET_KEY':'fake'}),patch('stockbot.broker.urlopen',side_effect=open_request):
            AlpacaPaper().find_order('client & id')
        self.assertEqual(seen[0].get_method(),'GET');self.assertIsNone(seen[0].data)
        self.assertIn('client_order_id=client+%26+id',seen[0].full_url)
