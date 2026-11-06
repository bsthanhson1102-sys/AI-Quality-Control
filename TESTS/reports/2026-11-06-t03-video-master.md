# T03 — Video Master: 20-second vertical wellness video

**Test date:** 2026-11-06  
**Runtime:** ChatGPT  
**Repository:** `bsthanhson1102-sys/AI-Quality-Control`  
**Branch/ref:** `main`

## 1. Intake and routing

**Test prompt:** Develop a 20-second vertical 9:16 social video for a fictional wellness brand. Deliver a timed storyboard, shot descriptions, voice-over, on-screen text, sound/edit notes and a loop or ending strategy. Critique pacing, clarity, feasibility and platform fit; revise weak points. State whether the result is rendered video or only a production plan.

**Expected routing:** Primary `video-master`; secondary `content-master` only if separate caption/campaign copy is requested; `research-master` if current factual claims need checking.

**Actual routing:** Primary `video-master`; no secondary. Correct routing; no external factual claims were required.

## 2. Retrieved sources

| Source | Version/status | Path | File blob SHA |
|---|---|---|---|
| Registry | 1.0.0 | `REGISTRY/skills-registry.yml` | `e38086d765fae7e0895ae95bf777da23de146315` |
| Video Master | 1.0.0 / active | `SKILLS/video-master/SKILL.md` | `9cf6206479af46e2e1f7903f51040a53eca2210a` |
| Test suite | — | `TESTS/skill-routing-test-suite.md` | `b9ddf3fd7d701efd9046dc9f788bdadcfba5e109` |
| CORE rubric | — | `CORE/quality-control.md` | `6b1de5d165912344d9f096d48c1fc81196cb1274` |

These are file blob SHAs, not commit SHAs.

## 3. Acceptance criteria

1. Vertical 9:16 format and exactly 20 seconds.
2. Timestamped storyboard with shot descriptions.
3. Voice-over and on-screen text align with visuals.
4. Sound/edit notes are actionable.
5. Loop or ending strategy is explicit.
6. No unsupported factual or wellness outcome claims.
7. Critic findings are actionable; Editor revises and re-checks.
8. Clearly distinguish a rendered video from a text-only production plan.

## 4. Creator artifact

**Concept:** “A short pause in a busy day” for a fictional wellness brand.

**Final revised storyboard:**

| Time | Visual / shot | Voice-over | On-screen text |
|---|---|---|---|
| 0–3s | Close-up: person pauses work and looks away from the screen | “Bận rộn? Nghỉ một chút nhé.” | Bận rộn? Nghỉ một chút |
| 3–7s | Medium shot: person places both feet steadily on the floor | “Ngồi thoải mái, đặt chân xuống sàn.” | 01 · Ngồi thoải mái |
| 7–12s | Close-up of shoulders; person rolls shoulders gently | “Thả lỏng vai, chuyển động nhẹ nhàng.” | 02 · Thả lỏng vai |
| 12–17s | Side angle: person looks away from screen and breathes naturally | “Rời mắt khỏi màn hình, hít thở tự nhiên.” | 03 · Tạm rời màn hình |
| 17–20s | Return to camera angle, pose and lighting similar to opening shot | “Lưu lại cho lần nghỉ sau.” | Lưu lại · Nghỉ một chút |

**Sound and edit notes**
- Soft background music, preferably original or appropriately licensed.
- Voice-over stays clearly above the music.
- Use gentle transitions and avoid distracting effects.
- Large, high-contrast captions inside 9:16 safe areas.
- Match the final frame's camera position, pose and lighting to the opening for a loop.

## 5. Independent Critic

**C1 — Minor: opening hook too long for three seconds.**
- Affected passage: initial voice-over “Đang bận? Hãy dành một khoảnh khắc cho bản thân.”
- Impact: may be rushed and reduce first-frame clarity.
- Correction: “Bận rộn? Nghỉ một chút nhé.”
- Status: fixed.

**C2 — Minor: loop point insufficiently specified.**
- Impact: ending could feel abrupt when replayed.
- Correction: return to camera angle, pose and lighting similar to the opening shot.
- Status: fixed.

**C3 — Enhancement: music rights.**
- Correction: specify original or appropriately licensed music rather than assuming popular audio is reusable.
- Status: addressed in sound notes.

## 6. Editor and re-check

- Total timing: 3 + 4 + 5 + 5 + 3 = **20 seconds**.
- Aspect ratio: vertical 9:16.
- Each scene includes a visual, voice-over and on-screen text.
- Voice-over length is proportionate to each proposed duration.
- Loop/ending instructions are explicit.
- No efficacy, medical or health outcome claim is made.
- Music licensing is flagged.
- No regression identified.

## 7. Final Audit and canonical artifact score

| CORE criterion | Score | Rationale |
|---|---:|---|
| Requirement and goal fit | 25/25 | All requested video-plan elements included |
| Accuracy and evidence | 20/20 | No unsupported factual or wellness claims |
| Completeness and depth | 15/15 | Five timed scenes, VO, text, shot and edit notes |
| Logic and consistency | 15/15 | Timing totals exactly 20 seconds; loop is coherent |
| Practical usefulness | 9/10 | Actionable plan; requires production assets and editing |
| Language and presentation | 9/10 | Concise Vietnamese copy and clear production directions |
| Format and constraint compliance | 5/5 | 9:16, 20 seconds and all requested fields |
| **Total** | **98/100** | |

**Process conformance:** PASS. Registry and Skill were retrieved; routing matched; criteria were defined; Critic, Editor and Final Auditor passes were completed.

**Artifact decision:** PASS WITH NOTES. The storyboard/production plan meets the brief. No rendered video or export was created; the score applies only to the production plan.

## 8. Unverified items

- No rendered footage, voice recording, music track or final edit was produced or inspected.
- Actual pacing, subtitle safe-area rendering, audio mix, continuity and export quality remain unverified until production.
- Music license must be checked for the chosen track before publication.

## 9. Repository changes

This report is a separate new test record. No Registry or Skill file was modified.
