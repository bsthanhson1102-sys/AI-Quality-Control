# T01 — Content Master: Facebook campaign post

**Test date:** 2026-11-06  
**Runtime:** ChatGPT  
**Repository:** `bsthanhson1102-sys/AI-Quality-Control`  
**Branch/ref:** `main`

## 1. Intake and routing

**Test prompt:** Create a Facebook campaign post for a fictional business using only business facts supplied in the prompt. Mark missing facts; do not invent prices, promotions, credentials, results, testimonials or scarcity. Define audience, message angle and CTA. Perform Critic, Editor and Final Audit.

**Expected routing:** Primary `content-master`; no secondary by default.

**Actual routing:** Primary `content-master`; Secondary: none. Correct routing.

## 2. Retrieved sources

| Source | Version/status | Path | File blob SHA |
|---|---|---|---|
| Registry | 1.0.0 | `REGISTRY/skills-registry.yml` | `e38086d765fae7e0895ae95bf777da23de146315` |
| Content Master | 1.0.0 / active | `SKILLS/content-master/SKILL.md` | `76363011479ed0342c3489d2f23b4b67fc8ec93d` |
| Test suite | — | `TESTS/skill-routing-test-suite.md` | `b9ddf3fd7d701efd9046dc9f788bdadcfba5e109` |
| CORE rubric | — | `CORE/quality-control.md` | `6b1de5d165912344d9f096d48c1fc81196cb1274` |

These are file blob SHAs, not commit SHAs.

## 3. Intake finding and acceptance criteria

The test prompt supplies no concrete business facts: no business name, product/service, offer, price, location, contact channel, credentials, results or testimonials.

Acceptance criteria:
1. Produce a Facebook post draft and define audience, message angle and CTA.
2. Preserve supplied facts; do not invent missing business facts.
3. Clearly mark unknowns/placeholders.
4. Do not invent offer details, testimonials, credentials, substantiation or scarcity.
5. Critic identifies exact defects and corrections.
6. Editor revises; Final Auditor checks the final version.
7. Do not claim current Meta/legal compliance without a current policy/legal check.

## 4. Creator artifact

**Audience:** people considering a product or service in the business's as-yet-unspecified category. This is a broad strategic audience assumption, not a supplied business fact.

**Message angle:** encourage informed consideration and request for information.

**CTA:** comment or send a message to request information.

**Draft:**

> **[TÊN DOANH NGHIỆP] — [THÔNG ĐIỆP CHÍNH]**
>
> Bạn đang tìm hiểu về **[TÊN SẢN PHẨM/DỊCH VỤ]**?
>
> Hãy bắt đầu bằng việc xác định nhu cầu, tìm hiểu thông tin và cân nhắc những yếu tố quan trọng trước khi lựa chọn.
>
> 📩 Bạn muốn tìm hiểu thêm về **[TÊN SẢN PHẨM/DỊCH VỤ]**? Hãy để lại bình luận hoặc gửi tin nhắn để được cung cấp thông tin.
>
> **Thông tin cần bổ sung trước khi đăng:**
> - [Tên doanh nghiệp]
> - [Sản phẩm/dịch vụ cụ thể]
> - [Thông tin hoặc lợi ích đã được xác minh]
> - [Kênh liên hệ chính thức]
>
> Các nội dung trong ngoặc vuông là chỗ trống cần điền, không phải thông tin đã được xác minh.

## 5. Independent Critic

**C1 — Minor: unsupported brand commitment in first draft.**
- Affected passage: “Tại [TÊN DOANH NGHIỆP], chúng tôi muốn giúp bạn tiếp cận thông tin rõ ràng…”
- Reason: the prompt did not supply this brand promise.
- Impact: attributes an unverified service commitment to the fictional business.
- Correction: removed the sentence and replaced it with neutral wording.
- Status: fixed.

**C2 — Major for publication readiness: essential business facts are absent.**
- Affected areas: business identity, product/service, verified differentiator and contact details.
- Reason: none are supplied by the test prompt.
- Impact: a reader cannot identify what is being promoted or how to verify the offer; publishing would require invented content or placeholders.
- Correction: retain explicit placeholders; do not publish until real facts are supplied.
- Status: remains blocked by missing input; not silently filled.

No current Meta policy or legal compliance claim was made.

## 6. Editor and regression re-check

Editor removed the unsupported brand promise, kept the CTA generic, and clearly labelled all required missing information.

Re-check:
- No prices, discounts, scarcity, credentials, results or testimonials were invented.
- Placeholders remain visibly marked.
- The revised post does not imply that a rendered campaign asset or platform compliance review exists.
- No regression identified.

## 7. Final Audit and canonical artifact score

| CORE criterion | Score | Rationale |
|---|---:|---|
| Requirement and goal fit | 24/25 | Facebook draft, audience, angle and CTA supplied |
| Accuracy and evidence | 20/20 | No invented business facts; unknowns explicitly marked |
| Completeness and depth | 13/15 | Safe template is complete as a template, but cannot be a publish-ready campaign without facts |
| Logic and consistency | 15/15 | CTA and neutral message are consistent |
| Practical usefulness | 8/10 | Useful starting draft; needs business details before use |
| Language and presentation | 9/10 | Clear and concise, intentionally generic |
| Format and constraint compliance | 5/5 | Facebook post format and all stated prohibitions respected |
| **Total** | **94/100** | |

**Process conformance:** PASS. Registry and full Skill were retrieved; routing matched; acceptance criteria were defined; Creator, Critic, Editor and Final Auditor passes were completed; revisions were re-checked.

**Artifact decision:** BLOCKED for publication because essential business facts were not supplied. The 94/100 score evaluates the safe placeholder draft, not a publish-ready campaign. This is not a PASS or PASS WITH NOTES approval for publishing.

## 8. Unverified items

- No actual business facts were provided, so the campaign cannot be made business-specific.
- No current Meta advertising policy or applicable legal review was performed; no compliance claim is made.
- No paid campaign, audience targeting setup or ad delivery was executed.

## 9. Repository changes

This report is a separate new test record. No Registry or Skill file was modified.
