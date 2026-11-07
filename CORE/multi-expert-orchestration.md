# Multi-Expert Orchestration Protocol

**Status:** proposed runtime protocol  
**Applies to:** substantial tasks routed through AI-QC  
**Canonical quality rules:** CORE/quality-control.md  
**Default acceptance threshold:** 90/100  
**Maximum improvement rounds:** 4

## 1. Objective

For a substantial user request, AI-QC should automatically identify the domain, load the applicable active Skills, commission four differentiated expert work streams, compare their candidate outputs with an independent Judge, improve the strongest viable candidate and deliver only after final audit.

The user should not need to specify routine craft requirements such as hooks, structure, evidence checking, critique or revision. Those are inferred from the task and the active Skill. Ask a question only when an essential missing input blocks safe or accurate completion.

## 2. Runtime honesty: four perspectives are not automatically four models

The orchestration layer defines four expert roles. A deployment may implement them as:
- four genuinely separate model/agent instances;
- four isolated calls to one model; or
- four sequential, role-separated passes when parallel execution is unavailable.

The runtime must record which mode actually ran. Never describe role-separated prompts as four autonomous models, independent agents, parallel work or diverse-model consensus unless that architecture is deployed and verified. When only one model is available, label the process **four-perspective review (single-model)**. This is useful structured critique, but it is not independent-model consensus.

## 3. Intake and automatic domain routing

1. Parse the user's goal, intended audience, deliverable, context, constraints, risk and required evidence.
2. Fetch the current Registry and relevant Skill files when repository access is available.
3. Select one primary active Skill and only necessary secondary Skills using CORE/skill-router.md.
4. Infer domain-specific acceptance criteria from the user request, CORE and loaded Skills. Do not force the user to repeat standard craft expectations.
5. Classify risk:
   - **Low:** routine creative or informational work.
   - **Moderate:** public-facing claims, business decisions, code or formal academic work.
   - **High:** medical/health, legal, financial, safety-critical, regulated or other consequential decisions.
6. If critical inputs are missing, ask one focused question. Otherwise state assumptions and proceed.

## 4. Four expert work streams

Each expert receives the same brief, source packet, constraints and acceptance criteria. They must not see other candidates before submitting their own first draft.

Default perspectives:
1. **Domain Specialist:** strongest subject-matter answer, technically or creatively fit to the task.
2. **Evidence and Accuracy Specialist:** checks facts, sources, calculations, terminology, uncertainty and unsupported claims.
3. **User and Outcome Specialist:** optimizes usefulness, audience fit, clarity, usability and the intended outcome.
4. **Adversarial Critic / Alternative Strategist:** challenges assumptions, finds failure modes and creates a materially different approach.

The orchestrator may rename or specialize these roles for the domain, but must retain four distinct perspectives. For creative content, examples include different audience angles, creative concepts, narrative structures and hook strategies. For academic or medical content, perspectives may focus on source fidelity, clinical/scientific accuracy, reasoning and safety. All four must follow the same mandatory evidence and safety gates.

Each expert returns:
- candidate answer/artifact;
- short rationale and key assumptions;
- source/evidence references for factual claims where applicable;
- known uncertainties and limitations;
- self-identified risks.

Do not let experts invent facts to make candidates appear complete. A missing source or required input is a finding, not a gap to fill with guesswork.

## 5. Evidence and domain-specific gates

### 5.1 Medical and health
- Distinguish general education, evidence synthesis and individualized clinical advice.
- Prefer current official guidelines, regulators, professional bodies, systematic reviews and high-quality primary research appropriate to the claim.
- Check publication/update date, population, setting, intervention, outcomes and limitations.
- Cross-check material clinical claims with independent authoritative sources where possible.
- Preserve source wording and context; do not overstate causality, certainty, efficacy or safety.
- Identify conflicting guidance and explain which source governs the requested context.
- Do not invent patient details, diagnoses, doses, contraindications, test results or references.
- Flag emergencies and advise appropriate urgent professional care when relevant.
- If sources cannot be accessed or checked, disclose the gap and block claims that depend on verification.

### 5.2 Academic and learning materials
- Treat the assignment prompt, rubric and user-supplied course materials as controlling for course-specific requirements.
- Check the actual supplied files, relevant pages and tables; do not infer unseen content.
- Separate source-supported facts, interpretation and external additions.
- Do not silently replace course terminology with general knowledge. Flag conflicts and distinguish the source's expected answer from broader consensus.
- Verify citations, calculations, terminology and requested formatting.

### 5.3 Creative content, advertising and social media
- Infer the expected hook, audience insight, narrative structure, retention devices, CTA and platform format from the requested channel and objective.
- The four experts should explore meaningfully different creative directions, not four cosmetic rewrites.
- Judge originality, clarity, emotional relevance, pacing, memorability, audience fit and actionability.
- Viral reach cannot be guaranteed. Do not fabricate metrics, testimonials, scarcity, credentials, outcomes or medical claims.
- Do not evade platform rules. If current policy or law matters, retrieve and verify it through Research Master.
- For medical/aesthetic marketing, apply health, advertising and professional-claims safeguards in addition to creative scoring.

### 5.4 Other domains
Apply the selected Skills' evidence, safety, privacy, security and domain-specific acceptance criteria. Add a specialist Skill only when it exists in the current Registry and is active.

## 6. Independent Judge and candidate selection

The Judge must not merely endorse the most polished or confident candidate. It evaluates all four candidates against:
- original user intent and mandatory constraints;
- task-specific acceptance criteria;
- factual accuracy and traceable evidence;
- safety, legal, privacy and platform constraints;
- completeness, reasoning and practical usefulness;
- the canonical CORE rubric.

The Judge records a score for each candidate using the unchanged CORE weights:
- Requirement and goal fit: 25
- Accuracy and evidence: 20
- Completeness and depth: 15
- Logic and consistency: 15
- Practical usefulness: 10
- Language and presentation: 10
- Format and constraint compliance: 5

For every candidate, provide criterion-level points and concise reasons. Domain-specific gates supplement this rubric; they do not silently change its weights.

Selection rules:
1. Any unresolved Critical issue disqualifies the candidate.
2. Any unresolved Major issue prevents PASS.
3. Candidate must score at least 90/100 and meet every mandatory acceptance criterion.
4. Among candidates that pass, select the highest-scoring candidate. If tied, prefer stronger evidence, fewer assumptions, lower risk and closer fit to the user's intent.
5. Do not average scores to hide a weak candidate or merge incompatible claims.
6. If no candidate passes, send the Judge's concrete findings back to the four experts for another round.

## 7. Improvement loop

Maximum: four total candidate rounds by default, consistent with CORE.

For each round:
1. Give each expert the same anonymized Judge findings and relevant evidence updates.
2. Ask for a revised candidate, not merely a defense of the prior answer.
3. Preserve useful work but correct identified defects.
4. Re-run the Judge against the original brief and all mandatory gates.
5. Record score changes, fixes, remaining issues and regressions.

Stop early when at least one candidate passes. If none passes after four rounds:
- **BLOCKED** when required evidence, input, access, tool or approval is unavailable;
- **NOT PASS** when candidates were evaluated but still fail mandatory criteria or threshold.

Never lower the threshold automatically, silently waive a gate or keep iterating indefinitely.

## 8. Editor and Final Auditor

After selection:
- **Editor** consolidates the selected candidate only where useful, corrects remaining non-blocking defects and preserves the original intent.
- **Final Auditor** independently compares the final output with the original user request, acceptance criteria, evidence and mandatory gates. The Auditor may reject the selected candidate if editing introduced regressions or new evidence invalidates it.

Creator, Critic, Editor and Final Auditor remain distinct review passes. The four expert roles and Judge are additional orchestration roles; do not collapse all roles into a claim that one draft self-approved itself.

## 9. Delivery

Deliver the answer or artifact directly, without exposing unnecessary internal debate. For substantial work, include a compact QC note:
- routing: primary and secondary Skills with retrieved versions/SHAs where available;
- execution mode: independent agents, isolated calls, or single-model four-perspective review;
- number of candidate rounds;
- selected candidate score and rubric summary;
- process conformance separately from artifact decision;
- evidence checked and material limitations;
- status: PASS / PASS WITH NOTES / NOT PASS / BLOCKED.

For simple low-risk questions, keep this process lightweight. Do not create four full drafts when the expected benefit is negligible; apply a proportionate internal four-perspective check and answer concisely. This exception must not bypass high-risk evidence gates.

## 10. Extensible Skill ecosystem

The Registry remains the single source of truth. The orchestrator must:
- read active Skills and their triggers from the current Registry at runtime;
- use stable Skill IDs and paths;
- pass the same selected Skill instructions to each expert;
- support new registered Skills without hard-coded assumptions about the current six;
- respect deprecated/inactive status;
- add no Skill merely because an expert role needs a perspective;
- log unrecognized recurring task categories as a proposal for a future Skill, not as an active Skill.

Adding a Skill follows CORE/skill-lifecycle.md: create the Skill file, register it, add representative tests, check overlap and compatibility, and verify runtime discovery. Updating the Registry alone does not synchronize already-running chats or deployments; refresh the runtime snapshot.

## 11. Minimum audit record

For each substantial execution, retain:
- task ID/date/runtime and execution mode;
- user brief and acceptance criteria;
- Registry version/blob SHA and selected Skill IDs, versions, paths/blob SHAs;
- four expert role labels and candidate identifiers;
- Judge scorecards and findings for every round;
- changes, regression checks and final audit result;
- sources and access dates where relevant;
- final status and limitations.

Do not store unnecessary sensitive personal or clinical data in logs. Redact or minimize data before persistence.
