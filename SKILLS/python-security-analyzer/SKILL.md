---
name: python-security-analyzer
description: Review Python syntax and potential security anti-patterns using AST and human contextual analysis; invoke for Python security review or as coding-master secondary skill.
version: 0.3.0-draft
status: draft
---

# Python Security & Syntax Analyzer

## Goal
Provide conservative, reproducible offline Python syntax and security analysis as a secondary Skill to coding-master.

## Inputs
- Python source files, Python version, trust boundary, intended execution environment and accepted scan scope.
- Actual scanner outputs, regression test logs and independently reviewed findings.

## Purpose
Supplement `coding-master` with **offline, non-executing** syntax and static security analysis. Findings are hypotheses, not proof of exploitability. No blanket OWASP Top 10 coverage claim.

## Workflow
1. Confirm source file and scope; protect secrets and personal data.
2. Run `python scanner.py path/to/file.py --output evidence.json` in an isolated, trusted environment. Do not execute scanned code.
3. Parse AST and report syntax errors with line/column. If syntax fails, state that security coverage is incomplete.
4. Review potential RCE, SQL injection, unsafe deserialization, secrets, dynamic paths, and weak hashes; supplement heuristic findings with manual dataflow/context review.
5. For each finding: rule, severity, confidence, line/column, impact, relevant snippet (redact secrets), and concrete fix.
6. Re-run the scan and project tests after edits; compare findings and regressions. Never infer security from a zero-finding scan.
7. Pass results to AI-QC CORE Final Auditor; do not approve a Skill or publish changes without human authorization.

## Quality gates
- Canonical CORE weights: 25/20/15/15/10/10/5; score >=90 and no unresolved Critical/Major.
- Maximum four rounds including initial draft; no PASS on missing evidence or unresolved blocking findings.
- Human approval is required for local activation; separate explicit approval for external publication.

## Evidence policy
- Record exact source SHA-256, scan output, test command, exit code, log digest and timestamp.
- Never treat model self-assessment or user-supplied pass flags as verified execution.
- Keep structural, functional, domain, and security review outcomes separate.

## Severity and confidence
Use Critical/High/Medium/Low for security impact and separately record confidence. Map confirmed Critical to CORE Critical and confirmed High with significant impact to CORE Major. Potential heuristic hits require validation, not automatic hard blocking.

## Safety and limitations
- `Path.resolve()` alone does not prevent traversal; check containment and symlink/race risks.
- MD5/SHA1 may be legitimate for non-security checksums; context matters.
- Parameterized SQL protects values, not dynamic SQL identifiers.
- Static scan is not taint analysis, runtime testing, penetration testing, or a security certification.
- This tool does not execute the target code, fetch external sources, use an AI API, or write GitHub.

## Taint heuristics
The scanner performs limited, order-sensitive, intra-procedural tracking, bounded direct-call summaries, simple keyword-argument binding, and conservative handling of conditional assignments. It does not provide a complete control-flow graph, whole-program taint analysis, sanitizer proof, recursion analysis, or all alias resolution. Report tainted findings as likely, not proven exploitable.

## Human review
A reviewer must verify domain limitations, actual regression evidence and the exact Skill digest before any local activation. No automatic GitHub writes.

## Acceptance tests
AST syntax, aliases, shell invocation, unsafe loaders, SQL dynamic strings, secret redaction, path heuristics, and false-positive control. Require actual executed test logs and independent review before activation.
