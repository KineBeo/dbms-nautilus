# Chapter 4 — Data Provenance

Comprehensive mapping of every data source used to produce every table, figure,
and number in Chapter 4 (Experiments and Evaluation).

**Last verified:** 2026-05-22

---

## Grammar Name Mapping

The thesis uses two names; internally three grammar versions were used:

| Thesis Name | RQ | Internal Label | Grammar File | Rules |
|---|---|---|---|---|
| DBMS-Nautilus (with seeds) | RQ1 | `v3.5` / `v35` | `grammars/sqlite_patterns.py` + seeds | 526 |
| DBMS-Nautilus (no seeds) | RQ2 | `v3.3` / `v33` | `grammars/sqlite_patterns.py` (no seeds) | 520 |
| DBMS-Nautilus (full) | RQ3 | `v3.4` | `grammars/sqlite_patterns.py` | 526 |
| EBNF-Baseline | RQ3 | `ebnf` | `grammars/sqlite_ebnf.py` | uniform |

---

## Campaign Matrix

| RQ | Grammar | Versions | Runs/ver | Duration | Total Campaigns |
|---|---|---|---|---|---|
| RQ1 | v3.5 | 4 | 5 | 15 min | 20 |
| RQ2 | v3.3 | 4 | 5 | 15 min | 20 |
| RQ3 (proposed) | v3.4 | 4 | 5 | 15 min | 20 |
| RQ3 (baseline) | ebnf | 4 | 5 | 15 min | 20 |
| **Total** | | | | | **80** |

All campaigns: single thread, 300-node max tree, 500 ms timeout, no seed corpus.

---

## RQ1: CVE Rediscovery

### Tables and Figures

| Artifact | Thesis Label | Primary Data Source |
|---|---|---|
| Table 4.2 | CVE rediscovery results | `results/rq1_v35/cve_hits.csv` |
| Figure 4.1 | Time to first CVE crash | `scripts/generate_figures.py` → `gather_f1_data()` |

### Data Files

| File | Path | Content |
|---|---|---|
| CVE hit matrix | `results/rq1_v35/cve_hits.csv` | Per-run yes/no/N/A per CVE with evidence (SQL, hash) |
| Campaign summary | `results/rq1_v35/campaigns_summary.csv` | Total crashes, debug_assert/signal/ubsan/asan per run |
| No-debug replay | `results/rq1_v35/cve_replay_nodebug.md` | CVE-2020-13871 and CVE-2020-9327 confirmation without SQLITE_DEBUG |
| Crash evidence | `results/crashes_v35/` | 3 bug classes, 13 unique crashes: trigger.sql, stderr.log, metadata.json |

### Raw Workdirs (20)

```
workdirs/sqlite-3.30.1_v35_run{1..5}/
workdirs/sqlite-3.31.1_v35_run{1..5}/
workdirs/sqlite-3.32.0_v35_run{1..5}/
workdirs/sqlite-3.32.2_v35_run{1..5}/
```

Each contains: `triage.json`, `coverage.csv`, `config.ron`, `grammar_weights.json`.

### How Table 4.2 Numbers Were Derived

- **Runs Found column:** count of `yes` entries per CVE in `cve_hits.csv`
- **CVE-2020-13434 (14/15):** 4/5 on 3.30.1 + 5/5 on 3.31.1 + 5/5 on 3.32.0
- **CVE-2020-13435 (5/5):** hash `9411c5875a64a648` matched on all 3.32.0 runs
- **CVE-2020-13871 (4/5):** 3.32.2 runs 2-5 (run1 had 0 seed_b crashes)
- **CVE-2020-15358 (5/5):** INTERSECT-pattern SQL on all 3.32.2 runs
- **CVE-2020-9327 (0/5):** no hits on 3.31.1 runs (found compositionally in RQ2)
- **Footnote †:** validated via `cve_replay_nodebug.md` — debug_assert crashes become UBSan under no-debug harness
- **Footnote ‡:** INTERSECT-pattern match; crash site differs from published CVE stack trace

### How Figure 4.1 Was Generated

`scripts/generate_figures.py` function `gather_f1_data()`:
1. Iterates `workdirs/sqlite-{ver}_v35_run{N}/`
2. Loads `triage.json` crashes, matches CVE predicates (function name, hash, SQL pattern)
3. Finds earliest matching crash's `sample_file` index
4. Maps exec index → wall-clock time via `coverage.csv`
5. Box plot of time-to-first-crash per CVE

---

## RQ2: Bug Detection

### Tables and Figures

| Artifact | Thesis Label | Primary Data Source |
|---|---|---|
| Table 4.3 | Bug classes (11 classes) | `results/rq2_fresh/bug_classes.csv` + `results/crashes_v33/registry.md` |
| Table 4.4 | Bug class discovery per campaign | `results/rq2_fresh/bug_classes.csv` (distinct class_ids per run) |
| Figure 4.2 | Bug class breakdown | `scripts/generate_figures.py` → `plot_f2()` reading `results/rq2_fresh/registry.json` |

### Data Files

| File | Path | Content |
|---|---|---|
| Campaign summary | `results/rq2_fresh/campaigns_summary.csv` | 20 rows: crashes, types per run |
| Bug class CSV | `results/rq2_fresh/bug_classes.csv` | Per-run, per-hash: type, subtype, key_function, class_id, count |
| Bug class registry | `results/rq2_fresh/registry.json` | Structured: class summaries, unique_hashes, severity, CVE mapping |
| Crash evidence | `results/crashes_v33/` | 13 bug classes (BC001-BC013), 48 unique crashes |
| Crash registry | `results/crashes_v33/registry.json` + `registry.md` | Full registry with hashes, versions, counts |

### Raw Workdirs (20)

```
workdirs/sqlite-3.30.1_v33_run{1..5}/
workdirs/sqlite-3.31.1_v33_run{1..5}/
workdirs/sqlite-3.32.0_v33_run{1..5}/
workdirs/sqlite-3.32.2_v33_run{1..5}/
```

### Bug Class Numbering Note

The raw registry (`crashes_v33/registry.md`) lists **13** classes (BC001-BC013).
The thesis Table 4.3 presents **11** classes with renumbered IDs. The mapping:

| Thesis BC | Raw Registry BC | Key Function |
|---|---|---|
| BC001 | BC002 | `sqlite3Fts5GetTokenizer` |
| BC002 | BC003 | `sqlite3WindowUnlinkFromSelect` |
| BC003 | BC004 | `sqlite3_str_vappendf` |
| BC004 | BC010 | `alsoAnInt` |
| BC006 | BC001 | `sqlite3ExprCodeTarget` (null ptr) |
| BC008 | BC007 | `sqlite3Atoi64` |
| BC009 | BC013 | `sqlite3VdbeMemNumerify` |
| BC010 | BC012 | `sqlite3Select` |
| BC011 | BC006 | `resetAccumulator` |
| BC012 | BC009 | `isAuxiliaryVtabOperator` |
| BC013 | BC011 | `sqlite3ExprCodeTarget` (misaligned) |

Raw BC005 (`sqlite3WindowListDelete`) and BC008 (`sqlite3ExprCodeTarget` signal) were excluded from the thesis table.

### How Table 4.4 Numbers Were Derived

From `results/rq2_fresh/bug_classes.csv`:
1. Group by `(sqlite_version, run)` → count distinct `class_id` values
2. Per version: mean ± std across 5 runs

---

## RQ3: Performance Trade-off

### Tables and Figures

| Artifact | Thesis Label | Primary Data Source |
|---|---|---|
| Table 4.5 | Statistical comparison (4 metrics × 4 versions) | `results/comparison/rq3_statistical_tests.csv` |
| Table 4.6 | Overall comparison (summary) | `results/comparison/data/campaigns_summary.csv` (cross-version averages) |
| Figure 4.3 | Coverage growth over time | `scripts/generate_figures.py` reading workdirs directly |
| Figure 4.4 | Throughput comparison | `scripts/generate_figures.py` reading `campaigns_summary.csv` |
| Figure 4.5 | Time to first crash | `scripts/generate_figures.py` reading workdirs directly |

### Data Files

| File | Path | Content |
|---|---|---|
| Campaign summary | `results/comparison/data/campaigns_summary.csv` | 41 rows: execs_per_sec, total_edges, unique_root_causes per run |
| Time series | `results/comparison/data/timeseries.csv` (35,957 rows) | Per-second: edges, crashes, exec_count |
| Bug classes | `results/comparison/data/bug_classes.csv` (4,165 rows) | Per-run per-hash: type, function, count, sample SQL |
| Statistical tests | `results/comparison/rq3_statistical_tests.csv` | Mann-Whitney U, p-value, Cliff's d for 4 metrics × 4 versions |
| Full metrics | `results/comparison/metrics.json` (320 KB) | Detailed per-campaign metrics |
| Comparison log | `results/comparison/full_log.txt` | Full comparison run output |

### Raw Workdirs (39)

```
# Proposed grammar (v3.4): 20 workdirs
workdirs/sqlite-3.30.1_comparison_v3.4_run{1..5}/
workdirs/sqlite-3.31.1_comparison_v3.4_run{1..5}/
workdirs/sqlite-3.32.0_comparison_v3.4_run{1..5}/
workdirs/sqlite-3.32.2_comparison_v3.4_run{1..5}/

# EBNF baseline: 19 workdirs (3.32.0 run1 missing)
workdirs/sqlite-3.30.1_comparison_ebnf_run{1..5}/
workdirs/sqlite-3.31.1_comparison_ebnf_run{1..5}/
workdirs/sqlite-3.32.0_comparison_ebnf_run{2..5}/     # run1 MISSING
workdirs/sqlite-3.32.2_comparison_ebnf_run{1..5}/
```

**Note:** `sqlite-3.32.0_comparison_ebnf_run1` is missing. The stats CSV shows
`ebnf_n=4` for 3.32.0 metrics (not 5). This affects the 3.32.0 p-value (0.151).

### How Table 4.5 Numbers Were Derived

From `results/comparison/rq3_statistical_tests.csv`:
- Header uses `v35_mean`/`v35_std` but data is from `v3.4` comparison campaigns
- Columns map directly to table cells: mean ± std, p-value, Cliff's d

### How Table 4.6 Numbers Were Derived

From `results/comparison/data/campaigns_summary.csv`:
1. Group by grammar (`v3.4` vs `ebnf`)
2. Compute grand mean ± std across all 20 (or 19) campaigns per grammar
3. Metrics: `unique_root_causes`, `total_edges`, `execs_per_sec`, TTFC

### TTFC Derivation

TTFC is not stored in `campaigns_summary.csv`. It is computed by:
1. Loading `triage.json` from each workdir
2. Finding the earliest crash's `sample_file` exec index
3. Mapping to wall-clock time via `coverage.csv`

---

## Discussion Section (4.6)

### Qualitative Analysis (Section 4.6.1)

Bug class categorization (CVE-matching / cross-pollination / emergent) derives from:
- `results/rq2_fresh/bug_classes.csv` — which classes appear, which match CVEs
- `results/crashes_v33/` — detailed crash evidence for BC011, BC012, BC013

### Comparison with Baseline (Section 4.6.2)

EBNF bug class discovery derives from:
- `results/comparison/data/bug_classes.csv` — filtering `grammar=ebnf`, grouping by `key_function`

---

## Processing Scripts

| Script | Purpose | Input → Output |
|---|---|---|
| `scripts/generate_figures.py` | All Ch4 figures | workdirs/ + results/ CSVs → `docs/thesis/v2/figures/fig_4_*.pdf` |
| `scripts/collect_crashes.py` | Crash evidence collection | workdirs/*/dedup_test/ → `results/crashes*/` |
| `scripts/compute_stats.py` | Statistical tests | `campaigns_summary.csv` → `rq3_statistical_tests.csv` |
| `scripts/consolidate_data.py` | Data consolidation | workdirs/ → `results/comparison/data/*.csv` |
| `scripts/triage_rq1_v35.py` | RQ1 triage | workdirs/*_v35_*/ → `results/rq1_v35/*.csv` |
| `scripts/triage_rq2.py` | RQ2 triage | workdirs/*_v33_*/ → `results/rq2_fresh/*.csv` |
| `triage/cve_signatures.py` | CVE signature matching | crash stack traces → CVE hit classification |
| `triage/stack_dedup.py` | Stack deduplication | raw crashes → unique hashes (top 5 frames) |
| `triage/fidelity_score.py` | Fidelity scoring | stack trace → 80% threshold match |

---

## Archived/Unused Data

These exist in the repo but are NOT used in the thesis:

| Path | Content | Why unused |
|---|---|---|
| `results/archive/campaigns/` | ~67 older campaigns (bandit, uniform, cross-version) | Exploratory/ablation from earlier phases |
| `results/crashes/` | 10 bug classes, 85 crashes (mixed grammar versions) | Superseded by `crashes_v33/` and `crashes_v35/` |
| `results/comparison/data_v3.3_backup/` | Backup of older v3.3 comparison | Superseded by v3.4 comparison |
| `results/zeroday/` | SQLite 3.53.0 zero-day findings | Separate from Ch4 evaluation |
| `workdirs/sqlite-3.53.0_*` | 7 zero-day campaigns | Not part of Ch4 |
| `workdirs/sqlite-*_comparison_v3.3_*` | 10 v3.3 comparison runs | Replaced by v3.4 comparison |
| `.worktrees/*/results/` | Worktree snapshots | Redundant copies |
