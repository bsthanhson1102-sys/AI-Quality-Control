# T10 — Pre-delivery marketing QC regression (2026-11-08)

## Scope and evidence
Status: **NOT PASS — observed artifact fails marketing acceptance**; cross-tab end-to-end Skill execution **NOT VERIFIED**.
Source: user-provided verbatim Facebook rhinoplasty post and AI-QC audit transcript from a separate chat, supplied in this conversation. No external worker logs or original draft were supplied.
GitHub sources read: `CORE/quality-control.md` blob `642b6e098c57a6b73d965f50b69e62f082c34e3f`; `SKILLS/content-master/SKILL.md` blob `f4e1021484c6fce304bfcd8ac931959b9ff9a016`. Registry current blob `93fe72a71a868644c106f05b99c5ca2538807c1a` (1.1.0); this was updated **after** the captured test and must not be misrepresented as its runtime source.

## Original request and returned artifact
Request: write a Facebook post about rhinoplasty, explicitly run AI-QC and provide Skill evidence, Critic defects, Editor fixes and Final Auditor result.
Returned hook: **"Nâng mũi không chỉ là chọn sống mũi cao bao nhiêu."**
Returned body: short general statement about facial harmony; a three-item checklist (desired shape, current nose/prior intervention, options/limits/recovery); generic consultation and engagement CTA.
Returned audit: Registry 1.0.0, content-master 1.0.0, claimed Critic/Editor/Re-check, self-awarded **97/100 PASS WITH NOTES**. No actual initial candidate, before/after diff or tool-execution log supplied.

## Critic findings against actual returned copy
- **T10-M01 MAJOR — Service-marketing intent not achieved:** content is primarily neutral consultation advice with a generic inbox CTA, despite service-marketing default in content-master. Fix: audience-specific but respectful service value, reason to contact provider without inventing differentiators, and coherent conversion path.
- **T10-M02 MAJOR — Hook/payoff mismatch and inadequate depth:** hook raises the choice of nose height versus harmony, but does not develop an insight, example or decision framework; body becomes a three-item checklist. Fix: deliver a concrete, useful explanation tied to the hook, preserving medical accuracy.
- **T10-M03 MAJOR — Audit resolution unsupported:** audit says Editor improved generic hook and content depth, yet the final artifact retains those substantive weaknesses; no candidate/diff available. Fix: preserve verifiable candidate/finding/revision/re-check evidence and block release if Major remains.
- **T10-m04 MINOR — Generic CTA and engagement question:** weak provider-specific reason to inquire; avoid fabricated service claims.
- **T10-S05 SAFETY POSITIVE:** no fabricated prices, guaranteed results, credentials or urgency. Paid-ad platform approval was correctly not claimed.

## CORE artifact score (reviewer assessment, not objective measurement)
Requirement/goal fit **18/25**; accuracy/evidence **19/20**; completeness/depth **8/15**; logic **13/15**; usefulness **6/10**; language **8/10**; format **5/5** = **77/100**. A different reviewer may score differently; regardless, unresolved M01–M03 block PASS even at >=90.

## Process vs artifact
- Process conformance: **PARTIAL / UNVERIFIED**. Returned report lists expected roles and matching historical file SHAs, but actual source reads, candidate and edit trace in that other tab were not independently observed.
- Artifact quality: **NOT PASS** due to unresolved Major findings.
- Original self-awarded 97/100: **not accepted as evidence of release approval**.
- Creator/Editor fixes in this audit: **NOT RUN**. This report is a regression diagnosis, not a fifth revision of the captured post.
- Live cross-tab runtime test: **NOT RUN**. A new chat must be witnessed separately.

## Next reproducible acceptance tests
1. With identical prompt and context, save raw first candidate, Critic findings, revised copy and before/after diff; reject if any finding is still present.
2. Negative fixture: deliberately use the captured weak copy and a fabricated 97/100; expected decision NOT PASS regardless of score.
3. Positive fixture: a substantive, factually restrained post with documented corrections, no unresolved Major, full 7-part score and applicable evidence; expected PASS only if all three CORE gates satisfied.
4. Offline deployment: verify script runs on a real local checkout, copies only active skills and rejects snapshot drift. NOT RUN in this session (GitHub network resolution failed in container).
5. Runtime discovery: check actual Codex or target runtime can load specialist skill and router. NOT RUN.
6. Record environment, versions, source hashes, actual output and limitations. Do not conflate repository changes with verified cross-tab behavior.

## Decision
**T10 NOT PASS (artifact); runtime installation and independent process evidence NOT RUN/UNVERIFIED.** No CORE thresholds or weights changed. No automatic skill activation claimed.
