#!/usr/bin/env python3
"""Generate 5 publication-quality charts from consolidated campaign data.

Reads: results/comparison/data/{campaigns_summary,bug_classes,timeseries}.csv
Outputs: results/comparison/figures/*.pdf
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "results" / "comparison" / "data"
FIG_DIR = ROOT / "results" / "comparison" / "figures"

BLUE = "#2196F3"
ORANGE = "#FF9800"
GRAMMAR_COLORS = {"v3.4": BLUE, "ebnf": ORANGE}
GRAMMAR_LABELS = {"v3.4": "Active (v3.4)", "ebnf": "Baseline (EBNF)"}
VERSION_LABELS = {
    "sqlite-3.30.1": "SQLite 3.30.1",
    "sqlite-3.31.1": "SQLite 3.31.1",
    "sqlite-3.32.0": "SQLite 3.32.0",
    "sqlite-3.32.2": "SQLite 3.32.2",
}
VERSIONS = ["sqlite-3.30.1", "sqlite-3.31.1", "sqlite-3.32.0", "sqlite-3.32.2"]
GRAMMARS = ["v3.4", "ebnf"]

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "figure.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
})


def mann_whitney(a: list, b: list) -> tuple[float, float]:
    if len(a) < 2 or len(b) < 2:
        return 0.0, 1.0
    try:
        stat, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        return stat, p
    except ValueError:
        return 0.0, 1.0


def p_label(p: float) -> str:
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "ns"


def chart1_unique_bugs(summary: pd.DataFrame) -> None:
    """Grouped bar chart: unique root causes per grammar × version."""
    fig, ax = plt.subplots(figsize=(7, 4.5))

    x = np.arange(len(VERSIONS))
    width = 0.3
    offsets = {"v3.4": -width / 2, "ebnf": width / 2}

    for grammar in GRAMMARS:
        means, stds, vals_list = [], [], []
        for version in VERSIONS:
            vals = summary[(summary.grammar == grammar) & (summary.sqlite_version == version)]["unique_root_causes"].values
            means.append(np.mean(vals))
            stds.append(np.std(vals, ddof=1) if len(vals) > 1 else 0)
            vals_list.append(vals)

        ax.bar(x + offsets[grammar], means, width, yerr=stds,
               label=GRAMMAR_LABELS[grammar], color=GRAMMAR_COLORS[grammar],
               alpha=0.85, capsize=4, edgecolor="black", linewidth=0.4)

    for i, version in enumerate(VERSIONS):
        a = summary[(summary.grammar == "v3.4") & (summary.sqlite_version == version)]["unique_root_causes"].values
        b = summary[(summary.grammar == "ebnf") & (summary.sqlite_version == version)]["unique_root_causes"].values
        _, p = mann_whitney(list(a), list(b))
        ymax = max(np.mean(a) + np.std(a, ddof=1), np.mean(b) + np.std(b, ddof=1)) if len(a) > 1 else max(a.max(), b.max())
        ax.text(i, ymax + 0.4, f"p={p:.3f} {p_label(p)}", ha="center", fontsize=9, color="gray")

    ax.set_xticks(x)
    ax.set_xticklabels([VERSION_LABELS[v] for v in VERSIONS])
    ax.set_ylabel("Unique Root Causes")
    ax.set_ylim(bottom=0)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    out = FIG_DIR / "unique_bugs_bar.pdf"
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
    print(f"  {out.name}")


def chart2_coverage_over_time(ts: pd.DataFrame) -> None:
    """Line plot: edge coverage over time with confidence bands."""
    nv = len(VERSIONS)
    ncols = min(nv, 2)
    nrows = (nv + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(6 * ncols, 4.5 * nrows), sharey=True)
    axes = np.atleast_1d(axes).flatten()

    for i, version in enumerate(VERSIONS):
        ax = axes[i]
        for grammar in GRAMMARS:
            subset = ts[(ts.grammar == grammar) & (ts.sqlite_version == version)]
            if subset.empty:
                continue

            grouped = subset.groupby("timestamp_sec")["total_edges"].agg(["mean", "std"]).reset_index()
            grouped["std"] = grouped["std"].fillna(0)

            ax.plot(grouped["timestamp_sec"], grouped["mean"],
                    color=GRAMMAR_COLORS[grammar], label=GRAMMAR_LABELS[grammar], linewidth=1.5)
            ax.fill_between(grouped["timestamp_sec"],
                          grouped["mean"] - grouped["std"],
                          grouped["mean"] + grouped["std"],
                          color=GRAMMAR_COLORS[grammar], alpha=0.15)

        ax.set_title(VERSION_LABELS[version])
        ax.set_xlabel("Time (seconds)")
        if i == 0:
            ax.set_ylabel("Total Edges")
        ax.legend(loc="lower right")
        ax.grid(alpha=0.3)

    plt.tight_layout()
    out = FIG_DIR / "coverage_over_time.pdf"
    plt.savefig(out)
    plt.close()
    print(f"  {out.name}")


def chart3_bug_breakdown(bugs: pd.DataFrame) -> None:
    """Horizontal grouped bar: bug subtypes per grammar × version."""
    nv = len(VERSIONS)
    ncols = min(nv, 2)
    nrows = (nv + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(6 * ncols, 4.5 * nrows))
    axes = np.atleast_1d(axes).flatten()

    for i, version in enumerate(VERSIONS):
        ax = axes[i]
        subset = bugs[bugs.sqlite_version == version].dropna(subset=["bug_subtype"])

        all_subtypes = sorted(subset["bug_subtype"].unique())
        if not all_subtypes:
            ax.set_title(VERSION_LABELS[version])
            ax.text(0.5, 0.5, "No bugs found", ha="center", va="center", transform=ax.transAxes)
            continue

        y = np.arange(len(all_subtypes))
        height = 0.35

        for j, grammar in enumerate(GRAMMARS):
            g_subset = subset[subset.grammar == grammar]
            agg = g_subset.groupby("bug_subtype")["crash_count"].sum().reindex(all_subtypes, fill_value=0)
            offset = -height / 2 if j == 0 else height / 2
            ax.barh(y + offset, agg.values, height,
                    label=GRAMMAR_LABELS[grammar], color=GRAMMAR_COLORS[grammar],
                    alpha=0.85, edgecolor="black", linewidth=0.4)

        ax.set_yticks(y)
        ax.set_yticklabels(all_subtypes, fontsize=9)
        ax.set_xlabel("Total Crash Count (sum of 5 runs)")
        ax.set_title(VERSION_LABELS[version])
        ax.legend(loc="lower right")
        ax.grid(axis="x", alpha=0.3)

    plt.tight_layout()
    out = FIG_DIR / "bug_class_breakdown.pdf"
    plt.savefig(out)
    plt.close()
    print(f"  {out.name}")


def chart4_crash_accumulation(ts: pd.DataFrame) -> None:
    """Line plot: crash accumulation over time."""
    nv = len(VERSIONS)
    ncols = min(nv, 2)
    nrows = (nv + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(6 * ncols, 4.5 * nrows), sharey=True)
    axes = np.atleast_1d(axes).flatten()

    for i, version in enumerate(VERSIONS):
        ax = axes[i]
        for grammar in GRAMMARS:
            subset = ts[(ts.grammar == grammar) & (ts.sqlite_version == version)]
            if subset.empty:
                continue

            grouped = subset.groupby("timestamp_sec")["total_crashes"].agg(["mean", "std"]).reset_index()
            grouped["std"] = grouped["std"].fillna(0)

            ax.plot(grouped["timestamp_sec"], grouped["mean"],
                    color=GRAMMAR_COLORS[grammar], label=GRAMMAR_LABELS[grammar], linewidth=1.5)
            ax.fill_between(grouped["timestamp_sec"],
                          grouped["mean"] - grouped["std"],
                          grouped["mean"] + grouped["std"],
                          color=GRAMMAR_COLORS[grammar], alpha=0.15)

        ax.set_title(VERSION_LABELS[version])
        ax.set_xlabel("Time (seconds)")
        if i == 0:
            ax.set_ylabel("Cumulative Crashes")
        ax.legend(loc="lower right")
        ax.grid(alpha=0.3)

    plt.tight_layout()
    out = FIG_DIR / "crash_accumulation.pdf"
    plt.savefig(out)
    plt.close()
    print(f"  {out.name}")


def chart5_throughput(summary: pd.DataFrame) -> None:
    """Grouped bar: executions per second."""
    fig, ax = plt.subplots(figsize=(7, 4.5))

    x = np.arange(len(VERSIONS))
    width = 0.3
    offsets = {"v3.4": -width / 2, "ebnf": width / 2}

    for grammar in GRAMMARS:
        means, stds = [], []
        for version in VERSIONS:
            vals = summary[(summary.grammar == grammar) & (summary.sqlite_version == version)]["execs_per_sec"].dropna().values
            means.append(np.mean(vals) if len(vals) > 0 else 0)
            stds.append(np.std(vals, ddof=1) if len(vals) > 1 else 0)

        ax.bar(x + offsets[grammar], means, width, yerr=stds,
               label=GRAMMAR_LABELS[grammar], color=GRAMMAR_COLORS[grammar],
               alpha=0.85, capsize=4, edgecolor="black", linewidth=0.4)

    ax.set_xticks(x)
    ax.set_xticklabels([VERSION_LABELS[v] for v in VERSIONS])
    ax.set_ylabel("Executions / second")
    ax.set_ylim(bottom=0)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    out = FIG_DIR / "throughput_bar.pdf"
    plt.savefig(out)
    plt.close()
    print(f"  {out.name}")


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    summary = pd.read_csv(DATA_DIR / "campaigns_summary.csv")
    bugs = pd.read_csv(DATA_DIR / "bug_classes.csv")
    ts = pd.read_csv(DATA_DIR / "timeseries.csv")

    print(f"Loaded: {len(summary)} campaigns, {len(bugs)} bug entries, {len(ts)} timeseries rows")
    print("\nGenerating charts...")

    chart1_unique_bugs(summary)
    chart2_coverage_over_time(ts)
    chart3_bug_breakdown(bugs)
    chart4_crash_accumulation(ts)
    chart5_throughput(summary)

    print(f"\nAll 5 charts saved to {FIG_DIR}/")


if __name__ == "__main__":
    main()
