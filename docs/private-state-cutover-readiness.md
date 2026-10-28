# Private state cutover readiness (2026-10-28)

**Decision: NOT READY.** This is a read-only code review; no existing workflow or state was modified.

## Verified

- A manually dispatched GitHub Actions smoke test authenticated as the dedicated GitHub App and committed a synthetic JSON marker to the private repository (`verification/actions-auth-smoke-test.json`, run 40655399529).
- The hourly workflow checks out `paper-hourly-state` in the source repository and commits/pushes `hourly-state` there.
- The intraday workflow also checks out `paper-hourly-state` in the source repository.
- `investment-lab/session_worker.py` hardcodes `paper-hourly-state` in both pull and push. Merely changing workflow checkout is therefore insufficient.
- Intraday sessions may run for up to 19,800 seconds (5.5 hours); a single GitHub App installation token may expire before a later push.

## Required before migration

1. Obtain a separate, verified backup of the state branch; record commit ID, file manifest and checksums. Do not place credentials or account identifiers in public logs.
2. Validate SQLite `PRAGMA integrity_check`, JSON schema and internal account/position consistency against a frozen snapshot; reject incomplete snapshots.
3. Implement a destination repository/branch allowlist with explicit fail-closed checks in both hourly workflow and intraday worker. Never fall back to `paper-hourly-state` on auth or push failure.
4. Implement a token refresh strategy for long-running intraday sessions. Avoid logging or persisting installation tokens.
5. Exercise synthetic end-to-end tests: initial checkout, update, retry, token expiration, network failure, concurrent writers, rollback and emergency-stop state.
6. Cut over scheduled workflows only after successful tests and operator review; observe results before retiring old state writes.
7. Treat public history as already exposed; migration to private storage does not remove historic public data.

## Explicit non-goals

No live brokerage trading, no strategy changes, no deletion or rewriting of public history, and no unreviewed transfer of state data.
