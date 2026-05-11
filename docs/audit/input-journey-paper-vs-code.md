# The Journey of One Input: Paper (NDSS'19) vs RL-Nautilus Code

**Date:** 2026-04-26
**Scope:** Step-by-step trace of a single input's lifecycle, comparing the original Nautilus paper (NDSS 2019) with the RL-Nautilus phase-2 codebase

---

## Overview Diagram

```
PAPER (Nautilus NDSS'19)                    RL-NAUTILUS (phase-2 code)
========================                    =========================

  Grammar (ANTLR/JSON)                       Grammar (Python via PyO3)
       |                                          |
  [1] Parse grammar                         [1] Load grammar (python_grammar_loader.rs)
       |                                          |
  [2] Generate tree (naive/uniform)         [2] Generate tree (weighted/loaded_dice)
       |                                          |
  [3] Unparse to string                     [3] Unparse to Vec<u8>
       |                                          |
  [4] Dedup check                           [4] Dedup check (ring buffer 10k)
       |                                          |
  [5] Write to temp file                    [5] Write to temp file
       |                                          |
  [6] Fork server exec                      [6] Fork server exec (AFL++ 4.x XOR handshake)
       |                                          |
  [7] Read bitmap (64KB)                    [7] Read bitmap (256KB)
       |                                          |
  [8] Check new bits                        [8] Check new bits + determinism check (5x re-run)
       |                                          |
  [9] Oracle: crash/new/discard             [9] Oracle: ASan(223)/UBSan(1)/Signal/Timeout/Normal
       |                                          |
 [10] If new: minimize + queue             [10] If new: minimize + queue + RL observe
       |                                          |
 [11] Mutate from queue                    [11] RL policy selects mutation strategy
       |                                          |
 [12] Back to [3]                          [12] Back to [3]
```

---

## Step-by-Step Deep Dive

### STEP 1: Grammar Loading

**Paper (Section IV-A, V-B):**
- Accepts JSON (native format) or ANTLR grammars
- ANTLR parser converts to internal representation
- Grammar = `(N, T, R, S)` — non-terminals, terminals, production rules, start symbol
- Precomputes: `min(n)` per non-terminal, `p(n,l,r)` per rule per length for uniform generation
- Supports "unparse scripts" for non-CFG languages (e.g., XML tags with matching IDs)

**RL-Nautilus code:**
- Grammars written in Python using `ctx.rule("NT", "format")` DSL
- Loaded via PyO3 bridge: `python_grammar_loader.rs` -> `PyContext`
- `Context::add_rule_weighted(nt, format, weight)` stores rules with float weights (`context.rs:70-81`)
- `Context::initialize(max_len)` precomputes `calc_min_len()` and `calc_num_options()` (`context.rs:47-50`)
- Also supports `add_script(nt, nts, script)` for Python callbacks and `add_regex(nt, regex)` for regex terminals — both unused in current grammars

**Key difference:** Paper uses JSON/ANTLR grammars with uniform generation. Code uses Python DSL with **weighted** rules via `loaded_dice::Dice` for O(1) weighted sampling. This is the central thesis addition — grammars carry CVE-informed weight priors.

---

### STEP 2: Tree Generation

**Paper (Section IV-A):**
Two generation algorithms:
- **Naive generation:** randomly pick one applicable rule per non-terminal. Leads to bias — 50% of trees terminate immediately if a terminal rule exists.
- **Uniform generation:** uses McKenzie's algorithm. For each non-terminal n, length l, rule r: precompute `p(n,l,r)` = number of possible subtrees. Pick rules proportional to subtree count. Produces unbiased sampling over all possible derivation trees.
- Both include a duplicate filter: check if the generated input was already tried recently.
- Initial batch: generate 1000 random inputs from scratch.

**RL-Nautilus code (`state.rs:191-197`):**
```rust
pub fn generate_random(&mut self, nt: &str) -> Result<(), SubprocessError> {
    let nonterm = self.ctx.nt_id(nt);
    let len = self.ctx.get_random_len_for_nt(&nonterm);
    let tree = self.ctx.generate_tree_from_nt(nonterm, len);
    self.fuzzer.run_on_with_dedup(&tree, ExecutionReason::Gen, &mut self.ctx)?;
}
```
- Uses `get_random_len_for_nt` which selects a random tree size
- `generate_tree_from_nt` uses the **weighted** rule selection via `loaded_dice` — NOT uniform generation
- Initial batch: `number_of_generate_inputs` = 100 (from config.ron), not 1000
- Dedup filter identical: ring buffer of 10,000 recent inputs (`fuzzer.rs:346-362`)

**Key difference:** Paper recommends uniform generation for unbiased exploration. Code uses weighted generation — CVE-stress patterns (weight 2.0-3.5) get sampled 2-7x more than base SQL (weight 0.2-1.0). The ablation showed this doesn't help at 15-min horizon (weighted = uniform for RC discovery).

---

### STEP 3: Unparse (Tree -> String)

**Paper (Section IV-D):**
- Derivation tree is "unparsed" by concatenating all terminal symbols left-to-right
- For plain CFGs: straightforward recursive concatenation
- For extended CFGs with scripts: the unparse function calls a user-defined script that can perform arbitrary computation on child subtree outputs (e.g., XML closing tags matching opening tags)

**RL-Nautilus code (`tree.rs:51-60` -> `unparse_to_vec`):**
```rust
fn unparse_step(n: NodeID, ...) {
    match rule {
        PlainRule { data } => output.extend(data),
        ScriptRule { script } => { /* call Python callback via PyO3 */ }
    }
}
```
- `tree.unparse_to_vec(ctx)` walks the tree and concatenates terminals
- Script rules supported but unused in current SQLite grammars
- Output is `Vec<u8>` — binary-safe

**Key difference:** Essentially identical. Both support scripts for non-CFG. Neither version uses scripts for SQLite (SQL is context-free enough).

---

### STEP 4: Dedup Check

**Paper:** Mentions a "filter that checks whether the generated input was already generated in the recent past."

**RL-Nautilus code (`fuzzer.rs:346-362`):**
```rust
fn input_is_known(&mut self, code: &[u8]) -> bool {
    if self.last_tried_inputs.contains(code) { return true; }
    self.last_tried_inputs.insert(code.to_vec());
    if self.last_inputs_ring_buffer.len() == 10000 {
        self.last_tried_inputs.remove(&self.last_inputs_ring_buffer.pop_back()...);
    }
    self.last_inputs_ring_buffer.push_front(code.to_vec());
    return false;
}
```
- `HashSet` + `VecDeque` ring buffer, capacity 10,000
- Exact byte-level match only
- Called by `run_on_with_dedup` — all mutation strategies except `Min`/`MinRec` use this

**Key difference:** None — same design.

---

### STEP 5: Write to Temp File + STEP 6: Fork Server Execution

**Paper (Section V-A):**
- AFL-style source-code instrumentation with 64KB shared bitmap
- Fork server protocol: parent sends run command, child reads input, child exits, parent reads status
- One execution per fork (NOT persistent mode)

**RL-Nautilus code (`forksrv/src/lib.rs:192-233`):**
```rust
pub fn run(&mut self, data: &[u8]) -> Result<ExitReason, SubprocessError> {
    // 1. Zero shared bitmap
    for i in self.get_shared_mut().iter_mut() { *i = 0; }
    // 2. Write data to temp file (truncate, seek, write, seek)
    unistd::ftruncate(self.inp_file, 0)?;
    unistd::write(self.inp_file, data)?;
    // 3. Send run command (4 zero bytes)
    unistd::write(self.ctl_in, &[0, 0, 0, 0])?;
    // 4. Read child PID
    let pid = self.st_out.read_i32::<LittleEndian>()?;
    // 5. Read exit status (or timeout -> SIGKILL)
    if let Ok(status) = self.st_out.read_i32::<LittleEndian>() {
        return Ok(ExitReason::from_wait_status(...));
    }
    signal::kill(pid, Signal::SIGKILL)?;
    return Ok(ExitReason::Timeouted);
}
```

The harness side (`sqlite_harness.c:98-119`):
```c
int main(int argc, char **argv) {
    __AFL_INIT();  // fork server starts here
    char *sql = read_input(argv[1], &sql_len);
    sqlite3_exec(db, sql, NULL, NULL, &errmsg);  // execute one SQL
    sqlite3_close(db);
    return 0;
}
```
- Schema is pre-loaded in `__attribute__((constructor)) setup_db()` — **before** `__AFL_INIT()`, so schema setup cost is paid once per fork server lifetime, not per execution

**Key differences:**
1. **Bitmap size:** Paper uses 64KB (1<<16). Code uses 256KB (262144) — 4x larger, catches more edge transitions
2. **AFL++ 4.x handshake:** Code implements XOR handshake protocol (`hello ^ 0xffffffff`), paper used AFL 2.x simple protocol
3. **Startup timeout:** Code uses 30-second startup timeout for ASan init, then switches to per-run timeout
4. **Schema pre-loading:** Code's harness pre-loads tables/indices/views/FTS before fork — the paper's targets (mruby, PHP, Lua, ChakraCore) had no equivalent

---

### STEP 7-8: Bitmap Reading + New Bit Detection

**Paper (Section V-D):**
- After execution, compare the run's bitmap against the global bitmap
- If any new bit is set (edge transition not seen before), the input is "interesting"
- No mention of determinism checking

**RL-Nautilus code (`fuzzer.rs:443-465` + `fuzzer.rs:424-441`):**

New bits detection:
```rust
pub fn new_bits(&mut self, is_crash: bool) -> Option<Vec<usize>> {
    let run_bitmap = self.forksrv.get_shared();
    let shared_bitmap = gstate_lock.bitmaps.get_mut(&is_crash)?;
    for (i, elem) in shared_bitmap.iter_mut().enumerate() {
        if (run_bitmap[i] != 0) && (*elem == 0) {
            *elem |= run_bitmap[i];
            res.push(i);
        }
    }
    if res.len() > 0 { Some(res) } else { None }
}
```

Determinism check — **NOT in the paper**:
```rust
fn check_deterministic_behaviour(&mut self, old_bitmap, new_bits, code) {
    for _ in 0..5 {
        self.exec_raw(code)?;  // re-run 5 times
        new_bits.retain(|&i| run_bitmap[i] != 0);  // keep only consistent bits
    }
}
```

**Key differences:**
1. **Separate crash/non-crash bitmaps:** Code maintains `bitmaps: HashMap<bool, Vec<u8>>` — separate bitmaps for crash paths vs normal paths. Paper has one bitmap.
2. **Determinism verification:** Code re-executes the input **5 additional times** and only keeps bits that appear consistently. This filters out non-deterministic coverage from SQLite's internal randomness. Paper doesn't do this — 6x cost per interesting input.

---

### STEP 9: Oracle (Crash Classification)

**Paper (Section V):**
- Crash = any signal (SIGSEGV, SIGABRT, etc.)
- Timeout = process exceeded time limit
- Normal = input processed successfully
- No ASan/UBSan distinction discussed

**RL-Nautilus code (`fuzzer.rs:202-307`):**

```
Exit code 223  -> ASan crash    -> save to outputs/signaled/ASAN_*
Exit code 1    -> UBSan crash   -> save to outputs/signaled/UBSAN_*
Signal(N)      -> OS signal     -> save to outputs/signaled/Signal_*
Timeout        -> killed        -> save to outputs/timeout/*
Normal(0)      -> clean exit    -> if new bits, add to queue
Normal(other)  -> semantic err  -> ignored (not a crash)
```

Per-strategy statistics tracked:
```rust
pub bits_found_by_havoc: u64,
pub bits_found_by_havoc_rec: u64,
pub bits_found_by_splice: u64,
pub bits_found_by_det: u64,
pub bits_found_by_gen: u64,
pub asan_found_by_havoc: u64,
// ... (14 counters total)
```

**Key difference:** Code has a **rich oracle** distinguishing ASan/UBSan/Signal/Timeout, with per-strategy crash attribution. Paper treats all crashes uniformly. This enables the triage pipeline (stack_dedup, fidelity scoring, CVE signature matching) that the paper doesn't have.

---

### STEP 10: Queue Addition + Minimization

**Paper (Section IV-B, V-D, Fig. 2):**
Queue item lifecycle (state machine):
```
init -> det -> detafl -> random
```
- **init:** Minimize the input (subtree minimization + recursive minimization)
- **det:** Rules mutation + Random (Recursive) mutation + Splice mutation
- **detafl:** AFL mutation (bit flips, arithmetic, interesting values) + Random + Splice
- **random:** Random mutation + Random Recursive mutation + Splice mutation (final state, loops forever)

Minimization has two phases:
1. **Subtree minimization:** For each node, try replacing its subtree with the smallest possible subtree of the same non-terminal. Keep if coverage is preserved.
2. **Recursive minimization:** Find recursive structures (e.g., `EXPR -> EXPR + EXPR`), collapse to remove one level of recursion. Keep if coverage is preserved.

After minimization, the tree is added to the **ChunkStore** for future splice operations.

**RL-Nautilus code (`main.rs:48-173`, `state.rs:41-106`):**

Queue item lifecycle (state machine):
```
Init(start_index) -> Det(cycle, start_index) -> Random
                                              OR
Init(start_index) -> Random  (if rl_enabled)
```

```rust
match inp.state {
    InputState::Init(start_index) => {
        if state.minimize(inp, start_index, end_index)? {
            if config.rl_enabled {
                inp.state = InputState::Random;  // SKIP Det when RL controls
            } else {
                inp.state = InputState::Det((0, 0));
            }
        }
    }
    InputState::Det((cycle, start_index)) => {
        // Rules mutation (deterministic)
        state.splice(inp)?;
        state.havoc(inp)?;
        state.havoc_recursion(inp)?;
    }
    InputState::Random => {
        match policy.select_action(&ctx_before) {
            None => {  // DefaultPolicy: run all three
                state.splice(inp)?;
                state.havoc(inp)?;
                state.havoc_recursion(inp)?;
            }
            Some(action) => {  // DqnPolicy: run ONE selected strategy
                match action {
                    0 => state.havoc(inp)?,
                    1 => state.havoc_recursion(inp)?,
                    2 => state.splice(inp)?,
                    3 => state.deterministic_tree_mutation(inp, 0, 1)?,
                    4 => state.generate_random("START")?,
                }
            }
        }
    }
}
```

**Key differences:**
1. **No `detafl` state.** The paper has a dedicated AFL mutation stage (bit flips, arithmetic, interesting values on the unparsed string). RL-Nautilus **removed AFL mutations entirely**. This is significant — the paper found that AFL mutations discover parser bugs that grammar mutations miss (Example IV.5: `1 + 2` -> `1xf`).
2. **RL skip of Det.** When `rl_enabled`, inputs go directly from Init to Random, skipping deterministic rule enumeration. The DQN can still select Det as action=3, but it's one strategy among 5 rather than an exhaustive phase.
3. **RL single-strategy selection.** In Random state with DqnPolicy, only ONE strategy runs per round instead of all three (splice + havoc + havoc_rec). This is the core RL intervention — choosing which strategy to invest time in.

---

### STEP 11: Mutation (the heart of the fuzzer)

**Paper (Section IV-C) — 6 mutation methods:**

| Method | Paper description | How it works |
|--------|------------------|--------------|
| **Random Mutation** | Pick random node, replace subtree with newly generated one of same NT | Same NT, random size |
| **Rules Mutation** | For each node, try ALL alternative rules for that NT | Exhaustive, deterministic |
| **Random Recursive Mutation** | Find recursive NT (e.g., EXPR -> ... EXPR), replicate recursion 2^n times (1<=n<=15) | Creates deeply nested trees |
| **Splicing Mutation** | Replace random subtree with a "fitting" subtree from another queue item | Cross-pollinates interesting fragments |
| **AFL Mutation** | Unparse subtree to string, apply bit flips/arithmetic/interesting values, store as Custom Rule | **Generates invalid grammar trees** — can find parser bugs |
| **Subtree/Recursive Minimization** | Shrink tree while preserving coverage bits | Not a mutation per se — a minimization |

**RL-Nautilus code — 5 mutation methods (mapped to DQN actions):**

| Action | Method | Code location | Iterations | Paper equivalent |
|--------|--------|--------------|------------|-----------------|
| 0 | **Havoc** | `mutator.rs:177 mut_random` | 100 | Random Mutation |
| 1 | **HavocRec** | `mutator.rs:197 mut_random_recursion` | 20 | Random Recursive Mutation |
| 2 | **Splice** | `mutator.rs:136 mut_splice` | 100 | Splicing Mutation |
| 3 | **Det** | `mutator.rs:103 mut_rules` | all alts | Rules Mutation |
| 4 | **Generate** | `state.rs:191` | 1 | Fresh generation (not in paper as mutation) |

**What's missing from the paper:**
- **AFL Mutation is completely removed.** No bit flips, no arithmetic mutations, no interesting values. The paper's Example IV.5 shows this creating `EXPR -> "1xf"` (a Custom Rule) — this cannot happen in RL-Nautilus. The paper found this method discovered the PHP stack overflow and 2 mruby CVEs (CVE-2018-10191, CVE-2018-12248) that no other method found (Fig. 6).
- **Generate is added as action=4.** The paper treats generation as a separate phase (initial batch of 1000), not as a mutation strategy. RL-Nautilus allows the DQN to choose "generate fresh" as an alternative to mutating an existing queue item.

---

### STEP 12: RL Feedback Loop (NOT IN PAPER)

This is entirely new in RL-Nautilus. After each mutation round in Random state:

```rust
// Before mutation: snapshot coverage state
let (bits_before, crashes_before, ...) = {
    let gs = global_state.lock();
    (total_bits, total_crashes, queue_size, total_coverage)
};

// Build PolicyContext for DQN
let ctx_before = PolicyContext {
    coverage_delta: 0, is_crash: false, total_coverage, exec_count, queue_size, ...
};

// DQN selects action (epsilon-greedy)
let action = policy.select_action(&ctx_before);  // 0-4

// Execute selected strategy
match action { 0 => havoc, 1 => havoc_rec, 2 => splice, 3 => det, 4 => generate }

// After mutation: compute reward signal
let coverage_delta = bits_after - bits_before;
let is_crash = crashes_after > crashes_before;

// DQN observes outcome
policy.observe(action, &ctx_after);
// Inside observe():
//   reward = coverage_delta + 10*is_crash - 1*is_timeout - 0.1*(no_progress)
//   replay_buffer.push(state, action, reward, next_state)
//   every 100 steps: train_step() (batch of 32 from replay buffer)
//   every 1000 train steps: sync online -> target network
//   epsilon decays: 1.0 -> 0.05 over 50,000 steps
```

The DQN state (12 dimensions):
```
[coverage_delta, total_coverage, coverage_velocity,
 is_crash, crash_rate, queue_size_norm, exec_count_norm,
 havoc_ema, havocrec_ema, splice_ema, det_ema, generate_ema]
```

---

## Summary: Paper vs Code Delta

| Aspect | Paper (NDSS'19) | RL-Nautilus (phase-2) | Impact |
|--------|----------------|----------------------|--------|
| Grammar format | JSON/ANTLR | Python DSL (PyO3) | More expressive, supports weights |
| Generation | Naive + Uniform | **Weighted** (loaded_dice) | CVE patterns sampled more often |
| Bitmap size | 64KB | 256KB | 4x more edge resolution |
| Fork server | AFL 2.x | AFL++ 4.x (XOR handshake) | Modern compatibility |
| Determinism check | None | 5x re-run | Filters non-deterministic bits (6x cost) |
| Oracle | Crash/Normal | ASan/UBSan/Signal/Timeout with per-strategy stats | Rich crash classification |
| State machine | init->det->detafl->random | init->det->random (or init->random if RL) | Simpler, no detafl |
| AFL mutation | Yes (bit flips, arithmetic) | **Removed entirely** | Loses ability to find parser bugs via invalid grammar |
| RL policy | None | DQN (12-dim state, 5 actions, epsilon-greedy) | **Never tested** (rl_enabled=false) |
| Strategy selection | Fixed pipeline (all run) | DQN picks ONE per round | Potential efficiency gain |
| Mutation budget | Run all strategies on each item | RL selects one | Trade-off: depth vs breadth |
| Fresh generation | Separate phase (1000 initial) | DQN action=4 (ongoing) | RL can re-inject fresh inputs |
| ChunkStore | Populated after minimize | Same | Splice source — identical |
| Logging | None mentioned | exec.log + rl_metrics.csv | Enables post-hoc analysis |
| Triage | Not in fuzzer | stack_dedup, fidelity_score, cve_signatures, report | Full CVE attribution pipeline |

### The 3 Most Significant Deltas

1. **Weighted grammar sampling** replaces uniform generation — the core thesis hypothesis, but ablation showed it doesn't help at 15-min horizon (patterns = uniform for RC count).

2. **AFL mutations removed** — the paper explicitly showed AFL mutations find bugs that grammar mutations miss (PHP stack overflow, 2 mruby CVEs). Removing them narrows the bug-finding surface. This was likely done to simplify the DQN action space to 5 clean grammar-aware strategies.

3. **DQN strategy selection** replaces the fixed "run all strategies" pipeline — the core RL contribution, but it has never been activated (`rl_enabled: false` in all experiments).
