"""T10 structural release gate. Validates supplied audit ledger; cannot prove reviewer independence or claim truth."""
import argparse
import json
from pathlib import Path

WEIGHTS = (25, 20, 15, 15, 10, 10, 5)
REQUIRED = ("brief", "candidate", "artifact", "critic", "editor_changes", "recheck", "final_auditor")

def decide(ledger):
    reasons = []
    if not isinstance(ledger, dict):
        return {"decision": "NOT PASS", "reasons": ["INVALID_LEDGER"]}
    for key in REQUIRED:
        if key not in ledger or ledger[key] is None:
            reasons.append("MISSING_" + key.upper())
    for key in ("brief", "candidate", "artifact"):
        if not isinstance(ledger.get(key), str) or not ledger[key].strip():
            reasons.append("INVALID_" + key.upper())
    critic = ledger.get("critic")
    if not isinstance(critic, list):
        reasons.append("INVALID_CRITIC_LIST")
        critic = []
    changes = ledger.get("editor_changes")
    if not isinstance(changes, list):
        reasons.append("INVALID_EDITOR_CHANGES")
        changes = []
    checks = ledger.get("recheck")
    if not isinstance(checks, dict):
        reasons.append("INVALID_RECHECK")
        checks = {}
    for finding in critic:
        if not isinstance(finding, dict) or not all(isinstance(finding.get(k), str) and finding[k].strip() for k in ("id", "severity", "passage", "reason")):
            reasons.append("INVALID_FINDING")
            continue
        if finding["severity"] not in ("CRITICAL", "MAJOR", "MINOR"):
            reasons.append("INVALID_SEVERITY")
        if finding["passage"] not in ledger.get("candidate", ""):
            reasons.append("FINDING_PASSAGE_NOT_IN_DRAFT")
        if finding["severity"] in ("CRITICAL", "MAJOR"):
            fid = finding["id"]
            mapped = [c for c in changes if isinstance(c, dict) and c.get("finding_id") == fid and isinstance(c.get("before"), str) and isinstance(c.get("after"), str) and c["before"] and c["after"] and c["before"] != c["after"]]
            if not mapped:
                reasons.append("UNMAPPED_BLOCKER_" + fid)
            elif not any(c["before"] in ledger.get("candidate", "") and c["after"] in ledger.get("artifact", "") for c in mapped):
                reasons.append("UNVERIFIED_TEXT_CHANGE_" + fid)
            if checks.get(fid) != "RESOLVED":
                reasons.append("UNRESOLVED_" + fid)
    audit = ledger.get("final_auditor")
    if not isinstance(audit, dict):
        reasons.append("INVALID_FINAL_AUDITOR")
        audit = {}
    scores = audit.get("scores")
    if not isinstance(scores, list) or len(scores) != 7 or any(type(s) is not int or s < 0 or s > w for s, w in zip(scores, WEIGHTS)):
        reasons.append("INVALID_CORE_SCORES")
        score = None
    else:
        score = sum(scores)
        if score < 90:
            reasons.append("SCORE_BELOW_90")
    for key in ("technical_gate", "domain_gate"):
        if audit.get(key) != "PASS":
            reasons.append(key.upper() + "_NOT_PASS")
    for key in ("evidence_complete", "regression_clear"):
        if audit.get(key) is not True:
            reasons.append(key.upper() + "_NOT_CONFIRMED")
    if type(ledger.get("rounds")) is not int or not 1 <= ledger["rounds"] <= 4:
        reasons.append("INVALID_ROUND_COUNT")
    return {"decision": "NOT PASS" if reasons else "SCHEMA_ACCEPTED_REVIEW_REQUIRED",
            "reasons": sorted(set(reasons)), "score": score,
            "warning": "Schema accepted is NOT AI-QC PASS. Independent review and claim verification cannot be proven by self-reported JSON."}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger", help="Path to JSON audit ledger")
    args = parser.parse_args()
    result = decide(json.loads(Path(args.ledger).read_text(encoding="utf-8")))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result["decision"] == "NOT PASS" else 0

if __name__ == "__main__":
    raise SystemExit(main())
