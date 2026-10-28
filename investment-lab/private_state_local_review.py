"""Local-only lookup of a redacted sensitive-scan finding.

Do not run this tool in GitHub Actions or paste its file path output publicly.
Never prints matching lines, values, or file contents.
"""
import argparse
import hashlib
from pathlib import Path
import sys

# Import the scanner without changing its detection rules.
from private_state_sensitive_scan import inspect, TEXT_EXT


def main():
    parser = argparse.ArgumentParser(description="Review one finding on your own computer only")
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--id", required=True, help="16-character ID from scan log")
    args = parser.parse_args()
    if not (len(args.id) == 16 and all(c in "0123456789abcdef" for c in args.id)):
        parser.error("Expected a 16-character lowercase hex ID")
    if "GITHUB_ACTIONS" in __import__("os").environ:
        parser.error("Local review is not permitted in GitHub Actions")
    root = args.state.resolve(strict=True)
    if not root.is_dir():
        parser.error("State must be a directory")
    matches = []
    for path in root.rglob("*"):
        if path.is_symlink():
            parser.error("Symlink encountered; aborting")
        if not path.is_file() or ".git" in path.relative_to(root).parts:
            continue
        if path.suffix.lower() not in TEXT_EXT:
            continue
        rel = path.relative_to(root).as_posix()
        fingerprint = hashlib.sha256(rel.encode()).hexdigest()[:16]
        if fingerprint == args.id:
            kinds, reason = inspect(path)
            matches.append((rel, kinds, reason))
    if len(matches) != 1:
        print("Matching file count:", len(matches))
        return 1
    rel, kinds, reason = matches[0]
    print("LOCAL ONLY - do not paste the path or contents into chat or public logs")
    print("Relative file path:", rel)
    print("Detection categories:", ", ".join(kinds or []) if not reason else reason)
    print("Inspect this file locally. Never disclose credential values.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
