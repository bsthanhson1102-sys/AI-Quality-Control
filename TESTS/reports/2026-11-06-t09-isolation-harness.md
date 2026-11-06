# T09 Isolation Harness — implementation and verification

**Date:** 2026-11-06  
**Repository:** `bsthanhson1102-sys/AI-Quality-Control`  
**Branch:** `main`  
**Primary Skill:** `coding-master` v1.0.0, active  
**Registry:** v1.0.0  
**Purpose:** provide a reproducible clean evaluation packet and evidence-integrity checker for a future T09 isolated run.

## 1. Intake and acceptance criteria

The harness must:
1. Prepare a minimal evaluation packet containing only a task prompt, evidence template, short instructions and empty artifact directory.
2. Avoid copying Registry, CORE, Skills or previous reports into that packet.
3. Record fresh-session, prior-context, attachment and retrieval-access states explicitly.
4. Hash the task prompt and full transcript with SHA-256.
5. Verify that artifact and transcript paths remain inside the evidence bundle.
6. Reject incomplete, contradictory or malformed evidence.
7. Never claim that local metadata checks prove hidden model-context isolation.
8. Use Python Standard Library only and include automated tests.

## 2. Source retrieval

- Repository: `bsthanhson1102-sys/AI-Quality-Control`, branch `main`.
- Registry `REGISTRY/skills-registry.yml`: v1.0.0, blob SHA `e38086d765fae7e0895ae95bf777da23de146315`.
- CORE `CORE/quality-control.md`: blob SHA `6b1de5d165912344d9f096d48c1fc81196cb1274`.
- Primary Skill: `coding-master`, v1.0.0, active, path `SKILLS/coding-master/SKILL.md`, blob SHA `79594e8be87fb2fa48ddba3e77be11e9472833c7`.

No secondary Skill was needed.

## 3. Deliverables

- `TOOLS/t09_isolation_harness.py` — `prepare` and `verify` CLI commands.
- `TESTS/test_t09_isolation_harness.py` — automated regression tests.
- `TESTS/T09-ISOLATION-HARNESS.md` — operating procedure and limitations.

### Usage

Prepare a fresh packet:

```bash
python TOOLS/t09_isolation_harness.py prepare /tmp/ai-qc-t09-run
```

After the independent evaluation, save its transcript, artifact files and completed evidence record, then run:

```bash
python TOOLS/t09_isolation_harness.py verify /tmp/ai-qc-t09-run
```

Exit code 0 means the evidence bundle is structurally consistent and hashes match. It does **not** mean hidden model context was independently proven to be isolated.

## 4. Creator → Critic → Editor → Re-check

### Creator

Implemented the packet generator and evidence verifier. The packet includes no Registry, CORE, Skill or prior report files. The verifier checks human attestations, explicit source-access state, prompt/transcript hashes, test-count consistency, artifact presence and path containment.

### Critic findings

- **T09-H01 — Major:** the first verifier checked artifact path containment but did not constrain the transcript path. A crafted transcript path could resolve outside the evidence bundle.
- **T09-H02 — Major:** the first verifier did not reject evidence claiming web/browser retrieval was still available, which conflicts with the hard source-isolation requirement.
- **T09-H03 — Minor:** malformed JSON with a non-object root could cause an attribute error rather than a controlled validation result.

### Editor changes

- Added transcript path containment validation.
- Rejects any evidence record that says GitHub, web/browser or network retrieval remains available.
- Requires explicit Registry and Skill access-result strings.
- Rejects non-object evidence JSON roots with a controlled error.
- Added regression tests for each finding.

### Re-check

Executed with the Python runtime:

```bash
python -m unittest -v test_t09_isolation_harness
```

Observed result: **11 tests run, 11 passed, 0 failures, 0 errors**.

Coverage includes minimal packet creation, valid evidence, missing evidence, non-object JSON, prior-context injection, Registry/Skill attachment, available retrieval channel, transcript hash mismatch, artifact path traversal, transcript path traversal and inconsistent test counts.

## 5. Final audit and limitations

| Check | Result |
|---|---|
| Minimal packet excludes Registry/CORE/Skills | PASS |
| Prompt and transcript hash verification | PASS |
| Transcript and artifact path containment | PASS |
| Contradictory retrieval-state evidence rejected | PASS |
| Malformed evidence root handled safely | PASS |
| Automated tests | PASS — 11/11 |
| True hidden model-context isolation | NOT VERIFIED |
| Platform-enforced connector/network disabling | NOT PROVIDED BY THIS SCRIPT |

**Important limitation:** this is an evidence preparation and validation harness, not a sandbox for the model. It cannot inspect hidden conversation context, control ChatGPT tool availability, or prove human attestations are truthful. A separate fresh evaluation runtime must actually omit prior context and disable repository, browser/web and network retrieval. The Final Auditor must inspect the transcript and runtime setup.

## 6. Artifact score — canonical CORE rubric

| Criterion | Score |
|---|---:|
| Requirement and goal fit | 25/25 |
| Accuracy and evidence | 19/20 |
| Completeness and depth | 14/15 |
| Logic and consistency | 15/15 |
| Practical usefulness | 9/10 |
| Language and presentation | 10/10 |
| Format and constraint compliance | 4/5 |
| **Total** | **96/100** |

**Artifact decision: PASS WITH NOTES.** The harness is implemented and its automated tests pass. The principal limitation is intentional and disclosed: it validates evidence consistency but cannot prove hidden runtime isolation.

**Process conformance for harness development: PASS.** Registry, CORE and the active primary Skill were retrieved; criteria were defined; Creator, Critic, Editor, Re-check and Final Audit passes were completed; findings were corrected and regression-tested.

**T09 isolated-fallback test decision: BLOCKED.** The harness is ready to prepare and inspect a future evidence bundle, but no new isolated model run has yet been executed. Do not change T09 to PASS until that run and its runtime evidence are reviewed.

## 7. Next action

Run the generated `prompt.md` in a genuinely fresh, separately configured evaluation session with no prior context or Registry/Skill payload and no retrieval channels. Preserve the full transcript and complete `evidence.json`; then run the verifier and conduct a human Final Audit.
