#!/usr/bin/env python3
"""Offline, stdlib-only AI-QC skill deployer. Run at repository root.
Usage: python PLATFORMS/CODEX/scripts/deploy_skills.py [target-project]
Copies active skills and shared CORE to target/.agents/skills/.
No network or silent GitHub fetch. Does not configure ChatGPT custom instructions.
"""
from pathlib import Path
import hashlib
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[3]
TARGET = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT
REG = ROOT / "REGISTRY/skills-registry.yml"
SNAP = ROOT / "PLATFORMS/CODEX/references/registry-snapshot.yml"
EXPECTED = "52391e03c29cd4f22935824716f57a8b5a7be2df"

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

if not REG.exists() or not SNAP.exists():
    raise SystemExit("BLOCKED: missing registry or pinned snapshot")
data = REG.read_bytes()
if git_blob_sha(data) != EXPECTED:
    raise SystemExit("BLOCKED: registry differs from pinned snapshot; refresh deployment metadata")
snapshot = SNAP.read_text(encoding="utf-8")
if snapshot.split("\n", 1)[1] != data.decode("utf-8"):
    raise SystemExit("BLOCKED: snapshot content does not match registry")
entries = re.findall(r"(?m)^  - id: ([^\n]+)\n    version: ([^\n]+)\n    path: ([^\n]+)\n    status: ([^\n]+)", data.decode())
if not entries:
    raise SystemExit("BLOCKED: no registry entries")
out = TARGET / ".agents/skills"
for name, version, path, status in entries:
    if status != "active":
        continue
    source = ROOT / path
    if not source.is_file():
        raise SystemExit("BLOCKED: missing " + path)
    meta = source.read_text(encoding="utf-8")
    for field, value in [("name", name), ("version", version), ("status", status)]:
        if not re.search(r"(?m)^" + field + r": " + re.escape(value) + r"$", meta):
            raise SystemExit("BLOCKED: metadata mismatch " + path + " " + field)
    destination = out / name
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination / "SKILL.md")
    refs = destination / "references"
    refs.mkdir(exist_ok=True)
    shutil.copy2(ROOT / "CORE/quality-control.md", refs / "core-rubric.md")
    shutil.copy2(SNAP, refs / "registry-snapshot.yml")
    print("DEPLOYED:", name, version)
print("DONE: source registry blob SHA", EXPECTED)
print("NOTE: runtime discovery, actual QC behavior and external validators NOT TESTED")
