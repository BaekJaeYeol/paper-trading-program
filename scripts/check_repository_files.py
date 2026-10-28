"""Check tracked repository paths for prohibited state files."""

import subprocess
import sys

from check_staged_files import is_blocked


def main():
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (OSError, subprocess.CalledProcessError):
        print("SECURITY CHECK ERROR: Cannot inspect tracked files.")
        return 2

    paths = [
        item.decode("utf-8", errors="surrogateescape")
        for item in result.stdout.split(b"\0")
        if item
    ]

    blocked = [path for path in paths if is_blocked(path)]

    if blocked:
        print(
            "SECURITY CHECK FAILED: "
            f"{len(blocked)} prohibited tracked file(s)."
        )
        return 1

    print(f"REPOSITORY SECURITY CHECK PASSED: {len(paths)} tracked files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())