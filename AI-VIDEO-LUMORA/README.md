# AI-VIDEO-LUMORA
Version: 0.1.0 (workflow package) | Status: DOCUMENTED / RUNTIME NOT DEPLOYED

An independent video-production workflow **inside** AI-Quality-Control. This is not a new Git repository, Git branch, or a fork of Content Master.

## Source of truth
At every substantial task, read current `REGISTRY/skills-registry.yml`, `CORE/quality-control.md`, `CORE/skill-router.md`, and selected active SKILL.md files on main. Never rely on hard-coded versions. Do not activate draft Skills.

**Primary:** `video-master` for video production, storyboard, edit planning and video QC.
**Conditional secondary:** `content-master` for audience strategy, hooks, dialogue, scripts, marketing; `image-master` for actual visual generation/editing, thumbnails, storyboards. `research-master` only for material factual/medical verification. No automatic three-Skill requirement.

## Invocation
Ask: "AI-VIDEO-LUMORA: [objective], [platform], [duration], [footage/assets], [language], [style], [desired output]". Infer optional details; ask only when essential. Output may be concept/script/shot list/edit plan or finished MP4 **only when actual rendering capability exists and is tested**.

## Responsibilities
Producer routes the request; Content Strategist develops message when needed; Director develops visual narrative; Cinematographer plans shots; Image Designer creates/edits required still assets; Editor assembles footage when a supported runtime exists; Sound/Subtitle Specialist handles licensed audio and captions; Critic, Re-check and Final Auditor apply canonical CORE. These are *logical roles*, not claims of separate autonomous agents.

See [WORKFLOW.md](WORKFLOW.md), [ROUTING.md](ROUTING.md), [QC-GATE.md](QC-GATE.md), [TESTS.md](TESTS.md).

## Deployment limits
This commit packages a reusable **procedure** only. It does not install Windows agents, connect ChatGPT/Codex to local programs, create a rendering engine, or prove automated MP4 export. Any external publishing or GitHub modifications require explicit approval.
