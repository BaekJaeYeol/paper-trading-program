import copy
import io
import json
import tempfile
import threading
import unittest
from contextlib import redirect_stdout,redirect_stderr
from datetime import timedelta
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock,patch
from stockbot import historical,cli
from stockbot.historical import fetch_compare,HistoricalDataError
from stockbot.cli import load_config
from test_research import fixture
ROOT=Path(__file__).resolve().parents[1]

class HistoryBroker:
    def __init__(self):
        self.bars=fixture(360);self.calls=[];self.offset=0
    def request(self,path,params=None,body=None,data=False):
        self.calls.append((path,params,body,data));assert body is None
        if path=='/v2/clock':return {'timestamp':str(self.bars[-1].day+timedelta(days=1))+'T14:00:00Z'}
        if path=='/v2/calendar':return [{'date':str(b.day)} for b in self.bars]
        if path=='/v2/stocks/AAPL/bars':
            start=0 if not params.get('page_token') else 180
            rows=self.bars[start:start+180]
            return {'symbol':'AAPL','bars':[{'t':str(b.day)+'T05:00:00Z','o':b.open,'h':b.high,'l':b.low,'c':b.close,'v':b.volume} for b in rows], 'next_page_token':'second' if start==0 else None}
        raise AssertionError('Unexpected or writable endpoint')

class HistoryTests(unittest.TestCase):
    def setUp(self):self.c=load_config(ROOT/'config.json');self.b=HistoryBroker()
    def test_paginated_readonly_fetch_preserves_config_and_has_provenance(self):
        before=copy.deepcopy(self.c);report=fetch_compare(self.b,'AAPL',self.c)
        self.assertEqual(self.c,before);self.assertEqual(report['bars'],360)
        self.assertEqual(report['data_provenance'],'alpaca_iex_split_only');self.assertFalse(report['automatic_promotion'])
        self.assertEqual(report['source_data']['pages'],2);self.assertFalse(report['source_data']['dividends_included'])
        self.assertTrue(all(body is None for _,_,body,_ in self.b.calls))
        for path,params,_,data in self.b.calls:
            self.assertNotIn('orders',path);self.assertNotIn('account',path)
            if data:self.assertEqual(params['adjustment'],'split');self.assertEqual(params['feed'],'iex')
        json.dumps(report,allow_nan=False)
    def mutate_page(self,change):
        old=self.b.request
        def request(path,params=None,body=None,data=False):
            result=old(path,params,body,data)
            return change(result,params) if path.endswith('/bars') else result
        self.b.request=request
    def test_current_day_excluded(self):
        def add(page,params):
            if not page['next_page_token']:
                row=dict(page['bars'][-1]);row['t']=str(self.b.bars[-1].day+timedelta(days=1))+'T05:00:00Z';page['bars'].append(row)
            return page
        self.mutate_page(add);report=fetch_compare(self.b,'AAPL',self.c)
        self.assertEqual(report['bars'],360);self.assertEqual(report['source_data']['excluded_out_of_range'],1)
    def test_duplicate_or_missing_session_rejected(self):
        for duplicate in (True,False):
            self.b=HistoryBroker()
            def alter(page,params):
                if not params.get('page_token'):
                    if duplicate:page['bars'].insert(2,copy.deepcopy(page['bars'][1]))
                    else:page['bars'].pop(2)
                return page
            self.mutate_page(alter)
            with self.assertRaises(HistoricalDataError):fetch_compare(self.b,'AAPL',self.c)
    def test_repeated_token_and_page_limit_rejected(self):
        self.mutate_page(lambda page,params:dict(page,bars=[],next_page_token='again'))
        with self.assertRaises(HistoricalDataError):fetch_compare(self.b,'AAPL',self.c)
        self.assertEqual(len(self.b.calls),4)
    def test_unique_tokens_still_stop_at_page_cap(self):
        counter=[0]
        def infinite(page,params):
            counter[0]+=1;return dict(page,bars=[],next_page_token=str(counter[0]))
        self.mutate_page(infinite)
        with self.assertRaises(HistoricalDataError):fetch_compare(self.b,'AAPL',self.c)
        self.assertEqual(len(self.b.calls),12)
    def test_cancel_during_get_prevents_followup_requests(self):
        event=threading.Event();old=self.b.request
        def request(*a,**kw):result=old(*a,**kw);event.set();return result
        self.b.request=request
        with self.assertRaises(HistoricalDataError):fetch_compare(self.b,'AAPL',self.c,cancel=event)
        self.assertEqual(len(self.b.calls),1)
    def test_last_session_missing_and_insufficient_history_rejected(self):
        self.mutate_page(lambda page,params:dict(page,bars=page['bars'][:-1] if params.get('page_token') else page['bars']))
        with self.assertRaises(HistoricalDataError):fetch_compare(self.b,'AAPL',self.c)
        self.b=HistoryBroker();self.b.bars=self.b.bars[:200]
        with self.assertRaises(HistoricalDataError):fetch_compare(self.b,'AAPL',self.c)
    def test_naive_timestamp_and_wrong_symbol_rejected(self):
        self.mutate_page(lambda page,params:dict(page,symbol='MSFT'))
        with self.assertRaises(HistoricalDataError):fetch_compare(self.b,'AAPL',self.c)
        with self.assertRaises(HistoricalDataError):historical.aware('2020-01-01')
    def test_invalid_symbol_and_cancel_before_any_get(self):
        broker=Mock();event=threading.Event();event.set()
        with self.assertRaises(ValueError):fetch_compare(broker,'AAPL/../account',self.c)
        with self.assertRaises(HistoricalDataError):fetch_compare(broker,'AAPL',self.c,cancel=event)
        broker.request.assert_not_called()
    def test_deadline_after_get_stops_before_calendar(self):
        clock=[0];old=self.b.request
        def request(*a,**kw):result=old(*a,**kw);clock[0]=61;return result
        self.b.request=request
        with patch.object(historical,'time',SimpleNamespace(monotonic=lambda:clock[0])):
            with self.assertRaises(HistoricalDataError):fetch_compare(self.b,'AAPL',self.c)
        self.assertEqual(len(self.b.calls),1)
    def test_errors_redact_arbitrary_transport_details(self):
        broker=Mock();broker.request.side_effect=RuntimeError('SECRET_KEY')
        with self.assertRaises(HistoricalDataError) as error:fetch_compare(broker,'AAPL',self.c)
        self.assertNotIn('SECRET_KEY',str(error.exception))
    def test_cli_api_research_has_no_state_writes(self):
        with tempfile.TemporaryDirectory() as d:
            config=dict(self.c,state_dir=str(Path(d)/'state'));out=io.StringIO()
            with patch.object(cli,'load_config',return_value=config),patch.object(cli,'AlpacaPaper',return_value=self.b),patch('sys.argv',['stockbot','research-api','--symbol','AAPL']),redirect_stdout(out):cli.main()
            self.assertEqual(json.loads(out.getvalue())['source_data']['symbol'],'AAPL');self.assertFalse(Path(d,'state').exists())
    def test_cli_rejects_execute_flag_before_broker(self):
        with patch.object(cli,'load_config',return_value=self.c),patch.object(cli,'AlpacaPaper') as broker,patch('sys.argv',['stockbot','research-api','--execute-paper']),redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):cli.main()
        broker.assert_not_called()
