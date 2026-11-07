
# AI Quality Control (AI-QC)

A modular multi-skill quality system for skill routing, independent critique, evidence-aware improvement and final quality assurance. The repository is the canonical, version-controlled source for specialist skills and shared protocols.

## Mission

Deliver work that is accurate, useful, safe, complete enough for the brief and honestly represented. The creator must not be the sole judge of their own work.

## Standard workflow

Intake → Criteria → Create → Independent Critique → Improve → Re-check → Final Audit → Deliver

## Four review roles

- **Creator:** creates against the brief.
- **Critic:** independently identifies errors and weaknesses.
- **Editor:** fixes prioritized defects while preserving successful work.
- **Final Auditor:** checks the finished result against the original request.

These are distinct review passes, not automatically separate autonomous agents or models.

## Quality gate

Default artifact score: **90/100**, using the canonical rubric in CORE/quality-control.md. Any unresolved Critical issue blocks approval. Default maximum: **4 improvement rounds**. If work cannot pass, disclose unresolved issues and use NOT PASS or BLOCKED accurately.

## Process and artifact are evaluated separately

AI-QC reports must distinguish:
- **Process conformance:** whether routing, retrieval, review passes, editing, re-check and evidence reporting actually occurred.
- **Artifact quality:** whether the resulting work meets its brief and mandatory gates.

Do not combine these into one ambiguous score. Do not score an artifact that was not produced.

## Repository map

- CORE/: shared QC protocol, critique, improvement, final audit, skill router, lifecycle policy and four-expert orchestration.
- REGISTRY/skills-registry.yml: central catalogue of skill IDs, versions, paths, status and routing triggers.
- SKILLS/: six modular specialist skills (Content, Image, Video, Academic, Research and Coding).
- PLATFORMS/CHATGPT/: global core instructions, master instructions and installation guidance.
- PLATFORMS/CODEX/: deployment guidance for Codex-compatible agent environments.
- TESTS/: quality gates, registry/routing checks, the nine-case skill routing/execution regression suite and multi-expert orchestration acceptance tests. TESTS/reports/: dated records of actual test runs and their evidence.
- TOOLS/validate_registry.py: standard-library validator for registry paths and skill metadata.
- .github/workflows/validate-ai-qc.yml: runs registry validation on pushes and pull requests to main.

## Multi-expert execution\n\nFor substantial tasks, CORE/multi-expert-orchestration.md defines four differentiated expert perspectives, an independent Judge, a maximum four-round improvement loop and a final audit. The runtime must disclose whether these perspectives are separate models, isolated calls or single-model role-separated passes. TESTS/multi-expert-orchestration-tests.md defines the required acceptance tests; the specification itself is not proof of runtime execution.\n\n## Add or update a skill

Follow CORE/skill-lifecycle.md. Add a new SKILLS/<skill-id>/SKILL.md, register it in REGISTRY/skills-registry.yml, add representative tests, and review routing/dependencies. For updates, fetch the latest file first, increment its version, append a changelog and verify dependent references. Prefer deprecation with a migration note over immediate deletion.

## Test the system

1. Run python TOOLS/validate_registry.py to check Registry structure and Skill metadata.
2. Execute the cases in TESTS/skill-routing-test-suite.md in the target runtime.
3. Use TESTS/registry-and-routing-tests.md as the summary acceptance checklist.
4. Record actual results, runtime, date, Registry/Skill SHAs, failures and blocked cases.

A test specification, checkbox or configured CI workflow is not proof that runtime testing passed. Do not call the full regression suite passed while a mandatory case is NOT RUN or BLOCKED.

## Platform and synchronization note

GitHub stores and versions these instructions; it does not automatically activate or synchronize them in ChatGPT. Install the compact global instructions in ChatGPT Custom Instructions and provide relevant specialist files through authorized repository retrieval, Project files or uploads. Existing chats/projects may retain an older snapshot until refreshed. For Codex or another agent runtime, install specialist skills in the supported skills directory and verify discovery using that runtime's current documentation.
