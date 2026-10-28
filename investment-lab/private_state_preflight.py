"""Read-only preflight for a frozen paper-trading state checkout.

No network, no Git writes, no account mutation. Output contains only aggregate counts.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sqlite3
import sys


def check(root: Path) -> dict:
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("state root must be a directory")
    report = {"sqlite_checked": 0, "json_checked": 0, "files_hashed": 0, "bytes_hashed": 0}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("symlinks are not allowed in snapshot")
        if not path.is_file():
            continue
        if ".git" in path.relative_to(root).parts:
            continue
        suffix = path.suffix.lower()
        if suffix not in {".json", ".sqlite", ".db"}:
            continue
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
                report["bytes_hashed"] += len(chunk)
        report["files_hashed"] += 1
        if suffix == ".json":
            with path.open("r", encoding="utf-8") as stream:
                json.load(stream)
            report["json_checked"] += 1
        else:
            uri = path.as_uri() + "?mode=ro&immutable=1"
            with sqlite3.connect(uri, uri=True) as db:
                result = db.execute("PRAGMA integrity_check").fetchone()
                if result is None or result[0] != "ok":
                    raise ValueError("SQLite integrity check failed")
            report["sqlite_checked"] += 1
    if report["files_hashed"] == 0:
        raise ValueError("no JSON or SQLite files found")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", required=True, type=Path)
    args = parser.parse_args()
    try:
        report = check(args.state)
    except (OSError, ValueError, json.JSONDecodeError, sqlite3.DatabaseError) as exc:
        print("Preflight failed: " + type(exc).__name__, file=sys.stderr)
        return 1
    print(json.dumps({"status": "passed", **report}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
