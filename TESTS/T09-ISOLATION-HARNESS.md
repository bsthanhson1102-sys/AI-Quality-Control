# T09 Isolation Harness

This harness prepares a minimal evaluation packet and checks the completeness,
consistency and SHA-256 integrity of the evidence returned from a fresh run.

## Important limitation

The harness **cannot inspect hidden model conversation context**, enforce ChatGPT
tool availability, or prove that a human attestation is truthful. A structurally
valid evidence bundle is not by itself proof of hard isolation. The evaluator
must preserve the fresh-session setup and transcript, and the Final Auditor
must review the actual runtime configuration.

## Prepare a clean packet

From the repository root:

```bash
python TOOLS/t09_isolation_harness.py prepare /tmp/ai-qc-t09-run
```

The new directory contains only:
- `prompt.md`: the task and isolation constraints;
- `evidence.template.json`: a blank evidence record with the prompt hash;
- `README.txt`: short instructions;
- `artifacts/`: empty destination for the model's code and tests.

No Registry, CORE, Skill or previous report files are copied into the packet.

## Run the evaluation

1. Start a genuinely new conversation or a separately provisioned model-evaluation session.
2. Ensure no previous AI-QC conversation, Registry/CORE/Skill file, memory snapshot,
   project instruction, or prior report is injected.
3. Disable repository/GitHub connectors, browser/web retrieval and network access
   for the evaluated model. If the platform cannot enforce this, record the
   limitation and do not call the run a hard-isolation test.
4. Provide only the contents of `prompt.md`. Do not attach this repository or
   prior T09 reports.
5. Save the full transcript as `transcript.md` in the bundle.
6. Save every produced source and test file under `artifacts/`.
7. Copy `evidence.template.json` to `evidence.json`, fill every field truthfully,
   and calculate the transcript SHA-256. Record the actual test command, exit
   code and test counts. Do not enter assumed results.
8. Have a human evaluator attest to the fresh session and absence of injected
   Registry/Skill content.

## Verify evidence

```bash
python TOOLS/t09_isolation_harness.py verify /tmp/ai-qc-t09-run
```

Exit codes:
- `0`: evidence structure and recorded hashes are internally consistent;
- `1`: evidence is incomplete, inconsistent, or fails a mandatory isolation assertion;
- `2`: evidence file is missing or unreadable.

Even exit code 0 prints that isolation is human-attested, not independently
proven by the script. A reviewer must still inspect the transcript and runtime
configuration. Do not infer a GitHub outage from a missing connector; report
"retrieval tool unavailable" instead.
