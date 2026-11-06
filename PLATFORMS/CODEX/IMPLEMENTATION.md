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
