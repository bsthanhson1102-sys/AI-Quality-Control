---
name: image-master
description: Plan, generate, inspect or revise images and visual concepts; quality-check composition, consistency, legibility, realism and brief adherence.
version: 1.0.0
status: active
---

# Image Master

## Purpose and scope
Handle image creation, image editing, visual direction, prompt writing and critique of supplied/generated images. Distinguish a rendered image from editable source files, layered documents or vector assets.

## Required inputs
Identify intended use, subject, audience, aspect ratio or dimensions, style, composition, visual hierarchy, text, palette, brand references, elements to preserve, elements to change and output format. Clarify only essential missing inputs; otherwise use sensible defaults and state them when relevant.

## Workflow
1. Determine whether the request is generation, editing, prompt design or visual analysis.
2. Inspect available references and extract constraints without guessing hidden details.
3. Build a concise visual brief: subject, framing, hierarchy, style, lighting, background, text and exclusions.
4. Choose an appropriate image-generation or editing capability when the user explicitly requests an image output.
5. Evaluate the result against the brief and reference fidelity.
6. Identify concrete defects and revise when the tool supports it.
7. Verify the final output's visible content, dimensions or file format only to the extent actually accessible.

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

## Changelog
- 1.0.0: Initial versioned release with defined scope, workflow, visual audit and output-truthfulness rules.
