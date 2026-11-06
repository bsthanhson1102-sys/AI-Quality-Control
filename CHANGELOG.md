
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


## 2026-11-06 — Specialist smoke test execution

- Recorded six specialist smoke tests (Content, Image prompt design, Video storyboard, Academic, Research and Coding) in TESTS/reports/2026-11-06-specialist-smoke-test.md; all six execution cases passed in this conversation/runtime.
- The coding smoke test completed 8/8 unit tests after Critic-driven fixes.
- GitHub Actions Registry validation completed successfully on the smoke-test report commit (run 42177079033).
- Cross-skill, unmatched-task and repository-access-failure scenarios remain NOT RUN; the complete nine-case regression suite is therefore NOT COMPLETE.


## 2026-11-06 — Global ChatGPT instruction refresh

- Updated GLOBAL-CORE-INSTRUCTIONS.txt to include the process/artifact split, canonical scoring rule, evidence traceability and consistent decision states while keeping the file at 1,492 characters.
- Updated the ChatGPT installation guide to require re-copying the global file after repository changes; GitHub does not synchronize saved Custom Instructions automatically.
