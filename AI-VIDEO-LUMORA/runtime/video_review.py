"""Integration: inspect a candidate video and run the QC worker pipeline.

This adapter never generates footage, grants consent, or self-certifies visual quality.
"""
from pathlib import Path
from orchestrator import inspect_video
from worker_pipeline import execute


def review_candidate(brief, candidate_path, reviewer_scores=None, medical_review=False, consent_verified=False):
    path = Path(candidate_path)
    def creator(_):
        return str(path)
    def critic(_, artifact):
        inspection = inspect_video(artifact)
        issues = []
        if not inspection["ok"]:
            issues.append({"severity": "Major", "code": inspection["reason"]})
        if not consent_verified:
            issues.append({"severity": "Major", "code": "CONSENT_NOT_VERIFIED"})
        if not medical_review:
            issues.append({"severity": "Major", "code": "MEDICAL_VISUAL_REVIEW_MISSING"})
        return issues
    def editor(_, artifact, findings):
        return artifact  # No fabricated repair capability.
    def regression(_, artifact):
        return inspect_video(artifact)["ok"]
    def auditor(_, artifact, findings):
        # No scores without an actual reviewer; never invent a PASS.
        return {"scores": reviewer_scores if reviewer_scores is not None else [0]*7, "findings": []}
    return execute(brief, creator, critic, editor, regression, auditor)
