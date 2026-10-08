import unittest, tempfile, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from engine import signals,evaluate,load
from paper import Paper
from research import run
from data import symbol_name

class Tests(unittest.TestCase):
    def setUp(self):self.rows=load(Path(__file__).resolve().parents[1]/'demo_synthetic.csv')
    def test_no_future(self):
        full=signals(self.rows);part=signals(self.rows[:300]);self.assertTrue(all(part[k]==full[k][:300] for k in full))
    def test_cash_and_costs(self):
        r=[(str(i),100,100,100,100,1000) for i in range(300)]
        self.assertEqual(evaluate(r,[0]*300,61,300,.002)['return'],0)
        self.assertAlmostEqual(evaluate(r,[1]*300,61,300,.002)['return'],.998**2-1)
    def test_forward_restart(self):
        with tempfile.TemporaryDirectory() as d:
            p=Paper(Path(d)/'paper.sqlite');p.start(self.rows[:300],'buy_hold','real_download')
            a=p.advance(self.rows[:310]);b=Paper(p.path).advance(self.rows[:310]);self.assertEqual(a,b)
            self.assertEqual(len(a['ledger']),10);self.assertGreater(a['qty'],0);self.assertGreaterEqual(a['cash'],0)
            self.assertEqual(sum(r[2]=='buy' for r in a['ledger']),1)
    def test_revision_halts(self):
        with tempfile.TemporaryDirectory() as d:
            p=Paper(Path(d)/'p.sqlite');p.start(self.rows[:300],'trend','real_download')
            rows=list(self.rows);r=list(rows[299]);r[4]*=.9;rows[299]=tuple(r)
            with self.assertRaises(ValueError):p.advance(rows)
            self.assertEqual(p.snapshot()['last_date'],self.rows[299][0])
    def test_no_synthetic_forward(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):Paper(Path(d)/'p.sqlite').start(self.rows,'trend','synthetic')
    def test_selection_holdout_separation(self):
        with tempfile.TemporaryDirectory() as d:
            out=run(Path(__file__).resolve().parents[1]/'demo_synthetic.csv',d,'synthetic')
            names={r['strategy'] for r in out['results'] if r['fold']=='holdout'}
            self.assertEqual(names,{'cash','buy_hold',out['selected']});self.assertFalse(out['live_ready'])
    def test_symbol(self):
        self.assertEqual(symbol_name('spy'),'SPY')
        with self.assertRaises(ValueError):symbol_name('../secret')
@unittest.skipUnless(sys.platform=='win32','Windows GUI launch check')
class GuiSmoke(unittest.TestCase):
    def test_launch_and_demo_report(self):
        import tkinter as tk
        from app import App
        root=tk.Tk()
        try:
            app=App(root);app.demo()
            with tempfile.TemporaryDirectory() as d:
                report=run(app.path,d,'synthetic');app.show_report(report)
            root.update_idletasks()
            self.assertEqual(len(app.table.get_children()),len(report['results']))
            self.assertIn('합성 데모',app.status.get())
        finally:
            root.destroy()
    def test_refresh_status_and_trade_display(self):
        import tkinter as tk
        from app import App
        root=tk.Tk()
        try:
            app=App(root);app.symbol_used='SPY';app.running=True
            snap={'active':True,'config':{'strategy':'trend'},'cash':10000,'qty':0,'equity':10000,'last_date':'2026-10-07','ledger':[],'latest_trade':None}
            app.refreshed((snap,0));root.update_idletasks()
            self.assertIn('새 데이터 없음',app.refresh_info.get())
            self.assertIn('KST',app.refresh_info.get());self.assertIn('SPY',app.account.get())
            self.assertIn('기록 없음',app.trade_info.get())
            trade=('2026-10-08',1,'buy',2,100,0.2,10000)
            snap.update(qty=2,latest_trade=trade,ledger=[trade],last_date='2026-10-08')
            app.refreshed((snap,1));self.assertIn('새 일봉 1개',app.refresh_info.get())
            self.assertIn('모의 매수',app.trade_info.get());self.assertIn('SPY 2.0000주',app.trade_info.get())
            app.stop();app.refreshed((snap,0));self.assertIn('중단',app.status.get())
        finally:root.destroy()
if __name__=='__main__':unittest.main()
