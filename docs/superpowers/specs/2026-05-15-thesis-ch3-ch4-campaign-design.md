# Thesis Ch3 + Ch4 + Campaign Comparison Design

**Date:** 2026-05-15
**Scope:** Three workstreams — Ch3 improvements, comparison campaign, Ch4 completion
**Dependencies:** Campaign data feeds Ch4 RQ3; Ch3 quantitative analysis informs Ch4 discussion

---

## Workstream 1: Chapter 3 Improvements

### 1A. Architecture Diagram — draw.io Redesign

**Current state:** TikZ diagram (`fig:architecture`) at `c3_method.tex:17-79`. Shows 5-component feedback loop with numbered boxes.

**Goal:** Redesign as draw.io XML for richer visuals (gradients, icons, shadows, cleaner typography). Export as PDF, replace TikZ block with `\includegraphics`.

**Components to show (same 5):**
1. Grammar Engine (Python DSL + PyO3 bridge)
2. Generation + Mutation (tree ops + unparse)
3. Fork Server + SQLite Harness (ASan + UBSan)
4. Coverage Feedback + Queue (shared memory bitmap)
5. Triage Pipeline (dedup + CVE matching)

**Data flow arrows:**
- Grammar → Generation: `rules + weights`
- Generation → Fork Server: `SQL string`
- Fork Server → Coverage: `bitmap + exit status`
- Coverage → Grammar/Generation: `interesting inputs` (feedback, dashed)
- Fork Server → Triage: `crashes` (branch, red)

**Visual improvements over TikZ:**
- Color-coded component groups (blue=grammar, green=generation, orange=execution, purple=feedback, red=triage)
- Subtle gradients on boxes
- Data type annotations on arrows with small icons
- Dashed enclosure for "fuzzing loop" region
- Clean sans-serif typography

**Output:** `docs/thesis/v2/figures/architecture.drawio` + `docs/thesis/v2/figures/architecture.pdf`

**Scope note:** Only `fig:architecture` gets draw.io treatment. The other 3 TikZ figures (two-layer, cross-pollination matrix, grammar evolution) are data-driven tables/matrices where TikZ is the right tool.

### 1B. Grammar Design — Quantitative Probability Analysis

**Add new subsection** after §3.2.3 (CVE Reachability Analysis), before §3.2.4 (Analysis).

**Title:** "Compositional Discovery Probability"

**Content:**

For each target CVE, compute the probability that a single randomly generated input contains all required structural patterns. Each pattern requires selecting the correct non-terminal alternative from a weighted distribution.

Example calculation for CVE-2020-13434:
- P(Boundary-Func-Call selected at Layer 2) = depends on Sql-Stmt structure
- P(printf alternative | Boundary-Func-Call) = w_printf / Σw_all = 3.0 / 6.5 ≈ 0.46
- P(%.*g format | Format-Spec) = 3.0 / 5.0 = 0.60
- P(INT32_MAX boundary | Boundary-Int) = 3.0 / 12.0 = 0.25
- P(all required) ≈ product of conditional probabilities

Repeat for each CVE. Show that:
- CVEs requiring 2 patterns (13434, 19646) have P ≈ 10^-2 to 10^-3
- CVEs requiring 4-5 patterns (9327, 13435) have P ≈ 10^-5 to 10^-7
- This explains time-to-first-crash ordering in campaign data

**Key insight to highlight:** Cross-pollination means adding one non-terminal improves probability for ALL CVEs that share that structural category, not just one. Quantify this multiplicative benefit.

### 1C. Grammar Design — Comparative Analysis

**Add new subsection** in §3.2 or §3.1, positioning DBMS-Nautilus against existing approaches.

**Comparison table:**

| Feature | SQLsmith | Squirrel | DBMS-Nautilus |
|---------|---------|----------|---------------|
| Grammar type | Procedural C++ | AST IR + mutation | CFG with weighted rules |
| Schema handling | Live introspection | Internal model | Self-contained (grammar generates schema) |
| Mutation strategy | Random AST node replacement | Type-aware IR mutation | Tree-level splice + havoc |
| Oracle | Crash only | Crash + differential | Crash (ASan/UBSan) |
| Coverage guidance | No | Yes | Yes |
| Vulnerability targeting | No (random) | No (semantic validity focus) | Yes (weighted structural patterns) |
| Test case isolation | No (requires running DB) | Partial | Full (empty DB, self-contained) |

**Narrative:** Each tool solves a different piece of the DBMS fuzzing problem:
- SQLsmith: broad SQL coverage via schema introspection, no guidance
- Squirrel: semantic validity via IR, reduces invalid inputs
- DBMS-Nautilus: vulnerability-directed via structural patterns, concentrates effort

---

## Workstream 2: Comparison Campaign Plan

### Configuration

| Parameter | Value |
|-----------|-------|
| Grammars | Active v3.3 (520 rules) vs Baseline EBNF (644 rules) |
| SQLite versions | 3.31.1 (CVE-2020-13434, CVE-2020-9327), 3.32.2 (CVE-2020-15358, CVE-2020-13871) |
| Runs per pair | 5 |
| Duration per run | 15 minutes (900 seconds) |
| Total campaigns | 2 grammars × 2 versions × 5 runs = 20 |
| Total compute | 20 × 15min = 5 hours |
| Threads | 1 (single-threaded for reproducibility) |
| Max tree size | 300 nodes |
| Timeout | 500ms |

### Campaign naming convention

```
YYYY-MM-DD_{grammar}_{sqlite-version}_{duration}_comparison_run{N}
```

Examples:
- `2026-05-15_v3.3_sqlite-3.31.1_15m_comparison_run1`
- `2026-05-15_ebnf_sqlite-3.31.1_15m_comparison_run1`

### Metrics to collect per campaign

1. **Total crashes** — count of files in `crashes/` dir
2. **Unique root causes** — stack-hash dedup (top 5 frames), grouped by crash function
3. **CVE signature matches** — regex match against `triage/cve_signatures.py`
4. **Edge coverage** — final bitmap count from `eval_coverage`
5. **Coverage growth curve** — sample bitmap count every 60 seconds (capture via coverage log or periodic snapshot)
6. **Throughput** — total executions / campaign duration (execs/sec)
7. **Time-to-first-crash** — timestamp of first crash file per bug class

### Automation scripts

**`scripts/run_comparison.sh`** — orchestrates all 20 campaigns:
```bash
for grammar in v3.3 ebnf; do
  for version in sqlite-3.31.1 sqlite-3.32.2; do
    for run in 1 2 3 4 5; do
      # Set grammar path, target binary, output dir
      # Run fuzzer with DURATION=900
      # Collect metrics after each campaign
    done
  done
done
```

**`scripts/collect_metrics.py`** — extracts structured data:
- Input: campaign directories
- Output: `results/comparison/metrics.json` with per-campaign metrics
- Calls triage pipeline for crash dedup + CVE matching

**`scripts/plot_results.py`** — generates publication-quality plots:
- Box plots: crash counts by grammar (matplotlib)
- Coverage growth curves with 95% confidence bands (matplotlib + scipy)
- Time-to-first-crash comparison (bar chart or survival-style)
- Throughput comparison (bar chart)
- Statistical test results annotation (Mann-Whitney U p-values)

### Statistical analysis

- **Mann-Whitney U test** (scipy.stats.mannwhitneyu) for each metric
- Null hypothesis: no difference between active and baseline grammar
- Report p-value and effect size (Cliff's delta or rank-biserial correlation)
- Significance threshold: p < 0.05
- 5 runs per group — minimum for Mann-Whitney with reasonable power

### Infrastructure prerequisites

Before running campaigns:
1. Verify baseline EBNF grammar loads: `cargo run --bin generator -- -g grammars/baseline/sqlite-ebnf.py -t 10`
2. Verify harness binaries exist: `harness/sqlite_harness_patterns_sqlite-3.31.1`, `harness/sqlite_harness_patterns_sqlite-3.32.2`
3. Verify triage pipeline works: `python3 scripts/collect_crashes.py --scan-only`
4. Coverage growth tracking: Nautilus logs edge count to `state/log.ron` periodically. If granularity is insufficient, add a 60s-interval coverage snapshot to `scripts/run_comparison.sh` using a background process that reads the bitmap file. Verify before first campaign run.

---

## Workstream 3: Chapter 4 Completion

### Structure (following school template)

```
Chapter 4: Experiments and Evaluation (Thực nghiệm và đánh giá)
├── 4.1 Research Questions [exists, update for RQ3]
├── 4.2 Experimental Setup [exists, update for comparison config]
├── 4.3 Comparison Methods (Các phương pháp đối sánh) [NEW]
│   ├── 4.3.1 Baseline EBNF Grammar
│   └── 4.3.2 Related Tools (SQLsmith, Squirrel — literature comparison)
├── 4.4 Evaluation Metrics (Độ đo đánh giá) [exists, add Mann-Whitney]
├── 4.5 Results (Kết quả thực nghiệm)
│   ├── 4.5.1 RQ1: CVE Rediscovery [exists, needs campaign data update]
│   ├── 4.5.2 RQ2: Novel Bug Discovery [partially exists]
│   └── 4.5.3 RQ3: Grammar Comparison [NEW — from campaign data]
├── 4.6 Analysis and Discussion (Phân tích và thảo luận) [NEW]
│   ├── Why structural patterns outperform EBNF
│   ├── Probability analysis connection (from Ch3 §3.2.X)
│   └── Limitations and threats to validity
└── 4.7 Threats to Validity [exists, expand]
```

### New RQ3 content plan

**RQ3: Does the structural-pattern grammar outperform a spec-complete baseline grammar for vulnerability discovery?**

Content:
- Table: active vs baseline across all metrics (mean ± std over 5 runs)
- Figure: box plots for crash counts
- Figure: coverage growth curves
- Figure: time-to-first-crash comparison
- Statistical test results with p-values
- Discussion: why structural patterns help (connect to Ch3 probability analysis)

### Ch4 "own vs reused" requirement

Template note: "Sinh viên cần mô tả phần mình cài đặt, phân tách với phần reuse"

Need a clear table or paragraph distinguishing:
- **Reused from Nautilus:** fork server protocol, coverage bitmap, tree representation, basic mutation operators
- **Original contributions:** grammar design methodology, weighted sampling integration, CVE reachability analysis framework, triage pipeline, harness design, all experiment infrastructure

### Figures to generate (Python scripts)

All in `results/comparison/figures/`:
1. `crash_counts_boxplot.pdf` — box plot, 2 grammars × 2 versions
2. `coverage_growth.pdf` — line plot with confidence bands
3. `time_to_first_crash.pdf` — grouped bar chart
4. `throughput_comparison.pdf` — bar chart
5. `cve_rediscovery_table.tex` — auto-generated LaTeX table

---

## Execution Order

```
Phase 1 (parallel):
  ├─ 1A: draw.io architecture diagram
  ├─ 1C: Ch3 comparative analysis subsection
  └─ 2-infra: Write automation scripts (run_comparison.sh, collect_metrics.py, plot_results.py)

Phase 2 (sequential, after Phase 1):
  └─ 2-run: Execute 20 campaigns (~5 hours)

Phase 3 (after campaigns complete):
  ├─ 2-analyze: Collect metrics + run statistical tests
  └─ 2-plot: Generate all figures

Phase 4 (after data available):
  ├─ 1B: Ch3 quantitative probability analysis (uses campaign data to validate predictions)
  ├─ 3-rq3: Write Ch4 RQ3 section with figures
  └─ 3-complete: Complete remaining Ch4 sections (analysis, discussion, threats)

Phase 5:
  └─ Final review: proofread + consistency check across Ch3-Ch4
```

---

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Baseline grammar produces zero crashes | RQ3 becomes trivial "baseline found nothing" | Still valid result; shows structural patterns are necessary, not just helpful |
| Baseline grammar outperforms active | Thesis contribution questioned | Unlikely given prior ablation data, but would indicate EBNF breadth > pattern depth for some versions |
| 15min too short for rare bugs | Undercount for complex CVEs (5-pattern requirement) | Prior campaigns show crashes within 5-10min; 15min is 3x that margin |
| Mann-Whitney with n=5 has low power | May not reject null even with real difference | Report effect size (Cliff's delta) alongside p-value; acknowledge limitation in threats to validity |
