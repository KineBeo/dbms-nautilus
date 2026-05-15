# Data Consolidation + Chart Generation Design

**Date:** 2026-05-15
**Scope:** Consolidate 20 campaign results into 3 CSVs, generate 5 publication-quality charts
**Input:** 20 workdirs under `workdirs/*comparison*`
**Output:** `results/comparison/data/` (CSVs) + `results/comparison/figures/` (PDFs)

---

## Step 1: Consolidated Data Files

### `campaigns_summary.csv` (20 rows)

| Column | Type | Source | Description |
|--------|------|--------|-------------|
| campaign_id | str | dirname | `v3.3_sqlite-3.31.1_run1` |
| grammar | str | parsed | `v3.3` or `ebnf` |
| sqlite_version | str | parsed | `sqlite-3.31.1` or `sqlite-3.32.2` |
| run | int | parsed | 1-5 |
| duration_sec | int | coverage.json | 900 |
| total_execs | int | coverage.csv last row exec_count | total executions in campaign |
| execs_per_sec | float | total_execs / duration_sec | throughput |
| total_edges | int | coverage.csv last row total_edges | unique edge coverage at end |
| total_signals | int | coverage.csv last row total_crashes | raw signal count (all types) |
| ubsan_crashes | int | triage_test.json sum(counts) | UBSan/ASan real crash inputs |
| unique_root_causes | int | triage_test.json unique_crashes | distinct bugs after stack dedup |
| asan_count | int | triage_test.json summary.asan | ASan-detected bugs |
| ubsan_count | int | triage_test.json summary.ubsan | UBSan-detected bug classes |
| queue_size | int | coverage.json queue_final | interesting inputs in queue |

### `bug_classes.csv` (variable rows, ~3-5 per campaign)

| Column | Type | Source |
|--------|------|--------|
| campaign_id | str | parent |
| grammar | str | parent |
| sqlite_version | str | parent |
| run | int | parent |
| bug_hash | str | triage_test.json crashes[].hash |
| bug_type | str | triage_test.json crashes[].type |
| bug_subtype | str | triage_test.json crashes[].subtype |
| key_function | str | triage_test.json crashes[].top_frames[1] |
| crash_count | int | triage_test.json crashes[].count |
| sample_sql | str | triage_test.json crashes[].sql_preview |

### `timeseries.csv` (~18,000 rows: 20 campaigns × ~900 seconds)

| Column | Type | Source |
|--------|------|--------|
| campaign_id | str | parent |
| grammar | str | parent |
| sqlite_version | str | parent |
| run | int | parent |
| timestamp_sec | int | coverage.csv |
| total_edges | int | coverage.csv |
| total_crashes | int | coverage.csv |
| exec_count | int | coverage.csv |

---

## Step 2: Charts

### Chart 1: Unique Bug Classes — Grouped Bar Chart

- **File:** `unique_bugs_bar.pdf`
- **Data source:** `campaigns_summary.csv` → `unique_root_causes`
- **Layout:** Single plot, grouped bars
- **X-axis:** SQLite version (3.31.1, 3.32.2) — categorical
- **Y-axis:** Unique root causes (count, integer)
- **Groups:** v3.3 (blue, `#2196F3`) vs EBNF (orange, `#FF9800`)
- **Error bars:** ±1 std deviation over 5 runs, cap width 4pt
- **Annotations:** Mann-Whitney U p-value above each version group
- **Style:** Serif font, 300 dpi, grid on y-axis only (alpha 0.3)

### Chart 2: Edge Coverage Over Time — Line Plot with Confidence Band

- **File:** `coverage_over_time.pdf`
- **Data source:** `timeseries.csv` → `total_edges` vs `timestamp_sec`
- **Layout:** 1×2 subplots (one per SQLite version)
- **X-axis:** Time (seconds, 0-900)
- **Y-axis:** Total edges (integer)
- **Lines:** Mean across 5 runs per grammar
- **Bands:** ±1σ shaded region (alpha 0.15)
- **Colors:** v3.3 blue, EBNF orange
- **Legend:** Bottom-right of each subplot
- **Note:** Uses actual per-second data from coverage.csv, not exec.log approximation

### Chart 3: Bug Class Breakdown — Grouped Horizontal Bar (per grammar × version)

- **File:** `bug_class_breakdown.pdf`
- **Data source:** `bug_classes.csv` → group by `bug_subtype`, aggregate `crash_count`
- **Layout:** 1×2 subplots (one per SQLite version)
- **X-axis:** Total crash count (sum across 5 runs)
- **Y-axis:** Bug subtype labels (e.g., "signed-integer-overflow", "null-pointer", "float-cast-overflow")
- **Groups:** v3.3 vs EBNF side-by-side horizontal bars
- **Purpose:** Shows diversity — v3.3 finds 3+ bug types, EBNF finds only 1

### Chart 4: Crash Accumulation Over Time — Line Plot

- **File:** `crash_accumulation.pdf`
- **Data source:** `timeseries.csv` → `total_crashes` vs `timestamp_sec`
- **Layout:** 1×2 subplots (one per SQLite version)
- **X-axis:** Time (seconds, 0-900)
- **Y-axis:** Cumulative crash count
- **Lines + bands:** Same as Chart 2 (mean ±1σ)
- **Purpose:** Shows crash discovery speed — EBNF hits more total signals faster (shallow FTS bug), v3.3 slower but more diverse

### Chart 5: Throughput — Grouped Bar Chart

- **File:** `throughput_bar.pdf`
- **Data source:** `campaigns_summary.csv` → `execs_per_sec`
- **Layout:** Single plot, grouped bars
- **X-axis:** SQLite version
- **Y-axis:** Executions per second
- **Groups:** v3.3 vs EBNF
- **Error bars:** ±1 std
- **Purpose:** Shows if grammar complexity affects fuzzing speed

---

## Implementation

### Scripts

1. `scripts/consolidate_data.py` — reads 20 workdirs, outputs 3 CSVs to `results/comparison/data/`
2. `scripts/plot_comparison.py` — reads 3 CSVs, outputs 5 PDFs to `results/comparison/figures/`

### Libraries

- `pandas` for CSV handling
- `matplotlib` for plotting
- `scipy.stats` for Mann-Whitney U test
- `numpy` for statistics

### Output structure

```
results/comparison/
├── data/
│   ├── campaigns_summary.csv
│   ├── bug_classes.csv
│   └── timeseries.csv
└── figures/
    ├── unique_bugs_bar.pdf
    ├── coverage_over_time.pdf
    ├── bug_class_breakdown.pdf
    ├── crash_accumulation.pdf
    └── throughput_bar.pdf
```
