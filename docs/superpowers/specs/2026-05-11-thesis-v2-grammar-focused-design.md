# Thesis V2 Design Spec: DBMS-Nautilus — Grammar-Based Fuzzing for SQLite Vulnerability Discovery

**Date:** 2026-05-11
**Status:** Approved
**Supersedes:** 2026-05-05-thesis-writing-design.md (bandit/RL version)

## Overview

Rewrite of the thesis focusing exclusively on grammar engineering for DBMS fuzzing. No bandit, no RL. Two research questions drive the evaluation:

- **RQ1**: Can DBMS-Nautilus rediscover existing CVEs through compositional grammar generation (not PoC replay)?
- **RQ2**: Can DBMS-Nautilus discover new bugs/crashes beyond known CVEs?

**System name:** DBMS-Nautilus
**Language:** English body text, Vietnamese cover/front matter per UET template
**Template:** `docs/thesis/template/` (UET KLTN format, 13pt, natbib, tikz)
**Reference PDF:** `docs/thesis/reference/AKALLM1012-1.pdf` (layout/structure reference only)
**Output location:** `docs/thesis/v2/` (separate from old `docs/thesis/content/`)

## Chapter Structure (4 chapters + conclusion)

### Chapter 1 — Introduction (~5 pages)

**Sections:**
1. **Context and Motivation**: SQLite ubiquity (most deployed DB engine), CVE persistence despite mature codebase. Six CVEs filed 2019-2020 across versions 3.30.1-3.32.2. Byte-level fuzzers (AFL, libFuzzer) fail on structured inputs — rejected at parser, never reach deep logic.
2. **Problem Statement**: Existing grammar-based fuzzers (Nautilus, Superion, Grimoire) use uniform random rule selection with no domain knowledge about which SQL constructs trigger vulnerability classes. Can a carefully engineered grammar with structural primitives improve vulnerability discovery?
3. **Research Questions**:
   - RQ1: Can DBMS-Nautilus rediscover existing CVEs in older SQLite versions through compositional grammar generation without embedding proof-of-concept inputs?
   - RQ2: Can DBMS-Nautilus discover previously unreported bugs in SQLite beyond the known CVEs?
4. **Contributions**:
   - Structural primitives grammar methodology (zero PoC contamination, layered decomposition, iterative refinement)
   - Grammar evolution v3.0→v3.3 guided by coverage and crash evidence
   - Empirical demonstration: 3 CVEs rediscovered + 7 new bug classes across 4 SQLite versions
5. **Thesis Organization**: Brief paragraph pointing to each chapter.

### Chapter 2 — Background and Related Work (~10 pages)

**Sections:**
1. **Coverage-Guided Greybox Fuzzing**: AFL architecture, coverage bitmap (2MB shared memory), edge transitions, fork server protocol. How coverage feedback steers input generation.
2. **Grammar-Based Fuzzing**: Context-free grammars for structured input generation. Nautilus: grammar derivation trees, subtree splicing, random regeneration, coverage-guided queue. Superion (grammar-aware AFL for JS/XML). Grimoire (grammar inference without explicit specification).
3. **DBMS Testing Tools**: SQLsmith (random valid SQL, no coverage feedback), Squirrel (coverage-guided SQL with validity constraints), SQLRight (semantic-aware SQL fuzzing), Griffin (statement-level mutation), SQLancer (logic testing, not crash detection). Comparison table positioning DBMS-Nautilus.
4. **Dynamic Analysis Oracles**: AddressSanitizer (buffer overflow, use-after-free, double-free detection via shadow memory), UndefinedBehaviorSanitizer (integer overflow, null pointer, shift violations). How sanitizers serve as bug oracles in fuzzing.
5. **SQLite Architecture**: Relevant internals — tokenizer/parser, query planner/optimizer, VDBE bytecode engine, window function engine, FTS3/FTS5 virtual table subsystem, generated columns. Map to where target CVEs live.

### Chapter 3 — DBMS-Nautilus: Design and Implementation (~15 pages)

**Sections:**
1. **System Overview**: Architecture diagram showing 5 components: Grammar Engine (grammartec/, Rust, 2441 LOC) → Fuzzer Coordinator (fuzzer/, Rust, 1658 LOC) → Fork Server (forksrv/, Rust, 570 LOC) → SQLite Harness (C, ~200 LOC) → Triage Pipeline (Python, ~500 LOC). Data flow: grammar rules → weighted sampling → tree generation/mutation → unparse to SQL → fork server → harness execution → coverage bitmap → queue update. No bandit feedback loop — weights are static per grammar version.
2. **Structural Primitives Philosophy**: Zero PoC contamination principle. Three design constraints: (a) no grammar rule contains a complete CVE PoC as fixed string, (b) every structural pattern needed to reach a target CVE exists as a composable non-terminal, (c) grammar preserves compositional freedom for novel combinations. Example: CVE-2020-13434 needs printf + INT32_MAX, but grammar provides these as independent non-terminals.
3. **Layer Decomposition**:
   - Layer 1 (SQL atoms): 30+ expression types, SELECT/FROM/WHERE/JOIN, window functions, CTEs, DML, DDL, function calls, terminal literals, boundary values
   - Layer 2 (composed shapes): Schema-Setup (6 alternatives), Stress-Query (8 patterns), Validation-Op (4 operations), Boundary-Func-Call (printf/substr/zeroblob with boundary values)
   - Code listings: Schema-Setup alternatives with weights, Stress-Query patterns, Boundary-Func-Call targeting integer overflow
4. **Grammar Evolution** (core contribution):

   | Version | Date | Rules | Key Change | Evidence That Drove It |
   |---------|------|-------|------------|----------------------|
   | v3.0 | 2026-04-27 | 449 | Initial structural primitives | CVE analysis of 6 target vulnerabilities |
   | v3.1 | 2026-04-28 | 449 | S5 (FTS) weight 2.0→0.5 | 92% of crashes were FTS-only; crash portfolio lacked diversity |
   | v3.2 | 2026-05-05 | 475 | +window functions, +self-ref genCol, +count(), +ORDER BY 3-term | Gap analysis: 4 CVEs unreachable without these primitives |
   | v3.3 | 2026-05-10 | 520 | +JSON/JSONB expansion (Json-Key, Json-Path, Json-Literal) | Targeting json.c in latest SQLite 3.53.0 |

5. **Harness Construction**: AFL fork server protocol (`__AFL_INIT()` only, not persistent mode). Three harness types: afl/ (fuzzing, coverage instrumented), test/ (ASan+UBSan triage replay), nosanit/ (production exploitability check). In-memory database, self-contained SQL (grammar generates schema via Schema-Setup). Compilation with `afl-clang-fast`, ASan+UBSan, SQLITE_ENABLE_FTS3/FTS5/RTREE/JSON1, SQLITE_DEBUG.
6. **Oracle Classification**: Exit code table — ASan→223, UBSan→1, SIGTRAP→133, normal→0. How each signal maps to a vulnerability class.
7. **Triage Pipeline**: Stack-hash deduplication (top 5 frames, filter system/sanitizer frames, SHA-256 hash). CVE signature matching (structural regex patterns per CVE). Crash evidence archive (per-crash directories: trigger.sql, stderr.log, metadata.json, reproduce.sh).

### Chapter 4 — Experiments and Evaluation (~15 pages)

**Sections:**
1. **Experimental Setup**: Hardware (Intel Core i7, 16GB RAM, Ubuntu 22.04), Rust 1.77, Clang 14. Campaign parameters: 15-30 min durations, single thread, 4 SQLite target versions (3.30.1, 3.31.1, 3.32.0, 3.32.2). Grammar versions v3.0 through v3.3. Metrics: unique root causes (stack-hash dedup), edge coverage, crash count. No statistical comparison between policies (no bandit) — instead compare across grammar versions and SQLite versions.

2. **RQ1: CVE Rediscovery**
   - Methodology: Run campaigns on 4 CVE-bearing SQLite versions, check crash evidence against CVE signature library
   - Results:
     - BC003 → CVE-2020-13434 (signed integer overflow in `sqlite3_str_vappendf`): Found on 3.30.1, 3.31.1, 3.32.0. 1501 crashes, 6 unique hashes. Grammar's Boundary-Func-Call with printf + INT32_MAX composes the triggering input.
     - BC010 → CVE-2020-9327 (null pointer in `sqlite3Select`): Found on 3.31.1. 1 crash, 1 unique hash. Requires Schema-Setup S2 (genCol) + CREATE VIEW + coalesce() + JOIN — 4 structural elements composed.
     - BC002 → CVE-2020-13871 (misaligned access in `sqlite3WindowUnlinkFromSelect`): Found on 3.30.1. 265 crashes, 1 hash. Stress-Query with window functions triggers use-after-free.
   - Grammar evolution impact: CVE reachability matrix (version × CVE). v3.0 finds CVE-2020-13434 only. v3.2 adds reachability for CVE-2020-9327 and CVE-2020-13871 via window function + genCol primitives.
   - Discussion: Why CVE-2020-13435 not found (needs 5 simultaneous elements — combinatorial probability extremely low in 30-min campaign). Why CVE-2019-19646 not found (infinite loop, not a crash — sanitizer oracle doesn't detect it).

3. **RQ2: New Bug Discovery**
   - Methodology: Analyze crash evidence archive for bug classes with no CVE signature match
   - Results table: All 10 bug classes

     | Class | Bug Type | Severity | CVE Match | Versions Affected | Unique Hashes |
     |-------|----------|----------|-----------|-------------------|---------------|
     | BC001 | Null pointer in sqlite3Fts5GetTokenizer | HIGH | None | 3.30.1, 3.31.1, 3.32.0, 3.32.2 | 4 |
     | BC002 | Misaligned access in sqlite3WindowUnlinkFromSelect | HIGH | CVE-2020-13871 | 3.30.1 | 1 |
     | BC003 | Signed integer overflow in sqlite3_str_vappendf | MEDIUM | CVE-2020-13434 | 3.30.1, 3.31.1, 3.32.0 | 6 |
     | BC004 | Float cast overflow in alsoAnInt | LOW | None | 3.30.1, 3.31.1, 3.32.0, 3.32.2 | 42 |
     | BC005 | Signal 6 in sqlite3WindowListDelete | MEDIUM | None | 3.30.1 | 4 |
     | BC006 | Null pointer in sqlite3AtoF | HIGH | None | 3.30.1 | 1 |
     | BC007 | Null pointer in sqlite3Atoi64 | HIGH | None | 3.30.1 | 1 |
     | BC008 | Float cast overflow in sqlite3VdbeMemNumerify | LOW | None | 3.30.1, 3.32.0 | 8 |
     | BC009 | Signal 6 (no stack) | MEDIUM | None | 3.30.1, 3.31.1 | 21 |
     | BC010 | Null pointer in sqlite3Select | HIGH | CVE-2020-9327 | 3.31.1 | 1 |

   - Key finding: 7 of 10 bug classes have NO CVE match — these are previously unreported bugs in old SQLite versions
   - Case studies:
     - BC001: FTS5 null pointer across all 4 versions — systematic FTS5 bug, not version-specific
     - BC004: 42 unique hashes for float cast overflow — rich cluster indicating pervasive numeric edge case
     - BC006+BC007: Null pointer pair in numeric conversion functions (sqlite3AtoF, sqlite3Atoi64) — related root cause in string-to-number parsing
   - v3.3 on SQLite 3.53.0: 30,627 edges (+17% over v3.2), 0 crashes. Grammar reaches json.c code but all known bugs patched. Demonstrates grammar generalizes to latest version.

4. **Coverage Analysis**
   - Edge counts across grammar versions: v3.0→v3.2 progression on same SQLite target
   - Coverage saturation curve on 3.53.0: 50% at 10s, 90% at 20min, 95% at 37min, 99% at 50min
   - Cross-version coverage comparison

5. **Threats to Validity**
   - Single DBMS (SQLite only)
   - Context-free grammar cannot enforce semantic constraints (type correctness, referential integrity)
   - Sanitizer oracle misses logic bugs (infinite loops, incorrect query results)
   - Campaign duration (15-30 min) may miss bugs requiring longer exploration
   - Stack-hash dedup may over-count or under-count unique root causes

### Conclusion (~2 pages)

- Summary: DBMS-Nautilus with structural primitives grammar rediscovers 3 of 6 target CVEs and finds 7 previously unreported bug classes across 4 SQLite versions
- Key insight: Grammar engineering (iterative refinement guided by evidence) is the primary driver of fuzzing effectiveness, not adaptive sampling
- Limitations: single DBMS, no semantic oracle, CFG limitations
- Future work: RL integration for adaptive rule selection, cross-DBMS grammar portability, semantic-aware generation (type-correct SQL), longer campaigns

## File Structure

```
docs/thesis/v2/
├── thesis.tex           # Main document (from template, adapted)
├── cover.tex            # Vietnamese cover pages (from template, filled in)
├── references.bib       # Bibliography (reuse + expand from old thesis)
├── figures/
│   ├── uet.jpg          # University logo (from template)
│   ├── architecture.tex # TikZ architecture diagram (adapted, no bandit arrow)
│   └── *.png            # Charts from results/charts/
├── chapters/
│   ├── acknowledgement.tex
│   ├── assurance.tex
│   ├── abstract_vi.tex
│   ├── abstract_en.tex
│   ├── glossary.tex
│   ├── c1_introduction.tex
│   ├── c2_background.tex
│   ├── c3_method.tex
│   ├── c4_experiments.tex
│   └── conclusion.tex
```

## Reuse Plan

| Source | Reuse | Changes |
|--------|-------|---------|
| Old C1 (introduction) | ~40% | Reframe around grammar engineering, remove bandit/RL motivation, new RQs |
| Old C2 (background) | ~70% | Remove bandit/MAB section, add DBMS testing tools comparison table |
| Old C3 (method) | ~60% | Remove Section 3.4 (bandit policy), remove Algorithm 1 (bandit update), remove uniform baseline section. Add grammar evolution section as core. |
| Old C4 (experiments) | ~30% | Completely new RQ structure. Reuse setup params, crash data. Remove bandit vs uniform comparison. |
| Old conclusion | ~20% | Rewrite for grammar-focused findings. |
| Template front matter | 100% | Fill in name, title, supervisor, dates |
| references.bib | ~80% | Remove bandit/MAB refs, add DBMS testing tool refs (SQLRight, Griffin, SQLancer, DynSQL) |
| Architecture diagram | ~90% | Remove bandit feedback arrow, simplify to static weights |
| Crash evidence data | 100% | All 10 bug classes, 89 hashes used as-is |
| Coverage charts | 100% | PNG files from results/charts/ |

## Non-Goals

- No bandit/RL content anywhere in the thesis
- No statistical comparison between sampling policies
- No Algorithm pseudocode boxes (no bandit update, no EXP3)
- No Thompson Sampling, no exploration-exploitation analysis
- No discussion of weight convergence or arm selection dynamics
