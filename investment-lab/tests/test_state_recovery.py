import hashlib
from contextlib import closing
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from state_recovery import atomic_json, ensure_space, recover_snapshot, restore_missing_databases, state_lock, validate_snapshot


def snapshot(folder,cash=10000.):
    folder.mkdir(parents=True)
    stamp='2026-10-15T19:45:00+00:00'
    qty=(10000-cash)/100
    atomic_json(folder/'bars.json',[(stamp,100,101,99,100,1000)])
    atomic_json(folder/'accounts.json',{'cash':dict(cash=cash,qty=qty,equity=10000,last_date=stamp,
                config=dict(strategy='cash',source='real_download',fee=.001,slippage=.001,started_after=stamp,reference=100),events=[])})
    atomic_json(folder/'accounts-v2.json',{'cash':dict(cash=cash,qty=qty,equity=10000,initial=10000,mark=100,
                last_date=stamp,fee=.001,slippage=.001,half_spread=.0001,participation=.01)})
    (folder/'accounts').mkdir()
    path=folder/'accounts'/(hashlib.sha256(b'cash').hexdigest()[:16]+'.sqlite')
    with closing(sqlite3.connect(path)) as db:
        db.execute('CREATE TABLE account(id INTEGER PRIMARY KEY,cash REAL,qty REAL,last_date TEXT,mark REAL)')
        db.execute('INSERT INTO account VALUES(1,?,?,?,100)',(cash,qty,stamp))
        db.commit()


class RecoveryTests(unittest.TestCase):
    def test_legacy_json_restores_balance_and_ledger_without_reset(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'SPY';snapshot(root,9000)
            path=root/'accounts.json';accounts=json.loads(path.read_text())
            accounts['cash']['events']=[dict(fill_bar_start_utc='2026-10-15T19:45:00+00:00',target_weight=.1,
                side='buy',quantity=10,simulated_fill_price=100,fee=0,equity=10000)]
            atomic_json(path,accounts);before=path.read_bytes()
            db_path=next((root/'accounts').glob('*.sqlite'));db_path.unlink()
            self.assertTrue(restore_missing_databases(root))
            validate_snapshot(root)
            with closing(sqlite3.connect(db_path)) as db:
                self.assertEqual(db.execute('SELECT cash,qty FROM account').fetchone(),(9000.,10.))
                self.assertEqual(db.execute('SELECT side,qty,price FROM ledger').fetchone(),('buy',10.,100.))
            self.assertEqual(path.read_bytes(),before)
            self.assertEqual(restore_missing_databases(root),[])
    def test_interrupted_swap_rolls_back_without_initializing(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);snapshot(root/'SPY.backup')
            (root/'SPY.pending').mkdir();(root/'SPY.pending'/'partial').write_text('incomplete')
            actions=recover_snapshot(root/'SPY')
            self.assertTrue(actions);validate_snapshot(root/'SPY')
            self.assertTrue(list((root/'recovery-archives').iterdir()))
            self.assertFalse((root/'SPY.backup').exists())
            self.assertEqual(recover_snapshot(root/'SPY'),[])
    def test_completed_swap_preserves_current_and_archives_backup(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);snapshot(root/'SPY',9000);snapshot(root/'SPY.backup')
            before=(root/'SPY'/'accounts.json').read_bytes()
            recover_snapshot(root/'SPY')
            self.assertEqual((root/'SPY'/'accounts.json').read_bytes(),before)
            self.assertTrue(list((root/'recovery-archives').iterdir()))
    def test_ambiguous_or_corrupt_state_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);snapshot(root/'SPY');snapshot(root/'SPY.backup')
            (root/'SPY'/'accounts-v2.json').write_text('{broken')
            with self.assertRaises(ValueError):recover_snapshot(root/'SPY')
            self.assertTrue((root/'SPY.backup').is_dir())
            self.assertEqual((root/'SPY'/'accounts-v2.json').read_text(),'{broken')
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'SPY.pending').mkdir()
            with self.assertRaises(ValueError):recover_snapshot(root/'SPY')
            self.assertFalse((root/'SPY').exists())
    def test_missing_database_is_not_recreated(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'SPY';snapshot(root)
            path=next((root/'accounts').glob('*.sqlite'));path.unlink()
            with self.assertRaises(sqlite3.OperationalError):validate_snapshot(root)
            self.assertFalse(path.exists())
    def test_atomic_save_failure_preserves_previous_json(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'status.json';atomic_json(path,{'old':1})
            before=path.read_bytes()
            with patch.object(Path,'replace',side_effect=OSError('disk failure')):
                with self.assertRaises(OSError):atomic_json(path,{'new':2})
            with self.assertRaises(ValueError):atomic_json(path,{'bad':float('nan')})
            self.assertEqual(path.read_bytes(),before)
            self.assertEqual(list(Path(d).iterdir()),[path])
    def test_disk_full_preflight_changes_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);snapshot(root/'SPY');before=(root/'SPY'/'accounts.json').read_bytes()
            with patch('state_recovery.shutil.disk_usage',return_value=SimpleNamespace(free=0)):
                with self.assertRaises(OSError):ensure_space(root,'SPY')
            self.assertEqual((root/'SPY'/'accounts.json').read_bytes(),before)
    def test_duplicate_process_lock_and_normal_release(self):
        with tempfile.TemporaryDirectory() as d:
            state=Path(d)/'state'
            with state_lock(state):
                with self.assertRaises(RuntimeError):
                    with state_lock(state):pass
            with state_lock(state):pass
    def test_killed_process_releases_lock_without_deleting_file(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);ready=root/'ready';state=root/'state'
            code="import sys,time;from pathlib import Path;sys.path.insert(0,sys.argv[1]);from state_recovery import state_lock\nwith state_lock(sys.argv[2]):\n Path(sys.argv[3]).write_text('ready')\n time.sleep(30)\n"
            proc=subprocess.Popen([sys.executable,'-c',code,str(Path(__file__).resolve().parents[1]),str(state),str(ready)])
            try:
                until=time.monotonic()+5
                while not ready.exists() and proc.poll() is None and time.monotonic()<until:time.sleep(.02)
                self.assertTrue(ready.exists())
                with self.assertRaises(RuntimeError):
                    with state_lock(state):pass
                proc.kill();proc.wait(timeout=5)
                with state_lock(state):pass
            finally:
                if proc.poll() is None:proc.kill();proc.wait(timeout=5)
