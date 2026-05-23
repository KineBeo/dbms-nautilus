# Chapter 4 Review Summary

**Date:** 2026-05-22
**Reviewer:** Automated systematic review (R1-R6 rule groups)
**Files:** `data_governance.md`, `flagged_issues.md`

---

## Issue Count by Priority

| Priority | Count | Description |
|---|---|---|
| **P1 Critical** | 12 | Fix before next advisor meeting |
| **P2 Important** | 10 | Fix before submission |
| **P3 Polish** | 2 | Cosmetic |
| **BLOCKED** | 1 | Cannot verify without re-running script |
| **Total** | **25** | |

---

## Top 5 Issues to Fix First

Ranked by impact on advisor feedback and credibility.

### 1. Table 4.5 mixes data from different campaign sets

**What:** The "DBMS-Nautilus" throughput and edge coverage in Table 4.5 come from v3.5 workdirs (RQ1 campaigns), while the EBNF baseline comes from comparison workdirs (RQ3). The RQ3 comparison is not apples-to-apples.

**Impact:** An advisor or reviewer checking any single throughput number against the v3.4 comparison workdirs will find a mismatch. This undermines the entire RQ3 comparison.

**Cascading:** Table 4.6, all ratio claims (61.5%, 14.5%, 2.6x), Figures 4.3-4.5, and the Summary (L394) all inherit this error.

**Fix:** Re-run `compute_stats.py` using v3.4 comparison workdirs for the proposed grammar. Or: since v3.4 and v3.5 differ only in two seed weights (0.1→0.5), document this and argue the difference is negligible. The unique RC numbers already come from v3.4 and are correct.

**Effort:** Medium — re-running the script is fast; updating all derived numbers in the .tex takes care.

---

### 2. Three grammar versions presented as one without disclosure

**What:** RQ1 uses v3.5 (boosted seeds), RQ2 uses v3.3 (no seeds), RQ3 uses v3.4 (base seeds) for RCs but v3.5 for throughput/edges. The thesis says "the proposed grammar" for all.

**Impact:** If an advisor asks "which grammar file did RQ3 use?" the answer is two different files for different metrics. This is the kind of issue that, once noticed, damages trust in all results.

**Fix:** Either (a) re-run RQ3 stats consistently from v3.4 data (preferred — they ARE the comparison campaigns), or (b) add a paragraph explaining the versioning: "v3.3 = base grammar, v3.4 = base + seeds, v3.5 = base + seeds with boosted weights for CVE-2020-13435 and CVE-2020-13871."

**Effort:** Small if option (b); Medium if option (a).

---

### 3. Unreported outlier runs distort statistics

**What:** Three anomalous runs are included in statistics but never discussed:
- EBNF 3.32.0 run1: throughput 418.5 (2x peers), edges 17218 (26% below peers). Workdir deleted.
- v3.4 3.31.1 run1: queue=123, RCs=43 (vs ~1300 queue and ~200 RCs for peers).
- v3.4 3.32.0 run1: queue=77, RCs=12 (vs ~1300 queue and ~170 RCs for peers).

**Impact:** The EBNF outlier inflates 3.32.0 throughput by 22% and makes the edge coverage p-value non-significant. The v3.4 outliers inflate standard deviations (72.4 and 73.0 in Table 4.5).

**Fix:** Either exclude with documented justification (queue_size < threshold) or discuss in threats to validity. Do not silently include.

**Effort:** Small — add a paragraph, possibly exclude and recompute.

---

### 4. Undocumented exclusions (BC005/BC007 gaps, campaign count)

**What:**
- Table 4.3 skips BC005 and BC007 with no explanation (raw data has 13 classes, thesis shows 11).
- Thesis claims "80 campaigns" but only 79 workdirs exist. Table 4.5 says "n=5 per cell" but EBNF 3.32.0 has n=4.
- EBNF 3.32.0 run1 outlier is inconsistently included (n=5 for throughput/edges, n=4 for TTFC/unique_bugs).

**Impact:** An advisor counting BC IDs will immediately ask "where is BC005?" Missing campaign = factual error.

**Fix:** Renumber BC001-BC011 sequentially or add footnote. Correct "80" to "79" or re-run missing campaign. Pick consistent n for EBNF 3.32.0.

**Effort:** Small.

---

### 5. "Previously unreported" bugs lack verification evidence

**What:** BC011, BC012, BC013 are called "newly discovered" and "previously unreported" but the thesis doesn't document any search to verify this. These bugs are on 5-6 year old SQLite versions.

**Impact:** A reviewer will ask: "Did you search the SQLite bug tracker? The NVD database? These versions are ancient."

**Fix:** Add one sentence: "We searched the NVD database and the SQLite changelog for versions 3.30.1 and 3.31.1 and found no matching reports as of [date]." Or weaken to "not matching any known CVE."

**Effort:** Small.

---

## All Issues by Priority

### P1 Critical (12 issues)

| # | Source | Rule | Issue |
|---|---|---|---|
| 1 | Step 2 | R1.1 | Table 4.5 throughput/edges from wrong campaign set (v3.5 not v3.4) |
| 2 | Step 2 | R1.1 | Table 4.6 inherits same wrong source |
| 3 | Step 2 | R1.3 | All derived ratios cascade from wrong data (61.5%, 14.5%, 2.6x) |
| 4 | Step 1 | R1.2 | Three grammar versions undisclosed |
| 5 | Step 2 | R1.2 | CVE-2020-13871 Table 4.2 says 3.32.2 but data is from 3.30.1 |
| 6 | Step 2 | R1.2 | "WindowListDelete" in discussion but data has "clearSelect" |
| 7 | Step 1 | R2.5 | "80 campaigns" but 79 exist |
| 8 | Step 1 | R2.5 | Table 4.5 says n=5 but EBNF 3.32.0 has n=4 |
| 9 | Step 3 | R2.2 | Unexplained BC005/BC007 ID gaps |
| 10 | Step 3 | R2.1 | Section order mismatch (intro says Setup→Baselines→Metrics) |
| 11 | Step 5 | R6.3 | Three outlier runs not discussed |
| 12 | Step 4 | R3.2 | EBNF 3.32.0 inconsistent n (5 for some metrics, 4 for others) |

### P2 Important (10 issues)

| # | Source | Rule | Issue |
|---|---|---|---|
| 13 | Step 6 | R4.1 | "coverage concentrated in non-vulnerable paths" — overreach |
| 14 | Step 6 | R4.1 | "vulnerability-relevant subset" — overreach |
| 15 | Step 6 | R4.2 | "demonstrates...compose" from n=2/20 — too strong |
| 16 | Step 6 | R4.2 | "demonstrating effectiveness of boosted weight" — no control |
| 17 | Step 6 | R4.3 | "previously unreported" without search documentation |
| 18 | Step 6 | R4.1 | "confirming" in summary — should be "supporting" |
| 19 | Step 7 | R5.2 | 5 of 8 hyperparameters unjustified |
| 20 | Step 7 | R5.1 | Missing: git hash, random seed, Python version, CFLAGS |
| 21 | Step 3 | R2.1 | EBNF-Baseline vs EBNF baseline inconsistency |
| 22 | Step 3 | R2.3 | Abbreviated CVE IDs in Table 4.3 |

### P3 Polish (2 issues)

| # | Source | Rule | Issue |
|---|---|---|---|
| 23 | Step 3 | — | Double spaces in 3 figure captions |
| 24 | Step 3 | R2.1 | "seed-augmented" used once, inconsistent with "with seed rules" |

### BLOCKED (1 issue)

| # | Source | Rule | Issue |
|---|---|---|---|
| 25 | Step 2 | R1.3 | Table 4.6 proposed std computation undocumented (23.6 vs 27.9 grand std) |

---

## Suggested Fix Order

The fixes have dependencies. This order minimizes rework:

1. **Decide on grammar version policy** (issue #4) — this determines whether you re-run stats or document.
2. **Re-compute RQ3 statistics from v3.4 data** (issues #1, #2, #3) — or document why v3.5 is acceptable.
3. **Handle outlier runs** (issue #11) — exclude or discuss; this changes Table 4.5 numbers.
4. **Fix n=4/5 inconsistency for EBNF 3.32.0** (issues #7, #8, #12) — decide: re-run, or use n=4 throughout.
5. **Fix Table 4.2 CVE-2020-13871** (issue #5) — clarify version in table.
6. **Fix section order sentence** (issue #10) — one-line edit.
7. **Renumber BC IDs or add footnote** (issue #9) — small edit.
8. **Fix "WindowListDelete" → "clearSelect"** (issue #6) — one word.
9. **Soften overreach claims** (issues #13-16, #18) — word substitutions.
10. **Add "previously unreported" evidence** (issue #17) — one sentence.
11. **Add reproducibility details** (issues #19, #20) — paragraph addition.
12. **Polish** (issues #21-24) — find-replace and formatting.

---

## Effort Estimates

| Fix group | Issues | Effort | Time estimate |
|---|---|---|---|
| Re-compute RQ3 from v3.4 | #1-3, #11-12 | **Large** | 2-3 hours (re-run script, update all numbers, rebuild figures) |
| Grammar version disclosure | #4 | **Small** | 30 min (add paragraph) |
| Table/text corrections | #5-10, #21-24 | **Small** | 1 hour (word edits, renumbering) |
| Soften claims + add evidence | #13-18 | **Small** | 1 hour (word substitutions, one search sentence) |
| Reproducibility additions | #19-20 | **Medium** | 1 hour (add setup details, justify parameters) |
| **Total** | 25 issues | | **5-6 hours** |
