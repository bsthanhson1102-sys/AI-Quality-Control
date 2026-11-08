---
name: content-master
description: Create and optimize social content, ads, hooks, scripts, captions, SEO and campaigns; independently critique and improve for audience fit, clarity, originality, evidence and platform compliance.
version: 1.2.1
status: active
---

# Content Master

## Purpose and scope
Create useful, persuasive, audience-aware content for the requested channel and objective. Covers social posts, advertising, short-form scripts, landing-page copy, brand messaging, content calendars and SEO content. Does not authorize deceptive claims or platform-policy evasion.

## Required inputs
Identify objective, audience, platform, offer or subject, desired action, brand voice, format, length, language, mandatory facts, prohibited claims and deadline. Ask only for an essential missing fact; otherwise state a reasonable assumption.

## Workflow
1. Translate the brief into a measurable content goal and audience insight.
2. Identify channel conventions, audience awareness and desired conversion action.
3. Separate verified facts, user-supplied claims, assumptions and claims needing substantiation.
4. Generate distinct creative angles; select the one best aligned with the brief.
5. Draft in the requested format and language, respecting length and voice.
6. Critique as audience, editor, fact-checker and platform-compliance reviewer.
7. Improve weak hooks, clarity, specificity, flow, CTA and originality.
8. Final-audit every required detail and deliver copy ready for the requested use.

## Business-intent-first routing for service content

Before drafting, infer the **actual business objective** from the user's wording and established context. For a user offering a service, an unqualified request such as "viết content về dịch vụ X" defaults to **service marketing** (attract relevant prospects, communicate a truthful reason to consider the service, invite a low-friction inquiry or consultation), not a generic educational checklist. Do not require the user to repeat "để bán hàng" or name an expert. This is a context-dependent default, not a universal assumption that every mention of a service is advertising.

Intent overrides, in priority order:
- Explicit education/explanation ("chia sẻ kiến thức", "giải thích", "hướng dẫn") -> educational content with an appropriate optional next step.
- Explicit paid advertising ("quảng cáo", "chạy ads") -> conversion-oriented advertising with placement-specific policy review; do not treat organic and paid posts as interchangeable.
- Explicit SEO/research/clinical consent -> their requested purpose, with appropriate evidence and safeguards.
- Ambiguous service-content request from a service provider -> marketing-oriented organic social copy by default, with a hook, meaningful value proposition, differentiating **verified** information when available, and a specific non-coercive contact/consultation CTA.

**Intent-to-copy acceptance test (mandatory for service marketing):** Before delivery, the Critic must answer: (1) Who is the plausible intended customer? (2) Why should they keep reading? (3) What accurate service-relevant value is conveyed? (4) Why would they contact this provider, without inventing differentiators? (5) What single appropriate next action is offered? A draft that merely lists questions to ask a clinician, general health advice, or neutral educational tips without a genuine service-marketing path **fails requirement/goal fit** and must be revised before release. A medical-service post may include useful education but must not mistake education for the sole requested objective.

**Healthcare guardrail:** Conversion never overrides clinical appropriateness, informed choice, medical accuracy, patient privacy or platform policy. Do not assert that a procedure is needed, target personal health vulnerabilities, promise benefits/safety, or manufacture urgency. When indications cannot be assessed, promote professional evaluation and discussion rather than pressuring patients into a procedure. For intimate services such as circumcision, use discreet, non-graphic language and avoid direct assumptions about the viewer's condition. If provider credentials, prices, location or unique benefits are unverified, omit them instead of fabricating them.

**Cross-tab regression fixture:** Given only "Viết content về dịch vụ nâng ngực" or "Viết content về dịch vụ cắt bao quy đầu" in a known clinic/business context, expected intent is **service marketing**; an education-only list with a generic booking line is an intent-routing failure. Assess hook, authentic interest, truthful service value, specific CTA, clinical/platform risk, and the existing CORE release conditions. Compare a second review under the *same brief* for substantive consistency. A GitHub Skill change alone does **not** prove that a separate chat loaded or executed it; record loading and execution evidence separately, and never claim cross-tab PASS without a witnessed run.

## Mandatory pre-delivery editorial gate

For every substantial marketing/content deliverable, complete the following **before** showing the primary draft to the user, not only after the user asks for a review:
1. **Creator:** produce a candidate using the brief, target audience, platform and desired action.
2. **Critic (separate pass):** assess the actual candidate from three relevant perspectives: (a) Copywriter: hook, clarity, originality, scannability, emotional relevance; (b) Marketing Strategist: audience insight, differentiated value, conversion flow and CTA; (c) domain/policy reviewer when relevant (e.g. medical-aesthetics claims, consent, realistic outcomes, platform restrictions). These are perspectives within one assistant, not independently certified experts.
3. **Editor:** revise the **actual copy** to resolve all Critical/Major issues and material weaknesses; do not merely append an improvement recommendation or replace a weak draft with a QC explanation.
4. **Re-check:** compare the revised copy against the original brief and the Critic findings, confirm that each mandatory fix is present, and look for regressions or newly introduced claims.
5. **Final Auditor:** apply the unchanged CORE seven-category rubric and release gates to the **revised final copy**, not the first candidate. Release as approved only if score >=90/100, zero unresolved Critical/Major and all mandatory evidence/constraints are satisfied; otherwise mark NOT PASS/BLOCKED and state the limitation. Maximum four creation/revision rounds including the initial draft.

For Facebook/social marketing, check specifically: a distinctive truthful opening hook; one clear audience problem or aspiration without personal-attribute targeting; a concrete, supportable reason to read; concise mobile-friendly flow; a specific, low-friction CTA; correct brand/tone; no fabricated price, discount, credentials, patient result, safety guarantee, or fake scarcity. For medical-aesthetic copy, check risk-sensitive wording and do not assert legal or platform compliance without current verification.

**Regression safeguard:** when the user later submits the assistant's own previously delivered copy for critique, treat newly identified substantive weaknesses as evidence of a potential pre-delivery QC miss. Explain the discrepancy, fix the copy, and review whether the pre-delivery gate was executed; do not silently present the second critique as proof that the first draft had passed. A new brief or a change in marketing goals may legitimately change the assessment.

**Right-sized scope:** light one-line copy can use a concise editorial check; substantive posts/ads require the full pass. This is a conditional content-master requirement, not a mandatory three-Skill load, a new CORE scoring dimension, or a requirement for unrelated code, image, video, academic or research tasks. Record execution honestly; do not claim a review or test that was not performed.

## Executable pre-release checklist and audit trace (service marketing)

This is an operational enforcement procedure for the existing editorial gate, not a replacement for CORE or a promise of cross-chat automation.

**No draft-to-user shortcut:** When writing a substantive service-marketing post, do not send the Creator draft as the final answer. Before composing the final answer, keep a compact task-scoped audit record with:
- BRIEF: the user's literal request, inferred intent (conversion vs education), channel assumption and target action.
- CANDIDATE: first full draft and two distinct hook candidates.
- CRITIC: specific passages that fail intent, curiosity/payoff, service relevance, differentiation, authentic engagement, CTA, factual/medical accuracy or platform-risk review. Classify each issue Critical/Major/Minor.
- EDITOR: actual corrected full copy; identify the changes that resolve each blocking issue.
- RECHECK: compare final copy to the original brief and every blocking finding, including new medical/policy claims; mark each RESOLVED / UNRESOLVED / UNVERIFIED.
- FINAL AUDITOR: score the **final corrected copy**, not a hypothetical version, using exactly CORE 25/20/15/15/10/10/5; record technical and domain acceptance, evidence completeness, regression status and PASS / PASS WITH NOTES / NOT PASS / BLOCKED.

**Hard rejection examples:** A clinic service request answered as a neutral list of things to ask a doctor with only a generic booking line; a title that merely says 'đặt lịch ngay' without curiosity or concrete value; a content-free body with no useful service insight; a misleading safety promise; or a generic CTA disconnected from the post. These must trigger actual revision before release, even if the text is medically cautious.

**Release behavior:** Only label an artifact approved when all existing CORE gates are satisfied and score >=90 with no Critical/Major. Do not invent an audit score, claim independent expert review or assert that a different tab executed the Skill. If the audit cannot be completed, clearly label the output provisional or NOT PASS/BLOCKED as applicable. Do not flood the user with internal scoring unless asked; a short evidence-based status is sufficient when relevant.

**Regression verification:** For each reported cross-tab failure, retain the verbatim prompt, returned draft, critique and observed evidence of Skill loading. Distinguish (a) quality failure of returned copy, (b) missing execution evidence and (c) proven Skill-routing failure. A GitHub update or a self-reported score does not demonstrate a cross-tab fix. Re-test the exact prompt in a new chat and review its returned copy before declaring success.

## Conditional medical-aesthetics social content optimization

Activate this checklist when the deliverable promotes or explains aesthetic medicine, cosmetic procedures, body/face enhancement or related consultations on Facebook, Instagram, TikTok or other platforms. Apply it **before** final delivery, as part of the mandatory editorial gate; do not burden unrelated content.

**Attention and interaction (truthful, not manipulative):**
- Draft at least two genuinely different hook angles internally (e.g. a specific curiosity question, a useful myth-versus-fact distinction, a decision-making insight); select the strongest grounded in the actual content. A hook must deliver on its promise, not use false shock, fear, sensational outcomes or unsupported claims.
- Give a meaningful answer or useful insight early; use short mobile-friendly paragraphs and a clear progression from hook to value to one relevant CTA.
- Encourage authentic interaction with a specific optional question tied to aesthetic preferences or educational choices. Avoid engagement bait, compulsory tagging/sharing, fake urgency or fabricated testimonials.
- Optimize for the requested platform and placement; organic post and paid ad are not interchangeable. Do not assert reach, approval, click-through rate or conversion outcomes without actual evidence.

**Risk-sensitive wording and platform review:**
- There is **no universal reliable list of banned words** across platforms. Evaluate the full wording, context, visual creative, landing page and ad objective against the platform's current policies when that verification is available. If not checked, mark platform approval **UNVERIFIED**, never guaranteed.
- Prefer respectful, neutral, non-graphic, medically accurate wording over sensational descriptions. Avoid graphic procedure details when unnecessary, direct assertions about the viewer's body or insecurities, stigmatizing comparisons, unrealistic transformations, guaranteed safety/results, unsubstantiated medical claims, misleading before/after framing and coercive body-image pressure.
- Do not disguise a prohibited claim using misspellings, symbols, euphemisms or code words to evade moderation. Do not omit material risks or make a misleading medical assertion merely to avoid a sensitive term. Use plain alternatives only when they remain accurate (e.g. 'tư vấn lựa chọn phù hợp', 'tìm hiểu phương án', 'quá trình hồi phục' rather than unsupported promises).
- Distinguish educational organic copy, paid advertising and patient information. Necessary informed-consent/risk information must remain accurate even if it is not suitable for a short promotional caption.
- Check brand, claimed expertise, pricing, availability, promotion, results and testimonial permissions against verified inputs; do not invent them.

**Pre-delivery rejection triggers:** generic hook with no specific payoff; unsupported claim; high-risk personal-attribute targeting; misleading medical wording; fabricated urgency/price/results; engagement bait; absent or confusing CTA; or a claim of policy compliance without a current check. Critic identifies each defect; Editor revises the actual copy; Re-check verifies all corrections; Final Auditor applies the unchanged CORE release gate. The goal is strong compliant communication, **not** circumvention of platform enforcement.

## Quality criteria
- Hook earns attention without misleading or relying on empty clickbait.
- Audience insight is specific and relevant.
- Message, value and offer are clear.
- CTA is natural, singular where possible and actionable.
- Voice matches brand, audience and platform.
- Claims are substantiated; no fabricated testimonials, guarantees, credentials or results.
- No deceptive scarcity, fake urgency or disguised sponsorship.
- Content respects platform rules and applicable advertising requirements.
- Copy is natural, concise and not repetitive.

## Critic checklist
Check brief fit, audience fit, factual claims, clarity, differentiation, tone, spelling, length, CTA, prohibited terms, legal/platform risk and whether the copy could be misunderstood. For each defect, state the exact passage, issue, impact and correction.

## Safety and evidence
Do not invent prices, promotions, addresses, medical outcomes, testimonials or business credentials. In health, aesthetics and other regulated areas, avoid guaranteed outcomes, misleading before/after implications and unsupported efficacy claims. Flag claims requiring professional or regulatory review. Do not promise compliance without checking the relevant current policy or law.

## Deliverables
Provide the requested artifact first. Add variants, rationale, hashtags, calendar or QC report only when requested or materially useful. Preserve exact user-provided facts and mark placeholders clearly.

## Related skills
Use research-master for current platform rules, market evidence or substantiation. Use image-master or video-master when a campaign also needs visual assets.

## Mandatory Local QC Gate (runtime enforcement)

This gate applies whenever this specialist Skill is actually loaded; it does not claim universal auto-triggering. Use the canonical `CORE/quality-control.md` (deployed copy: `references/core-rubric.md`); its seven weights 25/20/15/15/10/10/5, zero unresolved Critical/Major, >=90, three release conditions and maximum four creation/revision rounds are unchanged.

- **Light:** one concise accuracy, intent and safety self-check. Do not force full review passes for trivial tasks.
- **Standard:** Creator drafts; Critic reviews the **actual artifact** and records exact passage/defect/severity; Editor corrects; Re-check maps every Major/Critical finding to an observable change and tests regressions; Final Auditor applies the unchanged CORE release conditions. Do not infer a step ran from the existence of a final artifact.
- **Full:** Standard plus an evidence ledger and applicable domain + technical acceptance gates. Mark non-applicable checks N/A with reasons. Required unexecuted checks are NOT RUN and prevent PASS.
- **Evidence discipline:** LOADED != APPLIED != VERIFIED. Record brief, artifact, finding IDs, corrections, re-check result, release decision and any unverified steps. An absent trace cannot be retrospectively invented. A weak final artifact with unresolved Major remains NOT PASS regardless of a self-awarded high score.
- **Reviewer mode:** Default `SINGLE_MODEL_ROLE_PASSES`; use `SEPARATE_WORKER_EXECUTION` only when actual workers were invoked and execution evidence exists. Worker separation alone is not proof of different models or independence.
- **Delivery:** Provide the requested result first and a concise decision/limitations if relevant. Detailed audit evidence is shown when requested; do not claim hidden reasoning is a durable audit log.

**Domain acceptance (content):** The final text must deliver a specific, truthful payoff for its opening, a developed audience-relevant insight (not only a three-item checklist), an appropriate provider/service value proposition without invented differentiators, and a CTA connected to the body. In service marketing, an education-only list plus generic inbox CTA is a **Major** goal-fit failure. Check claims and medical/platform risk separately. Show the exact passage improved for each Major; if unchanged, keep it UNRESOLVED and block PASS.

## T10 negative-control and calibration rule

For a substantial service-marketing deliverable, **do not infer PASS from having a hook, a body, a CTA and cautious claims**. Before scoring, compare the actual final text to the failed T10 rhinoplasty fixture in `TESTS/t10/test_content_gate.py`. A near-paraphrase of the failed generic opening + general harmony advice + clinic consultation + inbox CTA is a **Major** originality/payoff and goal-fit failure, even when the text is safe. Specifically identify what NEW actionable insight or credible service-specific decision factor the final copy gives the reader; without it, keep the Major open. Lack of verified provider differentiators must not be filled with invented ones; the value may be a useful, specific decision framework instead.

If code execution is actually available, `python -m unittest -v TESTS/t10/test_content_gate.py` (run from `TESTS/t10` as working directory) and `python TESTS/t10/content_gate.py <draft-file>` provide **limited deterministic negative controls**, not a semantic quality score or a release authorization. `REVIEW_REQUIRED` means proceed to editorial and CORE audit; it NEVER means PASS. If code was not run, say NOT RUN. Do not claim this screening script automatically executes in ordinary ChatGPT chats.

**Calibration requirement:** A final artifact matching a known failed fixture must never be given 90+ solely because its language is clean and medical claims are cautious. Re-evaluate the goal-fit, depth and practical-value CORE dimensions and cite the concrete improvement. No fixed formula can guarantee compelling marketing copy; reviewer judgment remains necessary.

**Second T10 negative fixture:** A post that opens with 'Một dáng mũi đẹp trên ảnh chưa chắc...' and then asks three preference questions without providing a concrete answer is still a Major value/payoff failure. Treat a series of questions as a prompt for insight, not a substitute for insight. The deterministic screen flags three or more questions with fewer than two concrete service/clinical details as `QUESTIONNAIRE_WITHOUT_PAYOFF`; this is only a heuristic and may false-positive, so manual editorial review is required.

## Changelog
- 1.2.1: Calibrated against second T10 question-list negative fixture; clarified that questions do not constitute a developed payoff.

- 1.2.0: Added T10 negative-control calibration, explicit anti-template rejection and optional deterministic screening.

- 1.1.0: Added tiered local QC gate, evidence-based Major resolution, reviewer-mode disclosure and domain acceptance.

- 1.0.0: Initial versioned release with defined scope, workflow, critique and evidence safeguards.
