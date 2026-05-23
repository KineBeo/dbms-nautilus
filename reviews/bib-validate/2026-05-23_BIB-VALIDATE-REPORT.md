# Bibliography Validation Report

**Document:** docs/thesis/v2
**Date:** 2026-05-23
**Bibliography:** references.bib (29 entries)
**Citation commands:** 28 unique keys cited across 6 .tex files

## Summary

| Check | Critical | Warning | Info |
|-------|----------|---------|------|
| Missing entries (cited but not in .bib) | 0 | — | — |
| Unused entries (in .bib but not cited) | — | 1 | — |
| Possible typos | 0 | — | — |
| Missing required fields | — | 0 | — |
| Year issues | — | 0 | 0 |
| Author formatting | — | 0 | — |
| Preprint staleness | — | 0 | — |
| **Total** | **0** | **1** | **0** |

## Quality Score

| Metric | Value |
|--------|-------|
| **Score** | 98 / 100 |
| **Verdict** | Ship |

### Deductions

| # | Issue | Tier | Deduction | Category |
|---|-------|------|-----------|----------|
| 1 | Unused entry `loadeddice` | Minor | -2 | Unused entries |
| | **Total deductions** | | **-2** | |

---

## Cross-Reference Results

### Critical: Missing Entries
**None.** All 28 cited keys have corresponding .bib entries.

### Warning: Unused Entries

**W1: `loadeddice` (Vose 1991)**
- Entry defined at references.bib:105 but never cited in any .tex file
- This is the weighted sampling algorithm used by the grammar engine
- **Fix:** Either cite it in Ch3 Section 3.2 (Grammar Engine) where "weighted random selection" is discussed, or remove the entry

### Possible Typos
**None.** All keys match exactly.

---

## Quality Checks

### Entry Type Coverage

| Type | Count | Entries |
|------|-------|---------|
| `@inproceedings` | 11 | nautilus, squirrel, sqlright, griffin, sqlancer, asan, csmith, langfuzz, skyfire, norec, ifuzzer |
| `@misc` | 13 | afl, libfuzzer, sqlsmith, sqlite, dbms-wiki, dbengines, sql-standard, cve201919646, cve202013434, cve20209327, cve20209327ticket, cve202013435, cve202013871, cve202015358 |
| `@article` | 3 | loadeddice, fuzzingsurvey, tlp |
| `@book` | 1 | hopcroft |

### Required Fields Check

All entries have required fields for their type:
- All `@inproceedings`: author, title, booktitle, year — present
- All `@misc`: author, title, year — present (howpublished also present)
- All `@article`: author, title, journal, year — present
- `@book`: author, title, publisher, year — present

### Author Formatting
- No "et al." or "and others" in any author field
- Organization names properly braced: `{MITRE}`, `{Wikipedia}`, `{DB-Engines}`, `{ISO/IEC}`, `{LLVM Project}`

### Year Reasonableness
- Range: 1991 (loadeddice) to 2024 (dbms-wiki, dbengines)
- All years reasonable, no future dates

### Preprint Staleness
- No arxiv.org URLs found
- No `@techreport` or `@unpublished` entries
- No "Working Paper" or "mimeo" notes
- All conference/journal papers have proper venue citations

### Wikipedia Citation Note
- `dbms-wiki` cites Wikipedia for the basic DBMS definition. This is a minor quality concern (Wikipedia is not a peer-reviewed source) but acceptable for a non-controversial foundational definition. The proofread report already flagged this.

---

## Recommendations

1. **Decide on `loadeddice`:** Either add `\citep{loadeddice}` in Ch3 where the Vose alias method / loaded dice algorithm is used for weighted sampling, or remove the entry from references.bib.
2. **Consider replacing `dbms-wiki`** with a textbook citation (e.g., Ramakrishnan & Gehrke) for stronger academic rigor. Optional — the current usage is defensible.
