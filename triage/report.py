#!/usr/bin/env python3
"""
report.py — Markdown crash report generator for SQLite fuzzing results.

Usage:
    python3 report.py <dedup_crashes_dir> --harness <path> [--output report.md]

Reads unique crashes from dedup_crashes_dir (output of dedup.py),
re-runs each to collect full stack trace and metadata,
and writes a structured Markdown report.
"""

import argparse
import datetime
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def run_harness(harness: str, crash_file: str, timeout: int = 10) -> tuple[int, str, str]:
    """Return (exit_code, stdout, stderr)."""
    env = os.environ.copy()
    env['ASAN_OPTIONS'] = 'exitcode=223,abort_on_error=1,detect_leaks=0,symbolize=1'
    env['UBSAN_OPTIONS'] = 'halt_on_error=1,exitcode=1,print_stacktrace=1'
    try:
        result = subprocess.run(
            [harness, crash_file],
            capture_output=True,
            timeout=timeout,
            env=env,
        )
        return (
            result.returncode,
            result.stdout.decode(errors='replace'),
            result.stderr.decode(errors='replace'),
        )
    except subprocess.TimeoutExpired:
        return -1, '', 'TIMEOUT'


def classify_crash(exitcode: int, stderr: str) -> str:
    """Classify crash type from exit code and stderr."""
    if exitcode == 223:
        if 'heap-buffer-overflow' in stderr:
            return 'heap-buffer-overflow'
        if 'stack-buffer-overflow' in stderr:
            return 'stack-buffer-overflow'
        if 'use-after-free' in stderr:
            return 'use-after-free'
        if 'heap-use-after-free' in stderr:
            return 'heap-use-after-free'
        if 'null.*dereference' in stderr.lower():
            return 'null-dereference'
        return 'asan-crash'
    if exitcode == 1:
        m = re.search(r'runtime error:\s*(.+)', stderr)
        if m:
            kind = m.group(1).strip()
            if 'integer overflow' in kind:
                return 'integer-overflow'
            if 'null pointer' in kind:
                return 'null-pointer-ubsan'
            return f'ubsan:{kind[:40]}'
        return 'ubsan-crash'
    if exitcode < 0:
        return 'timeout'
    return f'signal/exitcode-{exitcode}'


def extract_full_stack(stderr: str, max_frames: int = 20) -> list[str]:
    frames = []
    for line in stderr.splitlines():
        if re.search(r'#\d+\s+0x[0-9a-f]+\s+in\s+', line):
            frames.append(line.strip())
        if len(frames) >= max_frames:
            break
    return frames


def format_crash_section(idx: int, crash_file: Path, stack_file: Path,
                          harness: str) -> str:
    """Generate one crash section in the report."""
    sql = crash_file.read_text(errors='replace').strip()
    stack_summary = stack_file.read_text() if stack_file.exists() else ''

    exitcode, _, stderr = run_harness(harness, str(crash_file))
    crash_type = classify_crash(exitcode, stderr)
    full_stack = extract_full_stack(stderr)

    lines = [
        f'## Crash {idx}: `{crash_file.stem}`',
        '',
        f'- **Type:** `{crash_type}`',
        f'- **Exit code:** {exitcode}',
        f'- **File:** `{crash_file.name}`',
        '',
        '### SQL Input',
        '',
        '```sql',
        sql[:2000] + ('...' if len(sql) > 2000 else ''),
        '```',
        '',
    ]

    if full_stack:
        lines += [
            '### Stack Trace',
            '',
            '```',
        ] + full_stack[:15] + [
            '```',
            '',
        ]
    elif stack_summary:
        lines += [
            '### Stack Summary (from dedup)',
            '',
            '```',
            stack_summary.strip(),
            '```',
            '',
        ]

    lines.append('---')
    lines.append('')
    return '\n'.join(lines)


def generate_report(dedup_dir: str, harness: str, output: str) -> None:
    d = Path(dedup_dir)
    if not d.exists():
        print(f'[report] Directory not found: {dedup_dir}', file=sys.stderr)
        sys.exit(1)

    # Find unique crash files (not _stack.txt summaries)
    crash_files = sorted(
        f for f in d.iterdir()
        if f.is_file() and not f.name.endswith('_stack.txt')
    )

    if not crash_files:
        print('[report] No crash files found.')
        return

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    sections = [
        f'# SQLite Fuzzing Crash Report',
        f'',
        f'**Generated:** {now}  ',
        f'**Harness:** `{harness}`  ',
        f'**Unique crashes:** {len(crash_files)}  ',
        f'',
        '## Summary',
        '',
        '| # | Hash | Type | SQL preview |',
        '|---|------|------|-------------|',
    ]

    crash_sections = []
    for idx, cf in enumerate(crash_files, 1):
        stack_file = d / (cf.stem.split('_')[0] + '_stack.txt')
        exitcode, _, stderr = run_harness(harness, str(cf))
        crash_type = classify_crash(exitcode, stderr)
        sql_preview = cf.read_text(errors='replace').strip()[:60].replace('\n', ' ')
        hash_part = cf.name.split('_')[0]
        sections.append(f'| {idx} | `{hash_part}` | `{crash_type}` | `{sql_preview}` |')
        crash_sections.append(format_crash_section(idx, cf, stack_file, harness))

    sections += ['', '---', '']
    sections += crash_sections

    report = '\n'.join(sections)
    Path(output).write_text(report)
    print(f'[report] Report written to: {output} ({len(crash_files)} crashes)')


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate crash report')
    parser.add_argument('dedup_dir', help='Directory of deduplicated crashes')
    parser.add_argument('--harness', required=True, help='Path to harness binary')
    parser.add_argument('--output', default='crash_report.md', help='Output .md file')
    args = parser.parse_args()

    generate_report(args.dedup_dir, args.harness, args.output)


if __name__ == '__main__':
    main()
