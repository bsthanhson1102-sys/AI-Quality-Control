---
name: ai-qc-router
description: Coordinate AI-QC for explicitly requested AI-QC audits, cross-domain deliverables and high-stakes Full reviews; specialist skills handle routine single-domain work.
version: 1.0.0
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
