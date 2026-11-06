# Auto-Improvement Loop

## Procedure
1. Read the Critic's findings.
2. Convert each finding into a concrete, testable correction.
3. Prioritize Critical, then Major, then Minor.
4. Make the smallest change that resolves the issue.
5. Preserve correct content, voice, intent and constraints.
6. Re-run the relevant checks.
7. Compare against the previous version for regressions.
8. Re-score and decide: pass, revise again, or stop.

## Guardrails
- Do not add unsupported facts, citations, testimonials, guarantees or statistics.
- Do not remove required content to improve style or brevity.
- Do not change the user's intended meaning without explaining why.
- Do not claim a test or verification occurred unless it did.
- Re-check dependent sections after structural or factual changes.
- If a tool cannot perform the requested operation, provide the closest honest alternative.

## Iteration log
| Round | Main findings | Changes made | Re-check result | Score | Decision |
|---|---|---|---|---:|---|

Default maximum: 4 rounds. If still below threshold, return NOT PASS or BLOCKED with unresolved issues and the precise missing input or decision. No infinite loops.
