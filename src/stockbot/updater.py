"""User-triggered immutable source updates from one fixed GitHub repository."""
import ast
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import time
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.parse import urlsplit

VERSION = '0.4.0'
REPOSITORY = 'BaekJaeYeol/paper-trading-program'
RAW = 'https://raw.githubusercontent.com/' + REPOSITORY
API = 'https://api.github.com/repos/' + REPOSITORY
MAX_FILE = 512 * 1024
MAX_TOTAL = 4 * 1024 * 1024


class UpdateError(RuntimeError):
    pass


def app_root():
    if sys.platform != 'win32' or not os.environ.get('LOCALAPPDATA'):
        raise UpdateError('업데이트 설치는 Windows에서만 지원합니다.')
    return Path(os.environ['LOCALAPPDATA']) / 'BaekJaeYeolStockbot'


class SafeRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parsed = urlsplit(newurl)
        if parsed.scheme != 'https' or parsed.netloc not in {'api.github.com', 'raw.githubusercontent.com'}:
            raise UpdateError('예상하지 못한 다운로드 주소입니다.')
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def download(url):
    parsed = urlsplit(url)
    if parsed.scheme != 'https' or parsed.netloc not in {'api.github.com', 'raw.githubusercontent.com'}:
        raise UpdateError('허용되지 않은 다운로드 주소입니다.')
    try:
        request = Request(url, headers={'User-Agent': 'Stockbot-Desktop-Updater', 'Accept': 'application/vnd.github+json'})
        with build_opener(SafeRedirect()).open(request, timeout=20) as response:
            data = response.read(MAX_TOTAL + 1)
        if len(data) > MAX_TOTAL:
            raise UpdateError('다운로드 크기 제한 초과')
        return data
    except UpdateError:
        raise
    except Exception:
        raise UpdateError('업데이트 서버에 연결하지 못했습니다. 기존 버전은 유지됩니다.') from None


def version(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{1,3}\.\d{1,3}\.\d{1,3}', value):
        raise UpdateError('버전 정보 형식 오류')
    return tuple(map(int, value.split('.')))


def channel(value):
    if (not isinstance(value, dict) or set(value) != {'schema', 'version', 'commit', 'python', 'mode'}
            or value['schema'] != 1 or value['python'] != '3.11+'
            or value['mode'] != 'toss-read-only'
            or not isinstance(value['commit'], str) or not re.fullmatch('[a-f0-9]{40}', value['commit'])):
        raise UpdateError('지원하지 않는 업데이트 정보입니다.')
    version(value['version'])
    return value


def check_update(fetch=download):
    try:
        candidate = channel(json.loads(fetch(RAW + '/main/desktop-channel.json')))
    except UpdateError:
        raise
    except Exception:
        raise UpdateError('업데이트 정보 확인 실패. 기존 버전을 유지합니다.') from None
    return candidate if version(candidate['version']) > version(VERSION) else None


def atomic_json(path, value):
    path = Path(path)
    fd, temporary = tempfile.mkstemp(prefix='.state-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(value, stream)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def state(root):
    path = Path(root) / 'current.json'
    if not path.exists():
        return {'active': 'bundled', 'previous': 'bundled'}
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
        if set(value) != {'active', 'previous'}:
            raise ValueError()
        for key in value.values():
            if key != 'bundled' and (not isinstance(key, str) or not re.fullmatch('[a-f0-9]{40}', key)):
                raise ValueError()
        return value
    except Exception:
        raise UpdateError('설치 버전 정보가 손상되었습니다. 기존 폴더의 실행 파일을 사용하세요.') from None


def install(candidate, *, root=None, fetch=download, monotonic=time.monotonic, cancelled=None):
    candidate = channel(candidate)
    if version(candidate['version']) <= version(VERSION):
        raise UpdateError('동일하거나 이전 버전으로 업데이트하지 않습니다.')
    root = Path(root) if root is not None else app_root()
    root.mkdir(parents=True, exist_ok=True)
    lock = acquire_lock(root)
    staging = None
    started = monotonic()
    try:
        state(root)  # Refuse a damaged pointer before preparing files.
        staging = Path(tempfile.mkdtemp(prefix='staging-', dir=root))
        package = staging / 'src' / 'stockbot'
        package.mkdir(parents=True)
        def read(url):
            if cancelled and cancelled():
                raise UpdateError('업데이트를 취소했습니다. 기존 버전은 유지됩니다.')
            if monotonic() - started > 120:
                raise UpdateError('업데이트 시간이 초과되어 취소했습니다.')
            value = fetch(url)
            if monotonic() - started > 120:
                raise UpdateError('업데이트 시간이 초과되어 취소했습니다.')
            return value
        commit = candidate['commit']
        entries = json.loads(read(API + '/contents/src/stockbot?ref=' + commit))
        if not isinstance(entries, list) or not 2 <= len(entries) <= 100:
            raise UpdateError('지원하지 않는 배포 구성입니다.')
        names, total = set(), 0
        for item in entries:
            name = item['name']
            if (item['type'] != 'file' or 'target' in item
                    or not isinstance(name, str) or not re.fullmatch(r'[a-z_][a-z0-9_]{0,63}\.py', name)
                    or name in names or item['path'] != 'src/stockbot/' + name
                    or not re.fullmatch('[a-f0-9]{40}', item['sha'])
                    or type(item['size']) is not int or not 0 <= item['size'] <= MAX_FILE):
                raise UpdateError('지원하지 않는 배포 파일입니다.')
            names.add(name)
        if sum(item['size'] for item in entries) > MAX_TOTAL:
            raise UpdateError('배포 크기 제한 초과')
        pool = ThreadPoolExecutor(max_workers=4)
        futures = {pool.submit(read, RAW + '/' + commit + '/src/stockbot/' + item['name']): item for item in entries}
        try:
            for future in as_completed(futures):
                item = futures[future]
                data = future.result()
                total += len(data)
                if len(data) != item['size'] or len(data) > MAX_FILE or total > MAX_TOTAL:
                    raise UpdateError('배포 크기가 일치하지 않습니다.')
                digest = hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()
                if digest != item['sha']:
                    raise UpdateError('다운로드 검증 실패. 기존 버전을 유지합니다.')
                ast.parse(data.decode('utf-8'), filename=item['name'])
                (package / item['name']).write_bytes(data)
        finally:
            pool.shutdown(wait=True, cancel_futures=True)
        if not {'__init__.py', 'toss_gui.py', 'toss.py', 'updater.py', 'credentials.py'}.issubset(names):
            raise UpdateError('필수 프로그램 파일이 없습니다.')
        # Channel version must match the staged application, without importing downloaded code.
        module = ast.parse((package / 'updater.py').read_text(encoding='utf-8'))
        versions = [node.value.value for node in module.body if isinstance(node, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id == 'VERSION' for t in node.targets)
                    and isinstance(node.value, ast.Constant)]
        if versions != [candidate['version']]:
            raise UpdateError('배포 버전 불일치')
        atomic_json(staging / 'ready.json', candidate)
        versions_dir = root / 'versions'
        versions_dir.mkdir(exist_ok=True)
        final = versions_dir / commit
        if final.exists():
            expected = {str(p.relative_to(staging)): p.read_bytes() for p in staging.rglob('*') if p.is_file()}
            actual = {str(p.relative_to(final)): p.read_bytes() for p in final.rglob('*') if p.is_file()}
            if final.is_symlink() or any(p.is_symlink() for p in final.rglob('*')) or actual != expected:
                raise UpdateError('기존 준비 파일 검증 실패. 현재 버전은 유지됩니다.')
        else:
            os.replace(staging, final)
            staging = None
        # Keep the version that was actually running as rollback target, not an unlaunched pending version.
        running = os.environ.get('STOCKBOT_ACTIVE_VERSION', 'bundled')
        if running != 'bundled' and not re.fullmatch('[a-f0-9]{40}', running):
            raise UpdateError('실행 버전 식별 실패')
        if cancelled and cancelled():
            raise UpdateError('업데이트를 취소했습니다. 기존 버전은 유지됩니다.')
        atomic_json(root / 'current.json', {'active': commit, 'previous': running})
        return candidate['version']
    except UpdateError:
        raise
    except Exception:
        raise UpdateError('업데이트 설치 실패. 기존 실행 버전을 유지합니다.') from None
    finally:
        if staging is not None:
            shutil.rmtree(staging, ignore_errors=True)
        lock.close()


def acquire_lock(root):
    stream = (Path(root) / 'update.lock').open('a+b')
    try:
        if stream.tell() == 0:
            stream.write(b'0')
            stream.flush()
        stream.seek(0)
        if sys.platform == 'win32':
            import msvcrt
            msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        return stream  # OS releases the lock on close or process termination.
    except OSError:
        stream.close()
        raise UpdateError('다른 업데이트가 진행 중입니다.') from None


def rollback(root=None):
    root = Path(root) if root is not None else app_root()
    root.mkdir(parents=True, exist_ok=True)
    lock = acquire_lock(root)
    try:
        value = state(root)
        if value['active'] == value['previous']:
            raise UpdateError('돌아갈 이전 버전이 없습니다.')
        atomic_json(root / 'current.json', {'active': value['previous'], 'previous': value['previous']})
    finally:
        lock.close()
