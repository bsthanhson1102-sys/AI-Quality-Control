# AI-QC — Repository Instructions for Codex and Coding Agents

## Mission and scope
Maintain and extend this repository as the source of truth for AI-QC and its AI-EDIT/video/content workflows. The user states the desired outcome in natural language; select relevant active Skills automatically. These instructions apply to work **inside this repository** and do not override higher-priority platform or user instructions.

## Read before substantial changes
1. Inspect `REGISTRY/skills-registry.yml`, `CORE/quality-control.md`, and relevant active `SKILLS/<skill-id>/SKILL.md` from the **current checkout/branch**. For cross-domain tasks, select only necessary secondary Skills.
2. Check `CORE/skill-router.md` where routing is relevant; inspect existing code, tests, and adapters before creating new ones.
3. Treat the current repository as authoritative; never substitute remembered versions, SHAs, or cached descriptions for files actually inspected.
4. If files are unavailable, disclose the limitation and do not claim to have loaded or applied a Skill.

## Execution standards
- Classify work as Light, Standard, or Full based on complexity and risk.
- For substantial work use role-separated Creator → Critic → Editor → Re-check → Final Auditor passes. These are **not** independent AI agents unless separate executions are demonstrated.
- Preserve existing behavior; favor small, reversible, focused changes. Investigate root causes before fixes and add targeted regression tests.
- For new Skills, check for duplicate scope and conflicts; use Registry for discovery, CORE for universal QC, SKILL.md for domain procedures, and adapters for tool-specific implementation. Do not require users to name Skills.
- Video and content tasks may combine active content-master, video-master, image-master, research-master, and coding-master as needed. Camera vocabulary is tool-neutral; verify actual tool capabilities and do not equate 2D zoom with genuine 3D camera motion.
- Do not automatically activate draft Skills. Do not modify canonical CORE, promote drafts, or change unrelated files without explicit authorization.

## Quality and evidence
- Follow the **current** CORE, including its seven weights `25/20/15/15/10/10/5`, minimum score `90/100`, zero unresolved Critical/Major findings, sufficient evidence, passing regression checks, and Final Auditor approval.
- At most **four** creation/improvement rounds total, including the first attempt. Stop with NOT PASS, BLOCKED, or UNVERIFIED where appropriate.
- Distinguish SELECTED, LOADED, APPLIED, and VERIFIED. A written plan, mock, passing synthetic fixture, or unexecuted test is not proof of a deployed integration or a finished video.
- Run available tests and report **exact commands, results, and limits**. Never invent execution, evidence, versions, independent agents, QC scores, or artifacts.

## Permissions and safety
- No purchases, credit usage, new subscriptions, publishing, deployment, credential exposure, or expanded permissions without explicit approval.
- Do not assume unattended/background execution or GUI control without an actual configured runtime.
- Respect patient privacy, consent, licensed media, accurate medical claims, and truthful representation of synthetic imagery.
- Do not overwrite unrelated user work or commit secrets.

## Delivery
Provide the requested deliverable first. Summarize changed paths, tests actually executed, remaining blockers, and evidence-backed status concisely. If an authorized persistent change is made, read back the committed file to verify its contents.
