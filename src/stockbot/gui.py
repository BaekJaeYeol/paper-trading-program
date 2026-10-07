"""Windows desktop dashboard; all orders go through the existing paper-only broker."""
import json
import os
import queue
import threading
import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox, filedialog
from .broker import AlpacaPaper
from .cli import load_config, cycle, read_csv
from .core import backtest

BG = '#f3f5fa'
INK = '#17233b'
BLUE = '#315bea'
STATUS = {'ok': '조회 완료', 'market_closed': '미국 정규장 마감',
          'halted': '비상 중단 중', 'daily_loss_limit': '일일 손실 한도 도달'}


def account_view(broker):
    """Read-only snapshot. Never return credentials or account identifiers."""
    account = broker.request('/v2/account')
    clock = broker.request('/v2/clock')
    positions = broker.request('/v2/positions')
    orders = broker.request('/v2/orders', {'status': 'open', 'limit': 500, 'nested': 'false'})
    if len(orders) >= 500:
        raise ValueError('Order snapshot may be truncated')
    return {'equity': float(account['equity']), 'cash': float(account['cash']),
            'buying_power': float(account['buying_power']),
            'daily_pnl': float(account['equity']) - float(account['last_equity']),
            'market_open': clock['is_open'],
            'positions': [{k: p.get(k, '') for k in
                           ('symbol', 'qty', 'avg_entry_price', 'current_price', 'unrealized_pl')}
                          for p in positions],
            'orders': [{k: o.get(k, '') for k in
                        ('symbol', 'side', 'qty', 'filled_qty', 'limit_price', 'status')}
                       for o in orders]}


class Dashboard:
    def __init__(self, root, config_path='config.json'):
        self.root = root
        self.path = Path(config_path).resolve()
        self.config = load_config(self.path)
        self.config['state_dir'] = str((self.path.parent / self.config['state_dir']).resolve())
        self.events = queue.Queue()
        self.busy = False
        self.running = False
        self.timer = None
        self.closed = False
        root.title('모의매매 프로그램 · Paper Trading')
        root.geometry('1180x820')
        root.minsize(940, 700)
        root.configure(bg=BG)
        root.protocol('WM_DELETE_WINDOW', self.close)
        style = ttk.Style(root)
        style.theme_use('clam')
        style.configure('.', font=('맑은 고딕', 10))
        style.configure('TFrame', background=BG)
        style.configure('TLabel', background=BG, foreground=INK)
        style.configure('TButton', padding=(14, 10), background='white', foreground=INK)
        style.configure('Primary.TButton', background=BLUE, foreground='white')
        style.map('Primary.TButton', background=[('active', '#2545ba')])
        style.configure('Danger.TButton', background='#fce5e8', foreground='#b8223c')
        style.configure('Treeview', rowheight=34, background='white', fieldbackground='white')
        style.configure('Treeview.Heading', background='#e8edf6', padding=9)
        outer = ttk.Frame(root, padding=16)
        outer.pack(fill='both', expand=True)
        header = ttk.Frame(outer)
        header.pack(fill='x')
        ttk.Label(header, text='모의매매 프로그램', font=('맑은 고딕', 23, 'bold')).pack(side='left')
        ttk.Label(header, text='ALPACA PAPER  ·  모의계좌 전용', foreground=BLUE).pack(side='right')
        self.status = tk.StringVar(value='API 연결 전 · 데모로 먼저 둘러보세요')
        ttk.Label(outer, textvariable=self.status, padding=(0, 12)).pack(anchor='w')
        cards = ttk.Frame(outer)
        cards.pack(fill='x', pady=(4, 16))
        self.values = {}
        for title, key in [('총 자산 (USD)', 'equity'), ('현금 (USD)', 'cash'),
                           ('매수 가능 금액 (USD)', 'buying_power'), ('전일 대비 손익 (USD)', 'daily_pnl')]:
            box = tk.Frame(cards, bg='white', padx=20, pady=17, highlightbackground='#e1e6ef', highlightthickness=1)
            box.pack(side='left', fill='both', expand=True, padx=(0, 8))
            tk.Label(box, text=title, bg='white', fg='#718099', font=('맑은 고딕', 10)).pack(anchor='w')
            value = tk.StringVar(value='—')
            tk.Label(box, textvariable=value, bg='white', fg=INK, font=('맑은 고딕', 22, 'bold')).pack(anchor='w', pady=(9, 0))
            self.values[key] = value
        toolbar = ttk.Frame(outer)
        toolbar.pack(fill='x', pady=(0, 12))
        self.actions = []
        for title, fn, sty in [('API 연결', self.credentials, 'TButton'),
                               ('계좌 새로고침', self.refresh, 'TButton'),
                               ('후보 조회', self.scan, 'TButton'),
                               ('모의매매 시작', self.start, 'Primary.TButton'),
                               ('데모 / 백테스트', self.demo, 'TButton'),
                               ('설정', self.settings, 'TButton')]:
            button = ttk.Button(toolbar, text=title, command=fn, style=sty)
            button.pack(side='left', padx=(0, 6))
            self.actions.append(button)
        ttk.Button(toolbar, text='비상 중단', command=self.stop, style='Danger.TButton').pack(side='right')
        tabs = ttk.Notebook(outer)
        # Pack the expanding notebook last so the log/footer always reserve space.
        self.tables = {}
        specs = [('보유종목', 'positions', ['종목', '수량', '평균 매수가', '현재가', '평가손익']),
                 ('미체결 주문', 'orders', ['종목', '방향', '수량', '체결 수량', '지정가', '상태']),
                 ('주문 계획', 'plans', ['종목', '수량', '진입가', '손절가', '익절가', '제출 여부']),
                 ('백테스트', 'demo', ['날짜', '방향', '수량', '가격'])]
        for title, key, columns in specs:
            panel = ttk.Frame(tabs, padding=10)
            tabs.add(panel, text=title)
            table = ttk.Treeview(panel, columns=list(range(len(columns))), show='headings', height=4)
            for i, heading in enumerate(columns):
                table.heading(i, text=heading)
                table.column(i, width=140, anchor='center')
            scroll = ttk.Scrollbar(panel, orient='vertical', command=table.yview)
            table.configure(yscrollcommand=scroll.set)
            scroll.pack(side='right', fill='y')
            table.pack(fill='both', expand=True)
            self.tables[key] = table
        self.demo_summary = tk.StringVar(value='백테스트는 합성 데이터 예제입니다. 실제 계좌 성과와 다릅니다.')
        ttk.Label(outer, textvariable=self.demo_summary, padding=(0, 8)).pack(anchor='w', side='bottom')
        # Log is below the notebook and above the footer.
        self.log = tk.Text(outer, height=5, bg='white', fg=INK, relief='flat', padx=12, pady=9,
                           font=('맑은 고딕', 10), state='disabled')
        self.log.pack(fill='x', pady=(7, 8), side='bottom')
        ttk.Label(outer, text='비상 중단은 신규 주문을 멈춥니다. 이미 제출한 주문·보유종목은 Alpaca에서 확인하세요.',
                  foreground='#738099').pack(anchor='w', side='bottom')
        tabs.pack(fill='both', expand=True)
        root.after(100, self.poll)

    def write(self, text):
        self.log.configure(state='normal')
        self.log.insert('end', text + '\n')
        self.log.see('end')
        self.log.configure(state='disabled')

    def work(self, kind, fn):
        if self.busy:
            return False
        self.busy = True
        for button in self.actions:
            button.state(['disabled'])
        self.status.set('처리 중…')
        def worker():
            try:
                self.events.put((kind, fn(), None))
            except Exception:
                # Do not log arbitrary exception strings: third-party errors may contain secrets.
                self.events.put((kind, None, True))
        threading.Thread(target=worker, daemon=True).start()
        return True

    def fill(self, key, rows):
        table = self.tables[key]
        table.delete(*table.get_children())
        for row in rows:
            table.insert('', 'end', values=row)

    def poll(self):
        if self.closed:
            return
        try:
            while True:
                kind, data, error = self.events.get_nowait()
                self.busy = False
                for button in self.actions:
                    button.state(['!disabled'])
                if error:
                    self.pause()
                    self.status.set('작업 실패 · 자동 실행 정지')
                    self.write('연결/설정/주문 상태를 확인하세요. 주문 요청 실패 시 재전송 전에 Alpaca에서 실제 주문을 대조하세요.')
                elif kind == 'account':
                    for key, value in self.values.items():
                        value.set(f"${data[key]:,.2f}")
                    self.fill('positions', [[p[k] for k in ('symbol', 'qty', 'avg_entry_price', 'current_price', 'unrealized_pl')] for p in data['positions']])
                    self.fill('orders', [[o[k] for k in ('symbol', 'side', 'qty', 'filled_qty', 'limit_price', 'status')] for o in data['orders']])
                    self.status.set('모의계좌 연결됨 · ' + ('미국 정규장 개장' if data['market_open'] else '미국 정규장 마감'))
                    self.write('모의계좌 정보를 새로고침했습니다.')
                elif kind in ('scan', 'trade'):
                    self.fill('plans', [[r['order']['symbol'], r['order']['qty'], r['order']['limit_price'],
                                        r['order']['stop_loss']['stop_price'], r['order']['take_profit']['limit_price'],
                                        '제출됨' if r['submitted'] else '조회만'] for r in data.get('orders', [])])
                    label = STATUS.get(data['status'], data['status'])
                    if (Path(self.config['state_dir']) / 'STOP').exists():
                        label = '비상 중단 · 신규 주문 차단'
                    self.status.set(label + (' · 5분마다 실행 중' if self.running else ''))
                    self.write(f"{label} · 주문 계획 {len(data.get('orders', []))}건")
                    if self.running and kind == 'trade':
                        if data['status'] in ('halted', 'daily_loss_limit'):
                            self.pause()
                        else:
                            self.timer = self.root.after(300000, self.trade)
                elif kind == 'demo':
                    self.fill('demo', [[r['date'], r['side'], r['qty'], f"${r['price']:,.2f}"] for r in data['trades']])
                    self.demo_summary.set(f"백테스트 최종자산 ${data['ending_equity']:,.2f} · 최대 낙폭 {data['max_drawdown']:.2%} · 미청산 {data['open_qty']}주 · 실제 성과 아님")
                    self.status.set('백테스트 완료 · 계좌 주문 없음')
                    self.write('CSV 백테스트를 완료했습니다. 기본 파일은 합성 데이터입니다.')
        except queue.Empty:
            pass
        self.root.after(100, self.poll)

    def credentials(self):
        if self.running or self.busy:
            return
        window = tk.Toplevel(self.root)
        window.title('Alpaca 모의 API 연결')
        window.transient(self.root)
        window.grab_set()
        ttk.Label(window, text='Paper Trading API 키를 입력하세요.\n키는 파일에 저장하지 않고 현재 실행 중에만 사용합니다.', padding=18).pack()
        fields = []
        for title in ('API Key', 'Secret Key'):
            ttk.Label(window, text=title).pack(anchor='w', padx=18)
            entry = ttk.Entry(window, show='●', width=48)
            entry.pack(padx=18, pady=6)
            fields.append(entry)
        def apply():
            if not all(e.get().strip() for e in fields):
                messagebox.showerror('입력 확인', '두 키를 모두 입력하세요.', parent=window)
                return
            os.environ['APCA_API_KEY_ID'] = fields[0].get().strip()
            os.environ['APCA_API_SECRET_KEY'] = fields[1].get().strip()
            window.destroy()
            self.refresh()
        ttk.Button(window, text='연결 확인', command=apply, style='Primary.TButton').pack(pady=18)

    def refresh(self):
        self.work('account', lambda: account_view(AlpacaPaper()))

    def scan(self):
        self.work('scan', lambda: cycle(dict(self.config), False))

    def start(self):
        if self.running or self.busy:
            return
        if not messagebox.askyesno('모의매매 시작', 'Alpaca 모의계좌에 주문을 제출하고 5분마다 반복합니다.\n기존 PowerShell 반복 실행을 먼저 종료하세요.\n모의매매를 시작할까요?'):
            return
        stop = Path(self.config['state_dir']) / 'STOP'
        if stop.exists():
            if not messagebox.askyesno('비상 중단 해제', 'STOP 파일이 있습니다. 비상 중단을 해제하고 재개할까요?'):
                return
            stop.unlink()
        self.running = True
        self.write('모의매매를 시작합니다. 실계좌 주문은 실행하지 않습니다.')
        self.trade()

    def trade(self):
        self.timer = None
        if self.running and not self.work('trade', lambda: cycle(dict(self.config), True)):
            self.timer = self.root.after(1000, self.trade)

    def pause(self):
        self.running = False
        if self.timer is not None:
            self.root.after_cancel(self.timer)
            self.timer = None

    def stop(self):
        self.pause()
        root = Path(self.config['state_dir'])
        root.mkdir(parents=True, exist_ok=True)
        (root / 'STOP').touch()
        self.status.set('비상 중단 · 신규 주문 차단')
        self.write('STOP 파일 생성. 이미 통신 중인 주문과 기존 주문은 Alpaca에서 확인하세요.')

    def demo(self):
        selected = filedialog.askopenfilename(title='백테스트 CSV 선택 (취소하면 기본 합성 데이터)',
                                              initialdir=self.path.parent / 'examples', filetypes=[('CSV', '*.csv')])
        path = Path(selected) if selected else self.path.parent / 'examples/demo.csv'
        def run():
            bars = read_csv(path)
            if any(a.day >= b.day for a, b in zip(bars, bars[1:])):
                raise ValueError('CSV ordering')
            return backtest(bars, dict(self.config))
        self.work('demo', run)

    def settings(self):
        if self.running:
            messagebox.showinfo('설정 변경', '비상 중단 후 설정을 변경하세요.')
            return
        window = tk.Toplevel(self.root)
        window.title('전략 설정')
        window.transient(self.root)
        window.grab_set()
        fields = {}
        rows = [('symbols', '종목 (쉼표 구분)', ','.join(self.config['symbols'])),
                ('volume_ratio', '평균 대비 거래량 배수', self.config['volume_ratio']),
                ('max_return', '1개월 수익률 상한 (%)', self.config['max_return'] * 100),
                ('max_position_fraction', '종목별 최대 비중 (%)', self.config['max_position_fraction'] * 100),
                ('max_positions', '최대 보유 종목 수', self.config['max_positions']),
                ('max_daily_loss', '일일 손실 한도 (%)', self.config['max_daily_loss'] * 100),
                ('stop_loss', '손절 (%)', self.config['stop_loss'] * 100),
                ('take_profit', '익절 (%)', self.config['take_profit'] * 100)]
        for key, label, value in rows:
            row = ttk.Frame(window, padding=8)
            row.pack(fill='x')
            ttk.Label(row, text=label, width=28).pack(side='left')
            entry = ttk.Entry(row, width=36)
            entry.insert(0, str(value))
            entry.pack(side='right')
            fields[key] = entry
        def save():
            try:
                c = dict(self.config)
                c['symbols'] = [s.strip().upper() for s in fields['symbols'].get().split(',') if s.strip()]
                c['max_positions'] = int(fields['max_positions'].get())
                c['volume_ratio'] = float(fields['volume_ratio'].get())
                for key in ('max_return', 'max_position_fraction', 'max_daily_loss', 'stop_loss', 'take_profit'):
                    c[key] = float(fields[key].get()) / 100
                import math
                if any(not math.isfinite(v) for v in c.values() if isinstance(v, (int, float))):
                    raise ValueError('Nonfinite')
                # Validate using the CLI rules before touching the user's original file.
                import tempfile
                with tempfile.TemporaryDirectory() as temp:
                    candidate = Path(temp) / 'config.json'
                    candidate.write_text(json.dumps(c))
                    load_config(candidate)
                c['state_dir'] = os.path.relpath(self.config['state_dir'], self.path.parent)
                self.path.write_text(json.dumps(c, indent=2), encoding='utf-8')
                c['state_dir'] = self.config['state_dir']
                self.config = c
            except (ValueError, OSError):
                messagebox.showerror('설정 오류', '종목과 숫자 범위를 확인하세요. 설정 파일을 쓸 수 있는지도 확인하세요.', parent=window)
                return
            window.destroy()
            self.write('전략 설정을 저장했습니다.')
        ttk.Button(window, text='설정 저장', command=save, style='Primary.TButton').pack(pady=15)

    def close(self):
        if self.busy or self.running:
            if not messagebox.askyesno('종료', '신규 주문을 중단하고 종료할까요?\n이미 제출한 주문은 유지됩니다.'):
                return
            self.stop()
            if self.busy:
                messagebox.showinfo('종료 대기', '통신 완료 후 창을 다시 닫아 주세요. 주문 기록을 안전하게 마무리합니다.')
                return
        self.closed = True
        self.root.destroy()


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='config.json')
    args = parser.parse_args()
    root = tk.Tk()
    try:
        Dashboard(root, args.config)
    except Exception:
        messagebox.showerror('실행 오류', '프로젝트 폴더에서 실행하고 config.json 내용을 확인하세요.')
        root.destroy()
        return
    root.mainloop()


if __name__ == '__main__':
    main()
