# AI-VIDEO-LUMORA QC gates — v0.2.0

Canonical authority: `../CORE/quality-control.md`. This supplement cannot lower or bypass CORE gates.

## Gate A — script and pre-production
Check goal/audience/platform, hook and payoff, feasible scenes and timings, brand, claims and factual evidence, patient consent/privacy, likeness and media rights. Distinguish planned from inspected footage.

## Gate B — rendered video (only if actually produced)
Verify actual file opening, duration, dimensions, codec, audio tracks, inspected frames, temporal continuity, readable captions/safe areas, subtitle sync, audio balance, rights and comparison with approved script. If absent, mark required checks NOT RUN and do not claim MP4 PASS.

## Gate C — error recovery and regression
Error Hunter records `finding_id, severity, affected_artifact, location_or_timecode, observed, expected, evidence, reproduction, owner, root_cause, fix, round, recheck, regression, status`. Every Critical/Major requires correction and observable re-test evidence. Re-test the originally failed case AND adjacent unaffected segments. Track a single four-round cap across all gates. A failed repair cannot be closed by a roadmap proposal.

## Gate D — development roadmap (post-audit only)
For recurring or costly defects, propose improvement with rationale, priority, effort, risk, measurable acceptance and regression fixture. Do not treat proposed features as implemented. Never change CORE or canonical Skills without separate authorization.

## Release decision
Technical and domain gates separately PASS / NOT PASS / BLOCKED / NOT RUN. Apply CORE 25/20/15/15/10/10/5, >=90, no unresolved Critical/Major, EVIDENCE COMPLETE, REGRESSION CLEAR and FINAL AUDIT APPROVED. Missing required tool/source => BLOCKED; failed mandatory gate/score => NOT PASS. Document both process conformance and artifact quality. Never claim independent agents or executed tests from prose alone.
