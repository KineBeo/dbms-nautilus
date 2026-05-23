# Zero-Day Hunting Plan — SQLite 3.53.0

**Date:** 2026-05-20
**Status:** In Progress
**Target:** SQLite 3.53.0 (latest stable)

## CVE Pattern Analysis (Contamination-Free)

### CVE-2025-7458 (Integer overflow in KeyInfo)
- **Root cause:** nCols * sizeof(CollSeq*) overflows in sqlite3KeyInfoFromExprList
- **Structural pattern:** SELECT DISTINCT with 65+ result columns + ORDER BY with many terms
- **Grammar encoding:** Wide-Result-Col-List (8/16/32/64 columns), Wide-Order-By
- **NOT contaminated:** no specific literals, just column count explosion

### CVE-2025-3277 (Integer overflow in concat_ws)
- **Root cause:** Sum of argument lengths overflows i64 in concatwsFunc
- **Structural pattern:** concat_ws() with massive argument count, fed by recursive CTE + group_concat
- **Grammar encoding:** concat_ws/concat/string_agg functions + recursive CTE + Cte-Limit non-terminal
- **NOT contaminated:** pattern is "variadic string func + large input generator", not PoC

## New Attack Surface (SQLite 3.44–3.53)

| Function | Added In | Attack Class | Priority |
|----------|----------|-------------|----------|
| parseuri() | 3.53.0 | String parsing, URI edge cases | HIGH |
| unistr() | 3.50.0 | Unicode escape processing | HIGH |
| fpdecode() | 3.53.0 | Float decode, numeric bounds | HIGH |
| median() | 3.46.0 | New aggregate, sorting paths | MEDIUM |
| percentile*() | 3.46.0 | New aggregate, allocation | MEDIUM |
| concat/concat_ws | 3.44.0 | Variadic, size overflow | HIGH |
| string_agg | 3.44.0 | Aggregate alias | MEDIUM |
| unhex() | 3.41.0 | Hex decode, validation | MEDIUM |
| Math functions | 3.45.0 | Numerical edge cases (NaN, Inf) | LOW-MEDIUM |
| octet_length() | 3.47.0 | Byte-length vs char-length | LOW |

## Campaign Plan

### Campaign 1 (30 min, running)
- Grammar: v4.0 (full attack surface)
- Target: sqlite-3.53.0
- Goal: Baseline, discover which code paths are reachable

### Campaign 2 (planned, 60 min)
- Grammar: v4.0a (refined based on Campaign 1 coverage/crashes)
- Target: sqlite-3.53.0
- Goal: Focus on highest-yield attack surfaces

### Campaign 3 (if time permits, 2h)
- Grammar: v4.0b (further refined)
- Target: sqlite-3.53.0
- Goal: Deep exploration of promising crash classes

## Grammar Version

- v4.0: 840+ rules from v3.4 base + ~120 new rules for new attack surface
- Key additions: Wide-Result-Col-List, Wide-Order-By, Variadic-Func-Call,
  New-Agg-Func, Math-Func-Chain, Cte-Limit, parseuri/unistr/fpdecode
