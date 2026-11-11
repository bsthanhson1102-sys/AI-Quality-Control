"""Offline packet validator. Never calls an AI, executes evidence, or publishes.

Validates recorded attestations, not their authenticity or semantic correctness.
A separate trusted reviewer must inspect the evidence. No automatic PASS claim.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

WEIGHTS = [25, 20, 15, 15, 10, 10, 5]
STAGES = ('brief', 'production', 'technical', 'critic', 'editor', 'recheck', 'ai_qc', 'final')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def confined(root, relative):
    if not isinstance(relative, str) or not relative.strip():
        raise ValueError('missing relative file path')
    part = Path(relative)
    if part.is_absolute():
        raise ValueError('absolute path forbidden')
    resolved = (root / part).resolve()
    if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
        raise ValueError('file missing or outside task directory')
    return resolved


def validate(packet, root):
    """Return all detectable packet defects; never authorize real publishing."""
    errors = []
    if not isinstance(packet, dict):
        return ['packet must be an object']
    if not isinstance(packet.get('task_id'), str) or not packet['task_id'].strip():
        errors.append('task_id required')
    rounds = packet.get('round')
    if type(rounds) is not int or not 1 <= rounds <= 4:
        errors.append('round must be integer 1..4')
    commit = packet.get('ai_qc_commit', '')
    if not isinstance(commit, str) or len(commit) != 40 or any(c not in '0123456789abcdef' for c in commit):
        errors.append('pinned AI-QC commit required')
    artifacts = packet.get('artifacts')
    manifest = {}
    if not isinstance(artifacts, list) or not artifacts:
        errors.append('nonempty artifact list required')
    else:
        for entry in artifacts:
            try:
                if not isinstance(entry, dict):
                    raise ValueError('artifact must be object')
                name = entry.get('path')
                path = confined(root, name)
                if name in manifest:
                    raise ValueError('duplicate artifact')
                actual = digest(path)
                if entry.get('sha256') != actual:
                    raise ValueError('artifact hash mismatch')
                manifest[name] = actual
            except (ValueError, OSError) as exc:
                errors.append(str(exc))
    stages = packet.get('stages')
    if not isinstance(stages, dict):
        stages = {}
    for name in STAGES:
        stage = stages.get(name)
        if not isinstance(stage, dict) or stage.get('status') != 'completed':
            errors.append(f'{name}: missing completed stage')
            continue
        if not isinstance(stage.get('reviewer'), str) or not stage['reviewer'].strip():
            errors.append(f'{name}: reviewer required')
        records = stage.get('evidence')
        if not isinstance(records, list) or not records:
            errors.append(f'{name}: evidence required')
        else:
            for record in records:
                try:
                    if not isinstance(record, dict):
                        raise ValueError('evidence must be object')
                    path = confined(root, record.get('path'))
                    if path.stat().st_size == 0 or record.get('sha256') != digest(path):
                        raise ValueError('empty or changed evidence')
                except (ValueError, OSError) as exc:
                    errors.append(f'{name}: {exc}')
        if name in ('technical', 'recheck', 'ai_qc', 'final'):
            if stage.get('artifact_hashes') != manifest:
                errors.append(f'{name}: reviewed artifact version differs')
            if stage.get('verdict') != 'approved':
                errors.append(f'{name}: approval missing')
    producer = stages.get('production', {}).get('reviewer') if isinstance(stages.get('production'), dict) else None
    final = stages.get('final', {})
    qc = stages.get('ai_qc', {})
    if isinstance(final, dict) and final.get('reviewer') == producer:
        errors.append('producer cannot be final reviewer')
    if isinstance(qc, dict) and qc.get('reviewer') == producer:
        errors.append('producer cannot be AI-QC reviewer')
    if isinstance(qc, dict) and isinstance(final, dict) and qc.get('reviewer') == final.get('reviewer'):
        errors.append('final reviewer must be separate from AI-QC reviewer')
    gates = packet.get('gates')
    if not isinstance(gates, dict):
        gates = {}
    for name in ('technical', 'domain', 'regression'):
        if gates.get(name) != 'verified':
            errors.append(f'{name} acceptance not verified')
    scores = packet.get('scores')
    if not isinstance(scores, list) or len(scores) != 7:
        errors.append('seven canonical scores required')
    elif any(type(x) not in (int, float) or not math.isfinite(x) or not 0 <= x <= w for x, w in zip(scores, WEIGHTS)):
        errors.append('score outside canonical range')
    elif sum(scores) < 90:
        errors.append('score below 90')
    findings = packet.get('findings')
    if not isinstance(findings, list):
        errors.append('findings list required')
    else:
        for finding in findings:
            if not isinstance(finding, dict) or finding.get('severity') not in ('Critical', 'Major', 'Minor', 'Enhancement'):
                errors.append('malformed finding')
            elif finding['severity'] in ('Critical', 'Major') and finding.get('resolution') != 'verified_fixed':
                errors.append('unresolved Critical/Major')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('packet', type=Path)
    args = parser.parse_args()
    try:
        packet = json.loads(args.packet.read_text(encoding='utf-8'))
        errors = validate(packet, args.packet.parent)
    except (ValueError, OSError, TypeError, AttributeError) as exc:
        errors = [f'invalid packet: {exc}']
    print(json.dumps({'packet_status': 'BLOCKED' if errors else 'STRUCTURALLY_VALID',
                      'errors': errors, 'publish_allowed': False,
                      'note': 'Offline validation only; attestations require trusted review. No live publisher.'}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
