import datetime as dt
import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from extended_strategies import NAMES, ema, extended_analysis


def bars(prices, volume=1000, spread=.1):
    start=dt.datetime(2026,10,15,13,30,tzinfo=dt.timezone.utc)
    return [((start+dt.timedelta(minutes=15*i)).isoformat(),c,c+spread,c-spread,c,volume)
            for i,c in enumerate(prices)]


class ExtendedStrategiesTests(unittest.TestCase):
    def test_seed_and_known_monotonic_indicators(self):
        self.assertEqual(ema([1.,2.,3.,4.],3),[None,None,2.,3.])
        signals,evidence=extended_analysis(bars(list(range(100,180)),spread=1.))
        self.assertEqual(evidence['rsi_14_recovery'][14]['indicators']['RSI14'],100.)
        self.assertEqual(evidence['mfi_14_recovery'][14]['indicators']['MFI14'],100.)
        self.assertEqual(evidence['atr_14_breakout'][25]['indicators']['prior_ATR14'],2.)
        self.assertEqual(signals['ema_12_26'][-1],1.)
        self.assertEqual(signals['obv_20'][-1],1.)

    def test_every_prefix_preserves_signals_and_evidence(self):
        rows=bars([100+math.sin(i*.8)*3+i*.03 for i in range(90)])
        all_signals,all_evidence=extended_analysis(rows)
        for length in (0,1,14,15,20,26,33,34,59,89):
            signals,evidence=extended_analysis(rows[:length])
            for name in NAMES:
                self.assertEqual(signals[name],all_signals[name][:length],(name,length))
                self.assertEqual(evidence[name],all_evidence[name][:length],(name,length))

    def test_flat_zero_volume_and_warmup_wait(self):
        signals,evidence=extended_analysis(bars([100.]*60,volume=0,spread=0))
        self.assertEqual(len(signals),20)
        for name in NAMES:
            self.assertEqual(signals[name],[0.]*60,name)
            for decision in evidence[name]:
                self.assertTrue(all(math.isfinite(x) for x in decision['indicators'].values()))
        self.assertEqual(extended_analysis([]),({n:[] for n in NAMES},{n:[] for n in NAMES}))

    def test_breakout_excludes_current_high_and_records_numeric_reason(self):
        signals,evidence=extended_analysis(bars([100.]*30+[110.]))
        self.assertEqual(signals['donchian_20'][-1],1.)
        self.assertEqual(signals['atr_14_breakout'][-1],1.)
        self.assertAlmostEqual(evidence['donchian_20'][-1]['indicators']['prior_high20'],100.1)
        for name in NAMES:
            self.assertEqual(evidence[name][-1]['target'],signals[name][-1])
            self.assertIn('=',evidence[name][-1]['reason'])
            self.assertTrue(all(0<=v<=1 for v in signals[name]))

    def test_recovery_pulses(self):
        signals,_=extended_analysis(bars(list(range(120,100,-1))+[120.]))
        self.assertEqual(signals['rsi_14_recovery'][-2:], [0.,1.])
        signals,_=extended_analysis(bars([100.]*30+[80.,95.,95.]))
        self.assertEqual(signals['bollinger_20_reentry'][-2:], [1.,0.])

    def test_vwap_resets_at_new_york_session_and_ignores_zero_volume(self):
        rows=bars([1000.]*26)
        rows += [('2026-10-16T13:30:00+00:00',100.,101.,99.,100.,1000.),
                 ('2026-10-16T13:45:00+00:00',102.,103.,101.,102.,0.)]
        signals,evidence=extended_analysis(rows)
        self.assertEqual(evidence['session_vwap'][-1]['indicators']['session_VWAP'],100.)
        self.assertEqual(signals['session_vwap'][-2:],[0.,1.])
