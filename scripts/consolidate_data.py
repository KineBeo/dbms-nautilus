#!/usr/bin/env python3
"""Consolidate 20 comparison campaign results into 3 CSVs.

Reads: workdirs/*comparison*/
Outputs:
  results/comparison/data/campaigns_summary.csv
  results/comparison/data/bug_classes.csv
  results/comparison/data/timeseries.csv
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKDIR_BASE = ROOT / "workdirs"
OUTPUT_DIR = ROOT / "results" / "comparison" / "data"

CAMPAIGN_RE = re.compile(r"(sqlite-[\d.]+)_comparison_(v3\.4|ebnf)_run(\d+)")


def parse_campaign(workdir: Path, version: str, grammar: str, run: int) -> dict | None:
    campaign_id = f"{grammar}_{version}_run{run}"

    # coverage.json
    cov_path = workdir / "coverage.json"
    cov = json.loads(cov_path.read_text()) if cov_path.exists() else {}

    # coverage.csv — last row for final values
    csv_path = workdir / "coverage.csv"
    final_edges = 0
    final_crashes = 0
    final_execs = 0
    if csv_path.exists():
        lines = csv_path.read_text().strip().split("\n")
        if len(lines) > 1:
            last = lines[-1].split(",")
            final_edges = int(last[1])
            final_crashes = int(last[2])
            final_execs = int(last[3])

    # triage_test.json
    triage_path = workdir / "triage_test.json"
    triage = json.loads(triage_path.read_text()) if triage_path.exists() else {}

    duration = cov.get("duration_seconds", 900)
    eps = final_execs / duration if duration > 0 and final_execs > 0 else None

    ubsan_crash_total = sum(c["count"] for c in triage.get("crashes", []))

    summary = {
        "campaign_id": campaign_id,
        "grammar": grammar,
        "sqlite_version": version,
        "run": run,
        "duration_sec": duration,
        "total_execs": final_execs,
        "execs_per_sec": round(eps, 1) if eps else None,
        "total_edges": final_edges,
        "total_signals": final_crashes,
        "ubsan_crashes": ubsan_crash_total,
        "unique_root_causes": triage.get("unique_crashes", 0),
        "asan_count": triage.get("summary", {}).get("asan", 0),
        "ubsan_count": triage.get("summary", {}).get("ubsan", 0),
        "queue_size": cov.get("queue_final", 0),
    }

    bug_rows = []
    for c in triage.get("crashes", []):
        bug_rows.append({
            "campaign_id": campaign_id,
            "grammar": grammar,
            "sqlite_version": version,
            "run": run,
            "bug_hash": c["hash"],
            "bug_type": c["type"],
            "bug_subtype": c["subtype"],
            "key_function": c["top_frames"][1] if len(c["top_frames"]) > 1 else "unknown",
            "crash_count": c["count"],
            "sample_sql": c.get("sql_preview", "")[:200],
        })

    ts_rows = []
    if csv_path.exists():
        lines = csv_path.read_text().strip().split("\n")
        for line in lines[1:]:
            parts = line.split(",")
            if len(parts) >= 4:
                ts_rows.append({
                    "campaign_id": campaign_id,
                    "grammar": grammar,
                    "sqlite_version": version,
                    "run": run,
                    "timestamp_sec": int(parts[0]),
                    "total_edges": int(parts[1]),
                    "total_crashes": int(parts[2]),
                    "exec_count": int(parts[3]),
                })

    return summary, bug_rows, ts_rows


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    summaries = []
    all_bugs = []
    all_ts = []

    for d in sorted(WORKDIR_BASE.iterdir()):
        m = CAMPAIGN_RE.match(d.name)
        if not m or not d.is_dir():
            continue
        version, grammar, run_n = m.groups()
        result = parse_campaign(d, version, grammar, int(run_n))
        if result is None:
            continue
        summary, bugs, ts = result
        summaries.append(summary)
        all_bugs.extend(bugs)
        all_ts.extend(ts)

    # Write campaigns_summary.csv
    summary_path = OUTPUT_DIR / "campaigns_summary.csv"
    summary_cols = [
        "campaign_id", "grammar", "sqlite_version", "run", "duration_sec",
        "total_execs", "execs_per_sec", "total_edges", "total_signals",
        "ubsan_crashes", "unique_root_causes", "asan_count", "ubsan_count", "queue_size",
    ]
    with open(summary_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=summary_cols)
        w.writeheader()
        w.writerows(summaries)
    print(f"campaigns_summary.csv: {len(summaries)} campaigns")

    # Write bug_classes.csv
    bugs_path = OUTPUT_DIR / "bug_classes.csv"
    bug_cols = [
        "campaign_id", "grammar", "sqlite_version", "run",
        "bug_hash", "bug_type", "bug_subtype", "key_function", "crash_count", "sample_sql",
    ]
    with open(bugs_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=bug_cols)
        w.writeheader()
        w.writerows(all_bugs)
    print(f"bug_classes.csv: {len(all_bugs)} bug entries")

    # Write timeseries.csv
    ts_path = OUTPUT_DIR / "timeseries.csv"
    ts_cols = [
        "campaign_id", "grammar", "sqlite_version", "run",
        "timestamp_sec", "total_edges", "total_crashes", "exec_count",
    ]
    with open(ts_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ts_cols)
        w.writeheader()
        w.writerows(all_ts)
    print(f"timeseries.csv: {len(all_ts)} rows")

    print(f"\nAll data written to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
