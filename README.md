# AI Quality Control (AI-QC)

A multi-skill quality system for independent critique, evidence-aware self-improvement and final quality assurance. Designed for parallel use in ChatGPT and GitHub/Codex-compatible agent environments.

## Mission
Deliver outputs that are accurate, useful, safe, complete enough for the brief and honestly represented. The creator must not be the sole judge of their own work.

## Standard workflow
`Intake → Criteria → Create → Independent Critique → Improve → Re-check → Final Audit → Deliver`

## Four roles
- **Creator:** creates against the brief.
- **Critic:** independently identifies errors and weaknesses.
- **Editor:** fixes prioritized defects while preserving successful work.
- **Final Auditor:** checks the finished result against the original request.

## Quality gate
Default score: **90/100**. Any unresolved Critical issue blocks approval regardless of score. Default maximum: **4 improvement rounds**. If still not acceptable, disclose the unresolved issues; do not fake a pass.

## Repository map
- `CORE/`: shared QC protocol, critique, improvement and final audit.
- `SKILLS/`: Content, Image, Video, Academic, Research and Coding.
- `PLATFORMS/CHATGPT/`: master instructions for ChatGPT configuration.
- `PLATFORMS/CODEX/`: deployment guidance for agent skills.
- `TESTS/`: acceptance tests.

## Platform note
GitHub stores and versions these instructions; it does not automatically activate them in ChatGPT. Configure or upload the ChatGPT instructions separately. For Codex or another agent runtime, install the specialist skill folders in the supported skills directory and verify discovery using that runtime's current documentation.

## First release
See `TESTS/quality-gates.md` before treating this system as production-ready.
