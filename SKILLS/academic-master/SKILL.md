---
name: academic-master
description: Plan, draft, revise and audit academic assignments, reports, theses and clinical case writeups for structure, evidence, methodology and formatting compliance.
version: 1.1.0
status: active
---

# Academic Master

## Purpose and scope
Produce and audit academic work against the actual assignment prompt, rubric, course materials and institutional formatting rules. Covers outlines, essays, reports, presentations, literature reviews and educational clinical case writeups.

## Required inputs
Identify assignment prompt, rubric, course/lecture files, subject, required sections, word/page count, citation style, formatting, submission format and deadline. Ask for missing essential materials only when they materially determine correctness. Never invent institutional requirements.

## Workflow
1. Read the assignment prompt, rubric and supplied course materials; inspect relevant sections of files.
2. Convert every rubric criterion into a checklist and map it to the outline.
3. Separate user-provided facts, source-backed facts, calculations, interpretations and assumptions.
4. Research and cite sources when the task requires evidence; prioritize primary and authoritative references.
5. Draft with appropriate academic tone, depth and terminology.
6. Audit structure, completeness, logic, methods, calculations, citations, originality and formatting.
7. Revise and verify every required section and file-format constraint.

## Image-based examination and answer-key verification gate

For visual identification quizzes, especially medical/parasitology training:
1. Inspect the actual source page image, including any caption, label, answer key and nearby context. Do not rely on PDF extracted text alone when the evidence is visual.
2. Build a per-question traceability ledger: question number; source filename/page/figure; precise target region or crop; proposed identification; answer stated by the course material (if present); verification status (VERIFIED / DISPUTED / UNVERIFIED); and a short diagnostic morphology cue.
3. If one figure contains multiple organisms or stages, crop or mark exactly which specimen is being asked about; otherwise rewrite or omit the ambiguous question.
4. Keep supplied course answers separate from independent expert interpretation. Where they disagree, flag the discrepancy and source; never silently overwrite the source.
5. Distinguish morphologically similar eggs, cysts, trophozoites and blood stages using the visible distinguishing features. When the image is inadequate, mark UNVERIFIED rather than guessing.
6. Check question count, numbering, answer mapping, source-page references, legibility and PDF openability as **technical acceptance**. Separately check identification accuracy, source traceability, target ambiguity and medical safety as **domain acceptance**.
7. Do not publish a definitive answer key or claim academic QC PASS while any material question remains UNVERIFIED or DISPUTED. Correct, replace, omit or label the entire affected material as provisional, then re-check every changed item.
8. Run Creator → Critic → Editor → Re-check → Final Auditor, at most four rounds including the first. Preserve the CORE weights and zero Critical/Major gate. State actual evidence and limits; do not claim independent verification unless another independent reviewer or tool was truly used.

## Release Gate for academic and medical study materials

Before describing a question bank, answer key or medical teaching PDF as approved, apply CORE's three Release Gate conditions: EVIDENCE COMPLETE, REGRESSION CLEAR and FINAL AUDIT APPROVED. A source-page or image-similarity match is a technical aid, not sufficient evidence of domain correctness. In particular, any CHECK_IMAGE, UNVERIFIED or DISPUTED question blocks an unqualified PASS. Record technical and domain gate results separately; verify each corrected question and recheck its answer mapping. If mandatory evidence is unavailable, report BLOCKED; if a known verification defect remains, report NOT PASS. A clearly marked provisional study draft may be handed over when safe, but never as a definitive answer key. Follow the four-round cap and unchanged CORE rubric.

## Quality criteria
- All required sections are present and proportionate.
- Claims have suitable support or are clearly identified as analysis.
- References are real, relevant and accurately represented.
- No invented patient data, research results, references or institutional requirements.
- Tables, figures, units, abbreviations and terminology are consistent.
- Formatting follows the actual rubric, not a guessed template.
- Conclusions do not exceed the evidence.

## Critic checklist
Compare the draft line-by-line with the rubric; check missing sections, unsupported claims, contradictory data, weak reasoning, incorrect terminology, citation integrity, calculation errors, repetition, formatting and scope. Preserve course-specific terminology where appropriate.

## Health and academic integrity safeguards
For clinical or health-related content, distinguish educational discussion from diagnosis or treatment advice. Do not fabricate patient details or clinical observations. Flag conflicts between supplied course materials and broader references rather than silently replacing one. Do not help misrepresent authorship, data collection or source consultation.

## Deliverables
Use the requested structure and file specifications. If a downloadable file is requested, verify that it was actually created and provide its real link. If only text is produced, do not claim a Word/PDF file exists.

## Related skills
Use research-master for literature search and evidence appraisal; coding-master for statistical scripts or data processing.

## Mandatory Local QC Gate (runtime enforcement)

This gate applies whenever this specialist Skill is actually loaded; it does not claim universal auto-triggering. Use the canonical `CORE/quality-control.md` (deployed copy: `references/core-rubric.md`); its seven weights 25/20/15/15/10/10/5, zero unresolved Critical/Major, >=90, three release conditions and maximum four creation/revision rounds are unchanged.

- **Light:** one concise accuracy, intent and safety self-check. Do not force full review passes for trivial tasks.
- **Standard:** Creator drafts; Critic reviews the **actual artifact** and records exact passage/defect/severity; Editor corrects; Re-check maps every Major/Critical finding to an observable change and tests regressions; Final Auditor applies the unchanged CORE release conditions. Do not infer a step ran from the existence of a final artifact.
- **Full:** Standard plus an evidence ledger and applicable domain + technical acceptance gates. Mark non-applicable checks N/A with reasons. Required unexecuted checks are NOT RUN and prevent PASS.
- **Evidence discipline:** LOADED != APPLIED != VERIFIED. Record brief, artifact, finding IDs, corrections, re-check result, release decision and any unverified steps. An absent trace cannot be retrospectively invented. A weak final artifact with unresolved Major remains NOT PASS regardless of a self-awarded high score.
- **Reviewer mode:** Default `SINGLE_MODEL_ROLE_PASSES`; use `SEPARATE_WORKER_EXECUTION` only when actual workers were invoked and execution evidence exists. Worker separation alone is not proof of different models or independence.
- **Delivery:** Provide the requested result first and a concise decision/limitations if relevant. Detailed audit evidence is shown when requested; do not claim hidden reasoning is a durable audit log.

**Domain acceptance (academic):** Verify source fidelity, exact requested structure, medical/academic accuracy, answer keys and any referenced figures. Unseen figures or unverified key answers block definitive approval where material. A generated document's existence is not proof its layout or citations were checked.

## Changelog
- 1.1.0: Added tiered local QC gate, evidence-based Major resolution, reviewer-mode disclosure and domain acceptance.

- 2026-11-08: Applied CORE Release Gate to question banks and medical study materials; unverified image IDs block definitive approval (v1.0.0 retained).
- 2026-11-08: Added per-image evidence ledger, ambiguous-figure handling, separate technical/domain gates and mandatory answer-key verification (v1.0.0 retained).
- 1.0.0: Initial versioned release with rubric-first workflow, source integrity and clinical safeguards.
