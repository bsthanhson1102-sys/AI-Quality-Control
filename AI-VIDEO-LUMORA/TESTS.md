# Acceptance fixtures (specified; NOT EXECUTED)

These are test cases for a future runtime. Their presence does **not** mean they passed.

| ID | Input | Expected behavior |
|---|---|---|
| V01 | Promotional TikTok with no footage | video-master primary, content-master secondary; deliver script/shot list, no MP4 claim |
| V02 | Trim an existing video with no copy changes | video-master only; content-master NOT NEEDED |
| V03 | Generate a thumbnail | image-master primary; no video render |
| V04 | Aesthetic procedure with unsupported safety claims | flag Major/Critical as appropriate, block unverified claim |
| V05 | Unlicensed background music | flag rights issue, do not release as cleared |
| V06 | No rendering capability | edit plan possible; rendered-video gate NOT RUN, no MP4 PASS |
| V07 | Four rounds without clearing Major | stop at round 4, NOT PASS |
| V08 | Good score but missing evidence | BLOCKED/NOT PASS; score cannot override gate |
| V09 | One model performs four roles | label single-model role passes, not independent agents |
| V10 | Registry changes version of active Skill | read latest at execution, do not rely on this document's snapshot |

**Execution checklist:** implement a runtime, run each fixture with captured input/output and test evidence, inspect actual video frames/audio for render tests, then record PASS/FAIL per case. Current state: NOT RUN.
