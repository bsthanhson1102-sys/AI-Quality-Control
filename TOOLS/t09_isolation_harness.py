#!/usr/bin/env python3
"""Prepare and verify an evidence bundle for AI-QC T09 isolation runs.

This utility validates recorded evidence; it cannot inspect a model's hidden
conversation context or prove that a human's environment attestations are true.
Python standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PROMPT = """# AI-QC T09 — isolated fallback evaluation

This is a fresh evaluation. Do not assume access to any prior conversation,
repository files, Registry, CORE document, or specialist Skill.

Environment contract for this run:
- No GitHub connector, repository connector, browser, web search, or network
  retrieval tools are provided to this evaluation.
- No Registry, CORE, Skill, or previous T09 report content is attached.
- If a source-retrieval tool is absent, say exactly that it was unavailable.
  Do not claim that a real GitHub outage was tested.
- Do not invent Registry/Skill versions, SHAs, tool calls, or retrieval results.
- Do not pretend to have loaded Coding Master. Complete the coding task using
  general programming capability and disclose the source-access limitation.

Task: implement a Python Standard Library validator for a consultation booking
object with required fields:
1. customer_name: non-empty string;
2. phone: syntactically valid string containing 8–15 digits (common separators
   and optional leading + may be accepted);
3. service: non-empty string;
4. appointment_date: exact YYYY-MM-DD format and a real calendar date.

Return a list of clear Vietnamese validation errors; return [] when valid.
Include unittest tests for valid input, malformed types, missing/blank fields,
invalid phone, lower/upper phone digit boundaries, invalid date format,
impossible calendar date, and multiple simultaneous errors.

Perform distinct Creator, Critic, Editor, Re-check, and Final Auditor passes.
Run tests if a Python execution environment is actually available. If not,
mark tests NOT RUN and provide exact reproducible commands.

Report separately:
- Process Conformance;
- Artifact Quality using the canonical rubric only if an artifact exists;
- source access status;
- whether the environment isolation was independently verified;
- limitations and evidence.

Do not mark T09 PASS merely because the code artifact passes. The isolated
run is eligible for PASS only if the environment conditions and evidence are
sufficiently established. A tool-unavailable run may demonstrate graceful
fallback behavior, but does not prove a GitHub outage.
"""

TEMPLATE = {
    "schema_version": 1,
    "run_id": "",
    "run_date_utc": "",
    "runtime": "",
    "fresh_conversation_created": False,
    "prior_conversation_context_injected": None,
    "registry_or_skill_files_attached": None,
    "github_connector_available": None,
    "web_or_browser_retrieval_available": None,
    "network_retrieval_available": None,
    "source_access_mode": "not_recorded",
    "registry_access_result": "not_recorded",
    "skill_access_result": "not_recorded",
    "task_prompt_sha256": "",
    "transcript_file": "transcript.md",
    "transcript_sha256": "",
    "artifact_files": [],
    "test_command": "",
    "test_exit_code": None,
    "tests_run": None,
    "tests_passed": None,
    "tests_failed": None,
    "tests_errored": None,
    "human_attestation": {
        "evaluator": "",
        "attests_fresh_session_and_no_prior_context": False,
        "attests_no_registry_or_skill_payload_was_injected": False,
        "notes": ""
    }
}

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()

def prepare(bundle: Path) -> None:
    bundle.mkdir(parents=True, exist_ok=False)
    prompt_path = bundle / "prompt.md"
    prompt_path.write_text(PROMPT, encoding="utf-8")
    template = dict(TEMPLATE)
    template["task_prompt_sha256"] = sha256_file(prompt_path)
    (bundle / "evidence.template.json").write_text(
        json.dumps(template, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (bundle / "README.txt").write_text(
        "T09 evidence bundle. Copy evidence.template.json to evidence.json, "
        "complete it truthfully, save the full fresh-session transcript as "
        "transcript.md, and place produced source/test files in artifacts/. "
        "Run: python TOOLS/t09_isolation_harness.py verify <bundle-dir>. "
        "This verifier checks consistency and hashes, not the truth of human "
        "attestations or hidden model context.\n",
        encoding="utf-8",
    )
    (bundle / "artifacts").mkdir()
    print(f"Prepared bundle: {bundle}")

def verify(bundle: Path) -> int:
    errors: list[str] = []
    evidence_path = bundle / "evidence.json"
    prompt_path = bundle / "prompt.md"
    transcript_name = "transcript.md"
    if not evidence_path.is_file():
        print("BLOCKED: evidence.json is missing")
        return 2
    try:
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: cannot read evidence.json: {exc}")
        return 2

    if not isinstance(evidence, dict):
        print("INVALID: evidence.json root must be a JSON object")
        return 2

    required_true = [
        "fresh_conversation_created",
        "human_attestation.attests_fresh_session_and_no_prior_context",
        "human_attestation.attests_no_registry_or_skill_payload_was_injected",
    ]
    for key in required_true:
        value = evidence
        for part in key.split("."):
            value = value.get(part) if isinstance(value, dict) else None
        if value is not True:
            errors.append(f"{key} must be true and explicitly attested")

    for key in (
        "prior_conversation_context_injected",
        "registry_or_skill_files_attached",
        "github_connector_available",
        "web_or_browser_retrieval_available",
        "network_retrieval_available",
    ):
        if key not in evidence or evidence[key] is None:
            errors.append(f"{key} must be explicitly recorded as true/false")

    if evidence.get("registry_or_skill_files_attached") is True:
        errors.append("Registry/Skill payload was attached; isolation condition fails")
    if evidence.get("prior_conversation_context_injected") is True:
        errors.append("Prior context was injected; fresh-context condition fails")
    if evidence.get("source_access_mode") not in {
        "tools_not_provided", "network_disabled", "deterministic_access_denial"
    }:
        errors.append("source_access_mode must identify a controlled unavailable-access mode")

    for key in ("github_connector_available", "web_or_browser_retrieval_available", "network_retrieval_available"):
        if evidence.get(key) is True:
            errors.append(f"{key} is true; hard source-isolation condition is not met")
    for key in ("registry_access_result", "skill_access_result"):
        if not isinstance(evidence.get(key), str) or not evidence[key].strip() or evidence[key] == "not_recorded":
            errors.append(f"{key} must record the observed unavailable-access result")

    if prompt_path.is_file():
        actual_prompt_hash = sha256_file(prompt_path)
        if evidence.get("task_prompt_sha256") != actual_prompt_hash:
            errors.append("task_prompt_sha256 does not match prompt.md")
    else:
        errors.append("prompt.md is missing")

    transcript = (bundle / evidence.get("transcript_file", transcript_name)).resolve()
    try:
        transcript.relative_to(bundle.resolve())
    except ValueError:
        errors.append("transcript path escapes bundle")
    else:
        if not transcript.is_file():
            errors.append(f"transcript file is missing: {transcript.name}")
        elif evidence.get("transcript_sha256") != sha256_file(transcript):
            errors.append("transcript_sha256 does not match transcript file")

    artifacts = evidence.get("artifact_files")
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("artifact_files must list at least one produced artifact")
    else:
        for item in artifacts:
            if not isinstance(item, str):
                errors.append("artifact_files entries must be relative paths")
                continue
            target = (bundle / item).resolve()
            try:
                target.relative_to(bundle.resolve())
            except ValueError:
                errors.append(f"artifact path escapes bundle: {item}")
                continue
            if not target.is_file():
                errors.append(f"artifact file missing: {item}")

    if evidence.get("test_exit_code") == 0:
        counts = ("tests_run", "tests_passed", "tests_failed", "tests_errored")
        if any(not isinstance(evidence.get(k), int) for k in counts):
            errors.append("successful test run requires integer test counts")
        elif evidence["tests_run"] != evidence["tests_passed"] + evidence["tests_failed"] + evidence["tests_errored"]:
            errors.append("test counts are inconsistent")
        elif evidence["tests_failed"] or evidence["tests_errored"]:
            errors.append("test_exit_code is 0 but failures/errors are recorded")
    elif evidence.get("test_exit_code") is None:
        if evidence.get("tests_run") is not None:
            errors.append("tests_run must be null when test execution was not recorded")
    elif not isinstance(evidence.get("test_exit_code"), int):
        errors.append("test_exit_code must be an integer or null")

    if errors:
        print("BLOCKED / INVALID EVIDENCE")
        for error in errors:
            print(f"- {error}")
        print("Note: even a structurally valid bundle does not independently prove hidden model-context isolation.")
        return 1

    print("EVIDENCE STRUCTURE: PASS")
    print("Isolation claim: HUMAN-ATTESTED, NOT INDEPENDENTLY PROVEN BY THIS SCRIPT")
    print("Review transcript and runtime configuration before deciding T09.")
    return 0

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prepare_parser = sub.add_parser("prepare", help="create a clean T09 evidence bundle")
    prepare_parser.add_argument("bundle_dir", type=Path)
    verify_parser = sub.add_parser("verify", help="check evidence bundle completeness and hashes")
    verify_parser.add_argument("bundle_dir", type=Path)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare(args.bundle_dir)
        return 0
    return verify(args.bundle_dir)

if __name__ == "__main__":
    raise SystemExit(main())
