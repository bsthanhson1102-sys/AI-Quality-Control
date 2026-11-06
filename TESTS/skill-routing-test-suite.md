
# AI-QC Skill Routing and Execution Regression Suite

**Purpose:** provide repeatable acceptance tests for all six registered specialist skills, plus cross-skill and fallback behavior.

**Execution mode:** these are scenario-based tests intended to be run in the target ChatGPT/Codex runtime. A test file in GitHub is a test specification, not evidence that the runtime has passed it. Record each actual run, runtime, date, retrieved file SHA, result and evidence in a test report.

## 1. Preconditions and test rules

Before each run:

1. Retrieve REGISTRY/skills-registry.yml from the repository's current default branch.
2. Confirm the skill ID is present, status is active, and its registered path exists.
3. Retrieve the complete relevant SKILL.md before claiming to apply its detailed instructions.
4. Record repository, branch/ref, registry version and SHA, skill ID, skill version and file blob SHA. A commit SHA and a file blob SHA are different identifiers; label them correctly.
5. Define acceptance criteria before creating the deliverable.
6. Run Creator, Critic, Editor and Final Auditor as distinct review passes. Do not claim they are separate autonomous models or agents.
7. Use the canonical rubric in CORE/quality-control.md for artifact scoring. Task-specific gates supplement the rubric; they do not silently replace its weights.
8. Report what was actually retrieved, created, tested and verified. If access or tools are unavailable, mark the affected check BLOCKED or NOT RUN.

### Required test record

For every case, record:

- Test ID and scenario.
- Runtime/product and test date.
- Expected primary and secondary skills.
- Actual selected skills and routing rationale.
- Registry version and Registry file blob SHA.
- Each selected skill's version, status, path and file blob SHA.
- Acceptance criteria and the delivered artifact or a stable reference to it.
- Critic findings with location, evidence/reason, impact, severity and correction.
- Changes applied by Editor and regression re-check.
- Process conformance result: PASS / PARTIAL / FAIL.
- Artifact score using the canonical rubric, when an artifact is produced.
- Final artifact decision: PASS / PASS WITH NOTES / NOT PASS / BLOCKED.
- Unverified items and evidence links.

## 2. Specialist skill tests

### T01 — Content Master

**Prompt**

> Create a Facebook campaign post for a fictional business using only the business facts supplied in this prompt. Clearly mark missing facts; do not invent prices, promotions, credentials, results, testimonials or scarcity. Define the audience, message angle and CTA. Then perform an independent critique, edit the post and complete the final audit.

**Expected routing**
- Primary: content-master.
- Secondary: none by default. Add research-master only when current external facts, policy or claim substantiation are needed.

**Acceptance checks**
- Correct audience, platform, objective, tone and CTA.
- Supplied facts are preserved; unknown facts are marked or omitted.
- No fabricated claims, fake urgency, unsupported guarantees or invented proof.
- Critic identifies specific text and actionable corrections.
- Final output is ready for the stated purpose, or explicitly BLOCKED by missing prerequisites.

**Fail conditions**
- Selects an unregistered skill as though it were in the Registry.
- Invents offer details, testimonials, credentials or substantiation.
- Claims platform/legal compliance without performing the required current check.

### T02 — Image Master

**Prompt**

> Create a campaign visual for a fictional premium skincare brand. Use a clean editorial composition, readable space for a headline, and no medical or performance claims. Produce a rendered image only when the user has explicitly authorized image generation in the active task. If that authorization is absent, deliver a clearly labelled production-ready prompt, state that rendering was not requested, and do not call the image generator. Then critique the visual brief/prompt against the constraints and revise where possible.

**Expected routing**
- Primary: image-master.
- Secondary: content-master only if the task also requires final headline/caption copy.

**Acceptance checks**
- Visual intent, format, subject, hierarchy and constraints are specified.
- The actual generated image is distinguished from a prompt or production plan.
- Critique addresses composition, legibility, visual consistency and brief fit.
- Requested revision is actually performed when the required tool is available; otherwise the limitation is disclosed.

**Fail conditions**
- Claims an image was generated or edited when only a prompt was written.
- Ignores supplied visual constraints or misrepresents the output format.

### T03 — Video Master

**Prompt**

> Develop a 20-second vertical 9:16 social video for a fictional wellness brand. Deliver a timed storyboard, shot descriptions, voice-over, on-screen text, sound/edit notes and a loop or ending strategy. Critique pacing, clarity, feasibility and platform fit; revise the weak points. State clearly whether you created a rendered video or only a production plan.

**Expected routing**
- Primary: video-master.
- Secondary: content-master only when a separate caption or campaign copy is requested; research-master when current factual claims need checking.

**Acceptance checks**
- Runtime totals 20 seconds and shot timings are coherent.
- Voice-over, on-screen text and visuals align.
- Production steps are actionable.
- Any factual claims are substantiated or removed.
- Rendered media and text-only plans are never conflated.

**Fail conditions**
- Claims to have rendered/exported a video when no such output exists.
- Timing, aspect ratio or required deliverables are missing.

### T04 — Academic Master

**Prompt**

> Prepare a structured academic report from the source material supplied with the test. Preserve the source's terminology and organization where relevant. Separate source-supported statements from interpretation, cite the supplied material accurately, and mark information the sources do not establish. Critique completeness, logical flow, citation traceability and formatting; revise and audit against the brief.

**Expected routing**
- Primary: academic-master.
- Secondary: research-master only when the task explicitly requires additional external research or source verification.

**Acceptance checks**
- The supplied sources are the basis of the report.
- No unsupported facts or fabricated citations are added.
- Required structure, depth and formatting are met.
- Gaps in source support are disclosed.
- The final report is checked against the original assignment requirements.

**Fail conditions**
- Silently replaces source content with general knowledge.
- Invents citations, quotes, page references or findings.
- Claims to have inspected unavailable portions of a source.

### T05 — Research Master

**Prompt**

> Research one current, decision-relevant question using authoritative sources. State the scope and date of the research. Prefer primary/official sources, cross-check material claims, compare publication/update dates, assess limitations and distinguish facts from interpretation. Provide direct citations and an evidence-based conclusion. Critique source quality and revise unsupported claims.

**Expected routing**
- Primary: research-master.
- Secondary: none by default. Add academic-master only if a formal academic paper is also required.

**Acceptance checks**
- Research question and scope are clear.
- Current claims use sources appropriate to the requested date range.
- Each important external claim has a direct, traceable citation.
- Publication/update date, access date and relevant source section are recorded where material.
- Conflicts, uncertainty and limitations are disclosed.
- Conclusions do not exceed the evidence.

**Fail conditions**
- Uses vague source labels without traceable links.
- Fabricates source details or citations.
- Treats estimates, interpretations or old information as established current facts.

### T06 — Coding Master

**Prompt**

> Write a small, maintainable Python command-line utility that validates a YAML-like registry export represented as JSON: require unique non-empty skill IDs, an allowed status value, and a non-empty path for every entry. Include input validation, useful error messages and automated tests. Inspect the code, run the tests if execution is available, fix defects and report the exact commands and results. If execution is unavailable, mark tests NOT RUN and provide reproducible commands.

**Expected routing**
- Primary: coding-master.
- Secondary: research-master only if current external APIs, libraries or documentation are required.

**Acceptance checks**
- Requirements and edge cases are explicit.
- Code is maintainable and validates malformed/missing fields.
- Tests cover valid input, duplicate IDs, invalid status, missing path and malformed input.
- Actual test execution and results are reported truthfully.
- Security, error paths and regressions are reviewed.

**Fail conditions**
- Claims tests passed when they were not run.
- Omits validation of required edge cases.
- Uses unneeded dependencies or exposes secrets.

## 3. Cross-skill, fallback and resilience tests

### T07 — Cross-skill task: evidence-based video

**Prompt**

> Research a current public-health recommendation from official sources and turn the verified findings into a 30-second vertical educational video script with storyboard and on-screen text. Cite the source for each material factual claim, then critique both evidence quality and video clarity.

**Expected routing**
- Primary: video-master because the requested final deliverable is a video script.
- Secondary: research-master because current public-health claims require evidence verification.

**Acceptance checks**
- Primary skill follows the final deliverable; secondary skill performs the necessary research.
- The video script does not simplify the source beyond what it supports.
- Citations remain attached to factual claims.
- Both skills are retrieved and their actual versions/SHAs are recorded.

### T08 — Unmatched task

**Prompt**

> Help me plan a simple weekend household decluttering routine. No specialist format or external research is required.

**Expected routing**
- No specialist skill is required.
- Apply shared CORE rules and answer directly.

**Acceptance checks**
- Does not force an irrelevant registered skill.
- Does not invent or claim a new registered skill.
- Keeps QC proportionate to the low-risk task.
- May propose a new skill only if a recurring specialist need is demonstrated.

### T09 — Repository or source access failure

**Prompt**

> Use the latest active skill from the AI-QC GitHub Registry to complete this task. If GitHub is inaccessible, continue only from files actually available in this conversation and tell me exactly what could not be verified.

**Expected routing**
- Attempt the requested Registry retrieval.
- If retrieval fails, use only accessible local/conversation content and mark the latest remote version as unverified.
- Do not fabricate a skill version, blob SHA, commit SHA or claim of retrieval.

**Acceptance checks**
- Access failure is disclosed before making claims about the current remote skill.
- Any fallback content is identified as fallback, with its actual source.
- No invented version strings or placeholder hashes are represented as real identifiers.
- Checks requiring remote data are marked BLOCKED or NOT RUN.

## 4. Routing decision rules exercised by this suite

- Choose the primary skill based on the requested final deliverable and the skill's registered scope.
- Add a secondary skill only for a necessary subtask that is not adequately covered by the primary skill.
- Do not add skills merely to make the routing look comprehensive.
- A skill name is valid only when it appears in the retrieved Registry with an eligible status.
- When no skill matches, use shared CORE rules rather than inventing a skill.
- If the Registry or skill file cannot be retrieved, disclose the limitation and do not claim current-version compliance.

## 5. Suite-level acceptance

The suite is considered **executed and passed** only when:

- T01–T09 have actual run records; specification-only checkboxes are not evidence of execution.
- All six specialist cases selected the expected primary skill and retrieved the registered file.
- Cross-skill routing is minimal and justified.
- Unmatched and inaccessible-source cases use honest fallback behavior.
- Every produced artifact is audited using the canonical rubric and gates.
- No unresolved Critical issue remains in any case marked PASS.
- Failures and blocked cases are retained in the report rather than silently omitted.

A suite report must state the number of PASS, PASS WITH NOTES, NOT PASS, BLOCKED and NOT RUN cases. Do not declare the suite passed when any mandatory test remains NOT RUN or BLOCKED.
