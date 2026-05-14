#!/usr/bin/env python3
"""Generate publication-quality plots from comparison campaign metrics.

Reads: results/comparison/metrics.json
Outputs: results/comparison/figures/*.pdf
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
METRICS_PATH = ROOT / "results" / "comparison" / "metrics.json"
FIGURES_DIR = ROOT / "results" / "comparison" / "figures"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "figure.figsize": (7, 4.5),
    "figure.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
})

GRAMMAR_LABELS = {"v3.3": "Active (v3.3)", "ebnf": "Baseline (EBNF)"}
GRAMMAR_COLORS = {"v3.3": "#2196F3", "ebnf": "#FF9800"}
VERSION_LABELS = {
    "sqlite-3.31.1": "SQLite 3.31.1",
    "sqlite-3.32.2": "SQLite 3.32.2",
}


def load_metrics() -> dict:
    if not METRICS_PATH.exists():
        print(f"Error: {METRICS_PATH} not found. Run collect_metrics.py first.")
        sys.exit(1)
    return json.loads(METRICS_PATH.read_text())


def plot_boxplot(campaigns: list, metric: str, ylabel: str, filename: str):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), sharey=True)

    for i, version in enumerate(["sqlite-3.31.1", "sqlite-3.32.2"]):
        ax = axes[i]
        data = []
        colors = []
        labels = []
        for grammar in ["v3.3", "ebnf"]:
            values = [
                c[metric] for c in campaigns
                if c["grammar"] == grammar and c["version"] == version
            ]
            data.append(values)
            labels.append(GRAMMAR_LABELS[grammar])
            colors.append(GRAMMAR_COLORS[grammar])

        bp = ax.boxplot(data, labels=labels, patch_artist=True, widths=0.5)
        for patch, color in zip(bp["boxes"], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

        ax.set_title(VERSION_LABELS[version])
        ax.set_ylabel(ylabel if i == 0 else "")
        ax.grid(axis="y", alpha=0.3)

        if len(data[0]) >= 3 and len(data[1]) >= 3:
            try:
                _stat, p = stats.mannwhitneyu(data[0], data[1], alternative="two-sided")
                sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
                ax.text(0.5, 0.95, f"p={p:.3f} {sig}",
                        transform=ax.transAxes, ha="center", va="top",
                        fontsize=9, color="gray")
            except ValueError:
                pass

    plt.tight_layout()
    out = FIGURES_DIR / filename
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


def plot_coverage_growth(campaigns: list, filename: str):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), sharey=True)

    for i, version in enumerate(["sqlite-3.31.1", "sqlite-3.32.2"]):
        ax = axes[i]
        for grammar in ["v3.3", "ebnf"]:
            runs = [
                c for c in campaigns
                if c["grammar"] == grammar and c["version"] == version
            ]
            if not runs:
                continue

            all_curves = []
            max_exec = 0
            for r in runs:
                growth = r.get("coverage_growth", [])
                if growth:
                    xs = [g["exec_count"] for g in growth]
                    ys = [g["cumulative_edges"] for g in growth]
                    all_curves.append((xs, ys))
                    max_exec = max(max_exec, xs[-1] if xs else 0)

            if not all_curves or max_exec == 0:
                continue

            common_x = np.linspace(0, max_exec, 100)
            interpolated = []
            for xs, ys in all_curves:
                interp_y = np.interp(common_x, xs, ys)
                interpolated.append(interp_y)

            interpolated_arr = np.array(interpolated)
            mean_y = np.mean(interpolated_arr, axis=0)
            std_y = np.std(interpolated_arr, axis=0)

            color = GRAMMAR_COLORS[grammar]
            label = GRAMMAR_LABELS[grammar]
            ax.plot(common_x, mean_y, color=color, label=label, linewidth=1.5)
            ax.fill_between(common_x, mean_y - std_y, mean_y + std_y,
                          color=color, alpha=0.15)

        ax.set_title(VERSION_LABELS[version])
        ax.set_xlabel("Executions")
        ax.set_ylabel("Unique edges" if i == 0 else "")
        ax.legend(loc="lower right")
        ax.grid(alpha=0.3)

    plt.tight_layout()
    out = FIGURES_DIR / filename
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


def plot_throughput(campaigns: list, filename: str):
    fig, ax = plt.subplots(figsize=(7, 4))

    x_labels = []
    active_means = []
    baseline_means = []
    active_stds = []
    baseline_stds = []

    for version in ["sqlite-3.31.1", "sqlite-3.32.2"]:
        x_labels.append(VERSION_LABELS[version])
        for grammar, means_list, stds_list in [
            ("v3.3", active_means, active_stds),
            ("ebnf", baseline_means, baseline_stds),
        ]:
            values = [
                c["throughput_eps"] for c in campaigns
                if c["grammar"] == grammar and c["version"] == version
                and c["throughput_eps"] is not None
            ]
            means_list.append(float(np.mean(values)) if values else 0)
            stds_list.append(float(np.std(values)) if len(values) > 1 else 0)

    x = np.arange(len(x_labels))
    width = 0.35

    ax.bar(x - width/2, active_means, width, yerr=active_stds,
           label=GRAMMAR_LABELS["v3.3"], color=GRAMMAR_COLORS["v3.3"], alpha=0.8,
           capsize=4)
    ax.bar(x + width/2, baseline_means, width, yerr=baseline_stds,
           label=GRAMMAR_LABELS["ebnf"], color=GRAMMAR_COLORS["ebnf"], alpha=0.8,
           capsize=4)

    ax.set_ylabel("Executions / second")
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    out = FIGURES_DIR / filename
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


def run_statistical_tests(campaigns: list, output_path: Path):
    lines = ["Mann-Whitney U Test Results", "=" * 50, ""]

    metrics = [
        ("total_crashes", "Total Crashes"),
        ("unique_root_causes", "Unique Root Causes"),
        ("edge_coverage", "Edge Coverage (Queue Size)"),
    ]

    for version in ["sqlite-3.31.1", "sqlite-3.32.2"]:
        lines.append(f"\n{VERSION_LABELS[version]}")
        lines.append("-" * 40)

        for metric_key, metric_name in metrics:
            active = [
                c[metric_key] for c in campaigns
                if c["grammar"] == "v3.3" and c["version"] == version
            ]
            baseline = [
                c[metric_key] for c in campaigns
                if c["grammar"] == "ebnf" and c["version"] == version
            ]

            if len(active) < 2 or len(baseline) < 2:
                lines.append(f"  {metric_name}: insufficient data")
                continue

            try:
                stat, p = stats.mannwhitneyu(active, baseline, alternative="two-sided")
                n1, n2 = len(active), len(baseline)
                dominance = sum(
                    (1 if a > b else -1 if a < b else 0)
                    for a in active for b in baseline
                )
                cliff_d = dominance / (n1 * n2)
                effect = ("large" if abs(cliff_d) > 0.474 else
                         "medium" if abs(cliff_d) > 0.33 else
                         "small" if abs(cliff_d) > 0.147 else "negligible")

                lines.append(
                    f"  {metric_name}:\n"
                    f"    Active:   {np.mean(active):.1f} +/- {np.std(active):.1f}\n"
                    f"    Baseline: {np.mean(baseline):.1f} +/- {np.std(baseline):.1f}\n"
                    f"    U={stat:.1f}, p={p:.4f}, Cliff's d={cliff_d:.3f} ({effect})"
                )
            except ValueError as e:
                lines.append(f"  {metric_name}: error -- {e}")

    output_path.write_text("\n".join(lines))
    print(f"  Saved: {output_path}")


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    data = load_metrics()
    campaigns = data["campaigns"]

    if not campaigns:
        print("No campaigns found in metrics.json")
        sys.exit(1)

    print(f"Loaded {len(campaigns)} campaigns")
    print("\nGenerating plots...")

    plot_boxplot(campaigns, "total_crashes", "Total Crashes", "crash_counts_boxplot.pdf")
    plot_boxplot(campaigns, "unique_root_causes", "Unique Root Causes", "unique_rc_boxplot.pdf")
    plot_coverage_growth(campaigns, "coverage_growth.pdf")
    plot_throughput(campaigns, "throughput_comparison.pdf")
    run_statistical_tests(campaigns, FIGURES_DIR / "statistical_tests.txt")

    print("\nDone. All figures in results/comparison/figures/")


if __name__ == "__main__":
    main()
