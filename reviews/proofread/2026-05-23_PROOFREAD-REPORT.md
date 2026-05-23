# Proofread Report

**Document:** c4_experiments.tex (Section 4.5.2 RQ2 through Section 4.6 Discussion)
**Date:** 2026-05-23
**Pages:** ~10 (pages 42-51 of thesis)

## Summary

| Category | Critical | Major | Minor |
|----------|----------|-------|-------|
| Grammar & spelling | 0 | 0 | 1 |
| Notation consistency | 0 | 0 | 0 |
| Citation format | 0 | 0 | 0 |
| Academic tone | 0 | 1 | 1 |
| LaTeX-specific | 0 | 0 | 0 |
| Citation voice balance | 0 | 0 | 0 |
| TikZ diagrams | 0 | 0 | 0 |
| Numeric cross-check | 1 | 1 | 0 |
| Causal language | 0 | 0 | 0 |
| Equation completeness | 0 | 0 | 0 |
| Preprint staleness | 0 | 0 | 0 |
| **Total** | **1** | **2** | **2** |

## Critical Issues

### C1: Summary section has stale RQ2 numbers (line 515)
- **Category:** Numeric cross-check
- **Location:** `c4_experiments.tex:515` (Section 4.6.5 Summary)
- **Problem:** The Summary says "3 are known CVE rediscoveries, 5 are grammar-exclusive production bugs affecting up to 10 consecutive releases each, and 5 are sanitizer-only detections" — but the RQ2 section above says 4 CVE matches, 6 non-CVE production bugs, and 3 sanitizer-only. The Summary was not updated when the CVE mappings changed.
- **Fix:** Change to: "4 are CVE rediscoveries, 6 are non-CVE production bugs affecting up to 10 consecutive releases each, and 3 are sanitizer-only detections"

## Major Issues

### M1: Summary says "EBNF-Baseline's CVE rediscovery was limited to CVE-2020-13871" (line 515)
- **Category:** Numeric cross-check
- **Location:** `c4_experiments.tex:515` (last sentence of Summary)
- **Problem:** The old text says EBNF found CVE-2020-13871 on version 3.30.1. But with the new CVE mapping, CVE-2020-13871 = BC007, and the EBNF did NOT find BC007 (source of truth: BC007 EBNF column is "---"). The EBNF found BC004, which is no longer mapped to any CVE. This sentence is now misleading.
- **Fix:** Remove or rewrite. Suggested: "The EBNF-Baseline found 4 of the 13 bug classes (BC002, BC004, BC005, BC011), none of which match the 4 CVE-rediscovery classes."

### M2: "dramatically" in RQ3 prose (line 440)
- **Category:** Academic tone
- **Location:** `c4_experiments.tex:440`
- **Problem:** "dramatically higher crash diversity" — vague intensifier. The exact number (108×) is stated elsewhere; "dramatically" adds no precision.
- **Fix:** Delete "dramatically" → "in exchange for higher crash diversity"

## Minor Issues

### m1: "We present" opening (line 260)
- **Category:** Academic tone
- **Location:** `c4_experiments.tex:260`
- **Problem:** "We present five representative bugs" — first-person is acceptable but could be more direct.
- **Fix:** Optional. Could change to "Five representative bugs illustrate..." but current form is acceptable for a thesis.

### m2: Inconsistent abbreviation "UAF" vs full "use-after-free" (Table 4.5 and prose)
- **Category:** Grammar & spelling
- **Location:** Table 4.5 line 227 ("Heap UAF") vs prose at lines 286, 305, 339 ("use-after-free")
- **Problem:** BC011 is called "Heap UAF" in the table but "Heap use-after-free" in the Selected Bugs prose. Inconsistent abbreviation.
- **Fix:** Use "Heap use-after-free" consistently, or define "UAF" on first use and use it throughout.

## Quality Score

| Metric | Value |
|--------|-------|
| **Score** | 88 / 100 |
| **Verdict** | Ship with notes |

### Deductions

| # | Issue | Tier | Deduction | Category |
|---|-------|------|-----------|----------|
| C1 | Summary section stale numbers (3 CVE → 4, 5 prod → 6, 5 sanit → 3) | Critical | -5 | Numeric cross-check |
| M1 | Summary EBNF/CVE-13871 claim now wrong | Major | -3 | Numeric cross-check |
| M2 | "dramatically" vague intensifier | Major | -2 | Academic tone |
| m1 | "We present" opening | Minor | -1 | Academic tone |
| m2 | Inconsistent UAF abbreviation | Minor | -1 | Grammar & spelling |
| | **Total deductions** | | **-12** | |

## Recommendations

1. **Fix C1 and M1 immediately** — the Summary section at the end of Chapter 4 has stale numbers from the old CVE mapping. This is the most impactful fix.
2. **M2 is easy** — just delete "dramatically" on line 440.
3. **m2** — either expand "Heap UAF" to "Heap use-after-free" in the table, or add "(UAF)" parenthetical on first prose use and use "UAF" in the table. Given the table space constraints, keeping "Heap UAF" in the table and spelling it out in prose is acceptable.
