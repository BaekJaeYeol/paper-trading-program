import copy
import json
import math
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from operational_audit import validate_account, record_run

class AuditTests(unittest.TestCase):
    def account(self):
        return dict(cash=9000.,qty=10.,mark=100.,equity=10000.,initial=10000.,fee=.001,slippage=.001,half_spread=.0001,participation=.01)
    def test_valid_and_roundoff(self):
        a=self.account();a['equity']+=.001;validate_account(a)
    def test_corrupt_numbers_and_balance(self):
        for key,value in [('cash',-1),('qty',float('nan')),('mark',float('inf')),('equity',999),('participation',2),('initial',True)]:
            a=self.account();a[key]=value;before=repr(a)
            with self.assertRaises(ValueError):validate_account(a)
            self.assertEqual(repr(a),before)
    def test_invalid_risk(self):
        a=self.account();a['risk']=dict(halted=False,peak=10000,day_equity=10000,daily_limit=-.03,drawdown_limit=.1)
        with self.assertRaises(ValueError):validate_account(a)
    def test_error_recovery_and_bounded_restart(self):
        with tempfile.TemporaryDirectory() as d:
            previous={}
            for i in range(205):
                s=dict(checked_utc=str(i),symbols={'SPY':dict(status='error' if i<204 else 'ok')})
                record_run(d,s,previous,1.25);previous=copy.deepcopy(s)
            self.assertTrue(s['symbols']['SPY']['recovered']);self.assertEqual(s['symbols']['SPY']['consecutive_errors'],0)
            record_run(d,s,previous,1.25)
            history=json.loads((Path(d)/'operations-history.json').read_text())
            self.assertEqual(len(history),200);self.assertEqual(history[-2]['symbols']['SPY']['consecutive_errors'],204)
if __name__=='__main__':unittest.main()
