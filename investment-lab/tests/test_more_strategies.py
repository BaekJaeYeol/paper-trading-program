import datetime as dt
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from extended_strategies import MORE_NAMES, extended_analysis
from test_extended_strategies import bars


class MoreStrategiesTests(unittest.TestCase):
    def test_known_trend_and_accumulation(self):
        rows=bars(list(range(100,180)))
        # Every close is at the high: money-flow multiplier is exactly one.
        rows=[(t,o,c,c-2,c,v) for t,o,h,l,c,v in rows]
        signals,evidence=extended_analysis(rows)
        self.assertEqual(evidence['adx_14_trend'][-1]['indicators']['ADX14'],100.)
        self.assertEqual(evidence['aroon_25_trend'][-1]['indicators']['Aroon_up'],100.)
        self.assertEqual(evidence['aroon_25_trend'][-1]['indicators']['Aroon_down'],0.)
        self.assertEqual(evidence['cmf_20_accumulation'][-1]['indicators']['CMF20'],1.)
        for name in MORE_NAMES:
            if name not in ('williams_14_recovery','opening_range_30m'):
                self.assertEqual(signals[name][-1],1.,name)

    def test_opening_range_requires_both_bars_and_resets(self):
        rows=[('2026-10-15T13:30:00+00:00',100,101,99,100,1000),
              ('2026-10-15T13:45:00+00:00',101,102,100,101,1000),
              ('2026-10-15T14:00:00+00:00',103,104,102,103,1000),
              ('2026-10-16T13:30:00+00:00',110,111,109,110,1000)]
        signals,evidence=extended_analysis(rows)
        self.assertEqual(signals['opening_range_30m'],[0.,0.,1.,0.])
        self.assertEqual(evidence['opening_range_30m'][2]['indicators']['opening_high'],102)
        self.assertEqual(extended_analysis(rows[1:])[0]['opening_range_30m'],[0.,0.,0.])
        # Winter New York 09:30 is 14:30 UTC.
        winter=[(t.replace('10-15','11-16').replace('T13:','T14:').replace('T14:00','T15:00'),o,h,l,c,v)
                for t,o,h,l,c,v in rows[:3]]
        self.assertEqual(extended_analysis(winter)[0]['opening_range_30m'],[0.,0.,1.])

    def test_williams_recovery_is_one_bar(self):
        signals,_=extended_analysis(bars(list(range(120,100,-1))+[120.,120.]))
        self.assertEqual(signals['williams_14_recovery'][-3:],[0.,1.,0.])

    def test_aroon_equal_extremes_use_most_recent(self):
        signals,evidence=extended_analysis(bars([100.]*30))
        metrics=evidence['aroon_25_trend'][-1]['indicators']
        self.assertEqual((metrics['Aroon_up'],metrics['Aroon_down']),(100.,100.))
        self.assertEqual(signals['aroon_25_trend'][-1],0.)

    def test_zero_range_and_zero_volume_have_no_money_flow_signal(self):
        signals,evidence=extended_analysis(bars([100.]*60,spread=0,volume=0))
        for name in MORE_NAMES:
            self.assertEqual(signals[name],[0.]*60,name)
        self.assertNotIn('CMF20',evidence['cmf_20_accumulation'][-1]['indicators'])
