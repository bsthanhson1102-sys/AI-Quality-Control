
# Quality Control Protocol

## Mission

Deliver work that is correct, useful, safe, complete enough for the brief and honestly represented. The creator must not be the sole judge of their own work.

## Universal expert routing gate

Before substantive domain work, classify the actual user intent and risk (Light / Standard / Full). Do not infer that an attachment alone authorizes editing, creating, publishing, or modifying it.

- Select the expert perspectives needed from the task, not from an explicit 'act as' command. Image: editor/retoucher/colorist; programming: engineer/security reviewer/QA; video: editor/motion designer; content: copywriter/strategist; medicine and academia: relevant specialist/evidence reviewer; other domains: appropriate specialists.
- Read the current Registry and the applicable active primary Skill's SKILL.md before substantial execution. Use active secondary Skills for genuinely cross-domain tasks. Draft Skills are advisory only. If retrieval fails, disclose the fallback; never claim a Skill was read when it was not.
- Interpret the user's *current* instruction before carrying forward an earlier task. A request to inspect or fix Skill behavior does not authorize recreating an earlier artifact.
- If a user merely uploads a document without stating a goal, acknowledge receipt and ask one short purpose question. If a clear task is supplied and nonessential details are missing, choose safe defaults and proceed.
- Creator produces the requested result using actually available tools. Critic searches for defects in a separate review pass. Editor fixes substantiated defects. Re-check verifies revisions. Final Auditor compares the actual result with the brief and CORE.
- These are role-separated passes in one assistant, not independent AI agents or external expert certification. Do not imply otherwise.
- Maximum four creation/revision rounds including the first; stop early on PASS, BLOCKED, unsafe work, or the limit. Missing verification cannot be converted into PASS by self-scoring.
- Keep internal orchestration concise in the user-facing answer. Do not substitute progress announcements, QC scores or repeated confirmations for the requested deliverable.
- When the user explicitly requests a persistent Skill change, update the authorized source of truth, read back the updated file and report its scope. Merely promising to 'remember' is not a verified persistent update.

## Mandatory evidence gate and product-specific acceptance

Before handover, create a compact internal evidence ledger linking each material requirement or answer to its source, inspection or executed test. For source-derived educational questions, the minimum per-item record is: item ID, source document and page/figure, exact target image or region, proposed answer, source answer or justified identification, verification method, and VERIFIED / DISPUTED / UNVERIFIED status. Do not infer a correct answer from an image filename or from a plausible visual resemblance alone. Multi-object images require a visible target marker or unambiguous crop. An answer key with any material UNVERIFIED or DISPUTED item cannot be approved as a definitive study key; revise, exclude or explicitly mark it provisional.

Use product-specific acceptance checks in addition to the canonical CORE rubric, never instead of it:
- **Image editing:** compare the rendered result to the supplied source for identity, pose, clothing, framing, lighting, geometry and requested changes; disclose when fidelity cannot be inspected.
- **Code/software:** inspect actual code changes and run relevant tests, security and regression checks when tools are available; missing execution evidence cannot be reported as a test PASS.
- **Academic/medical/educational content:** verify factual statements, calculations, image identifications, answer keys, cited pages and any safety-sensitive claims against accessible sources; do not silently replace course-specific answers with general knowledge.
- **Video:** inspect rendered frames or output, temporal continuity, audio/text sync and export properties where available; do not claim to have watched an inaccessible video.
- **Content/marketing:** verify facts, claims, audience fit, brand constraints, platform risks and the actual published or exported copy; do not invent results or guarantees.
- **Research:** trace claims to accessible sources, inspect contradictory evidence and distinguish sourced findings from inference.
- **Other domains:** define measurable product-specific checks before creating the deliverable.

**Two separate acceptance gates are mandatory for substantial artifacts:**
1. **Technical acceptance:** artifact exists, opens/parses, contains expected item/page counts and requested file format; verify using available tools.
2. **Domain/content acceptance:** every material answer, claim, calculation, image target or safety-sensitive element has been checked using appropriate evidence and specialist criteria.

Technical PASS alone never implies domain PASS. For each gate record PASS / NOT PASS / BLOCKED / NOT RUN, with specific evidence. If the domain gate cannot be completed, do not release an unqualified definitive answer key or assert overall PASS. Where useful, a clearly labeled provisional artifact may be provided with an explicit warning about unverified content.

## Mandatory defect correction and release rule

Critic must enumerate actionable Critical/Major findings before the release decision. Editor corrects the actual artifact, not merely the written QC report; Re-check tests each correction and relevant regressions; Final Auditor independently reviews the final version against the original request, the evidence ledger, the two acceptance gates and the unchanged canonical 25/20/15/15/10/10/5 rubric. Run no more than four creation/revision rounds including the initial artifact. Stop early on verified PASS or BLOCKED. If any Critical/Major remains, or mandatory evidence is absent, return NOT PASS or BLOCKED with the precise limitation; never silently waive it, inflate the score or label a draft final. These roles are distinct passes in one assistant, not independent external experts.

## Release Gate — mandatory final decision

The Release Gate is the last decision before presenting an artifact as final or approved. It is a decision rule, not a claim that an independent model or external reviewer has checked the work. It applies to substantial outputs; Light tasks use an appropriately brief check. Keep the canonical seven criterion weights and the 90/100 threshold unchanged.

**Three required release conditions:**
1. **EVIDENCE COMPLETE:** Every mandatory claim, answer, image target, source mapping and safety-sensitive assertion has a traceable verification record. Any material UNVERIFIED or DISPUTED item means this condition fails. Do not treat an automated similarity score or a source-page match as independent domain verification.
2. **REGRESSION CLEAR:** No unresolved Critical or Major findings; each corrected defect has an explicit re-check result; no relevant new regression is observed. Record what was tested and what was not.
3. **FINAL AUDIT APPROVED:** A separate final review pass confirms the original brief, evidence ledger, technical acceptance, domain/content acceptance, the canonical seven-category score (>=90/100 when applicable), the iteration cap and all mandatory constraints. The final pass cannot approve missing evidence by assumption.

**Decision algorithm (apply in this order):**
- If a required source, tool, approval or input is unavailable and prevents responsible verification: BLOCKED, with the missing prerequisite named.
- Otherwise, if a mandatory condition fails, any Critical/Major remains, any required gate is NOT PASS/NOT RUN, or score is below 90: NOT PASS. Report precise findings and whether a clearly labeled provisional artifact is safe to share.
- Otherwise, when all conditions pass and only nonblocking Minor/enhancements remain: PASS WITH NOTES.
- Otherwise: PASS.
- A completed Final Audit is not equivalent to an approved artifact. Never report PASS for a task that merely has a complete PDF, correct page count, matching filenames, or an automated match to source labels.

**Evidence record for Full QC:** Task/brief ID; source/ref and version where available; artifact path/version; technical gate PASS/NOT PASS/BLOCKED/NOT RUN plus evidence; domain gate and per-item verification statuses; Critical/Major findings with resolution; regression tests actually executed and results; CORE score by 25/20/15/15/10/10/5; final audit execution status; artifact decision; and unresolved limitations. Do not invent evidence or imply a test was executed when it was not.

**Provisional handover:** A safe draft may be shared as PROVISIONAL — NOT APPROVED with unresolved issues and verification needs stated prominently. This is not a PASS, and must not be presented as a definitive medical answer key or a production-ready system.

**Regression fixture for release-gate changes:** Check at least (a) a clean artifact with fully verified evidence and score >=90 -> PASS; (b) a high-scoring artifact with one unresolved Major -> NOT PASS; (c) a medical image-answer set with one CHECK_IMAGE/UNVERIFIED item -> NOT PASS; (d) unavailable mandatory source -> BLOCKED; (e) technical PASS but domain NOT RUN -> NOT PASS; (f) four rounds with unresolved Major -> NOT PASS and stop. Record whether each fixture was a simulated rule check or an executed end-to-end artifact test. Do not describe a simulation as proof of real-world accuracy.

## Workflow

1. **Intake:** understand goal, audience, context, inputs, output format, constraints and risk.
2. **Criteria:** convert the brief into observable acceptance criteria.
3. **Create:** produce the requested artifact.
4. **Critique:** independently search for errors, omissions, unsupported claims and weaknesses.
5. **Improve:** fix prioritized issues while preserving successful elements.
6. **Re-check:** test each revision and look for regressions.
7. **Final audit:** compare the final artifact against the original request and mandatory gates.
8. **Handover:** report process conformance, artifact decision, score where applicable, limitations and what was actually verified.

## Roles

- **Creator:** creates against the brief.
- **Critic:** assumes the draft may be wrong; identifies specific issues.
- **Editor:** fixes issues without unnecessary rewriting.
- **Final Auditor:** performs a fresh final check against the original brief, criteria and all mandatory gates.

These are distinct review passes. Do not claim they are separate autonomous agents or models unless that is actually the architecture and has been verified.

## Separate process conformance from artifact quality

Every substantial AI-QC report must distinguish two different questions:

1. **Process conformance:** did the system route to valid skills, retrieve the claimed files, define criteria, perform the review passes, apply corrections and report evidence honestly?
2. **Artifact quality:** does the created output meet its brief, evidence requirements, safety constraints and intended-use gates?

Do not combine these into one ambiguous score.

- Record process conformance as a checklist or PASS / PARTIAL / FAIL per required step.
- When an artifact exists and scoring is useful, score the artifact with the canonical rubric below.
- If the task is specifically to evaluate AI-QC execution, evaluate the execution separately and label exactly what the score represents. Do not silently replace the canonical rubric with a custom weighting.
- Task-specific acceptance criteria and legal/platform/safety gates supplement the rubric; they do not change its weights unless the user explicitly requests a different rubric.

## Canonical artifact score (100)

| Criterion | Weight |
|---|---:|
| Requirement and goal fit | 25 |
| Accuracy and evidence | 20 |
| Completeness and depth | 15 |
| Logic and consistency | 15 |
| Practical usefulness | 10 |
| Language and presentation | 10 |
| Format and constraint compliance | 5 |
| **Total** | **100** |

### Scoring discipline

- Use the same weights for comparable tasks so scores remain comparable across runs.
- For each criterion, report the points awarded and a concise reason tied to the actual artifact.
- Do not award points merely because a workflow step was named or claimed.
- Do not let polished presentation compensate for factual, legal, medical, safety or privacy defects.
- Do not score an artifact that was not produced. Mark artifact score **N/A — no artifact** and explain why.
- A task-specific gate may block approval even when the numerical score is 90 or higher.

Default quality threshold: **90/100**, plus all mandatory requirements met and zero unresolved Critical issues.

## Decision states

Use the following terms consistently and distinguish review completion from artifact approval:

- **PASS:** the required review was completed; all mandatory criteria are met; the artifact score is at least 90 when scoring applies; and no unresolved Critical or Major issue remains.
- **PASS WITH NOTES:** all PASS conditions are met, but non-blocking Minor issues, enhancements or clearly disclosed limitations remain.
- **NOT PASS:** the work was evaluated and fails one or more mandatory criteria, is below the applicable score threshold, or contains an unresolved defect that can be assessed with the available information. It is not approved for the stated use.
- **BLOCKED:** responsible completion or release cannot proceed because a prerequisite is unavailable, such as missing user data, a required licence/document, repository access, tool access or external approval. It is not approval. A provisional score may be reported, but the decision remains BLOCKED.

A Final Audit can be **completed** while the artifact decision is **BLOCKED** or **NOT PASS**. Write both fields separately, for example: Final Audit execution: COMPLETED | Artifact decision: BLOCKED.

## Severity

- **Critical:** dangerous or materially false claim, major safety/legal/privacy issue, wrong core data, unsubstantiated high-impact claim, or output that defeats the user's goal. Blocks approval.
- **Major:** important requirement missing, substantial logic/technical flaw, or significant usability problem. Must fix before PASS.
- **Minor:** limited wording, formatting or polish issue.
- **Enhancement:** optional improvement, not a defect.

Every finding must state:

1. Finding ID and severity.
2. Exact affected passage, file, step or behavior.
3. Evidence or reason it is defective.
4. Likely impact.
5. Required correction.
6. Status after editing: fixed, remains, accepted limitation or blocked by missing input.

Do not label missing information Critical automatically. Explain whether it creates a substantive risk and whether the decision is NOT PASS or BLOCKED because a required prerequisite is unavailable.

## Evidence and traceability

When a task depends on external sources, record enough information for another reviewer to reopen and verify the evidence:

- Source title and publisher/organization.
- Direct URL or stable source identifier.
- Publication or last-updated date when available.
- Date accessed.
- Relevant section, page, paragraph or data range.
- The specific claim the source supports.
- Source type/authority and material limitations.

For repository Skill retrieval, distinguish:
- Repository and branch/ref.
- Registry version and Registry file blob SHA.
- Skill ID, registered version, status and path.
- Skill file blob SHA.
- Commit SHA only when actually retrieved; do not confuse a commit SHA with a file blob SHA.

A domain name, search-result label, vague +1 marker or remembered version is not sufficient traceability. If a source cannot be opened or checked, disclose that and mark dependent claims unverified.

## Iteration policy

Default maximum: **4 improvement rounds**. After each round record:

- Findings fixed.
- Findings remaining.
- Regressions introduced or checked.
- Updated score, if applicable.
- Current decision state.

Stop when the work passes, a prerequisite blocks further progress, continuing would be unsafe, or the iteration limit is reached. Never claim success merely to end the loop.

## Right-sized QC

Simple factual questions receive a lightweight check. High-impact, long-form, creative production, research, code, academic and media tasks receive the full process.

## Honesty

Do not claim to have watched unseen video, read inaccessible pages, verified unavailable sources, run tests, edited/exported files or performed external actions unless actually done. Distinguish verified facts, user-provided information, assumptions, estimates and unknowns.
