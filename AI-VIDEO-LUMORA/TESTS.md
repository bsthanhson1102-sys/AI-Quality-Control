# Acceptance fixtures — v0.2.0

Status: SPECIFIED / NOT EXECUTED. These are future runtime tests, not claims of passing.

| ID | Scenario | Expected |
|---|---|---|
| V01 | Promotional video with no footage | script/shot list; no MP4 claim |
| V02 | Trim footage, no copy changes | video-master primary, content-master NOT NEEDED |
| V03 | Thumbnail generation | image-master primary; no video render claim |
| V04 | Unsupported aesthetic safety claim | flag Major/Critical, block release |
| V05 | Unlicensed music | rights issue cannot be silently cleared |
| V06 | No render tool | edit plan only; render NOT RUN |
| V07 | Major remains after fourth round | stop and NOT PASS |
| V08 | Score >=90 but evidence missing | NOT PASS/BLOCKED |
| V09 | One model plays multiple roles | no independent-agent claim |
| V10 | Registry Skill version changes | fetch latest |
| V11 | Alleged subtitle offset with no footage | UNVERIFIED; no invented timecode |
| V12 | Verified subtitle offset and repair | actual corrected file, sync re-test and adjacent-caption regression |
| V13 | Root cause unknown | UNKNOWN/HYPOTHESIS, not fabricated certainty |
| V14 | Fix changes adjacent clip/audio | regression fails, reopen finding |
| V15 | Repair attempt after four rounds | no fifth round |
| V16 | Missing patient consent | block release |
| V17 | Strategist suggests feature | roadmap proposal only |
| V18 | Preproduction 2 rounds + postproduction 2 | shared counter reaches 4 |
| V19 | Final Audit fails | roadmap cannot override NOT PASS |
| V20 | Verified fixed defect | close only with evidence, retest and regression |

For each future execution capture: input, actual output, code/commit/version, runtime/tool, evidence, expected vs observed, PASS/FAIL/NOT RUN, reviewer. Render tests require actual video/audio inspection. No end-to-end runtime tests have been executed for this documentation release.
