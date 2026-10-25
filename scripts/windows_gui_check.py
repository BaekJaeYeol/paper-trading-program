"""External mouse/keyboard interaction with the rendered Windows GUI."""
import json
import subprocess
import sys
import time
import traceback
from pathlib import Path
from PIL import ImageGrab
from pywinauto import Desktop, mouse, keyboard

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'gui-check'
OUT.mkdir(exist_ok=True)
checks = []
desktop = Desktop(backend='win32')

def state():
    try: return json.loads((OUT/'state.json').read_text(encoding='utf-8'))
    except (OSError, ValueError): return {}

def wait(predicate, timeout=30):
    end=time.monotonic()+timeout
    while time.monotonic()<end:
        s=state()
        if predicate(s): return s
        time.sleep(.15)
    raise TimeoutError(str(state()))

def capture(name): ImageGrab.grab().save(OUT/f'{name}.png')

def record(name):
    checks.append({'name':name,'passed':True})
    capture(f'{len(checks):02}-{name}')

def click(text,title=None):
    def matches(s):
        windows=[w for w in s.get('windows',[]) if title is None or w['title']==title]
        return [r for w in windows for r in w['widgets'] if r['class'] in ('TButton','TRadiobutton') and r.get('text')==text]
    s=wait(lambda s:len(matches(s))==1)
    p=matches(s)[0]
    mouse.click(coords=(p['x'],p['y']))


def modal(title):
    w=desktop.window(title=title,class_name='#32770')
    w.wait('visible',timeout=20)
    return w

def notice(title, yes=True):
    w=modal(title)
    buttons=w.descendants(class_name='Button')
    # Standard MessageBox IDs: IDYES=6, IDNO=7, IDOK=1.
    labels={'yes','ok','예','확인'} if yes else {'no','cancel','아니요','취소'}
    chosen=[b for b in buttons if b.window_text().replace('&','').strip().lower() in labels]
    if not chosen and len(buttons)==1 and yes:
        chosen=buttons
    assert chosen,(title,[(b.control_id(),b.window_text()) for b in buttons])
    chosen[0].click_input()
    w.wait_not('visible',timeout=10)

def entries(title):
    count=8 if title=='전략 설정' else 2
    s=wait(lambda s:sum(r['class']=='TEntry' for w in s.get('windows',[]) if w['title']==title for r in w['widgets'])==count)
    return [r for w in s['windows'] if w['title']==title for r in w['widgets'] if r['class']=='TEntry']

def type_entry(entry,text):
    mouse.click(coords=(entry['x'],entry['y']))
    keyboard.send_keys('^a')
    keyboard.send_keys(text,with_spaces=True)

def run():
    process=subprocess.Popen([sys.executable,str(ROOT/'scripts/gui_probe.py')],cwd=ROOT)
    try:
        s=wait(lambda s:len(s.get('windows',[]))==1)
        main=desktop.window(title='모의매매 프로그램 · Paper Trading').wrapper_object()
        main.set_focus()
        assert main.is_visible()
        bounds=main.rectangle()
        assert bounds.right <= s['screen'][0] and bounds.bottom <= s['screen'][1] - 40, str(bounds)
        assert any(w['class']=='Text' for w in s['windows'][0]['widgets'])
        record('main-window')
        click('계좌·주문 대조')
        s=wait(lambda s:s.get('cards',{}).get('equity')=='$10,000.00' and not s.get('busy',True))
        assert s['cards']['cash']=='$8,000.00'
        record('account-refresh-offline')
        click('후보 조회')
        s=wait(lambda s:len(s.get('tables',{}).get('plans',[]))==1 and not s.get('busy',True))
        assert s['tables']['plans'][0][-1]=='조회만' and s['submitted']==0
        record('scan-without-submission')
        assert '진입: 추세·급락 제한' in s['context']
        (OUT/'control.json').write_text('{"flat_strategy":true}')
        time.sleep(.3);click('후보 조회')
        s=wait(lambda s:not s.get('busy',True) and not s.get('tables',{}).get('plans') and '기본 신호 통과 후 제외 1종목' in s.get('log_text',''))
        assert s['submitted']==0
        record('applied-trend-filter-rejects-flat-volume-spike')
        click('설정');entries('전략 설정')
        click('기존 거래량 신호','전략 설정')
        wait(lambda s:any(r.get('text')=='기존 거래량 신호' and r.get('selected') for w in s.get('windows',[]) if w['title']=='전략 설정' for r in w['widgets']))
        click('설정 저장','전략 설정');wait(lambda s:len(s.get('windows',[]))==1)
        assert json.loads((OUT/'config.json').read_text())['entry_strategy']=='baseline'
        click('후보 조회');s=wait(lambda s:not s.get('busy',True) and len(s.get('tables',{}).get('plans',[]))==1)
        assert s['submitted']==0
        click('설정');entries('전략 설정')
        click('추세·급락 제한','전략 설정')
        wait(lambda s:any(r.get('text')=='추세·급락 제한' and r.get('selected') for w in s.get('windows',[]) if w['title']=='전략 설정' for r in w['widgets']))
        click('설정 저장','전략 설정');wait(lambda s:len(s.get('windows',[]))==1)
        assert json.loads((OUT/'config.json').read_text())['entry_strategy']=='trend_guard'
        (OUT/'control.json').write_text('{}');time.sleep(.3)
        record('entry-strategy-selection-and-safe-return-to-trend')
        click('데모 / 백테스트')
        dialog=modal('백테스트 CSV 선택 (취소하면 기본 합성 데이터)')
        dialog.type_keys('{ESC}')
        s=wait(lambda s:'백테스트 완료' in s.get('status',''))
        assert len(s['tables']['demo'])==0 # 65-bar legacy synthetic signal lacks the applied trend warmup.
        record('cancel-file-default-demo')
        s=state();target=next(t for t in s['notebook_tabs'] if t['text']=='백테스트')
        mouse.click(coords=(target['x'],target['y']))
        wait(lambda s:s.get('visible_tables',{}).get('demo'))
        click('전략 비교 (연구용)')
        modal('전략 연구 일봉 CSV 선택 (300~5000개)').type_keys('{ESC}')
        s=wait(lambda s:not s.get('busy',True) and len(s.get('windows',[]))==1)
        assert s['submitted']==0
        record('research-file-cancel-no-orders')
        before_reads=s['read_calls'];before_config=(OUT/'config.json').read_text()
        click('전략 비교 (연구용)')
        dialog=modal('전략 연구 일봉 CSV 선택 (300~5000개)')
        keyboard.send_keys('%n');keyboard.send_keys('^a')
        keyboard.send_keys(str(OUT/'examples'/'synthetic-strategy-research.csv'),with_spaces=True)
        keyboard.send_keys('{ENTER}')
        s=wait(lambda s:not s.get('busy',True) and any(w['title']=='전략 비교 · 연구용' for w in s.get('windows',[])))
        report_window=next(w for w in s['windows'] if w['title']=='전략 비교 · 연구용')
        rows=next(w['rows'] for w in report_window['widgets'] if w['class']=='Treeview')
        assert len(rows)==5 and rows[0][0]=='기존 전략'
        assert any('자동 적용 없음' in w.get('text','') for w in report_window['widgets'])
        assert s['submitted']==0 and s['read_calls']==before_reads and not s['power_active']
        assert (OUT/'config.json').read_text()==before_config
        record('offline-strategy-comparison-no-broker-or-auto-apply')
        click('닫기','전략 비교 · 연구용');wait(lambda s:len(s.get('windows',[]))==1)
        before_reads=state()['read_calls']
        click('Alpaca 일봉 비교');click('취소','Alpaca 일봉 연구')
        s=wait(lambda s:len(s.get('windows',[]))==1)
        assert s['read_calls']==before_reads and s['submitted']==0
        record('historical-api-research-cancel-no-network')
        click('Alpaca 일봉 비교');click('조회·비교','Alpaca 일봉 연구')
        s=wait(lambda s:not s.get('busy',True) and any(w['title']=='전략 비교 · 연구용' for w in s.get('windows',[])))
        report_window=next(w for w in s['windows'] if w['title']=='전략 비교 · 연구용')
        assert len(next(w['rows'] for w in report_window['widgets'] if w['class']=='Treeview'))==5
        assert any('합성 API 테스트 자료' in w.get('text','') and 'Alpaca AAPL' in w.get('text','') for w in report_window['widgets'])
        assert s['read_calls']==before_reads+4 and s['submitted']==0 and not s['power_active']
        assert (OUT/'config.json').read_text()==before_config
        record('historical-api-fixture-provenance-no-orders-or-settings-change')
        click('닫기','전략 비교 · 연구용');wait(lambda s:len(s.get('windows',[]))==1)
        click('설정')
        es=entries('전략 설정')
        assert len(es)==8
        type_entry(es[1],'4')
        click('설정 저장','전략 설정')
        wait(lambda s:len(s.get('windows',[]))==1)
        assert json.loads((OUT/'config.json').read_text())['volume_ratio']==4
        record('settings-save')
        click('설정'); es=entries('전략 설정');type_entry(es[1],'invalid')
        click('설정 저장','전략 설정');notice('설정 오류')
        assert json.loads((OUT/'config.json').read_text())['volume_ratio']==4
        type_entry(es[1],'3');click('설정 저장','전략 설정')
        wait(lambda s:len(s.get('windows',[]))==1)
        record('invalid-settings-recovery')
        click('API 연결');es=entries('Alpaca 모의 API 연결')
        assert len(es)==2 and all(e['masked'] for e in es)
        click('연결 확인','Alpaca 모의 API 연결');notice('입력 확인')
        # Empty-input validation only; no real credentials are supplied.
        desktop.window(title='Alpaca 모의 API 연결').close()
        wait(lambda s:len(s.get('windows',[]))==1)
        record('masked-credentials-empty-validation')
        click('모의매매 시작');notice('모의매매 시작',False)
        s=wait(lambda s:not s.get('running',True))
        assert s['submitted']==0
        record('start-cancel-no-orders')
        (OUT/'control.json').write_text('{"power_fail":true}')
        time.sleep(.3)
        click('모의매매 시작');notice('모의매매 시작')
        s=wait(lambda s:s.get('power_error')=='acquire' and not s.get('busy',True))
        assert s['submitted']==0 and not s['running'] and not s['power_active']
        record('sleep-request-failure-blocks-automatic-start')
        (OUT/'control.json').write_text('{}')
        time.sleep(.3)
        click('모의매매 시작');notice('모의매매 시작')
        s=wait(lambda s:s.get('running') and s.get('submitted')==1 and not s.get('busy',True))
        assert s['tables']['plans'][0][-1]=='제출됨'
        record('start-offline-order')
        s=wait(lambda s:s.get('running') and not s.get('busy',True) and '다음 실행' in s.get('schedule_status',''))
        assert 'KST' in s['schedule_status'] and s['schedule_delay_seconds']>=30
        record('next-run-time-and-countdown-visible')
        assert s['power_supported'] and s['power_active'] and '절전 방지 요청 적용' in s['schedule_status']
        record('windows-sleep-request-active-during-run')
        (OUT/'control.json').write_text('{"session_mode":"post","session_tick":1}')
        s=wait(lambda s:s.get('running') and not s.get('busy',True) and s.get('operating_interval')==60 and '애프터마켓' in s.get('session_status',''))
        assert s['submitted']==1 and s['power_active']
        record('after-hours-session-monitor-blocks-new-orders')
        (OUT/'control.json').write_text('{"session_mode":"regular","session_tick":2}')
        s=wait(lambda s:s.get('running') and not s.get('busy',True) and s.get('operating_interval')==300 and s.get('session_status','').startswith('정규장'))
        assert s['submitted']==1 and s['power_active']
        record('return-to-regular-rechecks-without-duplicate')
        (OUT/'control.json').write_text('{}')
        (OUT/'control.json').write_text('{"late_schedule":true}')
        s=wait(lambda s:s.get('schedule_skipped',0)>=10 and not s.get('busy',True) and '다음 실행' in s.get('schedule_status',''))
        assert s['submitted']==1 and s['schedule_delay_seconds']>=30
        record('late-callback-skips-slots-no-order-replay')
        (OUT/'control.json').write_text('{"budget_timeout":true,"run_for_budget_test":true}')
        s=wait(lambda s:not s.get('running',True) and not s.get('busy',True) and '전체 대조 60초' in s.get('order_notice',''))
        assert s['submitted']==1 and not s['power_active']
        record('full-reconciliation-timeout-stops-without-order-or-sleep-request')
        (OUT/'control.json').write_text('{}')
        time.sleep(.3)
        click('모의매매 시작');notice('모의매매 시작')
        s=wait(lambda s:s.get('running') and not s.get('busy',True))
        assert s['submitted']==1 and s['power_active']
        record('explicit-restart-rechecks-after-full-timeout')
        (OUT/'control.json').write_text('{}')
        click('비상 중단')
        wait(lambda s:s.get('stop') and not s.get('running',True))
        record('emergency-stop')
        s=wait(lambda s:not s.get('power_active',True) and not s.get('busy',True))
        record('emergency-stop-releases-windows-sleep-request')
        click('모의매매 시작');notice('모의매매 시작');notice('비상 중단 해제')
        s=wait(lambda s:s.get('running') and not s.get('busy',True) and not s.get('stop',True))
        assert s['submitted']==1
        assert s['power_active']
        record('resume-no-duplicate')
        click('비상 중단');wait(lambda s:s.get('stop') and not s.get('running',True))
        (OUT/'control.json').write_text('{"fail":true}')
        time.sleep(.3)
        click('계좌·주문 대조');wait(lambda s:s.get('account_error') and not s.get('busy',True))
        (OUT/'control.json').write_text('{"fail":false}')
        time.sleep(.3)
        click('계좌·주문 대조');wait(lambda s:not s.get('account_error',True) and not s.get('busy',True))
        record('network-error-recovery-offline')
        (OUT/'control.json').write_text('{"partial":true}')
        time.sleep(.3)
        click('계좌·주문 대조')
        s=wait(lambda s:not s.get('busy',True) and any(r[0]=='AAPL' and r[4]=='7' and r[-1]=='부분 체결' for r in s.get('tables',{}).get('orders',[])))
        assert s['tables']['orders'][0][4]=='7'
        assert s['tables']['orders'][0][-1]=='부분 체결'
        assert '비상 중단' in s['status']
        record('partial-fill-and-stop-persistence')
        (OUT/'control.json').write_text('{"delay":1}')
        time.sleep(.3)
        click('계좌·주문 대조');wait(lambda s:s.get('busy'))
        click('비상 중단')
        s=wait(lambda s:not s.get('busy',True))
        assert '비상 중단' in s['status'] and not s['running']
        assert '실계좌 주문 비활성화' in s['context']
        record('late-response-cannot-clear-stop')
        (OUT/'control.json').write_text('{"inject_unknown":true,"missing":true}')
        time.sleep(.4)
        click('계좌·주문 대조')
        s=wait(lambda s:not s.get('busy',True) and '미확인 1건' in s.get('order_notice',''))
        assert s['stop'] and not s['running'] and s['submitted']==1
        assert any(r[0]=='MSFT' and '조회 결과 없음' in r[4] for r in s['tables']['history'])
        record('unknown-missing-keeps-stop-no-replay')
        (OUT/'control.json').write_text('{"missing":false}')
        time.sleep(.3)
        click('계좌·주문 대조')
        s=wait(lambda s:not s.get('busy',True) and '미확인 0건' in s.get('order_notice',''))
        assert s['stop'] and not s['running'] and s['submitted']==1
        assert any(r[0]=='MSFT' and r[2]=='1' and r[3]=='1' and r[4]=='부분 체결' for r in s['tables']['history'])
        assert len(s['tables']['timeline'])>=3
        record('unknown-found-partial-read-only-recovery')
        tabs=wait(lambda s:any(t['text']=='봇 주문 추적' for t in s.get('notebook_tabs',[])))['notebook_tabs']
        target=next(t for t in tabs if t['text']=='봇 주문 추적')
        mouse.click(coords=(target['x'],target['y']))
        s=wait(lambda s:s.get('visible_tables',{}).get('history'))
        assert s['table_heights']['history']>=100,s['table_heights']
        record('history-tab-mouse-navigation')
        keyboard.send_keys('^{TAB}')
        s=wait(lambda s:s.get('visible_tables',{}).get('inventory'))
        assert any(r[0]=='MSFT' and r[3]=='일치' for r in s['tables']['inventory'])
        record('managed-inventory-matches')
        (OUT/'control.json').write_text('{"holding_extra":1}')
        time.sleep(.3)
        click('계좌·주문 대조')
        s=wait(lambda s:not s.get('busy',True) and any(r[0]=='MSFT' and '불일치' in r[3] for r in s.get('tables',{}).get('inventory',[])))
        assert s['stop'] and s['submitted']==1
        record('managed-inventory-mismatch-no-liquidation')
        click('모의매매 시작');notice('모의매매 시작')
        s=wait(lambda s:s.get('account_error') and not s.get('busy',True))
        assert s['stop'] and not s['running'] and s['submitted']==1
        record('inventory-mismatch-blocks-resume')
        tabs=state()['notebook_tabs'];target=next(t for t in tabs if t['text']=='보유 수량 대조')
        mouse.click(coords=(target['x'],target['y']))
        keyboard.send_keys('^{TAB}')
        wait(lambda s:s.get('visible_tables',{}).get('timeline'))
        record('timeline-tab-keyboard-navigation')
        (OUT/'control.json').write_text('{"root_replaced":true}')
        time.sleep(.3)
        click('계좌·주문 대조')
        s=wait(lambda s:not s.get('busy',True) and any(c['code']=='order_replaced' and c['active'] for c in s.get('review_cases',[])))
        assert s['stop'] and s['submitted']==1
        record('replacement-review-blocks-no-replay')
        target=next(t for t in s['notebook_tabs'] if t['text']=='차단 상세')
        mouse.click(coords=(target['x'],target['y']))
        s=wait(lambda s:s.get('visible_tables',{}).get('review'))
        widget=next(r for w in s['windows'] for r in w['widgets'] if r['class']=='Treeview')
        mouse.click(coords=(widget['x'],widget['y']))
        keyboard.send_keys('{HOME}{ENTER}')
        notice('차단 상세 · 읽기 전용')
        s=state();assert s['stop'] and s['submitted']==1
        record('review-detail-keyboard-read-only')
        (OUT/'control.json').write_text('{}')
        time.sleep(.3)
        click('계좌·주문 대조')
        s=wait(lambda s:not s.get('busy',True) and '미확인 0건' in s.get('order_notice',''))
        assert any(c['code']=='order_replaced' and c['active'] for c in s['review_cases'])
        assert '수동 검토' in s['order_notice'] or '수동검토' in s['order_notice']
        click('모의매매 시작');notice('모의매매 시작')
        s=wait(lambda s:s.get('account_error') and not s.get('busy',True))
        assert s['stop'] and not s['running'] and s['submitted']==1
        record('sticky-review-survives-normal-read-and-blocks-resume')
        click('진단 요약 저장')
        dialog=modal('진단 요약 저장')
        report_path=OUT/'diagnostics-export.json'
        keyboard.send_keys('%n')
        keyboard.send_keys('^a')
        keyboard.send_keys(str(report_path),with_spaces=True)
        keyboard.send_keys('{ENTER}')
        notice('진단 요약')
        report=json.loads(report_path.read_text(encoding='utf-8'))
        assert report['stop_requested'] and not report['live_orders_enabled']
        assert report['read_failed_since_snapshot'] and report['stale']
        assert any(r['code']=='order_replaced' for r in report['review']['reasons'])
        assert 'gui-response-lost-MSFT' not in report_path.read_text(encoding='utf-8')
        s=state();assert s['stop'] and s['submitted']==1 and not s['running']
        record('diagnostic-save-dialog-redacted-read-only-report')
        (OUT/'control.json').write_text('{"price_changed":true}')
        time.sleep(.3)
        click('계좌·주문 대조')
        s=wait(lambda s:not s.get('busy',True) and any(c['code']=='price_changed' and c['active'] for c in s.get('review_cases',[])))
        (OUT/'control.json').write_text('{"closed_flat":true}')
        time.sleep(.3)
        click('계좌·주문 대조')
        s=wait(lambda s:not s.get('busy',True) and '미확인 0건' in s.get('order_notice',''))
        widget=next(r for w in s['windows'] for r in w['widgets'] if r['class']=='Treeview')
        mouse.click(coords=(widget['x'],widget['y']));keyboard.send_keys('{HOME}')
        click('선택 기록 복구 점검');notice('선택 기록 복구 점검',yes=False)
        assert any(c['code']=='price_changed' and c['active'] for c in state()['review_cases'])
        record('recovery-confirmation-cancel-keeps-block')
        click('선택 기록 복구 점검');notice('선택 기록 복구 점검')
        s=wait(lambda s:not s.get('busy',True) and any(c['code']=='price_changed' and not c['active'] for c in s.get('review_cases',[])))
        assert s['stop'] and not s['running'] and s['submitted']==1
        assert any(c['code']=='order_replaced' and c['active'] for c in s['review_cases'])
        record('verified-closed-flat-recovery-keeps-stop-and-other-block')
        s=state();target=next(t for t in s['notebook_tabs'] if t['text']=='운영 상태')
        mouse.click(coords=(target['x'],target['y']))
        s=wait(lambda s:s.get('visible_tables',{}).get('health'))
        assert any('전체 대조 시간 초과' in row[1] for row in s['tables']['health'])
        click('세션 상세');notice('세션 상세 · 읽기 전용')
        s=state();assert s['stop'] and not s['running'] and s['submitted']==1
        record('session-details-read-only')
        widget=next(r for w in s['windows'] for r in w['widgets'] if r['class']=='Treeview')
        mouse.click(coords=(widget['x'],widget['y']));keyboard.send_keys('{HOME}{ENTER}')
        notice('운영 상태 · 읽기 전용')
        s=state();assert s['stop'] and not s['running'] and s['submitted']==1
        record('operational-history-detail-read-only')
        main.close();process.wait(timeout=20)
        assert process.returncode==0
        checks.append({'name':'window-close','passed':True})
        (OUT/'control.json').unlink(missing_ok=True)
        (OUT/'state.json').unlink(missing_ok=True)
        process=subprocess.Popen([sys.executable,str(ROOT/'scripts/gui_probe.py')],cwd=ROOT)
        s=wait(lambda s:s.get('submitted')==0 and bool(s.get('tables',{}).get('health')) and len(s.get('windows',[]))==1)
        assert not s['running'] and not s['power_active'] and s['read_calls']==0 and s['stop']
        assert any('전체 대조 시간 초과' in row[1] for row in s['tables']['health'])
        assert any('대조 복구' in row[1] for row in s['tables']['health'])
        main=desktop.window(title='모의매매 프로그램 · Paper Trading').wrapper_object();main.set_focus()
        target=next(t for t in s['notebook_tabs'] if t['text']=='운영 상태')
        mouse.click(coords=(target['x'],target['y']))
        wait(lambda s:s.get('visible_tables',{}).get('health'))
        record('restart-restores-incident-history-without-broker-or-auto-start')
        main.close();process.wait(timeout=20);assert process.returncode==0
    finally:
        if process.poll() is None: process.terminate();process.wait(timeout=10)

if __name__=='__main__':
    try: run()
    except Exception:
        capture('failure')
        (OUT/'failure.txt').write_text(traceback.format_exc(),encoding='utf-8')
        raise
    finally:
        (OUT/'results.json').write_text(json.dumps({'platform':sys.platform,'checks':checks,'real_api_tested':False},ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Windows GUI checks passed: {len(checks)}',flush=True)
