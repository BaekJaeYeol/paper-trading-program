"""Conservative local-only scan of a frozen snapshot; no content is printed.

Heuristics are not a substitute for manual review or secret scanning.
"""
import argparse
import json
from pathlib import Path
import re
import sys

KEY = re.compile(r"(?i)(?:api[_-]?key|private[_-]?key|client[_-]?secret|access[_-]?token|refresh[_-]?token|password|passwd|authorization|account[_-]?number|broker[_-]?account)")
TEXT_EXT = {".json", ".txt", ".yaml", ".yml", ".toml", ".ini", ".env", ".csv", ".md"}
MAX_BYTES = 8 * 1024 * 1024


def scan(root):
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("not a directory")
    checked = 0
    flagged = 0
    skipped = 0
    for path in root.rglob("*"):
        if path.is_symlink():
            raise ValueError("symlink rejected")
        if not path.is_file() or ".git" in path.relative_to(root).parts:
            continue
        if path.suffix.lower() not in TEXT_EXT:
            continue
        if path.stat().st_size > MAX_BYTES:
            skipped += 1
            continue
        checked += 1
        try:
            data = path.read_text(encoding="utf-8")
        except UnicodeError:
            skipped += 1
            continue
        if KEY.search(data) or "-----BEGIN PRIVATE KEY-----" in data:
            flagged += 1
    return {"checked": checked, "flagged": flagged, "skipped": skipped}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--state", type=Path, required=True)
    args = p.parse_args()
    try:
        result = scan(args.state)
    except (OSError, ValueError) as exc:
        print("Sensitive data preflight failed:", type(exc).__name__, file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    if result["flagged"] or result["skipped"] or not result["checked"]:
        print("Review required; transfer blocked", file=sys.stderr)
        return 2
    print("Heuristic scan passed; manual review still required")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
