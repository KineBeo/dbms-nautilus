# Pre-Submission Quality Report

**Project:** DBMS-Nautilus Thesis v2
**Date:** 2026-05-13
**File:** docs/thesis/v2/thesis.tex
**Target:** UET-VNU Bachelor's Thesis Defense (June 2026)

---

## Integrity Gate: PASS

- **Placeholders:** 0 found
- **Citation integrity:** all 24 keys resolved (24 cited = 24 bib entries)
- **Section completeness:** all sections present and non-empty (Abstract, Ch1–Ch4, Conclusion)
- **Broken references:** 0 undefined refs, 0 undefined citations

---

## Overall Score: 76/100 — Significant Revisions Recommended

This score reflects strong writing quality and methodology design with gaps in experimental rigor (no baseline comparison, no statistical replication) that are addressable before defense.

---

## Compilation

- **Status:** PASS
- **Overfull hbox:** 16 total, 2 >50pt (c2 listing 119pt, c4 case study 51pt)
- **Underfull hbox:** 13
- **LaTeX warnings:** 4 (font shape substitutions, non-critical)
- **Undefined references:** 0

## Citations

- **Missing keys:** 0
- **Unused keys:** 0
- **Suspect entries:** 0
- **Total:** 24 cited, 24 in bib — perfect match

## Adversarial Review (Paper Critic Agent)

- **Score:** 72/100
- **Verdict:** Minor revisions (calibrated for bachelor's thesis at UET-VNU)

### Dimension Scores

| Dimension | Score |
|-----------|-------|
| Clarity | 8/10 |
| Technical depth | 7/10 |
| Evaluation rigor | 6/10 |
| Novelty | 7/10 |
| Completeness | 7/10 |

### Top Strengths

1. Writing quality and logical flow well above average for bachelor's thesis
2. "Structural primitives / zero PoC contamination" methodology is clearly articulated and internally consistent
3. Threats-to-validity section is unusually honest and thorough

### Top Weaknesses

1. **No baseline comparison** — claim "grammar design is dominant factor" not empirically validated against generic grammar or SQLsmith
2. **No statistical replication** — single runs, no variance/confidence intervals for stochastic fuzzing
3. **CVE-2020-13434 cross-version finding is trivially true** — all 3 versions predate the fix

---

## Issues Found During This Report

| # | Severity | Category | Issue | Status |
|---|----------|----------|-------|--------|
| 1 | **CRITICAL** | Names | Wrong author name "Nguyen Viet Kien" in 3 files, wrong supervisor in 3 files | **FIXED** → Pham Trung Kien, Dr. Le Dinh Thanh |
| 2 | **HIGH** | Factual | v3.3 rule count: c3_method says "51 new rules" but 520-475=45 | **FIXED** → 45 |
| 3 | **HIGH** | Evaluation | No baseline comparison (generic grammar / SQLsmith) | Not fixed — needs experiment |
| 4 | **HIGH** | Evaluation | No statistical replication (repeated runs with variance) | Not fixed — needs experiment |
| 5 | **MEDIUM** | Technical | Weight → probability mapping never computed; reader can't verify bias | Not fixed |
| 6 | **MEDIUM** | Technical | Triage pipeline 80% fidelity threshold algorithm not specified | Not fixed |
| 7 | **MEDIUM** | Technical | Campaign parameters (500ms timeout, 2MB bitmap, 300 nodes) not justified | Not fixed |
| 8 | **MEDIUM** | Completeness | "crash instances" vs "stack hashes" conflated throughout | Not fixed |
| 9 | **MEDIUM** | Completeness | No version × bug-class matrix (which bugs on which versions) | Not fixed |
| 10 | **MEDIUM** | Evaluation | Coverage saturation "99% within 50 min" claimed but curve not shown | Not fixed |
| 11 | **LOW** | Clarity | "cross-pollination" used before defined | Not fixed |
| 12 | **LOW** | Factual | "b AS (b) STORED" may be syntactically invalid SQL | Not fixed |
| 13 | **LOW** | Completeness | JSON/JSONB expansion (v3.3) evaluated but found nothing | Not fixed |
| 14 | **LOW** | LaTeX | 2 overfull hbox >50pt in listings/tables | Not fixed |

---

## Fixes Applied in This Session

1. ✅ Author name: Nguyen Viet Kien → **Pham Trung Kien** (cover.tex, assurance.tex, thesis.tex)
2. ✅ Supervisor name: Dr. Nguyen Duc Anh → **Dr. Le Dinh Thanh** (cover.tex, assurance.tex, acknowledgement.tex)
3. ✅ Rule count: "51 new rules" → **"45 new rules"** (c3_method.tex:580)
4. ✅ TLP bib entry: duplicate of SQLancer → **corrected to TLP/OOPSLA paper** (previous session)
5. ✅ Cross-reference: `tab:cve-reachability` → **`tab:cve-structural`** (previous session)
6. ✅ Table overflows: Table 4.3 155pt → **fixed with \small** (previous session)
7. ✅ Unused bib entries: 5 removed, 2 cited (asan, loadeddice) (previous session)

---

## Recommendation

**Revise before defense.**

Top 3 priorities:
1. **Add one baseline experiment** — even a single 1-hour SQLsmith or generic-grammar Nautilus run on SQLite 3.31.1 would address the biggest gap
2. **Run 3 repeated campaigns** on at least one (grammar, version) pair to report mean ± std for crash count and coverage
3. **Add version × bug-class matrix** — small table, big clarity improvement

These three additions would move the score from 76 to ~85 (minor revisions / near publication-ready for a bachelor's thesis).
