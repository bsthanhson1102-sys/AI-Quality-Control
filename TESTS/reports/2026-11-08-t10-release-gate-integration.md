# T10 release-gate integration — 2026-11-08

## Scope
User authorized integration of release gate, tests, guidance, and workflow. Created:
- `TESTS/t10/release_gate.py` (blob d70474318a98332a65d3d8a89b968875f7828177)
- `TESTS/t10/test_release_gate.py` (blob ddcfd8f47b6a6fcf0ad7cc22616a1d2bc888ab31)
- `TESTS/t10/README.md` (blob e4f4a64640037c161e0be4518a9eaea4d4b2b375)
- `.github/workflows/t10-execution.yml` (blob 421c0908cf5343e0ec93906bcfe57cb4eb866b34)

## Actual evidence
- VERIFIED: GitHub create and readback for all four files.
- VERIFIED: Earlier local ZIP version of T10 gate ran 14/14 unit tests with `python -m unittest discover -v` in a container. This is NOT the exact committed version.
- NOT RUN: unit suite against exact committed files.
- NOT VERIFIED: GitHub Actions run status/logs (workflow file existence is not execution).
- NOT RUN: automatic invocation in a fresh ChatGPT tab.
- NOT RUN: end-to-end independent editorial judgment and real publication blocking.

## Findings and corrections
- Critic found that earlier local gate could return `PASS` for a self-reported, structurally complete ledger, even without independent content validation.
- Editor changed committed gate to return `SCHEMA_ACCEPTED_REVIEW_REQUIRED` instead of `PASS` on a structurally complete ledger.
- Editor added checks for critic passage occurring in initial draft, invalid severity, and score types.
- Re-check: GitHub file readback VERIFIED; exact committed-code regression NOT RUN.
- Final audit: integration artifact exists and is readable, but test execution and runtime integration remain unverified; overall T10 NOT PASS.

## Next action
Observe GitHub Actions run and logs for the exact committed test suite; repair failures if present. Then arrange an actual ChatGPT runtime integration or explicit orchestration invoking this gate. A new-tab content test without that integration is observational only and cannot demonstrate automatic enforcement.
