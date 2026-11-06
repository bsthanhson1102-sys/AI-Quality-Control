# AI Quality Control (AI-QC)

A modular multi-skill quality system for independent critique, evidence-aware self-improvement and final quality assurance. The repository is the canonical, version-controlled source for specialist skills and shared protocols.

## Mission
Deliver work that is accurate, useful, safe, complete enough for the brief and honestly represented. The creator must not be the sole judge of their own work.

## Standard workflow
`Intake → Criteria → Create → Independent Critique → Improve → Re-check → Final Audit → Deliver`

## Four roles
- **Creator:** creates against the brief.
- **Critic:** independently identifies errors and weaknesses.
- **Editor:** fixes prioritized defects while preserving successful work.
- **Final Auditor:** checks the finished result against the original request.

## Quality gate
Default score: **90/100**. Any unresolved Critical issue blocks approval regardless of score. Default maximum: **4 improvement rounds**. If still not acceptable, disclose unresolved issues; do not fake a pass.

## Repository map
- `CORE/`: shared QC protocol, critique, improvement, final audit, skill router and lifecycle policy.
- `REGISTRY/skills-registry.yml`: central catalogue of skill IDs, versions, paths, status and routing triggers.
- `SKILLS/`: modular specialist skills (Content, Image, Video, Academic, Research and Coding).
- `PLATFORMS/CHATGPT/`: global core instructions, master instructions and installation guidance.
- `PLATFORMS/CODEX/`: deployment guidance for Codex-compatible agent environments.
- `TESTS/`: quality gates and registry/routing acceptance tests.
- `TOOLS/validate_registry.py`: standard-library validator for registry paths and skill metadata.
- `.github/workflows/validate-ai-qc.yml`: runs registry validation on pushes and pull requests to `main`.

## Add or update a skill
Follow `CORE/skill-lifecycle.md`. Add a new `SKILLS/<skill-id>/SKILL.md`, register it in `REGISTRY/skills-registry.yml`, add representative tests, and review routing/dependencies. For updates, fetch the latest file first, increment its version, append a changelog and verify dependent references. Prefer deprecation with a migration note over immediate deletion.

## Platform and synchronization note
GitHub stores and versions these instructions; it does not automatically activate or synchronize them in ChatGPT. Install the compact global instructions in ChatGPT Custom Instructions and provide relevant specialist files through authorized repository retrieval, Project files or uploads. Existing chats/projects may retain an older snapshot until refreshed. For Codex or another agent runtime, install specialist skills in the supported skills directory and verify discovery using that runtime's current documentation.

## Validation
See `TESTS/quality-gates.md` and `TESTS/registry-and-routing-tests.md`. Run `python TOOLS/validate_registry.py` locally or let the GitHub Actions workflow run on a push/PR. A checklist or configured workflow is not proof that tests passed; record actual runtime results before calling a release production-ready.
