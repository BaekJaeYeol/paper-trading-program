import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock
from stockbot.cli import load_config,cycle,now_parse
from stockbot.core import Bar,backtest
from stockbot.strategies import decision,trend
from stockbot.research import candidates
from test_bot import FakeBroker
ROOT=Path(__file__).resolve().parents[1]

class AppliedStrategyTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.c=load_config(ROOT/'config.json');self.c.update(state_dir=self.temp.name,symbols=['AAPL']);self.b=FakeBroker()
    def bars(self):return [Bar(now_parse(r['t']).date(),r['o'],r['h'],r['l'],r['c'],r['v']) for r in self.b.bars()]
    def test_shipped_config_applies_guard_but_old_missing_key_stays_baseline(self):
        self.assertEqual(self.c['entry_strategy'],'trend_guard')
        old=dict(self.c);old.pop('entry_strategy');p=Path(self.temp.name)/'old.json';p.write_text(json.dumps(old))
        self.assertEqual(load_config(p)['entry_strategy'],'baseline')
        old['entry_strategy']='unknown';p.write_text(json.dumps(old))
        with self.assertRaises(ValueError):load_config(p)
    def test_trending_candidate_preserves_bracket_and_explains_filter(self):
        result=cycle(self.c,True,self.b);self.assertEqual(len(self.b.sent),1)
        self.assertTrue(result['orders'][0]['signal']['entry_filter']['allowed'])
        self.assertEqual(result['entry_filter']['strategy'],'trend_guard')
        body=self.b.sent[0];self.assertEqual(body['order_class'],'bracket');self.assertEqual(body['time_in_force'],'day')
        self.assertIn('sb-v1-AAPL-',body['client_order_id'])
    def test_flat_candidate_is_blocked_before_quote_or_submit(self):
        old=self.b.bars
        self.b.bars=lambda *a:[dict(r,o=100,c=100,h=101,l=99) for r in old(*a)]
        self.b.quote=Mock(side_effect=AssertionError('Must not query quote for rejected filter'))
        result=cycle(self.c,True,self.b)
        self.assertEqual(result['orders'],[]);self.assertEqual(self.b.sent,[])
        self.assertEqual(result['entry_filter']['excluded'],{'trend_not_met':1})
    def test_short_history_blocks_and_legacy_baseline_can_still_screen(self):
        old=self.b.bars;self.b.bars=lambda *a:old(*a)[-31:]
        blocked=cycle(self.c,False,self.b);self.assertEqual(blocked['entry_filter']['excluded'],{'insufficient_history':1})
        self.c['entry_strategy']='baseline';self.assertEqual(len(cycle(self.c,False,self.b)['orders']),1)
    def test_sharp_drop_rejected_even_with_volume_spike(self):
        bars=self.bars();last=bars[-1];bars[-1]=Bar(last.day,70,71,69,70,last.volume)
        result=decision(bars,'trend_guard');self.assertFalse(result['allowed']);self.assertEqual(result['reason'],'sharp_decline')
    def test_optional_volatility_guard_blocks_wild_ranges(self):
        bars=self.bars();wild=[Bar(b.day,b.open,b.high*2,b.low*.5,b.close,b.volume) for b in bars]
        self.assertTrue(decision(wild,'trend_guard')['allowed']);self.assertFalse(decision(wild,'trend_volatility_guard')['allowed'])
    def test_changing_strategy_does_not_reset_duplicate_key(self):
        cycle(self.c,True,self.b);self.c['entry_strategy']='baseline';cycle(self.c,True,self.b)
        self.assertEqual(len(self.b.sent),1)
    def test_unknown_outcome_blocks_even_after_strategy_switch(self):
        self.b.fail=True
        with self.assertRaises(RuntimeError):cycle(self.c,True,self.b)
        self.c['entry_strategy']='baseline'
        with self.assertRaises(RuntimeError):cycle(self.c,True,self.b)
        self.assertEqual(len(self.b.sent),1)
    def test_research_baseline_remains_unfiltered_when_active_default_guard(self):
        rows=candidates(self.c);self.assertEqual(rows[0][1]['entry_strategy'],'baseline');self.assertIsNone(rows[0][2])
        self.assertEqual(self.c['entry_strategy'],'trend_guard')
    def test_backtest_uses_same_guard_and_does_not_see_future(self):
        bars=self.bars();bar=bars[-1]
        bars.append(Bar(bar.day.replace(day=bar.day.day+1),100,101,99,100,1000))
        self.assertTrue(trend(bars[:60]))
        result=backtest(bars,self.c);self.assertEqual(len(result['trades']),1)
        flat=[Bar(b.day,100,101,99,100,b.volume) for b in bars]
        self.assertEqual(backtest(flat,self.c)['trades'],[])
