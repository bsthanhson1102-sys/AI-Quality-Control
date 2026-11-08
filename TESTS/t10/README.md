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
