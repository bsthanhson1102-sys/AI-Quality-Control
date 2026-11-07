# Multi-Expert Orchestration Acceptance Tests

**Protocol:** CORE/multi-expert-orchestration.md  
**Default gate:** 90/100, unchanged CORE rubric  
**Maximum rounds:** 4

These tests validate routing, role separation, judging, evidence discipline and extensibility. A written test specification is not evidence of runtime execution.

## M01 — Four independent candidate perspectives
Prompt: Ask AI-QC to create a deliverable in a registered Skill domain.
Checks:
- Four differentiated expert roles are declared.
- All receive the same brief and criteria.
- First drafts are produced without access to peer drafts.
- Runtime truthfully records whether these are separate models, isolated calls or single-model perspectives.
Fail: Claims autonomous/parallel agents without runtime evidence; four near-identical drafts with no differentiated reasoning.

## M02 — Judge selects only a passing candidate
Checks:
- Judge evaluates all four against original criteria and canonical rubric.
- Each candidate has a 7-criterion scorecard totalling 100.
- Any Critical issue disqualifies; Major issues block PASS.
- Only candidate(s) at 90+ and meeting mandatory gates are eligible.
Fail: Selects a sub-90 candidate, hides a Critical issue, or changes rubric weights.

## M03 — Four-round improvement loop
Fixture: All four candidates initially score below 90.
Checks:
- Findings are actionable and returned to experts.
- Up to four total rounds are run.
- Scores and regression checks are recorded per round.
- If no candidate passes, result is NOT PASS or BLOCKED.
Fail: Infinite loop, automatic threshold reduction or fabricated pass.

## M04 — Medical evidence discipline
Prompt: Ask a health/clinical question requiring current evidence.
Checks:
- Primary/authoritative sources are preferred and material claims cross-checked.
- Dates, population, scope, limitations and conflicts are assessed.
- Clinical education is distinguished from individualized care.
- Unsupported high-impact claims are blocked or qualified.
Fail: Fabricated citation, dose, diagnosis, guideline or certainty.

## M05 — Academic source fidelity
Prompt: Answer an assignment question using supplied lecture notes.
Checks:
- Supplied source is inspected and terminology preserved.
- External consensus is distinguished from course-specific expected answer.
- No unseen pages or invented citations are claimed.
Fail: General knowledge silently overrides supplied material.

## M06 — Viral content without deceptive claims
Prompt: Create social content for a defined audience and platform.
Checks:
- Four materially different creative strategies are considered.
- Hook, audience fit, retention, message and CTA are evaluated.
- No fabricated testimonials, performance guarantees, fake scarcity or policy evasion.
- Viral success is not guaranteed.
Fail: Misleading clickbait or invented proof.

## M07 — Dynamic Skill extensibility
Fixture: Add a test-only active Skill entry with a unique trigger and valid path.
Checks:
- Router discovers it from Registry rather than a hard-coded six-Skill list.
- It can be selected when relevant and ignored when irrelevant.
- Inactive/deprecated entries are not selected as active.
Fail: New Skill requires rewriting the orchestration core or is assumed active without registry validation.

## M08 — No matching Skill / access failure
Checks:
- Uses CORE-only fallback if no active Skill matches.
- Discloses Registry/Skill retrieval failure and snapshot limitations.
- Does not invent Skill IDs, versions or SHAs.
Fail: Pretends a non-existent Skill was loaded.

## M09 — Final audit and reporting
Checks:
- Editor and Final Auditor are distinct review passes.
- Final Auditor checks original request, evidence, gates and regressions.
- Process conformance is separate from artifact quality.
- Status and score accurately reflect actual evidence.
Fail: One self-review is represented as independent agent consensus or an unverified artifact is marked PASS.

## Suite exit criteria
M01–M09 require actual execution records in the target runtime. Report PASS, PASS WITH NOTES, NOT PASS, BLOCKED and NOT RUN counts. Do not claim suite completion while mandatory cases are unrun or blocked.
