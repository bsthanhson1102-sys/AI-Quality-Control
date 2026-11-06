# T02 — Image Master: Premium skincare campaign visual

**Test date:** 2026-11-06  
**Runtime:** ChatGPT  
**Repository:** `bsthanhson1102-sys/AI-Quality-Control`  
**Branch/ref:** `main`

## 1. Intake and routing

**Test prompt:** Create a campaign visual for a fictional premium skincare brand. Use a clean editorial composition, readable space for a headline, and no medical or performance claims. Render only when explicitly authorized; otherwise provide a production-ready prompt, disclose that rendering was not requested, critique and revise.

**Expected routing:** Primary `image-master`; Secondary `content-master` only if final headline/caption copy is requested.

**Actual routing:** Primary `image-master`; no secondary. Correct routing.

## 2. Retrieved sources

| Source | Version/status | Path | File blob SHA |
|---|---|---|---|
| Registry | 1.0.0 | `REGISTRY/skills-registry.yml` | `e38086d765fae7e0895ae95bf777da23de146315` |
| Image Master | 1.0.0 / active | `SKILLS/image-master/SKILL.md` | `6a0f8c0a14207f94df79a6d49362599fd460c192` |
| Test suite | — | `TESTS/skill-routing-test-suite.md` | `b9ddf3fd7d701efd9046dc9f788bdadcfba5e109` |
| CORE rubric | — | `CORE/quality-control.md` | `6b1de5d165912344d9f096d48c1fc81196cb1274` |

These are file blob SHAs, not commit SHAs.

## 3. Acceptance criteria

1. Define visual intent, subject, format, composition, hierarchy, style and constraints.
2. Preserve clear space for a headline.
3. Exclude medical and performance claims.
4. Do not generate a rendered image without explicit authorization in the active test.
5. Distinguish prompt/production plan from rendered image.
6. Critique composition, legibility, visual consistency and brief fit.
7. Revise weak points and perform a final check.

## 4. Creator artifact — production-ready prompt

**Visual brief**
- Use: fictional premium skincare campaign.
- Format: vertical 4:5 social feed visual.
- Subject: one unbranded frosted-glass skincare bottle.
- Style: minimal luxury editorial photography.
- Palette: warm ivory, beige, muted sage, restrained champagne accents.
- Layout: product in right third; generous headline space in upper-left.
- Lighting: soft diffused window light and natural contact shadows.
- Exclusions: text, logos, labels, certification marks, medical imagery, before/after comparisons, efficacy/performance claims, extra products and watermarks.

**Revised prompt:**

```text
Create a premium skincare campaign visual, vertical 4:5 aspect ratio,
with a clean luxury editorial art direction.

MAIN SUBJECT:
One unbranded frosted-glass skincare bottle, elegant and minimal,
occupying approximately 30–38% of the image height. Place it in the
right third of the composition, standing upright on a pale natural
stone pedestal. The bottle must have a blank, unprinted surface.

HEADLINE SPACE:
Reserve the upper-left 40% of the canvas as uncluttered negative
space. Keep this area visually quiet, with a smooth warm-ivory
background and even lighting, suitable for adding a headline later.

ART DIRECTION:
Warm ivory, soft beige, muted sage and restrained champagne accents.
Soft diffused window light, realistic contact shadows, subtle
stone and frosted-glass textures. Premium beauty magazine
photography, natural proportions, restrained styling.

COMPOSITION:
One bottle, one pedestal, no more than one subtle secondary prop.
Clear focal hierarchy. Product must remain recognizable at
mobile-feed size. No cropping of the bottle.

STRICT EXCLUSIONS:
No text, letters, logo, brand name, label, certification,
medical imagery, before-and-after comparison, efficacy claim,
performance claim, clinical symbols, extra products or watermark.
```

## 5. Independent Critic

**C1 — Minor: headline region insufficiently controlled in first draft.**
- Affected passage: “upper-left area”.
- Reason: local contrast or visual detail could reduce headline legibility.
- Impact: text overlay might be difficult to read.
- Correction: reserve the upper-left 40% with a smooth warm-ivory background and even lighting.
- Status: fixed.

**C2 — Minor: product scale and placement underspecified.**
- Reason: product could render too small, too large or cropped.
- Impact: weak visual hierarchy at mobile-feed size.
- Correction: specify right-third placement and 30–38% of canvas height; prohibit cropping.
- Status: fixed.

**C3 — Enhancement: limit secondary props.**
- Correction: no more than one subtle secondary prop.
- Status: fixed.

## 6. Editor and re-check

Editor revised the prompt with measurable layout guidance, product scale, reserved text space, prop limits and strict exclusions.

Re-check confirms:
- Vertical 4:5 format is explicit.
- Headline space is measurable and visually protected.
- Product hierarchy and crop constraints are clear.
- No medical or performance claims are requested.
- No text, brand or certification is invented.
- Rendering was not requested or performed.

## 7. Final Audit and canonical artifact score

| CORE criterion | Score | Rationale |
|---|---:|---|
| Requirement and goal fit | 25/25 | Meets visual brief and no-render condition |
| Accuracy and evidence | 20/20 | No factual/product efficacy claims |
| Completeness and depth | 14/15 | Detailed production prompt; no actual render by design |
| Logic and consistency | 15/15 | Subject, hierarchy and exclusions are coherent |
| Practical usefulness | 9/10 | Prompt is actionable and measurable |
| Language and presentation | 9/10 | Clear production directions |
| Format and constraint compliance | 5/5 | Correctly delivers prompt, not image |
| **Total** | **97/100** | |

**Process conformance:** PASS. Registry and Skill were retrieved; routing matched; criteria were defined; Critic, Editor and Final Auditor passes were completed.

**Artifact decision:** PASS WITH NOTES. The production-ready prompt meets the test. Note: no rendered image exists, because the test explicitly says not to render without authorization. The score applies to the prompt/brief, not an image.

## 8. Unverified items

- Actual image quality, typography rendering, artifact defects and dimensions of a rendered file are not evaluated because no image was generated.
- No real brand asset or product reference was supplied; the subject is intentionally fictional and unbranded.

## 9. Repository changes

This is a separate test report. No Registry or Skill file was modified.
