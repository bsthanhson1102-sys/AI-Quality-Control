---
name: image-master
description: Plan, generate, inspect or revise images and visual concepts; quality-check composition, consistency, legibility, realism and brief adherence.
version: 1.1.0
status: active
---

# Image Master

## Purpose and scope
Handle image creation, image editing, visual direction, prompt writing and critique of supplied/generated images. Distinguish a rendered image from editable source files, layered documents or vector assets.

## Required inputs
Identify intended use, subject, audience, aspect ratio or dimensions, style, composition, visual hierarchy, text, palette, brand references, elements to preserve, elements to change and output format. Clarify only essential missing inputs; otherwise use sensible defaults and state them when relevant.

## Mandatory preflight and edit fidelity
- For a substantial image task, verify the active image-master entry in the Registry and read this Skill before invoking an image tool. Do not retroactively claim preflight happened.
- Distinguish user requests to edit an existing image from generating a new image inspired by it. An edit must use the supplied image as the source/reference whenever the available tool supports it; never silently substitute a newly imagined portrait.
- If the user says only 'make it better', default to a conservative photographic retouch: preserve faces, identity, facial proportions, pose, hands, clothing, accessories, background content and original framing unless change is clearly requested.
- Set explicit preservation constraints before editing. When faithful source editing cannot be verified, disclose the limitation rather than claiming exact identity preservation.
- A question about Skill performance, QC, configuration or a prior image edit is a process-review task, NOT permission to edit or regenerate the image. Never invoke image generation solely to fix a process complaint.

## Conditional scientific-image verification

When explicitly routed for scientific or medical image identification, inspect the actual target region, labels and source-page mapping; describe observable morphological features, disambiguate multi-object panels and flag uncertainty. Coordinate factual taxonomy and diagnostic criteria with research-master or authoritative evidence as needed. Do not claim medical identification has been verified from visual plausibility or a matching page alone. For text-only content and already verified illustrative images, this Skill is not required.

## Workflow
1. Determine whether the request is generation, editing, prompt design or visual analysis.
2. Inspect available references and extract constraints without guessing hidden details.
3. Build a concise visual brief: subject, framing, hierarchy, style, lighting, background, text and exclusions.
4. Choose an appropriate image-generation or editing capability when the user explicitly requests an image output.
5. Perform a distinct Critic pass against the original image and the brief, including facial likeness, hands, clothing embroidery, accessories, framing, color and newly introduced details. State what was actually inspectable.
6. Perform an Editor pass on concrete defects when the tool supports another edit; re-check regressions. Use at most four rounds total including the first output; do not loop indefinitely or silently alter identity.
7. Perform a Final Auditor pass using CORE and its mandatory gates. Never award PASS without an inspected artifact; report NOT PASS or BLOCKED when verification is missing.
8. Verify the final output's visible content, dimensions or file format only to the extent actually accessible.

## Quality criteria
- Subject and visual hierarchy are clear.
- Composition, crop and aspect ratio fit intended placement.
- Required text is spelled correctly and legible.
- Anatomy, geometry, perspective, lighting and shadows are coherent.
- Repeated subjects and brand elements remain consistent.
- Required elements are present; forbidden elements are absent.
- No unintended objects, artifacts, misleading details or unwanted watermarks.
- The output matches the requested style without losing essential identity or information.

## Critic checklist
Inspect framing, balance, focal point, proportions, anatomy, perspective, lighting, material rendering, color, typography, text accuracy, edge artifacts, consistency, brand accuracy and adherence to every preserve/change instruction. Separate objective defects from subjective preferences.

## Safety and truthfulness
Respect image rights, privacy and applicable safety rules. Do not infer sensitive traits from appearance. Never claim layered, editable, vector, PSD or source-file output unless that exact format was actually produced and checked. Do not claim a precise edit was completed if only a prompt or edit plan was supplied.

## Deliverables
Return the requested image or prompt. When only planning is possible, provide a precise production brief and disclose that no rendered/editable file was created. Include a concise QC note for complex deliverables.

## Related skills
Use content-master for copy and typography; video-master for motion adaptation; research-master when factual visual details need verification.

## Mandatory Local QC Gate (runtime enforcement)

This gate applies whenever this specialist Skill is actually loaded; it does not claim universal auto-triggering. Use the canonical `CORE/quality-control.md` (deployed copy: `references/core-rubric.md`); its seven weights 25/20/15/15/10/10/5, zero unresolved Critical/Major, >=90, three release conditions and maximum four creation/revision rounds are unchanged.

- **Light:** one concise accuracy, intent and safety self-check. Do not force full review passes for trivial tasks.
- **Standard:** Creator drafts; Critic reviews the **actual artifact** and records exact passage/defect/severity; Editor corrects; Re-check maps every Major/Critical finding to an observable change and tests regressions; Final Auditor applies the unchanged CORE release conditions. Do not infer a step ran from the existence of a final artifact.
- **Full:** Standard plus an evidence ledger and applicable domain + technical acceptance gates. Mark non-applicable checks N/A with reasons. Required unexecuted checks are NOT RUN and prevent PASS.
- **Evidence discipline:** LOADED != APPLIED != VERIFIED. Record brief, artifact, finding IDs, corrections, re-check result, release decision and any unverified steps. An absent trace cannot be retrospectively invented. A weak final artifact with unresolved Major remains NOT PASS regardless of a self-awarded high score.
- **Reviewer mode:** Default `SINGLE_MODEL_ROLE_PASSES`; use `SEPARATE_WORKER_EXECUTION` only when actual workers were invoked and execution evidence exists. Worker separation alone is not proof of different models or independence.
- **Delivery:** Provide the requested result first and a concise decision/limitations if relevant. Detailed audit evidence is shown when requested; do not claim hidden reasoning is a durable audit log.

**Domain acceptance (image):** Inspect the actual final image, not just its prompt. Check requested edit fidelity, identity/source preservation where applicable, composition, typography, visual artifacts, and medical/scientific correctness when relevant. If no rendered image or preview was inspected, mark visual verification NOT RUN and never claim a visual PASS.

## Changelog
- 1.1.0: Added tiered local QC gate, evidence-based Major resolution, reviewer-mode disclosure and domain acceptance.

- 2026-11-08: Added mandatory preflight, source-fidelity defaults, distinct QC passes and prohibition on unrequested image generation during process reviews (no version/status change).
- 1.0.0: Initial versioned release with defined scope, workflow, visual audit and output-truthfulness rules.
