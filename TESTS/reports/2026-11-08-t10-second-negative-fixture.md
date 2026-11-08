# T10 second negative fixture — 2026-11-08

## User authorization and baseline
User approved adding the most recent weak rhinoplasty Facebook post as a second negative regression fixture. The post starts "Một dáng mũi đẹp trên ảnh chưa chắc..." and asks three preference questions, without developing a concrete service payoff. Prior editorial review rated it 75/100 (not a deterministic ground-truth metric).

## Changes committed
- Added `WEAK_SECOND` to `TESTS/t10/test_content_gate.py` with `test_reject_second_t10_fixture`, expecting BLOCK and `QUESTIONNAIRE_WITHOUT_PAYOFF`.
- Added conservative question-list heuristic to `TESTS/t10/content_gate.py`: three or more question marks AND fewer than two concrete service-detail terms triggers a Major editorial-screening finding. This is NOT semantic proof and can false-positive or false-negative.
- Updated content-master to 1.2.1 with explicit second-fixture calibration; Registry to 1.3.1, offline snapshot and deployment pin synchronized. Canonical CORE unchanged.

## Evidence
- Red/green local regression on a locally reconstructed equivalent of the screening rule and second fixture: initial test FAIL (missing finding), after change PASS (1 test). This does NOT establish that the complete GitHub test suite was executed.
- GitHub readback VERIFIED: second fixture and test present, gate includes new finding, Skill version 1.2.1, Registry 1.3.1, snapshot content matches Registry plus header, deploy script contains Registry blob SHA `448af3a4aa78803a073806d5fff5bb813f5ae727`.
- Full repository unit suite: NOT RUN. Cross-tab Skill execution: NOT RUN. Independent Worker: NOT RUN. Quality improvement on a fresh output: NOT RUN.

## Critic / Editor / Re-check / Final Auditor
- Creator: added second negative fixture and test.
- Critic: found old screen only blocked via LOW_SERVICE_DETAIL and did not identify questionnaire-without-payoff explicitly; warned that regex can be gamed.
- Editor: added specific conservative questionnaire heuristic and Skill acceptance wording.
- Re-check: local reconstructed red/green regression plus GitHub readback.
- Final Auditor: source consistency VERIFIED; T10 end-to-end still NOT PASS pending full suite and observed new-tab regression. No runtime deployment or multi-agent execution claim.
