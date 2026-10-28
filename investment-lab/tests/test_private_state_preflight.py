"""Synthetic tests only: no real account data or network access."""
import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "private_state_preflight.py"
spec = importlib.util.spec_from_file_location("private_state_preflight", MODULE)
preflight = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preflight)


class PrivateStatePreflightTests(unittest.TestCase):
    def test_valid_synthetic_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "state.json").write_text(json.dumps({"synthetic": True}), encoding="utf-8")
            with sqlite3.connect(root / "state.sqlite") as db:
                db.execute("CREATE TABLE marker (id INTEGER PRIMARY KEY)")
                db.execute("INSERT INTO marker VALUES (1)")
            result = preflight.check(root)
            self.assertEqual(result["json_checked"], 1)
            self.assertEqual(result["sqlite_checked"], 1)
            self.assertEqual(result["files_hashed"], 2)

    def test_invalid_json_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "bad.json").write_text("{", encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                preflight.check(Path(tmp))

    def test_invalid_sqlite_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "bad.sqlite").write_bytes(b"not a sqlite database")
            with self.assertRaises(sqlite3.DatabaseError):
                preflight.check(Path(tmp))

    def test_empty_snapshot_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                preflight.check(Path(tmp))


if __name__ == "__main__":
    unittest.main()
