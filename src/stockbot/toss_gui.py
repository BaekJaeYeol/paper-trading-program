"""Separate Toss real-account viewer. Never starts an order engine."""
import queue
import threading
import time
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from zoneinfo import ZoneInfo
from .toss import TossReadOnly
from .toss_preview import preview, describe, inputs, PreviewBlocked


def holding_rows(snapshot):
    """Preserve broker decimal strings; never infer ownership from a holding."""
    if snapshot.get('complete') is not True:
        raise ValueError('Incomplete snapshot')
    rows = []
    for item in snapshot['positions']:
        rows.append(tuple(str(item[k]) for k in (
            'symbol', 'name', 'marketCountry', 'quantity', 'currency',
            'averagePurchasePrice', 'lastPrice')) + ('관리 대상 아님',))
    return rows


class TossDashboard:
    def __init__(self, root, broker_factory=TossReadOnly):
        self.root = root
        self.factory = broker_factory
        self.results = queue.Queue()
        self.busy = False
        self.last_success = None
        self.closed = False
        root.title('토스증권 실계좌 · 조회 전용')
        root.geometry('980x520')
        root.minsize(700, 380)
        outer = ttk.Frame(root, padding=12)
        outer.pack(fill='both', expand=True)
        ttk.Label(outer, text='토스 실계좌 | 실제 주문·취소 차단 | 자동매매 미실행',
                  font=('Malgun Gothic', 13, 'bold')).pack(anchor='w')
        ttk.Label(outer, text='모든 보유종목은 관리 대상 아님으로 표시합니다. 기존 보유분을 자동 매도하지 않습니다.').pack(anchor='w', pady=6)
        self.status = tk.StringVar(value='아직 조회하지 않았습니다. 연결·새로고침을 누르세요.')
        ttk.Label(outer, textvariable=self.status, wraplength=900).pack(anchor='w')
        self.age = tk.StringVar(value='갱신 기록 없음')
        ttk.Label(outer, textvariable=self.age).pack(anchor='w', pady=4)
        self.button = ttk.Button(outer, text='토스 연결·새로고침', command=self.refresh)
        self.button.pack(anchor='w', pady=6)
        self.preview_button = ttk.Button(outer, text='1만 원 주문 미리보기 · 전송 없음', command=self.open_preview)
        self.preview_button.pack(anchor='w', pady=4)
        table_frame = ttk.Frame(outer)
        table_frame.pack(fill='both', expand=True)
        columns = ('종목', '이름', '시장', '보유 수량', '통화', '평균 매수가', '현재가', '관리 상태')
        self.table = ttk.Treeview(table_frame, columns=columns, show='headings')
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=110, minwidth=90, stretch=True)
        vertical = ttk.Scrollbar(table_frame, orient='vertical', command=self.table.yview)
        horizontal = ttk.Scrollbar(table_frame, orient='horizontal', command=self.table.xview)
        self.table.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set)
        self.table.grid(row=0, column=0, sticky='nsew')
        vertical.grid(row=0, column=1, sticky='ns')
        horizontal.grid(row=1, column=0, sticky='ew')
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)
        ttk.Label(outer, text='미체결 건수는 일반 주식 주문만 포함합니다. 조건주문·옵션·채권은 조회 범위 밖입니다.', wraplength=900).pack(anchor='w', pady=8)
        root.protocol('WM_DELETE_WINDOW', self.close)
        root.after(100, self.poll)

    def open_preview(self):
        if self.busy or self.closed:
            return
        dialog = tk.Toplevel(self.root)
        dialog.title('1만 원 예산 검사 · 실제 주문 없음')
        dialog.geometry('720x500')
        dialog.transient(self.root)
        dialog.grab_set()
        frame = ttk.Frame(dialog, padding=12)
        frame.pack(fill='both', expand=True)
        ttk.Label(frame, text='수동 후보 한 개 · 미국 보통주 · 정수 수량 · 실제 주문 차단').pack(anchor='w')
        values = []
        entries = []
        for label, default in [('미국 티커 (추천 종목 아님)', ''), ('지정가 USD (1달러 이상)', ''), ('수량 (정수)', '1')]:
            ttk.Label(frame, text=label).pack(anchor='w', pady=(6, 0))
            value = tk.StringVar(value=default)
            entry = ttk.Entry(frame, textvariable=value)
            entry.pack(fill='x')
            entries.append(entry)
            values.append(value)
        output = tk.Text(frame, height=11, wrap='word', state='disabled')
        def show(text):
            output.configure(state='normal')
            output.delete('1.0', 'end')
            output.insert('1.0', text)
            output.configure(state='disabled')
        pending = queue.Queue()
        active = [False]
        def calculate():
            if active[0]:
                return
            try:
                symbol, price, quantity = inputs(*(v.get() for v in values))
            except PreviewBlocked as error:
                show(str(error))
                return
            for entry in entries:
                entry.state(['disabled'])
            active[0] = True
            self.busy = True
            self.button.state(['disabled'])
            self.preview_button.state(['disabled'])
            calculate_button.state(['disabled'])
            show('계좌·일반 주문·조건주문·시세·환율·수수료 조회 중… 전송 없음')
            def worker():
                try:
                    text = describe(preview(self.factory(), symbol, str(price), str(quantity)))
                except PreviewBlocked as error:
                    text = '미리보기 차단: ' + str(error)
                except Exception:
                    text = '미리보기 실패: 인증정보·통신·API 응답을 확인하세요. 이전 결과는 폐기했습니다.'
                pending.put(text)
            threading.Thread(target=worker, daemon=True).start()
        def finish():
            # Closing hides the estimate; background reads may finish but never submit.
            dialog.grab_release()
            dialog.destroy()
        def collect():
            if self.closed:
                return
            try:
                text = pending.get_nowait()
            except queue.Empty:
                pass
            else:
                active[0] = False
                self.busy = False
                self.button.state(['!disabled'])
                self.preview_button.state(['!disabled'])
                if dialog.winfo_exists():
                    calculate_button.state(['!disabled'])
                    for entry in entries:
                        entry.state(['!disabled'])
                    show(text + '\n\n조회 시점의 단일 계산입니다. 입력을 변경하면 다시 계산하세요.')
            if active[0] or dialog.winfo_exists():
                self.root.after(100, collect)
        calculate_button = ttk.Button(frame, text='예산 계산 · 실제 주문 없음', command=calculate)
        calculate_button.pack(anchor='w', pady=8)
        output.pack(fill='both', expand=True)
        ttk.Button(frame, text='닫기', command=finish).pack(anchor='e', pady=6)
        dialog.protocol('WM_DELETE_WINDOW', finish)
        self.root.after(100, collect)

    def refresh(self):
        if self.busy or self.closed:
            return
        self.busy = True
        self.button.state(['disabled'])
        self.preview_button.state(['disabled'])
        self.status.set('토스 계좌 조회 중… 실제 주문은 실행하지 않습니다.')
        # Hide old holdings immediately so failed refresh cannot look current.
        self.table.delete(*self.table.get_children())
        def worker():
            try:
                snapshot = self.factory().account_snapshot()
                rows = holding_rows(snapshot)
                stamp = datetime.fromisoformat(snapshot['as_of'])
                if stamp.tzinfo is None:
                    raise ValueError('Timezone missing')
                self.results.put((True, (rows, len(snapshot['open_orders']), stamp)))
            except Exception:
                # Never expose arbitrary exception strings, account IDs or credentials.
                self.results.put((False, None))
        threading.Thread(target=worker, daemon=True).start()

    def poll(self):
        if self.closed:
            return
        try:
            success, result = self.results.get_nowait()
        except queue.Empty:
            pass
        else:
            self.busy = False
            self.button.state(['!disabled'])
            self.preview_button.state(['!disabled'])
            if success:
                rows, count, stamp = result
                for row in rows:
                    self.table.insert('', 'end', values=row)
                self.last_success = time.monotonic()
                kst = stamp.astimezone(ZoneInfo('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')
                self.status.set(f'조회 성공 · 보유 {len(rows)}종목 · 일반 미체결 {count}건 · {kst} KST · 조회 완료 시각 기준')
            else:
                self.last_success = None
                self.status.set('조회 실패 · 현재 잔고 확인 불가. 이 PowerShell의 토스 인증정보·허용 IP·계좌 선택·통신 상태를 확인하세요.')
        if self.last_success is None:
            self.age.set('유효한 조회 결과 없음')
        else:
            seconds = int(time.monotonic() - self.last_success)
            self.age.set(f'마지막 조회 후 {seconds}초' + (' · 60초 경과: 새로고침 필요' if seconds >= 60 else ' · 수동 조회 화면'))
        self.root.after(100, self.poll)

    def close(self):
        self.closed = True
        self.root.destroy()


def main():
    root = tk.Tk()
    TossDashboard(root)
    root.mainloop()


if __name__ == '__main__':
    main()
