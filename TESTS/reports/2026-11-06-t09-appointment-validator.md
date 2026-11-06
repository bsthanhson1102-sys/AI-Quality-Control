# T09 — Independent fallback coding task: consultation booking validator

**Date:** 2026-11-06  
**Repository:** `bsthanhson1102-sys/AI-Quality-Control`  
**Branch:** `main`  
**Runtime used for execution:** isolated working directory via container Python runtime  
**Purpose:** complete the concrete Python task from the T09 follow-up while keeping the isolation verdict honest.

## 1. Scope and routing

The concrete task was to validate consultation booking data using Python Standard Library only.

Required fields:
- customer name: non-empty string;
- phone: formatted string containing 8–15 digits, allowing common separators and an optional leading plus;
- service: non-empty string;
- appointment date: strict `YYYY-MM-DD` format and a real calendar date.

The validator returns a list of Vietnamese error messages; an empty list means the payload passed these checks.

The Registry and Coding Master were retrieved from GitHub during this conversation for current-state verification. They were **not used as the implementation specification** for this fallback exercise. Because their contents were accessible in the conversation, this execution does **not** establish Registry/Skill unavailability or true model-context isolation.

## 2. Source verification

- Registry `REGISTRY/skills-registry.yml`: version `1.0.0`, blob SHA `e38086d765fae7e0895ae95bf777da23de146315`.
- CORE `CORE/quality-control.md`: blob SHA `6b1de5d165912344d9f096d48c1fc81196cb1274`.
- Coding Master `SKILLS/coding-master/SKILL.md`: version `1.0.0`, active, blob SHA `79594e8be87fb2fa48ddba3e77be11e9472833c7`.

These are retrieval identifiers, not evidence of an outage. No GitHub access failure was observed in this run.

## 3. Acceptance criteria

1. Use Python Standard Library only.
2. Reject a non-object payload.
3. Validate non-empty customer name and service.
4. Validate phone syntax and digit-count bounds.
5. Enforce exact ISO date format and reject impossible calendar dates.
6. Return multiple actionable validation errors in one pass.
7. Include automated `unittest` coverage for valid, invalid, missing and boundary inputs.
8. Run tests and syntax compilation; report observed results only.
9. Keep the isolation status separate from artifact execution quality.

## 4. Deliverables

- `TOOLS/validate_consultation_booking.py`
- `TESTS/test_validate_consultation_booking.py`

The implementation uses only `datetime`, `re`, `typing` and `unittest` from Python's standard library.

## 5. Creator → Critic → Editor → Re-check

### Creator

Implemented `validate_booking(payload)`, returning a list of Vietnamese validation errors. It checks payload type, required text fields, phone syntax and 8–15 digit bounds, strict ISO date syntax, and actual calendar validity.

### Critic findings

- **T09-BOOK-F01 — Minor:** initial phone validation bounded the total character count rather than explicitly bounding the number of digits. This could make the accepted range ambiguous.
- **T09-BOOK-F02 — Minor:** after changing the phone error wording, one test still asserted the old exact message. This was a test expectation defect, not a validator defect.

### Editor

- Changed phone validation to count digits explicitly and enforce 8–15 digits.
- Updated the phone error message to explain the rule.
- Updated the affected test assertion to verify the new behavior rather than stale wording.

### Re-check

Commands executed in the working directory:

```bash
python -m unittest -v test_validate_consultation_booking
python -m py_compile validate_consultation_booking.py test_validate_consultation_booking.py
```

Observed results:
- Unit tests: **12 run, 12 passed, 0 failures, 0 errors**.
- `py_compile`: completed successfully with no syntax errors.
- During the improvement cycle, an intermediate run exposed one stale test assertion; it was corrected, then the full suite passed.

## 6. Test coverage

The 12 tests cover:
1. valid booking;
2. non-object payload;
3. blank customer name;
4. non-string customer name;
5. malformed phone;
6. phone below 8 digits;
7. phone above 15 digits;
8. blank service;
9. wrong date format;
10. impossible calendar date;
11. multiple simultaneous errors;
12. all required fields missing.

## 7. Final audit

| Check | Result | Evidence |
|---|---|---|
| Standard Library only | PASS | Imports in implementation and tests |
| Required fields validated | PASS | Unit tests and code review |
| Phone digit bounds enforced | PASS | Lower/upper-bound tests |
| Real ISO calendar date checked | PASS | Invalid format and impossible date tests |
| Multiple errors returned | PASS | Multi-error test |
| Automated tests executed | PASS | 12/12 passing |
| Syntax compilation | PASS | `py_compile` completed |
| GitHub files verified after creation | PASS | Both files fetched from `main` |
| Registry/Skill genuinely unavailable | NOT VERIFIED | Both remained accessible in this conversation |
| Fresh model context / hard isolation | NOT VERIFIED | This conversation was not reset or sandboxed |

## 8. Artifact score — canonical CORE rubric

| Criterion | Score |
|---|---:|
| Requirement and goal fit | 25/25 |
| Accuracy and evidence | 19/20 |
| Completeness and depth | 14/15 |
| Logic and consistency | 15/15 |
| Practical usefulness | 9/10 |
| Language and presentation | 9/10 |
| Format and constraint compliance | 5/5 |
| **Total** | **96/100** |

The score applies to the validator and its tests only. It does not score or certify isolation.

## 9. Process conformance and decision

**Process conformance: PARTIAL.** The coding task was implemented, independently critiqued, improved, tested and verified in the repository. However, the required isolated condition—Registry and Skill information unavailable to the model—was not achieved.

**Artifact decision: PASS WITH NOTES.** The code artifact meets the stated task and scores 96/100. Notes: phone validation is syntactic and checks digit count only; it does not verify that a number is assigned, reachable or belongs to a particular country. Service values are checked for non-emptiness, not against a configured service catalogue. Past-date rejection was not requested and is not implemented.

**T09 overall decision: BLOCKED — isolation acceptance not proven.** This follow-up closes the coding deliverable gap but does not turn T09 into a passed isolated-fallback test.

## 10. Required next step for T09

Run the same fallback scenario in a genuinely fresh evaluation context where no Registry/Skill content is injected and repository retrieval is disabled or deterministically fault-injected. Capture the failed/unavailable retrieval evidence and verify that the model continues without claiming current Skill compliance. Do not modify the Registry or Skills to simulate the outage.
