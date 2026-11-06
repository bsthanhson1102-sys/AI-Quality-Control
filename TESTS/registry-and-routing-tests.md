# Registry and Skill Routing Acceptance Tests

## Registry integrity
- [ ] Every active registry entry points to an existing SKILL.md.
- [ ] Every skill ID is unique and stable.
- [ ] Registry version and status match each skill's frontmatter.
- [ ] Triggers are clear and do not conflict without documented precedence.
- [ ] Deprecated skills are not selected as primary skills unless migration is requested.
- [ ] Run `python TOOLS/validate_registry.py`; require a PASS result.

## Routing scenarios
- [ ] Social advertisement selects content-master.
- [ ] Image generation or editing selects image-master.
- [ ] Video storyboard or editing selects video-master.
- [ ] Clinical assignment or report selects academic-master; add research-master when evidence verification is needed.
- [ ] Current-facts comparison selects research-master.
- [ ] Debugging or code architecture selects coding-master.
- [ ] Unmatched task uses shared CORE rules without pretending a specialist skill exists.
- [ ] Cross-domain task selects one primary skill and only necessary secondary skills.

## Lifecycle scenarios
- [ ] Adding a skill creates its file, registry entry and representative test.
- [ ] Updating a skill increments its version and records a changelog.
- [ ] Updating one skill does not silently alter unrelated skills.
- [ ] Deprecated skill has a migration note.
- [ ] Runtime synchronization limitations are disclosed.

## Quality gates
- [ ] Critic findings identify affected part, defect, impact and correction.
- [ ] Critical findings block PASS.
- [ ] Full rubric threshold is at least 90/100 when appropriate.
- [ ] Maximum four improvement rounds are respected.
- [ ] Tests are reported only if actually executed; otherwise mark NOT RUN.
