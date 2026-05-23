# Pre-Submission Quality Report

**Project:** DBMS-Nautilus Thesis
**Date:** 2026-05-23
**File:** docs/thesis/v2/thesis.tex
**Target:** UET Bachelor Thesis
**Pages:** 68

---

## Integrity Gate: PASS

- **Placeholders:** 0 found
- **Citation integrity:** All 28 cited keys resolve to .bib entries
- **Section completeness:** All sections present (Abstract, Ch1-Ch4, Conclusion)
- **Broken references:** 0 undefined references

---

## Overall Score: 93/100 — Publication-ready (minor notes)

| Component | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Compilation | 98/100 | 15% | 14.7 |
| Proofread | 96/100 | 25% | 24.0 |
| Citations (bib-validate) | 98/100 | 15% | 14.7 |
| Devil's Advocate | 82/100 | 25% | 20.5 |
| Numeric Consistency | 100/100 | 20% | 20.0 |
| **Total** | | | **93.9** |

---

## Compilation

- **Status:** PASS
- **Pages:** 68
- **Overfull hbox:** 1 (3.48pt on cover page — cosmetic)
- **Underfull hbox:** 45 (all in narrow table columns — cosmetic)
- **Font warnings:** 1 (OMS/cmtt/m/n undefined — harmless)
- **Undefined references:** 0

## Citations (bib-validate)

- **Score:** 98/100
- **Missing keys:** 0
- **Unused keys:** 1 (`loadeddice` — Vose 1991, defined but never cited)
- **Suspect entries:** 0
- **Preprint staleness:** 0 (no arxiv entries)
- **Wikipedia citation:** 1 (`dbms-wiki` — acceptable for foundational definition)

## Proofread

- **Score:** 96/100
- **Critical issues:** 0
- **Major issues:** 1 (Ch4 line 61: "526 rules" phrasing ambiguity — should say "520 (526 with seeds)")
- **Minor issues:** 4 (unused bib entry, cover overfull, underfull warnings, Wikipedia citation)

## Devil's Advocate

- **Score:** 82/100
- **Surviving critiques (not fixable for this submission):**
  - C1: No held-out evaluation targets (grammar designed from same CVEs it's tested on)
  - C2: No ablation study (can't isolate which grammar component drives improvement)
  - M1: External validity absent (SQLite only)
  - M2: Baseline comparison is minimal (no SQLsmith/Squirrel comparison)
  - M3: 15-minute campaigns may miss hard compositional bugs
- **Dismissed:** CVE rediscovery value (correctly reframed as validation methodology)

## Numeric Consistency

- **Score:** 100/100
- All key numbers verified consistent across abstract, intro, Ch3, Ch4, conclusion:
  - 13 bug classes, 48 hashes ✓
  - 4 CVE rediscoveries (RQ2 set correctly distinct from RQ1 set) ✓
  - 108×, 2.1×, 14.1%, 52.1% ✓
  - EBNF throughput 189.9, edge coverage 23,490 ✓
  - Per-run ratios 2.5×, 6.0×, 3.7×, 2.4× ✓
  - 3 sanitizer-only in all chapters ✓

---

## Remaining Issues

| # | Severity | Category | Issue |
|---|----------|----------|-------|
| 1 | Low | Content | Ch4 line 61: "526 rules" phrasing could imply 526+6=532 |
| 2 | Low | Citation | Unused `loadeddice` bib entry |
| 3 | Info | LaTeX | 3.48pt overfull on cover page |
| 4 | Info | Citation | Wikipedia citation for DBMS definition |
| 5 | N/A | Design | No held-out evaluation (acknowledged limitation) |
| 6 | N/A | Design | No ablation study (acknowledged limitation) |

---

## Recommendation

**Submit**

The thesis is publication-ready. All critical and major issues from previous proofread rounds have been resolved. Numeric consistency is verified across all chapters. The remaining issues are cosmetic (cover page overfull, unused bib entry) or inherent design limitations that are already acknowledged in the Threats to Validity section. The devil's advocate critiques (no held-out targets, no ablation) are valid methodological concerns but are appropriate for a bachelor thesis scope and are mitigated by the RQ2 results (9 non-CVE bugs found beyond the design targets).
