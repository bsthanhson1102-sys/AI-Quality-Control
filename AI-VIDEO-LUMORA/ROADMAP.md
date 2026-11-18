# Development roadmap — AI-VIDEO-LUMORA

Status: PROPOSED. No roadmap item is implemented or tested merely by appearing here.

## P0 — v0.2 documentation and defect protocol
Deliverables: documented Error Hunter -> Root Cause -> targeted Fix -> Re-test -> Final Audit -> Development Strategist; common four-round counter; stable finding record; test scenarios. Acceptance: files present/readable and consistent with CORE; review and read-back. Documentation-only release is not a runtime PASS.

## P1 — executable orchestration
Implement task state machine, Skill router reading current Registry, per-role input/output contracts (JSON schema), asset manifest, permissions/evidence ledger, durable defect ledger and shared revision counter. Acceptance: run routing/transition tests with captured outputs, reject invalid handoffs, stop on 4 rounds. Security: least-privilege tools and approval for external writes.

## P2 — editing pipeline
On Windows/Codex, evaluate locally available FFmpeg/ffprobe or a supported editing adapter. Implement subtitle timing, deterministic render presets, safe-area checks and audio pipeline only after environment inspection. Acceptance: render a permitted fixture MP4, inspect actual metadata, sample frames and audio, and preserve source-to-output traceability. Do not assume tools are installed.

## P3 — visual/audio quality automation
Add measured sync/black-frame/silence checks with documented thresholds; human/vision review for factual and patient-identity fidelity, consent and medical claims. Acceptance: known-good and intentionally broken media fixtures, false-positive/false-negative record, rollback.

## P4 — brand and operational scale
Add opt-in Lumora Brand Profile, brand templates, multilingual captions, asset license/consent register, export variants, metrics and optional publication approval flow. Acceptance: approved brand references, no fabricated clinic claims, audit logs and controlled publishing.

## Prioritization rule
Critical safety/privacy/rights defects first; then repeatable Major technical defects; then productivity enhancements. Each proposed change requires owner, scope, success metric, regression test and rollback plan. Do not change CORE, Registry or canonical Skills without separately justified authorization.

## Current known gaps
No verified autonomous multi-agent runtime, no verified renderer, no actual MP4 production, no end-to-end video QC execution, no empirical performance data. These gaps cannot be erased by self-scoring.
