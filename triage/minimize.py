#!/usr/bin/env python3
"""
minimize.py — Delta-debugging SQL minimizer for SQLite harness crashes.

Usage:
    python3 minimize.py <crash_file> --harness <path> [--output <min_file>]

Strategy:
    1. Split input into SQL statements (by ';')
    2. Try removing each statement — keep removal if crash still reproduces
    3. Within surviving statements, try removing clauses (WHERE, ORDER BY, etc.)
    4. Repeat until no further reduction is possible

The minimizer preserves the crash signature (exit code + top stack frames).
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


DEDUP_FRAMES = 3


def run_harness(harness: str, sql: str, timeout: int = 5) -> tuple[int, str]:
    """Run harness with given SQL, return (exit_code, stderr)."""
    env = os.environ.copy()
    env['ASAN_OPTIONS'] = 'exitcode=223,abort_on_error=1,detect_leaks=0'
    env['UBSAN_OPTIONS'] = 'halt_on_error=1,exitcode=1,print_stacktrace=1'

    with tempfile.NamedTemporaryFile(suffix='.sql', mode='w', delete=False) as f:
        f.write(sql)
        tmp = f.name
    try:
        result = subprocess.run(
            [harness, tmp],
            capture_output=True,
            timeout=timeout,
            env=env,
        )
        return result.returncode, result.stderr.decode(errors='replace')
    except subprocess.TimeoutExpired:
        return -1, ''
    finally:
        os.unlink(tmp)


def extract_frames(stderr: str) -> list[str]:
    frames = []
    for line in stderr.splitlines():
        m = re.search(r'#\d+\s+0x[0-9a-f]+\s+in\s+(\S+)', line)
        if m:
            frames.append(m.group(1))
        elif 'runtime error:' in line:
            frames.append(line.strip())
        if len(frames) >= DEDUP_FRAMES:
            break
    return frames


def same_crash(frames_orig: list[str], exit_orig: int,
               frames_new: list[str], exit_new: int) -> bool:
    """True if the crash looks like the same root cause."""
    if exit_new not in (223, 1) and exit_new < 0:
        return False
    if not frames_new:
        return exit_new == exit_orig
    # Top frame must match
    return frames_new[0] == frames_orig[0]


def split_statements(sql: str) -> list[str]:
    """Split SQL into individual statements, preserving semicolons."""
    stmts = []
    for s in sql.split(';'):
        s = s.strip()
        if s:
            stmts.append(s)
    return stmts


def join_statements(stmts: list[str]) -> str:
    return ';\n'.join(stmts) + ';'


# Simple clause patterns to try removing
CLAUSE_PATTERNS = [
    r'\s+WHERE\s+.+?(?=\s+(?:GROUP|ORDER|LIMIT|HAVING|WINDOW|$))',
    r'\s+ORDER\s+BY\s+.+?(?=\s+(?:LIMIT|$))',
    r'\s+LIMIT\s+\S+(?:\s+OFFSET\s+\S+)?',
    r'\s+HAVING\s+.+?(?=\s+(?:ORDER|LIMIT|WINDOW|$))',
    r'\s+GROUP\s+BY\s+.+?(?=\s+(?:HAVING|ORDER|LIMIT|$))',
]


def try_remove_clauses(stmt: str, harness: str,
                       frames_orig: list[str], exit_orig: int) -> str:
    """Try removing optional clauses from a single statement."""
    current = stmt
    for pattern in CLAUSE_PATTERNS:
        candidate = re.sub(pattern, '', current, flags=re.IGNORECASE | re.DOTALL).strip()
        if candidate == current or not candidate:
            continue
        exitcode, stderr = run_harness(harness, candidate + ';')
        frames = extract_frames(stderr)
        if same_crash(frames_orig, exit_orig, frames, exitcode):
            current = candidate
    return current


def minimize(crash_file: str, harness: str, output: str) -> None:
    sql = Path(crash_file).read_text(errors='replace')

    # Establish baseline
    exit_orig, stderr_orig = run_harness(harness, sql)
    frames_orig = extract_frames(stderr_orig)

    if exit_orig not in (223, 1) and exit_orig >= 0:
        print(f'[minimize] WARNING: baseline does not crash (exit={exit_orig})')
        print('[minimize] Proceeding anyway (may produce non-reproducing result)')

    print(f'[minimize] Baseline: exit={exit_orig}, top_frame={frames_orig[0] if frames_orig else "none"}')
    print(f'[minimize] Original size: {len(sql)} bytes')

    # Phase 1: remove whole statements
    stmts = split_statements(sql)
    print(f'[minimize] Phase 1: {len(stmts)} statements, trying removal...')

    changed = True
    while changed:
        changed = False
        for i in range(len(stmts)):
            candidate = stmts[:i] + stmts[i+1:]
            if not candidate:
                continue
            test_sql = join_statements(candidate)
            exitcode, stderr = run_harness(harness, test_sql)
            frames = extract_frames(stderr)
            if same_crash(frames_orig, exit_orig, frames, exitcode):
                print(f'  Removed stmt {i}: "{stmts[i][:60]}..."')
                stmts = candidate
                changed = True
                break

    # Phase 2: remove clauses within each surviving statement
    print(f'[minimize] Phase 2: clause removal on {len(stmts)} surviving statements...')
    stmts = [try_remove_clauses(s, harness, frames_orig, exit_orig) for s in stmts]

    minimized = join_statements(stmts)
    print(f'[minimize] Minimized size: {len(minimized)} bytes ({len(sql) - len(minimized)} bytes removed)')

    Path(output).write_text(minimized)
    print(f'[minimize] Written to: {output}')


def main() -> None:
    parser = argparse.ArgumentParser(description='Minimize a SQL crash input')
    parser.add_argument('crash_file', help='Path to crash input file')
    parser.add_argument('--harness', required=True, help='Path to harness binary')
    parser.add_argument('--output', default='minimized.sql', help='Output file')
    args = parser.parse_args()

    minimize(args.crash_file, args.harness, args.output)


if __name__ == '__main__':
    main()
