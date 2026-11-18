"""Injectable AI-QC worker pipeline; adapters are supplied by the caller.

Worker callbacks are not claimed to be independent AI models.
No external publishing, billing, or credential actions are performed here.
"""
import hashlib
import json
import math
from dataclasses import dataclass

THRESHOLD = 90
MAX_ROUNDS = 4
WEIGHTS = (25, 20, 15, 15, 10, 10, 5)


@dataclass
class Finding:
    code: str
    severity: str
    detail: str = ""


def score_review(review):
    """Validate an auditor's seven numeric criterion scores and findings."""
    scores = review.get("scores")
    if not isinstance(scores, list) or len(scores) != 7:
        raise ValueError("Seven criterion scores required")
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0 or v > 100 for v in scores):
        raise ValueError("Criterion scores must be numbers in [0, 100]")
    findings = review.get("findings", [])
    if not isinstance(findings, list) or any(not isinstance(f, dict) or f.get("severity") not in ("Critical", "Major", "Minor") for f in findings):
        raise ValueError("Findings require valid severity")
    total = round(sum(a * b for a, b in zip(scores, WEIGHTS)) / 100, 2)
    blocking = [f for f in findings if f["severity"] in ("Critical", "Major")]
    return {"score": total, "blocking": blocking, "pass": total >= THRESHOLD and not blocking}


def execute(brief, creator, critic, editor, regression, auditor):
    """Execute explicit worker callbacks; never infer missing QC evidence."""
    if brief.get("payment") or brief.get("publish") or brief.get("buy_credits"):
        return {"status": "BLOCKED", "reason": "AUTHORIZATION_REQUIRED", "history": []}
    history = []
    artifact = None
    for round_number in range(1, MAX_ROUNDS + 1):
        artifact = creator(brief) if round_number == 1 else editor(brief, artifact, history[-1]["findings"])
        if artifact is None:
            return {"status": "BLOCKED", "reason": "CREATOR_RETURNED_NO_ARTIFACT", "history": history}
        findings = critic(brief, artifact)
        if not isinstance(findings, list):
            raise ValueError("Critic must return a findings list")
        regression_result = regression(brief, artifact)
        if regression_result is not True:
            findings = findings + [{"severity": "Major", "code": "REGRESSION_FAILED"}]
        review = auditor(brief, artifact, findings)
        if not isinstance(review, dict):
            raise ValueError("Auditor must return a review dictionary")
        merged = dict(review)
        merged["findings"] = findings + review.get("findings", [])
        verdict = score_review(merged)
        evidence_hash = hashlib.sha256(json.dumps({"findings": merged["findings"], "scores": merged["scores"]}, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        history.append({"round": round_number, "score": verdict["score"], "findings": merged["findings"], "regression_pass": regression_result is True, "review_hash": evidence_hash})
        if verdict["pass"]:
            return {"status": "PASS", "score": verdict["score"], "rounds_used": round_number, "history": history, "artifact": artifact, "independent_agents_verified": False}
    return {"status": "NOT_PASS", "score": history[-1]["score"], "rounds_used": MAX_ROUNDS, "history": history, "independent_agents_verified": False}
