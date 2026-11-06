# GitHub / Codex Implementation

This repository is the source of truth for skill text. A GitHub repository alone does not activate skills.

## Suggested project-local deployment

Copy specialist skill folders to the Agent Skills directory supported by the target runtime. A common project-local convention is:

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

Keep CORE guidance available as shared reference. If the runtime does not automatically load referenced files, include relevant core rules in agent-level instructions or the skill itself.

## Verification
- Confirm the runtime recognizes each skill name and description.
- Test each skill using representative scenarios from TESTS/quality-gates.md.
- Confirm Critic behavior is specific and genuinely independent.
- Confirm Critical issues block delivery.
- Confirm the iteration limit is respected.
- Record runtime/version and test date in release notes.

Follow the target runtime's current official documentation; conventions may change.
