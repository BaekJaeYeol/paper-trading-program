"""Stable launcher. Keep this file/folder; updates live outside it."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time


def launch(bundled=None, root=None):
    bundled = Path(bundled) if bundled else Path(__file__).resolve().parent
    sys.path.insert(0, str(bundled / 'src'))
    from stockbot.updater import app_root, state, atomic_json, UpdateError
    root = Path(root) if root else app_root()
    root.mkdir(parents=True, exist_ok=True)
    pointer = state(root)
    for attempt in range(2):
        active = pointer['active']
        source = bundled / 'src' if active == 'bundled' else root / 'versions' / active / 'src'
        try:
            if not (source / 'stockbot' / 'toss_gui.py').is_file():
                raise UpdateError('프로그램 파일을 찾지 못했습니다.')
            if active != 'bundled':
                ready = json.loads((source.parent / 'ready.json').read_text(encoding='utf-8'))
                if ready['commit'] != active or ready['mode'] != 'toss-read-only':
                    raise UpdateError('설치 검증 실패')
            fd, name = tempfile.mkstemp(prefix='startup-', dir=root)
            os.close(fd)
            signal = Path(name)
            signal.unlink()
            env = os.environ.copy()
            env['PYTHONPATH'] = str(source)
            env['STOCKBOT_ACTIVE_VERSION'] = active
            env['STOCKBOT_READY_FILE'] = str(signal)
            process = subprocess.Popen([sys.executable, '-m', 'stockbot.toss_gui'], cwd=bundled, env=env)
            deadline = time.monotonic() + 30
            while process.poll() is None and not signal.exists() and time.monotonic() < deadline:
                time.sleep(.1)
            ready = signal.exists()
            signal.unlink(missing_ok=True)
            if ready:
                # Only startup validation is automatic; later runtime errors require manual rollback.
                return process.wait()
            if process.poll() is None:
                process.terminate()
                process.wait(timeout=10)
            elif process.returncode == 0:
                return 0  # User closed the window before heartbeat.
        except Exception:
            pass
        if attempt == 0 and active != pointer['previous']:
            pointer = {'active': pointer['previous'], 'previous': pointer['previous']}
            atomic_json(root / 'current.json', pointer)
            print('New version startup failed; restored the previous version.')
        else:
            print('Startup failed. No trading was started. Please keep this folder and report this message.')
            return 1
    return 1


if __name__ == '__main__':
    raise SystemExit(launch())
