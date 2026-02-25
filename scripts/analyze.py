#!/usr/bin/env python3
"""
analyze.py — Coverage growth and TTFC (Time To First Crash) analysis.

Usage:
    # Single run analysis
    python3 scripts/analyze.py /tmp/nautilus_eval/sqlite-3.31.1_run1

    # Compare multiple runs
    python3 scripts/analyze.py /tmp/nautilus_eval/sqlite-3.31.1_run{1,2,3}

    # Compare grammar vs baseline
    python3 scripts/analyze.py --label "structured" run1/ --label "baseline" run2/

Output:
    - TTFC per run (seconds to first crash)
    - Coverage growth curve (unique edges vs time)
    - Per-strategy bits_found statistics
    - Summary table
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime


def parse_nautilus_log(workdir: Path) -> dict:
    """
    Parse Nautilus workdir for metrics.
    Nautilus writes state to workdir/status.json periodically.
    Falls back to crash file timestamps if no status.json.
    """
    result = {
        'workdir': str(workdir),
        'crashes': [],
        'ttfc_seconds': None,
        'total_crashes': 0,
        'queue_size': 0,
        'coverage_snapshots': [],  # list of (timestamp, edges)
    }

    # Count crashes
    crashes_dir = workdir / 'crashes'
    if crashes_dir.exists():
        crash_files = sorted(crashes_dir.iterdir())
        result['total_crashes'] = len(crash_files)
        result['crashes'] = [str(f.name) for f in crash_files]

        if crash_files:
            # TTFC = mtime of first crash - mtime of oldest queue item (proxy for start)
            first_crash_time = crash_files[0].stat().st_mtime
            queue_dir = workdir / 'queue'
            if queue_dir.exists():
                queue_files = sorted(queue_dir.iterdir(), key=lambda f: f.stat().st_mtime)
                if queue_files:
                    start_time = queue_files[0].stat().st_mtime
                    result['ttfc_seconds'] = first_crash_time - start_time

    # Queue size
    queue_dir = workdir / 'queue'
    if queue_dir.exists():
        result['queue_size'] = len(list(queue_dir.iterdir()))

    # Try status.json
    status_file = workdir / 'status.json'
    if status_file.exists():
        try:
            status = json.loads(status_file.read_text())
            result['status'] = status
        except json.JSONDecodeError:
            pass

    # Try to parse coverage from queue file mtimes (approximate)
    if queue_dir.exists():
        snapshots = []
        base_time = None
        for qf in sorted(queue_dir.iterdir(), key=lambda f: f.stat().st_mtime):
            t = qf.stat().st_mtime
            if base_time is None:
                base_time = t
            snapshots.append((t - base_time, len(snapshots) + 1))
        result['coverage_snapshots'] = snapshots

    return result


def format_ttfc(seconds: float | None) -> str:
    if seconds is None:
        return 'N/A (no crash)'
    if seconds < 60:
        return f'{seconds:.1f}s'
    if seconds < 3600:
        return f'{seconds/60:.1f}m'
    return f'{seconds/3600:.2f}h'


def print_summary(results: list[dict], labels: list[str]) -> None:
    print('\n' + '=' * 60)
    print('  Fuzzing Campaign Analysis')
    print('=' * 60)

    header = f'{"Run":<25} {"TTFC":>10} {"Crashes":>8} {"Queue":>8}'
    print(header)
    print('-' * 60)

    for label, r in zip(labels, results):
        ttfc = format_ttfc(r['ttfc_seconds'])
        print(f'{label:<25} {ttfc:>10} {r["total_crashes"]:>8} {r["queue_size"]:>8}')

    print('=' * 60)

    # Coverage growth (if multiple runs, show queue growth rate)
    for label, r in zip(labels, results):
        snaps = r['coverage_snapshots']
        if snaps:
            total_time = snaps[-1][0]
            final_edges = snaps[-1][1]
            rate = final_edges / (total_time / 3600) if total_time > 0 else 0
            print(f'\n{label}: {final_edges} queue items in {format_ttfc(total_time)} '
                  f'({rate:.0f}/hr)')

    # TTFC comparison
    if len(results) > 1:
        print('\nTTFC comparison:')
        base_ttfc = results[0]['ttfc_seconds']
        for label, r in zip(labels[1:], results[1:]):
            if base_ttfc and r['ttfc_seconds']:
                ratio = base_ttfc / r['ttfc_seconds']
                print(f'  {labels[0]} vs {label}: {ratio:.2f}x speedup in crash finding')


def write_csv(results: list[dict], labels: list[str], output: str) -> None:
    """Write coverage snapshots as CSV for plotting."""
    with open(output, 'w') as f:
        f.write('run,elapsed_seconds,queue_size\n')
        for label, r in zip(labels, results):
            for t, edges in r['coverage_snapshots']:
                f.write(f'{label},{t:.1f},{edges}\n')
    print(f'\nCSV written to: {output}')


def main() -> None:
    parser = argparse.ArgumentParser(description='Analyze Nautilus fuzzing results')
    parser.add_argument('workdirs', nargs='+', help='Workdir paths to analyze')
    parser.add_argument('--label', action='append', dest='labels',
                        help='Label for each workdir (can repeat)')
    parser.add_argument('--csv', help='Output CSV file for coverage curves')
    args = parser.parse_args()

    workdirs = [Path(w) for w in args.workdirs]
    labels = args.labels or [w.name for w in workdirs]

    if len(labels) < len(workdirs):
        labels += [w.name for w in workdirs[len(labels):]]

    results = []
    for wd in workdirs:
        if not wd.exists():
            print(f'Warning: workdir not found: {wd}', file=sys.stderr)
            results.append({'workdir': str(wd), 'crashes': [], 'ttfc_seconds': None,
                            'total_crashes': 0, 'queue_size': 0, 'coverage_snapshots': []})
        else:
            results.append(parse_nautilus_log(wd))

    print_summary(results, labels)

    if args.csv:
        write_csv(results, labels, args.csv)


if __name__ == '__main__':
    main()
