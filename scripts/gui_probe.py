"""Launch real Tk widgets with an offline broker and export state for external UI tests."""
import json
from contextlib import closing
import os
import socket
import sys
import time
import tkinter as tk
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tests'))
from test_paper_journal import TrackingBroker
from stockbot.broker import AlpacaHTTPError
import stockbot.gui as gui

OUT = ROOT / 'gui-check'
OUT.mkdir(exist_ok=True)
import shutil
shutil.copytree(ROOT / "examples", OUT / "examples", dirs_exist_ok=True)
# Deterministic synthetic fixture; never a market-performance claim.
from datetime import date,timedelta
sample=['date,open,high,low,close,volume'];sample_day=date(2020,1,1)
for i in range(360):
    while sample_day.weekday()>4:sample_day+=timedelta(days=1)
    price=100+i*.02
    sample.append(f'{sample_day},{price},{price*1.025},{price*.998},{price},{10000 if i%15==0 else 1000}')
    sample_day+=timedelta(days=1)
(OUT/'examples'/'synthetic-strategy-research.csv').write_text('\n'.join(sample)+'\n',encoding='utf-8')
config = json.loads((ROOT / 'config.json').read_text())
config['symbols'] = ['AAPL']
config['state_dir'] = str(OUT / 'state')
path = OUT / 'config.json'
path.write_text(json.dumps(config), encoding='utf-8')
for key in ('APCA_API_KEY_ID', 'APCA_API_SECRET_KEY'):
    os.environ.pop(key, None)

class OfflineBroker(TrackingBroker):
    fail = False
    calls = 0
    read_calls=0
    partial = False
    delay = 0
    saved_orders={}
    saved_posts=[]
    missing=False
    injected=False
    holding_extra=0
    root_replaced=False
    price_changed=False
    closed_flat=False
    late_schedule_injected=False
    power_fail=False
    budget_timeout=False
    flat_strategy=False
    budget_run_injected=False
    def __init__(self):
        super().__init__()
        self.orders=OfflineBroker.saved_orders
        self.sent=OfflineBroker.saved_posts
    def bars(self,*args):
        rows=super().bars(*args)
        if OfflineBroker.flat_strategy:return [dict(row,o=100,c=100,h=101,l=99) for row in rows]
        return rows
    def request(self, path, params=None, body=None):
        if body is None:OfflineBroker.read_calls+=1
        if OfflineBroker.fail: raise RuntimeError('offline failure')
        if path=='/v2/orders:by_client_order_id' and OfflineBroker.missing and params['client_order_id']=='gui-response-lost-MSFT':raise AlpacaHTTPError(404)
        if path=='/v2/account' and OfflineBroker.budget_timeout:virtual_budget['offset']=65
        if path=='/v2/account' and OfflineBroker.delay:
            import time
            time.sleep(OfflineBroker.delay)
        if path=='/v2/orders' and body is None and OfflineBroker.partial:
            return [{'symbol':'AAPL','side':'buy','qty':'10','filled_qty':'3','limit_price':'100','status':'partially_filled'}]
        result = super().request(path, params, body)
        if path == '/v2/account': result['cash'] = '8000'
        if path=='/v2/positions' and OfflineBroker.holding_extra:
            for position in result:
                if position['symbol']=='MSFT':position['qty']=str(float(position['qty'])+OfflineBroker.holding_extra)
        if path=='/v2/orders:by_client_order_id' and OfflineBroker.root_replaced and params['client_order_id']=='gui-response-lost-MSFT':
            result=dict(result,status='pending_replace',replaced_by='offline-replacement')
        if path=='/v2/orders:by_client_order_id' and OfflineBroker.price_changed and result.get('symbol')=='AAPL':
            result=dict(result,limit_price='999')
        if body: OfflineBroker.calls += 1
        return result

# The virtual reconciliation clock affects only the journal, not Tk or scheduling.
from types import SimpleNamespace
import stockbot.paper_journal as journal
virtual_budget={'offset':0}
journal.time=SimpleNamespace(monotonic=lambda:time.monotonic()+virtual_budget['offset'])
real_reconcile=gui.reconcile_snapshot
def controlled_reconcile(*args,**kwargs):
    virtual_budget['offset']=0
    try:return real_reconcile(*args,**kwargs)
    finally:virtual_budget['offset']=0
gui.reconcile_snapshot=controlled_reconcile
gui.AlpacaPaper = OfflineBroker
import stockbot.cli as cli
cli.AlpacaPaper = OfflineBroker
# No outbound network is allowed from this process, even if an adapter changes.
def no_network(*args, **kwargs): raise RuntimeError('GUI verification blocks network')
socket.socket.connect = no_network
socket.create_connection = no_network
root = tk.Tk()
app = gui.Dashboard(root, path)
real_acquire=app.sleep_guard.acquire
def controlled_acquire():
    if OfflineBroker.power_fail:
        app.sleep_guard.error='acquire'
        return False
    return real_acquire()
app.sleep_guard.acquire=controlled_acquire

def snapshot():
    windows = []
    def inspect(window):
        widgets = []
        def visit(w):
            if w.winfo_ismapped():
                cls = w.winfo_class()
                record = {'class': cls, 'x': w.winfo_rootx() + w.winfo_width() // 2,
                          'y': w.winfo_rooty() + w.winfo_height() // 2,
                          'width': w.winfo_width(), 'height': w.winfo_height()}
                if cls in ('TButton', 'TLabel', 'Label'): record['text'] = str(w.cget('text'))
                if cls == 'TEntry': record['masked'] = bool(w.cget('show'))
                if cls == 'Treeview':record['rows']=[list(w.item(item,'values')) for item in w.get_children()]
                widgets.append(record)
            for child in w.winfo_children():
                if not isinstance(child, tk.Toplevel): visit(child)
        visit(window)
        windows.append({'title': window.title(), 'widgets': widgets})
    inspect(root)
    for child in root.winfo_children():
        if isinstance(child, tk.Toplevel) and child.winfo_exists(): inspect(child)
    notebook=app.notebook
    points={}
    for y in (12,20,8,28):
        for x in range(2,notebook.winfo_width(),4):
            try:index=notebook.index(f'@{x},{y}')
            except tk.TclError:continue
            points.setdefault(index,[]).append((x,y))
        if len(points)==notebook.index('end'):break
    tab_points=[]
    for index,coords in points.items():
        x,y=coords[len(coords)//2]
        tab_points.append({'text':notebook.tab(index,'text'),'x':notebook.winfo_rootx()+x,'y':notebook.winfo_rooty()+y})
    state = {'screen': [root.winfo_screenwidth(), root.winfo_screenheight()], 'windows': windows, 'status': app.status.get(), 'busy': app.busy,
             'running': app.running, 'log_text':app.log.get('1.0','end-1c'), 'power_active':app.sleep_guard.active,'power_supported':app.sleep_guard.supported,'power_error':app.sleep_guard.error, 'schedule_status':app.schedule_status.get(),
             'schedule_skipped':app.cadence.skipped if app.cadence else 0,
             'schedule_delay_seconds':app.cadence.delay(time.monotonic()) if app.cadence else None, 'order_notice':app.order_notice.get(), 'context':app.context.get(), 'freshness':app.freshness.get(), 'account_error':app.account_error, 'stop_failed':app.stop_failed, 'cards': {k:v.get() for k,v in app.values.items()},
             'tables': {k:[list(t.item(i,'values')) for i in t.get_children()] for k,t in app.tables.items()},
             'visible_tables':{k:bool(t.winfo_ismapped()) for k,t in app.tables.items()},
             'table_heights':{k:t.winfo_height() for k,t in app.tables.items()},
             'notebook_tabs':tab_points,
             'review_cases':list(app.review_items.values()),
             'demo_summary': app.demo_summary.get(), 'submitted': OfflineBroker.calls,
             'read_calls':OfflineBroker.read_calls,
             'stop': (Path(app.config['state_dir'])/'STOP').exists()}
    target = OUT / 'state.json'
    tmp = OUT / 'state.tmp'
    tmp.write_text(json.dumps(state, ensure_ascii=False), encoding='utf-8')
    try:
        os.replace(tmp, target)
    except PermissionError:
        # Windows readers can temporarily deny replacement; retry on the next tick.
        pass
    control = OUT / 'control.json'
    if control.exists():
        try:
            settings=json.loads(control.read_text())
            if settings.get('late_schedule') and app.running and not app.busy and app.cadence and not OfflineBroker.late_schedule_injected:
                # Simulate a delayed callback, not actual OS suspension or real trading.
                OfflineBroker.late_schedule_injected=True
                app.cadence.next_due-=3600
                app.schedule_trade()
            OfflineBroker.budget_timeout=settings.get('budget_timeout',False)
            OfflineBroker.flat_strategy=settings.get('flat_strategy',False)
            if settings.get('run_for_budget_test') and app.running and not app.busy and not OfflineBroker.budget_run_injected:
                OfflineBroker.budget_run_injected=True
                app.cadence.next_due=time.monotonic()-1
                app.schedule_trade()
            OfflineBroker.power_fail=settings.get('power_fail',False)
            OfflineBroker.fail=settings.get('fail',False)
            OfflineBroker.partial=settings.get('partial',False)
            OfflineBroker.delay=settings.get('delay',0)
            OfflineBroker.missing=settings.get('missing',False)
            OfflineBroker.holding_extra=settings.get('holding_extra',0)
            OfflineBroker.root_replaced=settings.get('root_replaced',False)
            OfflineBroker.price_changed=settings.get('price_changed',False)
            if settings.get('closed_flat') and not OfflineBroker.closed_flat:
                # Offline fixture only: account and bracket histories agree that all exposure exited.
                for order in OfflineBroker.saved_orders.values():
                    order['status']='canceled'
                    if not order.get('legs') and float(order['filled_qty'])>0:
                        order['legs']=[{'id':order['id']+'-tp','symbol':order['symbol'],'side':'sell','type':'limit','time_in_force':'day','qty':order['qty'],'filled_qty':order['filled_qty'],'status':'canceled','limit_price':order['take_profit']['limit_price']},{'id':order['id']+'-sl','symbol':order['symbol'],'side':'sell','type':'stop','time_in_force':'day','qty':order['qty'],'filled_qty':'0','status':'canceled','stop_price':order['stop_loss']['stop_price']}]
                    for leg in order.get('legs',[]):leg['status']='canceled'
                OfflineBroker.closed_flat=True
            if settings.get('inject_unknown') and not OfflineBroker.injected:
                import sqlite3
                from stockbot.paper_journal import intent,submission_uncertain
                payload={'symbol':'MSFT','qty':'2','side':'buy','type':'limit','limit_price':'100','time_in_force':'day','order_class':'bracket','client_order_id':'gui-response-lost-MSFT','take_profit':{'limit_price':'110'},'stop_loss':{'stop_price':'90'}}
                with closing(sqlite3.connect(Path(app.config['state_dir'])/'orders.sqlite')) as db:
                    intent(db,payload['client_order_id'],payload)
                    submission_uncertain(db,payload['client_order_id'])
                    db.commit()
                OfflineBroker.saved_orders[payload['client_order_id']]={**payload,'id':'gui-broker-uncertain','filled_qty':'1','status':'partially_filled'}
                OfflineBroker.injected=True
        except (ValueError, OSError): pass
    root.after(100, snapshot)
root.after(100, snapshot)
root.mainloop()
