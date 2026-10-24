"""Windows desktop dashboard; all orders go through the existing paper-only broker."""
import json
import os
import queue
import threading
import time
import math
from datetime import datetime,timedelta
from zoneinfo import ZoneInfo
from .ui_safety import order_row, resume_snapshot, unresolved_attempts
import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox, filedialog
from .broker import AlpacaPaper
from .kis import KISPaper
from .cli import load_config, cycle, read_csv
from .core import backtest
from .paper_journal import fingerprint,reconcile_snapshot,ReconciliationTimeout
from . import diagnostics,health
from .cadence import Cadence
from .strategies import LABELS
from .power import SleepGuard

BG = '#f3f5fa'
INK = '#17233b'
BLUE = '#315bea'
STATUS = {'ok': '조회 완료', 'market_closed': '미국 정규장 마감',
          'reconciliation_required':'주문·보유 수량 대조 필요','halted': '비상 중단 중', 'daily_loss_limit': '일일 손실 한도 도달'}


def account_view(broker):
    from .paper_journal import account_snapshot
    return account_snapshot(broker)


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
        self.cadence=None
        self.sleep_guard=SleepGuard()
        self.closed = False
        self.stop_event=threading.Event()
        self.resume_pending=False
        self.diagnostic_snapshot=None
        self.diagnostic_time=None
        self.last_account_time=None
        self.last_account_label="미조회"
        self.account_error=False
        self.stop_failed=False
        self.entry_blocked=False
        self.market = tk.StringVar(value="미국 · Alpaca")
        self.kis = None
        root.title('모의매매 프로그램 · Paper Trading')
        width = min(1180, max(940, root.winfo_screenwidth() - 32))
        height = min(820, max(620, root.winfo_screenheight() - 100))
        compact=height<760
        root.geometry(f'{width}x{height}+8+8')
        root.minsize(940, 620)
        root.configure(bg=BG)
        root.protocol('WM_DELETE_WINDOW', self.close)
        style = ttk.Style(root)
        style.theme_use('clam')
        style.configure('.', font=('맑은 고딕', 10))
        style.configure('TFrame', background=BG)
        style.configure('TLabel', background=BG, foreground=INK)
        style.configure('TButton', padding=(10, 8) if compact else (14, 10), background='white', foreground=INK)
        style.configure('Primary.TButton', background=BLUE, foreground='white')
        style.map('Primary.TButton', background=[('active', '#2545ba')])
        style.configure('Danger.TButton', background='#fce5e8', foreground='#b8223c')
        style.configure('Treeview', rowheight=28 if compact else 34, background='white', fieldbackground='white')
        style.configure('Treeview.Heading', background='#e8edf6', padding=6 if compact else 9)
        outer = ttk.Frame(root, padding=12 if compact else 16)
        outer.pack(fill='both', expand=True)
        header = ttk.Frame(outer)
        header.pack(fill='x')
        ttk.Label(header, text='모의매매 프로그램', font=('맑은 고딕', 20 if compact else 23, 'bold')).pack(side='left')
        selector = ttk.Combobox(header, textvariable=self.market,
                                values=('미국 · Alpaca', '한국 · KIS'), state='readonly', width=18)
        selector.pack(side='right')
        selector.bind('<<ComboboxSelected>>', self.change_market)
        self.selector = selector
        self.status = tk.StringVar(value='API 연결 전 · 데모로 먼저 둘러보세요')
        ttk.Label(outer, textvariable=self.status, padding=(0, 6 if compact else 12),wraplength=880).pack(anchor='w')
        self.context=tk.StringVar(value='모의투자 · Alpaca Paper · 미국 모의계좌 · USD · 실계좌 주문 비활성화')
        ttk.Label(outer,textvariable=self.context,foreground='#2545ba',wraplength=880).pack(anchor='w')
        self.schedule_status=tk.StringVar(value='자동 실행 대기 · 시작 전 계좌·주문 대조')
        ttk.Label(outer,textvariable=self.schedule_status,foreground='#526079',wraplength=880).pack(anchor='w')
        self.freshness=tk.StringVar(value='계좌 데이터 미조회 · 수신 시각과 시세 기준 시각은 다릅니다.')
        ttk.Label(outer,textvariable=self.freshness,foreground='#526079',wraplength=880).pack(anchor='w',pady=(2,6))
        cards = ttk.Frame(outer)
        cards.pack(fill='x', pady=(4, 8 if compact else 16))
        self.values = {}
        self.card_titles = {}
        for title, key in [('총 자산 (USD)', 'equity'), ('현금 (USD)', 'cash'),
                           ('매수 가능 금액 (USD)', 'buying_power'), ('전일 대비 손익 (USD)', 'daily_pnl')]:
            box = tk.Frame(cards, bg='white', padx=14 if compact else 20, pady=10 if compact else 17, highlightbackground='#e1e6ef', highlightthickness=1)
            box.pack(side='left', fill='both', expand=True, padx=(0, 8))
            label = tk.Label(box, text=title, bg='white', fg='#718099', font=('맑은 고딕', 10))
            label.pack(anchor='w')
            self.card_titles[key] = label
            value = tk.StringVar(value='—')
            tk.Label(box, textvariable=value, bg='white', fg=INK, font=('맑은 고딕', 18 if compact else 22, 'bold')).pack(anchor='w', pady=(9, 0))
            self.values[key] = value
        toolbar = ttk.Frame(outer)
        toolbar.pack(fill='x', pady=(0, 12))
        self.actions = []
        for title, fn, sty in [('API 연결', self.credentials, 'TButton'),
                               ('계좌·주문 대조', self.refresh, 'TButton'),
                               ('후보 조회', self.scan, 'TButton'),
                               ('모의매매 시작', self.start, 'Primary.TButton'),
                               ('데모 / 백테스트', self.demo, 'TButton'),
                               ('설정', self.settings, 'TButton')]:
            button = ttk.Button(toolbar, text=title, command=fn, style=sty)
            button.pack(side='left', padx=(0, 6))
            self.actions.append(button)
        ttk.Button(toolbar, text='비상 중단', command=self.stop, style='Danger.TButton').pack(side='right')
        tabs = ttk.Notebook(outer)
        tabs.enable_traversal()
        self.notebook=tabs
        root.bind('<Control-Tab>',lambda event:self.navigate_tabs(1))
        root.bind('<Control-Shift-Tab>',lambda event:self.navigate_tabs(-1))
        # Pack the expanding notebook last so the log/footer always reserve space.
        self.tables = {}
        self.review_items={}
        specs = [('보유종목', 'positions', ['종목', '수량', '평균 매수가', '현재가', '평가손익']),
                 ('미체결 주문', 'orders', ['종목', '방향', '주문 수량', '체결 수량', '잔여 수량', '지정가', '상태']),
                 ('주문 계획', 'plans', ['종목', '수량', '진입가', '손절가', '익절가', '제출 여부']),
                 ('봇 주문 추적', 'history', ['종목','주문 수량','체결 수량','잔여 수량','대조 상태','봇 주문 키','확인 시각 (KST)']),
                 ('보유 수량 대조','inventory',['종목','봇 기대 수량','계좌 실제 수량','대조 결과']),
                 ('주문 변경 기록', 'timeline', ['봇 주문 키','대조 결과','주문 상태','체결 수량','확인 시각 (KST)']),
                 ('차단 상세','review',['대상 주문/종목','확인된 변화','상태','마지막 확인 (KST)']),
                 ('운영 상태','health',['마지막 확인 (KST)','운영 상태','반복 횟수']),
                 ('백테스트', 'demo', ['날짜', '방향', '수량', '가격'])]
        for title, key, columns in specs:
            panel = ttk.Frame(tabs, padding=6 if compact else 10)
            tabs.add(panel, text=title)
            if key=='review':
                bar=ttk.Frame(panel);bar.pack(fill='x',pady=(0,4))
                ttk.Button(bar,text='진단 요약 저장',command=self.export_diagnostics).pack(side='left')
                recovery=ttk.Button(bar,text='선택 기록 복구 점검',command=self.recover_review)
                recovery.pack(side='left',padx=6);self.actions.append(recovery)
            if key=='demo':
                research=ttk.Button(panel,text='전략 비교 (연구용)',command=self.research)
                research.pack(anchor='w',pady=(0,4));self.actions.append(research)
            if key=='health':
                self.health_notice=tk.StringVar(value='미국 Alpaca 모의 대조 이력 · 최대 최근 50개 상태 묶음 · 자동 재개 아님')
                ttk.Label(panel,textvariable=self.health_notice,wraplength=850).pack(anchor='w')
                ttk.Button(panel,text='운영 이력 새로고침',command=self.refresh_health).pack(anchor='w',pady=(0,4))
            table = ttk.Treeview(panel, columns=list(range(len(columns))), show='headings', height=4)
            for i, heading in enumerate(columns):
                table.heading(i, text=heading)
                table.column(i, width=min(140,860//len(columns)), minwidth=70, anchor='center')
            scroll = ttk.Scrollbar(panel, orient='vertical', command=table.yview)
            table.configure(yscrollcommand=scroll.set)
            scroll.pack(side='right', fill='y')
            if key in ('history','timeline'):
                table.column(5 if key=='history' else 0,width=220,minwidth=120)
                table.column(6 if key=='history' else 4,width=220,minwidth=120)
                horizontal=ttk.Scrollbar(panel,orient='horizontal',command=table.xview)
                table.configure(xscrollcommand=horizontal.set)
                horizontal.pack(side='bottom',fill='x')
            table.pack(fill='both', expand=True)
            self.tables[key] = table
            if key=='health':
                self.health_items={}
                table.column(0,width=260);table.column(1,width=330)
                table.bind('<Return>',self.show_health_detail)
                table.bind('<Double-1>',self.show_health_detail)
            if key=='review':
                table.bind('<Return>',self.show_review_detail)
                table.bind('<Double-1>',self.show_review_detail)
        self.order_notice=tk.StringVar(value='미체결 주문 미조회 · 빈 표는 조회 성공을 의미하지 않습니다.')
        ttk.Label(outer,textvariable=self.order_notice,foreground='#526079',wraplength=880).pack(anchor='w',side='bottom')
        self.demo_summary = tk.StringVar(value='백테스트는 합성 데이터 예제입니다. 실제 계좌 성과와 다릅니다.')
        ttk.Label(outer, textvariable=self.demo_summary, padding=(0, 8)).pack(anchor='w', side='bottom')
        # Log is below the notebook and above the footer.
        self.log = tk.Text(outer, height=3 if compact else 5, bg='white', fg=INK, relief='flat', padx=12, pady=9,
                           font=('맑은 고딕', 10), state='disabled')
        self.log.pack(fill='x', pady=(7, 8), side='bottom')
        ttk.Label(outer, text='비상 중단은 신규 주문을 멈춥니다. 이미 제출한 주문·보유종목은 해당 증권사에서 확인하세요.',
                  foreground='#738099').pack(anchor='w', side='bottom')
        tabs.pack(fill='both', expand=True)
        self.refresh_health()
        root.after(100, self.poll)

    def navigate_tabs(self,direction):
        current=self.notebook.index(self.notebook.select())
        self.notebook.select((current+direction)%self.notebook.index('end'))
        self.notebook.focus_set()
        return 'break'

    def write(self, text):
        self.log.configure(state='normal')
        self.log.insert('end', text + '\n')
        if int(self.log.index('end-1c').split('.')[0])>1000:self.log.delete('1.0','201.0')
        self.log.see('end')
        self.log.configure(state='disabled')

    def work(self, kind, fn):
        if self.busy:
            return False
        self.busy = True
        self.read_cancel=threading.Event()
        for button in self.actions:
            button.state(['disabled'])
        self.selector.configure(state='disabled')
        self.status.set('처리 중…')
        def worker():
            try:
                self.events.put((kind, fn(), None))
            except ReconciliationTimeout:
                self.events.put((kind,None,'reconciliation_timeout'))
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
                self.selector.configure(state='disabled' if self.running else 'readonly')
                if error and kind=='research':
                    self.status.set('전략 연구 실패 · CSV와 비용·데이터 범위를 확인하세요.')
                    self.write('연구 입력은 날짜가 증가하는 일봉 300~5000개가 필요합니다. 계좌·주문·설정은 변경하지 않았습니다.')
                elif error:
                    self.resume_pending=False
                    self.account_error=True
                    self.pause()
                    if kind=='resume':
                        try:count=len(unresolved_attempts(self.config['state_dir']))
                        except Exception:count=None
                        self.order_notice.set(f'재개 차단 · 미확인 주문 {count}건 · 증권사 대조 필요' if count else '재개 점검 실패 · 계좌 권한·잔고·미체결·잠금을 확인하세요.')
                    self.status.set('작업 실패 · 자동 실행 정지')
                    self.write('연결 실패: 선택 시장의 모의투자 키·계좌번호·네트워크를 확인하세요. 주문 실패 시 증권사에서 주문 상태를 먼저 확인하세요.')
                    self.refresh_health()
                    if error=='reconciliation_timeout':
                        self.order_notice.set('전체 대조 60초 시간 제한 초과 · 자동 실행 중지 · 계좌·주문을 다시 대조한 뒤 명시적으로 재개하세요.')
                        self.status.set('대조 시간 초과 · 자동 실행 정지')
                        self.write('오래된 대조 결과로 주문하지 않았습니다. 밀린 예약은 재실행하지 않습니다.')
                elif kind == 'resume':
                    self.render_journal(data)
                    self.finish_resume(data)
                elif kind == 'account':
                    self.account_error=False
                    self.last_account_time=data.get('received_monotonic',time.monotonic())
                    self.last_account_label=data.get('received_at',datetime.now(ZoneInfo('Asia/Seoul')).isoformat())
                    kr = self.market.get().startswith('한국')
                    for key, value in self.values.items():
                        number = data[key]
                        value.set('미조회' if number is None else (f"₩{number:,.0f}" if kr else f"${number:,.2f}"))
                    self.fill('positions', [[p[k] for k in ('symbol', 'qty', 'avg_entry_price', 'current_price', 'unrealized_pl')] for p in data['positions']])
                    self.fill('orders', [order_row(o) for o in data['orders']])
                    self.order_notice.set('미체결 주문 미조회 · 한국 잔고 조회 전용' if kr else f"브로커 조회 완료 · 미체결 {len(data['orders'])}건 · 취소 기능은 수행하지 않음")
                    self.status.set('한국 모의계좌 연결됨 · 잔고 조회 전용 · 미체결 주문 미조회' if kr else
                                    '모의계좌 연결됨 · ' + ('미국 정규장 개장' if data['market_open'] else '미국 정규장 마감'))
                    self.render_journal(data)
                    self.write('모의계좌 정보를 새로고침했습니다.')
                elif kind in ('scan', 'trade'):
                    self.fill('plans', [[r['order']['symbol'], r['order']['qty'], r['order']['limit_price'],
                                        r['order']['stop_loss']['stop_price'], r['order']['take_profit']['limit_price'],
                                        '제출됨' if r['submitted'] else '조회만'] for r in data.get('orders', [])])
                    label = STATUS.get(data['status'], data['status'])
                    if (Path(self.config['state_dir']) / 'STOP').exists():
                        label = '비상 중단 · 신규 주문 차단'
                    if kind=='trade' and data['status'] in ('halted','daily_loss_limit','reconciliation_required'):self.pause()
                    self.status.set(label + (' · 5분 기준 예약 실행 중' if self.running else ''))
                    self.write(f"{label} · 주문 계획 {len(data.get('orders', []))}건")
                    if 'entry_filter' in data:
                        info=data['entry_filter'];excluded=sum(info['excluded'].values())
                        self.write(f"진입 필터: {LABELS[info['strategy']]} · 기본 신호 통과 후 제외 {excluded}종목 · 수익 우위 미검증")
                    if 'account_snapshot' in data:self.render_journal(data['account_snapshot'])
                    if self.running and kind == 'trade':
                        if data['status'] in ('halted', 'daily_loss_limit','reconciliation_required'):
                            self.pause()
                        else:
                            self.cadence.complete(time.monotonic())
                            self.schedule_trade()
                elif kind=='research':
                    self.show_research(data)
                    self.status.set('전략 연구 완료 · 실제 시장 개선 미검증 · 자동 적용 없음')
                elif kind == 'demo':
                    self.fill('demo', [[r['date'], r['side'], r['qty'], f"${r['price']:,.2f}"] for r in data['trades']])
                    self.demo_summary.set(f"백테스트 최종자산 ${data['ending_equity']:,.2f} · 최대 낙폭 {data['max_drawdown']:.2%} · 미청산 {data['open_qty']}주 · 실제 성과 아님")
                    self.status.set('백테스트 완료 · 계좌 주문 없음')
                    self.write('CSV 백테스트를 완료했습니다. 기본 파일은 합성 데이터입니다.')
        except queue.Empty:
            pass
        guard=getattr(self,'sleep_guard',None)
        if not self.running and not self.busy and guard and guard.active and guard.error!='release':guard.release()
        self.update_safety_display()
        self.root.after(100, self.poll)

    def render_journal(self,data):
        if 'system_health' in data:self.render_health(data['system_health'])
        if 'order_history' not in data:return
        # Build the allowlisted summary immediately; never retain account IDs or raw payloads.
        self.diagnostic_snapshot=diagnostics.build(data,age_seconds=0,read_failed=False,stopped=False,running=False)
        self.diagnostic_time=data.get('received_monotonic',time.monotonic())
        self.fill('history',[[r[k] for k in ('symbol','qty','filled_qty','remaining_qty','status','client_id','checked_at')] for r in data['order_history']])
        self.fill('timeline',[[r[k] for k in ('client_id','kind','status','filled_qty','checked_at')] for r in data['order_events']])
        r=data['reconciliation']
        self.order_notice.set(f"읽기 대조: 확인 {r['checked']}건 / 미확인 {r['unresolved']}건 / 이전 형식 {r['legacy']}건 · 중단 상태 변경 없음 · 주문 재전송/취소 없음")
        if 'review' in data:
            table=self.tables['review'];table.delete(*table.get_children());self.review_items={}
            for case in data['review']['cases']:
                item=table.insert('','end',values=(case['target'],case['title'],'검토 필요 · 차단 유지' if case['active'] else '해소 이력',case['last_seen']))
                self.review_items[item]=case
        inv=data.get('inventory')
        if inv:
            self.entry_blocked=not inv['ready']
            self.fill('inventory',[[r['symbol'],r['expected'],r['actual'],'일치' if r['matched'] else '불일치 · 재개 차단'] for r in inv['rows']])
            self.order_notice.set(self.order_notice.get()+' / 수량 대조: '+inv['reason'])
        self.write('계좌·주문 대조 결과를 갱신했습니다. 대조 완료는 자동매매 재개가 아닙니다.')
        if data.get('review_resolution',{}).get('resolved'):
            self.write('선택 기록의 복구 점검 통과 · 해소 이력 저장 · STOP 유지 · 자동매매는 재개하지 않았습니다.')

    def refresh_health(self):
        self.render_health(health.load(self.config['state_dir']))

    def render_health(self,data):
        if 'health' not in getattr(self,'tables',{}):return
        if not data['available']:
            self.health_notice.set('미국 모의 운영 이력 조회 실패 · 이전 표가 남아 있을 수 있습니다. DB 상태를 확인하세요.');return
        self.health_notice.set('미국 Alpaca 모의 대조 이력 · 최근 최대 50개 상태 묶음 · 복구 기록은 자동 재개가 아닙니다.' if data['events'] else '미국 모의 대조 장애 이력 없음 · 정상 연결을 의미하지 않습니다.')
        table=self.tables['health'];table.delete(*table.get_children());self.health_items={}
        for event in data['events']:
            item=table.insert('','end',values=(event['last_seen'],event['title'],event['occurrences']))
            self.health_items[item]=event

    def show_health_detail(self,event=None):
        table=self.tables['health'];selected=table.selection()
        record=self.health_items.get(selected[0]) if selected else None
        if record:
            messagebox.showinfo('운영 상태 · 읽기 전용',f"{record['title']}\n최초 확인: {record['first_seen']}\n마지막 확인: {record['last_seen']}\n같은 상태 반복: {record['occurrences']}회\n\n{record['next_action']}\n\n이 창을 닫아도 주문·STOP·차단·실행 상태는 바뀌지 않습니다.",parent=self.root)
            table.focus_set()
        return 'break'

    def recover_review(self):
        if self.busy or self.running:return
        if self.market.get().startswith('한국') or not (Path(self.config['state_dir'])/'STOP').is_file():
            messagebox.showinfo('복구 점검', '미국 모의계좌에서 비상 중단을 적용한 뒤 진행하세요.',parent=self.root);return
        selected=self.tables['review'].selection()
        case=self.review_items.get(selected[0]) if selected else None
        if not case or not case.get('recovery_supported'):
            messagebox.showinfo('복구 점검', '복구 가능한 활성 가격·주문 조건 기록을 선택하세요. 정정·교체·ID·수량·체결 변경은 이 절차로 해제할 수 없습니다.',parent=self.root);return
        if not messagebox.askyesno('선택 기록 복구 점검', '증권사에서 원래 주문 조건과 체결 내역을 직접 확인했습니까?\n모든 주문 종료·미체결 없음·관리 대상 보유 없음·원래 조건 일치를 새로 대조합니다.\n선택 기록만 해소하며 STOP은 유지하고 자동매매를 재개하지 않습니다.\n확인 후 복구 점검을 진행할까요?',parent=self.root):return
        selection=(case['target'],case['code'],case['version'])
        self.work('account',lambda:reconcile_snapshot({**self.config,'_reconcile_cancel':self.read_cancel},AlpacaPaper(),account_view,resolve_case=selection))

    def export_diagnostics(self):
        if self.busy:
            messagebox.showinfo('진단 요약', '대조 작업이 끝난 뒤 저장하세요.',parent=self.root)
            return
        if self.diagnostic_snapshot is None:
            messagebox.showinfo('진단 요약', '미국 모의계좌의 계좌·주문 대조를 먼저 실행하세요.',parent=self.root)
            return
        target=filedialog.asksaveasfilename(parent=self.root,title='진단 요약 저장',defaultextension='.json',filetypes=[('JSON 보고서','*.json')],initialfile='paper-diagnostics.json')
        if not target:return
        destination=Path(target).resolve()
        state=Path(self.config['state_dir']).resolve()
        if destination.suffix.lower()!='.json' or destination==self.path.resolve() or destination==state or state in destination.parents:
            messagebox.showerror('진단 요약', '설정 파일과 상태 폴더 밖의 JSON 파일을 선택하세요.',parent=self.root)
            return
        report=dict(self.diagnostic_snapshot)
        report['system_health']=health.summary(health.load(self.config['state_dir']))
        guard=getattr(self,'sleep_guard',None)
        report['sleep_prevention']={'supported':bool(guard and guard.supported),'requested':bool(guard and guard.active),'error':guard.error if guard and guard.error in ('acquire','release') else None}
        report.update(generated_at=datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
                      snapshot_age_seconds=max(0,int(time.monotonic()-self.diagnostic_time)),
                      read_failed_since_snapshot=bool(self.account_error),
                      stop_requested=self.stop_event.is_set() or (state/'STOP').exists(),
                      automatic_paper_running=bool(self.running))
        report['stale']=report['read_failed_since_snapshot'] or report['snapshot_age_seconds']>=60
        try:diagnostics.write_report(destination,report)
        except (OSError,ValueError):
            messagebox.showerror('진단 요약', '저장하지 못했습니다. 폴더 권한과 파일 사용 여부를 확인하세요.',parent=self.root)
            return
        messagebox.showinfo('진단 요약', '식별정보를 제외한 모의계좌 진단 요약을 저장했습니다. 캐시된 정보이며 주문·재개 상태는 바뀌지 않습니다.',parent=self.root)

    def show_review_detail(self,event=None):
        table=self.tables['review'];selection=table.selection()
        if not selection:return 'break'
        case=self.review_items.get(selection[0])
        if not case:return 'break'
        messagebox.showinfo('차단 상세 · 읽기 전용',f"{case['title']}\n대상: {case['target']}\n저장값: {case['expected']}\n조회값: {case['observed']}\n최초 확인: {case['first_seen']}\n마지막 확인: {case['last_seen']}\n변경 기록: {case['occurrences']}회\n\n{case['next_action']}\n\n이 창을 닫아도 차단은 해제되지 않습니다. 기업행위 원인 확정·자동 보정·재전송은 수행하지 않습니다.",parent=self.root)
        table.focus_set();return 'break'

    def update_safety_display(self):
        kr=self.market.get().startswith('한국')
        execution='중단' if self.stop_event.is_set() or (Path(self.config['state_dir'])/'STOP').exists() else ('재개 점검 중' if self.resume_pending else ('자동 모의매매' if self.running else ('대조 차단' if getattr(self,'entry_blocked',False) else '대기')))
        self.context.set('실행: '+execution+' · 모의투자 · '+('KIS · 한국 모의계좌 · KRW · 잔고 조회 전용' if kr else 'Alpaca Paper · 미국 모의계좌 · USD')+' · 실계좌 주문 비활성화'+('' if kr else ' · 진입: '+LABELS[self.config.get('entry_strategy','baseline')]))
        if self.last_account_time is None:self.freshness.set('계좌 데이터 미조회 · 시세 신선도는 엔진에서 별도 검증')
        else:
            age=max(0,int(time.monotonic()-self.last_account_time))
            state='조회 실패 · 이전 데이터' if self.account_error else ('오래된 계좌 정보' if age>=60 else '정상 수신')
            self.freshness.set(f'{state} · 마지막 정상 수신 {self.last_account_label} · {age}초 경과 / KST')
        if hasattr(self,'schedule_status'):
            cadence=getattr(self,'cadence',None)
            if self.running and cadence:
                if cadence.in_flight:label='자동 실행 처리 중 · 다음 예약은 완료 후 확인'
                else:
                    remaining=math.ceil(cadence.delay(time.monotonic()))
                    due=datetime.now(ZoneInfo('Asia/Seoul'))+timedelta(seconds=remaining)
                    label=f'다음 실행 {due:%H:%M:%S} KST · 약 {remaining}초 후'
                guard=getattr(self,'sleep_guard',None)
                self.schedule_status.set(label+f' · 건너뛴 예약 {cadence.skipped}회'+(' · '+guard.label() if guard else ''))
            else:
                guard=getattr(self,'sleep_guard',None)
                self.schedule_status.set('자동 실행 중지 · 밀린 예약 재실행 없음'+(' · '+guard.label() if guard else ''))
        if self.stop_failed:self.status.set('중단 기록 실패 · 이 창의 실행은 차단됨 · 다른 프로세스와 증권사 주문을 확인하세요.')
        elif (Path(self.config['state_dir'])/'STOP').exists():self.status.set('비상 중단 · 신규 주문 차단 확인 · 기존 주문 취소·보유종목 청산은 수행하지 않음')

    def credentials(self):
        if self.running or self.busy:
            return
        if self.market.get().startswith('한국'):
            return self.kis_credentials()
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

    def change_market(self, event=None):
        self.diagnostic_snapshot=None
        self.diagnostic_time=None
        self.last_account_time=None
        self.account_error=False
        self.order_notice.set('미체결 주문 미조회')
        for value in self.values.values():
            value.set('—')
        for key in self.tables:
            self.fill(key, [])
        kr = self.market.get().startswith('한국')
        titles = {'equity':'총 자산', 'cash':'예수금' if kr else '현금',
                  'buying_power':'매수 가능 금액', 'daily_pnl':'전일 대비 손익'}
        for key, label in self.card_titles.items():
            label.configure(text=titles[key] + (' (KRW)' if kr else ' (USD)'))
        self.demo_summary.set('한국: 인증·잔고 조회 전용. 주문·미체결·백테스트는 미지원.' if kr else
                              '백테스트는 미국 합성 데이터 예제입니다. 실제 성과와 다릅니다.')
        self.status.set('한국 KIS 모의투자 · API 연결을 눌러주세요' if kr else '미국 Alpaca 모의투자 · 계좌 새로고침을 눌러주세요')

    def korean_read_only(self):
        if self.market.get().startswith('한국'):
            messagebox.showinfo('한국 모의투자', '이번 단계는 모의계좌 인증·잔고·보유종목 조회입니다.\n한국 주문과 전략 실행은 아직 지원하지 않습니다.')
            return True
        return False

    def kis_credentials(self):
        window = tk.Toplevel(self.root)
        window.title('한국투자증권 모의투자 API 연결')
        window.transient(self.root)
        window.grab_set()
        ttk.Label(window, text='KIS 모의투자용 정보를 입력하세요. Alpaca 키는 사용할 수 없습니다.\n키·계좌·토큰은 파일에 저장하지 않습니다.', padding=16).pack()
        fields = []
        for title in ('모의투자 App Key', '모의투자 App Secret', '모의계좌 앞 8자리', '계좌 뒤 2자리 (상품코드)'):
            ttk.Label(window, text=title).pack(anchor='w', padx=16)
            entry = ttk.Entry(window, show='●', width=48)
            entry.pack(padx=16, pady=5)
            fields.append(entry)
        def apply():
            try:
                candidate = KISPaper(*(entry.get().strip() for entry in fields))
            except ValueError as exc:
                messagebox.showerror('입력 확인', str(exc), parent=window)
                return
            self.kis = candidate
            window.destroy()
            self.refresh()
        ttk.Button(window, text='연결 확인', command=apply, style='Primary.TButton').pack(pady=16)

    def refresh(self):
        if self.market.get().startswith('한국'):
            if self.kis is None:
                messagebox.showinfo('한국 모의투자 연결', 'API 연결에서 KIS 모의투자 키와 계좌를 입력하세요.')
                return
            self.work('account', self.kis.snapshot)
        else:
            self.work('account', lambda: reconcile_snapshot({**self.config,'_reconcile_cancel':self.read_cancel},AlpacaPaper(),account_view))

    def scan(self):
        if self.korean_read_only():
            return
        self.work('scan', lambda: cycle(dict(self.config), False))

    def start(self):
        if self.korean_read_only():
            return
        if self.running or self.busy:
            return
        if not messagebox.askyesno('모의매매 시작', f"Alpaca 모의계좌에 주문을 제출하고 5분 기준으로 반복합니다. 지연된 예약은 건너뜁니다.\n진입 필터: {LABELS[self.config.get('entry_strategy','baseline')]} · 실제 수익 우위 미검증\n기존 PowerShell 반복 실행을 먼저 종료하세요.\n모의매매를 시작할까요?"):
            return
        self.resume_pending=True
        self.work('resume',lambda:resume_snapshot({**self.config,'_reconcile_cancel':self.read_cancel},AlpacaPaper(),account_view))

    def finish_resume(self,data):
        if not self.resume_pending:return
        self.resume_pending=False
        stop=Path(self.config['state_dir'])/'STOP'
        if stop.exists():
            if not messagebox.askyesno('비상 중단 해제','계좌·미체결·미확인 주문 점검을 통과했습니다.\n기존 주문 취소나 청산을 의미하지 않습니다. STOP을 해제하고 모의매매를 재개할까요?'):return
        if time.monotonic()-data.get('received_monotonic',time.monotonic())>60:
            self.order_notice.set('재개 차단 · 오래된 계좌 조회 · 다시 점검하세요.');return
        if not self.sleep_guard.acquire():
            self.status.set('절전 방지 요청 실패 · 자동매매 시작 차단')
            self.write('Windows 절전 방지 요청에 실패했습니다. 전원 상태를 확인한 뒤 다시 시작하세요.');return
        if time.monotonic()-data.get('received_monotonic',time.monotonic())>60:
            self.sleep_guard.release()
            self.order_notice.set('재개 차단 · 오래된 계좌 조회 · 다시 점검하세요.');return
        if stop.exists():
            try:stop.unlink()
            except OSError:
                self.sleep_guard.release()
                self.status.set('STOP 해제 실패 · 재개 차단');return
        self.last_account_time=data.get('received_monotonic',time.monotonic());self.last_account_label=data['received_at'];self.account_error=False
        self.stop_event.clear();self.stop_failed=False
        self.cadence=Cadence(300,time.monotonic())
        self.running=True;self.selector.configure(state='disabled')
        self.write('재개 전 읽기 점검 통과. 모의매매 시작 · 실계좌 주문 비활성화.')
        self.trade()

    def checked_trade(self):
        b=AlpacaPaper()
        c={**self.config,'_stop_event':self.stop_event,'_reconcile_cancel':self.read_cancel}
        snapshot=reconcile_snapshot(c,b,account_view)
        if snapshot['reconciliation']['unresolved'] or not snapshot['inventory']['ready']:
            return {'status':'reconciliation_required','orders':[],'account_snapshot':snapshot}
        result=cycle(c,True,b);result['account_snapshot']=snapshot
        return result

    def schedule_trade(self):
        if self.timer is not None:self.root.after_cancel(self.timer)
        delay=max(1,math.ceil(self.cadence.delay(time.monotonic())*1000))
        self.timer=self.root.after(delay,self.trade)

    def trade(self):
        self.timer = None
        if not self.running:return
        if self.busy:
            self.timer=self.root.after(1000,self.trade);return
        if not self.cadence.claim(time.monotonic()):
            self.schedule_trade();return
        self.work('trade',self.checked_trade)

    def pause(self):
        self.running = False
        guard=getattr(self,'sleep_guard',None)
        if guard and not self.busy:guard.release()
        self.selector.configure(state='disabled' if self.busy else 'readonly')
        if self.timer is not None:
            self.root.after_cancel(self.timer)
            self.timer = None

    def stop(self):
        self.pause()
        self.resume_pending=False
        if hasattr(self,'stop_event'):self.stop_event.set()
        if hasattr(self,'read_cancel'):self.read_cancel.set()
        root = Path(self.config['state_dir'])
        try:
            root.mkdir(parents=True, exist_ok=True);(root/'STOP').touch()
            if not (root/'STOP').exists():raise OSError('STOP not found')
            self.stop_failed=False
            self.status.set('비상 중단 · 신규 주문 차단 확인 · 기존 주문 취소·보유종목 청산은 수행하지 않음')
            self.write('STOP 파일 확인. 이미 통신 중인 주문의 결과와 기존 주문은 증권사에서 확인하세요.')
        except OSError:
            self.stop_failed=True
            self.status.set('중단 기록 실패 · 이 창의 실행은 차단됨 · 다른 프로세스와 증권사 주문을 확인하세요.')
            self.write('STOP 기록 실패. 이 창은 중단했지만 다른 실행 프로세스의 차단은 확인하지 못했습니다.')

    def research(self):
        if self.busy:return
        if self.running:
            messagebox.showinfo('전략 연구','비상 중단 후 연구를 진행하세요. 연구 결과는 자동 적용하지 않습니다.',parent=self.root);return
        selected=filedialog.askopenfilename(parent=self.root,title='전략 연구 일봉 CSV 선택 (300~5000개)',initialdir=self.path.parent/'examples',filetypes=[('일봉 CSV','*.csv')])
        if not selected:return
        from .research import compare
        c=dict(self.config)
        self.work('research',lambda:compare(read_csv(Path(selected)),c))

    def show_research(self,data):
        window=tk.Toplevel(self.root);window.title('전략 비교 · 연구용');window.geometry('900x460+24+40');window.transient(self.root)
        ttk.Label(window,text='실제 시장 수익 개선 미검증 · 입력 CSV 출처/기업행위 미검증 · 자동 적용 없음',wraplength=860,padding=10).pack(anchor='w')
        names={'baseline':'기존 전략','trend_guard':'추세·급락 제한','trend_volume_2':'추세 + 거래량 2배','trend_volume_4':'추세 + 거래량 4배','trend_volatility_guard':'추세 + 변동성 제한'}
        selected=names.get(data['selected_on_training'],'없음 (학습 거래 표본 부족)')
        evidence={'insufficient_training_trades':'학습 거래 표본 부족','insufficient_holdout_trades':'검증·최종 거래 표본 부족','research_only_unverified_market_data':'연구용 · 실제 시장 개선 미검증'}[data['evidence_status']]
        ttk.Label(window,text=f"학습 기간만으로 선택: {selected} · {evidence}\n임의 연구 원금 10,000 (입력 가격 단위) · 비용 가정: 양쪽 수수료 0.10% + 슬리피지 0.10% · 매도세 가정 0%",wraplength=860,padding=10).pack(anchor='w')
        ttk.Label(window,text=f"일봉 {data['bars']}개 · 시간순 학습 60% / 검증 20% / 최종 20% · 공통 워밍업 60봉",padding=(10,0)).pack(anchor='w')
        table=ttk.Treeview(window,columns=list(range(6)),show='headings',height=6)
        for i,title in enumerate(('후보','학습 순수익률','검증 순수익률','최종 순수익률','최종 최대낙폭','최종 청산 거래 수')):
            table.heading(i,text=title);table.column(i,width=180 if i==0 else 135,anchor='center')
        for row in data['rows']:
            table.insert('','end',values=(names[row['name']],f"{row['train']['total_return']:.2%}",f"{row['validation']['total_return']:.2%}",f"{row['test']['total_return']:.2%}",f"{row['test']['max_drawdown']:.2%}",row['test']['closed_trades']))
        table.pack(fill='both',expand=True,padx=10)
        b=data['benchmarks']['test']
        ttk.Label(window,text=f"최종 비교: 현금 {b['cash_return']:.2%} / 같은 비중 단순 보유 {b['matched_allocation_hold']['total_return']:.2%} / 전액 단순 보유 {b['full_allocation_hold']['total_return']:.2%}\n기간별 독립 원금·무보유 시작 및 끝날 강제 청산 가정입니다. 실시간 지정가·브래킷 체결을 재현하지 않습니다.",wraplength=860,padding=10).pack(anchor='w')
        ttk.Button(window,text='닫기',command=window.destroy).pack(pady=8)

    def demo(self):
        if self.korean_read_only():
            return
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
        if self.korean_read_only():
            return
        if self.running:
            messagebox.showinfo('설정 변경', '비상 중단 후 설정을 변경하세요.')
            return
        window = tk.Toplevel(self.root)
        window.title('전략 설정')
        window.transient(self.root)
        window.grab_set()
        fields = {}
        strategy=tk.StringVar(value=LABELS[self.config.get('entry_strategy','baseline')])
        ttk.Label(window,text='미국 모의 진입 필터 · 실제 수익 우위 미검증').pack(anchor='w',padx=8)
        ttk.Combobox(window,textvariable=strategy,values=list(LABELS.values()),state='readonly',width=44).pack(padx=8,pady=4)
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
                c['entry_strategy']=next(key for key,label in LABELS.items() if label==strategy.get())
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
        guard=getattr(self,'sleep_guard',None)
        if guard:guard.release()
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
