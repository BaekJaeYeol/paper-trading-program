"""Block sensitive files from Git commits without reading their contents."""

import re
import subprocess
import sys
from pathlib import PurePosixPath


BLOCKED_SUFFIXES = (
    ".db",
    ".db3",
    ".sqlite",
    ".sqlite3",
    ".pem",
    ".key",
    ".p12",
    ".pfx",
)

BLOCKED_DIRECTORIES = {
    "state",
    "hourly-state",
    "intraday-state",
    "encrypted-backups",
    "private-backups",
}

BLOCKED_FILENAMES = {
    ".env",
    "id_rsa",
    "id_ed25519",
}

DATABASE_TEMP = re.compile(
    r"\.(?:db|db3|sqlite|sqlite3)-(?:wal|shm|journal)$",
    re.IGNORECASE,
)


def is_blocked(filename):
    path = PurePosixPath(filename)
    parts = [part.lower() for part in path.parts]
    name = path.name.lower()

    if any(part in BLOCKED_DIRECTORIES for part in parts[:-1]):
        return True

    if name in BLOCKED_FILENAMES:
        return True

    if name.startswith(".env.") and name != ".env.example":
        return True

    if name.endswith(BLOCKED_SUFFIXES):
        return True

    if DATABASE_TEMP.search(name):
        return True

    return False


def staged_paths():
    result = subprocess.run(
        [
            "git",
            "diff",
            "--cached",
            "--name-only",
            "--diff-filter=ACMR",
            "-z",
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    return [
        item.decode("utf-8", errors="surrogateescape")
        for item in result.stdout.split(b"\0")
        if item
    ]


def main():
    try:
        paths = staged_paths()
    except (OSError, subprocess.CalledProcessError):
        print("SECURITY CHECK ERROR: Git index inspection failed.")
        return 2

    blocked = [path for path in paths if is_blocked(path)]

    if blocked:
        print(
            "SECURITY CHECK FAILED: "
            f"{len(blocked)} prohibited staged file(s)."
        )
        print("Remove prohibited files from the Git index.")
        print("File names are hidden to avoid exposing sensitive paths.")
        return 1

    print(f"SECURITY CHECK PASSED: {len(paths)} staged file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())