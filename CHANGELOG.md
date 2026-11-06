
# Changelog

## 2026-11-06 — QC protocol and regression suite hardening

- Standardized the canonical artifact rubric and clarified that task-specific acceptance gates supplement rather than silently replace its weights.
- Separated process conformance from artifact quality so a completed review workflow cannot be confused with approval of the artifact.
- Defined consistent PASS, PASS WITH NOTES, NOT PASS and BLOCKED decision states.
- Added evidence traceability requirements for external sources and GitHub Registry/Skill retrieval, including the distinction between file blob SHAs and commit SHAs.
- Added a nine-case Skill routing and execution regression suite covering all six registered specialist skills, cross-skill routing, unmatched requests and repository-access failure.
- Updated Registry/routing acceptance checks, ChatGPT master instructions and repository documentation to use the same QC rules.
- These changes define and document the tests; they do not claim that all nine scenarios have been executed in a live ChatGPT/Codex runtime.
- Runtime-level Skill execution and the GitHub Actions run remain subject to actual verification in their target environments.
