# Proofread Report — Chapter 3 (Proposed Method)

**Document:** `chapters/c3_method.tex`
**Date:** 2026-05-17
**Pages:** ~12 (290 source lines)

## Summary

| Category | Critical | Major | Minor |
|----------|----------|-------|-------|
| Grammar & spelling | 0 | 0 | 1 |
| Notation consistency | 0 | 0 | 0 |
| Citation format | 0 | 1 | 0 |
| Academic tone | 0 | 0 | 0 |
| LaTeX-specific | 0 | 1 | 2 |
| Citation voice balance | 0 | 0 | 0 |
| TikZ diagrams | 0 | 0 | 0 |
| Numeric cross-check | 1 | 1 | 0 |
| Causal language | 0 | 0 | 0 |
| Equation completeness | 0 | 0 | 0 |
| Preprint staleness | 0 | 0 | 0 |
| **Total** | **1** | **3** | **3** |

## Critical Issues

### C1: Bug class count mismatch with crash archive (line 276)

- **Category:** Numeric cross-check
- **Location:** line 276
- **Problem:** Text says "seven non-CVE bug classes" and Chapter 4 says "10 bug classes" total with "89 unique stack hashes." However, the crash archive cleanup (2026-05-17) removed BC009 (signal-6 debug asserts = noise, not real bugs), reducing totals to **9 bug classes** and **85 unique hashes**. Also added BC006 (sqlite3ExprCodeTarget null ptr, 3 hashes from v3.4/EBNF campaigns) which wasn't in the original table.
- **Fix:** Update Chapter 3 line 276: "seven" → check against updated Ch4 table. Update Chapter 4: remove BC009 row, add new BC006 (ExprCodeTarget), update total from 89→85, update "10 bug classes" → "10 bug classes" (if BC006 replaces BC009 count stays same) or adjust accordingly. Cross-reference `results/crashes/` for ground truth.

## Major Issues

### M1: All citations use raw `\cite{}` — natbib is loaded (all 12 instances)

- **Category:** Citation format
- **Location:** lines 4, 11, 23, 29, 63, 84, 91, 133, 174, 202, 226, 285
- **Problem:** The document loads `natbib` with `\usepackage[sort&compress]{natbib}`, which provides `\citet{}` (textual) and `\citep{}` (parenthetical). All 12 citations in Ch3 use raw `\cite{}`. With `unsrt` bibliographystyle, `\cite` works identically to `\citep`, so this is not a compilation error, but it prevents future switching to author-year style and is inconsistent with natbib best practice.
- **Fix:** Convert each `\cite{key}` to `\citep{key}` (parenthetical) or `\citet{key}` (textual, when the author name is grammatically part of the sentence). In Ch3, all uses are parenthetical references, so all should become `\citep{key}`.

### M2: Overfull hbox in chapter intro paragraph (12.28pt)

- **Category:** LaTeX-specific
- **Location:** thesis.log line 1209 → c3_method.tex line 11 (System Overview opening paragraph)
- **Problem:** Overfull hbox 12.28pt too wide. This is visible in the PDF as text extending into the right margin.
- **Fix:** Reword the long sentence or add a discretionary hyphenation (`\-`) in a long word. The paragraph at line 11 has a 4-line sentence starting "Where existing SQL fuzzers..." that likely causes the overflow.

### M3: Chapter 4 numbers need sync after crash archive cleanup

- **Category:** Numeric cross-check
- **Location:** Chapter 3 line 276 references "seven non-CVE bug classes" from Ch4
- **Problem:** The checkpoint notes (2026-05-17) confirmed: BC004 hashes changed 42→56, new BC006 (ExprCodeTarget) added, old BC009 (signal-6 noise) removed, total 89→85 hashes. Ch3 forward-references Ch4 numbers that are now stale.
- **Fix:** After updating Ch4 tables, verify Ch3 line 276 still says the correct count of non-CVE bug classes.

## Minor Issues

### m1: "2~MB" inconsistent spacing (not in this file but referenced)

- **Category:** Grammar & spelling
- **Location:** Not directly in c3_method.tex but referenced from Ch4
- **Problem:** N/A for Ch3 — no instances found. Noting for cross-chapter consistency.
- **Fix:** N/A

### m2: Underfull hbox warnings in listings (badness 10000, 20+ instances)

- **Category:** LaTeX-specific
- **Location:** thesis.log lines 1261-1443 (listings in Sec 3.2)
- **Problem:** Code listings produce many underfull hbox warnings (badness 10000) because lstlisting environments with short lines leave large whitespace. This is cosmetic — listings render correctly.
- **Fix:** No action needed. These are inherent to `lstlisting` with `basicstyle=\ttfamily\small` in narrow columns.

### m3: Float placement `[htbp]` used consistently

- **Category:** LaTeX-specific
- **Location:** lines 15, 42, 65, 118, 230
- **Problem:** All floats use `[htbp]` — acceptable but `[tbp]` is generally preferred to avoid mid-paragraph float placement. Minor, current output looks fine.
- **Fix:** Optional. Switch to `[tbp]` if floats are breaking paragraph flow in the compiled PDF.

## Quality Score

| Metric | Value |
|--------|-------|
| **Score** | 88 / 100 |
| **Verdict** | Ship with notes |

### Deductions

| # | Issue | Tier | Deduction | Category |
|---|-------|------|-----------|----------|
| 1 | Bug class count stale after crash cleanup | Critical | -5 | Numeric cross-check |
| 2 | All `\cite` should be `\citep` (natbib loaded) | Major | -3 | Citation format |
| 3 | Overfull hbox 12.28pt in opening paragraph | Major | -2 | LaTeX-specific |
| 4 | Forward-reference to stale Ch4 numbers | Major | -2 | Numeric cross-check |
| | **Total deductions** | | **-12** | |

## Recommendations

1. **Priority 1:** Fix the numeric cross-check (C1/M3). Update Ch4 table first, then verify Ch3 line 276 matches.
2. **Priority 2:** Batch-convert `\cite` → `\citep` across all chapters for natbib consistency.
3. **Priority 3:** Reword line 11 sentence to fix the 12pt overfull hbox.
4. The writing quality is strong — clear structure, precise terminology, good code examples. Academic tone is appropriate throughout. No filler phrases detected.
