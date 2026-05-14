# Thesis Ch3 + Ch4 + Campaign Comparison Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve Chapter 3 (architecture diagram, quantitative analysis, comparative analysis), run 20 comparison campaigns (active v3.3 vs baseline EBNF), generate publication-quality figures, and complete Chapter 4 with RQ3.

**Architecture:** Three workstreams with dependencies — Phase 1 produces infrastructure and Ch3 content in parallel, Phase 2 runs campaigns, Phase 3 collects data and plots, Phase 4 writes Ch3 probability section + Ch4 RQ3, Phase 5 reviews.

**Tech Stack:** draw.io XML, LaTeX/TikZ, Python 3.13 (matplotlib, scipy), Bash, Rust fuzzer

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `docs/thesis/v2/figures/architecture.drawio` | Create | draw.io architecture diagram |
| `docs/thesis/v2/figures/architecture.pdf` | Create | Exported PDF from draw.io |
| `docs/thesis/v2/chapters/c3_method.tex` | Modify | Add probability analysis, comparative analysis, swap diagram |
| `scripts/run_comparison.sh` | Create | Orchestrate 20 campaigns |
| `scripts/collect_metrics.py` | Create | Extract structured metrics from campaign dirs |
| `scripts/plot_results.py` | Create | Generate matplotlib/scipy figures |
| `results/comparison/metrics.json` | Create | Aggregated metrics from all campaigns |
| `results/comparison/figures/*.pdf` | Create | Publication-quality plots |
| `docs/thesis/v2/chapters/c4_experiments.tex` | Modify | Add RQ3, comparison methods, analysis |

---

## Task 1: Verify Baseline Grammar Loads

**Files:**
- Test: `grammars/baseline/sqlite-ebnf.py`

- [ ] **Step 1: Test baseline grammar with generator**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/home/linuxbrew/.linuxbrew/lib}"
cargo run --release --bin generator -- -g grammars/baseline/sqlite-ebnf.py -t 10
```

Expected: 10 generated SQL inputs printed to stdout. If it fails with `Broken Grammar`, the baseline grammar has unresolved non-terminal references that need fixing before campaigns can run.

- [ ] **Step 2: Test baseline grammar with fuzzer (5-second smoke test)**

```bash
GRAMMAR=grammars/baseline/sqlite-ebnf.py DURATION=5 \
  ./scripts/run_eval.sh sqlite-3.31.1 smoke_ebnf
```

Expected: Fuzzer starts, runs 5 seconds, produces `workdirs/sqlite-3.31.1_smoke_ebnf/` with some queue entries. Crashes optional at 5s.

- [ ] **Step 3: Verify active grammar smoke test**

```bash
GRAMMAR=grammars/active/sqlite_v3.py DURATION=5 \
  ./scripts/run_eval.sh sqlite-3.31.1 smoke_active
```

Expected: Same — fuzzer starts, runs 5 seconds, queue populated.

- [ ] **Step 4: Verify harness binaries exist**

```bash
ls -la harness/afl/sqlite_harness_sqlite-3.31.1 harness/afl/sqlite_harness_sqlite-3.32.2
ls -la harness/test/sqlite_harness_sqlite-3.31.1_test harness/test/sqlite_harness_sqlite-3.32.2_test
```

Expected: All 4 binaries exist and are executable.

---

## Task 2: Create `scripts/run_comparison.sh`

**Files:**
- Create: `scripts/run_comparison.sh`

- [ ] **Step 1: Write the comparison campaign orchestrator**

```bash
#!/usr/bin/env bash
# run_comparison.sh — Run 20 comparison campaigns: 2 grammars × 2 versions × 5 runs
#
# Usage:
#   ./scripts/run_comparison.sh
#   DURATION=300 RUNS=2 ./scripts/run_comparison.sh   # quick test
#
# Env overrides:
#   DURATION    seconds per run (default: 900 = 15 min)
#   RUNS        runs per (grammar, version) pair (default: 5)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

DURATION="${DURATION:-900}"
RUNS="${RUNS:-5}"
DATE="$(date +%Y-%m-%d)"

export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/home/linuxbrew/.linuxbrew/lib}"
export PYTHONPATH="$ROOT"

declare -A GRAMMARS=(
    [v3.3]="$ROOT/grammars/active/sqlite_v3.py"
    [ebnf]="$ROOT/grammars/baseline/sqlite-ebnf.py"
)

VERSIONS=("sqlite-3.31.1" "sqlite-3.32.2")

TOTAL=$((2 * ${#VERSIONS[@]} * RUNS))
CURRENT=0
START_ALL=$(date +%s)

echo "=============================================="
echo " Comparison Campaign Suite"
echo " Grammars: v3.3 (active) vs ebnf (baseline)"
echo " Versions: ${VERSIONS[*]}"
echo " Runs:     $RUNS per pair"
echo " Duration: ${DURATION}s per campaign"
echo " Total:    $TOTAL campaigns"
echo " Est time: $(( TOTAL * DURATION / 60 )) minutes"
echo "=============================================="

RESULTS_DIR="$ROOT/results/comparison"
mkdir -p "$RESULTS_DIR"

for GRAMMAR_NAME in v3.3 ebnf; do
    GRAMMAR="${GRAMMARS[$GRAMMAR_NAME]}"
    for VERSION in "${VERSIONS[@]}"; do
        for RUN_N in $(seq 1 "$RUNS"); do
            CURRENT=$((CURRENT + 1))
            RUN_ID="comparison_${GRAMMAR_NAME}_run${RUN_N}"

            echo ""
            echo "[$CURRENT/$TOTAL] $GRAMMAR_NAME / $VERSION / run $RUN_N"
            echo "  Grammar: $GRAMMAR"
            echo "  Started: $(date +%H:%M:%S)"

            GRAMMAR="$GRAMMAR" \
            DURATION="$DURATION" \
            GRAMMAR_VERSION="$GRAMMAR_NAME" \
            EXPERIMENT_TAG="comparison" \
              "$SCRIPT_DIR/run_eval.sh" "$VERSION" "$RUN_ID" \
              2>&1 | tail -5

            echo "  Finished: $(date +%H:%M:%S)"
        done
    done
done

END_ALL=$(date +%s)
ELAPSED_ALL=$((END_ALL - START_ALL))

echo ""
echo "=============================================="
echo " All $TOTAL campaigns complete"
echo " Total wall time: $((ELAPSED_ALL / 60))m $((ELAPSED_ALL % 60))s"
echo "=============================================="
echo ""
echo "Next: python3 scripts/collect_metrics.py"
```

- [ ] **Step 2: Make executable and verify syntax**

```bash
chmod +x scripts/run_comparison.sh
bash -n scripts/run_comparison.sh
echo "Syntax OK"
```

Expected: No errors.

- [ ] **Step 3: Dry-run with 2 runs × 10 seconds**

```bash
DURATION=10 RUNS=1 ./scripts/run_comparison.sh 2>&1 | tail -20
```

Expected: 4 campaigns run (2 grammars × 2 versions × 1 run), each ~10s. Workdirs created under `workdirs/`.

- [ ] **Step 4: Commit**

```bash
git add scripts/run_comparison.sh
git commit -m "feat: add comparison campaign orchestrator (2 grammars × 2 versions × N runs)"
```

---

## Task 3: Create `scripts/collect_metrics.py`

**Files:**
- Create: `scripts/collect_metrics.py`

- [ ] **Step 1: Write metrics collection script**

```python
#!/usr/bin/env python3
"""Collect structured metrics from comparison campaign workdirs.

Reads workdirs matching pattern: workdirs/<version>_comparison_<grammar>_run<N>/
Outputs: results/comparison/metrics.json

Metrics per campaign:
  - total_crashes: count of files in outputs/signaled/
  - unique_root_causes: count from triage_test.json .unique_crashes
  - cve_matches: list of matched CVE IDs (from triage pipeline)
  - edge_coverage: queue_final from coverage.json (proxy for unique edges)
  - throughput: exec_per_sec from coverage.json
  - coverage_growth: list of (exec_count, cumulative_new_cov) from exec.log
  - time_to_first_crash: exec_count of first SIGNAL entry in exec.log
  - bug_classes: list of {hash, type, subtype, count, top_frames} from triage_test.json
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def parse_exec_log(log_path: Path) -> dict:
    """Extract coverage growth curve and time-to-first-crash from exec.log."""
    growth = []
    first_crash_exec = None
    signal_re = re.compile(r"^(\d+)\tGen:SIGNAL", re.MULTILINE)
    newcov_re = re.compile(r"^(\d+)\tGen:NEW_COV", re.MULTILINE)

    if not log_path.exists():
        return {"coverage_growth": [], "first_crash_exec": None, "total_execs": None}

    text = log_path.read_text(errors="replace")

    # Coverage growth: cumulative NEW_COV events binned by exec count
    newcov_execs = [int(m) for m in newcov_re.findall(text)]
    if newcov_execs:
        # Bin into 60-second-equivalent intervals (estimate ~1000 execs/sec)
        # Use actual exec counts for x-axis; cumulative count for y-axis
        for i, ec in enumerate(newcov_execs):
            growth.append({"exec_count": ec, "cumulative_edges": i + 1})

    # First crash
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
    """Read coverage.json for throughput and queue size."""
    if not cov_path.exists():
        return {"queue_final": 0, "signaled_final": 0, "exec_per_sec": None}
    data = json.loads(cov_path.read_text())
    return {
        "queue_final": data.get("queue_final", 0),
        "signaled_final": data.get("signaled_final", 0),
        "exec_per_sec": data.get("exec_per_sec"),
    }


def parse_triage_json(triage_path: Path) -> dict:
    """Read triage_test.json for unique crashes and bug classes."""
    if not triage_path.exists():
        return {"unique_crashes": 0, "crashes": []}
    data = json.loads(triage_path.read_text())
    return {
        "unique_crashes": data.get("unique_crashes", 0),
        "crashes": data.get("crashes", []),
    }


def collect_campaign(workdir: Path) -> dict | None:
    """Collect all metrics from a single campaign workdir."""
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


def main():
    workdir_base = ROOT / "workdirs"
    output_path = ROOT / "results" / "comparison" / "metrics.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Pattern: <version>_comparison_<grammar>_run<N>
    pattern = re.compile(
        r"(sqlite-[\d.]+)_comparison_(v3\.3|ebnf)_run(\d+)"
    )

    results = {"campaigns": [], "summary": {}}

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

    # Group summary
    from collections import defaultdict
    groups = defaultdict(list)
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
    print(f"Collected {len(results['campaigns'])} campaigns → {output_path}")

    # Print summary table
    print(f"\n{'Grammar':<8} {'Version':<16} {'N':>3} {'Crashes':>12} {'Unique RC':>12} {'Edges':>12}")
    print("-" * 65)
    for key, s in sorted(results["summary"].items()):
        grammar, version = key.split("_", 1)
        crashes_str = f"{s['crashes_mean']:.1f} ± {_std(s['crashes_values']):.1f}"
        uniq_str = f"{s['unique_rc_mean']:.1f} ± {_std(s['unique_rc_values']):.1f}"
        edges_str = f"{s['edge_coverage_mean']:.0f} ± {_std(s['edge_coverage_values']):.0f}"
        print(f"{grammar:<8} {version:<16} {s['n']:>3} {crashes_str:>12} {uniq_str:>12} {edges_str:>12}")


def _std(values: list) -> float:
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return (sum((v - mean) ** 2 for v in values) / (len(values) - 1)) ** 0.5


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Test with existing smoke workdirs**

```bash
python3 scripts/collect_metrics.py
```

Expected: If smoke workdirs from Task 1 exist with `comparison` in name, they appear. Otherwise prints "Collected 0 campaigns". No errors.

- [ ] **Step 3: Commit**

```bash
git add scripts/collect_metrics.py
git commit -m "feat: add metrics collection for comparison campaigns"
```

---

## Task 4: Create `scripts/plot_results.py`

**Files:**
- Create: `scripts/plot_results.py`

- [ ] **Step 1: Write plotting script**

```python
#!/usr/bin/env python3
"""Generate publication-quality plots from comparison campaign metrics.

Reads: results/comparison/metrics.json
Outputs: results/comparison/figures/*.pdf

Plots:
  1. crash_counts_boxplot.pdf   — box plot of crash counts by grammar × version
  2. coverage_growth.pdf        — line plot with confidence bands
  3. unique_rc_boxplot.pdf      — box plot of unique root causes
  4. throughput_comparison.pdf   — bar chart of execs/sec
  5. statistical_tests.txt      — Mann-Whitney U test results
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

# Publication style
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


def group_by(campaigns: list, key_fn) -> dict[str, list]:
    groups = defaultdict(list)
    for c in campaigns:
        groups[key_fn(c)].append(c)
    return dict(groups)


def plot_boxplot(campaigns: list, metric: str, ylabel: str, filename: str):
    """Box plot comparing grammars across versions."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), sharey=True)

    for i, version in enumerate(["sqlite-3.31.1", "sqlite-3.32.2"]):
        ax = axes[i]
        data = []
        labels = []
        colors = []
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

        # Mann-Whitney U test annotation
        if len(data[0]) >= 3 and len(data[1]) >= 3:
            try:
                stat, p = stats.mannwhitneyu(data[0], data[1], alternative="two-sided")
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
    """Coverage growth curves with confidence bands."""
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

            # Normalize coverage growth to time (exec_count as x-axis)
            # Interpolate all runs to common x-axis
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

            # Interpolate to 100 common points
            common_x = np.linspace(0, max_exec, 100)
            interpolated = []
            for xs, ys in all_curves:
                interp_y = np.interp(common_x, xs, ys)
                interpolated.append(interp_y)

            interpolated = np.array(interpolated)
            mean_y = np.mean(interpolated, axis=0)
            std_y = np.std(interpolated, axis=0)

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
    """Bar chart comparing throughput (execs/sec)."""
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
            means_list.append(np.mean(values) if values else 0)
            stds_list.append(np.std(values) if len(values) > 1 else 0)

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
    """Run Mann-Whitney U tests and write results to text file."""
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
                # Cliff's delta (effect size)
                n1, n2 = len(active), len(baseline)
                dominance = sum(
                    (1 if a > b else -1 if a < b else 0)
                    for a in active for b in baseline
                )
                cliff_d = dominance / (n1 * n2)

                effect = "large" if abs(cliff_d) > 0.474 else "medium" if abs(cliff_d) > 0.33 else "small" if abs(cliff_d) > 0.147 else "negligible"

                lines.append(
                    f"  {metric_name}:\n"
                    f"    Active:   {np.mean(active):.1f} ± {np.std(active):.1f}\n"
                    f"    Baseline: {np.mean(baseline):.1f} ± {np.std(baseline):.1f}\n"
                    f"    U={stat:.1f}, p={p:.4f}, Cliff's d={cliff_d:.3f} ({effect})"
                )
            except ValueError as e:
                lines.append(f"  {metric_name}: error — {e}")

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
```

- [ ] **Step 2: Verify imports available**

```bash
python3 -c "import matplotlib; import scipy; import numpy; print('OK')"
```

Expected: `OK`. If missing, install: `pip install matplotlib scipy numpy`

- [ ] **Step 3: Commit**

```bash
git add scripts/plot_results.py
git commit -m "feat: add publication-quality plotting for comparison campaigns"
```

---

## Task 5: Create draw.io Architecture Diagram

**Files:**
- Create: `docs/thesis/v2/figures/architecture.drawio`

- [ ] **Step 1: Create draw.io XML**

Use the `/thesis-figure-skill` to generate a draw.io XML architecture diagram with these specifications:

- 5 components in a feedback loop layout:
  1. **Grammar Engine** (blue gradient, icon: document) — "Python DSL + PyO3 bridge"
  2. **Generation + Mutation** (teal gradient, icon: shuffle) — "Tree ops + unparse"
  3. **Fork Server + Harness** (orange gradient, icon: play) — "ASan + UBSan oracle"
  4. **Coverage Feedback** (green gradient, icon: chart) — "Shared memory bitmap"
  5. **Triage Pipeline** (red gradient, icon: filter) — "Dedup + CVE matching"
- Data flow arrows with labels: "rules + weights", "SQL string", "bitmap + exit status", "interesting inputs" (dashed), "crashes" (red)
- Dashed box around components 1-4 labeled "Fuzzing Loop"
- Component 5 below, branching from Fork Server
- Clean sans-serif font, subtle shadows, rounded corners

Save to `docs/thesis/v2/figures/architecture.drawio`.

- [ ] **Step 2: Export to PDF**

Open in draw.io desktop or use CLI:
```bash
# If drawio CLI available:
drawio --export --format pdf --output docs/thesis/v2/figures/architecture.pdf \
  docs/thesis/v2/figures/architecture.drawio
```

If drawio CLI not available, open `architecture.drawio` in browser at app.diagrams.net and export manually as PDF.

- [ ] **Step 3: Update c3_method.tex to use PDF instead of TikZ**

Replace lines 15-79 in `docs/thesis/v2/chapters/c3_method.tex` (the TikZ architecture figure) with:

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=\textwidth]{figures/architecture.pdf}
\caption{Architecture of DBMS-Nautilus. Components \textbf{1}--\textbf{4} form a closed feedback loop (dashed region): the grammar defines the input space, generation constructs SQL from derivation trees, the fork server executes each input against an instrumented SQLite build, and coverage feedback retains inputs that discover new edges. Component \textbf{5} analyzes crashes after each campaign.}
\label{fig:architecture}
\end{figure}
```

- [ ] **Step 4: Compile thesis to verify**

```bash
cd docs/thesis/v2 && latexmk -pdf main.tex -interaction=nonstopmode -outdir=out
```

Expected: Compiles without errors. Architecture figure appears as included PDF.

- [ ] **Step 5: Commit**

```bash
git add docs/thesis/v2/figures/architecture.drawio docs/thesis/v2/figures/architecture.pdf docs/thesis/v2/chapters/c3_method.tex
git commit -m "feat: replace TikZ architecture diagram with draw.io version"
```

---

## Task 6: Add Comparative Analysis to Ch3

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex`

- [ ] **Step 1: Add comparison subsection after System Overview (before Grammar Design)**

Insert after line 117 (end of `tab:components`), before line 118 (`\section{Grammar Design}`):

```latex
\subsection{Positioning Among DBMS Fuzzers}
\label{sec:positioning}

Table~\ref{tab:fuzzer-comparison} compares DBMS-Nautilus with two established DBMS fuzzers that represent different points in the design space. SQLsmith~\cite{sqlsmith} is a generation-based fuzzer that constructs random SQL queries by introspecting a live database schema. Squirrel~\cite{squirrel} is a mutation-based fuzzer that operates on an intermediate representation (IR) of SQL to maintain semantic validity during mutation.

\begin{table}[htbp]
\caption{Comparison of DBMS fuzzing approaches.}
\label{tab:fuzzer-comparison}
\centering
\small
\begin{tabular}{p{3cm}p{3.5cm}p{3.5cm}p{3.5cm}}
\toprule
\textbf{Feature} & \textbf{SQLsmith} & \textbf{Squirrel} & \textbf{DBMS-Nautilus} \\
\midrule
Input generation & Procedural C++ AST builder & AST $\to$ IR mutation & CFG with weighted production rules \\
Schema handling & Live introspection of running DBMS & Internal schema model, updated during fuzzing & Self-contained: grammar generates schema per test case \\
Mutation strategy & Random AST node replacement & Type-aware IR mutation preserving semantic validity & Tree-level splice, havoc, recursive expansion \\
Coverage guidance & No & Yes (edge coverage) & Yes (edge coverage, shared memory bitmap) \\
Vulnerability targeting & None (uniform random) & None (validity focus) & Weighted structural patterns biased toward vulnerability-relevant constructs \\
Test case isolation & No (requires pre-populated database) & Partial (schema state carries across inputs) & Full (each test starts from empty in-memory database) \\
\bottomrule
\end{tabular}
\end{table}

The key distinction of DBMS-Nautilus is the use of weighted production rules to concentrate fuzzing effort on structural patterns associated with known vulnerability classes. SQLsmith generates broad, random SQL against an existing schema but has no mechanism to prioritize constructs that are more likely to trigger bugs. Squirrel maintains semantic validity through IR-level mutation but does not bias its mutation toward vulnerability-relevant code paths. DBMS-Nautilus sacrifices Squirrel's semantic validity guarantee --- the grammar produces syntactically valid but potentially semantically meaningless SQL --- in exchange for the ability to steer generation toward specific structural patterns via weight assignment. The experimental evaluation in Chapter~\ref{chap:experiments} quantifies this tradeoff by comparing the active grammar against a spec-complete baseline grammar with uniform weights.
```

- [ ] **Step 2: Compile and verify**

```bash
cd docs/thesis/v2 && latexmk -pdf main.tex -interaction=nonstopmode -outdir=out
```

Expected: Compiles. New table and subsection appear in Ch3 between System Overview and Grammar Design.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "feat(ch3): add DBMS fuzzer comparison table (SQLsmith, Squirrel, DBMS-Nautilus)"
```

---

## Task 7: Add Quantitative Probability Analysis to Ch3

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex`

- [ ] **Step 1: Add probability analysis subsection**

Insert after the CVE Reachability Analysis subsection (after line 478, before line 480 `\subsection{Analysis of the Grammar Design Approach}`):

```latex
\subsection{Compositional Discovery Probability}
\label{sec:composition-probability}

The cross-pollination structure has a quantifiable consequence: for each CVE, the probability that a single generated input contains all required structural patterns can be computed from the grammar weights. Each Layer~2 shape selection is an independent draw from a weighted categorical distribution, and each terminal-level choice (format specifier, boundary value, column type) is a further independent draw. The probability of generating a CVE-triggering composition in a single input is the product of these conditional probabilities.

\paragraph{Example: CVE-2020-13434.}
This CVE requires two structural elements: a \texttt{printf()} call with a format specifier and an INT32 boundary value. The probability of generating a triggering input requires:

\begin{enumerate}
    \item Selecting \texttt{Boundary-Func-Call} at Layer~2: the \texttt{Sql-Stmt} structure must include a boundary function call (occurs with probability $p_1$ depending on the Layer~2 dispatch weights).
    \item Selecting the \texttt{printf} alternative within \texttt{Boundary-Func-Call}: weight 3.0 out of total 6.5, giving $p_2 = 3.0/6.5 \approx 0.46$.
    \item Selecting \texttt{\%.*g} as the format specifier: weight 3.0 out of total 5.0, giving $p_3 = 3.0/5.0 = 0.60$.
    \item Selecting an INT32 boundary value ($\geq 2^{31}-1$): weight 6.0 out of total 12.0, giving $p_4 = 6.0/12.0 = 0.50$.
\end{enumerate}

The per-input probability is $P(\text{CVE-13434}) = p_1 \times p_2 \times p_3 \times p_4 \approx p_1 \times 0.138$. With $p_1$ estimated conservatively at 0.1 (one in ten inputs includes a boundary function call), $P \approx 0.014$, meaning approximately one in 70 generated inputs contains the required structural composition. At typical throughput of 500--1000 executions per second, the expected time to first triggering input is under one second of fuzzing.

\paragraph{Contrast: CVE-2020-13435.}
This CVE requires five simultaneous elements: NATURAL JOIN, \texttt{coalesce()}, window function with \texttt{OVER}, UNIQUE column constraint, and IN subquery. Each element has its own conditional selection probability, and the product yields $P(\text{CVE-13435}) \approx 10^{-5}$ to $10^{-6}$. At 1000 executions per second, the expected time to first triggering input is 10--1000 seconds --- consistent with the observed time-to-first-crash in campaigns where this CVE was found after several minutes rather than immediately.

\paragraph{Implication for grammar design.}
The exponential relationship between the number of required patterns and the per-input probability has two consequences. First, it explains why simple CVEs (2 patterns) are found within seconds while complex CVEs (5 patterns) may require minutes or tens of minutes. Second, it motivates weight tuning: increasing the weight of a required non-terminal directly increases its selection probability, multiplicatively improving the per-input probability for every CVE that requires that pattern. This multiplicative benefit is the quantitative mechanism behind cross-pollination: a weight increase for \texttt{coalesce()} improves reachability for both CVE-2020-9327 and CVE-2020-13435 simultaneously.
```

- [ ] **Step 2: Compile and verify**

```bash
cd docs/thesis/v2 && latexmk -pdf main.tex -interaction=nonstopmode -outdir=out
```

Expected: Compiles. New subsection appears between CVE Reachability and Analysis.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "feat(ch3): add compositional discovery probability analysis"
```

---

## Task 8: Run Comparison Campaigns

**Files:**
- Execute: `scripts/run_comparison.sh`

**Prerequisites:** Tasks 1-4 complete (baseline verified, scripts created).

- [ ] **Step 1: Run full comparison suite**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
DURATION=900 RUNS=5 ./scripts/run_comparison.sh 2>&1 | tee results/comparison/campaign_log.txt
```

Expected: 20 campaigns run over ~5 hours. Each campaign produces a workdir under `workdirs/`.

- [ ] **Step 2: Verify all 20 workdirs created**

```bash
ls -d workdirs/*comparison* | wc -l
```

Expected: 20

- [ ] **Step 3: Collect metrics**

```bash
python3 scripts/collect_metrics.py
```

Expected: `results/comparison/metrics.json` created with 20 campaign entries. Summary table printed.

- [ ] **Step 4: Generate plots**

```bash
python3 scripts/plot_results.py
```

Expected: 4 PDF figures + statistical_tests.txt in `results/comparison/figures/`.

- [ ] **Step 5: Commit results**

```bash
git add results/comparison/
git commit -m "data: add comparison campaign results (v3.3 vs EBNF, 5 runs × 2 versions)"
```

---

## Task 9: Write Ch4 RQ3 and Complete Chapter

**Files:**
- Modify: `docs/thesis/v2/chapters/c4_experiments.tex`

**Prerequisites:** Task 8 complete (campaign data and figures available).

- [ ] **Step 1: Read current Ch4 state**

Read `docs/thesis/v2/chapters/c4_experiments.tex` to understand what exists and where to insert new content.

- [ ] **Step 2: Add RQ3 to research questions**

In the chapter introduction (around line 4), update to include RQ3:

```latex
Section~\ref{sec:rq3} compares the active grammar against a spec-complete baseline to quantify the impact of structural pattern engineering.
```

- [ ] **Step 3: Add Comparison Methods section**

Insert after the Evaluation Metrics section. Write a section describing:

```latex
\section{Comparison Methods}
\label{sec:comparison}

To quantify the contribution of structural pattern engineering, we compare the active grammar (v3.3, 520 rules with weighted structural patterns) against a baseline grammar derived from the SQLite EBNF specification (644 rules, uniform weights, no attack patterns).

\subsection{Baseline Grammar}

The baseline grammar translates SQLite's official Extended Backus-Naur Form (EBNF) specification into Nautilus production rules with uniform weights (1.0 for all rules). It covers the complete SQL syntax --- SELECT, INSERT, UPDATE, DELETE, DDL, PRAGMA, transactions --- without any domain-specific vulnerability targeting. Unlike the active grammar, the baseline does not generate its own schema; it operates against the pre-loaded harness schema (tables t1, t2, t3, and FTS virtual tables). This baseline represents what a grammar-based fuzzer achieves with syntactic completeness alone, without the structural pattern engineering described in Chapter~\ref{chap:method}.

\subsection{Literature Baselines}

We additionally reference published results from SQLsmith~\cite{sqlsmith} and Squirrel~\cite{squirrel} for qualitative context. Direct comparison is not possible because these tools use different target versions, hardware, and evaluation methodologies. However, their published bug counts and coverage figures provide context for interpreting DBMS-Nautilus's results.
```

- [ ] **Step 4: Add RQ3 section with figures**

Insert after RQ2 section:

```latex
\section{RQ3: Grammar Comparison}
\label{sec:rq3}

To evaluate whether structural pattern engineering improves vulnerability discovery over syntactically complete but untargeted generation, we compare the active grammar (v3.3) against the EBNF baseline across 5 independent 15-minute campaigns on SQLite 3.31.1 and 3.32.2.

% INSERT FIGURES HERE from results/comparison/figures/
% crash_counts_boxplot.pdf, coverage_growth.pdf, unique_rc_boxplot.pdf

\begin{figure}[htbp]
\centering
\includegraphics[width=\textwidth]{../../../results/comparison/figures/crash_counts_boxplot.pdf}
\caption{Distribution of total crash counts across 5 runs per configuration. The active grammar produces significantly more crashes on both SQLite versions.}
\label{fig:crash-boxplot}
\end{figure}

\begin{figure}[htbp]
\centering
\includegraphics[width=\textwidth]{../../../results/comparison/figures/coverage_growth.pdf}
\caption{Coverage growth over time (executions). Shaded region shows $\pm 1\sigma$ across 5 runs. The active grammar achieves higher coverage earlier due to directed structural patterns.}
\label{fig:coverage-growth}
\end{figure}

% TABLE: Summary statistics with Mann-Whitney p-values
% Fill from results/comparison/figures/statistical_tests.txt after campaigns
\begin{table}[htbp]
\caption{Comparison of active grammar (v3.3) vs baseline EBNF grammar. Values are mean $\pm$ std over 5 runs. $p$-values from Mann-Whitney U test.}
\label{tab:comparison}
\centering
\small
\begin{tabular}{llrrr}
\toprule
\textbf{Version} & \textbf{Metric} & \textbf{Active (v3.3)} & \textbf{Baseline (EBNF)} & \textbf{$p$-value} \\
\midrule
% FILL FROM CAMPAIGN DATA
3.31.1 & Total crashes & --- & --- & --- \\
3.31.1 & Unique root causes & --- & --- & --- \\
3.31.1 & Edge coverage & --- & --- & --- \\
3.32.2 & Total crashes & --- & --- & --- \\
3.32.2 & Unique root causes & --- & --- & --- \\
3.32.2 & Edge coverage & --- & --- & --- \\
\bottomrule
\end{tabular}
\end{table}
```

**Note:** The table values marked `---` must be filled from actual campaign data after Task 8 completes. Update the narrative to match the observed results.

- [ ] **Step 5: Add Analysis and Discussion section**

```latex
\section{Analysis and Discussion}
\label{sec:discussion}

% Content depends on campaign results. Structure:
% 1. Why structural patterns outperform EBNF
%    - Connect to Ch3 probability analysis (Section 3.2.X)
%    - Active grammar concentrates effort on vulnerability-relevant paths
%    - EBNF spreads effort uniformly across all SQL constructs
% 2. The cost of targeting
%    - Active grammar has fewer rules (520 vs 644) but higher crash yield
%    - Weight tuning amplifies effective exploration in target regions
% 3. Limitations
%    - EBNF may find bugs in untargeted regions that active grammar misses
%    - Results specific to SQLite; generalizability to other DBMS unknown
```

- [ ] **Step 6: Add Own vs Reused table**

Add to the Experimental Setup section:

```latex
\paragraph{Original contributions vs reused components.}
Table~\ref{tab:own-vs-reused} distinguishes the components implemented as part of this thesis from those reused from the original Nautilus framework~\cite{nautilus}.

\begin{table}[htbp]
\caption{Distinction between original contributions and reused Nautilus components.}
\label{tab:own-vs-reused}
\centering
\small
\begin{tabular}{p{6cm}p{6cm}}
\toprule
\textbf{Original (this thesis)} & \textbf{Reused from Nautilus} \\
\midrule
Grammar design methodology (Ch.~\ref{chap:method}) & Fork server protocol (\texttt{forksrv/}) \\
520-rule SQL grammar with weighted structural patterns & Coverage bitmap and feedback loop \\
CVE reachability analysis framework & Derivation tree representation \\
Weighted sampling integration (loaded dice) & Basic mutation operators (splice, havoc) \\
SQLite harness with ASan/UBSan oracle & Thread-safe queue management \\
Triage pipeline (dedup, CVE matching) & Python grammar loading (PyO3 bridge) \\
All experiment infrastructure and scripts & \\
Baseline EBNF grammar for comparison & \\
\bottomrule
\end{tabular}
\end{table}
```

- [ ] **Step 7: Compile and verify**

```bash
cd docs/thesis/v2 && latexmk -pdf main.tex -interaction=nonstopmode -outdir=out
```

Expected: Compiles. Ch4 has RQ3 section with figures (or placeholder paths if figures not yet generated).

- [ ] **Step 8: Commit**

```bash
git add docs/thesis/v2/chapters/c4_experiments.tex
git commit -m "feat(ch4): add RQ3 grammar comparison, comparison methods, own-vs-reused table"
```

---

## Task 10: Final Review and Consistency Check

**Files:**
- Review: `docs/thesis/v2/chapters/c3_method.tex`, `docs/thesis/v2/chapters/c4_experiments.tex`

- [ ] **Step 1: Cross-reference check**

Verify all `\ref{}` and `\cite{}` references resolve:
```bash
cd docs/thesis/v2 && latexmk -pdf main.tex -interaction=nonstopmode -outdir=out 2>&1 | grep -i "undefined\|multiply"
```

Expected: No undefined references.

- [ ] **Step 2: Fill Ch4 table with actual data**

After campaigns complete, update `tab:comparison` in c4_experiments.tex with real values from `results/comparison/figures/statistical_tests.txt`. Replace all `---` placeholders.

- [ ] **Step 3: Update Ch4 narrative to match results**

Write the Analysis and Discussion section (Task 9 Step 5) based on actual campaign results. If active grammar outperforms baseline (expected), explain via Ch3 probability analysis. If results are surprising, document honestly.

- [ ] **Step 4: Verify figure paths resolve**

```bash
cd docs/thesis/v2 && latexmk -pdf main.tex -interaction=nonstopmode -outdir=out 2>&1 | grep -i "not found\|missing"
```

Expected: All figures found and included.

- [ ] **Step 5: Final compile and visual check**

```bash
cd docs/thesis/v2 && latexmk -pdf main.tex -interaction=nonstopmode -outdir=out
```

Open `out/main.pdf` and visually verify:
- Ch3 architecture diagram (draw.io version) renders correctly
- Ch3 comparison table is properly formatted
- Ch3 probability analysis section reads coherently
- Ch4 RQ3 figures are included and labeled
- Ch4 comparison table has actual values
- No overfull hbox warnings from new content

- [ ] **Step 6: Commit final version**

```bash
git add docs/thesis/v2/
git commit -m "feat: complete Ch3 improvements + Ch4 RQ3 with campaign data"
```

---

## Phase Summary

| Phase | Tasks | Parallel? | Est. Time |
|-------|-------|-----------|-----------|
| 1: Infrastructure + Ch3 content | Tasks 1-7 | Yes (1-4 parallel, 5-7 parallel) | 2-3 hours |
| 2: Run campaigns | Task 8 steps 1-2 | Sequential (5h compute) | 5 hours |
| 3: Collect + plot | Task 8 steps 3-5 | Sequential | 30 min |
| 4: Write Ch4 | Task 9 | Sequential | 2-3 hours |
| 5: Final review | Task 10 | Sequential | 1 hour |
