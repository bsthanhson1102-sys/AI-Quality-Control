"""AI-QC pilot runtime. Deterministic role passes, NOT independent agents."""
import argparse, hashlib, json, os
from pathlib import Path

MAX_ROUNDS = 4

def run(brief, state_dir, capability=None):
    capability = capability or {}
    root = Path(state_dir)
    root.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha256(json.dumps({"brief": brief, "capability": capability}, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    path = root / (key + ".json")
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    evidence = []
    def record(role, result):
        evidence.append({"role": role, "result": result})
    record("intake", {"brief_hash": key, "independent_agents": False})
    if any(brief.get(k) for k in ("payment", "publish", "buy_credits")):
        record("authorization", {"approved": False})
        status, findings = "BLOCKED", ["AUTHORIZATION_REQUIRED"]
    elif not capability.get("realistic_video_generator") and not capability.get("licensed_footage"):
        record("capability", {"realistic_video": False})
        status, findings = "BLOCKED", ["PRODUCTION_CAPABILITY_MISSING"]
    else:
        record("creator", {"status": "NOT_RUN", "reason": "Production adapter not implemented"})
        record("critic", {"severity": "Major", "finding": "NO_RENDERED_ARTIFACT"})
        record("fixer", {"status": "BLOCKED", "root_cause": "Missing production adapter"})
        record("regression", {"status": "NOT_RUN"})
        status, findings = "NOT_PASS", ["NO_RENDERED_ARTIFACT"]
    record("final_auditor", {"status": status, "qc_score": None, "round_limit": MAX_ROUNDS, "independent_worker_consensus": False})
    result = {"id": key, "status": status, "findings": findings, "rounds_used": 0, "evidence": evidence, "video_created": False}
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, path)
    return result

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--brief", required=True)
    p.add_argument("--state-dir", default=".aiqc-state")
    p.add_argument("--capability")
    a = p.parse_args()
    brief = json.loads(Path(a.brief).read_text(encoding="utf-8"))
    cap = json.loads(Path(a.capability).read_text(encoding="utf-8")) if a.capability else None
    print(json.dumps(run(brief, a.state_dir, cap), ensure_ascii=False, indent=2))
