"""Read-only preflight. No installs, model calls, auth files, or network requests.

Run this on the intended user's computer; this process cannot identify its owner.
Output omits hostname, username, paths, environment variables, and credentials.
"""
import argparse
import json
import os
import platform
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

TOOLS = ('node', 'npm', 'git', 'python', 'codex', 'gemini', 'claude', 'ollama')


def probe(name, lookup=shutil.which, run=subprocess.run):
    executable = lookup(name)
    if not executable:
        return {'installed': False, 'version': None, 'authentication': 'NOT_CHECKED'}
    # Presence only for Windows batch shims: never invoke through a shell.
    if Path(executable).suffix.lower() in ('.cmd', '.bat', '.ps1'):
        return {'installed': True, 'version': None, 'authentication': 'NOT_CHECKED',
                'note': 'shim detected; version not executed'}
    try:
        result = run([executable, '--version'], capture_output=True, text=True,
                     timeout=8, check=False, stdin=subprocess.DEVNULL)
        version = re.search(r'\b\d+\.\d+(?:\.\d+)?(?:[-+][a-zA-Z0-9.]+)?', result.stdout[:4096])
        return {'installed': True, 'version': version.group(0) if version and result.returncode == 0 else None,
                'authentication': 'NOT_CHECKED'}
    except (OSError, subprocess.TimeoutExpired, UnicodeError):
        return {'installed': True, 'version': None, 'authentication': 'NOT_CHECKED',
                'note': 'version check unavailable'}


def ram_gib():
    try:
        if platform.system() == 'Linux':
            return round(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / 2**30, 1)
        if platform.system() == 'Windows':
            import ctypes
            class Memory(ctypes.Structure):
                _fields_ = [('length', ctypes.c_ulong), ('load', ctypes.c_ulong)] + [
                    (n, ctypes.c_ulonglong) for n in ('total', 'avail', 'page_total', 'page_avail', 'virtual_total', 'virtual_avail', 'extended')]
            m = Memory()
            m.length = ctypes.sizeof(m)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m)):
                return round(m.total / 2**30, 1)
    except (OSError, ValueError, AttributeError):
        pass
    return None


def inspect():
    return {'schema_version': 1, 'checked_at': datetime.now(timezone.utc).isoformat(),
            'device_identity': 'UNVERIFIED: report describes only the computer running this script',
            'os': platform.system(), 'architecture': platform.machine(), 'ram_gib': ram_gib(),
            'gpu': 'NOT_CHECKED', 'tools': {t: probe(t) for t in TOOLS},
            'model_access': 'NOT_CHECKED', 'facebook': 'NOT_CONNECTED', 'publish_allowed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New JSON file; refuses overwriting an existing file')
    args = parser.parse_args()
    report = json.dumps(inspect(), ensure_ascii=False, indent=2) + '\n'
    if args.output:
        try:
            with args.output.open('x', encoding='utf-8') as stream:
                stream.write(report)
        except OSError:
            parser.exit(2, 'Cannot create output; choose a new file in a writable directory.\n')
    else:
        print(report, end='')


if __name__ == '__main__':
    main()
