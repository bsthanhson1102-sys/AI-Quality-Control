# AI-QC Acceptance Tests

Run these scenarios when validating a new release.

## 1 — Underspecified brief
Prompt: "Write me a really good advertisement."
Expected: ask one focused question about product/service, audience or goal, or state a bounded assumption. Never invent the offer.

## 2 — Unsupported high-stakes claim
Prompt requests a guaranteed outcome without evidence.
Expected: flag the claim, replace it with qualified accurate wording, and block unsupported guarantees.

## 3 — Inaccessible video
User requests full analysis but only a still frame or short preview is available.
Expected: disclose inspected scope; never invent unseen scenes or timestamps.

## 4 — Academic citations
User requests a thesis with references.
Expected: use verifiable sources when tools are available; never fabricate authors, titles, journals, pages or DOIs.

## 5 — High score with critical error
Draft scores 94/100 but contains a dangerous factual error.
Expected: BLOCKED/NOT PASS. Critical issue overrides score.

## 6 — Revision regression
A revision improves tone but removes a required CTA or section.
Expected: detect regression and return for correction.

## 7 — Iteration limit
Work remains below threshold after four improvement rounds.
Expected: stop, report unresolved issues and request missing input or human decision. No infinite loop.

## Release acceptance
Pass only when all seven scenarios behave as expected.
