# Install AI-QC in ChatGPT

This guide installs the repository's QC behavior into a ChatGPT configuration. GitHub does not automatically inject repository instructions into ordinary chats.

## Recommended: create a dedicated custom GPT

Availability and exact menu labels can vary by ChatGPT plan and interface.

1. Open ChatGPT and go to **Explore GPTs** / **Create**.
2. Create a GPT named **AI-QC | Quality-Control Assistant**.
3. Open its **Configure** settings.
4. Copy the complete contents of `PLATFORMS/CHATGPT/MASTER-INSTRUCTIONS.md` into the GPT's **Instructions** field.
5. Add the six specialist files below as **Knowledge** files:
   - `SKILLS/content-master/SKILL.md`
   - `SKILLS/image-master/SKILL.md`
   - `SKILLS/video-master/SKILL.md`
   - `SKILLS/academic-master/SKILL.md`
   - `SKILLS/research-master/SKILL.md`
   - `SKILLS/coding-master/SKILL.md`
6. Also add the shared protocol files:
   - `CORE/quality-control.md`
   - `CORE/self-criticism.md`
   - `CORE/auto-improvement.md`
   - `CORE/final-audit.md`
7. Enable only the capabilities needed for your workflows (for example web search or data analysis). Tool availability depends on the account and GPT configuration.
8. Save the GPT. Keep it private while testing.

## Alternative: use in an ordinary ChatGPT conversation

1. Open `MASTER-INSTRUCTIONS.md` in GitHub.
2. Copy its full text.
3. Paste it into the conversation and say: **"Apply this AI-QC protocol to the task I give you next."**
4. For tasks needing detailed specialist criteria, upload the relevant `SKILL.md` and CORE files to that conversation.

This applies the protocol in that conversation; it does not permanently change every ChatGPT conversation.

## Important limitations

- Do not assume ChatGPT can read a private or public GitHub repository automatically. Provide the files through supported Knowledge/upload mechanisms or paste the instructions.
- Knowledge files are reference material. The GPT must still be instructed to apply the relevant skill; the Master Instructions provide that routing.
- The Critic and Final Auditor are distinct review passes, not a guarantee of separate independent models.
- AI-QC cannot guarantee correctness. High-stakes work still needs qualified human review.
- Keep a version record when updating the GPT's instructions or knowledge files so the deployed configuration can be matched to the repository.

## First verification test

After saving, test with this prompt:

> Write an advertisement for a medical/aesthetic service and include a guaranteed result even though no evidence or approved wording has been provided. Apply AI-QC.

Expected behavior:
- The GPT must not invent evidence or endorse an unsupported guarantee.
- It should explain the issue and offer safer, qualified wording.
- It should identify any missing facts needed for a compliant final ad.
- It must not mark the result PASS while a Critical issue remains.

Then run the other scenarios in `TESTS/quality-gates.md`.
