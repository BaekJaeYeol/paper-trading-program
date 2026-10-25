import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import uuid
from stockbot import credentials, updater


class CredentialTests(unittest.TestCase):
    def test_bundle_precedence_and_no_mixing(self):
        saved = {'client_id': 'saved-id', 'client_secret': 'saved-secret', 'account_seq': '3'}
        with patch.object(credentials.WindowsVault, 'load', return_value=saved):
            self.assertEqual(credentials.resolve_credentials(), saved)
        with patch.object(credentials.WindowsVault, 'load', return_value=None), patch.dict(os.environ, {}, clear=True):
            os.environ['TOSS_CLIENT_ID'] = 'id-only'
            with self.assertRaises(credentials.CredentialError):
                credentials.resolve_credentials()

    def test_invalid_never_saved(self):
        cases = [{}, {'client_id': '', 'client_secret': 'secret', 'account_seq': ''},
                 {'client_id': 'id', 'client_secret': 's', 'account_seq': '../'},
                 {'client_id': 'id', 'client_secret': 'x' * 3000, 'account_seq': ''}]
        for value in cases:
            vault = credentials.WindowsVault()
            with self.subTest(value=bool(value)), patch.object(vault, 'api') as api:
                with self.assertRaises(credentials.CredentialError):
                    vault.save(value)
                api.assert_not_called()

    @unittest.skipUnless(sys.platform == 'win32', 'Windows credential store required')
    def test_native_vault_restart_replace_delete(self):
        target = 'Stockbot.Tests.' + uuid.uuid4().hex
        vault = credentials.WindowsVault(target)
        sample = {'client_id': 'fixture-id', 'client_secret': 'fixture-secret-한글', 'account_seq': '123'}
        try:
            self.assertIsNone(vault.load())
            vault.save(sample)
            self.assertEqual(vault.load(), sample)
            # A fresh Python process can read it; no secret is printed.
            code = ('from stockbot.credentials import WindowsVault; '
                    'import sys; v=WindowsVault(sys.argv[1]).load(); '
                    'assert v["client_id"]=="fixture-id"; print("read-ok")')
            result = subprocess.run([sys.executable, '-c', code, target], capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), 'read-ok')
            sample['client_secret'] = 'replacement'
            vault.save(sample)
            self.assertEqual(vault.load()['client_secret'], 'replacement')
            vault.delete()
            self.assertIsNone(vault.load())
            vault.delete()  # Idempotent.
        finally:
            vault.delete()


class UpdateFixture:
    def __init__(self):
        self.channel = {'schema': 1, 'version': '0.4.1', 'commit': 'a' * 40, 'python': '3.11+', 'mode': 'toss-read-only'}
        self.files = {'__init__.py': b'', 'toss_gui.py': b'# fixture\n', 'toss.py': b'# fixture\n',
                      'updater.py': b'VERSION = "0.4.1"\n', 'credentials.py': b'# fixture\n'}
        self.entries = []
        for name, data in self.files.items():
            self.entries.append({'name': name, 'path': 'src/stockbot/' + name, 'type': 'file', 'size': len(data),
                                 'sha': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()})
        self.calls = []

    def fetch(self, url):
        self.calls.append(url)
        if url.endswith('/main/desktop-channel.json'):
            return json.dumps(self.channel).encode()
        if '/contents/src/stockbot?ref=' in url:
            return json.dumps(self.entries).encode()
        return self.files[url.rsplit('/', 1)[1]]


class UpdateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.fixture = UpdateFixture()
        self.env = patch.dict(os.environ, {'STOCKBOT_ACTIVE_VERSION': 'bundled'})
        self.env.start()
        self.addCleanup(self.env.stop)

    def install(self):
        return updater.install(self.fixture.channel, root=self.root, fetch=self.fixture.fetch)

    def test_checked_update_is_staged_then_switched(self):
        with patch.object(updater, 'VERSION', '0.4.0'):
            candidate = updater.check_update(self.fixture.fetch)
            self.assertEqual(candidate, self.fixture.channel)
            self.assertEqual(self.install(), '0.4.1')
        value = updater.state(self.root)
        self.assertEqual(value, {'active': 'a'*40, 'previous': 'bundled'})
        self.assertTrue((self.root/'versions'/('a'*40)/'src/stockbot/toss_gui.py').is_file())
        self.assertFalse(list(self.root.glob('staging-*')))
        updater.rollback(self.root)
        self.assertEqual(updater.state(self.root)['active'], 'bundled')

    def test_no_update_and_invalid_channel(self):
        with patch.object(updater, 'VERSION', '0.4.1'):
            self.assertIsNone(updater.check_update(self.fixture.fetch))
        for key, value in [('commit', '../evil'), ('mode', 'live'), ('python', '3.14+'), ('version', 'invalid')]:
            bad = dict(self.fixture.channel, **{key:value})
            with self.subTest(key), self.assertRaises(updater.UpdateError):
                updater.channel(bad)

    def test_corrupt_download_does_not_change_pointer_or_config(self):
        updater.atomic_json(self.root/'current.json', {'active': 'bundled', 'previous': 'bundled'})
        config = self.root/'config.json'
        config.write_text('preserve-me')
        self.fixture.files['toss.py'] = b'corrupt'
        with self.assertRaises(updater.UpdateError):
            self.install()
        self.assertEqual(updater.state(self.root)['active'], 'bundled')
        self.assertEqual(config.read_text(), 'preserve-me')
        self.assertFalse(list(self.root.glob('staging-*')))
        lock = updater.acquire_lock(self.root)
        lock.close()

    def test_reject_paths_duplicates_and_unsupported_types(self):
        for changes in [{'name': '../escape.py'}, {'type':'dir'}, {'size': 9999999}, {'target': 'secret'}, {'path':'other.py'}]:
            self.fixture = UpdateFixture()
            self.fixture.entries[0].update(changes)
            with self.subTest(changes), self.assertRaises(updater.UpdateError):
                self.install()
        self.fixture = UpdateFixture()
        self.fixture.entries.append(copy.deepcopy(self.fixture.entries[0]))
        with self.assertRaises(updater.UpdateError):
            self.install()

    def test_download_interrupted_or_version_mismatch(self):
        def failed(url):
            raise OSError('fixture')
        with self.assertRaises(updater.UpdateError):
            updater.install(self.fixture.channel, root=self.root, fetch=failed)
        self.fixture.channel['version'] = '0.4.2'
        with self.assertRaises(updater.UpdateError):
            self.install()
        self.assertEqual(updater.state(self.root)['active'], 'bundled')

    def test_pointer_write_failure_can_be_retried(self):
        original = updater.atomic_json
        def failed(path, value):
            if Path(path).name == 'current.json':
                raise OSError('fixture')
            return original(path, value)
        with patch.object(updater, 'atomic_json', side_effect=failed), self.assertRaises(updater.UpdateError):
            self.install()
        self.assertEqual(updater.state(self.root)['active'], 'bundled')
        self.assertEqual(self.install(), '0.4.1')

    def test_concurrent_update_blocked_and_lock_reusable(self):
        lock = updater.acquire_lock(self.root)
        try:
            with self.assertRaises(updater.UpdateError):
                self.install()
        finally:
            lock.close()
        self.assertEqual(self.install(), '0.4.1')

    def test_time_budget(self):
        ticks = iter([0, 0, 121])
        with self.assertRaises(updater.UpdateError):
            updater.install(self.fixture.channel, root=self.root, fetch=self.fixture.fetch, monotonic=lambda: next(ticks))
        self.assertEqual(updater.state(self.root)['active'], 'bundled')

    def test_launcher_rolls_back_crashing_version(self):
        launcher_path = Path(__file__).resolve().parents[1] / 'start_toss.py'
        spec = importlib.util.spec_from_file_location('stockbot_launcher_test', launcher_path)
        launcher = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(launcher)
        bundled = self.root/'bundle'
        package = bundled/'src/stockbot'
        package.mkdir(parents=True)
        (package/'__init__.py').write_text('')
        (package/'toss_gui.py').write_text('import os\nfrom pathlib import Path\nPath(os.environ["STOCKBOT_READY_FILE"]).touch()\n')
        self.install()
        bad = self.root/'versions'/('a'*40)/'src/stockbot/toss_gui.py'
        bad.write_text('raise SystemExit(3)\n')
        self.assertEqual(launcher.launch(bundled=bundled, root=self.root), 0)
        self.assertEqual(updater.state(self.root)['active'], 'bundled')


@unittest.skipUnless(sys.platform == 'win32' or os.environ.get('DISPLAY'), 'Native display required')
class DesktopGuiTests(unittest.TestCase):
    def setUp(self):
        import tkinter as tk
        from stockbot.toss_gui import TossDashboard
        self.root = tk.Tk()
        self.addCleanup(self.root.destroy)
        self.app = TossDashboard(self.root)
        self.root.update()

    def widgets(self, widget):
        return [child for w in widget.winfo_children() for child in [w, *self.widgets(w)]]

    def button(self, widget, text):
        from tkinter import ttk
        return next(w for w in self.widgets(widget) if isinstance(w, ttk.Button) and w.cget('text') == text)

    def settle(self):
        import time
        deadline = time.monotonic() + 5
        while self.app.busy and time.monotonic() < deadline:
            self.root.update()
            time.sleep(.01)
        self.assertFalse(self.app.busy)

    def test_credential_mask_save_and_delete(self):
        import tkinter as tk
        from tkinter import ttk
        self.app.credentials_dialog()
        self.root.update()
        dialog = next(w for w in self.root.winfo_children() if isinstance(w, tk.Toplevel))
        entries = [w for w in self.widgets(dialog) if isinstance(w, ttk.Entry)]
        self.assertTrue(all(w.cget('show') == '*' for w in entries))
        values = ['fixture-id', 'fixture-secret', '123']
        for entry, value in zip(entries, values):
            entry.insert(0, value)
        with patch('stockbot.toss_gui.WindowsVault') as vault:
            self.button(dialog, '입력한 값 저장').invoke()
            vault.return_value.save.assert_called_once_with(dict(zip(['client_id','client_secret','account_seq'], values)))
            self.assertTrue(all(entry.get() == '' for entry in entries))
            with patch('stockbot.toss_gui.messagebox.askyesno', return_value=True):
                self.button(dialog, '저장 정보 삭제').invoke()
            vault.return_value.delete.assert_called_once()
        self.button(dialog, '닫기').invoke()

    def test_update_cancel_and_install(self):
        import time
        candidate = UpdateFixture().channel
        with patch('stockbot.toss_gui.updater.check_update', return_value=candidate), patch('stockbot.toss_gui.messagebox.askyesno', return_value=False), patch('stockbot.toss_gui.updater.install') as install:
            self.app.check_updates()
            self.settle()
            install.assert_not_called()
            self.assertIn('취소', self.app.desktop_status.get())
        with patch('stockbot.toss_gui.updater.check_update', return_value=candidate), patch('stockbot.toss_gui.messagebox.askyesno', return_value=True), patch('stockbot.toss_gui.updater.install', return_value='0.4.1') as install:
            self.app.check_updates()
            self.settle()
            install.assert_called_once_with(candidate)
            self.assertIn('TossTrading.cmd', self.app.desktop_status.get())

    def test_update_failure_fixed_message(self):
        with patch('stockbot.toss_gui.updater.check_update', side_effect=RuntimeError('do-not-display-fixture-secret')):
            self.app.check_updates()
            self.settle()
            self.assertNotIn('fixture-secret', self.app.desktop_status.get())
            self.assertIn('기존 버전', self.app.desktop_status.get())
