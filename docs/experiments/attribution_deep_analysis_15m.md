# Deep Attribution Analysis — 15-min Baseline Campaign

**Date:** 2026-04-26  
**Target:** sqlite-3.31.1  
**Grammar:** sqlite_patterns.py (26 Sql-Stmt alternatives)  
**Duration:** 900s  
**Results:** 5,374 log entries, 329 saved crash files, 1,423 queue entries, 83,092 total executions

---

## Q1: Crash Signal Types

All crashes are SIGNAL(5) (SQLite debug assert) or SIGNAL(6) (SIGABRT). No ASan (exit 223) or UBSan (exit 1) detected.

| Signal | Count | Meaning |
|--------|-------|---------|
| SIGNAL(5) | 3,672 | SQLite SQLITE_MISUSE / debug assert |
| SIGNAL(6) | 473 | SIGABRT (likely assertion failure) |

**R25 (Pattern-DDL-DQL)** uniquely produces SIGNAL(6) at high rate (378/1975 = 19%), suggesting it triggers a different class of assertions than other rules.

---

## Q2: Temporal Discovery Pattern

Discovery is heavily front-loaded. Most rules find their coverage in Q1 (execs 0–20k), then plateau.

**Rules that keep finding new paths late (Q3+Q4):**
- R7 Create-Table-Stmt: 27+34 in Q3+Q4 (acceleration!)
- R26 Pattern-GenCol-Op: 27+32 in Q3+Q4 (sustained)
- R27 Pattern-Compound: 24+28 in Q3+Q4 (late bloomer)
- R21 Json-Deep: 12+24 in Q3+Q4 (late surge)

**Rules that exhaust early (Q1 only):**
- R3 Select-Stmt: 5→0→0→0
- R5 Update-Stmt: 4→0→0→0
- R17 Deep-Nested-Select: 7→0→0→0
- R20 Window-Func-Complex: 9→0→0→0

**Implication for RL:** An RL agent should learn to shift weight FROM early-exhausting rules TO late-blooming rules over the campaign lifetime. This is a natural curriculum learning signal.

---

## Q3: Crash-to-Coverage Ratio

| Category | Rules | Interpretation |
|----------|-------|----------------|
| **CRASH MAGNET** (>10x) | R25 (21.9x) | Finds crashes 22x more often than new coverage |
| **Crash-heavy** (3–10x) | R15, R11, R21, R23, R14, R16, R24 | Consistently trigger known crash paths |
| **Balanced** (1–3x) | R19, R22, R7, R12 | Good mix of exploration and crash-finding |
| **Explorer** (<1x) | R28, R26, R27 | High coverage, low crashes — explores new code |
| **Dead** (0 crashes) | R3,R4,R5,R6,R8,R10,R13,R17,R18,R20 | 10 rules that never crash |

**Key insight:** R25 has a 21.9x crash ratio — it barely explores new paths but hammers the same crash sites. The RL agent should recognize this: R25 is valuable early (finds crash paths) but becomes redundant mid-campaign.

---

## Q4: SQL Keyword Fingerprints in Crashes

**Common crash ingredients across top rules:**
1. **CREATE TABLE + SELECT + EXISTS** — present in >75% of crashes for 6/8 top rules
2. **JOIN / NATURAL JOIN** — present in 60–88% of crashes
3. **coalesce()** — present in 38–80% of crashes (appears in query planner optimization paths)

**Rule-specific signatures:**
- **R25 (DDL-DQL):** 100% have CREATE TABLE + SELECT + EXISTS. 80% have NATURAL JOIN + coalesce. This is the "table + complex query" pattern.
- **R21 (Json-Deep):** 100% have json_* functions. Combined with CREATE TABLE (79%) and EXISTS (77%).
- **R24 (Boundary-Func):** 78% have printf(), 41% zeroblob() — boundary integer arguments.
- **R19 (Recursive-CTE):** 100% WITH RECURSIVE + UNION + AS(). The CTE recursion structure itself is the trigger.
- **R11 (Virtual-Table):** 72% fts5, 8% fts3. FTS virtual tables are a distinct crash surface.
- **R23 (Explain-Stress):** 100% EXPLAIN. Forces query planner to materialize plans for complex queries.

**Insight for grammar redesign:** The crash-producing "shape" is: **DDL (create structure) → DQL (query with optimizer-stressing constructs)**. The specific stressors are: EXISTS subqueries, NATURAL JOIN, coalesce(), recursive CTEs, and FTS virtual tables.

---

## Q5: Weight Efficiency

Current weights vs optimal weights (based on crash production):

| Verdict | Rules | Total Weight | Total Crashes |
|---------|-------|--------------|---------------|
| **UNDER-WEIGHTED** (>3x eff) | R25, R11, R7, R21, R14 | 4.4 (13.8%) | 3,059 (73.8%) |
| **Well-calibrated** | R23, R12, R24, R19, R15 | 7.4 (23.2%) | 929 (22.4%) |
| **OVER-WEIGHTED** (<0.5x eff) | R9, R16, R22, R26, R28, R27 | 9.1 (28.5%) | 157 (3.8%) |
| **WASTED WEIGHT** (0 crashes) | R3-R6, R8, R10, R13, R17, R18, R20 | 11.0 (34.5%) | 0 (0%) |

**34.5% of sampling probability produces zero crashes.** The RL agent's primary job is to reallocate this wasted weight to R25, R11, R7, R21, R14.

**Ideal weight rebalancing (based on efficiency):**
- R11 (0.3 → ~1.5): 5.7x under-weighted, virtual tables find unique crashes
- R7 (0.3 → ~1.5): 5.1x under-weighted, plain CREATE TABLE is a crash workhorse
- R21 (1.0 → ~4.0): 4.0x under-weighted, json functions + DDL is productive
- R14 (0.3 → ~1.0): 3.8x under-weighted, PRAGMA triggers assertions
- R20 (3.0 → ~0.3): highest weight, zero crashes — should be demoted
- R17 (2.5 → ~0.3): zero crashes, demote
- R18 (2.0 → ~0.3): zero crashes, demote

---

## Q6: Crash Uniqueness

| Metric | Value |
|--------|-------|
| Crash log entries | 4,145 |
| Saved crash files | 329 |
| Unique file hashes | 329 (100% unique) |
| Unique SQL prefixes (100ch) | 1,205 |

The 4,145 crash log entries collapse to 329 saved files — the fork server only saves crashes with new coverage bits. Each saved file is genuinely unique (329/329 unique SHA-256 hashes). The 1,205 unique SQL prefixes show the fuzzer is generating diverse crash triggers, not just replaying the same template.

**Signal breakdown:** 292 SIGNAL(5), 37 SIGNAL(6).

---

## Q7: Mutation Amplification

How much do mutations (Havoc, HavocRec, Splice) amplify initial Gen discoveries?

| Category | Rules | Pattern |
|----------|-------|---------|
| **Mutation-dependent** (0 Gen crashes, many Mut crashes) | R21 (0→394), R7 (0→143), R23 (0→145), R14 (0→122), R11 (7→177) | Need Gen seed + mutation to crash |
| **Gen-sufficient** (crashes from Gen alone) | R25 (21 Gen + 279 Mut), R24 (4 Gen + 360 Mut) | Gen finds some, mutation amplifies |
| **Explorer-only** (high COV amp, no crashes) | R26 (4.9x), R27 (3.8x) | Mutations explore but don't crash |
| **Mutation-dead** (0x amplification) | R17, R18, R20, R3, R5, R6, R10, R13 | Mutations add nothing |

**Critical finding:** R21 (Json-Deep) has the highest amplification at 13.7x — it generates only 6 COV paths from Gen, but mutations explore 82 new paths and cause 394 crashes. This means the Gen template is a "seed" that mutations evolve into crash-inducing variants. Same for R7 (8.1x) and R9 (11.0x).

**RL implication:** The agent should NOT just optimize for Gen-phase crashes. It needs to recognize that some rules are "seed rules" whose value is unlocked by mutation, while others (R25) are "direct crashers" productive from Gen phase.

---

## Summary: What This Means for the Roadmap

### For Grammar Redesign (#3):
1. **Keep and boost:** R25 (DDL-DQL), R11 (Virtual Table), R7 (Create Table), R21 (Json), R14 (Pragma), R24 (Boundary Func)
2. **Keep but reduce weight:** R26 (GenCol-Op), R27 (Compound), R28 (Schema-Pragma) — good explorers, low crash rate
3. **Demote or remove:** R17 (Deep-Nested-Select), R18 (Long-Join-Chain), R20 (Window-Func-Complex) — zero crashes, zero mutation value
4. **The crash recipe:** DDL + optimizer-stressing DQL (EXISTS, NATURAL JOIN, coalesce, recursive CTE)

### For RL Rewiring (#4):
1. **State features needed:** per-rule COV velocity (from Q2 temporal data), crash-to-COV ratio, mutation amplification factor
2. **Action space:** adjust weights on 26 Sql-Stmt rules via ctx.set_weight()
3. **Reward signal:** new coverage bits + crash discovery, with diminishing returns for repeated crash paths (R25 saturation)
4. **Curriculum learning:** shift from crash-magnet rules (R25) early to explorer rules (R26, R27) late

### For Evaluation (#3b):
1. **TTFC (Time to First Crash):** R25 first crash at exec 595, R24 at exec 375, R21 at exec 3151
2. **Crash diversity:** 329 unique crash files from 292 SIGNAL(5) + 37 SIGNAL(6)
3. **Weight efficiency metric:** crashes_per_unit_weight is the key metric for comparing grammar variants
