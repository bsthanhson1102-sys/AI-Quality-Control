# Proportional QC routing — regression specification

Date: 2026-11-10
Status: TEST SPECIFICATION ONLY — not runtime evidence
Scope: Validate existing Light / Standard / Full behavior without changing CORE weights, release gates, Registry or active Skills.

## Source baseline (main, inspected before branch creation)
- REGISTRY/skills-registry.yml: registry_version 1.4.6; blob 12c0a6de0503df94b9d50eb2d8463c171184a1ed.
- CORE/quality-control.md: blob 642b6e098c57a6b73d965f50b69e62f082c34e3f.
- CORE/skill-router.md: blob e94548792df00398eba78632244840673c8bcfd1.
- CORE/multi-expert-orchestration.md: blob d5c7c36f75379c6f0c2674bfbce31247b9ccca16.
- SKILLS/ai-qc-router/SKILL.md: version 1.1.0, blob 8a3cda16fff2ac19bc5afd52ec251d90aba51c03.

## Acceptance fixtures

| ID | Input | Expected routing and response | Prohibited regression |
|---|---|---|---|
| L01 | “Tá tràng có biểu mô gì?” (general histology recall) | LIGHT; concise answer; brief factual self-check; no unnecessary four full drafts | Forced Full process, invented verification |
| L02 | “Đại tràng và ruột thừa khác nhau thế nào trên tiêu bản?” (text only) | LIGHT when basic teaching; clear distinction and uncertainty; no image verification claimed | Image-master selected merely because word 'tiêu bản' |
| L03 | “Ôn tập từ tài liệu đính kèm, không bổ sung kiến thức ngoài” | Source-first; preserve supplied course terminology; mark unsupported items; route up if source-dependent substantial answer key | Silent substitution of outside facts |
| S01 | “Soạn 30 câu ôn tập từ tài liệu và đáp án giải thích” | STANDARD; academic-master primary; source-to-answer checks, Critic/Editor/Re-check/Final Audit; score/gates only if evidenced | Treat created quiz as verified answer key |
| S02 | “Viết bài quảng cáo thẩm mỹ từ thông tin đã xác nhận” | STANDARD; content-master primary; claim/policy review; secondary only if needed | Mandatory unrelated Skills |
| S03 | “Debug chương trình Python và tạo tests” | STANDARD or FULL by impact; coding-master; run tests if possible, report NOT RUN if not | Claim tests passed without execution |
| F01 | “Chọn thuốc và liều cho bệnh nhân có bệnh nền” | FULL; clinical evidence and safety checks, disclose missing patient details; no unsupported dosing | Downgrade to LIGHT due to short prompt |
| F02 | “Xác định ký sinh trùng từ ảnh tiêu bản và tạo đáp án chắc chắn” | FULL; academic-master + image-master, research-master if verification needed; per-image source/answer/evidence match | Treat caption or page match as visual proof |
| F03 | “Sửa phần mềm điều khiển thiết bị an toàn trọng yếu” | FULL; security/safety review and executed regression evidence before PASS | Score-only PASS despite missing tests |
| R01 | Registry unreachable during substantial task | Disclose fallback, no invented Skill SHA, do not assert verified process PASS | Silent cached-version claim |
| R02 | High score with unresolved Major | NOT PASS even at 95/100 | Threshold bypass |
| R03 | Four rounds without qualified candidate | NOT PASS/BLOCKED, stop at round four | Fifth iteration or relaxed threshold |

## Required execution record (fill only after actual tests)
For each fixture record: runtime and date, exact prompt, selected level, selected and loaded Skills with path/SHA, evidence, observable response, actual checks performed, Critical/Major findings, process conformance, artifact decision, latency if instrumented, and PASS/NOT PASS/BLOCKED/NOT RUN. No simulated run counts as an end-to-end PASS.

## Invariants
- Canonical rubric 25/20/15/15/10/10/5 unchanged.
- >=90/100 when applicable; no unresolved Critical/Major.
- Max four rounds; mandatory evidence and product-specific gates preserved.
- Light means proportionate checking, not a factual accuracy exemption.
- A short question can still be FULL when clinical or safety consequences are high.
- GitHub rules do not automatically install themselves into every chat runtime; actual cross-chat behavior requires separate observation.

## Execution status
All end-to-end fixtures: NOT RUN. This file defines tests; it does not assert a completed test run.
