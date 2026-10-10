import csv, datetime, hashlib, json, os, queue, shutil, threading, tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from engine import load
from data import download, symbol_name, current_quote
from research import run
from validation import batch_validate, Fleet
from paper import Paper
from drive_sync import DriveSync, payload
from zoneinfo import ZoneInfo

ROOT=Path(__file__).resolve().parent
WORK=ROOT/'workspace';WORK.mkdir(exist_ok=True)
LABELS={'trend':'추세','momentum':'모멘텀','breakout':'돌파','reversion':'평균회귀','volume_filter':'거래량 필터','cash':'현금','buy_hold':'매수 후 보유'}

class App:
    def __init__(self,root):
        self.root=root;root.title('투자랩 — 과거 검증 · 일봉 모의투자');root.geometry('1120x760');root.minsize(900,650)
        self.fleet_running=False;self.fleet_generation=0;self.fleet_timer=None;self.timer=None;self.events=queue.Queue();self.busy=False;self.running=False;self.path=None;self.source=None;self.report=None;self.paper=None;self.symbol_used=None
        self.sync=DriveSync(WORK);self.sync_status=tk.StringVar(value='자동 저장 꺼짐');self.sync_enabled=tk.BooleanVar(value=self.sync.settings['enabled']);self.sync_folder=tk.StringVar(value=self.sync.settings['folder'])
        self.refresh_info=tk.StringVar(value='아직 갱신하지 않았습니다');self.trade_info=tk.StringVar(value='모의 매수·매도 기록 없음');self.last_success=None;self.refreshing=False
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
        lab=ttk.Frame(tabs,padding=12);tabs.add(lab,text='확장 검증 · 병렬 계좌')
        self.lab_symbols=tk.StringVar(value='SPY,QQQ,IWM,DIA')
        ttk.Label(lab,text='쉼표로 종목 입력 | 이전 252일로 선정 → 다음 63일 평가 반복 | 종목별 별도 실험').pack(anchor='w')
        ttk.Entry(lab,textvariable=self.lab_symbols,width=65).pack(anchor='w',pady=8)
        for title,action in [('여러 종목 실제 데이터 반복 검증',self.batch_compare),('현재 CSV 반복 검증',self.csv_walk),('현재 종목 전략별 계좌 시작 / 갱신',self.fleet_update)]:
            button=ttk.Button(lab,text=title,command=action);button.pack(anchor='w',pady=3);self.buttons.append(button)
        self.lab_info=tk.StringVar(value='검증 대기 · 병렬 계좌는 각 $10,000이며 다음 새 일봉부터 거래합니다.')
        ttk.Label(lab,textvariable=self.lab_info,wraplength=1000).pack(anchor='w',pady=8)
        self.lab_table=self.make_table(lab,('종목','전략','평가 기간','수익률 / 평가액','최대 낙폭','회전량'),(80,250,240,130,100,80))
        sync_tab=ttk.Frame(tabs,padding=16);tabs.add(sync_tab,text='Google Drive 자동 저장')
        ttk.Label(sync_tab,text='Google Drive 데스크톱 앱의 내 드라이브에 결과 폴더를 만든 뒤 선택하세요.',wraplength=900).pack(anchor='w',pady=8)
        ttk.Label(sync_tab,textvariable=self.sync_folder,wraplength=900).pack(anchor='w',pady=8)
        ttk.Button(sync_tab,text='동기화 폴더 선택',command=self.choose_sync_folder).pack(anchor='w')
        ttk.Checkbutton(sync_tab,text='검증 완료 · 모의계좌 갱신 후 자동 저장',variable=self.sync_enabled,command=self.configure_sync).pack(anchor='w',pady=12)
        ttk.Button(sync_tab,text='현재 결과 저장 / 대기 건 재시도',command=self.sync_results).pack(anchor='w')
        ttk.Label(sync_tab,textvariable=self.sync_status,wraplength=900).pack(anchor='w',pady=16)
        ttk.Label(sync_tab,text='최신 결과는 JSON, 이전 결과는 월별 ZIP으로 자동 보관합니다. 전체 거래 기록을 포함합니다. 원본 시세·인증 정보는 전송하지 않습니다.\nDrive 로그인과 동기화는 데스크톱 앱이 담당합니다. 업로드 완료 여부는 Drive에서 확인하세요.\n이 기능은 ChatGPT의 자동 분석을 시작하지 않습니다.',wraplength=900).pack(anchor='w')
        ttk.Label(compare,text='개발·검증 구간의 모든 후보와 마지막 구간의 선정 후보를 표시합니다. 비용: 수수료 0.1% + 슬리피지 0.1% (편도)').pack(anchor='w',pady=6)
        self.table=self.make_table(compare,('구간','전략','수익률','최대 낙폭','Sharpe','회전량'),(140,300,100,100,90,90))
        control=ttk.Frame(paper);control.pack(fill='x')
        for text,fn in [('선정 후보로 시작 / 재개',self.start),('지금 갱신',self.update),('운영 중단',self.stop)]:
            b=ttk.Button(control,text=text,command=fn);b.pack(side='left',padx=4)
        ttk.Label(paper,textvariable=self.account,wraplength=1000).pack(anchor='w',pady=8)
        ttk.Label(paper,textvariable=self.refresh_info,wraplength=1000).pack(anchor='w',pady=4)
        ttk.Label(paper,textvariable=self.trade_info,wraplength=1000).pack(anchor='w',pady=4)
        ttk.Label(paper,text='가상 $10,000 / 최초 시작은 조회 가격 모의체결, 이후 일봉 다음 시가 체결 가정. 새 일봉만 처리하며 재시작해도 중복 처리하지 않습니다.').pack(anchor='w')
        self.ledger=self.make_table(paper,('날짜','신호 비중','매매','수량','가격','수수료','평가금액'),(110,95,80,110,110,100,140))
        text=tk.Text(guide,wrap='word',font=('맑은 고딕',11),background='white');text.pack(fill='both',expand=True)
        text.insert('end','1. 종목을 입력하고 실제 데이터를 수집하거나 CSV를 가져옵니다.\n2. 전략 비교 실행을 누릅니다. 개발 50% / 검증 25% / 최종 보류 25%로 나눕니다.\n3. 검증 구간 Sharpe와 최소 회전량으로 후보를 정합니다. 최종 결과를 보고 다시 후보를 고르지 않습니다.\n4. 실제 다운로드 데이터에서는 후보를 고정해 일봉 모의 운영을 시작할 수 있습니다.\n5. 시작일 이후 새로 완료된 거래일만 가상 체결합니다. 첫날 거래가 없어도 정상입니다.\n6. 운영 중에는 5분마다 갱신합니다. PC와 앱이 켜져 있어야 합니다.\n\nCSV 열: date,open,high,low,close,volume. 최소 252행, 날짜 오름차순.\n실제 다운로드: Yahoo 데이터, 당일 봉 제외, 배당 미반영. 다운로드가 제한될 수 있습니다.\n출처 불명 CSV와 합성 데모로 실데이터 검증 통과를 표시하지 않습니다.\n각 종목은 별도 모의계좌이며 여러 계좌를 합산한 포트폴리오가 아닙니다.\n\n이 버전은 시세 기반 로컬 모의계좌입니다. 증권사 모의주문, 실시간 호가·부분 체결·공매도·실거래 기능은 없습니다.\n운영 중단은 갱신을 멈추며 보유분을 청산하지 않습니다. 중단 중 지난 일봉은 재개 때 순서대로 처리됩니다.\n과거 데이터가 수정되거나 주식 분할로 가격 기준이 바뀌면 계좌 처리를 멈춥니다.\n\n결과와 데이터는 workspace 폴더에 저장됩니다. 같은 최종 보류 구간을 반복해서 보며 전략을 수정하면 독립 검증이 아닙니다.\n실계좌 전환은 자동 승인하지 않습니다.')
        text.config(state='disabled');root.protocol('WM_DELETE_WINDOW',self.close);root.after(100,self.poll)
    def batch_compare(self):
        if self.busy:return
        try:
            symbols=list(dict.fromkeys(symbol_name(s) for s in self.lab_symbols.get().split(',')))
            if len(symbols)>12:raise ValueError('한 번에 최대 12종목입니다')
        except ValueError as exc:messagebox.showerror('종목',str(exc));return
        self.lab_info.set('여러 종목 데이터 수집 및 반복 검증 중…')
        def work():
            inputs={};errors={}
            for symbol in symbols:
                try:inputs[symbol]=download(symbol,WORK/'batch_data'/f'{symbol}.csv')
                except Exception as exc:errors[symbol]=str(exc)
            report=batch_validate(inputs,WORK/'batch_reports'/datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f'),'real_download',errors=errors)
            return report
        self.task(work,self.show_batch)
    def csv_walk(self):
        if self.busy or not self.path:return
        path=self.path;source=self.source;symbol=self.symbol_used or 'CSV'
        self.task(lambda:batch_validate({symbol:path},WORK/'batch_reports'/datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f'),source),self.show_batch)
    def show_batch(self,report):
        self.lab_table.delete(*self.lab_table.get_children())
        for row in report['results']:
            name=row['strategy']+(' [사전 선정]' if row['selected'] else '')
            self.lab_table.insert('','end',values=(row['symbol'],name,row['test_start']+' ~ '+row['test_end'],f"{row['return']:.2%}",f"{row['max_drawdown']:.2%}",f"{row['turnover']:.1f}"))
        self.lab_info.set(f"{report['source']} | 평가 {len(report['results'])}건 | 실패: {report['errors'] or '없음'} | 반복 탐색 결과이며 최종 독립 검증 아님")
    def fleet_update(self):
        if self.busy:return
        if self.source!='real_download' or not self.symbol_used:
            messagebox.showinfo('조건','현재 종목의 실제 데이터를 먼저 수집하세요');return
        symbol=self.symbol_used
        if self.fleet_timer:
            self.root.after_cancel(self.fleet_timer);self.fleet_timer=None
        self.fleet_symbol=symbol;self.fleet_running=True;self.fleet_generation+=1
        generation=self.fleet_generation
        def work():
            rows=load(download(symbol,WORK/'fleet_data'/f'{symbol}.csv'))
            return Fleet(WORK/'fleet').update(symbol,rows)
        self.task(work,lambda snapshots:self.show_fleet(symbol,snapshots,generation))
    def show_fleet(self,symbol,snapshots,generation):
        if not self.fleet_running or generation!=self.fleet_generation:return
        self.lab_table.delete(*self.lab_table.get_children())
        for name,snap in snapshots.items():
            self.lab_table.insert('','end',values=(symbol,name,snap['last_date'],f"${snap['equity']:,.2f}",'—','—'))
        self.lab_info.set('전략별 계좌 저장 완료 · 각각 별도 $10,000 · 다음 새 일봉부터 거래 · 실행 중 5분마다 자동 갱신')
        if not hasattr(self,'fleet_timer') or self.fleet_timer is None:
            self.fleet_timer=self.root.after(300000,self.fleet_auto)
    def fleet_auto(self):
        self.fleet_timer=None
        if not self.fleet_running:return
        generation=self.fleet_generation
        if not self.busy:
            symbol=self.fleet_symbol
            def work():
                rows=load(download(symbol,WORK/'fleet_data'/f'{symbol}.csv'))
                return Fleet(WORK/'fleet').update(symbol,rows)
            self.task(work,lambda snapshots:self.show_fleet(symbol,snapshots,generation))
        else:self.fleet_timer=self.root.after(300000,self.fleet_auto)
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
            if kind=='error':
                if self.refreshing:
                    self.refreshing=False;self.refresh_info.set('갱신 실패 '+self.now_text()+' | 최근 성공: '+(self.last_success or '없음')+' | '+result)
                self.stop();self.status.set('작업 중단: '+result);messagebox.showerror('작업 확인',result)
            else:done(result)
        except queue.Empty:pass
        self.root.after(100,self.poll)
    def set_data(self,path,source,symbol=None):
        self.path=Path(path);self.source=source;self.symbol_used=symbol;self.report=None;self.paper=None
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
        self.sync_results()
    def start(self):
        if self.busy or self.running:return
        if self.source!='real_download' or not self.report:messagebox.showinfo('시작 조건','실제 데이터를 다운로드하고 전략 비교를 먼저 실행하세요.');return
        self.paper=Paper(WORK/'paper'/f'{self.symbol_used}.sqlite')
        paper=self.paper;path=self.path;report=self.report;symbol=self.symbol_used
        self.status.set('시작 시 가격 확인 중…')
        def begin():
            rows=load(path);snap=paper.snapshot()
            if not snap['active']:
                if hashlib.sha256(path.read_bytes()).hexdigest()!=report['data_sha256']:raise ValueError('데이터가 바뀌었습니다. 전략 비교를 다시 실행하세요.')
                snap=paper.start(rows,report['selected'],self.source)
            if not snap['config'].get('instant_entry_done'):
                snap=paper.enter_now(rows,current_quote(symbol),symbol)
            return snap
        self.task(begin,self.started)
    def started(self,snap):
        self.last_success=None;self.refresh_info.set('시작 시 신호 확인 완료 · 첫 일봉 갱신 대기')
        self.running=True;self.show_account(snap)
        config=snap['config'];quote=config.get('instant_quote')
        if quote:
            session={'pre':'프리마켓','regular':'정규장','post':'애프터마켓'}[quote['session']]
            stamp=datetime.datetime.fromtimestamp(quote['timestamp'],ZoneInfo('Asia/Seoul')).strftime('%m-%d %H:%M KST')
            self.refresh_info.set(f'최초 시작 시 신호 {config["instant_signal"]:.0%} | {session} 조회 가격 ${quote["price"]:.2f} ({stamp}) | 실제 주문 없음 · 지연 가능')
        self.status.set('일봉 모의 운영 중 — 시작 시 1회 신호 적용 완료 · 이후 5분 간격 일봉 갱신')
        self.timer=self.root.after(100,self.auto)
    def update(self):
        if self.busy or not self.running or not self.paper:return
        symbol=self.symbol_used;path=self.path;paper=self.paper
        self.refreshing=True;self.refresh_info.set('데이터 확인 중… | 최근 성공: '+(self.last_success or '없음'))
        def refresh():
            before=paper.snapshot()['last_date']
            rows=load(download(symbol,path))
            snap=paper.advance(rows)
            return snap,sum(r[0]>before for r in rows)
        self.task(refresh,self.refreshed)
    def now_text(self):
        return datetime.datetime.now(ZoneInfo('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S KST')
    def refreshed(self,result):
        self.refreshing=False;s,count=result;self.last_success=self.now_text()
        detail=f'새 일봉 {count}개 처리' if count else '새 데이터 없음 · 완료된 새 일봉 대기'
        self.refresh_info.set(f'최근 갱신 성공: {self.last_success} | {detail} | 최신 처리일: {s["last_date"]}')
        self.show_account(s)
        if self.running:self.status.set('일봉 모의 운영 중 — 5분 간격 갱신')
    def auto(self):
        if not self.running:return
        self.update();self.timer=self.root.after(300000,self.auto)
    def show_account(self,s):
        self.account.set(f"종목: {self.symbol_used} | 고정 전략: {s['config']['strategy']} | 현금 ${s['cash']:,.2f} | 보유: {self.symbol_used} {s['qty']:.4f}주 | 평가 ${s['equity']:,.2f} | 마지막 처리 {s['last_date']}")
        trade=s.get('latest_trade')
        if trade:
            day,signal,side,qty,price,cost,equity=trade
            self.trade_info.set(f'최근 모의 {"매수" if side=="buy" else "매도"}: {day} | {self.symbol_used} {qty:.4f}주 | 체결 가정 ${price:.2f} | 수수료 ${cost:.2f}')
        else:self.trade_info.set(f'모의 매수·매도 기록 없음 | {self.symbol_used} 보유 {s["qty"]:.4f}주 | 시작 이후 새 일봉과 전략 신호에 따라 처리')
        self.ledger.delete(*self.ledger.get_children())
        for day,signal,side,qty,price,cost,equity in s['ledger']:
            self.ledger.insert('','end',values=(day,f'{signal:.0%}',{'buy':'모의 매수','sell':'모의 매도','hold':'유지'}[side],f'{qty:.4f}',f'{price:.2f}',f'{cost:.2f}',f'{equity:.2f}'))
        self.sync_results()
    def choose_sync_folder(self):
        if self.busy:return
        folder=filedialog.askdirectory(title='Google Drive 내 드라이브 결과 폴더 선택')
        if folder:self.sync_folder.set(folder);self.configure_sync()
    def configure_sync(self):
        if self.busy:
            self.sync_enabled.set(self.sync.settings['enabled']);return
        try:
            self.sync.configure(self.sync_folder.get(),self.sync_enabled.get());self.sync_results()
        except Exception as e:
            self.sync_enabled.set(self.sync.settings['enabled']);messagebox.showerror('Drive 설정',str(e))
    def sync_results(self):
        if self.busy:return
        if not self.sync.settings['enabled']:
            self.sync_status.set('자동 저장 꺼짐');return
        report=self.report;paper=self.paper;symbol=self.symbol_used
        self.sync_status.set('동기화 폴더 저장 중…')
        def export():
            try:
                account=paper.snapshot(full=True) if paper else None
                value=payload(report,account,symbol) if report or account else None
                return self.sync.export(value)
            except Exception:
                return '자동 저장 오류 · 모의 운영은 계속됩니다. 폴더와 디스크 공간을 확인하세요.'
        self.task(export,self.sync_status.set)
    def stop(self):
        self.fleet_running=False;self.fleet_generation+=1
        self.lab_info.set('병렬 계좌 운영 중단 · 진행 중인 갱신은 완료될 수 있으며 이후 자동 갱신은 멈춥니다')
        self.running=False
        if self.timer:
            self.root.after_cancel(self.timer);self.timer=None
        if getattr(self,'fleet_timer',None):
            self.root.after_cancel(self.fleet_timer);self.fleet_timer=None
        self.status.set('모의 운영 중단 — 보유분은 유지합니다')
    def close(self):self.running=False;self.root.destroy()

if __name__=='__main__':App(tk.Tk()).root.mainloop()
