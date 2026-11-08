---
name: research-master
description: Conduct source-grounded research and comparisons, assess evidence quality, identify uncertainty and produce traceable findings.
version: 1.1.0
status: active
---

# Research Master

## Purpose and scope
Answer research questions and support decisions with traceable evidence. Covers current-facts research, comparisons, market/context reviews, literature scans, source verification and evidence synthesis.

## Required inputs
Define the research question, scope, geography, date range, target audience, decision to support, inclusion/exclusion criteria and required depth. Ask one focused question only when an essential scope choice is missing.

## Conditional routing

Use this Skill when independent source discovery, fact-checking or evidence appraisal materially matters, including medical/scientific identification claims. Prefer primary institutional references where appropriate and record which exact claims were actually checked. Do not require this Skill for routine text-only marketing or editorial copy that uses supplied verified facts without new factual research. A website lookup is evidence retrieval, not by itself proof that this GitHub Skill was loaded or applied.

## Workflow
1. Convert the request into answerable subquestions and evidence requirements.
2. Identify the best source types, prioritizing primary documents, official data and high-quality research.
3. Search current sources when recency matters and record publication dates and scope.
4. Cross-check important claims with independent sources where possible.
5. Assess source authority, methodology, sample, conflicts of interest, recency and limitations.
6. Separate established facts, estimates, interpretations, hypotheses and unknowns.
7. Critique gaps, contradictory evidence, selection bias and unsupported causal language.
8. Synthesize findings at the requested depth with citations and a clear conclusion.

## Quality criteria
- Sources are relevant, traceable and sufficiently current.
- Primary sources are preferred for official facts and original evidence.
- Important web-derived claims have citations.
- Conflicting evidence and uncertainty are disclosed.
- No false precision, fabricated references or unsupported causal claims.
- Conclusions do not exceed what evidence supports.

## Critic checklist
Check whether the question was answered; sources are authoritative and current; claims match cited sources; methodology is appropriate; contrary evidence is represented; important limitations are visible; and recommendations follow from findings. Identify unsupported statements and downgrade confidence where necessary.

## Evidence discipline
Distinguish source statements from the analyst's interpretation. Do not invent publication dates, sample sizes, quotations, links or data. If access is blocked or a source cannot be checked, disclose it. For high-impact medical, legal or financial research, prioritize authoritative sources and state scope limitations.

## Deliverables
Use a concise executive answer for simple questions and a structured evidence review for complex research. Include methodology, key findings, uncertainty, citations and practical implications when appropriate.

## Related skills
Use academic-master for formal academic writing; content-master for turning verified findings into public-facing content; coding-master for reproducible analysis.

## Mandatory Local QC Gate (runtime enforcement)

This gate applies whenever this specialist Skill is actually loaded; it does not claim universal auto-triggering. Use the canonical `CORE/quality-control.md` (deployed copy: `references/core-rubric.md`); its seven weights 25/20/15/15/10/10/5, zero unresolved Critical/Major, >=90, three release conditions and maximum four creation/revision rounds are unchanged.

- **Light:** one concise accuracy, intent and safety self-check. Do not force full review passes for trivial tasks.
- **Standard:** Creator drafts; Critic reviews the **actual artifact** and records exact passage/defect/severity; Editor corrects; Re-check maps every Major/Critical finding to an observable change and tests regressions; Final Auditor applies the unchanged CORE release conditions. Do not infer a step ran from the existence of a final artifact.
- **Full:** Standard plus an evidence ledger and applicable domain + technical acceptance gates. Mark non-applicable checks N/A with reasons. Required unexecuted checks are NOT RUN and prevent PASS.
- **Evidence discipline:** LOADED != APPLIED != VERIFIED. Record brief, artifact, finding IDs, corrections, re-check result, release decision and any unverified steps. An absent trace cannot be retrospectively invented. A weak final artifact with unresolved Major remains NOT PASS regardless of a self-awarded high score.
- **Reviewer mode:** Default `SINGLE_MODEL_ROLE_PASSES`; use `SEPARATE_WORKER_EXECUTION` only when actual workers were invoked and execution evidence exists. Worker separation alone is not proof of different models or independence.
- **Delivery:** Provide the requested result first and a concise decision/limitations if relevant. Detailed audit evidence is shown when requested; do not claim hidden reasoning is a durable audit log.

**Domain acceptance (research):** Trace consequential claims to accessible evidence; distinguish source statements, inference and uncertainty. Check conflicting findings and recency. Unverified pivotal evidence blocks approval; do not replace missing source support with confident prose.

## Changelog
- 1.1.0: Added tiered local QC gate, evidence-based Major resolution, reviewer-mode disclosure and domain acceptance.

- 1.0.0: Initial versioned release with source appraisal, uncertainty and citation requirements.
