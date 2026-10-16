import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from intraday import decode_bars,intraday_candidates,tick as actual_tick,NY

def tick(*args):
    return actual_tick(*args,now=dt.datetime(2026,10,9,19,59,tzinfo=dt.timezone.utc).timestamp())

def rows(count=130):
    result=[]
    for day in range(5):
        start=dt.datetime(2026,10,5+day,9,30,tzinfo=NY)
        for slot in range(26):
            i=len(result);price=100+i*.1
            stamp=(start+dt.timedelta(minutes=slot*15)).astimezone(dt.timezone.utc).isoformat()
            result.append((stamp,price,price+1,price-1,price,1000))
    return result[:count]

def raw_bars(rs):
    return {'chart':{'result':[{'meta':{'symbol':'SPY','currency':'USD','exchangeTimezoneName':'America/New_York'},
        'timestamp':[int(dt.datetime.fromisoformat(r[0]).timestamp()) for r in rs],
        'indicators':{'quote':[{k:[r[i] for r in rs] for i,k in enumerate(('open','high','low','close','volume'),1)}]}}]}}

class IntradayTests(unittest.TestCase):
    def test_restart_after_interrupted_directory_swap(self):
        rs=rows()
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(tick(d,['SPY'],lambda _:rs)['symbols']['SPY']['status'],'ok')
            folder=Path(d)/'SPY'
            before=[(folder/name).read_bytes() for name in ('accounts.json','accounts-v2.json')]
            folder.rename(Path(d)/'SPY.backup')
            (Path(d)/'SPY.pending').mkdir()
            result=tick(d,['SPY'],lambda _:rs)
            self.assertEqual(result['symbols']['SPY']['status'],'ok')
            self.assertTrue(result['recovery_actions']['SPY'])
            self.assertEqual([(folder/name).read_bytes() for name in ('accounts.json','accounts-v2.json')],before)
            self.assertEqual(result['symbols']['SPY']['new_trades'],0)

    def test_strategy_expansion_preserves_existing_accounts(self):
        from unittest.mock import patch
        from extended_strategies import MORE_NAMES, extended_analysis
        def original_candidates(rows):
            signals,evidence=extended_analysis(rows)
            return ({k:v for k,v in signals.items() if k not in MORE_NAMES},
                    {k:v for k,v in evidence.items() if k not in MORE_NAMES})
        rs=rows()
        with tempfile.TemporaryDirectory() as d:
            with patch('intraday.extended_analysis',side_effect=original_candidates):
                first=tick(d,['SPY'],lambda symbol:rs)
            self.assertEqual(first['symbols']['SPY']['accounts'],37)
            folder=Path(d)/'SPY'
            old_v1=json.loads((folder/'accounts.json').read_text())
            old_v2=json.loads((folder/'accounts-v2.json').read_text())
            result=tick(d,['SPY'],lambda symbol:rs)
            self.assertEqual(result['symbols']['SPY']['accounts'],47)
            new_v1=json.loads((folder/'accounts.json').read_text())
            new_v2=json.loads((folder/'accounts-v2.json').read_text())
            for name in old_v1:
                self.assertEqual(new_v1[name],old_v1[name])
                self.assertEqual(new_v2[name],old_v2[name])
            for name in MORE_NAMES:
                self.assertEqual(new_v2[name]['cash'],10000.)
                self.assertEqual(new_v2[name]['events'],[])
            research=json.loads((folder/'comparison.json').read_text())
            self.assertEqual(len(research['results']),47)
            result=tick(d,['SPY'],lambda symbol:rs)
            self.assertEqual(result['symbols']['SPY']['new_trades'],0)

    def test_complete_regular_only(self):
        rs=rows();raw=raw_bars(rs)
        now=dt.datetime.fromisoformat(rs[-1][0]).timestamp()+500
        decoded=decode_bars(raw,'SPY',now)
        self.assertEqual(len(decoded),129)
        self.assertEqual(decoded[-1],rs[-2])
        raw['chart']['result'][0]['meta']['currency']='KRW'
        with self.assertRaises(ValueError):decode_bars(raw,'SPY',now)
    def test_order_and_bad_price(self):
        rs=rows();raw=raw_bars(rs);now=dt.datetime.fromisoformat(rs[-1][0]).timestamp()+901
        raw['chart']['result'][0]['timestamp'][-1]=raw['chart']['result'][0]['timestamp'][-2]
        with self.assertRaises(ValueError):decode_bars(raw,'SPY',now)
        raw=raw_bars(rs);raw['chart']['result'][0]['indicators']['quote'][0]['open'][0]=-1
        with self.assertRaises(ValueError):decode_bars(raw,'SPY',now)
    def test_prefix_signals_and_next_open(self):
        rs=rows()
        self.assertEqual(intraday_candidates(rs[:100])['trend_8_26'],intraday_candidates(rs)['trend_8_26'][:100])
        with tempfile.TemporaryDirectory() as d:
            tick(d,['SPY'],lambda symbol:rs[:-1])
            initial=json.loads((Path(d)/'SPY/accounts.json').read_text())
            self.assertEqual(initial['buy_hold']['qty'],0)
            result=tick(d,['SPY'],lambda symbol:rs)
            self.assertEqual(result['symbols']['SPY']['new_bars'],1)
            v2=json.loads((Path(d)/'SPY/accounts-v2.json').read_text())
            for name in __import__('extended_strategies').NAMES:
                event=v2[name]['events'][-1]
                self.assertEqual(event['evidence']['signal_bar'],rs[-2][0])
                self.assertEqual(event['evidence']['target'],event['target'])
                self.assertIn('다음 봉 시가',event['reason'])
            path=Path(d)/'SPY/accounts.json';first=path.read_bytes()
            account=json.loads(first)['buy_hold'];self.assertGreater(account['qty'],0)
            event=account['events'][0]
            self.assertEqual(event['signal_bar_start_utc'],rs[-2][0])
            self.assertAlmostEqual(event['simulated_fill_price'],rs[-1][1]*1.001)
            self.assertGreater(event['fee'],0)
            result=tick(d,['SPY'],lambda symbol:rs)
            self.assertEqual(result['symbols']['SPY']['new_trades'],0)
            self.assertEqual(path.read_bytes(),first)
            def fail(symbol):raise ValueError('network failed')
            tick(d,['SPY'],fail);self.assertEqual(path.read_bytes(),first)
            revised=list(rs);r=revised[-1];revised[-1]=(r[0],r[1],r[2],r[3],r[4]+.1,r[5])
            result=tick(d,['SPY'],lambda symbol:revised)
            self.assertEqual(result['symbols']['SPY']['status'],'ok')
            self.assertEqual(result['symbols']['SPY']['provider_revisions'],1)
            self.assertEqual(path.read_bytes(),first)
            revised[-1]=(r[0],r[1],r[2],r[3],r[4]+2,r[5])
            result=tick(d,['SPY'],lambda symbol:revised)
            self.assertEqual(result['symbols']['SPY']['status'],'error')
            self.assertEqual(path.read_bytes(),first)

    def test_cross_session_gap_preserves_accounts(self):
        rs=rows()
        with tempfile.TemporaryDirectory() as d:
            initial=rs[:103]
            now=dt.datetime.fromisoformat(initial[-1][0]).timestamp()+901
            result=actual_tick(d,['SPY'],lambda symbol:initial,now=now)
            self.assertEqual(result['symbols']['SPY']['status'],'ok')
            paths=[Path(d)/'SPY'/name for name in ('accounts.json','accounts-v2.json','bars.json')]
            before=[path.read_bytes() for path in paths]
            # Omit Thursday's final bar, then provide Friday's opening bar.
            missing=rs[:103]+rs[104:105]
            now=dt.datetime.fromisoformat(missing[-1][0]).timestamp()+901
            result=actual_tick(d,['SPY'],lambda symbol:missing,now=now)
            self.assertEqual(result['symbols']['SPY']['status'],'error')
            self.assertEqual([path.read_bytes() for path in paths],before)
