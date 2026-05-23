#!/usr/bin/env python3
"""
Generate Chapter 4 thesis figures for rl-nautilus-phase-2.

Run with:  uv run python scripts/generate_figures.py
"""

import csv
import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent.parent
WORKDIRS = ROOT / "workdirs"
RESULTS = ROOT / "results"
OUT_DIR = ROOT / "docs" / "thesis" / "v2" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

VERSIONS = ["3.30.1", "3.31.1", "3.32.0", "3.32.2"]
RUNS = list(range(1, 6))

# Brand colours
COLOR_V35 = "#2196F3"   # blue – DBMS-Nautilus
COLOR_EBNF = "#9E9E9E"  # grey – EBNF-Baseline

# ---------------------------------------------------------------------------
# Shared style
# ---------------------------------------------------------------------------
plt.rcParams.update({
    "font.family": "serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
})


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_triage(workdir: Path, prefer_test: bool = True) -> dict:
    """Load triage JSON, preferring triage_test.json if present."""
    if prefer_test:
        candidates = ["triage_test.json", "triage.json"]
    else:
        candidates = ["triage.json"]
    for name in candidates:
        p = workdir / name
        if p.exists():
            with open(p) as f:
                return json.load(f)
    raise FileNotFoundError(f"No triage JSON found in {workdir}")


def load_coverage_csv(workdir: Path) -> list[dict]:
    """Load coverage.csv rows as list of dicts."""
    p = workdir / "coverage.csv"
    with open(p) as f:
        return list(csv.DictReader(f))


def exec_idx_to_time(exec_idx: int, cov_rows: list[dict]) -> int | None:
    """Return timestamp (seconds) when exec_count first reached exec_idx."""
    for row in cov_rows:
        if int(row["exec_count"]) >= exec_idx:
            return int(row["timestamp_sec"])
    return None


def parse_exec_idx(sample_file: str) -> int:
    """Parse execution index from 'X_NNNNNNNNN' sample_file string."""
    return int(sample_file.split("_")[1])


# ---------------------------------------------------------------------------
# F1 – Time-to-first-CVE-crash (RQ1)
# ---------------------------------------------------------------------------

def gather_f1_data() -> dict[str, list[int]]:
    """
    For each CVE that was found, collect time-to-first-crash across all runs
    that found it.

    CVEs found in v35:
      CVE-2020-13434 – signed-integer-overflow in sqlite3_str_vappendf
      CVE-2020-13435 – null-pointer hash 9411c5875a64a648 (sqlite3.32.0)
      CVE-2020-15358 – INTERSECT pattern (sqlite 3.32.2)
    """
    cve_times: dict[str, list[int]] = {
        "CVE-2020-13434": [],
        "CVE-2020-13435": [],
        "CVE-2020-15358": [],
    }

    def is_cve13434(c: dict) -> bool:
        return (c.get("subtype") == "signed-integer-overflow"
                and any("vappendf" in f for f in c.get("top_frames", [])))

    def is_cve13435(c: dict) -> bool:
        return c.get("hash") == "9411c5875a64a648"

    def is_cve15358(c: dict) -> bool:
        # INTERSECT pattern crash on sqlite3.32.2
        return "INTERSECT" in c.get("sql_preview", "")

    predicates = {
        "CVE-2020-13434": is_cve13434,
        "CVE-2020-13435": is_cve13435,
        "CVE-2020-15358": is_cve15358,
    }

    for version in VERSIONS:
        for run in RUNS:
            workdir = WORKDIRS / f"sqlite-{version}_v35_run{run}"
            if not workdir.exists():
                continue
            try:
                triage = load_triage(workdir, prefer_test=True)
                cov_rows = load_coverage_csv(workdir)
            except FileNotFoundError:
                continue

            crashes = triage["crashes"]

            for cve, pred in predicates.items():
                matching = [c for c in crashes if pred(c)]
                if not matching:
                    continue
                first = min(matching, key=lambda c: parse_exec_idx(c["sample_file"]))
                exec_idx = parse_exec_idx(first["sample_file"])
                t = exec_idx_to_time(exec_idx, cov_rows)
                if t is not None:
                    cve_times[cve].append(t)

    return cve_times


def load_ttfc_csv() -> list[dict]:
    """Load the pre-computed TTFC-per-CVE CSV with both grammars."""
    p = RESULTS / "ch4_final" / "rq1_ttfc_per_cve.csv"
    with open(p) as f:
        return list(csv.DictReader(f))


def plot_f1(cve_times: dict[str, list[int]]) -> None:
    CAMPAIGN_CEIL = 900
    CVE_ORDER = ["CVE-2020-13434", "CVE-2020-13435", "CVE-2020-13871", "CVE-2020-15358"]

    rows = load_ttfc_csv()

    dbms_data: dict[str, list[int]] = {c: [] for c in CVE_ORDER}
    ebnf_data: dict[str, list[int]] = {c: [] for c in CVE_ORDER}

    for r in rows:
        cve = r["cve"]
        t = int(r["ttfc_sec"])
        if r["grammar"] == "DBMS-Nautilus":
            dbms_data[cve].append(t)
        else:
            ebnf_data[cve].append(t)

    fig, ax = plt.subplots(figsize=(9, 5.5))

    bar_width = 0.32
    x = np.arange(len(CVE_ORDER))
    rng = np.random.default_rng(42)

    dbms_medians = []
    ebnf_medians = []
    for cve in CVE_ORDER:
        dbms_medians.append(float(np.median(dbms_data[cve])) if dbms_data[cve] else 0)
        ebnf_medians.append(float(np.median(ebnf_data[cve])) if ebnf_data[cve] else CAMPAIGN_CEIL)

    bars_dbms = ax.bar(
        x - bar_width / 2, dbms_medians, bar_width,
        color=COLOR_V35, alpha=0.85, label="DBMS-Nautilus", zorder=2,
    )
    bars_ebnf = ax.bar(
        x + bar_width / 2, ebnf_medians, bar_width,
        color=COLOR_EBNF, alpha=0.85, label="EBNF-Baseline", zorder=2,
    )

    for i, cve in enumerate(CVE_ORDER):
        if dbms_data[cve]:
            jitter = rng.uniform(-0.06, 0.06, len(dbms_data[cve]))
            ax.scatter(
                [i - bar_width / 2 + j for j in jitter],
                dbms_data[cve],
                color="white", edgecolors=COLOR_V35, linewidths=1.0,
                s=28, zorder=4, alpha=0.9,
            )
            ax.text(
                i - bar_width / 2, -55,
                f"n={len(dbms_data[cve])}", ha="center", va="top",
                fontsize=8, color="#444",
            )

        if ebnf_data[cve]:
            jitter = rng.uniform(-0.06, 0.06, len(ebnf_data[cve]))
            ax.scatter(
                [i + bar_width / 2 + j for j in jitter],
                ebnf_data[cve],
                color="white", edgecolors=COLOR_EBNF, linewidths=1.0,
                s=28, zorder=4, alpha=0.9,
            )
            ax.text(
                i + bar_width / 2, -55,
                f"n={len(ebnf_data[cve])}", ha="center", va="top",
                fontsize=8, color="#444",
            )
        else:
            bars_ebnf[i].set_hatch("///")
            bars_ebnf[i].set_edgecolor("#666")
            bars_ebnf[i].set_alpha(0.35)
            ax.text(
                i + bar_width / 2, CAMPAIGN_CEIL / 2,
                "Not\nfound", ha="center", va="center",
                fontsize=10, color="#B71C1C", fontweight="bold",
                rotation=90,
            )

    short_labels = [c.replace("CVE-2020-", "CVE-") for c in CVE_ORDER]
    ax.set_xticks(x)
    ax.set_xticklabels(short_labels, fontsize=11)
    ax.set_ylabel("Time to first CVE crash (seconds)", fontsize=11)
    ax.set_xlabel("CVE", fontsize=11)
    ax.set_title(
        "Time to First CVE-Matching Crash: DBMS-Nautilus vs EBNF-Baseline",
        fontsize=12,
    )
    ax.set_ylim(-75, CAMPAIGN_CEIL + 50)
    ax.axhline(y=CAMPAIGN_CEIL, color="#B71C1C", linestyle="--", linewidth=0.8, alpha=0.4)
    ax.text(
        len(CVE_ORDER) - 0.15, CAMPAIGN_CEIL + 15,
        "campaign limit (900 s)", ha="right", va="bottom",
        fontsize=10, color="black", alpha=0.9, fontweight="bold",
    )
    ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
    ax.tick_params(labelsize=10)

    fig.tight_layout()
    out = OUT_DIR / "fig_4_1_time_to_first_cve.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"F1 saved → {out}")


# ---------------------------------------------------------------------------
# F2 – Bug class breakdown (RQ2)
# ---------------------------------------------------------------------------

def plot_f2() -> None:
    csv_path = RESULTS / "ch4_final" / "rq2_bug_classes.csv"
    with open(csv_path) as f:
        classes = list(csv.DictReader(f))

    classes = sorted(classes, key=lambda c: int(c["unique_hashes"]), reverse=True)

    labels = [c["class_id"] for c in classes]
    unique_hashes = [int(c["unique_hashes"]) for c in classes]
    severities = [c["severity"] for c in classes]
    has_cve = [bool(c["cve"].strip()) for c in classes]

    sev_colors = {"HIGH": "#F44336", "MEDIUM": "#FF9800", "LOW": "#4CAF50"}
    bar_colors = [sev_colors[s] for s in severities]

    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(labels))

    bars = ax.bar(x, unique_hashes, color=bar_colors, width=0.6, alpha=0.85,
                  edgecolor="white", linewidth=0.5)

    # Hatching for CVE-matching classes
    for bar, is_cve in zip(bars, has_cve):
        if is_cve:
            bar.set_hatch("///")
            bar.set_edgecolor("#333")
            bar.set_linewidth(0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9)
    ax.set_ylabel("Unique crash hashes", fontsize=12)
    ax.set_xlabel("Bug class", fontsize=12)
    ax.set_title("Bug Class Breakdown – DBMS-Nautilus (RQ2, 4 × 5 runs)", fontsize=12)
    ax.tick_params(labelsize=10)

    # Legend
    legend_handles = [
        mpatches.Patch(facecolor=sev_colors["HIGH"], label="HIGH severity"),
        mpatches.Patch(facecolor=sev_colors["MEDIUM"], label="MEDIUM severity"),
        mpatches.Patch(facecolor=sev_colors["LOW"], label="LOW severity"),
        mpatches.Patch(facecolor="#aaa", hatch="///", edgecolor="#333", label="CVE-matching"),
    ]
    ax.legend(handles=legend_handles, fontsize=9, loc="upper right")

    # Value labels on top of bars
    for bar, val in zip(bars, unique_hashes):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                str(val), ha="center", va="bottom", fontsize=8)

    fig.tight_layout()
    out = OUT_DIR / "fig_4_2_bug_class_breakdown.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"F2 saved → {out}")


# ---------------------------------------------------------------------------
# F3 – Coverage growth over time (RQ3)
# ---------------------------------------------------------------------------

def gather_coverage_series(workdir_pattern: str, label: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Collect per-second edge coverage for all matching workdirs.
    Returns (time_axis, mean_coverage, std_coverage) for 0-900 s.
    """
    T = 900
    all_series: list[np.ndarray] = []

    for workdir in sorted(WORKDIRS.iterdir()):
        if workdir_pattern not in workdir.name:
            continue
        cov_file = workdir / "coverage.csv"
        if not cov_file.exists():
            continue
        with open(cov_file) as f:
            rows = list(csv.DictReader(f))
        # Build dense array: index = second (0-based)
        series = np.zeros(T + 1)
        for row in rows:
            t = int(row["timestamp_sec"])
            if t <= T:
                series[t] = int(row["total_edges"])
        # Forward-fill zeros (no entry for a second means no change)
        for t in range(1, T + 1):
            if series[t] == 0:
                series[t] = series[t - 1]
        all_series.append(series)

    if not all_series:
        print(f"F3: no coverage data found for pattern '{workdir_pattern}'")
        return np.arange(T + 1), np.zeros(T + 1), np.zeros(T + 1)

    arr = np.stack(all_series)  # shape: (n_runs, T+1)
    t_axis = np.arange(T + 1)
    return t_axis, arr.mean(axis=0), arr.std(axis=0)


def plot_f3() -> None:
    t_v35, mean_v35, std_v35 = gather_coverage_series("_v35_run", "Proposed (v3.5)")
    t_ebnf, mean_ebnf, std_ebnf = gather_coverage_series("_comparison_ebnf_run", "EBNF")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(t_v35, mean_v35, color=COLOR_V35, linewidth=2, label="DBMS-Nautilus")
    ax.fill_between(t_v35, mean_v35 - std_v35, mean_v35 + std_v35,
                    color=COLOR_V35, alpha=0.15)

    ax.plot(t_ebnf, mean_ebnf, color=COLOR_EBNF, linewidth=2, label="EBNF-Baseline")
    ax.fill_between(t_ebnf, mean_ebnf - std_ebnf, mean_ebnf + std_ebnf,
                    color=COLOR_EBNF, alpha=0.15)

    ax.set_xlabel("Time (seconds)", fontsize=12)
    ax.set_ylabel("Cumulative edge coverage (edges)", fontsize=12)
    ax.set_title("Edge Coverage Growth (mean ± 1 std, 4 versions × 5 runs)", fontsize=11)
    ax.set_xlim(0, 900)
    ax.tick_params(labelsize=10)
    ax.legend(fontsize=11, loc="lower right")

    fig.tight_layout()
    out = OUT_DIR / "fig_4_3_coverage_growth.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"F3 saved → {out}")


# ---------------------------------------------------------------------------
# F4 – Throughput comparison (RQ3)
# ---------------------------------------------------------------------------

def gather_throughput(workdir_pattern: str) -> dict[str, list[float]]:
    """Return dict version -> list of execs_per_sec across runs."""
    by_version: dict[str, list[float]] = {v: [] for v in VERSIONS}

    for workdir in sorted(WORKDIRS.iterdir()):
        if workdir_pattern not in workdir.name:
            continue
        # Determine SQLite version from directory name
        matched_version = None
        for v in VERSIONS:
            if f"sqlite-{v}" in workdir.name:
                matched_version = v
                break
        if matched_version is None:
            continue

        cov_file = workdir / "coverage.csv"
        if not cov_file.exists():
            continue
        with open(cov_file) as f:
            rows = list(csv.DictReader(f))
        if not rows:
            continue
        last = rows[-1]
        total_execs = int(last["exec_count"])
        duration = int(last["timestamp_sec"])
        if duration > 0:
            eps = total_execs / duration
            by_version[matched_version].append(eps)

    return by_version


def plot_f4() -> None:
    # v3.5 throughput from workdirs
    v35_tput = gather_throughput("_v35_run")

    # EBNF throughput – prefer workdirs, fall back to campaigns_summary.csv
    ebnf_tput = gather_throughput("_comparison_ebnf_run")
    if all(len(v) == 0 for v in ebnf_tput.values()):
        # Load from campaigns_summary.csv
        csv_path = RESULTS / "comparison" / "data" / "campaigns_summary.csv"
        with open(csv_path) as f:
            rows = list(csv.DictReader(f))
        for row in rows:
            if row["grammar"] != "ebnf":
                continue
            ver = row["sqlite_version"].replace("sqlite-", "")
            if ver in ebnf_tput and "execs_per_sec" in row:
                ebnf_tput[ver].append(float(row["execs_per_sec"]))

    x = np.arange(len(VERSIONS))
    width = 0.35

    fig, ax = plt.subplots(figsize=(9, 5.5))

    v35_means = [np.mean(v35_tput[v]) if v35_tput[v] else 0 for v in VERSIONS]
    v35_stds  = [np.std(v35_tput[v])  if v35_tput[v] else 0 for v in VERSIONS]
    ebnf_means = [np.mean(ebnf_tput[v]) if ebnf_tput[v] else 0 for v in VERSIONS]
    ebnf_stds  = [np.std(ebnf_tput[v])  if ebnf_tput[v] else 0 for v in VERSIONS]

    bars_v35 = ax.bar(x - width / 2, v35_means, width, yerr=v35_stds,
                      label="DBMS-Nautilus", color=COLOR_V35, alpha=0.85,
                      capsize=4, error_kw=dict(elinewidth=1.2))
    bars_ebnf = ax.bar(x + width / 2, ebnf_means, width, yerr=ebnf_stds,
                       label="EBNF-Baseline", color=COLOR_EBNF, alpha=0.85,
                       edgecolor="#666",
                       capsize=4, error_kw=dict(elinewidth=1.2))

    ax.set_xticks(x)
    ax.set_xticklabels([f"SQLite {v}" for v in VERSIONS], fontsize=10)
    ax.set_ylabel("Executions per second", fontsize=12)
    ax.set_xlabel("SQLite version", fontsize=12)
    ax.set_title("Throughput Comparison (mean ± 1 std, 5 runs)", fontsize=11, pad=10)
    ax.tick_params(labelsize=10)

    ax.legend(fontsize=11, ncol=2, framealpha=0.95, edgecolor="black",
              fancybox=False, loc="upper center",
              bbox_to_anchor=(0.5, 1.18))
    fig.tight_layout()
    out = OUT_DIR / "fig_4_4_throughput.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"F4 saved → {out}")


# ---------------------------------------------------------------------------
# F5 – Time-to-first-real-crash (RQ3)
# ---------------------------------------------------------------------------

def gather_first_real_crash_times(workdir_pattern: str) -> dict[str, list[int]]:
    """
    For each SQLite version, return list of times (seconds) to first
    UBSan/ASan crash (NOT debug_assert / SIGNAL(5)) across all matching runs.
    """
    by_version: dict[str, list[int]] = {v: [] for v in VERSIONS}

    for workdir in sorted(WORKDIRS.iterdir()):
        if workdir_pattern not in workdir.name:
            continue
        matched_version = None
        for v in VERSIONS:
            if f"sqlite-{v}" in workdir.name:
                matched_version = v
                break
        if matched_version is None:
            continue

        try:
            triage = load_triage(workdir, prefer_test=True)
            cov_rows = load_coverage_csv(workdir)
        except FileNotFoundError:
            continue

        crashes = triage["crashes"]
        # Real crashes: ubsan or asan (not debug_assert)
        real = [c for c in crashes if c.get("type") in ("ubsan", "asan")]
        if not real:
            continue

        first = min(real, key=lambda c: parse_exec_idx(c["sample_file"]))
        exec_idx = parse_exec_idx(first["sample_file"])
        t = exec_idx_to_time(exec_idx, cov_rows)
        if t is not None:
            by_version[matched_version].append(t)

    return by_version


def plot_f5() -> None:
    v35_times  = gather_first_real_crash_times("_v35_run")
    ebnf_times = gather_first_real_crash_times("_comparison_ebnf_run")

    n_versions = len(VERSIONS)
    group_gap = 1.0
    box_width = 0.28

    fig, ax = plt.subplots(figsize=(10, 5.5))

    x = np.arange(len(VERSIONS))
    bar_width = 0.32
    rng = np.random.default_rng(42)

    v35_means = [np.mean(v35_times[v]) if v35_times[v] else 0 for v in VERSIONS]
    v35_stds  = [np.std(v35_times[v])  if v35_times[v] else 0 for v in VERSIONS]
    ebnf_means = [np.mean(ebnf_times[v]) if ebnf_times[v] else 0 for v in VERSIONS]
    ebnf_stds  = [np.std(ebnf_times[v])  if ebnf_times[v] else 0 for v in VERSIONS]

    bars1 = ax.bar(x - bar_width / 2, v35_means, bar_width, yerr=v35_stds,
                   label="DBMS-Nautilus", color=COLOR_V35, edgecolor="black",
                   linewidth=1.2, alpha=0.85, capsize=4,
                   error_kw=dict(elinewidth=1.2, capthick=1.2))
    bars2 = ax.bar(x + bar_width / 2, ebnf_means, bar_width, yerr=ebnf_stds,
                   label="EBNF-Baseline", color=COLOR_EBNF, edgecolor="black",
                   linewidth=1.2, alpha=0.85, capsize=4,
                   error_kw=dict(elinewidth=1.2, capthick=1.2))

    for i, v in enumerate(VERSIONS):
        if v35_times[v]:
            jitter = rng.uniform(-0.06, 0.06, len(v35_times[v]))
            ax.scatter(np.full(len(v35_times[v]), i - bar_width / 2) + jitter,
                      v35_times[v], color="white", edgecolors=COLOR_V35,
                      linewidths=1.0, s=30, zorder=4, alpha=0.9)
        if ebnf_times[v]:
            jitter = rng.uniform(-0.06, 0.06, len(ebnf_times[v]))
            ax.scatter(np.full(len(ebnf_times[v]), i + bar_width / 2) + jitter,
                      ebnf_times[v], color="white", edgecolors=COLOR_EBNF,
                      linewidths=1.0, s=30, zorder=4, alpha=0.9)

    ax.legend(fontsize=11, loc="upper left", framealpha=0.95,
              edgecolor="black", fancybox=False)

    ax.set_xticks(x)
    ax.set_xticklabels([f"SQLite {v}" for v in VERSIONS], fontsize=11)
    ax.set_ylabel("Time to first crash (seconds)", fontsize=12)
    ax.set_xlabel("SQLite version", fontsize=12)
    ax.set_title("Time to First Crash (mean ± 1 std, 5 runs per version)",
                 fontsize=12, fontweight="bold")
    ax.tick_params(labelsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.3, linestyle="--")

    fig.tight_layout()
    out = OUT_DIR / "fig_4_5_time_to_first_crash.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"F5 saved → {out}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"Output directory: {OUT_DIR}")

    print("\n--- F1: Time-to-first-CVE-crash ---")
    cve_times = gather_f1_data()
    for cve, times in cve_times.items():
        print(f"  {cve}: {len(times)} data points, times={sorted(times)}")
    plot_f1(cve_times)

    print("\n--- F2: Bug class breakdown ---")
    plot_f2()

    print("\n--- F3: Coverage growth ---")
    plot_f3()

    print("\n--- F4: Throughput comparison ---")
    plot_f4()

    print("\n--- F5: Time-to-first-real-crash ---")
    plot_f5()

    print("\nDone.")


if __name__ == "__main__":
    main()
