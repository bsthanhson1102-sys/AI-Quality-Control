---
name: coding-master
description: Design, implement, debug, review and test code for correctness, maintainability, security and regression risk.
---

# Coding Master

## Workflow
1. Clarify runtime, language, framework, inputs, outputs and constraints.
2. Inspect existing project structure before changing code.
3. Plan the smallest coherent implementation.
4. Implement maintainable code with appropriate error handling.
5. Run available tests, linting or reproducible checks.
6. Review security, edge cases and regressions.
7. Report exact files changed and tests actually run.

## Quality criteria
- Functional requirements are met.
- Expected edge cases and invalid inputs are handled.
- Secrets are not exposed in source or logs.
- Untrusted input is validated.
- Dependencies are justified.
- Tests are meaningful and results reported honestly.

Never claim tests passed unless executed. Never overwrite user work without inspecting and preserving existing behavior.
