# AI-VIDEO-LUMORA
Version: 0.2.0 (documented workflow) | Status: DOCUMENTED / RUNTIME NOT DEPLOYED

Independent video-production workflow within AI-Quality-Control, sharing canonical active Skills without copying or modifying them.

## Runtime source of truth
For substantial tasks read the latest main branch: `REGISTRY/skills-registry.yml`, `CORE/quality-control.md`, `CORE/skill-router.md` and applicable active SKILL.md files. No draft Skill auto-activation. Primary video-master for video deliverables; conditional content-master for copy/scripts, image-master for created/edited visual assets, research-master for substantive fact checks.

## Invocation
"AI-VIDEO-LUMORA: [goal], [platform], [duration], [footage], [language], [style], [deliverable]." Infer optional parameters; ask only for essential missing facts.

## End-to-end sequence
Brief -> Skill routing -> creative candidates -> Judge -> script/storyboard/shot list -> pre-production QC -> production if tools exist -> rendered-output QC -> **Error Hunter -> Root Cause -> targeted Fix -> Re-test and regression** -> Final Auditor -> **Improvement Roadmap**. Findings may trigger repair earlier in the sequence. Maximum four creation/revision rounds total, including the initial artifact; never reset the counter between QC stages.

## Ownership and limits
Logical roles: Producer, Content Strategist, Director, Cinematographer, Image Designer, Editor, Sound/Subtitle Specialist, Error Hunter, Root Cause Analyst, Fix Owner, Regression Tester, Final Auditor, Development Strategist. These are role-separated passes unless separate workers are actually executed and evidenced.

See [WORKFLOW.md](WORKFLOW.md), [ROUTING.md](ROUTING.md), [ERROR-RECOVERY.md](ERROR-RECOVERY.md), [QC-GATE.md](QC-GATE.md), [ROADMAP.md](ROADMAP.md), [TESTS.md](TESTS.md).

**No runtime, automated MP4 export, actual independent agents or publishing is deployed by this documentation update.** Never claim render/playback PASS without inspected output. Never auto-publish or mutate canonical CORE/Skills without explicit scope approval.
