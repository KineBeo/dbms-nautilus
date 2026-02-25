#!/usr/bin/env python3
"""
dedup.py — Stack-hash crash deduplication for SQLite harness crashes.

Usage:
    python3 dedup.py <workdir> [--output dedup_crashes/]

Reads crash files from <workdir>/crashes/, re-runs each under the harness
with AddressSanitizer, extracts the top-N frames of the stack trace,
and deduplicates by hash. Unique crashes are written to --output.

Requirements:
    - HARNESS env var or --harness argument: path to the harness binary
    - ASan must be compiled into the harness (it is, via Makefile)
"""

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


# Number of stack frames to use for deduplication hash
DEDUP_FRAMES = 5


def extract_asan_frames(stderr_output: str) -> list[str]:
    """Extract function names from ASan/UBSan stack trace output."""
    frames = []
    # ASan format: #0 0xdeadbeef in function_name file.c:42
    for line in stderr_output.splitlines():
        m = re.search(r'#\d+\s+0x[0-9a-f]+\s+in\s+(\S+)', line)
        if m:
            frames.append(m.group(1))
        # UBSan format: file.c:42: runtime error: ...
        elif 'runtime error:' in line:
            frames.append(line.strip())
        if len(frames) >= DEDUP_FRAMES:
            break
    return frames


def crash_hash(frames: list[str]) -> str:
    """SHA256 of top N frame names."""
    key = '\n'.join(frames[:DEDUP_FRAMES])
    return hashlib.sha256(key.encode()).hexdigest()[:16]


def run_crash(harness: str, crash_file: str, timeout: int = 5) -> tuple[int, str]:
    """Run harness on crash file, return (exit_code, stderr)."""
    env = os.environ.copy()
    env['ASAN_OPTIONS'] = 'exitcode=223,abort_on_error=1,detect_leaks=0'
    env['UBSAN_OPTIONS'] = 'halt_on_error=1,exitcode=1,print_stacktrace=1'
    try:
        result = subprocess.run(
            [harness, crash_file],
            capture_output=True,
            timeout=timeout,
            env=env,
        )
        return result.returncode, result.stderr.decode(errors='replace')
    except subprocess.TimeoutExpired:
        return -1, ''


def dedup(workdir: str, harness: str, output_dir: str) -> None:
    crashes_dir = Path(workdir) / 'crashes'
    if not crashes_dir.exists():
        print(f'[dedup] No crashes directory found at {crashes_dir}')
        return

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    seen_hashes: dict[str, str] = {}  # hash -> original filename
    crash_files = sorted(crashes_dir.iterdir())
    total = len(crash_files)
    unique = 0

    print(f'[dedup] Processing {total} crash files...')

    for crash_file in crash_files:
        if not crash_file.is_file():
            continue

        exitcode, stderr = run_crash(harness, str(crash_file))

        if exitcode not in (223, 1) and exitcode >= 0:
            # Not an ASan/UBSan crash on replay — skip
            continue

        frames = extract_asan_frames(stderr)
        if not frames:
            # No stack trace — use file hash as fallback
            content = crash_file.read_bytes()
            h = hashlib.sha256(content).hexdigest()[:16]
            frames = [f'<no-stack-{h}>']

        h = crash_hash(frames)

        if h not in seen_hashes:
            seen_hashes[h] = crash_file.name
            dest = out / f'{h}_{crash_file.name}'
            shutil.copy2(crash_file, dest)
            # Write stack summary alongside
            summary = out / f'{h}_stack.txt'
            summary.write_text(
                f'Original: {crash_file.name}\n'
                f'Exit code: {exitcode}\n'
                f'Hash: {h}\n'
                f'Top frames:\n' + '\n'.join(f'  {f}' for f in frames) + '\n'
            )
            unique += 1
            print(f'  [NEW]  {h} ← {crash_file.name} ({len(frames)} frames)')
        else:
            print(f'  [DUP]  {h} ← {crash_file.name} (same as {seen_hashes[h]})')

    print(f'\n[dedup] {unique} unique crashes out of {total} total.')


def main() -> None:
    parser = argparse.ArgumentParser(description='Deduplicate ASan/UBSan crashes')
    parser.add_argument('workdir', help='Nautilus workdir containing crashes/')
    parser.add_argument('--harness', default=os.environ.get('HARNESS', ''),
                        help='Path to harness binary (or set HARNESS env var)')
    parser.add_argument('--output', default='dedup_crashes',
                        help='Output directory for unique crashes (default: dedup_crashes)')
    args = parser.parse_args()

    if not args.harness:
        print('Error: --harness required (or set HARNESS env var)', file=sys.stderr)
        sys.exit(1)

    dedup(args.workdir, args.harness, args.output)


if __name__ == '__main__':
    main()
