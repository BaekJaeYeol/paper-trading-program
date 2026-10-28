# Paper trading state: private storage migration plan

Status: **PLAN ONLY**. No workflow, branch, credentials, or state data has been migrated.
Date: 2026-10-28.

## Verified current dependencies
- Public code repository: `BaekJaeYeol/paper-trading-program`.
- Public state branch: `paper-hourly-state`; used by `.github/workflows/investment-hourly.yml` and `.github/workflows/investment-intraday.yml`.
- `investment-lab/session_worker.py` hardcodes `paper-hourly-state` in `refresh()` and `publish()`.
- `investment-lab/hourly.py` accepts a filesystem state directory.
- `investment-lab/state_recovery.py` checks snapshots and uses a process lock.
- The state branch includes JSON and SQLite research checkpoints, and large generated dashboard output. These are already public and making a new private copy does **not** erase public history.

## Proposed destination (not created)
- Dedicated **private** repository, proposed name `paper-trading-private-state` (availability and final name to confirm).
- Private repo should contain **state only**, not credentials, personal identifiers, or application source.
- Limit automation access to contents read/write for that destination; no general-purpose PAT in workflow text.
- Prefer a dedicated GitHub App installation token with narrowly scoped repository access; validate token lifetime and renewal for long-running sessions. Do not expose token in logs.
- If the existing GitHub App / Actions permissions cannot provide secure cross-repo access, **stop** instead of silently falling back to the public branch.

## Migration phases
1. Freeze a consistent checkpoint; record source commit SHA, inventory, per-file SHA-256, file counts and validation status. Do not freeze while a writer is active.
2. Create destination private repo and restricted credentials; test read/write with non-sensitive dummy data only.
3. Copy checkpoints to the private destination, preserving paths and metadata needed for recovery; validate SQLite integrity and representative balances/positions against the source.
4. Make branch/ref and remote configurable in `session_worker.py`; fail closed if the remote is not the approved private destination. Ensure `publish()` never pushes private state to the public repo.
5. Update both workflows' checkout, authentication and state paths; run dry-run and failure-injection tests before enabling scheduled jobs.
6. Cut over one controlled session with concurrent writers disabled; verify next-run restoration, duplicate-order protection, lock behavior and checkpoint persistence.
7. Only after a verified cutover, decide whether to disable public state publication and how to handle previously exposed public history. Never rewrite history or delete state automatically.

## Test gates
- No real brokerage orders or live trading enabled.
- Balance/position equality; all expected SQLite DBs readable; no missing state.
- Interrupted write, failed pull/rebase/push, token expiry, private repo unavailable.
- Simultaneous session attempts, emergency stop, retry idempotence, checkpoint recovery.
- Secret scanning on files and logs, artifact publication and GitHub Step Summary.
- Confirm public branch receives **zero** new state commits after cutover.

## Rollback
- Preserve original public branch and source SHA until verified; do not delete.
- Rollback requires explicit review of privacy consequences: reverting to public state publication would re-expose newly generated state. Prefer pausing automated writes over publishing sensitive state to public.
- Restore from the last validated private checkpoint; require operator approval if account snapshots diverge.

## Explicitly out of scope now
- Creating a repository or token; modifying GitHub Actions; moving or deleting data; rewriting Git history; changing trading strategies or activating real trades.
