"""Read-only bounded-memory scan. No file paths, values, or content are logged."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

PATTERNS = {
    "credential_field": re.compile(rb"(?i)(?:api[_-]?key|private[_-]?key|client[_-]?secret|access[_-]?token|refresh[_-]?token|password|passwd|authorization)"),
    "account_identifier_field": re.compile(rb"(?i)(?:account[_-]?number|broker[_-]?account)"),
    "pem_private_key_marker": re.compile(rb"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----"),
}
TEXT_EXT = {".json", ".txt", ".yaml", ".yml", ".toml", ".ini", ".env", ".csv", ".md"}
CHUNK_SIZE = 1024 * 1024
OVERLAP = 256
MAX_FILE_BYTES = 1024 * 1024 * 1024
# Exact Git blob of the manually reviewed state-branch README. Changes fail closed.
REVIEWED_README_BLOB = "81626893c0573d93cec3b0b5da974615e092e2e3"


def inspect(path):
    kinds = set()
    size = path.stat().st_size
    if size > MAX_FILE_BYTES:
        return None, "over_1gib"
    with path.open("rb") as stream:
        tail = b""
        while True:
            chunk = stream.read(CHUNK_SIZE)
            if not chunk:
                break
            data = tail + chunk
            for name, pattern in PATTERNS.items():
                if pattern.search(data):
                    kinds.add(name)
            tail = data[-OVERLAP:]
    return sorted(kinds), None


def scan(root):
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("not a directory")
    result = {"checked": 0, "flagged": 0, "skipped": 0, "reviewed_documentation": 0, "findings": []}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("symlink rejected")
        if not path.is_file() or ".git" in path.relative_to(root).parts:
            continue
        if path.suffix.lower() not in TEXT_EXT:
            continue
        fingerprint = hashlib.sha256(path.relative_to(root).as_posix().encode()).hexdigest()[:16]
        try:
            kinds, reason = inspect(path)
        except OSError:
            result["skipped"] += 1
            result["findings"].append({"id": fingerprint, "status": "skipped", "reason": "read_error"})
            continue
        if reason:
            result["skipped"] += 1
            result["findings"].append({"id": fingerprint, "status": "skipped", "reason": reason})
            continue
        result["checked"] += 1
        if kinds == ["credential_field"] and path.relative_to(root).as_posix() == "README.md":
            # Only suppress the known documentation-only false positive for
            # the exact content reviewed. Any README change triggers review.
            with path.open("rb") as stream:
                body = stream.read()
            blob = hashlib.sha1(b"blob " + str(len(body)).encode() + b"\\0" + body).hexdigest()
            if blob == REVIEWED_README_BLOB:
                result["reviewed_documentation"] += 1
                continue
            # A blob mismatch may be a line-ending conversion or changed text.
            # Log only the Git object digest, never README contents or paths.
            result["reviewed_documentation_blob_mismatch"] = blob
        if kinds:
            result["flagged"] += 1
            result["findings"].append({"id": fingerprint, "status": "flagged", "categories": kinds})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    args = parser.parse_args()
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
