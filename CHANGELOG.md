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
