# AI-QC Skill Lifecycle and Versioning

## Principles
- GitHub is the canonical source of truth for skill files.
- Skills are modular: add, revise, deprecate or replace one module without rebuilding the system.
- Keep stable skill IDs and paths. Renames require a migration note.
- Every change must preserve shared CORE quality gates and document compatibility.

## Required skill structure
Every skill should define: name and description; version and status; purpose and scope; activation triggers and exclusions; required inputs; workflow; deliverable standards; critique checklist; evidence and safety rules; acceptance criteria; related skills; changelog.

## Versioning
Use semantic versioning per skill:
- MAJOR: incompatible scope, workflow or output-contract change.
- MINOR: backward-compatible capability addition.
- PATCH: clarification, correction or non-behavioral fix.

## Change workflow
1. Capture the requested change and its reason.
2. Fetch the current file before editing; never update from a stale copy.
3. Analyze impact on dependent skills, registry, router, CORE rules, tests and platform instructions.
4. Change only necessary files and preserve existing successful behavior.
5. Critique for ambiguity, conflicts, safety, omissions, compatibility and regressions.
6. Run relevant tests where tools permit; mark tests NOT RUN if not executed.
7. Re-check paths, versions, registry references and links.
8. Commit only when the user has authorized the repository update.
9. Report changed files, versions, commit result, actual tests and limitations.

## Add a skill
- Assign a unique kebab-case ID.
- Create SKILLS/<id>/SKILL.md.
- Add an active entry to REGISTRY/skills-registry.yml with concise triggers.
- Add representative tests under TESTS/.
- Update routing guidance only when necessary.
- Check overlap and define precedence with existing skills.

## Update a skill
- Preserve ID and path whenever possible.
- Increment version and append a changelog entry.
- Check all dependent references and tests.
- Do not overwrite a newer version using an old blob SHA.

## Deprecation
Prefer status deprecated with a migration note before deletion. Never remove a skill or its history without explicit approval.

## Runtime synchronization
A GitHub update does not automatically refresh content already loaded into a ChatGPT chat, Project, custom GPT or another runtime. The runtime must retrieve the latest file or have its local/project copy refreshed. If retrieval fails, disclose the version or snapshot actually used.
