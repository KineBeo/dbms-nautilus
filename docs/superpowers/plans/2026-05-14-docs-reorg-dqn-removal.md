# Documentation Reorganization + DQN Code Removal — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove dead DQN code, reorganize docs/ into layered folders (core/extensions/cve2grammar), update CLAUDE.md and workflow-deep-dive.md to match.

**Architecture:** Two sequential phases — code cleanup first (verify build), then documentation restructuring. DQN code (dqn.rs, dqn_test.rs, candle deps, DqnPolicy) is deleted. GrammarBandit and MutationPolicy trait are preserved. Docs split from one 463-line architecture.md into focused per-topic files under docs/core/.

**Tech Stack:** Rust (Cargo workspace), Markdown, Bash scripts

**Spec:** `docs/superpowers/specs/2026-05-14-docs-reorg-dqn-removal-design.md`

---

### Task 1: Remove DQN dependencies from Cargo.toml

**Files:**
- Modify: `fuzzer/Cargo.toml`

- [ ] **Step 1: Remove candle deps and dqn_test binary**

Remove lines 21-22 (`candle-core`, `candle-nn`) and lines 38-40 (`[[bin]] name = "dqn_test"`):

```toml
[dependencies]
nix = "0.17.0"
time = "0.1"
subprocess = "0.2.4"
grammartec = {path = "../grammartec"}
forksrv =  {path = "../forksrv"}
libc = "*"
serde = "1.0"
serde_json = "1.0"
serde_derive = "1.0"
argparse = "0.2.2"
ron = "*"
clap = "2.33.1"
pyo3 = "0.21.2"
rand = "0.8"
rand_distr = "0.4"

[[bin]]
name = "fuzzer"
path = "src/main.rs"

[[bin]]
name = "generator"
path = "src/generator.rs"

[[bin]]
name = "mutator"
path = "src/mutation_tester.rs"
```

---

### Task 2: Delete DQN source files

**Files:**
- Delete: `fuzzer/src/dqn.rs`
- Delete: `fuzzer/src/dqn_test.rs`
- Delete: `fuzzer/src/rl_logger.rs`

- [ ] **Step 1: Delete the three files**

```bash
rm fuzzer/src/dqn.rs fuzzer/src/dqn_test.rs fuzzer/src/rl_logger.rs
```

`rl_logger.rs` is only used by `DqnPolicy` in `rl_hook.rs` — once DqnPolicy is removed, it becomes dead code.

---

### Task 3: Strip DQN from rl_hook.rs

**Files:**
- Modify: `fuzzer/src/rl_hook.rs`

- [ ] **Step 1: Rewrite rl_hook.rs — keep MutationPolicy trait + DefaultPolicy only**

Replace entire file with:

```rust
// MutationPolicy trait for pluggable mutation strategy selection.
// DefaultPolicy: Nautilus uses its normal mutation pipeline (all strategies).
// The trait is preserved for future RL integration.

pub struct PolicyContext {
    pub coverage_delta: usize,
    pub is_crash: bool,
    pub is_timeout: bool,
    pub total_coverage: usize,
    pub exec_count: u64,
    pub queue_size: usize,
    pub strategy_emas: [f32; 5],
    pub last_action: Option<u8>,
}

pub trait MutationPolicy: Send {
    fn select_action(&mut self, _ctx: &PolicyContext) -> Option<u8> {
        None
    }

    fn observe(&mut self, _action: u8, _ctx: &PolicyContext) {}
}

pub struct DefaultPolicy;

impl MutationPolicy for DefaultPolicy {}
```

Removed: `DqnPolicy` struct, `ctx_to_dqn_state()`, `use crate::dqn::*`, `use crate::rl_logger::RlLogger`.

---

### Task 4: Strip DQN from config.rs

**Files:**
- Modify: `fuzzer/src/config.rs`

- [ ] **Step 1: Rewrite config.rs — remove all rl_ fields and default functions**

Replace entire file with:

```rust
// Nautilus
// Copyright (C) 2024  Daniel Teuchert, Cornelius Aschermann, Sergej Schumilo

fn default_policy() -> String {
    "uniform".to_string()
}

#[derive(Deserialize, Clone)]
pub struct Config {
    pub number_of_threads: u8,
    pub thread_size: usize,
    pub number_of_generate_inputs: u16,
    pub number_of_deterministic_mutations: usize,
    pub max_tree_size: usize,
    pub bitmap_size: usize,
    pub timeout_in_millis: u64,
    pub path_to_bin_target: String,
    pub path_to_grammar: String,
    pub path_to_workdir: String,
    pub arguments: Vec<String>,

    // Grammar weight policy: "uniform" or "bandit"
    #[serde(default = "default_policy")]
    pub policy: String,
}
```

Removed: `rl_enabled`, all 9 `rl_*` hyperparameter fields, all `default_rl_*()` functions.

---

### Task 5: Strip DQN from main.rs

**Files:**
- Modify: `fuzzer/src/main.rs`

- [ ] **Step 1: Remove DQN extern crates and mod declarations**

Remove these lines from the top of the file:

```rust
// REMOVE these two lines:
extern crate candle_core;
extern crate candle_nn;

// REMOVE this mod:
mod dqn;

// REMOVE this mod:
mod rl_logger;
```

Keep: `mod grammar_bandit;` and all other mods. Keep `mod rl_hook;` but prefix with `#[allow(dead_code)]` to suppress unused warning — the module preserves `MutationPolicy` for future RL work:

```rust
#[allow(dead_code)]
mod rl_hook;
```

- [ ] **Step 2: Update use declarations**

Change:

```rust
use dqn::DqnTrainer;
use rl_hook::{DefaultPolicy, DqnPolicy, MutationPolicy, PolicyContext};
```

To: remove both lines entirely. After Step 4 inlines the default behavior and Step 6 removes the `policy` parameter, no types from `rl_hook` are referenced in main.rs anymore. Keep `mod rl_hook;` in the mod declarations — the module still exists and preserves `MutationPolicy` for future RL integration.

- [ ] **Step 3: Simplify process_input — remove rl_enabled branch**

In `process_input()` (line 58-176), replace the `InputState::Init` match arm:

```rust
InputState::Init(start_index) => {
    let end_index = start_index + 200;

    if state.minimize(inp, start_index, end_index)? {
        if config.rl_enabled {
            inp.state = InputState::Random;
        } else {
            inp.state = InputState::Det((0, 0));
        }
    } else {
        inp.state = InputState::Init(end_index);
    }
}
```

With:

```rust
InputState::Init(start_index) => {
    let end_index = start_index + 200;

    if state.minimize(inp, start_index, end_index)? {
        inp.state = InputState::Det((0, 0));
    } else {
        inp.state = InputState::Init(end_index);
    }
}
```

- [ ] **Step 4: Simplify process_input Random state — remove DQN dispatch**

Replace the entire `InputState::Random` arm (lines 90-173) with:

```rust
InputState::Random => {
    state.splice(inp)?;
    state.havoc(inp)?;
    state.havoc_recursion(inp)?;
}
```

The `PolicyContext` snapshots, `policy.select_action()`, DQN action dispatch, and `policy.observe()` are all DQN-only code paths. `DefaultPolicy.select_action()` always returns `None` which runs all three strategies — so we inline that directly.

- [ ] **Step 5: Simplify fuzzing_thread signature — remove dqn_trainer parameter**

Change the `fuzzing_thread` function signature from:

```rust
fn fuzzing_thread(
    global_state: Arc<Mutex<GlobalSharedState>>,
    config: Config,
    ctx: Context,
    cks: Arc<ChunkStoreWrapper>,
    dqn_trainer: Option<Arc<Mutex<DqnTrainer>>>,
    shared_bandit: Option<Arc<Mutex<GrammarBandit>>>,
) {
```

To:

```rust
fn fuzzing_thread(
    global_state: Arc<Mutex<GlobalSharedState>>,
    config: Config,
    ctx: Context,
    cks: Arc<ChunkStoreWrapper>,
    shared_bandit: Option<Arc<Mutex<GrammarBandit>>>,
) {
```

- [ ] **Step 6: Remove DQN policy construction inside fuzzing_thread**

Remove the entire DQN policy block (lines 205-225):

```rust
// REMOVE this entire block:
let thread_dqn_cfg = dqn::DqnConfig { ... };
let mut dqn_policy_storage: Option<DqnPolicy> = dqn_trainer.map(|trainer| { ... });
let mut default_policy_storage = DefaultPolicy;
let policy: &mut dyn MutationPolicy = if let Some(ref mut p) = dqn_policy_storage { ... };
```

Since `process_input` no longer takes a `policy` parameter (after Step 4 inlined the default behavior), also remove the `policy` argument from `process_input` calls. Update the `process_input` signature:

Change:

```rust
fn process_input(
    state: &mut FuzzingState,
    inp: &mut QueueItem,
    config: &Config,
    policy: &mut dyn MutationPolicy,
    global_state: &Arc<Mutex<GlobalSharedState>>,
) -> Result<(), SubprocessError> {
```

To:

```rust
fn process_input(
    state: &mut FuzzingState,
    inp: &mut QueueItem,
    config: &Config,
    global_state: &Arc<Mutex<GlobalSharedState>>,
) -> Result<(), SubprocessError> {
```

And update the call site in the loop (line 236) from:

```rust
if process_input(&mut state, &mut inp, &config, policy, &global_state).is_err() {
```

To:

```rust
if process_input(&mut state, &mut inp, &config, &global_state).is_err() {
```

- [ ] **Step 7: Remove DQN trainer initialization in main()**

Remove the entire DQN trainer block (lines 487-513):

```rust
// REMOVE this entire block:
let dqn_cfg = dqn::DqnConfig { ... };
let dqn_trainer: Option<Arc<Mutex<DqnTrainer>>> = if config.rl_enabled { ... };
```

- [ ] **Step 8: Update thread spawning — remove trainer parameter**

Change the thread spawn block (lines 529-541). Remove the `trainer` clone and update the `fuzzing_thread` call:

```rust
let threads = (0..config.number_of_threads).map(|_| {
    let state = shared.clone();
    let config = config.clone();
    let ctx = my_context.clone();
    let cks = shared_chunkstore.clone();
    let bandit = shared_bandit.clone();
    thread_number += 1;
    thread::Builder::new()
        .name(format!("fuzzer_{}", thread_number))
        .stack_size(config.thread_size)
        .spawn(move || fuzzing_thread(state, config, ctx, cks, bandit))
});
```

Remove the `let trainer = dqn_trainer.clone();` line.

- [ ] **Step 9: Remove "dqn" from CLI possible_values**

Change line 380:

```rust
.possible_values(&["uniform", "bandit", "dqn"])
.help("Grammar weight policy: uniform (default), bandit (Thompson Sampling), dqn"),
```

To:

```rust
.possible_values(&["uniform", "bandit"])
.help("Grammar weight policy: uniform (default), bandit (Thompson Sampling)"),
```

---

### Task 6: Build verification

- [ ] **Step 1: Build release**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release
```

Expected: successful compilation with no errors. Warnings about unused imports in `rl_hook.rs` are acceptable (they'll be cleaned up if they appear).

- [ ] **Step 2: Run cargo test**

```bash
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo test
```

Expected: all tests pass.

- [ ] **Step 3: Commit DQN removal**

```bash
git add -u fuzzer/
git commit -m "refactor: remove dead DQN code (dqn.rs, rl_logger.rs, candle deps)

Keep MutationPolicy trait and DefaultPolicy for future RL integration.
Keep GrammarBandit (has campaign data, used in bandit policy).
Simplify process_input — inline default mutation strategy.

GitNexus impact: all DQN symbols LOW risk, 0 upstream deps, 0 flows affected."
```

---

### Task 7: Create docs/core/ directory and architecture.md

**Files:**
- Create: `docs/core/architecture.md`

- [ ] **Step 1: Create docs/core/ directory**

```bash
mkdir -p docs/core docs/extensions docs/cve2grammar
```

- [ ] **Step 2: Write docs/core/architecture.md**

Extract §1 System Overview and §2 Component Map from `docs/architecture.md`, removing DQN/bandit nodes from the Mermaid diagram. Remove `dqn.rs`, `rl_hook.rs` rows from component table. Add appendix with core file references only.

Content: system overview paragraph, 5-layer pipeline Mermaid diagram (grammar → engine → fuzzer → fork server → harness → triage, no DQN/bandit nodes), component map table (fuzzer, grammartec, forksrv, harness, triage, cve2grammar, scripts, grammars), key file reference appendix.

Target: ~120 lines.

---

### Task 8: Create docs/core/grammar-engine.md

**Files:**
- Create: `docs/core/grammar-engine.md`

- [ ] **Step 1: Write grammar-engine.md**

Extract from `docs/architecture.md`:
- §3 Data Flow Steps 1-3 (grammar loading, thread init, input generation)
- §5 Grammar Weight System — static weights only (Rule weight storage, weighted random selection, PyO3 bridge)

Exclude: GrammarBandit runtime adaptation (→ extensions/bandit.md), DQN runtime adaptation (→ extensions/dqn-archived.md).

Content: grammar loading via PyO3, `Context::add_rule_weighted()`, weighted sampling algorithm, `Rule` weight field, Python DSL examples.

Target: ~100 lines.

---

### Task 9: Create docs/core/coverage-loop.md

**Files:**
- Create: `docs/core/coverage-loop.md`

- [ ] **Step 1: Write coverage-loop.md**

Extract from `docs/architecture.md`:
- §3 Data Flow Step 4 (mutation — without DqnPolicy dispatch)
- §3 Data Flow Steps 5-6 (execution, coverage detection)
- §4 Coverage Feedback Loop (bitmap loop Mermaid diagram, GlobalSharedState, coverage.csv)

Also incorporate from `docs/workflow-deep-dive.md`:
- §4 Coverage Bitmap (shared memory, dual bitmaps)
- §5 Deterministic Validation
- §6 Mutation Strategies (strategy table, attribution counters — without DqnPolicy dispatch)

Content: mutation strategies table (DefaultPolicy: all three strategies), fork server execution, bitmap feedback, deterministic validation, coverage.csv.

Target: ~150 lines.

---

### Task 10: Create docs/core/triage-pipeline.md

**Files:**
- Create: `docs/core/triage-pipeline.md`

- [ ] **Step 1: Write triage-pipeline.md**

Extract from `docs/architecture.md`:
- §3 Data Flow Step 7 (crash classification)

Also incorporate from `docs/workflow-deep-dive.md`:
- §3 Exit Code Classification (ExitReason table)

Add from code reading of `triage/` directory:
- `classify.py` workflow
- Stack dedup (`stack_dedup.py`)
- CVE signature matching (`cve_signatures.py`)
- Fidelity scoring (`fidelity_score.py`)
- Minimization (`minimize.py`)

Content: exit code classification table, triage pipeline flow, dedup method, CVE matching, fidelity scoring.

Target: ~120 lines.

---

### Task 11: Create docs/core/build-and-run.md

**Files:**
- Create: `docs/core/build-and-run.md`

- [ ] **Step 1: Write build-and-run.md**

Extract from `docs/architecture.md`:
- §6 Build Architecture (Cargo workspace, build prereqs, harness compilation, AFL handshake — without candle deps)

Also incorporate from `docs/workflow-deep-dive.md`:
- §1 Campaign Lifecycle (run_eval.sh steps, config.ron template — without rl_enabled/dqn)
- §10 Configuration Reference (config fields table — without rl_ fields)

Content: Cargo workspace structure, build commands, harness compilation, config.ron reference (without DQN fields), campaign commands.

Target: ~130 lines.

---

### Task 12: Create docs/extensions/bandit.md

**Files:**
- Create: `docs/extensions/bandit.md`

- [ ] **Step 1: Write bandit.md**

Extract from `docs/architecture.md`:
- §5 Grammar Weight System → Runtime weight adaptation — GrammarBandit section

Also incorporate from `docs/workflow-deep-dive.md`:
- §9 Grammar Bandit (full section)

Content: GrammarBandit architecture, Thompson Sampling algorithm, rule groups table, reward/Beta update formulas, apply_multipliers, bandit_log.csv, how to run with `--policy bandit`.

Target: ~120 lines.

---

### Task 13: Create docs/extensions/dqn-archived.md

**Files:**
- Create: `docs/extensions/dqn-archived.md`

- [ ] **Step 1: Write dqn-archived.md**

Extract from `docs/architecture.md`:
- §5 Grammar Weight System → Runtime weight adaptation — DQN section

Note at top: "**Archived:** DQN code was removed on 2026-05-14. This document preserves the design for reference. The `MutationPolicy` trait remains in `rl_hook.rs` for future RL integration."

Content: DQN architecture (state vector, 5 Q-values, epsilon-greedy, experience replay, AdamW), MutationPolicy trait design, how DqnPolicy dispatched actions 0-4.

Target: ~80 lines.

---

### Task 14: Create docs/cve2grammar/pipeline.md

**Files:**
- Create: `docs/cve2grammar/pipeline.md`

- [ ] **Step 1: Write pipeline.md**

Extract from `docs/architecture.md`:
- §7 CVE-to-Grammar Pipeline (full section including Mermaid diagram)

Content: 4-stage pipeline (scrape → generalize → validate → emit), Mermaid diagram, validation invariants, composition with base grammar.

Target: ~80 lines.

---

### Task 15: Archive old architecture.md and update README

**Files:**
- Move: `docs/architecture.md` → `docs/archive/architecture-v2.md`
- Modify: `docs/README.md`

- [ ] **Step 1: Move architecture.md to archive**

```bash
mv docs/architecture.md docs/archive/architecture-v2.md
```

- [ ] **Step 2: Rewrite docs/README.md**

```markdown
# Documentation

## Core (thesis-aligned)

| Document | Description |
|----------|-------------|
| [System Architecture](core/architecture.md) | System overview, component map, 5-layer pipeline diagram |
| [Grammar Engine](core/grammar-engine.md) | Weight system, PyO3 bridge, rule selection, grammar DSL |
| [Coverage & Mutation Loop](core/coverage-loop.md) | Bitmap feedback, queue management, mutation strategies |
| [Triage Pipeline](core/triage-pipeline.md) | Crash classification, dedup, CVE signatures, fidelity scoring |
| [Build & Run](core/build-and-run.md) | Build prereqs, harness compilation, campaign commands, config reference |

## Extensions

| Document | Description |
|----------|-------------|
| [Grammar Bandit (Thompson Sampling)](extensions/bandit.md) | Runtime grammar weight adaptation via Thompson Sampling |
| [DQN Agent (archived)](extensions/dqn-archived.md) | DQN mutation policy design (code removed 2026-05-14) |

## CVE-to-Grammar Pipeline

| Document | Description |
|----------|-------------|
| [Pipeline Reference](cve2grammar/pipeline.md) | CVE bug → generalized grammar rules (4-stage pipeline) |

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
| [audit/research-audit-en.md](audit/research-audit-en.md) | Research gap analysis (English) |
| [audit/research-audit-vi.md](audit/research-audit-vi.md) | Research gap analysis (Vietnamese) |
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

## Archive

| Document | Description |
|----------|-------------|
| [archive/phase1-progress-journal.md](archive/phase1-progress-journal.md) | Phase 1 weekly build log |
| [archive/system-guide-v1.md](archive/system-guide-v1.md) | System guide v1 (11-chapter fuzzing pedagogy) |
| [archive/architecture-v1.md](archive/architecture-v1.md) | Architecture v1 |
| [archive/architecture-v2.md](archive/architecture-v2.md) | Architecture v2 (pre-reorganization, DQN included) |
| [archive/plans/](archive/plans/) | 14 completed plan/spec pairs (Apr 22 — Apr 29) |
```

- [ ] **Step 3: Commit documentation reorganization**

```bash
git add docs/core/ docs/extensions/ docs/cve2grammar/pipeline.md docs/archive/architecture-v2.md docs/README.md
git rm docs/architecture.md
git commit -m "docs: reorganize into layered folders (core/extensions/cve2grammar)

Split 463-line architecture.md into focused per-topic files:
- docs/core/ — thesis-aligned system reference (5 files)
- docs/extensions/ — bandit + archived DQN design (2 files)
- docs/cve2grammar/ — CVE-to-grammar pipeline (1 file)
Old architecture.md archived as docs/archive/architecture-v2.md."
```

---

### Task 16: Update workflow-deep-dive.md

**Files:**
- Modify: `docs/workflow-deep-dive.md`

- [ ] **Step 1: Remove DQN references from workflow-deep-dive.md**

Changes needed:

1. §1 Step 2 config.ron example (line 34): remove `rl_enabled: false,`

2. §1 Step 4 (line 47-48): change `The \`--policy\` flag accepts \`uniform\`, \`bandit\`, or \`dqn\`` to `The \`--policy\` flag accepts \`uniform\` or \`bandit\``

3. §6 Mutation Strategies §`InputState::Random` dispatch (lines 248-254): remove the `DqnPolicy` bullet:
   - Remove: "- `DqnPolicy` (RL enabled): calls `policy.select_action()` and routes to exactly one strategy by action index..."
   - Keep: "- `DefaultPolicy` (no RL): runs all three strategies..."
   - Reword DefaultPolicy description: remove "(no RL)" → just "Runs all three strategies — `splice`, `havoc`, `havoc_recursion` — unconditionally."

4. §10 Configuration Reference table (lines 440-450): remove all `rl_*` rows and the `rl_enabled` row

5. §10 Quick-start config (line 467): remove `rl_enabled: false,`

6. §10 last paragraph (line 472): remove "For DQN, set `rl_enabled: true` and optionally tune the `rl_*` hyperparameters."

- [ ] **Step 2: Commit workflow update**

```bash
git add docs/workflow-deep-dive.md
git commit -m "docs: remove DQN references from workflow-deep-dive.md"
```

---

### Task 17: Update parent CLAUDE.md

**Files:**
- Modify: `/home/kienbeovl/Desktop/claude-code-fuzzing/CLAUDE.md`

- [ ] **Step 1: Update Project Overview**

Change line 7:

```markdown
Grammar-based fuzzer (Nautilus 2.0) enhanced with Reinforcement Learning for automated CVE discovery in SQLite. Fuzzes 4 CVE-bearing SQLite versions (3.30.1, 3.31.1, 3.32.0, 3.32.2) to compare weighted grammar sampling vs uniform sampling, then integrate DQN agent for adaptive mutation strategies.
```

To:

```markdown
Grammar-based fuzzer (Nautilus 2.0) with weighted grammar sampling for automated CVE discovery in SQLite. Fuzzes 4 CVE-bearing SQLite versions (3.30.1, 3.31.1, 3.32.0, 3.32.2) to measure how grammar design affects CVE rediscovery rates. Optional Thompson Sampling bandit for runtime weight adaptation.
```

- [ ] **Step 2: Update Phase Status table**

Change line 96:

```markdown
| Phase 3 — RL integration | Not started | DQN agent, MutationPolicy trait, runtime weight tuning |
```

To:

```markdown
| Phase 3 — RL integration | Deferred | DQN code removed 2026-05-14; MutationPolicy trait preserved for future work |
```

- [ ] **Step 3: Commit CLAUDE.md update**

```bash
git add /home/kienbeovl/Desktop/claude-code-fuzzing/CLAUDE.md
git commit -m "docs: update CLAUDE.md — remove DQN references, update phase status"
```

---

### Task 18: Update phase-2 CLAUDE.md

**Files:**
- Modify: `/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/CLAUDE.md`

No changes needed — the phase-2 CLAUDE.md doesn't contain Architecture at a Glance or Key Dependencies tables (those are in the parent). Verify this by confirming the file content doesn't reference DQN directly.

- [ ] **Step 1: Verify no DQN references in phase-2 CLAUDE.md**

```bash
grep -n "dqn\|DQN\|candle\|rl_enabled" /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/CLAUDE.md
```

Expected: no matches (or only in archived plan/spec references which are fine to keep).

---

### Task 19: Final verification

- [ ] **Step 1: Full release build**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release
```

Expected: clean build, no warnings about missing modules.

- [ ] **Step 2: Verify all doc links resolve**

```bash
# Check that all core docs exist
ls docs/core/architecture.md docs/core/grammar-engine.md docs/core/coverage-loop.md docs/core/triage-pipeline.md docs/core/build-and-run.md
ls docs/extensions/bandit.md docs/extensions/dqn-archived.md
ls docs/cve2grammar/pipeline.md
ls docs/archive/architecture-v2.md
```

Expected: all files exist.

- [ ] **Step 3: Verify old architecture.md is gone from docs/**

```bash
test ! -f docs/architecture.md && echo "OK: architecture.md moved to archive"
```

- [ ] **Step 4: Verify bandit code still compiles**

```bash
grep -c "grammar_bandit" fuzzer/src/main.rs
```

Expected: 4+ matches (mod declaration, use, function calls).
