# Proofread Report — Full Thesis

**Document:** thesis.tex (all chapters)
**Date:** 2026-05-23
**Pages:** 68

## Summary

| Category | Critical | Major | Minor |
|----------|----------|-------|-------|
| Grammar & spelling | 1 | 0 | 2 |
| Notation consistency | 1 | 1 | 2 |
| Citation format | 0 | 2 | 6 |
| Academic tone | 0 | 5 | 4 |
| LaTeX-specific | 0 | 0 | 4 |
| Citation voice balance | 0 | 1 | 0 |
| Numeric cross-check | 4 | 2 | 1 |
| Causal language | 0 | 2 | 0 |
| Equation completeness | 0 | 0 | 0 |
| Preprint staleness | 0 | 0 | 0 |
| Duplicate content | 1 | 0 | 0 |
| **Total** | **7** | **13** | **19** |

---

## Critical Issues

### C1: Abstract broken grammar (abstract_en.tex:10)
"The heart of the proposed system is a context-free grammar consisting of 526 production rules encodes several SQL attack patterns" — fused predicate, missing "that."
**Fix:** "...a context-free grammar of 526 production rules that encodes..."

### C2: Abstract/intro conflate two different CVE sets (abstract:12, intro:14)
RQ1 (with seeds) = {13434, 13435, 13871, 15358}. RQ2 (without seeds) = {13434, 13435, 9327, 13871}. Current text implies both "all 4 target CVEs" and "4 CVE rediscoveries without seeds" are the same set. CVE-15358 is RQ1-only; CVE-9327 is RQ2-only.
**Fix:** Separate the two findings with distinct CVE sets.

### C3: Numeric error — EBNF mean throughput (c4:411, 470)
Prose says "189.4". Actual: (196.3+182.7+198.0+182.4)/4 = 189.85 ≈ 189.9.
**Fix:** Change 189.4 → 189.9 in both locations.

### C4: Numeric error — Unique RC ratio range (c4:411)
Prose says 70×–297×. Actual minimum: 215.4/3.6 = 59.8× ≈ 60×.
**Fix:** Change 70× → 60×. (Note: we changed 60→70 earlier based on wrong arithmetic; the original 60× was correct.)

### C5: Numeric error — Per-run ratio for v3.32.0 (c4:247, Table 4.6)
Table shows 3.5×. Actual: 4.4/1.2 = 3.67 ≈ 3.7×.
**Fix:** Change 3.5× → 3.7×.

### C6: Incorrect TTFC bolding in Table 4.7 (c4:403-404)
DBMS-Nautilus is bolded for TTFC on v3.30.1 (tie: 1.8 vs 1.8) and v3.31.1 (worse: 1.8 vs 1.2). Bold should mark the better value.
**Fix:** Remove bold from DBMS on v3.30.1 (tie), move bold to EBNF on v3.31.1.

### C7: Duplicate passage in Ch2 (c2:134 and 149)
Near-verbatim repetition about Nautilus discovering 13 bugs across 4 targets.
**Fix:** Cut the repeat at line 149.

---

## Major Issues

### M1: Missing asterisk footnote in Table 4.3 (c4:143)
`4/5*` has no footnote explaining the asterisk.
**Fix:** Add table note.

### M2: Abstract/intro omit "3 sanitizer-only" sub-count (abstract:12, intro:14)
4+6=10, not 13. Missing third sub-category.
**Fix:** Add "and 3 sanitizer-only detections."

### M3: Abstract "heart of the proposed system" metaphor (abstract:10)
Informal for academic writing.
**Fix:** "The central component of DBMS-Nautilus is..."

### M4: Abstract "promising approach" filler (abstract:8)
**Fix:** Delete or replace with specific characterization.

### M5: Abstract "wasting energy (time)" parenthetical gloss (abstract:8)
**Fix:** "wasting fuzzing time on low-value syntactic paths."

### M6: Intro "pay enough attention" colloquial (intro:6)
**Fix:** "none of these systems treat the grammar as a design variable."

### M7: Ch3 "chicken-and-egg" informal (c3:499)
**Fix:** "creating a circularity: the grammar must be evaluated to assess its weights."

### M8: Ch3 520 vs 526 rules (c3:6)
Overview says 520 without noting RQ1 augmentation to 526.
**Fix:** "520 production rules (526 with RQ1 seed rules)."

### M9: Causal overclaim "dominant factor" (abstract:12)
**Fix:** "suggesting that grammar specificity has a larger effect on crash diversity than throughput."

### M10: Causal overclaim "redirects" (conclusion:12)
**Fix:** "is consistent with the hypothesis that structural complexity concentrates effort on crash-prone code paths."

### M11: Ch2 misplaced `\citep{sqlancer}` for SQL dialect claim (c2:7)
**Fix:** Cite a more appropriate reference or restructure.

### M12: EBNF mean edge coverage discrepancy (c4:411)
Prose says 23,482. Actual: (23323+23182+23645+23811)/4 = 23490.
**Fix:** Change 23,482 → 23,490.

### M13: Throughput percentage rounding (c4:446)
Answer box says 52.0%. Actual: (1-90.85/189.85)×100 = 52.1%.
**Fix:** Change 52.0% → 52.1%.

---

## Minor Issues (top 10)

- m1: 11 instances of `\citep` where `\citet` needed (Ch2/Ch3: tool names as subjects)
- m2: Em-dash spacing inconsistency across chapters
- m3: Dangling participial phrase (c2:9)
- m4: "crowding out" informal (c3:499)
- m5: "no amount of" informal (c3:501)
- m6: "genuine" filler qualifier (conclusion:4)
- m7: "lever" metaphor (intro:8)
- m8: Undefined INT32_MAX etc. first use (c3:392)
- m9: 28 underfull hbox warnings from Table 4.2 monospace columns
- m10: Ambiguous campaign counting — are RQ2 and RQ3 DBMS campaigns the same runs? (c4:100)

---

## Quality Score

| Metric | Value |
|--------|-------|
| **Score** | 72 / 100 |
| **Verdict** | Revise |

### Deductions

| # | Issue | Tier | Deduction | Category |
|---|-------|------|-----------|----------|
| C1 | Abstract broken grammar | Critical | -5 | Grammar |
| C2 | CVE set conflation | Critical | -5 | Numeric |
| C3 | EBNF throughput 189.4→189.9 | Critical | -3 | Numeric |
| C4 | RC ratio 70×→60× | Critical | -3 | Numeric |
| C5 | Per-run ratio 3.5×→3.7× | Critical | -2 | Numeric |
| C6 | TTFC bolding wrong | Critical | -2 | Notation |
| C7 | Duplicate passage Ch2 | Critical | -3 | Duplicate |
| M1-M13 | 13 major issues | Major | -1 each = -13 | Various |
| m1-m10 | Minor pattern | Minor | 0 (grouped) | Various |
| | **Total deductions** | | **-36** | |

Note: Score of 72 is "Revise" — the 7 Critical issues (especially C2 and the numeric errors) must be fixed before submission. Most are quick fixes (word changes, number corrections).

---

## Recommendations

**Priority 1 — Fix immediately (Critical):**
1. C1: One-word grammar fix in abstract
2. C2: Separate RQ1 and RQ2 CVE sets in abstract/intro
3. C3-C5: Three arithmetic corrections (189.4→189.9, 70×→60×, 3.5×→3.7×)
4. C6: Fix TTFC bolding in Table 4.7
5. C7: Cut duplicate Nautilus paragraph in Ch2

**Priority 2 — Fix before submission (Major):**
6. M1: Add asterisk footnote to Table 4.3
7. M2: Add "3 sanitizer-only" to abstract/intro
8. M3-M6: Tone fixes in abstract/intro (5 word changes)
9. M9-M10: Soften causal language
10. M12-M13: Fix edge coverage and throughput percentage numbers

**Priority 3 — Polish (Minor):**
11. Convert `\citep` to `\citet` where tool names are subjects (11 instances)
12. Fix informal language in Ch3 (chicken-and-egg, crowding out)
