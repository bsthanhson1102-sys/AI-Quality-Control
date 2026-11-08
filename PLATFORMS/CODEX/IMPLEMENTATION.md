# GitHub / Codex Implementation

This repository is the canonical source for AI-QC skill text. A GitHub repository alone does not activate skills; the target runtime must retrieve or install them.

## Registry-driven architecture
- `REGISTRY/skills-registry.yml` lists stable skill IDs, paths, statuses and routing triggers.
- `CORE/skill-router.md` defines selection, multi-skill precedence and no-match behavior.
- `CORE/skill-lifecycle.md` defines how skills are added, updated, versioned and deprecated.
- `CORE/` contains shared quality rules that apply across specialist skills.

## Suggested project-local deployment
Copy active specialist skill folders to the Agent Skills directory supported by the target runtime. A common project-local convention is:

```text
.agents/
  skills/
    content-master/SKILL.md
    image-master/SKILL.md
    video-master/SKILL.md
    academic-master/SKILL.md
    research-master/SKILL.md
    coding-master/SKILL.md
```

Keep shared CORE guidance and the registry available as agent-level context or references. If the runtime does not automatically load referenced files, include the relevant shared rules in its instructions or skill files. Follow the target runtime's current official documentation; directory conventions may change.

## Adding a skill
1. Create `SKILLS/<new-id>/SKILL.md` using the skill structure in `CORE/skill-lifecycle.md`.
2. Add its ID, path, status and clear triggers to `REGISTRY/skills-registry.yml`.
3. Add representative routing and quality tests under `TESTS/`.
4. Review overlap and precedence with existing skills.
5. Verify the runtime discovers the skill after deployment.

## Updating a skill
1. Fetch the current repository version before editing.
2. Preserve the ID and path unless a migration is required.
3. Increment semantic version and append a changelog.
4. Review registry, router, dependent skills and tests.
5. Refresh the runtime's installed copy; GitHub updates do not automatically refresh local or previously loaded runtime context.

## Verification
- Confirm each active registry path exists.
- Confirm the runtime recognizes each skill name and description.
- Test representative scenarios from `TESTS/quality-gates.md` and `TESTS/registry-and-routing-tests.md`.
- Confirm Critic findings are specific and independent.
- Confirm Critical issues block delivery and the iteration limit is respected.
- Record runtime/version, commit or snapshot, test date and actual results.
- Mark tests NOT RUN if no runtime execution occurred.

## Version-pinned offline deployment (2026-11-08)
- The six domain specialists remain primary for ordinary single-domain work. The optional active `ai-qc-router` is for explicit AI-QC, multi-domain coordination and Full-risk review; it is **not** a universal auto-trigger.
- Source of truth remains `REGISTRY/skills-registry.yml` and `CORE/quality-control.md`. The pinned copy is `PLATFORMS/CODEX/references/registry-snapshot.yml` (registry blob SHA `93fe72a71a868644c106f05b99c5ca2538807c1a`, registry version 1.1.0). Snapshot is a fallback, not proof that GitHub is current.
- To deploy from a local checkout, run `python PLATFORMS/CODEX/scripts/deploy_skills.py /path/to/project` (on Windows, use a Windows project path). This verifies the registry blob and snapshot, copies active skills to `.agents/skills/<id>/SKILL.md`, and bundles `references/core-rubric.md` plus `references/registry-snapshot.yml` with each installed skill. No draft skills are deployed.
- This is **project-local**, not automatic global ChatGPT installation. Check runtime documentation for skill directories; `.user_skills/` is not assumed. Refresh the checkout and pin when updating; script refuses mismatched versions.
- A minimal global ChatGPT Custom Instruction can still request Light/Standard/Full classification and routing. GitHub updates do not install or activate skills in new ChatGPT tabs.

## Quality tiers and release evidence
- **Light:** concise accuracy/safety self-check, no elaborate audit transcript.
- **Standard:** Creator → Critic → Editor → Re-check → Final Auditor on the actual deliverable; do not accept generic feedback without verified corrections.
- **Full:** Standard plus a durable evidence ledger when supported and both domain and technical acceptance gates when relevant. A non-applicable gate is marked N/A with reason; a required but unexecuted gate is NOT RUN and blocks PASS.
- Canonical CORE remains unchanged: 25/20/15/15/10/10/5; threshold 90; at most four creation/revision rounds; zero unresolved Critical/Major; EVIDENCE COMPLETE + REGRESSION CLEAR + FINAL AUDIT APPROVED.
- Output is the artifact plus concise decision/limitations by default. Keep an auditable record in a real file where supported; do not present hidden reasoning as a persisted ledger.
- `verifier-hub`, `artifact-preview` and independent Workers are optional, runtime-dependent capabilities; verify actual availability and log execution before citing them as evidence. Role-separated passes in one model are not independent agents.

## Regression / deployment verification
1. Verify all active skill paths and versions and ensure the draft is excluded.
2. Check that offline deploy rejects registry drift and missing files.
3. Check that the runtime actually discovers specialist skills and router.
4. Test Light, Standard and Full tasks separately, including a deliberately weak service-marketing post; a self-awarded high score with unresolved Major must result in NOT PASS.
5. Test one missing-evidence case and one fourth-round unresolved Major case; both must block PASS.
6. Record which checks were actually executed; repository edits alone do not prove runtime integration or output quality.
