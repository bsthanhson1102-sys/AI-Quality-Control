# QC and release gate

Canonical authority: `../CORE/quality-control.md`; this file adds **video-specific checks** without changing CORE weights or thresholds.

## Gate A — Script / pre-production
- Objective, audience, brand and platform fit; distinctive hook and real payoff.
- Clear beginning, narrative beats, CTA where appropriate; shot list feasible.
- Medical/aesthetic claims backed by evidence when necessary; no safety promises, misleading before/after imagery or fabricated patient results.
- Consent/privacy and rights for patients, faces, footage, voice and music.
- Proposed timestamps clearly marked; no false claims of having inspected unavailable source footage.

## Gate B — Rendered output
- File opens, actual duration, dimensions, ratio, codec and audio track checked when tools permit.
- Inspect actual frames for continuity, image quality, text safe areas and legibility.
- Inspect/listen for subtitle sync, audio balance, music rights and voice clarity.
- Compare final video with approved script, source footage and user brief.
- Any unavailable render or playback check is NOT RUN, not PASS.

## Review evidence
Record: task ID, brief, Skill versions/SHA, role-execution mode, candidate, finding ID and severity, corrected artifact, re-check result, evidence ledger, technical gate, domain gate, CORE rubric result, Final Auditor decision.

**Release rule:** >=90/100 under 25/20/15/15/10/10/5, no unresolved Critical/Major, evidence complete, regression clear, Final Auditor approval, max 4 rounds total. When evidence is insufficient report UNVERIFIED / NOT PASS / BLOCKED accurately. No auto-publication.
