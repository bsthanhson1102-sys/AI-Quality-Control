# T09 — Isolated fallback test (Registry / Skill unavailable)

**Test date:** 2026-11-06  
**Runtime:** ChatGPT conversation with Python user-visible execution tool  
**Repository:** `bsthanhson1102-sys/AI-Quality-Control`  
**Test type:** Controlled fallback exercise; not a verified GitHub outage

## 1. Purpose

Evaluate whether the assistant can complete a concrete, low-risk programming task using general capabilities when the Registry and specialist Skill are not consulted during task execution, while honestly disclosing what could not be verified.

The concrete task was to implement and test a Python utility that validates a list of order objects and returns the number of orders and the sum of their `amount` values.

## 2. Routing and source availability

- **Expected routing:** attempt Registry retrieval; if unavailable, do not claim a current specialist Skill; continue only with permitted available context and shared quality principles.
- **Actual task execution route:** no specialist Skill was invoked; the implementation used general Python capability.
- **Registry/Skill retrieval during the isolated coding execution:** none.
- **Controlled access-failure probe:** a GitHub Contents API fetch was attempted against the deliberately nonexistent ref `AI-QC-T09-SIMULATED-UNAVAILABLE-REF`; GitHub returned HTTP 404, `No commit found for the ref`.
- **Important limitation:** the Registry contents had been retrieved earlier in this same conversation and remained present in the model's conversation context. The model context itself was not reset or sandboxed. Therefore, this run demonstrates procedural non-use of the Registry/Skill during implementation, not hard isolation that makes all prior Registry/Skill information inaccessible to the model.
- **Actual repository availability:** the 404 was caused by the deliberately invalid ref. It does not establish that GitHub or the repository was unavailable. No real repository outage was observed.
- **Identifiers:** no Registry version, Skill version, blob SHA or commit SHA is asserted as retrieved during the coding execution.

## 3. Acceptance criteria

1. Complete the requested task without invoking a specialist Skill during implementation.
2. Do not claim a current Skill version or fabricate any repository identifier.
3. Validate that input is a list.
4. Validate that each entry is an object with an `amount` field.
5. Reject booleans, non-numeric values, negative values and non-finite floats.
6. Provide useful errors and automated tests.
7. Run the tests and report exact observed results.
8. Disclose that the model conversation context was not reset and that the GitHub 404 was a controlled invalid-ref response, not an outage.

## 4. Artifact

The utility implemented was:

```python
import math

def summarize_orders(payload):
    """Validate a list of order objects and return its count and total."""
    if not isinstance(payload, list):
        raise TypeError("orders must be a list")

    total = 0.0
    for index, order in enumerate(payload):
        if not isinstance(order, dict):
            raise ValueError(f"order at index {index} must be an object")
        if "amount" not in order:
            raise ValueError(f"order at index {index} is missing 'amount'")

        amount = order["amount"]
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise ValueError(f"order at index {index} has a non-numeric amount")
        if isinstance(amount, float) and not math.isfinite(amount):
            raise ValueError(f"order at index {index} has a non-finite amount")
        if amount < 0:
            raise ValueError(f"order at index {index} has a negative amount")

        total += amount

    return {"count": len(payload), "total": round(total, 2)}
```

## 5. Creator → Critic → Editor → Re-check

### Initial run

The first implementation was tested against seven cases. All seven passed. The independent Critic then identified two missing edge-case protections:

- **T09-F01 — Minor:** NaN and positive/negative Infinity were not explicitly rejected. These values can undermine meaningful numeric totals. **Correction:** use `math.isfinite()` for float inputs.
- **T09-F02 — Minor:** a non-object list entry did not have a dedicated test. **Correction:** add an explicit object-type validation case and test it.

### Editor changes

- Added finite-number validation for float values.
- Added a test for a non-object entry.
- Preserved the existing input checks and error messages.

### Re-check

The revised test suite was executed with Python's `unittest` runner.

Observed result:

- Tests run: **9**
- Failures: **0**
- Errors: **0**
- Runner result: **OK**

Cases: valid orders; empty list; non-list input; non-object entry; missing amount; non-numeric amount; Boolean amount; negative amount; NaN/Infinity.

The code and tests were executed in the Python user-visible execution environment. No claim is made about a separately installed local Python version or a command run on the user's computer.

## 6. Final audit

| Check | Result | Evidence / limitation |
|---|---|---|
| No specialist Skill invoked during implementation | PASS | Task implemented directly with general Python capability |
| No invented Skill/version/SHA | PASS | No such identifiers asserted as retrieved during execution |
| Input and edge-case validation | PASS | Nine automated tests |
| Actual test execution | PASS | 9 run, 0 failures, 0 errors |
| Critic findings corrected | PASS | Non-finite values and non-object entries covered |
| Regression re-check | PASS | Entire nine-test suite rerun successfully |
| Registry and Skill truly inaccessible to model | NOT VERIFIED | Prior Registry material remained in conversation context |
| Real GitHub outage | NOT VERIFIED | Only a deliberately invalid ref returned 404 |

## 7. Scoring and decision

### Artifact score — canonical CORE rubric

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

The score applies to the Python utility and its test coverage, not to proof of complete Registry outage resilience.

### Separate process-conformance result

**PARTIAL.** The fallback coding task and tests were completed without invoking a specialist Skill. However, the model's prior conversation context was not reset, so the stronger condition that Registry and Skill information be unavailable to the model was not established.

### T09 test decision

**BLOCKED — full isolation acceptance not proven.**

The concrete fallback artifact is usable and scored 96/100, but the T09 scenario cannot be marked PASS or PASS WITH NOTES as a fully isolated Registry/Skill-unavailable test until it is rerun in a fresh context or harness where the Registry and Skill contents are genuinely unavailable to the model. The controlled invalid-ref 404 must not be represented as a real repository outage.

## 8. Recommended next test

Repeat T09 in a fresh conversation or isolated evaluation harness with:
- no Registry or Skill contents injected into the prompt/context;
- network/repository retrieval disabled or deterministically fault-injected;
- the same concrete programming task;
- captured tool-call evidence showing retrieval attempts fail or are unavailable;
- the same acceptance criteria and regression tests.

Do not modify the Registry or any Skill to run this test.
