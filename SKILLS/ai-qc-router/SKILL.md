---
name: ai-qc-router
description: Coordinate AI-QC for explicitly requested AI-QC audits, cross-domain deliverables and high-stakes Full reviews; specialist skills handle routine single-domain work.
version: 1.1.0
status: active
---

# AI-QC Router (thin orchestration skill)

## Trigger
Use for explicitly requested AI-QC reviews, multi-domain tasks requiring coordination, or Full-risk work. Do **not** rely on this skill to auto-trigger on every chat message. The host runtime's global instructions or agent configuration must implement universal routing.

## Select and execute
1. Classify Light / Standard / Full by task, not keywords alone. Light: brief self-check; Standard: Creator -> Critic -> Editor -> Re-check -> Final Auditor; Full: same passes plus evidence ledger, technical acceptance and domain acceptance when applicable.
2. Route to the minimum active specialist skills in REGISTRY; identify primary owner and only materially necessary secondary skills. Never treat a draft skill as active.
3. Read the installed version of the selected skill and shared CORE/quality-control.md (deployment reference: references/core-rubric.md). Record source and version. If reference unavailable, disclose it and do not claim a CORE-compliant PASS.
4. For substantive deliverables, compare actual output against the original objective. Critic must cite specific defects, Editor must fix them, Re-check must inspect the revised artifact, and Final Auditor must independently reconsider release gates. Maximum four creation/revision rounds.
5. Use the canonical seven weights 25/20/15/15/10/10/5, zero unresolved Critical/Major, >=90, and all three release conditions (evidence complete, regression clear, final audit approved). Do not invent scores, verification, external workers or source retrieval.
6. Technical validators and artifact previews are optional integrations: use only when installed, relevant, and actually executed; record NOT RUN otherwise. For Full tasks, missing *required* validation prevents approval.
7. Keep a concise evidence record in an actual file if the runtime supports it, otherwise record observable checks in the final report when requested. Never imply hidden reasoning is a durable audit artifact.
8. Return the requested deliverable first. Show only decision state and material limitations by default; show detailed audit evidence when explicitly requested.

## Source and offline deployment
GitHub is canonical for updates; a pinned, verified registry snapshot is a runtime fallback, **not** evidence of the latest upstream state. Record registry blob SHA and snapshot date. On updates refresh snapshots and check active paths and versions; never silently mix revisions. See PLATFORMS/CODEX/IMPLEMENTATION.md.

## Mode disclosure
Default: role-separated passes in one assistant. Describe separate Organizer/Workers as independent only if the runtime actually ran them and the evidence is available.

## Cross-runtime compatibility and T10 integration (v1.1.0)

A third-party/backup skill bundle may describe Organizer/Workers, absolute paths under `/home/user/.dola/`, and native tools unavailable in the current host. These are **optional environment-specific implementations**, not mandatory prerequisites and not evidence that independent agents ran. For every task, discover the actual runtime capabilities first; default to `SINGLE_MODEL_ROLE_PASSES` and mark unavailable workers/tools NOT RUN. Never substitute a pinned old registry for a verified current Registry without disclosure.

For service-marketing tasks, use active `content-master` and its editorial acceptance criteria. If a tool-enabled execution environment can run repository Python, optionally execute `TESTS/t10/content_gate.py` as a negative-control preflight and `TESTS/t10/release_gate.py` on an actual JSON evidence ledger. **Neither is automatically invoked merely by reading this Skill**. The release-gate outcome `SCHEMA_ACCEPTED_REVIEW_REQUIRED` is not PASS: a separate content/domain review and the canonical CORE Release Gate remain mandatory. Record command, exit status, test output and artifact hash where available; otherwise mark NOT RUN.

A real automatic publication block requires an explicit runtime/orchestrator hook that invokes the gate and respects its exit status. ChatGPT conversations without that hook cannot be claimed to have executable pre-release enforcement. Do not claim a new-chat regression PASS without observing the new chat's actual behavior and evidence.

**Migration policy:** treat bundled ZIP Skills as reference material. Preserve the canonical `CORE/quality-control.md`, current active specialist Skills, registry status/version and T10 fixtures. Only port compatible incremental improvements after source comparison, regression checks and versioned changes; never overwrite the live Skill tree with an old snapshot.

## Changelog
- 1.1.0: Added portable runtime capability checks, safe ZIP migration policy and explicit T10 gate integration boundaries.
