"""Fail-closed release candidate scanner for CI. Does not publish."""
import json
import sys
from pathlib import Path
from publish_gate import verify

def inspect(root):
    pending = root / "RELEASES" / "pending"
    approvals = root / "RELEASES" / "approvals"
    files = sorted(pending.glob("*.json")) if pending.exists() else []
    if not files:
        return {"decision": "NO_CANDIDATES", "checked": 0, "errors": []}
    errors = []
    for file in files:
        try:
            ledger = json.loads(file.read_text(encoding="utf-8"))
            approval_file = approvals / file.name
            if not approval_file.is_file():
                errors.append(f"{file.name}: MISSING_APPROVAL")
                continue
            approval = json.loads(approval_file.read_text(encoding="utf-8"))
            result = verify(ledger, approval)
            if result["decision"] != "APPROVAL_RECORDED":
                errors.append(f"{file.name}: {','.join(result['reasons'])}")
        except (OSError, ValueError, UnicodeError) as exc:
            errors.append(f"{file.name}: INPUT_ERROR {exc}")
    return {"decision": "BLOCKED" if errors else "APPROVAL_RECORDS_ACCEPTED",
            "checked": len(files), "errors": errors}

if __name__ == "__main__":
    result = inspect(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("."))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(2 if result["decision"] == "BLOCKED" else 0)
