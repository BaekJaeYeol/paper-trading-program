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
    s=wait(lambda s: bool(s.get('windows')))
    windows=[w for w in s['windows'] if title is None or w['title']==title]
    matches=[r for w in windows for r in w['widgets'] if r['class']=='TButton' and r.get('text')==text]
    assert len(matches)==1,(text,matches)
    p=matches[0]
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
        click('데모 / 백테스트')
        dialog=modal('백테스트 CSV 선택 (취소하면 기본 합성 데이터)')
        dialog.type_keys('{ESC}')
        s=wait(lambda s:'백테스트 완료' in s.get('status',''))
        assert len(s['tables']['demo'])==1
        record('cancel-file-default-demo')
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
        click('모의매매 시작');notice('모의매매 시작')
        s=wait(lambda s:s.get('running') and s.get('submitted')==1 and not s.get('busy',True))
        assert s['tables']['plans'][0][-1]=='제출됨'
        record('start-offline-order')
        click('비상 중단')
        wait(lambda s:s.get('stop') and not s.get('running',True))
        record('emergency-stop')
        click('모의매매 시작');notice('모의매매 시작');notice('비상 중단 해제')
        s=wait(lambda s:s.get('running') and not s.get('busy',True) and not s.get('stop',True))
        assert s['submitted']==1
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
        main.set_focus()
        for _ in range(6):
            if state().get('visible_tables',{}).get('history'):break
            keyboard.send_keys('^{TAB}')
            time.sleep(.2)
        wait(lambda s:s.get('visible_tables',{}).get('history'))
        record('history-tab-keyboard-navigation')
        keyboard.send_keys('^{TAB}')
        wait(lambda s:s.get('visible_tables',{}).get('timeline'))
        record('timeline-tab-keyboard-navigation')
        main.close();process.wait(timeout=20)
        assert process.returncode==0
        checks.append({'name':'window-close','passed':True})
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
