# Proofread Report

**Document:** docs/thesis/v2 (all chapters)
**Date:** 2026-05-13
**Pages:** ~54

## Summary

| Category | Critical | Major | Minor |
|----------|----------|-------|-------|
| Grammar & spelling | 0 | 0 | 1 |
| Notation consistency | 0 | 0 | 0 |
| Citation format | 0 | 1 | 0 |
| Academic tone | 0 | 0 | 0 |
| LaTeX-specific | 1 | 2 | 1 |
| Citation voice balance | 0 | 0 | 0 |
| TikZ diagrams | 0 | 0 | 0 |
| Numeric cross-check | 0 | 1 | 0 |
| Causal language | 0 | 0 | 0 |
| Equation completeness | 0 | 0 | 0 |
| Preprint staleness | 0 | 0 | 0 |
| **Total** | **1** | **4** | **2** |

## Critical Issues

### C1: Duplicate bibliography entry — `sqlancer` and `tlp` are identical

- **File:** `references.bib`
- **Lines:** 110–118 (`sqlancer`) and 263–270 (`tlp`)
- **Problem:** Both entries have identical title ("Testing Database Engines via Pivoted Query Synthesis"), authors (Rigger, Su), venue (OSDI 2020), and pages (667–682). The `tlp` key is cited in `c2_background.tex` but refers to TLP (Ternary Logic Partitioning), which is a **different** paper from SQLancer (Pivoted Query Synthesis). The metadata for `tlp` is wrong — it should reference the correct TLP paper.
- **Fix:** Replace `tlp` bib entry with the correct paper:
  ```bibtex
  @inproceedings{tlp,
      author = {Rigger, Manuel and Su, Zhendong},
      title = {Finding Bugs in Database Systems via Query Partitioning},
      booktitle = {Proceedings of the ACM on Programming Languages (OOPSLA)},
      year = {2020},
      volume = {4},
      pages = {1--30},
      publisher = {ACM},
  }
  ```

## Major Issues

### M1: All citations use `\cite{}` instead of `\citet{}`/`\citep{}`

- **Category:** Citation format
- **Locations:** All 52 citations across c1_introduction.tex (9), c2_background.tex (23), c3_method.tex (13), c4_experiments.tex (7)
- **Problem:** The thesis loads `natbib` package (line 24 of thesis.tex) which provides `\citet` (textual: "Author (Year)") and `\citep` (parenthetical: "(Author, Year)"). All citations use raw `\cite{}` instead, which with `unsrt` bibliography style produces numeric references `[N]`. With numeric styles, `\cite` is acceptable — but since `natbib` is loaded, consistent use of `\citep` for numeric-parenthetical is preferred for cleanliness. **If numeric `[N]` style is intentional, this is Minor rather than Major.** Flag for author decision.
- **Fix:** If switching to author-year style: replace `\cite{}` with `\citet{}` (textual) or `\citep{}` (parenthetical) as appropriate. If keeping numeric `[N]` style: no change needed, downgrade to Minor.

### M2: Overfull hbox >50pt in tables (2 instances)

- **Category:** LaTeX-specific
- **Locations:**
  - `c2_background.tex:164–176` (Table 2.1, related work comparison) — 27.6pt overflow
  - `c4_experiments.tex:155–173` (Table 4.3, all bugs) — 155.1pt overflow, very severe
  - `c3_method.tex:500–511` (Table 3.2, grammar evolution) — 50.1pt overflow
- **Problem:** Tables extend beyond the text margin. The 155pt overflow on Table 4.3 is likely to produce visually broken output, with text extending into or past the right margin.
- **Fix:** For Table 4.3 (`tab:all-bugs`), either: (a) reduce font size with `\small` or `\footnotesize` inside the table, (b) use `tabularx` with `X` columns, or (c) abbreviate column headers. For the others, `\small` inside the table environment usually suffices.

### M3: Forward cross-reference to wrong table in Chapter 3

- **Category:** Numeric cross-check
- **File:** `c3_method.tex:563`
- **Problem:** Text says "as documented in Table~\ref{tab:cve-reachability}" but `tab:cve-reachability` is defined in Chapter 4 (`c4_experiments.tex:81`). The text should reference `tab:cve-structural` (defined in `c3_method.tex:335`), which is the table in the same chapter that maps CVEs to structural patterns.
- **Fix:** Change `Table~\ref{tab:cve-reachability}` to `Table~\ref{tab:cve-structural}` at line 563 of c3_method.tex.

### M4: Overfull hbox in listings/code blocks (4 instances)

- **Category:** LaTeX-specific
- **Locations:**
  - `c2_background.tex:105–116` — 119.5pt overflow (Listing in Related Work section)
  - `c3_method.tex:237–238` — 46.1pt overflow (TikZ figure caption area)
  - `c4_experiments.tex:114–115` — 51.8pt overflow (case study text)
  - `c3_method.tex:566–567, 569–570, 572–573` — 4.5–13pt overflow (grammar evolution text)
- **Problem:** Long lines in code listings and dense technical prose exceed column width.
- **Fix:** For listings, set `breaklines=true` (already set globally but may be overridden). For prose, minor rewording of long sentences or adding `\allowbreak` hints.

## Minor Issues

### m1: Abstract uses Vietnamese (`abstract_vi.tex`)

- **Category:** Grammar & spelling
- **File:** `chapters/abstract_vi.tex`
- **Problem:** The thesis includes a Vietnamese abstract ("Tóm tắt"), but the checkpoint notes say "All English, single cover page, no Vietnamese content." If this file is intentionally included per UET template requirements, it's fine. If not, it should be removed from thesis.tex.
- **Fix:** Verify with advisor whether Vietnamese abstract is required by UET template. If not, remove `\input{chapters/abstract_vi}` from thesis.tex.

### m2: 7 unused bibliography entries

- **Category:** LaTeX-specific
- **File:** `references.bib`
- **Problem:** 7 bib entries defined but never cited: `asan`, `dynsql`, `ecofuzz`, `grimoire`, `loadeddice`, `mopt`, `superion`. With `unsrt` style these won't appear in the output, so no visual issue, but they add noise to the source.
- **Fix:** Either cite them where relevant (e.g., `asan` could be cited in Ch4 setup description, `loadeddice` in Ch3 grammar engine description) or remove unused entries.

## Quality Score

| Metric | Value |
|--------|-------|
| **Score** | 85 / 100 |
| **Verdict** | Ship with notes |

### Deductions

| # | Issue | Tier | Deduction | Category |
|---|-------|------|-----------|----------|
| C1 | Duplicate bib entry (sqlancer/tlp) | Critical | -8 | Citation format |
| M2 | Overfull hbox >50pt in tables | Major | -3 | LaTeX-specific |
| M3 | Wrong table cross-reference in Ch3 | Major | -2 | Numeric cross-check |
| M4 | Overfull hbox in code/prose | Major | -1 | LaTeX-specific |
| m2 | 7 unused bib entries | Minor | -1 | LaTeX-specific |
| | **Total deductions** | | **-15** | |

## Recommendations

1. **Fix C1 immediately** — the duplicate `tlp`/`sqlancer` bib entry means the TLP citation in the text references the wrong paper. This is the only issue a reviewer would catch instantly.

2. **Fix M3** — wrong table reference is a one-line fix (`tab:cve-reachability` → `tab:cve-structural` in c3_method.tex:563).

3. **Fix M2** — Table 4.3's 155pt overflow is likely visually broken in the PDF. Adding `\small` or `\footnotesize` inside the table environment is a 1-line fix.

4. **Consider citing unused bib entries** — `asan` (cited in text as "AddressSanitizer" but not `\cite{asan}`), `loadeddice` (the weighted sampling algorithm used by grammartec), and `dynsql` (a recent DBMS fuzzer that would strengthen Related Work).

5. **Overall writing quality is strong.** No contractions, no casual hedging, consistent academic tone, correct tense usage, well-structured arguments. The cross-pollination narrative is clear and well-supported.

6. **Consider `/bib-validate`** for a thorough cross-check of all citation keys and metadata accuracy.
