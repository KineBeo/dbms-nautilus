#!/usr/bin/env python3
"""Collect structured metrics from comparison campaign workdirs.

Reads workdirs matching: workdirs/<version>_comparison_<grammar>_run<N>/
Outputs: results/comparison/metrics.json
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def parse_exec_log(log_path: Path) -> dict:
    growth = []
    first_crash_exec = None
    signal_re = re.compile(r"^(\d+)\tGen:SIGNAL", re.MULTILINE)
    newcov_re = re.compile(r"^(\d+)\tGen:NEW_COV", re.MULTILINE)

    if not log_path.exists():
        return {"coverage_growth": [], "first_crash_exec": None, "total_execs": None}

    text = log_path.read_text(errors="replace")

    newcov_execs = [int(m) for m in newcov_re.findall(text)]
    if newcov_execs:
        for i, ec in enumerate(newcov_execs):
            growth.append({"exec_count": ec, "cumulative_edges": i + 1})

    signal_execs = [int(m) for m in signal_re.findall(text)]
    if signal_execs:
        first_crash_exec = min(signal_execs)

    total = max(newcov_execs[-1] if newcov_execs else 0,
                signal_execs[-1] if signal_execs else 0,
                0)

    return {
        "coverage_growth": growth,
        "first_crash_exec": first_crash_exec,
        "total_execs": total if total > 0 else None,
    }


def parse_coverage_json(cov_path: Path) -> dict:
    if not cov_path.exists():
        return {"queue_final": 0, "signaled_final": 0, "exec_per_sec": None}
    data = json.loads(cov_path.read_text())
    return {
        "queue_final": data.get("queue_final", 0),
        "signaled_final": data.get("signaled_final", 0),
        "exec_per_sec": data.get("exec_per_sec"),
    }


def parse_triage_json(triage_path: Path) -> dict:
    if not triage_path.exists():
        return {"unique_crashes": 0, "crashes": []}
    data = json.loads(triage_path.read_text())
    return {
        "unique_crashes": data.get("unique_crashes", 0),
        "crashes": data.get("crashes", []),
    }


def collect_campaign(workdir: Path) -> dict | None:
    cov = parse_coverage_json(workdir / "coverage.json")
    triage = parse_triage_json(workdir / "triage_test.json")
    execlog = parse_exec_log(workdir / "exec.log")

    return {
        "workdir": str(workdir),
        "total_crashes": cov["signaled_final"],
        "unique_root_causes": triage["unique_crashes"],
        "edge_coverage": cov["queue_final"],
        "throughput_eps": cov["exec_per_sec"],
        "first_crash_exec": execlog["first_crash_exec"],
        "total_execs": execlog["total_execs"],
        "coverage_growth": execlog["coverage_growth"],
        "bug_classes": [
            {
                "hash": c["hash"],
                "type": c["type"],
                "subtype": c["subtype"],
                "count": c["count"],
                "key_function": c["top_frames"][1] if len(c["top_frames"]) > 1 else "unknown",
            }
            for c in triage["crashes"]
        ],
    }


def _std(values: list) -> float:
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return (sum((v - mean) ** 2 for v in values) / (len(values) - 1)) ** 0.5


def main():
    workdir_base = ROOT / "workdirs"
    output_path = ROOT / "results" / "comparison" / "metrics.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pattern = re.compile(
        r"(sqlite-[\d.]+)_comparison_(v3\.3|ebnf)_run(\d+)"
    )

    results: dict = {"campaigns": [], "summary": {}}

    for d in sorted(workdir_base.iterdir()):
        m = pattern.match(d.name)
        if not m or not d.is_dir():
            continue

        version, grammar, run_n = m.groups()
        metrics = collect_campaign(d)
        if metrics is None:
            continue

        metrics["version"] = version
        metrics["grammar"] = grammar
        metrics["run"] = int(run_n)
        results["campaigns"].append(metrics)

    groups: dict[str, list] = defaultdict(list)
    for c in results["campaigns"]:
        key = f"{c['grammar']}_{c['version']}"
        groups[key].append(c)

    for key, campaigns in groups.items():
        crashes = [c["total_crashes"] for c in campaigns]
        uniq = [c["unique_root_causes"] for c in campaigns]
        edges = [c["edge_coverage"] for c in campaigns]
        results["summary"][key] = {
            "n": len(campaigns),
            "crashes_mean": sum(crashes) / len(crashes) if crashes else 0,
            "crashes_values": crashes,
            "unique_rc_mean": sum(uniq) / len(uniq) if uniq else 0,
            "unique_rc_values": uniq,
            "edge_coverage_mean": sum(edges) / len(edges) if edges else 0,
            "edge_coverage_values": edges,
        }

    output_path.write_text(json.dumps(results, indent=2))
    print(f"Collected {len(results['campaigns'])} campaigns -> {output_path}")

    print(f"\n{'Grammar':<8} {'Version':<16} {'N':>3} {'Crashes':>12} {'Unique RC':>12} {'Edges':>12}")
    print("-" * 65)
    for key, s in sorted(results["summary"].items()):
        grammar, version = key.split("_", 1)
        crashes_str = f"{s['crashes_mean']:.1f} +/- {_std(s['crashes_values']):.1f}"
        uniq_str = f"{s['unique_rc_mean']:.1f} +/- {_std(s['unique_rc_values']):.1f}"
        edges_str = f"{s['edge_coverage_mean']:.0f} +/- {_std(s['edge_coverage_values']):.0f}"
        print(f"{grammar:<8} {version:<16} {s['n']:>3} {crashes_str:>12} {uniq_str:>12} {edges_str:>12}")


if __name__ == "__main__":
    main()
