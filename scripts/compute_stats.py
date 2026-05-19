#!/usr/bin/env python3
"""
Statistical comparison: v3.5 grammar vs EBNF baseline for SQLite fuzzing.

Metrics per SQLite version (4 metrics × 4 versions = 16 tests):
  1. Throughput (execs/sec)
  2. Edge coverage (unique edges)
  3. Unique root causes (UBSan + ASan unique crashes from triage_test.json)
  4. Time-to-first-crash (seconds, from coverage.csv)

Tests per (metric, version) pair:
  - Mann-Whitney U (non-parametric, n=5 per group)
  - Cliff's delta effect size

Output: results/comparison/rq3_statistical_tests.csv
"""

import csv
import json
import math
import os
import sys
from pathlib import Path

import numpy as np
from scipy.stats import mannwhitneyu

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
WORKDIRS = ROOT / "workdirs"
V35_CSV = ROOT / "results" / "rq1_v35" / "campaigns_summary.csv"
EBNF_CSV = ROOT / "results" / "comparison" / "data" / "campaigns_summary.csv"
OUT_CSV = ROOT / "results" / "comparison" / "rq3_statistical_tests.csv"

VERSIONS = ["3.30.1", "3.31.1", "3.32.0", "3.32.2"]
RUNS = [1, 2, 3, 4, 5]
DURATION_SEC = 900  # all campaigns are 15-minute (900 s) runs

# ---------------------------------------------------------------------------
# Data extraction helpers
# ---------------------------------------------------------------------------


def last_exec_from_log(workdir: Path) -> float | None:
    """Return the last exec number from exec.log (= total executions)."""
    log = workdir / "exec.log"
    if not log.exists():
        return None
    last_line = None
    with open(log) as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                last_line = stripped
    if last_line is None:
        return None
    try:
        return float(last_line.split()[0])
    except (IndexError, ValueError):
        return None


def final_edges_from_coverage_csv(workdir: Path) -> float | None:
    """Return the final total_edges from coverage.csv."""
    cov = workdir / "coverage.csv"
    if not cov.exists():
        return None
    last_row = None
    with open(cov) as f:
        for row in csv.DictReader(f):
            last_row = row
    if last_row is None:
        return None
    try:
        return float(last_row["total_edges"])
    except (KeyError, ValueError):
        return None


def unique_real_bugs_from_triage_test(workdir: Path) -> int | None:
    """Count unique UBSan + ASan crashes from triage_test.json."""
    tj = workdir / "triage_test.json"
    if not tj.exists():
        return None
    with open(tj) as f:
        d = json.load(f)
    crashes = d.get("crashes", [])
    return sum(1 for c in crashes if c.get("type") in ("ubsan", "asan"))


def time_to_first_crash_from_coverage_csv(workdir: Path) -> float | None:
    """
    Return the first timestamp_sec where total_crashes > 0.
    This captures first detection of ANY crash (signal/debug assert/ubsan/asan)
    during the fuzzing campaign, measured in seconds.
    """
    cov = workdir / "coverage.csv"
    if not cov.exists():
        return None
    with open(cov) as f:
        for row in csv.DictReader(f):
            try:
                if int(row["total_crashes"]) > 0:
                    return float(row["timestamp_sec"])
            except (KeyError, ValueError):
                continue
    return None  # no crash detected


# ---------------------------------------------------------------------------
# Gather v3.5 data
# ---------------------------------------------------------------------------


def gather_v35_data() -> dict:
    """
    Returns dict keyed by version, each value a dict of lists for each metric.
    throughput: execs/sec (last_exec / DURATION_SEC)
    edges: final total_edges
    unique_bugs: UBSan+ASan unique crashes from triage_test.json
    ttfc: time-to-first-crash in seconds
    """
    data = {v: {"throughput": [], "edges": [], "unique_bugs": [], "ttfc": []} for v in VERSIONS}

    for version in VERSIONS:
        for run in RUNS:
            wdir = WORKDIRS / f"sqlite-{version}_v35_run{run}"
            if not wdir.exists():
                print(f"  WARNING: missing v35 workdir {wdir.name}", file=sys.stderr)
                continue

            # Throughput
            total_exec = last_exec_from_log(wdir)
            if total_exec is not None:
                data[version]["throughput"].append(total_exec / DURATION_SEC)
            else:
                print(f"  WARNING: no exec.log for {wdir.name}", file=sys.stderr)

            # Edge coverage
            edges = final_edges_from_coverage_csv(wdir)
            if edges is not None:
                data[version]["edges"].append(edges)
            else:
                print(f"  WARNING: no coverage.csv for {wdir.name}", file=sys.stderr)

            # Unique real bugs
            bugs = unique_real_bugs_from_triage_test(wdir)
            if bugs is not None:
                data[version]["unique_bugs"].append(bugs)
            else:
                print(f"  WARNING: no triage_test.json for {wdir.name}", file=sys.stderr)

            # Time to first crash
            ttfc = time_to_first_crash_from_coverage_csv(wdir)
            if ttfc is not None:
                data[version]["ttfc"].append(ttfc)
            else:
                # No crash at all in this run — use DURATION_SEC as censored value
                data[version]["ttfc"].append(float(DURATION_SEC))

    return data


# ---------------------------------------------------------------------------
# Gather EBNF data
# ---------------------------------------------------------------------------


def gather_ebnf_data() -> dict:
    """
    EBNF throughput and edges come from campaigns_summary.csv directly.
    Unique bugs and TTFC come from workdirs (same pattern as v35).
    EBNF 3.32.0 run1 workdir is missing — handled gracefully.
    """
    # Load campaigns_summary for throughput + edges
    csv_throughput = {v: [] for v in VERSIONS}
    csv_edges = {v: [] for v in VERSIONS}

    with open(EBNF_CSV) as f:
        for row in csv.DictReader(f):
            if row["grammar"] != "ebnf":
                continue
            # sqlite_version column uses "sqlite-X.Y.Z" format
            ver_raw = row["sqlite_version"]
            # Strip "sqlite-" prefix if present
            ver = ver_raw.replace("sqlite-", "")
            if ver not in VERSIONS:
                continue
            try:
                csv_throughput[ver].append(float(row["execs_per_sec"]))
                csv_edges[ver].append(float(row["total_edges"]))
            except (KeyError, ValueError) as e:
                print(f"  WARNING: EBNF CSV parse error for {row}: {e}", file=sys.stderr)

    data = {
        v: {
            "throughput": csv_throughput[v],
            "edges": csv_edges[v],
            "unique_bugs": [],
            "ttfc": [],
        }
        for v in VERSIONS
    }

    # Unique bugs + TTFC from workdirs
    for version in VERSIONS:
        for run in RUNS:
            wdir = WORKDIRS / f"sqlite-{version}_comparison_ebnf_run{run}"
            if not wdir.exists():
                print(
                    f"  INFO: missing EBNF workdir {wdir.name} — skipping bug/ttfc for this run",
                    file=sys.stderr,
                )
                # For missing workdir, use NaN as sentinel (will be excluded from lists)
                continue

            bugs = unique_real_bugs_from_triage_test(wdir)
            if bugs is not None:
                data[version]["unique_bugs"].append(bugs)

            ttfc = time_to_first_crash_from_coverage_csv(wdir)
            if ttfc is not None:
                data[version]["ttfc"].append(ttfc)
            else:
                data[version]["ttfc"].append(float(DURATION_SEC))

    return data


# ---------------------------------------------------------------------------
# Statistical tests
# ---------------------------------------------------------------------------


def cliffs_delta(a: list[float], b: list[float]) -> float:
    """
    Cliff's delta: d = (# pairs where a > b - # pairs where b > a) / (|a| * |b|)
    Positive d means 'a' tends to be larger.
    """
    n_a, n_b = len(a), len(b)
    if n_a == 0 or n_b == 0:
        return float("nan")
    n_greater = sum(1 for x in a for y in b if x > y)
    n_less = sum(1 for x in a for y in b if x < y)
    return (n_greater - n_less) / (n_a * n_b)


def effect_size_label(d: float) -> str:
    """Categorise |Cliff's d| using standard thresholds."""
    if math.isnan(d):
        return "N/A"
    ad = abs(d)
    if ad >= 0.474:
        return "large"
    if ad >= 0.330:
        return "medium"
    if ad >= 0.147:
        return "small"
    return "negligible"


def run_test(
    v35_vals: list[float],
    ebnf_vals: list[float],
) -> tuple[float, float, float, str]:
    """
    Returns (U_stat, p_value, cliffs_d, effect_label).
    Mann-Whitney U: H0 = distributions are equal, two-sided.
    """
    if len(v35_vals) < 2 or len(ebnf_vals) < 2:
        return float("nan"), float("nan"), float("nan"), "N/A"

    try:
        u_stat, p_val = mannwhitneyu(v35_vals, ebnf_vals, alternative="two-sided")
    except ValueError:
        u_stat, p_val = float("nan"), float("nan")

    d = cliffs_delta(v35_vals, ebnf_vals)
    label = effect_size_label(d)
    return u_stat, p_val, d, label


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    print("Gathering v3.5 data...")
    v35 = gather_v35_data()

    print("Gathering EBNF data...")
    ebnf = gather_ebnf_data()

    metrics = [
        ("throughput", "Throughput (execs/sec)"),
        ("edges", "Edge coverage (unique edges)"),
        ("unique_bugs", "Unique root causes (UBSan+ASan)"),
        ("ttfc", "Time-to-first-crash (seconds)"),
    ]

    rows = []
    for metric_key, metric_label in metrics:
        for version in VERSIONS:
            v35_vals = v35[version][metric_key]
            ebnf_vals = ebnf[version][metric_key]

            if not v35_vals:
                print(
                    f"  WARNING: no v35 data for {metric_key} / {version}",
                    file=sys.stderr,
                )
                continue
            if not ebnf_vals:
                print(
                    f"  WARNING: no EBNF data for {metric_key} / {version}",
                    file=sys.stderr,
                )
                continue

            v35_mean = float(np.mean(v35_vals))
            v35_std = float(np.std(v35_vals, ddof=1))
            ebnf_mean = float(np.mean(ebnf_vals))
            ebnf_std = float(np.std(ebnf_vals, ddof=1))

            u_stat, p_val, d, label = run_test(v35_vals, ebnf_vals)

            rows.append(
                {
                    "metric": metric_key,
                    "sqlite_version": version,
                    "v35_n": len(v35_vals),
                    "v35_mean": round(v35_mean, 4),
                    "v35_std": round(v35_std, 4),
                    "ebnf_n": len(ebnf_vals),
                    "ebnf_mean": round(ebnf_mean, 4),
                    "ebnf_std": round(ebnf_std, 4),
                    "U_statistic": round(u_stat, 4) if not math.isnan(u_stat) else "NaN",
                    "p_value": round(p_val, 6) if not math.isnan(p_val) else "NaN",
                    "cliffs_d": round(d, 4) if not math.isnan(d) else "NaN",
                    "effect_size": label,
                    # convenience: direction of v35 vs ebnf
                    "v35_vs_ebnf": (
                        "v35_higher" if v35_mean > ebnf_mean else "ebnf_higher"
                    ),
                }
            )

    # Write CSV
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "metric",
        "sqlite_version",
        "v35_n",
        "v35_mean",
        "v35_std",
        "ebnf_n",
        "ebnf_mean",
        "ebnf_std",
        "U_statistic",
        "p_value",
        "cliffs_d",
        "effect_size",
        "v35_vs_ebnf",
    ]
    with open(OUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nResults written to: {OUT_CSV}")

    # -----------------------------------------------------------------------
    # Pretty-print summary table
    # -----------------------------------------------------------------------
    print("\n" + "=" * 110)
    print("STATISTICAL COMPARISON: v3.5 grammar vs EBNF baseline")
    print(
        "Mann-Whitney U (two-sided, n=5 per group) + Cliff's delta effect size"
    )
    print("=" * 110)

    col_w = [22, 8, 14, 14, 12, 12, 12, 12]
    header = (
        f"{'Metric':<{col_w[0]}} {'Version':<{col_w[1]}} "
        f"{'v3.5 mean±std':<{col_w[2]}} {'EBNF mean±std':<{col_w[3]}} "
        f"{'U-stat':<{col_w[4]}} {'p-value':<{col_w[5]}} "
        f"{'Cliff d':<{col_w[6]}} {'Effect':<{col_w[7]}}"
    )
    print(header)
    print("-" * 110)

    for row in rows:
        m = row["metric"]
        v = row["sqlite_version"]
        v35_str = f"{row['v35_mean']:.2f}±{row['v35_std']:.2f}"
        ebnf_str = f"{row['ebnf_mean']:.2f}±{row['ebnf_std']:.2f}"
        u_str = f"{row['U_statistic']}"
        p_str = f"{row['p_value']}"
        d_str = f"{row['cliffs_d']}"
        eff = row["effect_size"]

        # Mark significant results
        try:
            p_float = float(p_str)
            sig_mark = " *" if p_float < 0.05 else "  "
        except ValueError:
            sig_mark = "  "

        print(
            f"{m:<{col_w[0]}} {v:<{col_w[1]}} "
            f"{v35_str:<{col_w[2]}} {ebnf_str:<{col_w[3]}} "
            f"{u_str:<{col_w[4]}} {p_str:<{col_w[5]}} "
            f"{d_str:<{col_w[6]}} {eff:<{col_w[7]}}{sig_mark}"
        )

    print("=" * 110)
    print("* p < 0.05 (two-sided Mann-Whitney U)")
    print()

    # -----------------------------------------------------------------------
    # Summary of significant findings
    # -----------------------------------------------------------------------
    sig_rows = [r for r in rows if _is_sig(r["p_value"])]
    print(f"Significant results (p < 0.05): {len(sig_rows)} / {len(rows)}")
    for r in sig_rows:
        dir_str = "v3.5 HIGHER" if r["v35_vs_ebnf"] == "v35_higher" else "EBNF HIGHER"
        print(
            f"  [{r['metric']} / sqlite-{r['sqlite_version']}] "
            f"p={r['p_value']}, d={r['cliffs_d']}, effect={r['effect_size']}, "
            f"direction: {dir_str}"
        )

    # Notes on data quality
    print()
    print("Notes:")
    print("  - EBNF sqlite-3.32.0 run1 workdir missing; unique_bugs/ttfc based on n=4 for that version.")
    print("  - ttfc = seconds until first ANY crash (debug assert, signal, UBSan, or ASan).")
    print("    This is an upper-bound proxy; UBSan-only ttfc would require replaying the triage queue.")
    print("  - Runs with no crash within 900 s are censored at 900 s (TTFC metric only).")
    print("  - Edge coverage for v3.5 taken from coverage.csv final row (direct bitmap count).")
    print("  - Edge coverage for EBNF taken from campaigns_summary.csv total_edges column.")
    print("  - Cliff's d > 0: v3.5 tends to score higher than EBNF.")


def _is_sig(p) -> bool:
    try:
        return float(p) < 0.05
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    main()
