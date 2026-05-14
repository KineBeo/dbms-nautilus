# Spec: Documentation Reorganization + DQN Code Removal

**Date:** 2026-05-14
**Status:** Draft
**Scope:** docs/ restructure into layered folders, DQN dead code removal, CLAUDE.md update

---

## Problem

1. `docs/architecture.md` (463 lines) mixes core Nautilus architecture with DQN neural network details and GrammarBandit Thompson Sampling. Claude has no clean single source of truth for thesis-aligned system documentation.
2. No dedicated docs for grammar engine design or triage pipeline — these are buried inside the monolithic architecture file.
3. DQN code (`dqn.rs`, `dqn_test.rs`, `candle-core`/`candle-nn` deps) compiles but is never used in thesis campaigns. Dead weight in build times and documentation scope.
4. Bandit code has real campaign data and should be preserved, but documented as an extension separate from core.

## Decision Record

- **Audience:** Full system reference — keep everything documented, reorganize into layers.
- **Code changes:** Remove dead DQN code. Keep bandit (has campaign results).
- **Doc structure:** Layer-based folders (`core/`, `extensions/`, existing folders unchanged).

---

## Workstream 1 — Documentation Reorganization

### Target folder structure

```
docs/
├── core/                         # Thesis Ch3 source of truth
│   ├── architecture.md           # System overview, component map, 5-layer pipeline diagram
│   ├── grammar-engine.md         # Weight system, PyO3 bridge, rule selection, grammar DSL
│   ├── coverage-loop.md          # Bitmap feedback, queue management, mutation strategies
│   ├── triage-pipeline.md        # Crash classification, dedup, CVE signatures, fidelity
│   └── build-and-run.md          # Build prereqs, harness compilation, campaign commands
├── extensions/                   # Non-thesis components, documented for completeness
│   ├── bandit.md                 # GrammarBandit Thompson Sampling — architecture + results
│   └── dqn-archived.md           # DQN/MutationPolicy design (code removed, doc preserved)
├── cve2grammar/
│   └── pipeline.md               # CVE-to-grammar pipeline (from architecture.md §7)
├── experiments/                  # (unchanged)
├── audit/                        # (unchanged)
├── archive/                      # (unchanged, receives old architecture.md)
│   └── architecture-v2.md        # Current architecture.md moved here
├── feedbacks/                    # (unchanged)
├── thesis/                       # (unchanged)
├── onboarding.md                 # (unchanged, update cross-refs)
├── cve-list.md                   # (unchanged)
├── tree-sitter-sqlite.ebnf       # (unchanged)
├── RL-Fuzzer-for-idea.drawio.png # (unchanged)
└── README.md                     # Updated master index
```

### Content mapping — what goes where

Source: current `docs/architecture.md` (463 lines)

| Current section | Target file | What to include | What to exclude |
|---|---|---|---|
| §1 System Overview | `core/architecture.md` | 5-layer pipeline, component map table, Mermaid diagram | Remove DQN/bandit nodes from diagram |
| §2 Component Map | `core/architecture.md` | Core components only (fuzzer, grammartec, forksrv, harness, triage, cve2grammar, scripts, grammars) | Remove `dqn.rs`, `rl_hook.rs` from table |
| §3 Data Flow Steps 1-7 | Split across core files | Steps 1-3 → `core/grammar-engine.md`, Step 4 → `core/coverage-loop.md`, Steps 5-6 → `core/coverage-loop.md`, Step 7 → `core/triage-pipeline.md` | Remove DqnPolicy dispatch from Step 4 |
| §4 Coverage Feedback Loop | `core/coverage-loop.md` | Bitmap loop diagram, GlobalSharedState, coverage.csv | — |
| §5 Grammar Weight System | `core/grammar-engine.md` (static weights), `extensions/bandit.md` (runtime adaptation) | PyO3 bridge, weighted sampling in core; Thompson Sampling in extensions | DQN runtime adaptation → `extensions/dqn-archived.md` |
| §6 Build Architecture | `core/build-and-run.md` | Cargo workspace, build prereqs, harness compilation, AFL handshake | Remove candle-core/candle-nn from dep table |
| §7 CVE-to-Grammar Pipeline | `cve2grammar/pipeline.md` | Full pipeline (scrape → generalize → validate → emit) | — |
| Appendix Key File Reference | `core/architecture.md` (appendix) | Core files only | Remove dqn.rs, rl_hook.rs entries |

### Content for new files (not derived from architecture.md)

| File | Content source |
|---|---|
| `core/triage-pipeline.md` | `docs/workflow-deep-dive.md` triage sections + `triage/` code reading |
| `core/build-and-run.md` | `docs/onboarding.md` + `docs/workflow-deep-dive.md` campaign lifecycle |
| `extensions/dqn-archived.md` | Extract from architecture.md §5 DQN subsection + rl_hook.rs design notes |
| `extensions/bandit.md` | Extract from architecture.md §5 GrammarBandit + `results/fixed_bandit_evaluation.md` |

### docs/README.md update

Rewrite master index to reflect new folder structure. Group by layer:

```markdown
# Documentation

## Core (thesis-aligned)
- [System Architecture](core/architecture.md)
- [Grammar Engine](core/grammar-engine.md)
- [Coverage & Mutation Loop](core/coverage-loop.md)
- [Triage Pipeline](core/triage-pipeline.md)
- [Build & Run](core/build-and-run.md)

## Extensions
- [Grammar Bandit (Thompson Sampling)](extensions/bandit.md)
- [DQN Agent (archived)](extensions/dqn-archived.md)

## CVE-to-Grammar Pipeline
- [Pipeline Reference](cve2grammar/pipeline.md)

## Experiments
(existing links unchanged)

## Audits
(existing links unchanged)
```

---

## Workstream 2 — DQN Code Removal

### GitNexus Impact Analysis Summary

All DQN symbols: **LOW risk, 0 upstream dependencies, 0 execution flows affected.**

| Target | Risk | d=1 | Processes | Action |
|---|---|---|---|---|
| `fuzzer/src/dqn.rs` | LOW | 0 | 0 | DELETE |
| `fuzzer/src/dqn_test.rs` | LOW | 0 | 0 | DELETE |
| `DqnTrainer` struct | LOW | 0 | 0 | DELETE |
| `DqnPolicy` struct | LOW | 0 | 0 | DELETE |
| `MutationPolicy` trait | LOW | 2 impls | 0 | KEEP trait + DefaultPolicy |
| `rl_hook.rs` | LOW | 0 | 0 | EDIT — remove DqnPolicy impl |
| `rl_logger.rs` | LOW | 0 | 0 | KEEP — used by rl_hook |
| `grammar_bandit.rs` | LOW | 0 | 0 | KEEP |
| `config.rs` | — | — | — | EDIT — remove `rl_enabled` field |
| `main.rs` | — | — | — | EDIT — remove DQN init path |
| `Cargo.toml` | — | — | — | EDIT — remove candle deps + dqn_test binary |

### Files to DELETE

1. `fuzzer/src/dqn.rs` — DQN trainer, worker, state, config, neural network
2. `fuzzer/src/dqn_test.rs` — DQN test binary

### Files to EDIT

3. **`fuzzer/Cargo.toml`**
   - Remove `candle-core = { version = "0.9" }`
   - Remove `candle-nn = { version = "0.9" }`
   - Remove `[[bin]] name = "dqn_test"` section

4. **`fuzzer/src/main.rs`**
   - Remove `extern crate candle_core;` (line 4)
   - Remove `extern crate candle_nn;` (line 5)
   - Remove `mod dqn;` (line 19)
   - Remove `use dqn::DqnTrainer;` (line 30)
   - Remove `use rl_hook::{..., DqnPolicy, ...};` — keep DefaultPolicy, MutationPolicy, PolicyContext
   - Remove DQN trainer initialization block (~lines 487-510)
   - Remove `DqnPolicy::new()` in `fuzzing_thread()` (~lines 205-218)
   - Simplify policy selection: always use DefaultPolicy (remove DQN branch)
   - Remove `--policy dqn` from CLI possible_values (keep `uniform`, `bandit`)
   - Keep all bandit-related code unchanged

5. **`fuzzer/src/rl_hook.rs`**
   - Remove `DqnPolicy` struct and its `MutationPolicy` impl
   - Remove `use crate::dqn::*;` import
   - Keep `MutationPolicy` trait, `DefaultPolicy`, `PolicyContext`
   - Keep `use crate::rl_logger::RlLogger;` (still used by remaining code)

6. **`fuzzer/src/config.rs`**
   - Remove `rl_enabled: bool` field (line 53)
   - Remove all 9 DQN hyperparameter fields and their default functions:
     - `rl_epsilon_start: f32` + `default_rl_epsilon_start()`
     - `rl_epsilon_end: f32` + `default_rl_epsilon_end()`
     - `rl_epsilon_decay: u64` + `default_rl_epsilon_decay()`
     - `rl_batch_size: usize` + `default_rl_batch_size()`
     - `rl_replay_size: usize` + `default_rl_replay_size()`
     - `rl_gamma: f32` + `default_rl_gamma()`
     - `rl_lr: f32` + `default_rl_lr()`
     - `rl_target_update: u64` + `default_rl_target_update()`
     - `rl_train_interval: u64` + `default_rl_train_interval()`
   - Remove comment "Phase 2 hook: when true, RL policy controls mutation selection"
   - Update comment on `policy` field: `"uniform"` or `"bandit"` (remove `"dqn"`)
   - Keep `policy: String` field + `default_policy()` (still used for uniform/bandit)

### Files to KEEP (no changes)

- `fuzzer/src/grammar_bandit.rs` — has campaign data, used in main.rs bandit path
- `fuzzer/src/rl_logger.rs` — used by rl_hook.rs
- `fuzzer/src/fuzzer.rs`, `queue.rs`, `shared_state.rs`, `state.rs`, etc. — core, no DQN refs

### Verification

After all edits:
1. `cargo build --release` must succeed
2. `cargo test` must pass
3. Smoke test: `DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 smoke` (60s campaign, uniform policy)
4. Smoke test: `DURATION=60 POLICY=bandit ./scripts/run_eval.sh sqlite-3.31.1 smoke-bandit` (bandit still works)

---

## Workstream 3 — CLAUDE.md Update

After both workstreams complete, update `CLAUDE.md`:

- Remove DQN from "Architecture at a Glance" table
- Remove `candle-core`/`candle-nn` from Key Dependencies
- Update "Phase Status" — Phase 3 note: "DQN code removed; MutationPolicy trait preserved for future RL integration"
- Update doc pointers to new `docs/core/` paths
- Remove `rl_hook.rs`, `dqn.rs` from component descriptions

---

## Workstream 4 — docs/workflow-deep-dive.md Update

- Remove `--policy dqn` references
- Remove `rl_enabled: true` from config.ron example
- Keep `--policy bandit` references
- Update file references to point to new `docs/core/` paths where applicable

---

## Out of Scope

- Removing bandit code or campaign results
- Modifying grammar files
- Thesis .tex changes
- cve2grammar/ subtree changes
- `docs/experiments/` or `docs/audit/` content changes
- Running new fuzzing campaigns

---

## Execution Order

1. **DQN code removal** (Workstream 2) — code changes first, verify build
2. **Documentation reorganization** (Workstream 1) — split architecture.md, create new files
3. **CLAUDE.md update** (Workstream 3)
4. **workflow-deep-dive.md update** (Workstream 4)
5. **Final verification** — build, test, smoke campaigns

Each workstream gets its own commit.
