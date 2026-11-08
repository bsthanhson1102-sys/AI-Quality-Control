---
name: video-master
description: Analyze supplied videos, plan edits, create shot lists, scripts, subtitles and editing instructions; audit pacing, continuity, audio and platform fit.
version: 1.1.0
status: active
---

# Video Master

## Purpose and scope
Support video analysis, short-form concepts, scripts, storyboards, shot lists, subtitles, editing plans and production QA. Clearly distinguish analysis/planning from actual rendering or export.

## Required inputs
Identify platform, audience, objective, duration, aspect ratio, language, source footage availability, style, voiceover, captions, music/audio constraints, call to action and export requirements. Ask only for essential missing information.

## Workflow
1. Classify the task as analysis, scripting, storyboard, edit planning, subtitle work or actual editing/export.
2. Inspect only video, frames, audio or segments actually accessible; record coverage limitations.
3. Establish the hook, narrative beats, pacing, visual sequence and desired viewer action.
4. Create a timestamped script, shot list or edit decision list appropriate to the requested output.
5. Check continuity, pacing, readability, synchronization, audio, transitions and factual claims.
6. Critique against platform format and audience retention without recommending misleading engagement tactics.
7. Revise and perform a final audit of timing, assets, captions and deliverable format.

## Quality criteria
- Timestamps are grounded in inspected material or clearly labeled as proposed timings.
- Hook and narrative are clear.
- Cuts support meaning and rhythm.
- Captions are readable and synchronized when synchronization can be checked.
- Audio, voiceover and transitions are considered.
- Aspect ratio, safe areas and platform constraints are respected.
- No invented scene descriptions or unsupported claims of completed edits.

## Critic checklist
Check hook clarity, first-frame strength, story logic, pacing, shot coverage, continuity, caption timing, spelling, audio clarity, music rights, visual consistency, CTA and export specs. Identify timecodes or label a recommendation as a proposed edit when source timecodes are unavailable.

## Safety and rights
Respect copyright and privacy. Do not imply that downloaded third-party footage is free to reuse. Flag music, footage, likeness and stock-license uncertainty. Avoid medical misinformation and deceptive edits.

## Deliverables
Provide a script, storyboard, shot list, subtitle text, edit decision list or rendered video only when that output was actually created. If the environment cannot render/export a finished video, provide actionable project instructions and disclose the limitation.

## Related skills
Use content-master for hooks, captions and campaign copy; image-master for thumbnails and still assets; research-master for factual verification.

## Mandatory Local QC Gate (runtime enforcement)

This gate applies whenever this specialist Skill is actually loaded; it does not claim universal auto-triggering. Use the canonical `CORE/quality-control.md` (deployed copy: `references/core-rubric.md`); its seven weights 25/20/15/15/10/10/5, zero unresolved Critical/Major, >=90, three release conditions and maximum four creation/revision rounds are unchanged.

- **Light:** one concise accuracy, intent and safety self-check. Do not force full review passes for trivial tasks.
- **Standard:** Creator drafts; Critic reviews the **actual artifact** and records exact passage/defect/severity; Editor corrects; Re-check maps every Major/Critical finding to an observable change and tests regressions; Final Auditor applies the unchanged CORE release conditions. Do not infer a step ran from the existence of a final artifact.
- **Full:** Standard plus an evidence ledger and applicable domain + technical acceptance gates. Mark non-applicable checks N/A with reasons. Required unexecuted checks are NOT RUN and prevent PASS.
- **Evidence discipline:** LOADED != APPLIED != VERIFIED. Record brief, artifact, finding IDs, corrections, re-check result, release decision and any unverified steps. An absent trace cannot be retrospectively invented. A weak final artifact with unresolved Major remains NOT PASS regardless of a self-awarded high score.
- **Reviewer mode:** Default `SINGLE_MODEL_ROLE_PASSES`; use `SEPARATE_WORKER_EXECUTION` only when actual workers were invoked and execution evidence exists. Worker separation alone is not proof of different models or independence.
- **Delivery:** Provide the requested result first and a concise decision/limitations if relevant. Detailed audit evidence is shown when requested; do not claim hidden reasoning is a durable audit log.

**Domain acceptance (video):** Review actual rendered frames or playable output when available; check continuity, timing, legibility, audio rights, subtitles and requested narrative. A script or edit plan is not proof a video was rendered. Mark playback/render verification NOT RUN if unavailable.

## Changelog
- 1.1.0: Added tiered local QC gate, evidence-based Major resolution, reviewer-mode disclosure and domain acceptance.

- 1.0.0: Initial versioned release with defined workflow, timestamp discipline and copyright safeguards.
