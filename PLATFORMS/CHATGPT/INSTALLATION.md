# Install AI-QC in ChatGPT

## Goal
Use the compact AI-QC core across ordinary ChatGPT conversations, with the GitHub repository as the version-controlled source for specialist skills. A Project is optional for long-running work; a separate custom GPT is not required.

## Step 1 — Apply the global core
1. Open ChatGPT Settings → Personalization → Custom Instructions (menu wording may vary).
2. Open `GLOBAL-CORE-INSTRUCTIONS.txt` in this folder.
3. Copy its complete text into the custom-instructions field that describes how ChatGPT should respond.
4. Save the setting. This is the layer intended to apply across ordinary chats, subject to the account's current settings and limits.
5. After GLOBAL-CORE-INSTRUCTIONS.txt changes in GitHub, replace the old Custom Instructions text with the complete current file and save again. GitHub updates do not sync into an already-saved Custom Instructions field.

## Step 2 — Keep the skill library in GitHub
Repository: https://github.com/bsthanhson1102-sys/AI-Quality-Control

The repository contains:
- `REGISTRY/skills-registry.yml`: skill catalogue and routing triggers.
- `CORE/skill-router.md`: selection and multi-skill rules.
- `CORE/skill-lifecycle.md`: add, update, version and deprecate process.
- `SKILLS/<skill-id>/SKILL.md`: specialist instructions.

When GitHub access is available in a conversation, ask ChatGPT to retrieve the current registry and only the relevant skill file(s). If the connector is not available, upload or paste the needed files. Never assume a GitHub update has synchronized into a chat that already contains an older snapshot.

## Step 3 — Optional Project for substantial ongoing work
Create a Project only when a long-running workflow benefits from persistent project-specific files and context. Add the Master Instructions, registry, shared CORE files and the relevant specialist skills, subject to the account's current file limits. Project instructions and files apply within that Project; they do not automatically become global instructions for chats outside it.

## Step 4 — Verify behavior
Try these prompts in an ordinary chat:
1. "Create a social post for a new product." Expected: route to content-master and apply the brief/QC rules.
2. "Plan a 20-second short video." Expected: route to video-master, adding content-master only if needed.
3. "Review this assignment against its rubric." Expected: route to academic-master and use supplied course materials.
4. "Debug this code." Expected: route to coding-master and report tests only if actually run.
5. Ask for a new recurring specialist capability. Expected: propose a modular Skill, identify registry/tests affected and request authorization before writing to GitHub.

## Important limitations
- Custom Instructions provide the compact global core; they do not embed every specialist skill.
- GitHub is not automatically injected into every chat. The current skill must be retrieved through an available connector or supplied in context.
- The text saved in Custom Instructions is a snapshot. Re-copy GLOBAL-CORE-INSTRUCTIONS.txt after a core update; updating the repository alone does not change your saved ChatGPT settings.
- A Project is optional and provides project-scoped instructions/files, not universal global behavior.
- The Critic and Final Auditor are distinct review passes, not a guarantee of separate independent models.
- AI-QC cannot guarantee correctness. High-stakes work still needs qualified human review.
- Record repository commit/version and actual tests when releasing changes. Mark tests NOT RUN when no runtime test was executed.
