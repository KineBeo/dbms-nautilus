# Fixed Thompson Sampling Bandit Evaluation

**Date:** 2026-05-07
**Campaigns:** N=5 per policy, 5 minutes each, sqlite-3.31.1, 1 thread
**Grammar:** grammars/active/sqlite_v3.py (v3 distilled attack grammar)

## Changes Made

1. **Beta increment condition** (`grammar_bandit.rs:213`): `raw_reward == 0.0` → `self.reward_ema > 0.1 && raw_reward < self.reward_ema * 0.5`. The old condition never fired because coverage always increases during fuzzing, collapsing all Beta distributions to Beta(alpha, 1).
2. **Alpha/beta decay**: `BETA_DECAY=0.995` applied to all groups each update round. Effective memory window ~138 rounds (70s at 200 exec/s). Prevents early-phase successes from permanently dominating.
3. **Logging**: Added per-group Beta mean (`alpha/(alpha+beta)`) column to `bandit_log.csv`.

## Results

| Metric | Fixed Bandit (N=5) | Uniform (N=5) | Diff |
|--------|-------------------|---------------|------|
| Mean total crashes | 190.0 +/- 26.0 | 180.4 +/- 21.9 | +5.3% |
| Mean unique root causes | 3.2 +/- 0.4 | 3.6 +/- 1.3 | -11% |
| Mean total edges | 18,746 +/- 169 | 18,925 +/- 267 | -0.9% |

**Mann-Whitney U (unique RCs):** U=12.0 — not statistically significant at p<0.05 (N=5 too small). Distributions are effectively equivalent.

**Mann-Whitney U (total crashes):** U=11.0 — not significant. Bandit trends higher but within noise.

### Per-Run Breakdown

| Run | Bandit crashes | Bandit RCs | Uniform crashes | Uniform RCs |
|-----|---------------|------------|-----------------|-------------|
| 1 | 198 | 3 | 166 | 3 |
| 2 | 184 | 4 | 192 | 3 |
| 3 | 190 | 3 | 149 | 3 |
| 4 | 225 | 3 | 200 | 3 |
| 5 | 153 | 3 | 195 | 6 |

## Beta Distribution Convergence

Pre-fix: all Beta means were 0.95-0.99 (beta stuck at 1.0, Polya urn — no discrimination).

Post-fix (run1, round 265):

| Group | Beta Mean | Interpretation |
|-------|-----------|----------------|
| S6_Validation | 0.4954 | Highest — validation/pragma queries rewarded |
| S3_Query | 0.4638 | High — complex SELECT patterns rewarded |
| S5_FTS | 0.4416 | Mid — FTS patterns moderately rewarded |
| S4_Boundary | 0.4203 | Mid — boundary/printf patterns moderate |
| S1_Schema | 0.3540 | Low — schema DDL penalized (saturates early) |
| S2_DML | 0.3460 | Lowest — basic DML penalized (low novelty) |

The bandit correctly identifies that Schema/DML groups saturate quickly (their coverage contribution drops after the first minute), while Validation and Query groups continue producing novel coverage later in the campaign.

## Comparison with Pre-Fix Bandit

| Metric | Pre-fix Bandit | Fixed Bandit | Uniform |
|--------|---------------|--------------|---------|
| Beta values | Stuck at 1.0 | Range 1.3-23.8 | N/A |
| Beta means | All ~0.99 (no discrimination) | Range 0.35-0.50 | N/A |
| Inter-run variance (CV) | 0.23 (high) | 0.14 (moderate) | 0.12 |
| Crash rate vs uniform | -14% (worse) | +5.3% (comparable) | baseline |
| Unique RCs vs uniform | -50% (worse) | -11% (comparable) | baseline |

The fix eliminated the pre-fix bandit's systematic underperformance. The fixed bandit is now statistically equivalent to uniform on both crash count and diversity.

## Conclusion

The fix restores discriminative power to Thompson Sampling — Beta distributions now differentiate between groups, and the decay mechanism handles the non-stationary coverage landscape. However, the fixed bandit does not yet **outperform** uniform on crash diversity (3.2 vs 3.6 mean unique RCs, p>0.05).

**Why no advantage yet:** The bandit operates on 6 coarse grammar groups covering only ~18 of many nonterminals. Most of the grammar (Expr, Literal, Table-Name, Join-Clause, etc.) is never influenced by the bandit. The adaptive weighting affects a small fraction of total grammar rules, limiting its impact.

**Next steps for improvement:**
1. Expand group coverage to include structural nonterminals (Expr, Where-Clause, Join, etc.)
2. Run longer campaigns (15-30 min) where saturation effects become more pronounced
3. Consider finer-grained per-nonterminal bandits instead of 6 coarse groups
