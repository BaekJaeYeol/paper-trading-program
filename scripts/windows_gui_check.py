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
    ids=(6,1) if yes else (7,2)
    chosen=[b for b in buttons if b.control_id() in ids]
    assert chosen,(title,[(b.control_id(),b.window_text()) for b in buttons])
    chosen[0].click_input()
    w.wait_not('visible',timeout=10)

def entries(title):
    s=wait(lambda s:any(w['title']==title for w in s.get('windows',[])))
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
        record('main-window')
        click('계좌 새로고침')
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
        click('계좌 새로고침');wait(lambda s:'작업 실패' in s.get('status',''))
        (OUT/'control.json').write_text('{"fail":false}')
        time.sleep(.3)
        click('계좌 새로고침');wait(lambda s:'모의계좌 연결됨' in s.get('status','') and not s.get('busy',True))
        record('network-error-recovery-offline')
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
