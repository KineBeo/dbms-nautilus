# Thesis v2 Outline Design

**Date:** 2026-05-12
**Status:** Approved
**Scope:** Full thesis chapter-by-chapter outline with depth, figures, and writing guidance per section

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Ch3 structure | 3 sections (overview + grammar design + grammar evolution) | Template requires "proposed method" — harness/oracle/triage are implementation, not method |
| Implementation details | Drop from Ch3 entirely | Brief mentions in 3.1 overview and 4.1 setup only |
| Triage pipeline | Inline in Ch4 methodology | Development-phase tool, not proposed method |
| Related work | Ch2 section 2.4 | Template lists "related research" as Ch2 content |
| Research questions | 2 RQs | RQ1: CVE rediscovery, RQ2: new bugs. Focused for undergrad thesis |
| Figures | 10 total (heavy) | Architecture done, 9 new needed |
| Page target | 40-50 pages | Current estimate ~38, expand Ch3.2 and Ch4 case studies to reach 40 |
| Ch3.2 key narrative | Cross-pollination | Grammar encodes CVE patterns without labeling which serves which CVE. Composition is genuine discovery. |

## Chapter 1: Introduction (DONE)

- **Pages:** 2
- **Figures:** 0 | **Tables:** 0
- **Status:** Complete. No changes needed.
- **Content:** Problem statement (byte-level fuzzers fail on structured input), contributions (3 bullets: grammar design methodology, CVE rediscovery, new bug discovery), thesis organization.

## Chapter 2: Background (~7 pages)

### 2.1 DBMS (DONE, ~1 page)
- What is a DBMS, SQL language, SQLite as target
- No figures, no tables

### 2.2 Context-Free Grammars (DONE text, ~2.5 pages)
- Formal definition (N, T, R, S tuple)
- Derivation steps, derivation trees
- SQL as a context-free language
- **NEW Fig 2.1:** Derivation tree example showing a SQL SELECT statement derived from grammar rules. Similar to Nautilus Example II.1 but with SQL non-terminals (Sql-Stmt → Schema-Setup ";" Stress-Query → ...).
- **Writing note:** This is the theoretical foundation for Ch3. Reader must understand derivation trees before seeing grammar design.

### 2.3 Fuzzing (DONE text, ~1.5 pages)
- Mutation-based vs generation-based
- Blackbox / greybox / whitebox classification
- Coverage-guided feedback loop
- **NEW Fig 2.2:** Fuzzing taxonomy diagram. 2x3 grid or tree: (mutation/generation) x (black/grey/white). Position Nautilus and DBMS-Nautilus as generation + greybox.
- **Writing note:** Keep concise. Reader needs enough to understand Ch3 overview but not a fuzzing survey.

### 2.4 Related Work (NEW, ~2 pages)
- **Mutation-based fuzzers:** AFL — coverage-guided byte mutation, struggles with structured input
- **Grammar-based fuzzers:** CSmith (C programs, no feedback), LangFuzz/IFuzzer (JavaScript, corpus-dependent), Skyfire (corpus-derived probabilistic grammar)
- **DBMS-specific fuzzers:** SQLsmith (schema introspection, random SQL, no feedback), Squirrel (IR-based mutation with semantic awareness), NoREC/TLP (differential/metamorphic testing — different goal)
- **Nautilus:** Grammar + coverage feedback, general-purpose. DBMS-Nautilus extends with domain-specific SQL grammar and weighted sampling.
- **NEW Fig 2.3 / Table:** Feature comparison matrix. Columns: Grammar, Feedback, Corpus-free, Bypasses parsing, Domain-specific. Rows: AFL, CSmith, SQLsmith, Squirrel, Nautilus, DBMS-Nautilus.
- **Writing note:** Position, don't survey. Each tool gets 2-3 sentences. End with: "DBMS-Nautilus combines Nautilus's grammar+feedback architecture with a domain-specific SQL grammar engineered for vulnerability-triggering patterns."

## Chapter 3: Proposed Method (~10 pages)

Chapter intro paragraph: bridge from Ch2 (grammar fuzzers treat all constructs equally) to our proposal (domain-specific grammar with cross-pollinating structural patterns). State 3-section roadmap.

### 3.1 System Overview (DONE, ~2 pages)
- What DBMS-Nautilus is, how it differs from SQLsmith/Squirrel
- Architecture diagram (Fig 3.1, DONE)
- One paragraph per component: Grammar Engine, Generation+Mutation, Fork Server+Harness, Coverage Feedback, Triage Pipeline
- Self-contained test cases design decision
- Component summary table (Table 3.1, DONE)
- **No code listings, no implementation details**

### 3.2 Grammar Design (~6 pages) — CORE CONTRIBUTION

**Narrative arc:**

1. **Structural Primitives Philosophy** (~1 page)
   - Zero PoC contamination principle
   - Three constraints: (a) no complete PoC as fixed string, (b) every structural pattern needed for target CVEs exists as composable non-terminal, (c) sufficient compositional freedom for novel combinations
   - Tension between (b) and (c) — the design challenge

2. **Cross-Pollination** (~1.5 pages) — KEY DIFFERENTIATOR
   - Grammar contains structural patterns extracted from CVE root-cause analysis
   - Patterns are NOT labeled or isolated per CVE
   - Schema-Setup has generated columns (needed for CVE-2020-9327 AND CVE-2019-19646, but also general coverage)
   - Stress-Query has NATURAL JOIN (needed for CVE-2020-13435, but exercises query planner generally)
   - Boundary-Func-Call has printf with boundary integers (needed for CVE-2020-13434, but also tests other functions)
   - The power: fuzzer freely combines patterns across Layer 2 shapes → discovers compositions the grammar designer didn't plan
   - Example walkthrough: Schema-Setup(generated columns) + Stress-Query(NATURAL JOIN) + Boundary-Func-Call(printf) = novel combination no single CVE analysis would produce
   - This means: any CVE rediscovery is genuine compositional achievement, not replay

3. **Two-Layer Architecture** (~1 page)
   - Layer 1: SQL Atoms — 30+ expression types, clauses, functions, literals
   - Layer 2: Composed Shapes — Schema-Setup, Stress-Query, Validation-Op, Boundary-Func-Call
   - How layers compose: Sql-Stmt → Schema-Setup ";" Stress-Query (optionally + Validation-Op)
   - **NEW Fig 3.2:** Two-layer architecture diagram. Show Layer 1 atoms feeding into Layer 2 shapes, which compose into Sql-Stmt. Visual representation of the composability.

4. **Code Listings** (~1.5 pages)
   - Listing: Schema-Setup alternatives with weights (6 variants, already written)
   - Listing: Stress-Query alternatives (representative 4, already written)
   - Listing: Boundary-Func-Call alternatives (already written)
   - Each listing: explain what patterns it encodes and WHY those weights
   - **Writing note:** Don't describe each rule mechanically. Focus on: "S2 (generated columns) gets weight 3.0 because generated columns are involved in 2/6 target CVEs — but the fuzzer doesn't know this, it just samples more frequently."

5. **CVE Reachability Analysis** (~0.5 page)
   - **NEW Fig 3.3:** CVE reachability matrix. Rows = structural patterns (generated columns, NATURAL JOIN, window functions, printf+boundary, compound queries, etc.). Columns = 6 target CVEs. Cells = checkmark if pattern is needed. Shows: each CVE requires 2-5 patterns, patterns are shared across CVEs (cross-pollination visible).
   - Table: CVE structural requirements (already written, may merge with figure)

6. **Pros/Cons Analysis** (~0.5 page) — template requires this
   - Pros: genuine discovery (no hardcoding), cross-pollination, composable, grammar-version-independent
   - Cons: requires manual domain expertise for grammar design, weight sensitivity (wrong weights → FTS saturation problem), grammar can only reach bugs whose structural prerequisites exist as non-terminals

### 3.3 Grammar Evolution (~2 pages)

Evidence-driven iterative refinement. Each version addresses a specific deficiency found through experimentation.

1. **v3.0 → v3.1: Weight Rebalancing** — FTS saturation problem. 92% crashes = FTS. Fix: S5 weight 2.0→0.5. Result: crash diversity improved.
2. **v3.1 → v3.2: Structural Expansion** — Gap analysis: 4/6 CVEs structurally unreachable. Added window functions, self-ref generated columns, count() zero-arg. Result: CVE reachability 2/6 → 6/6.
3. **v3.2 → v3.3: JSON/JSONB Expansion** — Extending reach to modern SQLite. 51 new rules for json.c module.
4. **Key Insight: Two Axes** — Weight tuning (probability distribution) vs structural expansion (input space boundaries). Both necessary.

- **NEW Fig 3.4:** Grammar evolution visualization. Either timeline showing rule count + key changes per version, or before/after CVE reachability (v3.0: 2/6, v3.2: 6/6).
- **Table:** Grammar version history (already written)

## Chapter 4: Experiments and Evaluation (~8 pages)

Chapter intro: state the two RQs.

### 4.1 Experimental Setup (~1.5 pages)
- **Research Questions:**
  - RQ1: Can DBMS-Nautilus rediscover known CVEs in vulnerable SQLite versions?
  - RQ2: Can DBMS-Nautilus discover previously unknown bugs?
- **Target versions:** 4 SQLite versions (3.30.1, 3.31.1, 3.32.0, 3.32.2) with 6 confirmed CVEs
- **Campaign parameters:** duration, seeds, grammar version used
- **Hardware:** machine specs
- **Evaluation metrics:** CVE match count, unique crash count (by stack hash), bug class count
- Brief note on harness: "SQLite compiled with ASan+UBSan instrumentation. Crashes classified by exit code: ASan violations (exit 223), UBSan violations (exit 1), debug assertions (SIGTRAP)."
- Brief note on triage: "Crashes deduplicated by top-5 stack frame hash, matched against structural CVE signatures."
- **Table 4.1:** Experimental configuration summary
- **No figures**

### 4.2 RQ1: CVE Rediscovery (~3 pages)
- **Methodology:** Run campaigns on each vulnerable version. Match crashes against CVE signatures.
- **Results:** Which CVEs found, which not, how many campaigns needed
- **Case studies (2-3):** Pick most interesting CVE rediscoveries. Show the trigger SQL. Explain what DBMS-Nautilus composed. Demonstrate cross-pollination in action.
- **Unfound CVEs analysis:** Why certain CVEs weren't found (structural gap? insufficient campaign time? weight distribution?)
- **NEW Fig 4.1:** CVE rediscovery results (table-figure: version × CVE × found/not-found, or bar chart)
- **Table 4.2:** CVE rediscovery detailed results

### 4.3 RQ2: New Bug Discovery (~2.5 pages)
- **Methodology:** Analyze crashes that don't match any CVE signature
- **Results:** 10 bug classes, 89 unique hashes across 4 versions
- **Case studies (2-3):** Most interesting new bugs. Show trigger SQL, ASan/UBSan output, what went wrong in SQLite.
- **Modern SQLite verification:** Results on SQLite 3.53.0 (if any)
- **NEW Fig 4.2:** Bug class distribution (bar chart: bug type × count, or version × bug class heatmap)
- **Table 4.3:** New bugs summary (10 classes with description and severity)

### 4.4 Threats to Validity (~1 page)
- **Internal:** Campaign duration, seed randomness, grammar version choice
- **External:** Single target DBMS (SQLite), specific CVE versions
- **Construct:** Stack-hash dedup granularity, CVE signature pattern completeness
- No figures, no tables

## Conclusion (~1 page)
- Summary of contributions
- Key results: X/6 CVEs rediscovered, Y new bug classes, Z unique crashes
- Limitations: manual grammar design, SQLite-only, no semantic validity
- Future work: RL-based adaptive weight tuning, automated grammar generation, extension to other DBMS

## Figure Plan (10 total)

| # | Figure | Location | Type | Priority |
|---|--------|----------|------|----------|
| 1 | SQL derivation tree | Ch2.2 | TikZ tree diagram | Medium |
| 2 | Fuzzing taxonomy | Ch2.3 | TikZ grid/tree | Medium |
| 3 | Related work comparison | Ch2.4 | Table (see Table plan #7) | Medium |
| 4 | System architecture | Ch3.1 | TikZ (DONE) | Done |
| 5 | Two-layer grammar arch | Ch3.2 | TikZ layer diagram | High |
| 6 | CVE reachability matrix | Ch3.2 | TikZ heatmap/grid | High |
| 7 | Grammar evolution | Ch3.3 | TikZ timeline or chart | Medium |
| 8 | CVE rediscovery results | Ch4.2 | Chart or table-figure | High |
| 9 | Bug class distribution | Ch4.3 | Bar chart | High |
| 10 | Coverage/crash curve | Ch4.2 | Line chart (optional) | Low |

## Table Plan (7 total)

| # | Table | Location | Status |
|---|-------|----------|--------|
| 1 | System components | Ch3.1 | Done |
| 2 | CVE structural requirements | Ch3.2 | Done (review needed) |
| 3 | Grammar version history | Ch3.3 | Done (review needed) |
| 4 | Experimental config | Ch4.1 | New |
| 5 | CVE rediscovery results | Ch4.2 | New |
| 6 | New bugs summary | Ch4.3 | New |
| 7 | Related work comparison | Ch2.4 | New |

## Page Budget

| Chapter | Pages |
|---------|-------|
| Front matter (cover, abstract, TOC, glossary) | ~5 |
| Ch1 Introduction | 2 |
| Ch2 Background + Related Work | 7 |
| Ch3 Proposed Method | 10 |
| Ch4 Experiments | 8 |
| Conclusion | 1 |
| References | 2 |
| **Total** | **~35-38** |

To reach 40: expand Ch3.2 cross-pollination analysis (+1 page) and Ch4 case studies (+1-2 pages).

## Writing Order

1. Ch3.2 Grammar Design (core contribution, highest priority)
2. Ch3.3 Grammar Evolution
3. Ch2.4 Related Work
4. Ch4 Experiments (rewrite old draft)
5. Conclusion (rewrite old draft)
6. Ch2.2-2.3 figures (add to existing text)
7. Final compilation and consistency check

## Key Principles

- **Ch3 = only proposed method.** No implementation artifacts.
- **Cross-pollination is the narrative center** of 3.2.
- **Every figure must be referenced and explained** (template requirement).
- **No bullet-point writing** (template requirement: "Khong viet KLTN theo dang gach dau dong").
- **All claims reference sources** (template requirement).
- **Pros/cons analysis required** in Ch3 (template requirement).
