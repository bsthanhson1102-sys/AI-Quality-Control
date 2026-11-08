# T10 execution gate

## Purpose
`content_gate.py` is a conservative text preflight. `release_gate.py` validates a JSON evidence ledger for traceability and refuses structural approval when mandatory fields, correction mappings, scores, or domain gates are absent. **It cannot verify that an LLM reviewer actually performed its review, or that its factual judgments are true.**

## Run
From repository root:

```bash
python -m unittest discover -s TESTS/t10 -p 'test_*.py' -v
python TESTS/t10/content_gate.py path/to/draft.txt
python TESTS/t10/release_gate.py path/to/ledger.json
```

Exit code 2 means blocked; exit code 0 on the release gate means only `SCHEMA_ACCEPTED_REVIEW_REQUIRED`, **not** CORE PASS. An actual reviewer must validate content quality, evidence and platform risk separately.

## Ledger contract
Required: `brief`, `candidate` (initial full draft), `artifact` (revised full text), `critic` (array of findings with id/severity/passage/reason), `editor_changes` (array of finding_id/before/after), `recheck` (finding ID -> RESOLVED), `final_auditor` (scores seven numbers 25/20/15/15/10/10/5, technical_gate/domain_gate PASS, evidence_complete/regression_clear true), and `rounds` (1..4). For each Major/Critical, the exact passage must exist in the draft, the correction must be visible in the final artifact and recheck must be RESOLVED.

## Boundaries
- The gate only checks supplied JSON and exact text substrings; self-reported evidence can be fabricated. Schema acceptance must never be marketed as independent quality certification.
- GitHub files do not automatically execute in normal ChatGPT tabs.
- An external orchestrator or supported tool integration must explicitly invoke the gate and enforce its exit status before publication. Without that integration, cross-tab auto-enforcement is NOT RUN.
- Existing CORE 90/100 threshold, seven weights, no unresolved Critical/Major, and four-round maximum remain unchanged.

## Test matrix
Missing Critic; missing Editor map; unresolved Major; missing Final Auditor; low CORE score; five rounds; domain NOT RUN; fake correction; blank finding; nonexistent finding passage; invalid score type; valid schema (review required). Run the command above and retain its output for evidence.

## Fail-closed publishing adapter

`publish_gate.py` is the executable integration point for **external publication workflows**. The workflow must refuse to publish unless this command exits 0:

```bash
python TESTS/t10/publish_gate.py path/to/ledger.json --approval path/to/approval.json
```

The separate approval file must contain `artifact_sha256` (SHA-256 of the exact UTF-8 final artifact string), `decision: "APPROVED"`, non-empty `reviewer` and `evidence`, and `domain_review: "PASS"`, `technical_review: "PASS"`. Any missing approval, changed artifact, missing reviewer, unresolved Major, insufficient CORE score or unexecuted gate returns exit code 2 and `BLOCKED`. Success returns `APPROVAL_RECORDED`, **not** an independently verified PASS: the approval is an attributable claim, not cryptographically authenticated. The operator and publishing system must verify reviewer identity, claims and actual review evidence before using it to publish. Never accept an LLM-generated approval as independent human approval.

This adapter **does not automatically hook into ChatGPT** and the repository does not yet contain a production publishing system. A workflow using this adapter must explicitly check its exit code and only proceed when authorized.

Run all T10 tests:

```bash
python -m unittest discover -s TESTS/t10 -p 'test_*.py' -v
```
