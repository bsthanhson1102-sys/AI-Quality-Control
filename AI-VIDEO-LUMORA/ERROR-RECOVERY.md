# Error Discovery, Root Cause, Fix and Re-test — v0.2.0

## Purpose
Make defect discovery proactive and repairs traceable, without pretending a documentation-only module can execute video edits or tests.

## 1. Error Hunter — detection
Review requirements, script, shot list, asset manifest, source footage when accessible, final output when accessible, copyright/consent, medical claims, audio/subtitle sync, render metadata and visual continuity. Never infer a defect's exact timecode from unseen video. Record a finding for each actionable issue.

## 2. Finding record
Use this minimum schema for every defect:
- `id`: stable identifier (e.g., V-F001)
- `severity`: Critical | Major | Minor | Enhancement
- `artifact`, `location`: file, shot, frame or timecode; `proposed` if uninspected
- `expected`, `observed`, `evidence`, `reproduction_steps`
- `root_cause`: VERIFIED | HYPOTHESIS | UNKNOWN, with rationale
- `owner`: Content | Director | Image | Editor | Audio | Render | Rights | Evidence
- `fix_plan`, `change_record`, `round`, `retest_result`, `regression_result`
- `status`: OPEN | FIXED_UNVERIFIED | VERIFIED_CLOSED | BLOCKED

## 3. Root Cause Analyzer
Reproduce before diagnosing when possible. Separate root cause from symptom. Identify which input, transform, asset, timing or policy rule produced the defect. If evidence is unavailable, label HYPOTHESIS/UNKNOWN rather than inventing causality.

## 4. Fix Owner
Correct the actual source artifact, not just the QC report. Apply minimal diff; preserve approved visuals, patient identity/consent, factual meaning and licensed assets. A missing permission or medical evidence cannot be "fixed" by rewriting its status as approved. Request legitimate evidence or remove unsafe material.

## 5. Re-test and regression
Re-run the failure check; compare before/after; check adjacent shots, captions, audio and safe areas, plus any affected rights/claims. Record actual command, tool/version, output path/hash and observation when available. If unable to execute, record NOT RUN and retain FIXED_UNVERIFIED or BLOCKED.

## 6. Stop rules
One shared maximum of four creation/revision rounds, counting initial draft as round 1. No Critical/Major may remain at PASS. Missing mandatory evidence blocks approval regardless of numeric score. Stop on verified PASS, BLOCKED, unsafe task or round limit. Report unresolved defects, do not hide them.

## 7. Learning loop
After Final Audit, cluster recurring failures, rank corrective system improvements by impact, frequency, implementation effort and safety. Add proposed test fixture and acceptance criteria. Roadmap is advisory and never changes canonical CORE/Skills automatically.

## Example — illustrative, not an executed test
Finding V-F001: subtitle is allegedly 0.8 s late. Status OPEN until actual playback/timecode evidence exists. If verified, owner Editor adjusts subtitle timeline and re-tests full affected segment plus neighboring captions. Close only with observed sync evidence. No simulated PASS.

## Root-cause-driven creative correction (v0.2.1)
An identified weakness is not an acceptable final finding by itself. Every issue must record: observed defect with frame/timecode or script beat; affected audience need or emotion; likely root cause; severity; proposed corrective edit; success criterion; post-edit inspection evidence; and regression impact. Creative defects include camera angles failing to convey audience concern, an unpersuasive opening, weak narrative stakes, unconvincing transformation, missing story payoff, pacing, lighting, sound design, and generic CTA. The fixer may replace the creative approach, shot list or hook—not merely tweak text. Judge compares before/after with the same rubric and must not claim higher retention or CTR without audience data. For medical aesthetics, AI-generated transformations cannot be represented as genuine patient before/after outcomes. After at most four total rounds, stop with NOT PASS if the mandatory quality gate is not met. Do not auto-publish. The user's only creative approval is the final deliverable; required permissions, paid expenditure and external publication remain separately authorized.

## Preventive Fix Engine: non-regression, measurable improvement and future-risk prevention (v0.2.2)
For every proposed repair, the Fixer MUST (1) inspect prior defect patterns and identify a causal mechanism, not just a symptom; (2) define a change-impact map covering hook, target pain point, narrative, continuity, face/anatomy, camera, lighting, typography, audio/music synchronization, platform compliance, and medical truthfulness; (3) define baseline measurements/observable evidence and an expected post-fix improvement before editing; (4) choose a repair that removes the causal mechanism, including redesigning the shot/story when necessary; (5) re-test the original failing case, related known failures, neighboring shots and full final render; (6) reject a fix that reintroduces an old Critical/Major issue or causes an unacceptable regression; (7) add a future-facing regression fixture, guardrail or preflight check for any newly identified failure mode; and (8) record residual risks and whether the prevention was actually tested. Use a simple risk priority of severity × likelihood × detectability difficulty to prioritize proactive checks, not to assert certainty about future defects. An improvement is VERIFIED only with observed evidence (e.g., legibility, continuity, synchronization, comparative rubric), not a guessed uplift in CTR or retention. Preventive controls are PROPOSED until implemented and tested. Preserve the overall four-round cap and release thresholds. Never claim absolute perfection or elimination of all future errors.
