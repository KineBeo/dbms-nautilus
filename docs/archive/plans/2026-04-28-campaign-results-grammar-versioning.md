# Campaign Results Storage & Grammar Versioning — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Structured storage for campaign results and grammar version snapshots so thesis paper tables and experiment comparisons are reproducible and easy to generate.

**Architecture:** Grammar versions are immutable snapshots under `grammars/vX.Y/`. Campaign results archive metadata + dedup + attribution under `results/campaigns/{auto-id}/`. An `experiments.json` registry maps experiment tags to campaign IDs. Scripts auto-archive after each campaign run.

**Tech Stack:** Bash (run_eval.sh, run_ablation.sh, archive_campaign.sh), Python 3.13 (compare_campaigns.py), JSON (campaign.json, meta.json, experiments.json)

---

## File Structure

| File | Responsibility |
|------|----------------|
| `grammars/active/sqlite_v3.py` | Current working grammar — fuzzer loads this |
| `grammars/v3.0/sqlite_v3.py` | Immutable snapshot of V3.0 (commit e719c76) |
| `grammars/v3.0/meta.json` | Version metadata for V3.0 |
| `grammars/CHANGELOG.md` | Human-readable grammar version history |
| `results/campaigns/` | Campaign result directories |
| `results/experiments.json` | Experiment tag → campaign ID registry |
| `scripts/archive_campaign.sh` | Manual archiver for past/existing campaigns |
| `scripts/compare_campaigns.py` | Thesis table generator (markdown + LaTeX) |
| `scripts/run_eval.sh` | Modified: post-campaign auto-archive |
| `scripts/run_ablation.sh` | Modified: pass GRAMMAR_VERSION, update experiments.json |
| `.gitignore` | Modified: add exec.log exclusion for results/ |

---

### Task 1: Grammar Versioning Directory Structure

**Files:**
- Create: `grammars/v3.0/sqlite_v3.py`
- Create: `grammars/v3.0/meta.json`
- Create: `grammars/active/sqlite_v3.py`
- Create: `grammars/CHANGELOG.md`

- [ ] **Step 1: Create v3.0 snapshot directory**

```bash
mkdir -p grammars/v3.0
```

- [ ] **Step 2: Copy current V3 grammar as v3.0 snapshot**

```bash
cp grammars/sqlite_v3.py grammars/v3.0/sqlite_v3.py
```

- [ ] **Step 3: Create v3.0/meta.json**

Write `grammars/v3.0/meta.json`:

```json
{
  "version": "3.0",
  "date": "2026-04-27",
  "commit": "e719c76",
  "description": "Structural primitives: Schema-Setup x Stress-Query x Validation-Op",
  "rule_count": 449,
  "changes": "Initial V3 — decomposed monolithic DDL+DQL into composable non-terminals. 4 Sql-Stmt shapes, 6 Schema-Setup, 8 Stress-Query, 4 Validation-Op.",
  "parent_version": null
}
```

- [ ] **Step 4: Create active/ directory with working copy**

```bash
mkdir -p grammars/active
cp grammars/sqlite_v3.py grammars/active/sqlite_v3.py
```

- [ ] **Step 5: Create CHANGELOG.md**

Write `grammars/CHANGELOG.md`:

```markdown
# Grammar Changelog

## v3.0 — 2026-04-27
- Initial structural primitives design (commit e719c76)
- 4 Sql-Stmt shapes: Schema+Query, Schema+Insert+Query, Schema+Insert+Validation, Boundary-Func
- 6 Schema-Setup alternatives: single table, genCol, two tables, table+view, virtual table, table+index
- 8 Stress-Query alternatives: base SELECT, EXISTS, NATURAL JOIN, recursive CTE, compound, self-JOIN, nested subquery, EXPLAIN
- 4 Validation-Op: PRAGMA integrity_check, quick_check, ANALYZE, EXPLAIN
- 449 rules total
```

- [ ] **Step 6: Update scripts that reference grammar path**

The existing `scripts/smoke_test.sh` and `scripts/deep_test.sh` reference `grammars/sqlite_v3.py`. Update them to point to `grammars/active/sqlite_v3.py`.

In `scripts/smoke_test.sh`, find and replace:
```
grammars/sqlite_v3.py
```
with:
```
grammars/active/sqlite_v3.py
```

In `scripts/deep_test.sh`, same replacement:
```
grammars/sqlite_v3.py
```
with:
```
grammars/active/sqlite_v3.py
```

- [ ] **Step 7: Verify smoke test still works**

Run: `bash scripts/smoke_test.sh 2>&1 | head -30`
Expected: Grammar loads from `grammars/active/sqlite_v3.py` without error.

- [ ] **Step 8: Commit**

```bash
git add grammars/v3.0/ grammars/active/ grammars/CHANGELOG.md scripts/smoke_test.sh scripts/deep_test.sh
git commit -m "feat(grammar): versioning system — v3.0 snapshot, active/ working copy, CHANGELOG"
```

---

### Task 2: Results Directory & experiments.json

**Files:**
- Create: `results/campaigns/.gitkeep`
- Create: `results/experiments.json`
- Modify: `.gitignore`

- [ ] **Step 1: Create results directory structure**

```bash
mkdir -p results/campaigns
touch results/campaigns/.gitkeep
```

- [ ] **Step 2: Create experiments.json with historical experiments**

Write `results/experiments.json`:

```json
{
  "E1-attribution-baseline": {
    "hypothesis": "Per-rule attribution reveals weight inefficiency in old grammar",
    "campaigns": [],
    "conclusion": "34.5% weight wasted, R25 crash magnet at 21.9x"
  },
  "E2-v3-ab-test": {
    "hypothesis": "Structural primitives grammar finds real crashes without PoC contamination",
    "campaigns": [],
    "conclusion": "1508 queue (+6%), 131 crashes (all real), but 92% FTS5"
  }
}
```

Note: `campaigns` arrays are empty because those runs pre-date the archive system. The conclusions are recorded for thesis reference.

- [ ] **Step 3: Update .gitignore**

Add to `.gitignore` after the existing entries:

```
# Campaign results: exclude large regenerable files
results/campaigns/*/exec.log
```

- [ ] **Step 4: Commit**

```bash
git add results/ .gitignore
git commit -m "feat(results): campaign archive directory and experiments.json registry"
```

---

### Task 3: archive_campaign.sh

**Files:**
- Create: `scripts/archive_campaign.sh`

This script manually archives an existing campaign from `/tmp/nautilus_eval/` into `results/campaigns/`.

- [ ] **Step 1: Write archive_campaign.sh**

Write `scripts/archive_campaign.sh`:

```bash
#!/usr/bin/env bash
# archive_campaign.sh — Archive a campaign from a workdir into results/campaigns/
#
# Usage:
#   ./scripts/archive_campaign.sh \
#     --workdir /tmp/nautilus_eval/sqlite-3.31.1_v3_baseline_15m \
#     --grammar-version v3.0 \
#     --target sqlite-3.31.1 \
#     --duration 900 \
#     --run-id run1 \
#     [--tag E2-v3-ab-test] \
#     [--notes "15-min A/B baseline"]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

WORKDIR=""
GRAMMAR_VERSION=""
TARGET=""
DURATION=""
RUN_ID=""
TAG=""
NOTES=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --workdir) WORKDIR="$2"; shift 2 ;;
        --grammar-version) GRAMMAR_VERSION="$2"; shift 2 ;;
        --target) TARGET="$2"; shift 2 ;;
        --duration) DURATION="$2"; shift 2 ;;
        --run-id) RUN_ID="$2"; shift 2 ;;
        --tag) TAG="$2"; shift 2 ;;
        --notes) NOTES="$2"; shift 2 ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

if [[ -z "$WORKDIR" || -z "$GRAMMAR_VERSION" || -z "$TARGET" || -z "$DURATION" || -z "$RUN_ID" ]]; then
    echo "Usage: $0 --workdir <path> --grammar-version <vX.Y> --target <sqlite-ver> --duration <secs> --run-id <id> [--tag <tag>] [--notes <text>]"
    exit 1
fi

if [[ ! -d "$WORKDIR" ]]; then
    echo "Error: workdir not found: $WORKDIR"
    exit 1
fi

# Convert duration seconds to human-readable
duration_human() {
    local secs=$1
    if (( secs >= 86400 )); then
        echo "$((secs / 86400))d"
    elif (( secs >= 3600 )); then
        echo "$((secs / 3600))h"
    else
        echo "$((secs / 60))m"
    fi
}

TODAY=$(date +%Y-%m-%d)
DURATION_H=$(duration_human "$DURATION")
CAMPAIGN_ID="${TODAY}_${GRAMMAR_VERSION}_${TARGET}_${DURATION_H}_${RUN_ID}"

ARCHIVE_DIR="$ROOT/results/campaigns/$CAMPAIGN_ID"

if [[ -d "$ARCHIVE_DIR" ]]; then
    echo "Error: archive already exists: $ARCHIVE_DIR"
    exit 1
fi

mkdir -p "$ARCHIVE_DIR"

# Count results from workdir
CRASHES=$(ls "$WORKDIR/outputs/signaled/" 2>/dev/null | wc -l)
QUEUE=$(ls "$WORKDIR/outputs/queue/" 2>/dev/null | wc -l)

# Read total_executions from coverage.json if it exists
TOTAL_EXEC="null"
if [[ -f "$WORKDIR/coverage.json" ]]; then
    TOTAL_EXEC=$(python3 -c "import json; d=json.load(open('$WORKDIR/coverage.json')); print(d.get('total_executions') or 'null')" 2>/dev/null || echo "null")
fi

# Read unique_root_causes from dedup.json if it exists
UNIQUE_RC="null"
if [[ -f "$WORKDIR/dedup.json" ]]; then
    UNIQUE_RC=$(python3 -c "import json; d=json.load(open('$WORKDIR/dedup.json')); print(d.get('unique_root_causes') or 'null')" 2>/dev/null || echo "null")
fi

# Read config values from config.ron if it exists
MAX_TREE_SIZE=300
TIMEOUT_MS=500
THREADS=1
BITMAP_SIZE=2097152
if [[ -f "$WORKDIR/config.ron" ]]; then
    MAX_TREE_SIZE=$(grep -oP 'max_tree_size:\s*\K\d+' "$WORKDIR/config.ron" 2>/dev/null || echo 300)
    TIMEOUT_MS=$(grep -oP 'timeout_in_millis:\s*\K\d+' "$WORKDIR/config.ron" 2>/dev/null || echo 500)
    THREADS=$(grep -oP 'number_of_threads:\s*\K\d+' "$WORKDIR/config.ron" 2>/dev/null || echo 1)
    BITMAP_SIZE=$(grep -oP 'bitmap_size:\s*\K\d+' "$WORKDIR/config.ron" 2>/dev/null || echo 2097152)
fi

# Build tags JSON array
if [[ -n "$TAG" ]]; then
    TAGS_JSON="[\"$TAG\"]"
else
    TAGS_JSON="[]"
fi

# Write campaign.json
cat > "$ARCHIVE_DIR/campaign.json" <<ENDJSON
{
  "id": "$CAMPAIGN_ID",
  "date": "$TODAY",
  "grammar_version": "$GRAMMAR_VERSION",
  "grammar_file": "grammars/$GRAMMAR_VERSION/sqlite_v3.py",
  "target": "$TARGET",
  "duration_seconds": $DURATION,
  "run_id": "$RUN_ID",
  "config": {
    "max_tree_size": $MAX_TREE_SIZE,
    "timeout_ms": $TIMEOUT_MS,
    "threads": $THREADS,
    "bitmap_size": $BITMAP_SIZE
  },
  "results": {
    "total_executions": $TOTAL_EXEC,
    "crashes": $CRASHES,
    "queue_paths": $QUEUE,
    "unique_root_causes": $UNIQUE_RC
  },
  "tags": $TAGS_JSON,
  "notes": "$NOTES"
}
ENDJSON

# Copy dedup.json if present
if [[ -f "$WORKDIR/dedup.json" ]]; then
    cp "$WORKDIR/dedup.json" "$ARCHIVE_DIR/dedup.json"
fi

# Generate attribution report if exec.log exists
GRAMMAR_FILE="$ROOT/grammars/$GRAMMAR_VERSION/sqlite_v3.py"
if [[ -f "$WORKDIR/exec.log" && -f "$GRAMMAR_FILE" ]]; then
    echo "[archive] generating attribution report..."
    python3 "$SCRIPT_DIR/analyze_attribution.py" "$WORKDIR" \
        --grammar "$GRAMMAR_FILE" \
        > "$ARCHIVE_DIR/attribution.txt" 2>/dev/null \
        || echo "[archive] warning: attribution generation failed (non-fatal)"
fi

echo "========================================"
echo " Campaign archived"
echo " ID:      $CAMPAIGN_ID"
echo " Path:    $ARCHIVE_DIR"
echo " Crashes: $CRASHES"
echo " Queue:   $QUEUE"
echo "========================================"

# Update experiments.json if --tag was provided
if [[ -n "$TAG" ]]; then
    EXPERIMENTS_FILE="$ROOT/results/experiments.json"
    if [[ -f "$EXPERIMENTS_FILE" ]]; then
        python3 -c "
import json, sys
with open('$EXPERIMENTS_FILE') as f:
    data = json.load(f)
tag = '$TAG'
cid = '$CAMPAIGN_ID'
if tag not in data:
    data[tag] = {'hypothesis': '', 'campaigns': [], 'conclusion': None}
if cid not in data[tag]['campaigns']:
    data[tag]['campaigns'].append(cid)
with open('$EXPERIMENTS_FILE', 'w') as f:
    json.dump(data, f, indent=2)
print(f'[archive] added {cid} to experiment {tag}')
" || echo "[archive] warning: experiments.json update failed (non-fatal)"
    fi
fi
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/archive_campaign.sh
```

- [ ] **Step 3: Test with dry run (verify argument parsing)**

```bash
./scripts/archive_campaign.sh --workdir /nonexistent --grammar-version v3.0 --target sqlite-3.31.1 --duration 900 --run-id test1
```

Expected: `Error: workdir not found: /nonexistent`

- [ ] **Step 4: Test with existing V3 baseline campaign (if /tmp workdir still exists)**

```bash
ls /tmp/nautilus_eval/sqlite-3.31.1_v3_baseline_15m/outputs/signaled/ 2>/dev/null | wc -l
```

If the workdir exists, archive it:
```bash
./scripts/archive_campaign.sh \
  --workdir /tmp/nautilus_eval/sqlite-3.31.1_v3_baseline_15m \
  --grammar-version v3.0 \
  --target sqlite-3.31.1 \
  --duration 900 \
  --run-id baseline \
  --tag E2-v3-ab-test \
  --notes "15-min V3 baseline A/B test"
```

Expected: `Campaign archived` with correct crash/queue counts.

Verify: `cat results/campaigns/2026-04-28_v3.0_sqlite-3.31.1_15m_baseline/campaign.json`

- [ ] **Step 5: Commit**

```bash
git add scripts/archive_campaign.sh
# Also add any archived campaign results if they were created:
git add results/
git commit -m "feat(scripts): archive_campaign.sh — manual campaign archiver"
```

---

### Task 4: run_eval.sh Auto-Archive Integration

**Files:**
- Modify: `scripts/run_eval.sh`

- [ ] **Step 1: Add GRAMMAR_VERSION to env vars documentation**

In `scripts/run_eval.sh`, add to the environment variables comment block (after the `HARNESS_SUFFIX` line):

```bash
#   GRAMMAR_VERSION grammar version tag for archiving (e.g., "v3.0")
#                   If set, campaign results are archived to results/campaigns/
```

- [ ] **Step 2: Read GRAMMAR_VERSION at the top with other env vars**

After the line `DURATION="${DURATION:-86400}"`, add:

```bash
GRAMMAR_VERSION="${GRAMMAR_VERSION:-}"
```

- [ ] **Step 3: Add GRAMMAR_VERSION to the campaign info banner**

After the line `echo " Duration:     ${DURATION}s"`, add:

```bash
if [[ -n "$GRAMMAR_VERSION" ]]; then
    echo " Grammar Ver:  $GRAMMAR_VERSION"
    echo " Auto-archive: ON"
fi
```

- [ ] **Step 4: Add archive block at the end of the script**

After the coverage capture block (the last line of the file), append:

```bash

# ----------------------------------------------------------------
# Auto-archive: save campaign results to results/campaigns/
# ----------------------------------------------------------------
if [[ -n "$GRAMMAR_VERSION" ]]; then
    echo "[run_eval] archiving campaign..."
    ARCHIVE_ARGS=(
        --workdir "$WORKDIR"
        --grammar-version "$GRAMMAR_VERSION"
        --target "$VERSION"
        --duration "$DURATION"
        --run-id "$RUN_ID"
    )
    if [[ -n "${EXPERIMENT_TAG:-}" ]]; then
        ARCHIVE_ARGS+=(--tag "$EXPERIMENT_TAG")
    fi
    "$SCRIPT_DIR/archive_campaign.sh" "${ARCHIVE_ARGS[@]}" \
        || echo "[run_eval] warning: archiving failed (non-fatal)"
fi
```

- [ ] **Step 5: Commit**

```bash
git add scripts/run_eval.sh
git commit -m "feat(scripts): run_eval.sh auto-archives when GRAMMAR_VERSION is set"
```

---

### Task 5: run_ablation.sh Integration

**Files:**
- Modify: `scripts/run_ablation.sh`

- [ ] **Step 1: Add GRAMMAR_VERSION to env vars**

After the `TARGET="${TARGET:-sqlite-3.31.1}"` line, add:

```bash
GRAMMAR_VERSION="${GRAMMAR_VERSION:-}"
EXPERIMENT_TAG="${EXPERIMENT_TAG:-}"
```

- [ ] **Step 2: Pass GRAMMAR_VERSION and EXPERIMENT_TAG to run_eval.sh**

In the inner loop where `run_eval.sh` is called, change:

```bash
        DURATION="$DURATION" \
        GRAMMAR="$GRAMMAR" \
        HARNESS_SUFFIX=patterns_ \
        "$SCRIPT_DIR/run_eval.sh" "$TARGET" "$RUN_ID"
```

to:

```bash
        DURATION="$DURATION" \
        GRAMMAR="$GRAMMAR" \
        GRAMMAR_VERSION="$GRAMMAR_VERSION" \
        EXPERIMENT_TAG="$EXPERIMENT_TAG" \
        HARNESS_SUFFIX=patterns_ \
        "$SCRIPT_DIR/run_eval.sh" "$TARGET" "$RUN_ID"
```

- [ ] **Step 3: Commit**

```bash
git add scripts/run_ablation.sh
git commit -m "feat(scripts): run_ablation.sh passes GRAMMAR_VERSION to run_eval for auto-archive"
```

---

### Task 6: compare_campaigns.py

**Files:**
- Create: `scripts/compare_campaigns.py`

- [ ] **Step 1: Write compare_campaigns.py**

Write `scripts/compare_campaigns.py`:

```python
#!/usr/bin/env python3
"""Compare campaigns within an experiment for thesis tables.

Usage:
    python3 scripts/compare_campaigns.py <experiment-tag>
    python3 scripts/compare_campaigns.py <experiment-tag> --latex
    python3 scripts/compare_campaigns.py --list
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_experiments(root: Path) -> dict:
    path = root / "results" / "experiments.json"
    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


def load_campaign(root: Path, campaign_id: str) -> dict | None:
    path = root / "results" / "campaigns" / campaign_id / "campaign.json"
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


def format_duration(seconds: int) -> str:
    if seconds >= 86400:
        return f"{seconds // 86400}d"
    if seconds >= 3600:
        return f"{seconds // 3600}h"
    return f"{seconds // 60}m"


def shorten_id(campaign_id: str) -> str:
    parts = campaign_id.split("_")
    if len(parts) >= 5:
        return f"...{parts[-2]}_{parts[-1]}"
    return campaign_id


def render_markdown(tag: str, experiment: dict, campaigns: list[dict]) -> str:
    lines = []
    lines.append(f"## Experiment: {tag}")
    lines.append(f"**Hypothesis:** {experiment['hypothesis']}")
    lines.append("")

    if not campaigns:
        lines.append("*No archived campaigns yet.*")
        if experiment.get("conclusion"):
            lines.append(f"\n**Conclusion:** {experiment['conclusion']}")
        return "\n".join(lines)

    headers = ["Campaign", "Grammar", "Target", "Duration", "Crashes", "Queue", "Executions", "Unique RC"]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for c in campaigns:
        r = c.get("results", {})
        row = [
            shorten_id(c["id"]),
            c.get("grammar_version", "?"),
            c.get("target", "?").replace("sqlite-", ""),
            format_duration(c.get("duration_seconds", 0)),
            str(r.get("crashes", "?")),
            str(r.get("queue_paths", "?")),
            str(r.get("total_executions", "?") or "?"),
            str(r.get("unique_root_causes", "?") or "?"),
        ]
        lines.append("| " + " | ".join(row) + " |")

    conclusion = experiment.get("conclusion")
    if conclusion:
        lines.append(f"\n**Conclusion:** {conclusion}")
    else:
        lines.append("\n**Conclusion:** *pending*")

    return "\n".join(lines)


def render_latex(tag: str, experiment: dict, campaigns: list[dict]) -> str:
    lines = []
    lines.append(f"% Experiment: {tag}")
    lines.append(f"% Hypothesis: {experiment['hypothesis']}")
    lines.append("\\begin{table}[h]")
    lines.append("\\centering")
    lines.append(f"\\caption{{Experiment: {tag}}}")
    lines.append("\\begin{tabular}{llllrrrr}")
    lines.append("\\toprule")
    lines.append("Campaign & Grammar & Target & Duration & Crashes & Queue & Executions & Unique RC \\\\")
    lines.append("\\midrule")

    for c in campaigns:
        r = c.get("results", {})
        row = [
            shorten_id(c["id"]).replace("_", "\\_"),
            c.get("grammar_version", "?"),
            c.get("target", "?").replace("sqlite-", ""),
            format_duration(c.get("duration_seconds", 0)),
            str(r.get("crashes", "?")),
            str(r.get("queue_paths", "?")),
            str(r.get("total_executions", "?") or "?"),
            str(r.get("unique_root_causes", "?") or "?"),
        ]
        lines.append(" & ".join(row) + " \\\\")

    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append("\\end{table}")
    return "\n".join(lines)


def list_experiments(root: Path) -> None:
    experiments = load_experiments(root)
    print(f"{'Tag':<30} {'Campaigns':>10} {'Conclusion'}")
    print("-" * 80)
    for tag, exp in experiments.items():
        n = len(exp.get("campaigns", []))
        conclusion = exp.get("conclusion") or "pending"
        if len(conclusion) > 40:
            conclusion = conclusion[:37] + "..."
        print(f"{tag:<30} {n:>10} {conclusion}")


def main() -> None:
    root = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(description="Compare campaigns within an experiment")
    parser.add_argument("tag", nargs="?", help="Experiment tag from experiments.json")
    parser.add_argument("--latex", action="store_true", help="Output LaTeX table format")
    parser.add_argument("--list", action="store_true", help="List all experiments")
    args = parser.parse_args()

    if args.list:
        list_experiments(root)
        return

    if not args.tag:
        print("Error: provide an experiment tag, or use --list", file=sys.stderr)
        sys.exit(1)

    experiments = load_experiments(root)
    if args.tag not in experiments:
        print(f"Error: experiment '{args.tag}' not found in experiments.json", file=sys.stderr)
        print(f"Available: {', '.join(experiments.keys())}", file=sys.stderr)
        sys.exit(1)

    experiment = experiments[args.tag]
    campaign_ids = experiment.get("campaigns", [])

    campaigns = []
    for cid in campaign_ids:
        c = load_campaign(root, cid)
        if c:
            campaigns.append(c)
        else:
            print(f"Warning: campaign {cid} not found in results/campaigns/", file=sys.stderr)

    if args.latex:
        print(render_latex(args.tag, experiment, campaigns))
    else:
        print(render_markdown(args.tag, experiment, campaigns))


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/compare_campaigns.py
```

- [ ] **Step 3: Test --list flag**

Run: `python3 scripts/compare_campaigns.py --list`

Expected output:
```
Tag                            Campaigns Conclusion
--------------------------------------------------------------------------------
E1-attribution-baseline                0 34.5% weight wasted, R25 crash mag...
E2-v3-ab-test                          0 1508 queue (+6%), 131 crashes (all...
```

- [ ] **Step 4: Test markdown output for an experiment**

Run: `python3 scripts/compare_campaigns.py E2-v3-ab-test`

Expected output:
```
## Experiment: E2-v3-ab-test
**Hypothesis:** Structural primitives grammar finds real crashes without PoC contamination

*No archived campaigns yet.*

**Conclusion:** 1508 queue (+6%), 131 crashes (all real), but 92% FTS5
```

(No campaigns yet because past runs pre-date the archive. Once Task 3 archives them, this will show data.)

- [ ] **Step 5: Test --latex flag**

Run: `python3 scripts/compare_campaigns.py E2-v3-ab-test --latex`

Expected: LaTeX `\begin{tabular}` output (empty table body since no archived campaigns).

- [ ] **Step 6: Commit**

```bash
git add scripts/compare_campaigns.py
git commit -m "feat(scripts): compare_campaigns.py — thesis table generator with markdown and LaTeX output"
```

---

### Task 7: End-to-End Verification

- [ ] **Step 1: Archive existing V3 baseline (if workdir still exists in /tmp)**

```bash
ls /tmp/nautilus_eval/sqlite-3.31.1_v3_baseline_15m/ 2>/dev/null && \
./scripts/archive_campaign.sh \
  --workdir /tmp/nautilus_eval/sqlite-3.31.1_v3_baseline_15m \
  --grammar-version v3.0 \
  --target sqlite-3.31.1 \
  --duration 900 \
  --run-id baseline \
  --tag E2-v3-ab-test \
  --notes "15-min V3 baseline A/B test"
```

If the workdir is gone, skip this step — future campaigns will auto-archive.

- [ ] **Step 2: Verify compare_campaigns.py shows archived data**

```bash
python3 scripts/compare_campaigns.py E2-v3-ab-test
```

Expected: markdown table now shows the archived campaign row with crash/queue counts.

- [ ] **Step 3: Verify grammar versioning diff works**

```bash
diff grammars/v3.0/sqlite_v3.py grammars/active/sqlite_v3.py
```

Expected: no differences (they should be identical at this point).

- [ ] **Step 4: Verify run_eval.sh auto-archive flag is present**

```bash
grep "GRAMMAR_VERSION" scripts/run_eval.sh
```

Expected: shows the env var documentation, reading, and archive block.

- [ ] **Step 5: Commit any archived results**

```bash
git add results/
git commit -m "chore(results): archive existing V3 baseline campaign"
```

(Only if Step 1 created an archive.)

- [ ] **Step 6: Final verification — directory structure matches spec**

```bash
find grammars/ -type f | sort
find results/ -type f | sort
```

Expected:
```
grammars/active/sqlite_v3.py
grammars/CHANGELOG.md
grammars/legacy/sqlite_attack.py
grammars/legacy/sqlite_patterns.py
grammars/legacy/sqlite_patterns_uniform.py
grammars/sqlite_v3.py           (original — can be removed later)
grammars/v3.0/meta.json
grammars/v3.0/sqlite_v3.py

results/campaigns/.gitkeep       (or campaign dirs if archived)
results/experiments.json
```
