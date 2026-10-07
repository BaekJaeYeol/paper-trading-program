import json
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError
from stockbot.kis import KISPaper, PAPER_URL, NoRedirect

class Response:
    def __init__(self, data, continuation=''):
        self.payload=json.dumps(data).encode();self.headers={'tr_cont':continuation}
    def read(self): return self.payload
    def __enter__(self): return self
    def __exit__(self,*args): pass

class KISTests(unittest.TestCase):
    def broker(self): return KISPaper('private-key','private-secret','12345678','01')
    def balance(self, code='005930'):
        return {'rt_cd':'0','output2':[{'tot_evlu_amt':'1000000','dnca_tot_amt':'900000'}],
                'output1':[{'pdno':code,'hldg_qty':'1','pchs_avg_pric':'50000','prpr':'60000','evlu_pfls_amt':'10000'}]}
    def test_paper_only_token_reuse_and_safe_snapshot(self):
        b=self.broker();calls=[]
        def send(req, timeout):
            calls.append(req)
            if req.full_url.endswith('tokenP'):
                return Response({'access_token':'private-token','expires_in':86400})
            return Response(self.balance())
        b.opener.open=send
        result=b.snapshot();b.snapshot()
        self.assertEqual(len(calls),3)
        self.assertTrue(all(r.full_url.startswith(PAPER_URL+'/') for r in calls))
        self.assertEqual(calls[1].get_header('Tr_id'),'VTTC8434R')
        self.assertEqual(calls[1].get_method(),'GET')
        self.assertEqual(result['equity'],1000000)
        self.assertIsNone(result['buying_power'])
        self.assertNotIn('private',str(result))
        with self.assertRaises(ValueError): b._send('/uapi/domestic-stock/v1/trading/order-cash')
    def test_complete_balance_pagination(self):
        b=self.broker();first=self.balance();first.update(ctx_area_fk100='cursor',ctx_area_nk100='next')
        b.opener.open=Mock(side_effect=[Response({'access_token':'token','expires_in':86400}),Response(first,'M'),Response(self.balance('000660'))])
        with patch('stockbot.kis.time.sleep'):
            result=b.snapshot()
        self.assertEqual(len(result['positions']),2)
        self.assertIn('CTX_AREA_NK100=next',b.opener.open.call_args[0][0].full_url)
    def test_bad_account_and_secret_redaction(self):
        with self.assertRaises(ValueError): KISPaper('key','secret','123','01')
        b=self.broker()
        b.opener.open=Mock(side_effect=HTTPError('private-secret',403,'private-secret',{},None))
        with self.assertRaises(RuntimeError) as ctx: b.snapshot()
        self.assertNotIn('private-secret',str(ctx.exception))
    def test_api_failure_and_incomplete_balance_rejected(self):
        b=self.broker();b.token='token';b.expires=float('inf')
        b.opener.open=lambda *a,**kw:Response({'rt_cd':'1','msg1':'private-secret'})
        with self.assertRaises(RuntimeError): b.snapshot()
        b.opener.open=lambda *a,**kw:Response(self.balance(),'M')
        with self.assertRaises(RuntimeError): b.snapshot()
    def test_redirect_blocked(self):
        self.assertIsNone(NoRedirect().redirect_request(None,None,302,'',{},'https://example.com'))

class MarketRoutingTests(unittest.TestCase):
    def test_korean_actions_never_call_us_broker(self):
        from stockbot.gui import Dashboard
        d=Dashboard.__new__(Dashboard)
        d.market=Mock();d.market.get.return_value='한국 · KIS'
        with patch('stockbot.gui.messagebox.showinfo'), patch('stockbot.gui.cycle') as cycle:
            d.scan();d.start();d.demo();d.settings()
            cycle.assert_not_called()
    def test_korean_refresh_routes_to_kis(self):
        from stockbot.gui import Dashboard
        d=Dashboard.__new__(Dashboard)
        d.market=Mock();d.market.get.return_value='한국 · KIS'
        d.kis=Mock();d.work=Mock()
        with patch('stockbot.gui.AlpacaPaper') as us:
            d.refresh()
            us.assert_not_called()
            d.work.assert_called_once_with('account',d.kis.snapshot)
    def test_switch_clears_all_market_data(self):
        from stockbot.gui import Dashboard
        d=Dashboard.__new__(Dashboard)
        d.market=Mock();d.market.get.return_value='한국 · KIS'
        d.values={'cash':Mock()};d.card_titles={'cash':Mock()}
        d.tables={'positions':Mock(),'orders':Mock(),'plans':Mock(),'demo':Mock()}
        d.fill=Mock();d.demo_summary=Mock();d.status=Mock()
        d.change_market()
        d.values['cash'].set.assert_called_once_with('—')
        self.assertEqual(d.fill.call_count,4)
        d.card_titles['cash'].configure.assert_called_once_with(text='예수금 (KRW)')
