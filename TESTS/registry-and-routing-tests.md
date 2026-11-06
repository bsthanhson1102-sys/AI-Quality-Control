
# Registry and Skill Routing Acceptance Tests

## Registry integrity

- [ ] Every active registry entry points to an existing SKILL.md.
- [ ] Every skill ID is unique and stable.
- [ ] Registry version and status match each skill's frontmatter.
- [ ] Triggers are clear and do not conflict without documented precedence.
- [ ] Deprecated skills are not selected as primary skills unless migration is requested.
- [ ] Run python TOOLS/validate_registry.py; require a PASS result. If not run, record NOT RUN.
- [ ] Record the Registry file blob SHA and distinguish it from the repository commit SHA.

## Routing coverage

- [ ] Social advertisement selects content-master.
- [ ] Image generation or editing selects image-master.
- [ ] Video storyboard or editing selects video-master.
- [ ] Clinical assignment or report selects academic-master; add research-master when external evidence verification is needed.
- [ ] Current-facts comparison selects research-master.
- [ ] Debugging or code architecture selects coding-master.
- [ ] Unmatched task uses shared CORE rules without pretending a specialist skill exists.
- [ ] Cross-domain task selects one primary skill based on the final deliverable and only necessary secondary skills.
- [ ] If repository access fails, the runtime discloses the limitation and does not fabricate a version or SHA.

## Execution coverage

- [ ] Execute all six specialist scenarios in TESTS/skill-routing-test-suite.md.
- [ ] Retrieve the complete selected Skill before claiming to apply it.
- [ ] Record the actual selected skills, versions, statuses, paths and file blob SHAs.
- [ ] Critic findings identify the affected part, evidence/reason, impact, severity and correction.
- [ ] Editor records which findings were fixed and which remain.
- [ ] Final Auditor checks the final artifact against the original brief and mandatory gates.
- [ ] Report process conformance separately from artifact quality.
- [ ] Use the canonical rubric in CORE/quality-control.md; task-specific gates supplement rather than silently replace it.
- [ ] Distinguish Final Audit execution status from final artifact approval status.

## Lifecycle scenarios

- [ ] Adding a skill creates its file, registry entry and representative test.
- [ ] Updating a skill increments its version and records a changelog.
- [ ] Updating one skill does not silently alter unrelated skills.
- [ ] Deprecated skill has a migration note.
- [ ] Runtime synchronization limitations are disclosed.

## Quality gates and reporting

- [ ] Critical findings block PASS.
- [ ] Major defects are fixed before PASS.
- [ ] Full artifact score is at least 90/100 when scoring applies.
- [ ] PASS WITH NOTES is used only when all PASS conditions are met and remaining notes are non-blocking.
- [ ] BLOCKED is used when an unavailable prerequisite prevents responsible completion/release.
- [ ] NOT PASS is used when evaluated work fails a requirement or contains an unresolved defect.
- [ ] Maximum four improvement rounds are respected.
- [ ] Tests are reported only if actually executed; otherwise mark NOT RUN.
- [ ] A test specification or checklist is not represented as evidence that runtime testing passed.
