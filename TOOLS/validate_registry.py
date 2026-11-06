#!/usr/bin/env python3
"""Validate AI-QC registry entries against skill files using only Python stdlib."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "REGISTRY" / "skills-registry.yml"

def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)

if not REGISTRY.is_file():
    fail(f"Registry not found: {REGISTRY}")

entries = []
current = None
for raw in REGISTRY.read_text(encoding="utf-8").splitlines():
    line = raw.rstrip()
    if re.match(r"^  - id:\s*", line):
        if current:
            entries.append(current)
        current = {"id": line.split(":", 1)[1].strip()}
    elif current and re.match(r"^    (version|path|status):\s*", line):
        key, value = line.strip().split(":", 1)
        current[key] = value.strip()

if current:
    entries.append(current)

if not entries:
    fail("No skill entries found in registry.")

seen = set()
errors = []
for item in entries:
    skill_id = item.get("id", "")
    if skill_id in seen:
        errors.append(f"Duplicate skill ID: {skill_id}")
    seen.add(skill_id)

    for required in ("version", "path", "status"):
        if not item.get(required):
            errors.append(f"{skill_id}: missing registry field {required}")

    rel_path = item.get("path", "")
    skill_path = ROOT / rel_path
    if not skill_path.is_file():
        errors.append(f"{skill_id}: missing file {rel_path}")
        continue

    content = skill_path.read_text(encoding="utf-8")
    frontmatter = content.split("---", 2)
    if len(frontmatter) < 3:
        errors.append(f"{skill_id}: missing YAML frontmatter")
        continue

    metadata = frontmatter[1]
    for key in ("name", "version", "status"):
        if not re.search(rf"(?m)^{key}:\\s*.+$", metadata):
            errors.append(f"{skill_id}: missing frontmatter field {key}")

    for key in ("name", "version", "status"):
        match = re.search(rf"(?m)^{key}:\\s*(.+)$", metadata)
        if match:
            actual = match.group(1).strip()
            expected = skill_id if key == "name" else item.get(key)
            if actual != expected:
                errors.append(
                    f"{skill_id}: {key} mismatch (registry={expected!r}, file={actual!r})"
                )

if errors:
    for error in errors:
        print(f"FAIL: {error}")
    sys.exit(1)

print(f"PASS: validated {len(entries)} skill registry entries.")
