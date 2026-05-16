# Chapter 4: Experiments and Evaluation — Design Spec

**Date:** 2026-05-16
**Branch:** chapter-4-writing
**Status:** Approved for implementation

## Overview

Rewrite Chapter 4 of the thesis to satisfy the UET school template requirements for a research thesis:

1. Research questions
2. Data and experimental setup
3. Comparison methods (baseline)
4. Evaluation metrics
5. Experimental results
6. Analysis and discussion

The primary change: add a formal comparison between the structural-primitives grammar (v3.4) and a standard EBNF SQL grammar baseline, folded into the existing RQ1/RQ2 structure. A new grammar version v3.4 adds low-weight (1%) CVE seed rules to v3.3 to reliably pass RQ1 (CVE rediscovery).

## Prerequisites (Campaign Inputs)

All prerequisites must be completed before writing begins.

### P1: Grammar v3.4 — CVE Seed Rules

Create `grammars/sqlite_patterns_v3.4.py` (or modify `sqlite_patterns.py`) based on v3.3 (520 rules).

Add 6 CVE seed production rules, each with weight = 1% of the `Sql-Stmt` non-terminal's total weight:

| CVE | Seed Pattern | SQLite Function | Notes |
|-----|-------------|-----------------|-------|
| CVE-2019-19646 | `SELECT * FROM t1 NOT INDEXED WHERE ...` | `flattenSubquery` | Infinite loop — oracle can't detect, but grammar should express it |
| CVE-2020-13434 | `SELECT printf('%.*g', 2147483647, ...)` | `sqlite3_str_vappendf` | Already found by v3.3 compositionally; seed guarantees it |
| CVE-2020-9327 | Schema with self-ref generated col + coalesce + JOIN | `sqlite3Select` | Requires 4 simultaneous elements |
| CVE-2020-13435 | NATURAL JOIN + coalesce + OVER() + UNIQUE + IN subquery | `isAuxiliaryVtabOperator` | Requires 5 simultaneous elements |
| CVE-2020-13871 | Window function + complex subquery | `sqlite3WindowUnlinkFromSelect` | Already found; seed guarantees |
| CVE-2020-15358 | INTERSECT inside scalar subquery context | `sqlite3VdbeMemNumerify` | Specific nesting pattern |

Each seed is a single production rule under `Sql-Stmt` (or a dedicated `CVE-Seed-Stmt` non-terminal) with weight configured so selection probability is ~1%.

Expected grammar size: ~526 rules.

### P2: New Campaigns — v3.4

| Grammar | SQLite Version | Runs | Duration | Total Time |
|---------|---------------|------|----------|------------|
| v3.4 | sqlite-3.30.1 | 5 | 15 min | 75 min |
| v3.4 | sqlite-3.31.1 | 5 | 15 min | 75 min |
| v3.4 | sqlite-3.32.0 | 5 | 15 min | 75 min |
| v3.4 | sqlite-3.32.2 | 5 | 15 min | 75 min |

**Subtotal: 20 campaigns, 300 min compute**

### P3: EBNF Baseline Campaigns (Missing Versions)

Existing EBNF data: sqlite-3.31.1 (5 runs) and sqlite-3.32.2 (5 runs).

| Grammar | SQLite Version | Runs | Duration | Total Time |
|---------|---------------|------|----------|------------|
| EBNF | sqlite-3.30.1 | 5 | 15 min | 75 min |
| EBNF | sqlite-3.32.0 | 5 | 15 min | 75 min |

**Subtotal: 10 campaigns, 150 min compute**

### P4: Triage

Run triage pipeline on all 30 new campaigns:
```bash
python3 scripts/collect_crashes.py --incremental
```

### P5: Comparison Charts

Generate from the combined 40-campaign dataset (20 v3.4 + 20 EBNF):
- Coverage growth over time (line chart, v3.4 vs EBNF, per version)
- Unique root causes bar chart (v3.4 vs EBNF, per version)
- Throughput comparison bar (execs/sec, v3.4 vs EBNF)
- Bug class breakdown by grammar (stacked or grouped bar)

### P6: Statistical Tests

Run Mann-Whitney U test with Cliff's d effect size for each metric × version:
- Total crashes
- Unique root causes
- Edge coverage (queue size)
- Throughput (execs/sec)

**Total campaign compute: 30 campaigns × 15 min = 7.5 hours sequential**
Can parallelize: run all 4 versions simultaneously = ~75 min wall clock.

---

## Chapter 4 Outline

### 4.1 Experimental Setup

**Status: EXISTS — needs updates**

#### 4.1.1 Environment
Hardware, compiler (Clang 14), ASan+UBSan instrumentation, sanitizer behavior.
No changes needed.

#### 4.1.2 Campaign Parameters (Table 4.1)
Update table to include v3.4 grammar row. Update duration range if needed.
Add: "Grammar versions: v3.0, v3.1, v3.2, v3.3, v3.4 (449–526 rules)"

#### 4.1.3 Target Versions and CVEs
No changes needed. Same 4 versions, 6 CVEs.

#### 4.1.4 Grammar Versions
**UPDATE:** Add v3.4 description paragraph:
- v3.4 adds 6 CVE seed rules (~1% weight each) to v3.3's 520 rules
- Seed rules encode minimal structural patterns from CVE PoCs
- Purpose: ensure grammar can express all 6 CVE-triggering patterns with guaranteed probability
- Distinction from hardcoding: seeds are production rules composed by the grammar engine, not literal SQL strings

#### 4.1.5 Baseline: EBNF Grammar
**NEW subsection.** Describe:
- Standard EBNF SQL grammar derived from SQLite's public grammar specification
- File: `grammars/baseline/sqlite-ebnf.py` (campaigns reference it as `grammars/ebnf/sqlite_v3.py` — same grammar, path alias)
- No domain-specific structural primitives, no CVE-motivated rules, no weight tuning
- Represents the "grammar-based fuzzing without domain knowledge" baseline
- Same campaign parameters (15 min, same harness, same bitmap size)

#### 4.1.6 Evaluation Metrics
No changes needed. Same 4 metrics: unique root causes, edge coverage, total crashes, CVE signature match.

### 4.2 RQ1: Can DBMS-Nautilus Rediscover Known CVEs?

#### 4.2.1 Methodology
**Minor update:** Mention v3.4 grammar with seed rules used for final evaluation.

#### 4.2.2 Results (Table 4.2: CVE Rediscovery)
**UPDATE table** with v3.4 results. Expected: 5/6 rediscovered (all except CVE-2019-19646 which is infinite loop, oracle-invisible). Or possibly 5/6 if all seed-covered CVEs trigger.

Update "First Grammar" column to show v3.4 for seed-enabled CVEs.

#### 4.2.3 Reachability Matrix (Table 4.3)
**ADD v3.4 column.** All 6 CVEs reachable (same as v3.2+), but v3.4 also has seed rules guaranteeing higher trigger probability.

#### 4.2.4 Case Studies
**EXISTS.** Keep BC003, BC010, BC002 case studies. If new CVEs found via seeds (e.g., CVE-2020-13435 or CVE-2020-15358), add case studies for those.

#### 4.2.5 Analysis of Unfound CVEs
**UPDATE.** With v3.4 seeds, fewer unfound CVEs. CVE-2019-19646 remains unfound (oracle limitation). Discuss whether other previously-unfound CVEs now trigger.

#### 4.2.6 Comparison: v3.4 vs EBNF on CVE Rediscovery
**NEW subsection.**
- Table: CVE rediscovery counts (v3.4 vs EBNF, per version)
- EBNF expected to find 0-1 CVEs (only BC003/int overflow if lucky)
- v3.4 expected to find 5/6
- Analysis: structural primitives + seed rules = dramatically higher CVE hit rate

#### 4.2.7 Key Finding
**UPDATE** to incorporate comparison result.

### 4.3 RQ2: Can DBMS-Nautilus Discover New Bugs?

#### 4.3.1 Methodology
**Minor update:** Mention v3.4 campaigns and EBNF baseline.

#### 4.3.2 Results (Table 4.4: All Bug Classes)
**UPDATE** with v3.4 campaign data. May discover same 10 bug classes or additional ones.

#### 4.3.3 Case Studies
**EXISTS.** Keep all existing case studies (BC001-BC009).

#### 4.3.4 Verification on Modern SQLite
**EXISTS.** No changes unless re-running on 3.53.0 with v3.4.

#### 4.3.5 Comparison: v3.4 vs EBNF on Bug Discovery
**NEW subsection.** This is the main new content for RQ2.

Contents:
- **Unique root causes comparison table** (per version, v3.4 vs EBNF, with mean±std)
- **Figure 4.1: Coverage growth over time** — line chart showing edge coverage for v3.4 and EBNF over 15-minute campaign, averaged across runs with confidence bands. One panel per SQLite version or combined.
- **Figure 4.2: Unique root causes bar chart** — grouped bar chart, v3.4 vs EBNF, per version
- **Figure 4.3: Throughput comparison** — bar chart of execs/sec
- **Table 4.5: Statistical significance** — Mann-Whitney U test results:

```
| Metric | Version | v3.4 (mean±std) | EBNF (mean±std) | U | p | Cliff's d | Effect |
```

For each of: total crashes, unique root causes, edge coverage, throughput.

- **Discussion:** Interpret what the numbers mean. v3.4 likely finds more unique bugs but EBNF may have higher throughput (simpler grammar = faster generation). Coverage patterns may differ (v3.4 targets deeper paths, EBNF covers broader surface).

#### 4.3.6 Key Finding
**UPDATE** with comparison-informed conclusion.

### 4.4 Analysis and Discussion

**NEW section.** Cross-cutting analysis.

#### 4.4.1 Grammar Design as Primary Bottleneck
Synthesize RQ1 + RQ2 evidence: grammar structural coverage determines what bugs are reachable. v3.0→v3.4 evolution proves this.

#### 4.4.2 Effectiveness of CVE Seed Rules
Discuss advisor's strategy: low-weight seeds guarantee CVE rediscovery without dominating generation. Analyze whether seeds affected non-CVE bug discovery (cross-pollination or interference).

#### 4.4.3 Cross-Pollination Evidence
Bugs found beyond CVE targets (RQ2) demonstrate that structural primitives designed for specific CVEs also exercise adjacent code paths. Quantify: X bug classes found with 0 dedicated grammar rules.

#### 4.4.4 Comparison Summary
Synthesize v3.4 vs EBNF findings across all metrics. Key claim: domain-knowledge-driven grammar engineering produces significantly more bugs than generic grammar-based fuzzing.

### 4.5 Threats to Validity

**EXISTS — minor update.** Add:
- Seed rule bias: CVE seeds may inflate RQ1 results; mitigated by low weight (1%) and RQ2 showing non-seed bugs
- Single baseline: only EBNF compared; other tools (SQLsmith, Squirrel) not directly tested

---

## Figures Inventory

| Figure ID | Title | Type | Source Data | Status |
|-----------|-------|------|-------------|--------|
| Fig 4.1 | Coverage growth: v3.4 vs EBNF over time | Line chart with CI bands | timeseries.csv | Generate from new campaigns |
| Fig 4.2 | Unique root causes by grammar and version | Grouped bar chart | campaigns_summary.csv | Generate from new campaigns |
| Fig 4.3 | Throughput comparison | Bar chart | campaigns_summary.csv | Generate from new campaigns |
| Fig 4.4 | Bug class breakdown by grammar | Grouped/stacked bar | bug_classes.csv | Generate from new campaigns |

All figures: PDF output for `\includegraphics` in LaTeX.

## Tables Inventory

| Table ID | Title | Status |
|----------|-------|--------|
| Tab 4.1 | Campaign parameters | UPDATE (add v3.4) |
| Tab 4.2 | CVE rediscovery results | UPDATE (v3.4 data) |
| Tab 4.3 | Grammar evolution and CVE reachability | UPDATE (add v3.4 column) |
| Tab 4.4 | All bug classes discovered | UPDATE (v3.4 data) |
| Tab 4.5 | Statistical comparison: v3.4 vs EBNF | NEW |

## Implementation Order

1. **Grammar engineering:** Create v3.4 with CVE seed rules
2. **Campaigns:** Run 30 campaigns (20 v3.4 + 10 EBNF missing versions)
3. **Triage:** Process all crash data
4. **Charts:** Generate 4 comparison figures
5. **Statistical tests:** Run Mann-Whitney U on all metrics
6. **Writing:** Update existing sections + write new sections
7. **Figure integration:** `\includegraphics` for all 4 new figures
8. **PDF build:** Compile thesis and verify

## Non-Goals

- No new SQLite versions beyond the 4 targets
- No 30-minute campaigns (15m is primary; 30m data mentioned as supplementary)
- No comparison with SQLsmith/Squirrel (conceptual comparison only in related work)
- No RL/bandit integration (deferred per Phase 3 decision)
- No grammar semantic awareness improvements
