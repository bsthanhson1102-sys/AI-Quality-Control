"""Fail-closed publication gate: structural QC plus explicit artifact-bound human approval.

This is an executable integration for workflows that invoke it. It is NOT installed
as a ChatGPT conversation hook. The approval record is an operator assertion,
not cryptographic proof of independence or content quality.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

from release_gate import decide


def verify(ledger, approval):
    result = decide(ledger)
    reasons = list(result["reasons"])
    if result["decision"] != "SCHEMA_ACCEPTED_REVIEW_REQUIRED":
        return {"decision": "BLOCKED", "reasons": reasons, "score": result.get("score")}
    if not isinstance(approval, dict):
        reasons.append("MISSING_EXTERNAL_APPROVAL")
    else:
        digest = hashlib.sha256(ledger["artifact"].encode("utf-8")).hexdigest()
        if approval.get("artifact_sha256") != digest:
            reasons.append("ARTIFACT_HASH_MISMATCH")
        if approval.get("decision") != "APPROVED":
            reasons.append("REVIEW_NOT_APPROVED")
        if not isinstance(approval.get("reviewer"), str) or not approval["reviewer"].strip():
            reasons.append("REVIEWER_NOT_IDENTIFIED")
        if not isinstance(approval.get("evidence"), str) or not approval["evidence"].strip():
            reasons.append("REVIEW_EVIDENCE_MISSING")
        if approval.get("domain_review") != "PASS":
            reasons.append("DOMAIN_REVIEW_NOT_PASS")
        if approval.get("technical_review") != "PASS":
            reasons.append("TECHNICAL_REVIEW_NOT_PASS")
    return {"decision": "BLOCKED" if reasons else "APPROVAL_RECORDED",
            "reasons": sorted(set(reasons)), "score": result.get("score"),
            "warning": "Approval is an attributed assertion, not independently authenticated; publishing host must enforce exit status."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger")
    parser.add_argument("--approval", required=True)
    args = parser.parse_args()
    try:
        ledger = json.loads(Path(args.ledger).read_text(encoding="utf-8"))
        approval = json.loads(Path(args.approval).read_text(encoding="utf-8"))
        result = verify(ledger, approval)
    except (OSError, ValueError, UnicodeError) as exc:
        result = {"decision": "BLOCKED", "reasons": ["INPUT_ERROR"], "detail": str(exc)}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["decision"] == "APPROVAL_RECORDED" else 2


if __name__ == "__main__":
    sys.exit(main())
