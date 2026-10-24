import copy
import io
import json
import math
import tempfile
import unittest
from contextlib import redirect_stdout,redirect_stderr
from datetime import date,timedelta
from pathlib import Path
from unittest.mock import Mock,patch
from stockbot.core import Bar,backtest
from stockbot.research import compare,trend,calm_trend
from stockbot.cli import load_config
from stockbot import cli
from stockbot.gui import Dashboard
import test_ui_safety
ROOT=Path(__file__).resolve().parents[1]

def fixture(n=400):
    rows=[];day=date(2020,1,1)
    for i in range(n):
        while day.weekday()>4:day+=timedelta(days=1)
        price=100+i*.02
        rows.append(Bar(day,price,price*1.025,price*.998,price,10000 if i%15==0 else 1000));day+=timedelta(days=1)
    return rows

class ResearchTests(unittest.TestCase):
    def setUp(self):self.c=load_config(ROOT/'config.json');self.c.update(stop_loss=.01,take_profit=.01)
    def test_holdout_changes_cannot_change_training_selection(self):
        bars=fixture();first=compare(bars,self.c);changed=bars[:240]
        changed += [Bar(b.day,b.open*2,b.high*2,b.low*2,b.close*2,b.volume*2) for b in bars[240:]]
        second=compare(changed,self.c)
        self.assertEqual(first['selected_on_training'],second['selected_on_training'])
        self.assertEqual([r['train'] for r in first['rows']],[r['train'] for r in second['rows']])
        self.assertNotEqual(first['data_sha256'],second['data_sha256'])
    def test_flat_nontrading_data_cannot_win_by_zero_trades(self):
        bars=[Bar(b.day,100,101,99,100,1000) for b in fixture()]
        report=compare(bars,self.c)
        self.assertIsNone(report['selected_on_training']);self.assertEqual(report['evidence_status'],'insufficient_training_trades')
    def test_config_unchanged_and_report_json_finite(self):
        before=copy.deepcopy(self.c);report=compare(fixture(),self.c)
        self.assertEqual(before,self.c);self.assertFalse(report['automatic_promotion'])
        self.assertEqual(report['data_provenance'],'unverified_csv');json.dumps(report,allow_nan=False)
        self.assertEqual(report['periods']['train']['bars'],180)
        self.assertEqual(report['periods']['validation']['bars'],80);self.assertEqual(report['periods']['test']['bars'],80)
    def test_too_short_or_unsorted_input_rejected(self):
        for rows in (fixture(65),list(reversed(fixture())),fixture()+[fixture()[-1]]):
            with self.assertRaises(ValueError):compare(rows,self.c)
    def test_past_only_filter_and_forced_exit_costs(self):
        bars=fixture(90);seen=[]
        def guard(history):seen.append(len(history));self.assertEqual(history,bars[:len(history)]);return True
        report=backtest(bars,self.c,entry_filter=guard,start_index=60,liquidate_end=True)
        self.assertTrue(seen);self.assertTrue(all(60<=i<len(bars) for i in seen));self.assertEqual(report['open_qty'],0)
        self.assertGreater(report['estimated_costs'],0)
    def test_loss_accounting_includes_initial_equity_and_stop_first(self):
        base=[Bar(date(2020,1,1)+timedelta(days=i),100,101,99,100,3000 if i==30 else 1000) for i in range(31)]
        bars=base+[Bar(date(2020,2,1),100,120,90,100,1000)]
        self.c.update(stop_loss=.05,take_profit=.15,entry_strategy='baseline')
        r=backtest(bars,self.c,fee=0,slippage=0)
        self.assertEqual(r['closed_trades'],1);self.assertAlmostEqual(r['ending_equity'],9975)
        self.assertAlmostEqual(r['max_drawdown'],.0025);self.assertEqual(r['win_rate'],0)
    def test_forced_terminal_liquidation_pays_sell_costs(self):
        bars=fixture(70);self.c.update(take_profit=.50,stop_loss=.5)
        held=backtest(bars,self.c);closed=backtest(bars,self.c,liquidate_end=True)
        self.assertGreater(held['open_qty'],0);self.assertEqual(closed['open_qty'],0)
        self.assertLess(closed['ending_equity'],held['ending_equity']);self.assertGreater(closed['estimated_costs'],held['estimated_costs'])
    def test_invalid_capital_costs_and_signal_settings(self):
        for kwargs in ({'fee':-1},{'slippage':float('nan')},{'sell_tax':1},{'fee':.6,'sell_tax':.5},{'cash':0}):
            with self.assertRaises(ValueError):backtest(fixture(),self.c,**kwargs)
        with self.assertRaises(ValueError):backtest(fixture(),dict(self.c,volume_ratio=float('nan')))
    def test_filters_block_flat_falling_and_extreme_volatility(self):
        self.assertFalse(trend(fixture(59)))
        flat=[Bar(b.day,100,101,99,100,1000) for b in fixture(60)]
        self.assertFalse(trend(flat));self.assertTrue(trend(fixture(60)))
        wild=[Bar(b.day,b.open,b.high*2,b.low*.5,b.close,b.volume) for b in fixture(60)]
        self.assertFalse(calm_trend(wild));self.assertTrue(calm_trend(fixture(60)))
    def test_cost_matched_cash_and_holding_benchmarks(self):
        r=compare(fixture(),self.c)
        for period in r['benchmarks'].values():
            self.assertEqual(period['cash_return'],0)
            self.assertEqual(period['matched_allocation_hold']['allocation_fraction'],.05)
            self.assertEqual(period['full_allocation_hold']['allocation_fraction'],1)
    def test_cli_research_never_constructs_broker_or_writes_state(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'bars.csv'
            path.write_text('date,open,high,low,close,volume\n'+''.join(f'{b.day},{b.open},{b.high},{b.low},{b.close},{b.volume}\n' for b in fixture()))
            config=dict(self.c,state_dir=str(Path(d)/'state'));out=io.StringIO()
            with patch.object(cli,'load_config',return_value=config),patch.object(cli,'AlpacaPaper') as broker,patch('sys.argv',['stockbot','research','--csv',str(path),'--fee-bps','20']),redirect_stdout(out):cli.main()
            broker.assert_not_called();self.assertFalse(Path(d,'state').exists());self.assertEqual(json.loads(out.getvalue())['cost_assumptions']['fee_each_side'],.002)
    def test_cli_rejects_execute_flag(self):
        with patch.object(cli,'load_config',return_value=self.c),patch.object(cli,'AlpacaPaper') as broker,patch('sys.argv',['stockbot','research','--execute-paper']),redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):cli.main()
        broker.assert_not_called()
    def test_gui_research_cancel_does_not_start_worker(self):
        app=Dashboard.__new__(Dashboard);app.busy=False;app.running=False;app.root=Mock();app.path=ROOT/'config.json';app.work=Mock()
        with patch('stockbot.gui.filedialog.askopenfilename',return_value=''):app.research()
        app.work.assert_not_called()
    def test_research_failure_does_not_mark_account_connection_failed(self):
        with tempfile.TemporaryDirectory() as d:
            app=test_ui_safety.SafetyTests().fake_dashboard(d);app.events.put(('research',None,True));app.poll()
            self.assertFalse(app.account_error);self.assertFalse(Path(d,'STOP').exists())
