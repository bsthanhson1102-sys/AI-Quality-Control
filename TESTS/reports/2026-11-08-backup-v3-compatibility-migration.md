# Backup v3 vs canonical AI-QC — compatibility audit (2026-11-08)

## Scope and source
User supplied `ai-qc-skills-backup-v3.zip` (7 Skill folders, 21 ZIP entries) and standalone `SKILL.md` for coding-master. Compared with current GitHub `SKILLS/*/SKILL.md`, Registry and CORE. Backup quick validator was actually run against all 7 directories: 7/7 `Skill is valid!`. This validates frontmatter format only, not runtime behavior or quality.

## Per-skill decision
| Skill | Backup strength | Canonical strength | Decision |
| --- | --- | --- | --- |
| ai-qc-router | Detailed runtime modes, snapshot refresh and smoke tests | Current registry/CORE routing and truthful role-pass limits | PORT selective runtime compatibility; no Organizer/Worker claims without tool evidence |
| content-master | Content QC structure, practical channel-specific rules | Newer service-marketing intent routing, pre-delivery editorial gate, T10 negative fixtures | KEEP canonical; do not replace with older backup |
| image-master | Detailed preflight and visual production steps | Source-fidelity safeguards, conditional medical image checks, domain gate | KEEP canonical; consider backup only for optional visual checklist |
| video-master | Rich workflow and timing/continuity checklist | Rendering-vs-plan distinction, copyright and actual playback acceptance | KEEP canonical; optional production checklist only |
| academic-master | Structured evidence ledger and academic formatting | Medical image-answer verification and CORE release gate | KEEP canonical; backup cannot supersede safety gates |
| research-master | Evidence and contradiction checklist | Source-grounded claims, recency and evidence traceability | KEEP canonical; optional source-quality rubric only |
| coding-master | Detailed security/QA checklist, optional native skills | Current repository guardrails and tested-code truthfulness | KEEP canonical; import checklists only when tools exist |

## Critic findings
- MAJOR: Backup router pinned to registry 1.1.0 and hard-coded `/home/user/.dola/` paths; not portable to generic ChatGPT.
- MAJOR: Worker references are conditional; copying them as operational facts would falsely imply independent models.
- MAJOR: No direct invocation of T10 `release_gate.py` by specialist Skills; installing Skill text does not enforce automatic pre-delivery checks.
- MAJOR: Replacing canonical content-master would risk losing T10 fixtures and current intent-routing safeguards.
- MINOR: Backup `quick_validate.py` requires PyYAML and only validates frontmatter; not a substitute for actual tests.

## Editor changes
- Updated canonical `SKILLS/ai-qc-router/SKILL.md` to 1.1.0 with cross-runtime capability check, conditional T10 gate invocation, migration safeguards and explicit runtime limitations.
- Updated Registry to 1.4.0; synchronized offline snapshot and deploy script pin.
- Deliberately did not overwrite six active specialist Skills or CORE.

## Verification
- VERIFIED: Backup quick validator executed for all seven Skills, 7/7 success (frontmatter-only).
- VERIFIED: GitHub commits and readback for router, Registry, snapshot and deploy pin.
- NOT RUN: End-to-end ChatGPT new-tab automatic gate invocation.
- NOT RUN: Independent Organizer/Worker execution.
- NOT RUN: Full deployment in target user's environment.
- NOT RUN: Repository Python tests against this new router revision (T10 GitHub Actions previously 17/17 on earlier commit only).

## Release decision
Compatibility migration PARTIAL / NOT PASS for full runtime auto-enforcement. Source synchronization and router documentation integration verified. The runtime enforcement gap is not fixed by these text changes. Canonical CORE weights 25/20/15/15/10/10/5, >=90 threshold, four-round limit and no unresolved Critical/Major preserved.
