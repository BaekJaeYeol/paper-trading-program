import csv, datetime, hashlib, json, os, queue, shutil, threading, tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from engine import load
from data import download, symbol_name
from research import run
from paper import Paper

ROOT=Path(__file__).resolve().parent
WORK=ROOT/'workspace';WORK.mkdir(exist_ok=True)
LABELS={'trend':'추세','momentum':'모멘텀','breakout':'돌파','reversion':'평균회귀','volume_filter':'거래량 필터','cash':'현금','buy_hold':'매수 후 보유'}

class App:
    def __init__(self,root):
        self.root=root;root.title('투자랩 — 과거 검증 · 일봉 모의투자');root.geometry('1120x760');root.minsize(900,650)
        self.timer=None;self.events=queue.Queue();self.busy=False;self.running=False;self.path=None;self.source=None;self.report=None;self.paper=None;self.symbol_used=None
        self.symbol=tk.StringVar(value='SPY');self.status=tk.StringVar(value='검증 대기 — 실제 데이터 또는 CSV를 선택하세요');self.account=tk.StringVar(value='모의계좌 미시작')
        style=ttk.Style();style.theme_use('clam');style.configure('TFrame',background='#f5f7fb');style.configure('TLabel',background='#f5f7fb',font=('맑은 고딕',10));style.configure('Title.TLabel',font=('맑은 고딕',22,'bold'));style.configure('Treeview',rowheight=27)
        main=ttk.Frame(root,padding=24);main.pack(fill='both',expand=True)
        ttk.Label(main,text='투자랩',style='Title.TLabel').pack(anchor='w')
        ttk.Label(main,text='과거 전략 검증 + 완료된 일봉으로 전진 모의 운영 | 실제 계좌 주문 없음').pack(anchor='w',pady=(0,16))
        bar=ttk.Frame(main);bar.pack(fill='x')
        ttk.Label(bar,text='종목').pack(side='left');ttk.Entry(bar,textvariable=self.symbol,width=12).pack(side='left',padx=8)
        self.buttons=[]
        for text,fn in [('실제 데이터 수집 (5년)',self.collect),('CSV 가져오기',self.import_csv),('합성 데모',self.demo),('전략 비교 실행',self.compare)]:
            b=ttk.Button(bar,text=text,command=fn);b.pack(side='left',padx=4);self.buttons.append(b)
        ttk.Label(main,textvariable=self.status,wraplength=1020).pack(anchor='w',pady=12)
        tabs=ttk.Notebook(main);tabs.pack(fill='both',expand=True)
        compare=ttk.Frame(tabs,padding=12);paper=ttk.Frame(tabs,padding=12);guide=ttk.Frame(tabs,padding=12)
        tabs.add(compare,text='전략 비교');tabs.add(paper,text='모의계좌 · 거래 기록');tabs.add(guide,text='사용 안내')
        ttk.Label(compare,text='개발·검증 구간의 모든 후보와 마지막 구간의 선정 후보를 표시합니다. 비용: 수수료 0.1% + 슬리피지 0.1% (편도)').pack(anchor='w',pady=6)
        self.table=self.make_table(compare,('구간','전략','수익률','최대 낙폭','Sharpe','회전량'),(140,300,100,100,90,90))
        control=ttk.Frame(paper);control.pack(fill='x')
        for text,fn in [('선정 후보로 시작 / 재개',self.start),('지금 갱신',self.update),('운영 중단',self.stop)]:
            b=ttk.Button(control,text=text,command=fn);b.pack(side='left',padx=4)
        ttk.Label(paper,textvariable=self.account).pack(anchor='w',pady=12)
        ttk.Label(paper,text='가상 $10,000 / 소수점 수량 / 일봉 다음 시가 체결 가정. 새 일봉만 처리하며 재시작해도 중복 처리하지 않습니다.').pack(anchor='w')
        self.ledger=self.make_table(paper,('날짜','신호 비중','매매','수량','가격','수수료','평가금액'),(110,95,80,110,110,100,140))
        text=tk.Text(guide,wrap='word',font=('맑은 고딕',11),background='white');text.pack(fill='both',expand=True)
        text.insert('end','1. 종목을 입력하고 실제 데이터를 수집하거나 CSV를 가져옵니다.\n2. 전략 비교 실행을 누릅니다. 개발 50% / 검증 25% / 최종 보류 25%로 나눕니다.\n3. 검증 구간 Sharpe와 최소 회전량으로 후보를 정합니다. 최종 결과를 보고 다시 후보를 고르지 않습니다.\n4. 실제 다운로드 데이터에서는 후보를 고정해 일봉 모의 운영을 시작할 수 있습니다.\n5. 시작일 이후 새로 완료된 거래일만 가상 체결합니다. 첫날 거래가 없어도 정상입니다.\n6. 운영 중에는 5분마다 갱신합니다. PC와 앱이 켜져 있어야 합니다.\n\nCSV 열: date,open,high,low,close,volume. 최소 252행, 날짜 오름차순.\n실제 다운로드: Yahoo 데이터, 당일 봉 제외, 배당 미반영. 다운로드가 제한될 수 있습니다.\n출처 불명 CSV와 합성 데모로 실데이터 검증 통과를 표시하지 않습니다.\n각 종목은 별도 모의계좌이며 여러 계좌를 합산한 포트폴리오가 아닙니다.\n\n이 버전은 시세 기반 로컬 모의계좌입니다. 증권사 모의주문, 실시간 호가·부분 체결·공매도·실거래 기능은 없습니다.\n운영 중단은 갱신을 멈추며 보유분을 청산하지 않습니다. 중단 중 지난 일봉은 재개 때 순서대로 처리됩니다.\n과거 데이터가 수정되거나 주식 분할로 가격 기준이 바뀌면 계좌 처리를 멈춥니다.\n\n결과와 데이터는 workspace 폴더에 저장됩니다. 같은 최종 보류 구간을 반복해서 보며 전략을 수정하면 독립 검증이 아닙니다.\n실계좌 전환은 자동 승인하지 않습니다.')
        text.config(state='disabled');root.protocol('WM_DELETE_WINDOW',self.close);root.after(100,self.poll)
    def make_table(self,parent,cols,widths):
        box=ttk.Frame(parent);box.pack(fill='both',expand=True,pady=8)
        table=ttk.Treeview(box,columns=cols,show='headings');scroll=ttk.Scrollbar(box,orient='vertical',command=table.yview);table.configure(yscrollcommand=scroll.set)
        for c,w in zip(cols,widths):table.heading(c,text=c);table.column(c,width=w,minwidth=60)
        table.pack(side='left',fill='both',expand=True);scroll.pack(side='right',fill='y');return table
    def task(self,fn,done):
        if self.busy:return
        self.busy=True
        for b in self.buttons:b.config(state='disabled')
        def worker():
            try:self.events.put(('ok',fn(),done))
            except Exception as e:self.events.put(('error',str(e),None))
        threading.Thread(target=worker,daemon=True).start()
    def poll(self):
        try:
            kind,result,done=self.events.get_nowait();self.busy=False
            for b in self.buttons:b.config(state='normal')
            if kind=='error':self.stop();self.status.set('작업 중단: '+result);messagebox.showerror('작업 확인',result)
            else:done(result)
        except queue.Empty:pass
        self.root.after(100,self.poll)
    def set_data(self,path,source,symbol=None):
        self.path=Path(path);self.source=source;self.symbol_used=symbol;self.report=None
        rows=load(path);self.status.set(f'{source} | {len(rows):,}일 | {rows[0][0]} ~ {rows[-1][0]} | 전략 비교를 실행하세요')
    def collect(self):
        if self.running:messagebox.showinfo('운영 중','중단한 뒤 새 데이터를 선택하세요.');return
        try:s=symbol_name(self.symbol.get())
        except ValueError as e:messagebox.showerror('종목',str(e));return
        self.status.set('실제 과거 데이터 수집 중…')
        self.task(lambda:download(s,WORK/'data'/f'{s}.csv'),lambda p:self.set_data(p,'real_download',s))
    def import_csv(self):
        if self.running:return
        p=filedialog.askopenfilename(filetypes=[('CSV','*.csv')])
        if not p:return
        try:
            load(p);dest=WORK/'imports'/f'{hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]}.csv';dest.parent.mkdir(exist_ok=True);shutil.copyfile(p,dest);self.set_data(dest,'imported_csv')
        except Exception as e:messagebox.showerror('CSV',str(e))
    def demo(self):
        if not self.running:self.set_data(ROOT/'demo_synthetic.csv','synthetic')
    def compare(self):
        if not self.path or self.running:return
        path=self.path;source=self.source;stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
        out=WORK/'reports'/stamp
        self.task(lambda:run(path,out,source),self.show_report)
    def show_report(self,r):
        self.report=r;self.table.delete(*self.table.get_children())
        for x in r['results']:
            self.table.insert('', 'end',values=(x['fold'],x['strategy'],f"{x['return']:.2%}",f"{x['max_drawdown']:.2%}",f"{x['sharpe_rf0']:.2f}",f"{x['turnover']:.1f}"))
        self.status.set(f"{r['status']} | 선정 후보: {r['selected']} | 실거래 적합 판정은 미완료")
    def start(self):
        if self.busy or self.running:return
        if self.source!='real_download' or not self.report:messagebox.showinfo('시작 조건','실제 데이터를 다운로드하고 전략 비교를 먼저 실행하세요.');return
        try:
            self.paper=Paper(WORK/'paper'/f'{self.symbol_used}.sqlite')
            snap=self.paper.snapshot()
            if not snap['active'] and hashlib.sha256(self.path.read_bytes()).hexdigest()!=self.report['data_sha256']:raise ValueError('데이터가 바뀌었습니다. 전략 비교를 다시 실행하세요.')
            if not snap['active']:snap=self.paper.start(load(self.path),self.report['selected'],self.source)
            self.running=True;self.show_account(snap);self.status.set('일봉 모의 운영 중 — 5분 간격 갱신');self.timer=self.root.after(100,self.auto)
        except Exception as e:messagebox.showerror('모의계좌',str(e))
    def update(self):
        if self.busy or not self.running or not self.paper:return
        symbol=self.symbol_used;path=self.path;paper=self.paper
        self.task(lambda:paper.advance(load(download(symbol,path))),self.show_account)
    def auto(self):
        if not self.running:return
        self.update();self.timer=self.root.after(300000,self.auto)
    def show_account(self,s):
        self.account.set(f"고정 전략: {s['config']['strategy']} | 현금 ${s['cash']:,.2f} | 수량 {s['qty']:.4f} | 평가 ${s['equity']:,.2f} | 마지막 처리 {s['last_date']}")
        self.ledger.delete(*self.ledger.get_children())
        for day,signal,side,qty,price,cost,equity in s['ledger']:
            self.ledger.insert('','end',values=(day,f'{signal:.0%}',side,f'{qty:.4f}',f'{price:.2f}',f'{cost:.2f}',f'{equity:.2f}'))
    def stop(self):
        self.running=False
        if self.timer:
            self.root.after_cancel(self.timer);self.timer=None
        self.status.set('모의 운영 중단 — 보유분은 유지합니다')
    def close(self):self.running=False;self.root.destroy()

if __name__=='__main__':App(tk.Tk()).root.mainloop()
