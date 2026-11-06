# AI-QC T07 — Cross-skill Video + Research Test Report

**Test ID:** T07  
**Run date:** 2026-11-06  
**Runtime:** ChatGPT with connected GitHub repository and web access  
**Repository:** `bsthanhson1102-sys/AI-Quality-Control`  
**Branch:** `main`

## 1. Test scenario

Research a current public-health recommendation from official sources and turn the verified findings into a 30-second vertical educational video script with storyboard and on-screen text. Cite the source for each material factual claim, then critique both evidence quality and video clarity.

**Research topic selected:** WHO physical-activity recommendations for adults aged 18–64 years.

**Deliverable:** Vietnamese 30-second, 9:16 educational video script and storyboard. This is a production plan, not a rendered video.

## 2. Routing and retrieval evidence

**Expected routing**
- Primary: `video-master`
- Secondary: `research-master`

**Actual routing:** PASS. The final deliverable is a video script/storyboard, so `video-master` is Primary. Current public-health facts require verification, so `research-master` is the necessary Secondary Skill.

**Registry**
- Version: 1.0.0
- Path: `REGISTRY/skills-registry.yml`
- Status of both selected Skills: active
- Registry file blob SHA: `e38086d765fae7e0895ae95bf777da23de146315`

**Primary Skill**
- ID: `video-master`
- Version: 1.0.0
- Path: `SKILLS/video-master/SKILL.md`
- File blob SHA: `9cf6206479af46e2e1f7903f51040a53eca2210a`

**Secondary Skill**
- ID: `research-master`
- Version: 1.0.0
- Path: `SKILLS/research-master/SKILL.md`
- File blob SHA: `9cdb7355ade7e00b06290b2cc3047a99dd49063a`

**CORE Quality Control**
- Path: `CORE/quality-control.md`
- File blob SHA: `6b1de5d165912344d9f096d48c1fc81196cb1274`

**Test specification**
- Path: `TESTS/skill-routing-test-suite.md`
- File blob SHA: `b9ddf3fd7d701efd9046dc9f788bdadcfba5e109`

All listed SHA values are file blob SHAs, not commit SHAs.

## 3. Research question and scope

**Question:** What weekly physical-activity recommendations does WHO make for adults aged 18–64, and what does WHO advise people to do if they are not currently meeting those recommendations?

**Scope:** WHO's 2020 evidence-based physical-activity guideline for adults aged 18–64, checked against WHO's fact sheet updated 2026-11-04.

**Access date:** 2026-11-06.

## 4. Verified findings and claim-to-source mapping

### F1 — Aerobic physical activity

WHO recommends that adults aged 18–64 undertake at least 150–300 minutes of moderate-intensity aerobic physical activity per week, or at least 75–150 minutes of vigorous-intensity aerobic physical activity, or an equivalent combination throughout the week.

**Source:** World Health Organization, *WHO Guidelines on Physical Activity and Sedentary Behaviour* (2020).  
**Direct URL:** https://iris.who.int/bitstream/handle/10665/336656/9789240015128-eng.pdf?sequence=1  
**Relevant sections:** Executive summary, adults aged 18–64, printed pp. 4–5; Chapter “Adults (aged 18–64 years) — Physical activity recommendation”, p. 32.  
**Access date:** 2026-11-06.  
**Evidence strength as reported by WHO:** Strong recommendation, moderate certainty evidence.

### F2 — Muscle strengthening

WHO recommends that adults also perform muscle-strengthening activities at moderate or greater intensity, involving all major muscle groups, on 2 or more days per week.

**Source:** Same WHO guideline (2020).  
**Direct URL:** https://iris.who.int/bitstream/handle/10665/336656/9789240015128-eng.pdf?sequence=1  
**Relevant sections:** Executive summary, adults aged 18–64, printed pp. 4–5; adult physical-activity recommendation, p. 32.  
**Access date:** 2026-11-06.  
**Evidence strength as reported by WHO:** Strong recommendation, moderate certainty evidence.

### F3 — Starting from current ability

WHO states that doing some physical activity is better than doing none. Adults who are not meeting the recommendations can benefit from doing some activity and should start with small amounts, then gradually increase frequency, intensity and duration.

**Source 1:** World Health Organization, *WHO Guidelines on Physical Activity and Sedentary Behaviour* (2020).  
**Direct URL:** https://iris.who.int/bitstream/handle/10665/336656/9789240015128-eng.pdf?sequence=1  
**Relevant section:** Executive summary, adult recommendations and good-practice statements, printed p. 5.  
**Access date:** 2026-11-06.

**Source 2:** World Health Organization, “Physical activity”, fact sheet updated 2026-11-04.  
**Direct URL:** https://www.who.int/news-room/fact-sheets/detail/physical-activity  
**Update date:** 2026-11-04.  
**Access date:** 2026-11-06.  
**Relevant section:** “How much physical activity is recommended?”

### Source appraisal and limitations

- Both sources are primary WHO publications.
- The 2020 guideline is the source for the specific dose and frequency recommendations. The 2026 fact sheet confirms that WHO continues to direct readers to the global guidelines and reiterates that any amount of activity is better than none.
- The two documents are from the same organization and are not independent external corroboration.
- The scope is adults aged 18–64. This video must not be presented as an individualized exercise prescription for every person, age group or clinical condition.
- No claim is made that meeting these targets guarantees prevention or treatment of a particular disease.

## 5. Creator deliverable — final 30-second storyboard

**Format:** 9:16 vertical  
**Duration:** 00:30 exactly  
**Language:** Vietnamese  
**Audience:** General adult audience; recommendation scope explicitly limited to ages 18–64  
**Style:** Clear, calm, energetic educational explainer  
**Assets:** Proposed stock/recorded exercise scenes or simple motion graphics. No source footage was supplied or inspected.  
**Audio:** Original voice-over; use licensed or original background music only.

| Time | Visual / shot | Voice-over | On-screen text | Evidence |
|---|---|---|---|---|
| 00:00–00:03 | Close-up of a weekly calendar; numbers animate in | “Người trưởng thành cần vận động bao nhiêu mỗi tuần?” | “Mỗi tuần cần vận động bao nhiêu?” | Framing question; no factual claim |
| 00:03–00:10 | Calendar fills with highlighted activity blocks; show “18–64 tuổi” clearly | “Với người từ 18 đến 64 tuổi, WHO khuyến nghị 150 đến 300 phút vận động aerobic cường độ vừa mỗi tuần.” | “18–64 tuổi” / “150–300 phút/tuần” / “Cường độ vừa” | F1 |
| 00:10–00:16 | Graphic switches to a second route with a stronger activity icon; keep both options visually distinct | “Hoặc 75 đến 150 phút cường độ mạnh, hay kết hợp hai mức tương đương.” | “HOẶC 75–150 phút/tuần” / “Cường độ mạnh” / “Có thể kết hợp tương đương” | F1 |
| 00:16–00:21 | Simple animation highlights major muscle groups; no exaggerated body transformation | “Đừng quên tập tăng cường các nhóm cơ chính, ít nhất hai ngày mỗi tuần.” | “Tập tăng cường cơ” / “≥ 2 ngày/tuần” | F2 |
| 00:21–00:27 | Person begins with a short walk, then a calendar shows gradual progression | “Nếu chưa đạt mục tiêu, hãy bắt đầu từ mức nhỏ và tăng dần. Một chút vẫn tốt hơn không.” | “Bắt đầu từ mức phù hợp” / “Tăng dần” | F3 |
| 00:27–00:30 | Clean end card with WHO source attribution in small readable type | “Lưu lại để tham khảo và chọn cách vận động phù hợp với mình.” | “Lưu lại • Chia sẻ” / “Nguồn: WHO, 2020; cập nhật thông tin 04/11/2026” | CTA; source attribution |

### Suggested caption

WHO khuyến nghị người trưởng thành 18–64 tuổi đạt 150–300 phút vận động aerobic cường độ vừa hoặc 75–150 phút cường độ mạnh mỗi tuần (hoặc kết hợp tương đương), đồng thời tập tăng cường các nhóm cơ chính ít nhất 2 ngày/tuần. Nếu chưa đạt, hãy bắt đầu từ mức nhỏ và tăng dần.

Nguồn:
- WHO, *Guidelines on Physical Activity and Sedentary Behaviour* (2020), phần người trưởng thành 18–64 tuổi, tr. 4–5 và 32: https://iris.who.int/bitstream/handle/10665/336656/9789240015128-eng.pdf?sequence=1
- WHO, “Physical activity”, cập nhật 04/11/2026: https://www.who.int/news-room/fact-sheets/detail/physical-activity

*Thông tin giáo dục sức khỏe chung, không thay thế tư vấn cá nhân từ nhân viên y tế.*

## 6. Independent Critic findings

**V1 — Major: Risk of collapsing the recommendation into a single daily-minute rule.**  
A simplified “30 minutes every day” line would omit the alternative vigorous-intensity range and equivalent combinations.  
**Impact:** The video could misstate the guideline.  
**Correction:** Retained the full weekly ranges and explicit “or equivalent combination” wording.  
**Status:** FIXED.

**V2 — Major: Population scope could be misunderstood as universal.**  
The recommendation is specifically presented for adults aged 18–64.  
**Impact:** Viewers outside this age group or with individual clinical limitations could mistake it for personalized advice.  
**Correction:** Display “18–64 tuổi” in the same scene as the numeric recommendation and include a general-health disclaimer in the caption.  
**Status:** FIXED.

**V3 — Minor: Numeric density could reduce comprehension in a 30-second format.**  
The two aerobic alternatives and strength-training frequency create several numbers.  
**Impact:** Viewers may not retain the recommendation.  
**Correction:** Separate moderate and vigorous alternatives into different scenes, keep each numeric range on screen, and use a dedicated strength-training scene.  
**Status:** FIXED.

**V4 — Minor: Visuals could imply a guaranteed body transformation.**  
**Impact:** A before/after or dramatic physique visual would introduce an unsupported implication.  
**Correction:** Use neutral activity/calendar graphics and avoid transformation imagery.  
**Status:** FIXED.

## 7. Editor changes and regression re-check

- Preserved all WHO numeric ranges and the equivalent-combination qualification.
- Kept the target age range visible.
- Separated aerobic and muscle-strengthening recommendations.
- Added gradual-start guidance without implying a personalized prescription.
- Attached source IDs to each factual scene.
- Checked timeline arithmetic: 3 + 7 + 6 + 5 + 6 + 3 = 30 seconds.
- Checked that the deliverable is a storyboard/script only; no rendered video or source-footage inspection is claimed.
- Checked that music and footage must be original or appropriately licensed.

**Regression re-check:** PASS for the listed content, evidence mapping, timing and output-format constraints.

## 8. Final audit

| Acceptance criterion | Result |
|---|---|
| Primary skill follows final deliverable | PASS — video-master |
| Secondary skill is necessary and justified | PASS — research-master |
| Both complete registered Skills retrieved | PASS |
| Current recommendation checked against official sources | PASS |
| Each material factual claim mapped to evidence | PASS |
| Population and recommendation scope are clear | PASS |
| Script does not exceed source support | PASS |
| 30-second timing is internally consistent | PASS |
| 9:16 vertical production requirements stated | PASS |
| Critique and revision performed | PASS |
| Rendered video distinguished from production plan | PASS |

### Canonical artifact score

| Criterion | Score |
|---|---:|
| Requirement and goal fit | 25/25 |
| Accuracy and evidence | 20/20 |
| Completeness and depth | 14/15 |
| Logic and consistency | 15/15 |
| Practical usefulness | 9/10 |
| Language and presentation | 9/10 |
| Format and constraint compliance | 5/5 |
| **Total** | **97/100** |

**Process conformance:** PASS for T07 in this ChatGPT runtime.

**Final artifact decision:** PASS WITH NOTES.

**Notes:** The output is a production-ready script/storyboard, not a rendered video. The guideline is general population guidance for ages 18–64 and is not individualized medical advice. The WHO guideline and fact sheet are authoritative but originate from the same organization.

## 9. Suite status after T07

| Test | Status |
|---|---|
| T01–T04 | PASS per existing smoke-test report; not re-run in this T07 session |
| T05 | PASS WITH NOTES — separate re-check report created |
| T06 | PASS per existing smoke-test report; not re-run in this T07 session |
| T07 | PASS WITH NOTES — executed in this run |
| T08 | NOT RUN |
| T09 | NOT RUN |

**Suite decision: NOT COMPLETE.** T07 does not certify T08 or T09 and does not constitute a full T01–T09 regression pass.

**No video media was rendered or exported.**
