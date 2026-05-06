# Documentation Cleanup & Standardization — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure the documentation tree into a maintainable system with clear audience separation, no duplicates, and a master index.

**Architecture:** Three-phase cleanup — Phase 1 moves/archives/deletes files (zero content changes), Phase 2 fixes and creates content (cve-list, README, CHANGELOG, docs index), Phase 3 rewrites architecture.md and workflow-deep-dive.md from the current codebase.

**Tech Stack:** Git, Markdown, Mermaid diagrams

**Spec:** `docs/superpowers/specs/2026-05-05-documentation-cleanup-design.md`

---

## Task 1: Phase 1a — Delete duplicates and create target directories

**Files:**
- Delete: `docs/audit/research-audit-EN.md`
- Delete: `docs/audit/research-audit-VI.md`
- Create dirs: `docs/archive/`, `docs/archive/plans/`, `docs/experiments/`

- [ ] **Step 1: Create target directories**

```bash
mkdir -p docs/archive/plans docs/experiments
```

- [ ] **Step 2: Delete duplicate audit files**

```bash
rm docs/audit/research-audit-EN.md
rm docs/audit/research-audit-VI.md
```

- [ ] **Step 3: Verify deletions and dirs**

```bash
ls docs/audit/research-audit-*.md
# Expected: only research-audit-en.md and research-audit-vi.md remain

ls -d docs/archive docs/archive/plans docs/experiments
# Expected: all three directories exist
```

---

## Task 2: Phase 1b — Archive stale core docs

**Files:**
- Move: `README.md` → `docs/archive/phase1-progress-journal.md`
- Move: `docs/system-guide.md` → `docs/archive/system-guide-v1.md`
- Move: `docs/architecture.md` → `docs/archive/architecture-v1.md`

- [ ] **Step 1: Archive the root README (Phase 1 progress journal)**

```bash
mv README.md docs/archive/phase1-progress-journal.md
```

- [ ] **Step 2: Archive system-guide and architecture before rewrite**

```bash
mv docs/system-guide.md docs/archive/system-guide-v1.md
mv docs/architecture.md docs/archive/architecture-v1.md
```

- [ ] **Step 3: Verify archives exist and originals are gone**

```bash
ls docs/archive/phase1-progress-journal.md docs/archive/system-guide-v1.md docs/archive/architecture-v1.md
# Expected: all three exist

test ! -f README.md && test ! -f docs/system-guide.md && test ! -f docs/architecture.md && echo "OK"
# Expected: OK
```

---

## Task 3: Phase 1c — Move experiment docs to docs/experiments/

**Files:**
- Move: `docs/a1-manual-verification.md` → `docs/experiments/`
- Move: `docs/attack-grammar-pilot-sqlite-3.31.1.md` → `docs/experiments/`
- Move: `docs/attack-grammar-ablation-sqlite-3.31.1.md` → `docs/experiments/`
- Move: `docs/attribution_deep_analysis_15m.md` → `docs/experiments/`
- Move: `docs/crash-report-patterns-pilot.md` → `docs/experiments/`

- [ ] **Step 1: Move all experiment files**

```bash
mv docs/a1-manual-verification.md docs/experiments/
mv docs/attack-grammar-pilot-sqlite-3.31.1.md docs/experiments/
mv docs/attack-grammar-ablation-sqlite-3.31.1.md docs/experiments/
mv docs/attribution_deep_analysis_15m.md docs/experiments/
mv docs/crash-report-patterns-pilot.md docs/experiments/
```

- [ ] **Step 2: Verify**

```bash
ls docs/experiments/
# Expected: 5 files — a1-manual-verification.md, attack-grammar-pilot-sqlite-3.31.1.md,
#   attack-grammar-ablation-sqlite-3.31.1.md, attribution_deep_analysis_15m.md,
#   crash-report-patterns-pilot.md
```

---

## Task 4: Phase 1d — Move legacy CVE analyses to reference/

**Files:**
- Move: `docs/nautilus-legacy-cve-analyze/` → `reference/legacy-analysis/`

- [ ] **Step 1: Move the directory**

```bash
mv docs/nautilus-legacy-cve-analyze reference/legacy-analysis
```

- [ ] **Step 2: Verify**

```bash
ls reference/legacy-analysis/
# Expected: mruby-analyze/ and php-anaylyze/ (note: original typo in dir name, preserve as-is)

test ! -d docs/nautilus-legacy-cve-analyze && echo "OK"
# Expected: OK
```

---

## Task 5: Phase 1e — Rename ONBOARDING.md to lowercase

**Files:**
- Move: `docs/ONBOARDING.md` → `docs/onboarding.md`

- [ ] **Step 1: Rename**

```bash
mv docs/ONBOARDING.md docs/onboarding.md
```

- [ ] **Step 2: Verify**

```bash
ls docs/onboarding.md
# Expected: exists

test ! -f docs/ONBOARDING.md && echo "OK"
# Expected: OK
```

---

## Task 6: Phase 1f — Archive completed plan/spec pairs

**Files:**
- Move 7 plans from `docs/superpowers/plans/` → `docs/archive/plans/`
- Move 7 specs from `docs/superpowers/specs/` → `docs/archive/plans/`

- [ ] **Step 1: Move completed plans**

```bash
for f in \
  2026-04-22-attack-pattern-grammar.md \
  2026-04-22-measurement-and-fidelity.md \
  2026-04-25-component-smoke-tests.md \
  2026-04-25-deep-component-test.md \
  2026-04-27-grammar-v3-structural-primitives.md \
  2026-04-28-campaign-results-grammar-versioning.md \
  2026-04-29-oracle-classification.md; do
  mv "docs/superpowers/plans/$f" docs/archive/plans/
done
```

- [ ] **Step 2: Move completed specs**

```bash
for f in \
  2026-04-22-attack-pattern-grammar-design.md \
  2026-04-22-measurement-and-fidelity-design.md \
  2026-04-25-component-smoke-tests-design.md \
  2026-04-25-deep-component-test-design.md \
  2026-04-27-grammar-v3-structural-primitives-design.md \
  2026-04-28-campaign-results-grammar-versioning-design.md \
  2026-04-29-oracle-classification-design.md; do
  mv "docs/superpowers/specs/$f" docs/archive/plans/
done
```

- [ ] **Step 3: Verify only in-progress plans/specs remain**

```bash
ls docs/superpowers/plans/
# Expected: 2026-05-02-proportional-reward-bandit.md, 2026-05-05-thesis-writing.md

ls docs/superpowers/specs/
# Expected: 2026-05-05-documentation-cleanup-design.md, 2026-05-05-thesis-writing-design.md

ls docs/archive/plans/ | wc -l
# Expected: 14 (7 plans + 7 specs)
```

---

## Task 7: Phase 1 — Commit

- [ ] **Step 1: Review the full diff**

```bash
git status
git diff --stat
```

Expected: only moves and deletes — no content modifications.

- [ ] **Step 2: Stage and commit**

```bash
git add -A
git commit -m "docs: reorganize documentation tree (move/archive/delete)"
```

---

## Task 8: Phase 2a — Fix docs/cve-list.md

**Files:**
- Modify: `docs/cve-list.md`

The existing file has all 6 CVEs but uses an extremely wide single-line table that's unreadable. Rewrite as a clean, readable reference document.

- [ ] **Step 1: Rewrite cve-list.md**

Write `docs/cve-list.md` with this content:

```markdown
# CVE Target List

6 CVEs across 4 vulnerable SQLite versions. This is the authoritative reference for the project.

## Target Versions & CVEs

### sqlite-3.30.1

**CVE-2019-19646** — Infinite loop (DoS)
- **Type:** PRAGMA integrity_check loops forever on generated column with NOT NULL
- **Fix:** 3.31.0 (2020-01-22)
- **Harness:** Built
- **PoC:**
  ```sql
  CREATE TABLE t0 (c0, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0));
  INSERT INTO t0(c0) VALUES (0);
  PRAGMA integrity_check; -- hangs
  ```
- **Source:** [sqlite.org/src/info/bd8c280671ba44a7](https://sqlite.org/src/info/bd8c280671ba44a7)

### sqlite-3.31.1

**CVE-2020-13434** — Integer overflow in printf()
- **Type:** UBSan integer overflow — stack overwrite with 2B+ bytes of 0x30/0x20
- **Fix:** 3.32.1 (2020-05-25)
- **Harness:** Built
- **PoC (simplified):**
  ```sql
  SELECT printf('%.*g', 2147483647, 0.01);
  ```
- **Source:** [sqlite.org/src/info/23439ea582241138](https://sqlite.org/src/info/23439ea582241138)

**CVE-2020-9327** — Uninitialized pointer read
- **Type:** Segfault via generated column + UNIQUE + VIEW + JOIN
- **Fix:** 3.32.0 (2020-05-22)
- **Harness:** Built
- **PoC:**
  ```sql
  CREATE TABLE v0(v3, v1 AS(v1) UNIQUE);
  CREATE TABLE v5(v6 UNIQUE, v7 UNIQUE);
  CREATE VIEW v8(v9) AS SELECT coalesce(v3, v1) FROM v0 WHERE v1 IN('MED BOX');
  SELECT * FROM v8 JOIN v5 WHERE 0 > v7 AND v9 OR v6 = 's%';
  ```
- **Source:** [sqlite.org/src/info/4374860b29383380](https://sqlite.org/src/info/4374860b29383380)

### sqlite-3.32.0

**CVE-2020-13435** — NULL pointer dereference
- **Type:** Read access to NULL pointer via JOIN + window function regression
- **Fix:** 3.32.1 (2020-05-25)
- **Harness:** Built
- **PoC:**
  ```sql
  CREATE TABLE a(c UNIQUE);
  SELECT a.c FROM a JOIN a b ON 3 = a.c NATURAL JOIN a
    WHERE a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM a d WHERE a.c));
  ```
- **Source:** [sqlite.org/src/info/7a5279a25c57adf1](https://sqlite.org/src/info/7a5279a25c57adf1)

### sqlite-3.32.2

**CVE-2020-13871** — Use-after-free
- **Type:** Read-only use-after-free in GROUP BY + HAVING + window function + EXCEPT
- **Fix:** 3.32.3 (2020-06-18)
- **Harness:** Built
- **PoC:**
  ```sql
  CREATE TABLE a(b);
  SELECT(SELECT b FROM a GROUP BY b HAVING(NULL AND b IN(
    (SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY 3.100000
    * SUM(DISTINCT CASE WHEN b LIKE 'SM PACK' THEN b * b ELSE 0 END) / b)))))
  FROM a EXCEPT SELECT b FROM a ORDER BY b, b, b;
  ```
- **Source:** [sqlite.org/src/info/c8d3b9f0a750a529](https://sqlite.org/src/info/c8d3b9f0a750a529)

**CVE-2020-15358** — Heap buffer read-past
- **Type:** Read past end of heap buffer via INTERSECT + JOIN subquery
- **Fix:** 3.32.3 (2020-06-18)
- **Harness:** Built
- **PoC (simplified):**
  ```sql
  CREATE TABLE t1(c1); INSERT INTO t1 VALUES(12),(123),(1234),(NULL),('abc');
  CREATE TABLE t2(c2); INSERT INTO t2 VALUES(44),(55),(123);
  CREATE TABLE t3(c3,c4); INSERT INTO t3 VALUES(66,1),(123,2),(77,3);
  CREATE VIEW t5 AS SELECT c3 FROM t3 ORDER BY c4;
  SELECT * FROM t1, t2
    WHERE c1=(SELECT 123 INTERSECT SELECT c2 FROM t5) AND c1=123;
  ```
- **Source:** [sqlite.org/src/info/8f157e8010b22af0](https://sqlite.org/src/info/8f157e8010b22af0)

## Summary Table

| Version | CVE | Type | Difficulty | Harness |
|---------|-----|------|------------|---------|
| 3.30.1 | CVE-2019-19646 | Infinite loop | Easy-Medium | Built |
| 3.31.1 | CVE-2020-13434 | Integer overflow (UBSan) | Easy | Built |
| 3.31.1 | CVE-2020-9327 | Uninitialized pointer | Hard | Built |
| 3.32.0 | CVE-2020-13435 | NULL ptr deref | Hard | Built |
| 3.32.2 | CVE-2020-13871 | Use-after-free | Medium-Hard | Built |
| 3.32.2 | CVE-2020-15358 | Heap buffer read-past | Medium | Built |
```

- [ ] **Step 2: Verify the file is well-formed**

```bash
wc -l docs/cve-list.md
# Expected: ~85-95 lines
```

---

## Task 9: Phase 2b — Create new README.md

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write the new README**

Write `README.md` with this content:

```markdown
# RL-Nautilus: Grammar-Based Fuzzer with RL for CVE Discovery

Grammar-based coverage-guided fuzzer (Nautilus 2.0) enhanced with Reinforcement Learning for automated CVE discovery in SQLite. Fuzzes 4 CVE-bearing SQLite versions (3.30.1, 3.31.1, 3.32.0, 3.32.2) to compare weighted grammar sampling vs uniform sampling, then integrates a DQN agent for adaptive mutation strategies.

## Quick Start

### Prerequisites

- Rust toolchain (cargo)
- Python 3.13+ with dev headers
- AFL++ (`afl-clang-fast` on PATH)
- clang

### Build

```bash
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
cargo build --release
```

### Build a harness (example: sqlite-3.31.1)

```bash
cd harness
make TARGET=sqlite_harness_patterns_sqlite-3.31.1 SQLITE=../cve_builds/sqlite-3.31.1/sqlite3.c
```

### Run a 15-minute campaign

```bash
DURATION=900 ./scripts/run_eval.sh sqlite-3.31.1 my_run
```

### Run the full ablation (4 variants x 2 seeds)

```bash
DURATION=900 RUNS=2 TARGET=sqlite-3.31.1 ./scripts/run_ablation.sh
```

## Phase Status

| Phase | Status | Key Result |
|-------|--------|------------|
| Phase 1 — Infrastructure | Complete | Fork server, harnesses, grammar engine, oracle verified |
| Phase 2 — Attack grammar + measurement | Complete | TTFC ~1-2s; uniform > bandit on crash diversity (p~0.01) |
| Phase 3 — RL integration | Not started | DQN agent, MutationPolicy trait, runtime weight tuning |

## CVE Targets

| Version | CVEs | Type |
|---------|------|------|
| sqlite-3.30.1 | CVE-2019-19646 | Infinite loop |
| sqlite-3.31.1 | CVE-2020-13434, CVE-2020-9327 | Integer overflow, uninitialized ptr |
| sqlite-3.32.0 | CVE-2020-13435 | NULL ptr deref |
| sqlite-3.32.2 | CVE-2020-15358, CVE-2020-13871 | Heap read-past, use-after-free |

See [docs/cve-list.md](docs/cve-list.md) for full PoC SQL and details.

## Key Results (Phase 2)

- **Time-to-first-crash:** ~1-2 seconds across all versions and policies
- **Crash diversity:** Uniform sampling significantly outperforms bandit (p~0.01, Mann-Whitney U)
- **54 campaigns** completed: 3 versions x 2 policies x N=5, plus cross-version and smoke tests
- **Grammar v3.2:** 475 structural primitive rules covering all 6 CVE building blocks

## Architecture

```
Grammar (Python DSL) → PyO3 → Grammartec (weighted sampling, tree mutation)
                                    ↓
                              Fuzzer Core (multi-threaded coordination)
                                    ↓
                              Fork Server (AFL-compatible, shared memory bitmap)
                                    ↓
                              SQLite Harness (ASan + UBSan oracle)
                                    ↓
                              Triage Pipeline (dedup, classify, CVE signature match)
```

See [docs/architecture.md](docs/architecture.md) for full system design with diagrams.

## Documentation

See [docs/README.md](docs/README.md) for the full documentation index.

| Document | Description |
|----------|-------------|
| [Architecture](docs/architecture.md) | System design, component diagrams, data flow |
| [Workflow Deep Dive](docs/workflow-deep-dive.md) | Fuzzer internals, execution loop, config reference |
| [Onboarding](docs/onboarding.md) | Build, install, run your first campaign |
| [CVE List](docs/cve-list.md) | CVE targets with PoC SQL and harness status |
| [CHANGELOG](CHANGELOG.md) | Project-level changelog |

## License

See [LICENSE.md](LICENSE.md).
```

- [ ] **Step 2: Verify**

```bash
wc -l README.md
# Expected: ~100-120 lines
```

---

## Task 10: Phase 2c — Create CHANGELOG.md

**Files:**
- Create: `CHANGELOG.md`

- [ ] **Step 1: Write CHANGELOG.md**

Write `CHANGELOG.md` with this content. Source data: git log + `grammars/CHANGELOG.md` + archived plans.

```markdown
# Changelog

All notable changes to RL-Nautilus, organized by date.

## 2026-05-05

### Grammar
- **v3.2:** Add 15 window function rules, 3 self-referential GenCol-Expr rules, 3 Col-Def-List-GenCol templates, count() zero-arg, ORDER BY 3-term. All 6 CVEs now reachable. 475 rules total.

### Thesis
- Scaffold LaTeX thesis (cover, chapters 1-4, conclusion, references, front matter)

## 2026-05-01 — 2026-05-04

### Experiments
- Run N=5 bandit vs uniform campaigns on sqlite-3.30.1, 3.31.1, 3.32.0
- Run N=5 fixed-weight bandit vs uniform on sqlite-3.31.1
- Collect time-to-first-crash metrics: ~1-2s for all versions/policies
- Key finding: uniform > bandit on crash diversity (p~0.01, Mann-Whitney U)

### Fuzzer Core
- Thompson Sampling bandit over grammar rule groups (`--policy=bandit`)
- Fix weight compounding bug in bandit reward
- Fix UBSan counter misclassification
- Proportional reward with EMA normalization

### Scripts
- `run_campaign_matrix.sh` for N=5 experiments
- POLICY env var in `run_eval.sh` for bandit/dqn campaigns

## 2026-04-29

### Triage
- `classify.py` — unified dedup + crash classification + markdown report
- Auto-triage integrated into `run_eval.sh` pipeline
- Classify SIGTRAP (signal-5) as debug_assert
- Remove deprecated `dedup.py` and `report.py`

### Scripts
- `compare_campaigns.py` — thesis table generator (markdown + LaTeX)
- `archive_campaign.sh` — manual campaign archiver

## 2026-04-28

### Grammar
- **v3.1:** Reduce FTS virtual table (S5) weight from 2.0 to 0.5 (92% FTS crash dominance fix)

### Results
- Campaign archive directory and `experiments.json` registry
- Grammar versioning system: snapshots, active/ working copy, CHANGELOG

## 2026-04-27

### Grammar
- **v3.0:** Structural primitives design — Schema-Setup x Stress-Query x Validation-Op
- 4 Sql-Stmt shapes, 6 Schema-Setup, 8 Stress-Query, 4 Validation-Op. 449 rules total.

## 2026-04-22 — 2026-04-26

### Grammar
- Attack pattern grammar v1 with tight non-terminals (B2)
- 7 tight NTs for pattern fidelity, 5 rewritten attack patterns
- CVE PoC grammar, attribution analysis scripts

### Triage
- CVE signature library for per-pattern fidelity
- Per-pattern fidelity scorer (A3)

### Scripts
- Attribution analysis, smoke tests, deep component tests

## 2026-03 (Phase 1)

### Infrastructure
- Weighted grammar sampling: `Rule::weighted()`, `loaded_dice`, Python API via PyO3
- AFL-compatible fork server with AFL++ 4.x XOR handshake
- SQLite harness with ASan + UBSan oracle (exit 223 / exit 1)
- Harnesses built for sqlite-3.30.1, 3.31.1, 3.32.0, 3.32.2

### Triage
- Stack-hash deduplication (top-5 frames)
- Delta-debugging minimizer (statement + clause level)

### Scripts
- `run_eval.sh` campaign launcher
- `analyze.py` TTFC + coverage analysis

### Experiments
- Pilot eval on CVE-2020-13434: 219 crashes in 5 minutes (sqlite-3.31.1)
- E1 attribution baseline: 34.5% weight wasted, R25 crash magnet at 21.9x
- E2 v3 A/B test: 1508 queue (+6%), 131 crashes, 92% FTS5
```

- [ ] **Step 2: Verify**

```bash
wc -l CHANGELOG.md
# Expected: ~100-120 lines
```

---

## Task 11: Phase 2d — Create docs/README.md (docs index)

**Files:**
- Create: `docs/README.md`

- [ ] **Step 1: Write the docs index**

Write `docs/README.md`:

```markdown
# Documentation

Master index for all RL-Nautilus documentation.

## Core

| Document | Description |
|----------|-------------|
| [architecture.md](architecture.md) | System design, component diagrams, data flow |
| [workflow-deep-dive.md](workflow-deep-dive.md) | Fuzzer internals, execution loop, config reference |
| [onboarding.md](onboarding.md) | Build, install, run your first campaign |
| [cve-list.md](cve-list.md) | 6 CVE targets with PoC SQL, versions, harness status |

## Experiments

| Document | Description |
|----------|-------------|
| [experiments/a1-manual-verification.md](experiments/a1-manual-verification.md) | Stack-dedup manual verification on sqlite-3.31.1 |
| [experiments/attack-grammar-pilot-sqlite-3.31.1.md](experiments/attack-grammar-pilot-sqlite-3.31.1.md) | Pilot eval: 219 crashes in 5 min on CVE-2020-13434 |
| [experiments/attack-grammar-ablation-sqlite-3.31.1.md](experiments/attack-grammar-ablation-sqlite-3.31.1.md) | E2 ablation: attack vs patterns vs uniform grammar |
| [experiments/attribution_deep_analysis_15m.md](experiments/attribution_deep_analysis_15m.md) | Signal type analysis (SIGNAL(5) vs SIGNAL(6)) |
| [experiments/crash-report-patterns-pilot.md](experiments/crash-report-patterns-pilot.md) | Crash pattern analysis from pilot campaigns |

## Audits

| Document | Description |
|----------|-------------|
| [audit/research-audit-en.md](audit/research-audit-en.md) | Research gap analysis (English) — 2026-04-24 |
| [audit/research-audit-vi.md](audit/research-audit-vi.md) | Research gap analysis (Vietnamese) — 2026-04-24 |
| [audit/grammar-strategy-landscape.md](audit/grammar-strategy-landscape.md) | Grammar mutation strategy inventory |
| [audit/input-journey-paper-vs-code.md](audit/input-journey-paper-vs-code.md) | Paper vs implementation flow mapping |
| [audit/2026-04-30-comprehensive-audit.md](audit/2026-04-30-comprehensive-audit.md) | Multi-expert comprehensive audit |
| [audit/thesis-completeness-checklist.md](audit/thesis-completeness-checklist.md) | Thesis readiness scorecard |

## Feedback

| Document | Description |
|----------|-------------|
| [feedbacks/mentor-feedback.md](feedbacks/mentor-feedback.md) | Thesis advisor feedback notes |

## Reference

| Document | Description |
|----------|-------------|
| [../reference/codebase-walkthrough.md](../reference/codebase-walkthrough.md) | Component-by-component thesis defense walkthrough |
| [../reference/graduate-thesis-policy/policy.md](../reference/graduate-thesis-policy/policy.md) | UET graduation requirements |
| [../reference/legacy-analysis/](../reference/legacy-analysis/) | Original Nautilus CVE analyses (mruby, PHP) |

## Archive

| Document | Description |
|----------|-------------|
| [archive/phase1-progress-journal.md](archive/phase1-progress-journal.md) | Phase 1 weekly build log (original README) |
| [archive/system-guide-v1.md](archive/system-guide-v1.md) | System guide v1 (11-chapter fuzzing pedagogy) |
| [archive/architecture-v1.md](archive/architecture-v1.md) | Architecture v1 (Mermaid diagrams + GitNexus scope) |
| [archive/plans/](archive/plans/) | 14 completed plan/spec pairs (Apr 22 — Apr 29) |
```

- [ ] **Step 2: Verify**

```bash
wc -l docs/README.md
# Expected: ~65-75 lines
```

---

## Task 12: Phase 2 — Commit

- [ ] **Step 1: Review changes**

```bash
git status
git diff --stat
```

Expected: 4 files changed — `docs/cve-list.md` (modified), `README.md` (new), `CHANGELOG.md` (new), `docs/README.md` (new).

- [ ] **Step 2: Stage and commit**

```bash
git add docs/cve-list.md README.md CHANGELOG.md docs/README.md
git commit -m "docs: fix cve-list, rewrite README, create CHANGELOG and docs index"
```

---

## Task 13: Phase 3a — Rewrite docs/architecture.md

**Files:**
- Create: `docs/architecture.md`
- Read (for accuracy): `fuzzer/src/main.rs`, `fuzzer/src/fuzzer.rs`, `grammartec/src/context.rs`, `grammartec/src/rule.rs`, `forksrv/src/lib.rs`, `harness/src/sqlite_harness.c`, `triage/classify.py`, `cve2grammar/cve2grammar/generalizer/pattern_generalizer.py`

- [ ] **Step 1: Read current source files for accuracy**

Read the key source files to extract current function signatures, struct names, and data flows. Do NOT rely on archived docs — read the actual code.

Key files and what to extract:
- `fuzzer/src/main.rs` — thread spawning, status display, main loop entry
- `fuzzer/src/fuzzer.rs` — `Fuzzer` struct, `run_on()`, `exec()`, `new_bits()`, crash classification
- `fuzzer/src/grammar_bandit.rs` — `GrammarBandit`, `select_action()`, `observe_reward()`
- `grammartec/src/context.rs` — `Context`, `add_rule_weighted()`, `dumb_get_random_rule_for_nt()`
- `grammartec/src/rule.rs` — `Rule::plain()`, `Rule::weighted()`, weight field
- `grammartec/src/mutator.rs` — mutation strategies
- `forksrv/src/lib.rs` — `ForkServer`, `run()`, shared memory
- `harness/src/sqlite_harness.c` — `setup_db()`, `__AFL_INIT()`, oracle logic
- `triage/classify.py` — `classify_crash()`, dedup logic
- `cve2grammar/cve2grammar/generalizer/pattern_generalizer.py` — `generalize()` entry point

- [ ] **Step 2: Write docs/architecture.md**

Write `docs/architecture.md` with these sections (target: 400-500 lines):

1. **System Overview** — one-paragraph intro + Mermaid diagram of full pipeline
2. **Component Map** — table with columns: Component | Language | Lines | Key Files | Purpose
   - fuzzer/ (Rust, 3,254 LoC)
   - grammartec/ (Rust, 2,466 LoC)
   - forksrv/ (Rust, 426 LoC)
   - harness/ (C, 89 LoC)
   - triage/ (Python, 878 LoC)
   - cve2grammar/ (Python, separate subtree)
   - scripts/ (Bash+Python, 1,990 LoC)
3. **Data Flow** — step-by-step from grammar rule selection to crash classification, with code references
4. **Coverage Feedback Loop** — Mermaid diagram: bitmap → new_bits → queue → mutation → execute → bitmap
5. **Grammar Weight System** — loaded_dice alias method, `ctx.add_rule_weighted()`, PyO3 bridge, bandit adaptation
6. **Build Architecture** — Cargo workspace members, PyO3 bridge, AFL instrumentation flags, harness compilation
7. **CVE-to-Grammar Pipeline** — tree-sitter parse → AST traversal → pattern_generalizer → ctx.rule() output

Each section must reference actual file paths and function names from the current codebase (verified in Step 1).

- [ ] **Step 3: Verify line count and section completeness**

```bash
wc -l docs/architecture.md
# Expected: 400-500 lines

grep "^##" docs/architecture.md
# Expected: 7 section headers matching the outline above
```

---

## Task 14: Phase 3b — Rewrite docs/workflow-deep-dive.md

**Files:**
- Create: `docs/workflow-deep-dive.md`
- Read (for accuracy): `fuzzer/src/fuzzer.rs`, `fuzzer/src/main.rs`, `fuzzer/src/state.rs`, `fuzzer/src/queue.rs`, `fuzzer/src/config.rs`, `fuzzer/src/grammar_bandit.rs`, `forksrv/src/lib.rs`, `forksrv/src/exitreason.rs`, `scripts/run_eval.sh`, `config.ron`

- [ ] **Step 1: Read current source files for accuracy**

Read the key source files. Extract:
- `fuzzer/src/fuzzer.rs` — `exec()` (line ~318), `exec_raw()`, `run_on()`, `new_bits()` (line ~427), `check_deterministic_behaviour()` (line ~408), exit code classification (line ~181)
- `fuzzer/src/main.rs` — fuzz_loop thread function, attribution counters (line ~160), status display (line ~333)
- `fuzzer/src/state.rs` — `FuzzingState` methods: `minimize()`, `deterministic_tree_mutation()`, `havoc()`, `splice()`, `generate_random()`
- `fuzzer/src/queue.rs` — `Queue`, `QueueItem`, `add()`, `bit_to_inputs`
- `fuzzer/src/config.rs` — all `Config` fields with types and defaults
- `fuzzer/src/grammar_bandit.rs` — `select_action()`, `observe_reward()`, UCB1 formula, EMA
- `forksrv/src/exitreason.rs` — `ExitReason` enum variants
- `scripts/run_eval.sh` — campaign setup flow
- `config.ron` — example configuration

- [ ] **Step 2: Write docs/workflow-deep-dive.md**

Write `docs/workflow-deep-dive.md` with these sections (target: 500-600 lines):

1. **Campaign Lifecycle** — what `run_eval.sh` does: write config.ron → set env vars → launch fuzzer → collect outputs → run triage
2. **Execution Loop** — the per-thread loop: pop queue → mutate (minimize/det/havoc/splice/gen) → `run_on_with_dedup()` → `run_on()` → `exec()` → `exec_raw()` → `ForkServer::run()`
3. **Exit Code Classification** — table:

   | ExitReason | Condition | is_crash | Action | Output Path |
   | Normal(0) | Clean exit | false | Track coverage only | — |
   | Normal(1) | UBSan | true | Save to outputs/signaled/UBSAN_* | exec.log |
   | Normal(223) | ASan | true | Save to outputs/signaled/ASAN_* | exec.log |
   | Signaled(sig) | Signal kill | true | Save to outputs/signaled/{sig}_* | exec.log |
   | Timeouted | Timeout | — | Save to outputs/timeout/* | exec.log |

4. **Coverage Bitmap** — 262144 bytes, dual bitmap (crash/clean), `new_bits()` detection logic
5. **Deterministic Validation** — 5x re-run, `new_bits.retain()` filter
6. **Mutation Strategies** — ExecutionReason enum, attribution counters per strategy, how they map to FuzzingState methods
7. **Input Deduplication** — ring buffer (10k), HashSet, `input_is_known()`
8. **Queue Management** — QueueItem fields, `bit_to_inputs` reverse index, queue file naming convention
9. **Grammar Bandit** — UCB1 formula, EMA normalization, `select_action()` → `observe_reward()` flow, reward computation
10. **Configuration Reference** — table of all config.ron parameters:

    | Parameter | Type | Default | Purpose |
    | number_of_threads | u8 | — | Worker thread count |
    | timeout_in_millis | u64 | 200 | Per-execution timeout |
    | bitmap_size | usize | 262144 | Coverage bitmap bytes |
    | ... (all fields from config.rs) |

Each section must reference actual file paths and line numbers from the current codebase (verified in Step 1).

- [ ] **Step 3: Verify line count and section completeness**

```bash
wc -l docs/workflow-deep-dive.md
# Expected: 500-600 lines

grep "^##" docs/workflow-deep-dive.md
# Expected: 10 section headers matching the outline above
```

---

## Task 15: Phase 3 — Commit

- [ ] **Step 1: Review the new docs**

```bash
git diff --stat
```

Expected: 2 new files — `docs/architecture.md`, `docs/workflow-deep-dive.md`.

- [ ] **Step 2: Stage and commit**

```bash
git add docs/architecture.md docs/workflow-deep-dive.md
git commit -m "docs: rewrite architecture.md and workflow-deep-dive.md from scratch"
```

---

## Task 16: Final verification

- [ ] **Step 1: Verify the complete file tree matches spec**

```bash
echo "=== Core docs ==="
ls docs/README.md docs/architecture.md docs/workflow-deep-dive.md docs/onboarding.md docs/cve-list.md

echo "=== Root docs ==="
ls README.md CHANGELOG.md CLAUDE.md AGENTS.md

echo "=== Experiments ==="
ls docs/experiments/

echo "=== Audits ==="
ls docs/audit/

echo "=== Archive ==="
ls docs/archive/
ls docs/archive/plans/ | wc -l

echo "=== Reference ==="
ls reference/

echo "=== No orphans in docs/ root ==="
ls docs/*.md
# Expected: README.md, architecture.md, workflow-deep-dive.md, onboarding.md, cve-list.md (5 files only)
```

- [ ] **Step 2: Verify no broken internal links**

```bash
# Check that all links in docs/README.md point to existing files
grep -oP '\[.*?\]\((.*?)\)' docs/README.md | grep -oP '\((.*?)\)' | tr -d '()' | while read link; do
  target="docs/$link"
  if [[ "$link" == ../* ]]; then
    target="${link#../}"
  fi
  if [ ! -e "$target" ] && [ ! -e "docs/$link" ]; then
    echo "BROKEN: $link"
  fi
done
# Expected: no output (no broken links)
```

- [ ] **Step 3: Verify git status is clean**

```bash
git status
# Expected: nothing to commit, working tree clean
```
