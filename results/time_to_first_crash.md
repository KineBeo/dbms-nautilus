# Time-to-First-Crash Analysis

**Date:** 2026-05-05
**Data source:** `workdirs/*/coverage.csv` (1-second resolution)
**Campaigns:** N=5 per (version, policy) pair; 3 versions × 2 policies = 30 total runs (+9 from 3.31.1 unfixed series)

## Summary

**Both policies find their first crash within 1-2 seconds.** No meaningful difference in time-to-first-crash between bandit and uniform sampling. The grammar generates triggering inputs essentially immediately.

This metric does NOT differentiate policies. The differentiating metric is **crash diversity** (unique root causes per campaign), where uniform outperforms bandit significantly (p≈0.01, Mann-Whitney U).

## Time-to-First-Crash

| Version | Policy | N | Mean(s) | Median(s) | Min | Max | Std |
|---------|--------|---|---------|-----------|-----|-----|-----|
| sqlite-3.30.1 | bandit | 5 | 1.0 | 1.0 | 1 | 1 | 0.0 |
| sqlite-3.30.1 | uniform | 5 | 1.2 | 1.0 | 1 | 2 | 0.4 |
| sqlite-3.31.1 | bandit | 10 | 1.5 | 1.5 | 1 | 2 | 0.5 |
| sqlite-3.31.1 | uniform | 10 | 1.4 | 1.0 | 1 | 2 | 0.5 |
| sqlite-3.32.0 | bandit | 4 | 1.5 | 1.5 | 1 | 2 | 0.6 |
| sqlite-3.32.0 | uniform | 5 | 1.8 | 2.0 | 1 | 3 | 0.8 |
| **ALL** | **bandit** | **19** | **1.4** | **1.0** | **1** | **2** | **0.5** |
| **ALL** | **uniform** | **20** | **1.4** | **1.0** | **1** | **3** | **0.6** |

## Crash Accumulation Over Time

| Version | Policy | N | @60s | @300s | @600s | @900s | @1800s |
|---------|--------|---|------|-------|-------|-------|--------|
| sqlite-3.30.1 | bandit | 5 | 21 | 53 | 99 | 140 | 243 |
| sqlite-3.30.1 | uniform | 5 | 21 | 54 | 106 | 150 | 278 |
| sqlite-3.31.1 | bandit | 10 | 25 | 59 | 104 | 142 | 196 |
| sqlite-3.31.1 | uniform | 10 | 28 | 60 | 109 | 144 | 195 |
| sqlite-3.32.0 | bandit | 4 | 26 | 56 | 88 | 119 | 198 |
| sqlite-3.32.0 | uniform | 5 | 23 | 59 | 103 | 148 | 261 |

## Crash Rate Decay (crashes/min by time window)

| Version | Policy | 0-5min | 5-10min | 10-15min | 15-30min |
|---------|--------|--------|---------|----------|----------|
| sqlite-3.30.1 | bandit | 10.7 | 9.0 | 8.3 | 6.9 |
| sqlite-3.30.1 | uniform | 10.8 | 10.4 | 8.9 | 8.5 |
| sqlite-3.31.1 | bandit | 11.9 | 8.9 | 7.7 | 3.5 |
| sqlite-3.31.1 | uniform | 12.1 | 9.6 | 7.0 | 3.4 |
| sqlite-3.32.0 | bandit | 11.2 | 6.4 | 6.2 | 5.3 |
| sqlite-3.32.0 | uniform | 11.9 | 8.6 | 9.2 | 7.5 |
| **ALL** | **bandit** | **11.4** | **8.4** | **7.5** | **4.8** |
| **ALL** | **uniform** | **11.7** | **9.6** | **8.0** | **5.7** |

**Rate decay:** Bandit -58%, Uniform -51% (early → late window).

## Interpretation

1. **TTFC is not a differentiator** — both policies crash within 1-2 seconds. The grammar's structural patterns are immediately effective.

2. **Crash accumulation** — roughly equal at short timescales (first minute), slight divergence at 30 minutes (uniform accumulates ~14% more total crashes on 3.30.1 and 3.32.0).

3. **Rate decay supports exploitation hypothesis** — bandit's crash discovery rate drops faster (-58%) than uniform (-51%) as it converges on exploiting known-good rule paths. Uniform maintains broader exploration, finding new crash paths longer.

4. **Key thesis point:** Time-to-first-crash is the wrong metric for grammar-based fuzzers targeting CVE-class bugs. What matters is structural diversity of discovered crashes, not speed to first trigger. This is where uniform's exploration advantage manifests (2x unique root causes per campaign).
