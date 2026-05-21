# Proofread Report: Chapter 2 Citation Source Audit

**Document:** docs/thesis/v2/chapters/c2_background.tex
**Date:** 2026-05-21
**Scope:** Ensuring all citations point to appropriate original sources, not secondary references

## Summary

| Category | Critical | Major | Minor |
|----------|----------|-------|-------|
| Citation source appropriateness | 0 | 2 | 0 |
| **Total** | **0** | **2** | **0** |

## Major Issues (all FIXED)

### M1: Section 2.1 cited research papers for textbook-level DBMS facts
- **Problem:** "DBMS is software" cited `fuzzingsurvey`; "relational model" cited `sqlancer`; "SQL is a language" cited `griffin`
- **Fix:** Replaced with proper general sources:
  - `dbms-wiki` (Wikipedia) for DBMS/relational model definitions
  - `sql-standard` (ISO/IEC 9075) for SQL definition
  - `dbengines` (DB-Engines) for "hundreds of DBMSs" claim
  - Kept `sqlancer` only for "each one extends or deviates from the standard" (Rigger's own observation)

### M2: Section 2.3 cited Nautilus paper 6 times for formal language theory
- **Problem:** CFG tuple definition, derivation rules, derivation tree -- all cited `nautilus`. CFGs are from Chomsky (1956)/textbook material, not Nautilus's contribution.
- **Fix:** Replaced with `hopcroft` (Hopcroft, Motwani & Ullman, "Introduction to Automata Theory, Languages, and Computation", 3rd ed., 2006) for all formal CFG definitions. Kept `nautilus` only for:
  - "byte mutations fail for structured input" (their observation)
  - "unparsing" as a term in grammar-based fuzzing (their terminology)
  - Bug count and performance claims (their results)

## New bib entries added

| Key | Source | Purpose |
|-----|--------|---------|
| `hopcroft` | Hopcroft, Motwani & Ullman (2006) | CFG formal definitions |
| `dbms-wiki` | Wikipedia: Database | General DBMS definition |
| `sql-standard` | ISO/IEC 9075:2023 | SQL language standard |
| `dbengines` | DB-Engines Ranking | DBMS product count |

## Final Citation Audit

Every citation in Ch2 now follows the principle: **cite the original source for the fact, not a paper that happens to mention it.**

- Textbook facts (DBMS, relational model, CFG) → textbook/standard references
- Tool-specific facts (SQLsmith generates queries, Squirrel uses IR) → that tool's paper
- Analysis/observations (DBMS fuzzing is hard, SQL dialects diverge) → the paper that makes that argument
- Fuzzing definitions → fuzzing survey
- SQLite facts → SQLite website

Build: 63 pages, 0 errors, 0 undefined citations.
