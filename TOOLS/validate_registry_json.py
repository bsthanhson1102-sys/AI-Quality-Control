#!/usr/bin/env python3
"""Validate a JSON export containing a list of AI-QC skill records."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

DEFAULT_ALLOWED_STATUSES = ("active",)


class RegistryValidationError(ValueError):
    """Raised when a registry document violates the expected structure."""


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream, parse_constant=_reject_nonstandard_constant)
    except FileNotFoundError as exc:
        raise RegistryValidationError(f"Input file not found: {path}") from exc
    except UnicodeDecodeError as exc:
        raise RegistryValidationError("Input is not valid UTF-8 text") from exc
    except json.JSONDecodeError as exc:
        raise RegistryValidationError(
            f"Malformed JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def _reject_nonstandard_constant(value: str) -> None:
    raise ValueError(f"Non-standard JSON constant is not allowed: {value}")


def _extract_skills(document: Any) -> list[Any]:
    if not isinstance(document, dict):
        raise RegistryValidationError("Top-level JSON value must be an object")
    skills = document.get("skills")
    if not isinstance(skills, list):
        raise RegistryValidationError("Field 'skills' must be a JSON array")
    return skills


def validate_document(
    document: Any, allowed_statuses: Iterable[str] = DEFAULT_ALLOWED_STATUSES
) -> list[str]:
    """Return all validation errors; an empty list means the document is valid."""
    errors: list[str] = []
    if not isinstance(document, dict):
        return ["Top-level JSON value must be an object"]

    skills = document.get("skills")
    if not isinstance(skills, list):
        return ["Field 'skills' must be a JSON array"]

    allowed = set(allowed_statuses)
    seen_ids: set[str] = set()

    for index, skill in enumerate(skills):
        prefix = f"skills[{index}]"
        if not isinstance(skill, dict):
            errors.append(f"{prefix} must be an object")
            continue

        skill_id = skill.get("id")
        if not _non_empty_string(skill_id):
            errors.append(f"{prefix}.id must be a non-empty string")
        else:
            normalized_id = skill_id.strip()
            if normalized_id in seen_ids:
                errors.append(f"{prefix}.id duplicates '{normalized_id}'")
            else:
                seen_ids.add(normalized_id)

        status = skill.get("status")
        if not _non_empty_string(status) or status.strip() not in allowed:
            choices = ", ".join(sorted(allowed))
            errors.append(f"{prefix}.status must be one of: {choices}")

        path = skill.get("path")
        if not _non_empty_string(path):
            errors.append(f"{prefix}.path must be a non-empty string")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate skill IDs, statuses and paths in a JSON registry export."
    )
    parser.add_argument("input", type=Path, help="Path to the JSON registry export")
    parser.add_argument(
        "--allowed-status",
        action="append",
        dest="allowed_statuses",
        help=(
            "Allowed status value (repeatable); defaults to 'active', "
            "the status observed in the verified Registry"
        ),
    )
    args = parser.parse_args(argv)

    try:
        document = _load_json(args.input)
    except (RegistryValidationError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    allowed = args.allowed_statuses or DEFAULT_ALLOWED_STATUSES
    errors = validate_document(document, allowed)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"INVALID: {len(errors)} error(s)", file=sys.stderr)
        return 1

    skills = _extract_skills(document)
    print(f"VALID: {len(skills)} skill record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
