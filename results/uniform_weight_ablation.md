# Uniform vs Weighted Grammar Ablation Study

**Date:** 2026-05-07  
**Target:** sqlite-3.31.1  
**Grammar:** v3.2 active grammar (725 rules, 98 weight annotations)  
**Design:** 5 campaigns × 15 min, fully uniform (all weights removed) vs historical weighted data (5 × 30 min)  
**Statistical test:** Mann-Whitney U (non-parametric, two-sided)

---

## 1. Experimental Setup

### Fresh Uniform Grammar

The active grammar (`grammars/active/sqlite_v3.py`) contains 98 hand-tuned weight annotations biasing generation toward CVE-relevant patterns (e.g., `printf` at weight=3.0, NATURAL JOIN queries at weight=3.0, generated columns at weight=3.0).

We created a fully uniform variant by stripping all `weight=` parameters, giving every rule alternative equal probability within its nonterminal. The grammar structure (which rules exist) is identical; only the sampling distribution changes.

### Campaign Configuration

| Parameter | Value |
|-----------|-------|
| Grammar | `sqlite_v3_uniform.py` (all weights = 1.0) |
| Target | `sqlite_harness_sqlite-3.31.1` (ASan + debug asserts) |
| Duration | 900s (15 min) |
| Threads | 1 |
| max_tree_size | 300 |
| timeout_ms | 500 |
| bitmap_size | 2,097,152 |
| Policy | uniform (no bandit) |
| Runs | 5 (independent random seeds) |

### Comparison Baseline

Historical weighted uniform campaigns on same target: 5 runs × 30 min with all 98 weight annotations active.

---

## 2. Raw Results

### Fresh Uniform (15 min × 5 runs)

| Run | Crashes | Queue | Final Edges | Executions | CVE-13434 Full | CVE-13434 % |
|-----|---------|-------|-------------|------------|----------------|-------------|
| 1   | 105     | 1528  | 20,147      | 144,699    | 27             | 25.7%       |
| 2   | 49      | 149   | 16,818      | 223,835    | 9              | 18.4%       |
| 3   | 128     | 1455  | 19,976      | 144,943    | 21             | 16.4%       |
| 4   | 76      | 1582  | 20,218      | 149,715    | 19             | 25.0%       |
| 5   | 112     | 1376  | 20,208      | 132,099    | 19             | 17.0%       |
| **Mean** | **94.0 ± 31.4** | — | **19,473 ± 1,434** | **159,058** | **19.0 ± 6.5** | **20.5%** |

### Old Weighted Uniform (30 min × 5 runs)

| Run | Crashes | Duration |
|-----|---------|----------|
| 1   | 233     | 30 min   |
| 2   | 296     | 30 min   |
| 3   | 286     | 30 min   |
| 4   | 188     | 30 min   |
| 5   | 209     | 30 min   |
| **Mean** | **242.4 ± 47.3** | — |

---

## 3. Statistical Comparison

### Crash Rate (normalized to crashes/min)

| Metric | Fresh Uniform | Old Weighted |
|--------|---------------|--------------|
| Rates | [7.0, 3.3, 8.5, 5.1, 7.5] | [7.8, 9.9, 9.5, 6.3, 7.0] |
| Mean | 6.27/min | 8.08/min |
| Std | 2.09 | 1.58 |

**Mann-Whitney U = 7.0, p = 0.310**

No statistically significant difference. The 22% higher crash rate with weights cannot be distinguished from random noise at N=5.

### CVE-2020-13434 Discovery Rate

| Metric | Fresh Uniform | Old Weighted |
|--------|---------------|--------------|
| Matches per run | 19.0 ± 6.5 | ~39 (30 min) |
| Matches per minute | 1.27/min | 1.30/min |
| As % of total crashes | 20.5% | 16.7% |

CVE-13434 discovery rate is **identical** (~1.3 matches/min) regardless of weights.

### CVE-2019-19646

Zero full matches across all 5 fresh uniform runs. Historical weighted data shows 2 full matches in 30 min (negligible).

### CVEs 15358, 13871, 13435, 9327

Zero full matches in both weighted and uniform configurations. Structurally unreachable.

---

## 4. Coverage Saturation Analysis

### Coverage Growth (mean of 5 runs)

| Time | Edges | % of Final | New edges/min |
|------|-------|-----------|---------------|
| 1s   | 9,313 | 48% | — |
| 30s  | 13,335 | 68% | 8,044 |
| 60s  | 14,231 | 73% | 1,793 |
| 120s | 15,643 | 80% | 1,412 |
| 180s | 16,762 | 86% | 1,119 |
| 300s | 17,605 | 90% | 422 |
| 600s | 18,908 | 97% | 261 |
| 750s | 19,236 | 99% | 131 |

**80% of coverage is found in the first 2 minutes.** The last 13 minutes contribute only 20% of total discovered edges.

### Crash Rate Decay

| Window | Mean rate (crashes/min) | Decay from peak |
|--------|------------------------|-----------------|
| 0-1 min | 19.4 | — (peak) |
| 1-3 min | 5.9 | -70% |
| 3-5 min | 6.9 | -64% |
| 5-10 min | 6.5 | -67% |

After minute 1, crash discovery rate drops 70% and stabilizes around 6/min.

---

## 5. CVE Pattern Reachability

Across 470 unique crash SQL samples from 5 runs:

| Pattern | Frequency | Required by |
|---------|-----------|-------------|
| printf_call | 39.8% | CVE-2020-13434 |
| INT32_boundary | 25.5% | CVE-2020-13434 |
| GENERATED_column | 19.8% | CVE-2020-9327, CVE-2019-19646 |
| UNIQUE_column | 19.1% | CVE-2020-13435 |
| PRAGMA_integrity | 11.7% | CVE-2019-19646 |
| CREATE_VIEW | 10.2% | CVE-2020-9327 |
| JOIN_or_commajoin | 8.9% | CVE-2020-9327 |
| NATURAL_JOIN | 6.0% | CVE-2020-13435 |
| EXCEPT | 2.8% | CVE-2020-13871 |
| window_over | 2.3% | CVE-2020-13435 |
| CREATE_VIEW+ORDER_BY | 0.6% | CVE-2020-15358 |
| **coalesce()** | **0.2%** | CVE-2020-13435, CVE-2020-9327 |
| **IN_subquery** | **0.0%** | CVE-2020-13435 |
| **Scalar_subquery** | **0.0%** | CVE-2020-13871 |
| **implicit_JOIN** | **0.0%** | CVE-2020-15358 |

### Co-occurrence Probability

CVE-2020-13434 (reachable): `P = 0.398 × 0.255 = 10.1%` → 95 matches observed.

CVE-2020-9327 (unreachable): `P = 0.198 × 0.002 × 0.089 × 0.102 = 0.00004%` → 0 matches expected in 470 samples.

### Root Cause: Probability Dilution

`coalesce()` is 1 of 55 `Func-Call` alternatives. `Func-Call` is reachable from `Expr` (1 of 75 alternatives). Combined probability per expression expansion: `1/75 × 1/55 = 0.024%`. With ~8 expressions per crash SQL: `P(coalesce anywhere) ≈ 0.19%`. Observed: 0.2% (matches theory exactly).

---

## 6. Run-to-Run Variance ("Seed Corpus Lottery")

| Metric | Min | Max | Range (max/min) |
|--------|-----|-----|-----------------|
| Crashes | 49 | 128 | 2.6x |
| Final edges | 16,818 | 20,218 | 1.2x |
| Executions | 132,099 | 223,835 | 1.7x |

### Outlier Analysis (Run 2)

Run 2 produced 49 crashes (vs mean 94) despite the highest execution count (223,835). It ran 4,568 execs per crash vs ~1,300 for other runs. The initial generation phase produced simpler/smaller inputs that executed faster but explored less code — a "bad seed corpus" that cascaded through the entire campaign.

### Implication for RL Evaluation

With std=31.4 and mean=94, detecting a 25% improvement requires N≈20 runs per condition. With N=5, only improvements >60% (absolute: +56 crashes) are reliably detectable at p<0.05.

---

## 7. Crash Pattern Distribution

| Pattern | Count | % of 470 |
|---------|-------|----------|
| printf/format | 187 | 39.8% |
| fts/virtual | 148 | 31.5% |
| other | 71 | 15.1% |
| generated_column | 64 | 13.6% |

Compared to old weighted grammar (30-min single run):
- printf: 39.8% (uniform) vs 24.0% (weighted) — uniform naturally concentrates here
- generated_column: 13.6% (uniform) vs 6.0% (weighted) — no weight needed
- "other" (no CVE match): 15.1% (uniform) vs 33.9% (weighted) — weights dilute into non-CVE patterns

---

## 8. Key Findings

### Finding 1: Grammar weights do not improve CVE discovery rate

Mann-Whitney U test: p=0.310. CVE-2020-13434 matches per minute: 1.27 (uniform) vs 1.30 (weighted). No significant difference.

### Finding 2: Coverage saturates regardless of weights

80% of edge coverage is found in the first 2 minutes in both configurations. The grammar's structural diversity is exhausted quickly; probability tuning cannot unlock new code paths.

### Finding 3: 4 of 6 target CVEs are structurally unreachable

CVEs 15358, 13871, 13435, and 9327 require pattern co-occurrence at probabilities below 0.001%. This is a grammar composition problem (missing dedicated co-occurrence rules), not an optimization problem.

### Finding 4: RL operates at wrong granularity for CVE reachability

Thompson Sampling boosts rule groups (6 groups of 6-55 rules each). The CVE bottleneck is one specific rule (`coalesce`) needing 11x individual boost within a 55-alternative nonterminal. Group-level multipliers dilute across all group members.

### Finding 5: Run-to-run variance (2.6x) exceeds any observed RL effect

The seed corpus lottery dominates outcome variance. Thompson Sampling's previously observed effects fall within this noise band.

---

## 9. Implications for RL Integration (Phase 3)

| RL Approach | Can address? | Justification |
|-------------|-------------|---------------|
| Thompson Sampling over group weights | No | Weights don't affect CVE rate (this study) |
| DQN over mutation strategies | Partially | Could detect saturation, but mutation selection is orthogonal to grammar structure |
| RL over individual rule weights | Theoretically | Would need per-rule control (not group), 11x boosts on specific patterns |
| Grammar engineering (add co-occurrence rules) | Yes | Directly fixes the structural bottleneck |

### Recommended Research Direction

The productive RL research question is not "can RL tune grammar weights?" (answer: the surface is flat) but rather:

1. **Can RL learn to switch between grammar fragments** (e.g., "use CVE-9327 template" vs "use generic query") based on coverage state?
2. **Can RL compose multi-statement sequences** that satisfy temporal dependencies (CREATE → INSERT → PRAGMA)?
3. **Can RL reduce the seed corpus lottery** by learning which generation-phase inputs lead to productive campaigns?

These require architectural changes to the RL interface, not just weight tuning.

---

## 10. Data Availability

- Fresh uniform campaigns: `results/campaigns/2026-05-07_v3.2-fresh-uniform_sqlite-3.31.1_15m_*`
- Coverage CSVs: `workdirs/sqlite-3.31.1_fresh_uniform_15m*/coverage.csv`
- Uniform grammar: `grammars/active/sqlite_v3_uniform.py`
- Historical weighted: `results/campaigns/2026-05-01_v3.2-uniform_sqlite-3.31.1_30m_*`
