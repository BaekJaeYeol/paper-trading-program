"""Launch real Tk widgets with an offline broker and export state for external UI tests."""
import json
import os
import socket
import sys
import tkinter as tk
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tests'))
from test_bot import FakeBroker
import stockbot.gui as gui

OUT = ROOT / 'gui-check'
OUT.mkdir(exist_ok=True)
import shutil
shutil.copytree(ROOT / "examples", OUT / "examples", dirs_exist_ok=True)
config = json.loads((ROOT / 'config.json').read_text())
config['symbols'] = ['AAPL']
config['state_dir'] = str(OUT / 'state')
path = OUT / 'config.json'
path.write_text(json.dumps(config), encoding='utf-8')
for key in ('APCA_API_KEY_ID', 'APCA_API_SECRET_KEY'):
    os.environ.pop(key, None)

class OfflineBroker(FakeBroker):
    fail = False
    calls = 0
    partial = False
    delay = 0
    def __init__(self): super().__init__()
    def request(self, path, params=None, body=None):
        if OfflineBroker.fail: raise RuntimeError('offline failure')
        if path=='/v2/account' and OfflineBroker.delay:
            import time
            time.sleep(OfflineBroker.delay)
        if path=='/v2/orders' and body is None and OfflineBroker.partial:
            return [{'symbol':'AAPL','side':'buy','qty':'10','filled_qty':'3','limit_price':'100','status':'partially_filled'}]
        result = super().request(path, params, body)
        if path == '/v2/account': result['cash'] = '8000'
        if body: OfflineBroker.calls += 1
        return result

gui.AlpacaPaper = OfflineBroker
import stockbot.cli as cli
cli.AlpacaPaper = OfflineBroker
# No outbound network is allowed from this process, even if an adapter changes.
def no_network(*args, **kwargs): raise RuntimeError('GUI verification blocks network')
socket.socket.connect = no_network
socket.create_connection = no_network
root = tk.Tk()
app = gui.Dashboard(root, path)

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
                widgets.append(record)
            for child in w.winfo_children():
                if not isinstance(child, tk.Toplevel): visit(child)
        visit(window)
        windows.append({'title': window.title(), 'widgets': widgets})
    inspect(root)
    for child in root.winfo_children():
        if isinstance(child, tk.Toplevel) and child.winfo_exists(): inspect(child)
    state = {'screen': [root.winfo_screenwidth(), root.winfo_screenheight()], 'windows': windows, 'status': app.status.get(), 'busy': app.busy,
             'running': app.running, 'context':app.context.get(), 'freshness':app.freshness.get(), 'account_error':app.account_error, 'stop_failed':app.stop_failed, 'cards': {k:v.get() for k,v in app.values.items()},
             'tables': {k:[list(t.item(i,'values')) for i in t.get_children()] for k,t in app.tables.items()},
             'demo_summary': app.demo_summary.get(), 'submitted': OfflineBroker.calls,
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
            OfflineBroker.fail=settings.get('fail',False)
            OfflineBroker.partial=settings.get('partial',False)
            OfflineBroker.delay=settings.get('delay',0)
        except (ValueError, OSError): pass
    root.after(100, snapshot)
root.after(100, snapshot)
root.mainloop()
