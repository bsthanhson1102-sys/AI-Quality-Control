# AI-VIDEO-LUMORA production, repair and improvement workflow — v0.2.0

1. **Intake and criteria:** identify audience, platform, objective, duration, aspect ratio, language, brand, source footage, consent, music/footage rights and exact output. Classify Light/Standard/Full.
2. **Preflight:** read latest Registry, CORE and selected active Skills; record actual version/blob SHA and SELECTED/LOADED status. Define evidence and technical/domain acceptance criteria.
3. **Creative proposals:** develop distinct content angles and visual concepts where appropriate; no mandatory secondary Skill when it adds no value. Distinguish proposed from inspected timecodes.
4. **Creative Judge:** select on relevance, truthfulness, feasibility, safety, originality and platform fit. Single-model perspectives are not independent agents.
5. **Director package:** structured script, timestamps, storyboard, shot list, VO/captions, asset manifest, rights/consent status, edit decision list and CTA as applicable.
6. **Pre-production QC:** Critic finds precise defects; Editor fixes; Re-check inspects changes and regressions. Record each revision against one shared round counter.
7. **Production (conditional):** edit/render only when supported tools, rights and footage are available; otherwise deliver a plan and mark render NOT RUN.
8. **Post-production QC:** inspect real frames/audio when available; check continuity, subtitle timing, legibility, aspect ratio, audio and export properties.
9. **Error Discovery:** proactively review pre-production and output evidence; Error Hunter records actionable finding IDs with severity, location/timecode, impact, evidence and reproducible steps. See ERROR-RECOVERY.md.
10. **Root Cause:** distinguish script, source asset, image generation, timeline, audio, render settings, permission or evidence gap; identify owning component without guessing.
11. **Targeted Fix:** repair only affected component, preserve known-good behavior; no silent safety/medical-claim changes or invented rights.
12. **Re-test and Regression:** check original failure, neighboring shots/captions, source-to-output fidelity, domain and technical gates. Missing tools => NOT RUN, never PASS. Stop at four creation/revision rounds including first, or earlier on BLOCKED/PASS.
13. **Final Auditor:** apply canonical 25/20/15/15/10/10/5, >=90, zero Critical/Major, evidence complete, regression clear, technical/domain acceptance and actual test records. Report PASS / PASS WITH NOTES / NOT PASS / BLOCKED.
14. **Continuous Improvement:** AFTER audit, analyze recurrence, root causes, effort and impact; propose ranked changes with owner, acceptance criteria and test plan in ROADMAP.md. This stage cannot override a failed release gate. No automatic CORE/Skill modifications.
15. **Handover and publishing:** deliver actual artifact and QC evidence; never auto-publish without approval.

## Shared round counter
Initial artifact = round 1. Every material re-generation/revision increments by one; pre-production and post-production repair share the same maximum of 4. Pure inspection and proposed roadmap items do not consume a round. No reset by switching role or gate.

## Artifact examples
Concept/script/shot list/SRT/edit plan can be delivered without rendering. MP4 is delivered only if actually produced and verified; script acceptance and MP4 acceptance are separate decisions.

## Autonomous internal approval; single user-facing decision (v0.2.1 policy)
For a user-authorized creative deliverable, the Producer may decide internally on creative direction, script, image selection, typography, editing, audio and technical presets without requesting approval at each step. The AI-QC Judge reviews the actual output, routes concrete findings to Editor, and Final Auditor reviews the corrected artifact. Only deliver the finished candidate to the user with one decision: ACCEPT or REJECT. Do not ask for preference approval on substeps unless essential source rights, irreversible publication, paid credits, patient consent or other legally necessary authorization is missing. Internal role passes are not independent AI agents unless independently executed and evidenced. User acceptance never overrides medical accuracy, rights or mandatory gates. A rendered file that fails QC must be reported as NOT PASS rather than disguised as final. Do not auto-post.
