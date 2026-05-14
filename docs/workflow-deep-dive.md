# Workflow Deep Dive — RL-Nautilus Fuzzer

Operational reference for the project owner. Describes what happens step-by-step
when the fuzzer runs, with references to actual source file paths and line numbers.

---

## 1. Campaign Lifecycle

Entry point: `scripts/run_eval.sh <sqlite_version> [run_id]`

**Step 1 — Resolve paths.**
The script computes `ROOT` (repo root) and checks that the harness binary at
`$ROOT/harness/afl/sqlite_harness_${VERSION}` exists. If it does not, it
prints the `make` command needed to build it and exits.

**Step 2 — Write `config.ron`.**
A `config.ron` is written to `$WORKDIR/${VERSION}_${RUN_ID}/config.ron`
(`run_eval.sh` lines 73–89). Key values templated from env vars:

```
Config(
    path_to_bin_target: "<harness binary>",
    arguments: ["@@"],
    path_to_grammar: "<grammar>",
    path_to_workdir: "<workdir>",
    number_of_threads: $THREADS,
    timeout_in_millis: $TIMEOUT_MS,
    bitmap_size: 2097152,           # 2 MiB
    thread_size: 4194304,           # 4 MiB stack per thread
    number_of_generate_inputs: 1000,
    max_tree_size: $MAX_TREE_SIZE,
    number_of_deterministic_mutations: 1,
)
```

**Step 3 — Set environment variables.**
`run_eval.sh` lines 101–104 export:
- `ASAN_OPTIONS=exitcode=223,abort_on_error=1,detect_leaks=0`
- `UBSAN_OPTIONS=halt_on_error=1,exitcode=1`
- `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1`
- `LD_LIBRARY_PATH` (linuxbrew lib path for Python shared objects)

**Step 4 — Launch the fuzzer.**
`timeout "$DURATION" ./target/release/fuzzer -c "$CONFIG" [--policy $POLICY]`
(`run_eval.sh` lines 114–120). The `--policy` flag accepts `uniform` or `bandit`; omitting it defaults to `uniform`.

**Step 5 — Workdir structure created by `main.rs`.**
`main.rs` lines 476–485 create four subdirectories under `$WORKDIR`:

| Path | Contents |
|------|----------|
| `outputs/signaled/` | ASAN, UBSan, and signal crashes |
| `outputs/queue/` | All queue entries (raw SQL text, named by id and ExitReason) |
| `outputs/timeout/` | Timed-out inputs |
| `outputs/chunks/` | Chunkstore serialisation (used by Splice) |

**Step 6 — Post-run triage.**
After the fuzzer exits, `run_eval.sh` lines 139–173 run in sequence:
1. `scripts/capture_coverage.py` — writes `$WORKDIR/coverage.json`.
2. `triage/classify.py` — classifies and deduplicates crashes; writes
   `$WORKDIR/triage.json` and `$WORKDIR/triage_report.md`.
3. `scripts/archive_campaign.sh` — (only when `$GRAMMAR_VERSION` is set)
   copies results to `results/campaigns/`.

---

## 2. Execution Loop

`main.rs` spawns `config.number_of_threads` threads, each running
`fuzzing_thread()` (lines 179–347). Each thread owns one `ForkServer`
instance and one `FuzzingState`.

**Per-iteration logic (`fuzzing_thread` main loop, lines 232–346):**

```
loop {
    inp = global_state.queue.pop()            // queue.rs:130
    if inp is Some:
        process_input(state, inp, config, policy)   // main.rs:51
        global_state.queue.finished(inp)      // queue.rs:155
    else:
        for _ in 0..number_of_generate_inputs:
            state.generate_random("START")    // state.rs:191
        global_state.queue.new_round()        // queue.rs:192

    // Bandit weight update (if policy=bandit): every UPDATE_INTERVAL=100 execs
    if bandit is Some && exec_count >= last_bandit_exec + 100:
        bandit.observe_reward(cov_delta, crash_delta)
        mults = bandit.select_group()
        apply_multipliers(state.ctx, bandit, mults)

    // Aggregate per-thread counters into global_state
}
```

**`process_input` state machine (`main.rs` lines 51–177):**

| `InputState` | Action |
|---|---|
| `Init(start)` | `state.minimize(inp, start, start+200)` → on complete: advance to `Det` or `Random` |
| `Det((cycle, start))` | `state.deterministic_tree_mutation(inp, start, start+1)` then `splice` + `havoc` + `havoc_recursion` |
| `Random` | `policy.select_action()` → dispatch to one or all mutation strategies |

**Call chain from `run_on_with_dedup` down to the fork server:**

```
FuzzingState::havoc / splice / det / generate_random
  └─ Fuzzer::run_on_with_dedup(tree, exec_reason, ctx)   fuzzer.rs:170
       ├─ input_is_known(code)                             fuzzer.rs:347
       └─ Fuzzer::run_on(code, tree, exec_reason, ctx)    fuzzer.rs:194
            └─ Fuzzer::exec(code, tree, ctx, strategy)    fuzzer.rs:365
                 └─ Fuzzer::exec_raw(code)                fuzzer.rs:332
                      └─ ForkServer::run(data)            forksrv/src/lib.rs:192
```

---

## 3. Exit Code Classification

`ExitReason` is defined in `forksrv/src/exitreason.rs` lines 7–12.
`ExitReason::from_wait_status()` (lines 15–22) converts the raw POSIX
`WaitStatus` returned by the fork server into one of four variants.

| ExitReason variant | Condition | `is_crash` | Action in `run_on` | Output path |
|----|----|----|----|----|
| `Normal(223)` | ASan exit code (set by `ASAN_OPTIONS=exitcode=223`) | true | Saved if `new_bits.is_some()`, increments `total_found_asan` | `outputs/signaled/ASAN_{exec_count}_{thread}` |
| `Normal(1)` | UBSan exit code (set by `UBSAN_OPTIONS=exitcode=1`) | true | Saved if `new_bits.is_some()`, increments `total_found_ubsan` | `outputs/signaled/UBSAN_{exec_count}_{thread}` |
| `Normal(n)` (other) | Clean exit | false | Increments `bits_found_by_*` attribution counter if new path found | (none) |
| `Timeouted` | `st_out.read_i32()` times out; process killed with SIGKILL | false | Always saved regardless of new bits; increments timeout log | `outputs/timeout/{exec_count}` |
| `Signaled(sig)` | Process killed by a UNIX signal (e.g., SIGABRT=6 for assert) | true | Saved if `new_bits.is_some()`, increments `total_found_sig` | `outputs/signaled/{sig}_{exec_count}` |
| `Stopped(sig)` | Process stopped (rare; ptrace) | false | Silently ignored (`fuzzer.rs:307`) | (none) |

The `is_crash` flag determines which of the two global bitmaps is compared
against — see Section 4.

**Exec log** (`fuzzer.rs` lines 48–92): every crash, timeout, and new-coverage
event is appended to `$WORKDIR/exec.log` as a tab-separated line:
`exec_count TAB label TAB rule_tag TAB sql_snippet`. The log rotates
(truncates and restarts) at 10 MiB (`EXEC_LOG_SIZE_LIMIT`, line 48).

---

## 4. Coverage Bitmap

**Shared memory allocation** (`forksrv/src/lib.rs` lines 242–268).
`ForkServer::create_shm(bitmap_size)` calls `shmget(IPC_PRIVATE, bitmap_size, ...)`
and `shmat()` to map the segment. The segment ID is passed to the child via
`__AFL_SHM_ID` in the environment. Each byte is an edge-hit counter (AFL
semantics: byte at index `src_id XOR (dst_id >> 1)` is incremented on each
branch transition).

**Default size**: `bitmap_size: 65536` (1 << 16 = 64 KiB) in the root
`config.ron`; campaigns set `bitmap_size: 2097152` (2 MiB = 1 << 21) via
`run_eval.sh` line 83. Pass `AFL_MAP_SIZE=<n>` to tell the AFL++ runtime to
use the same size.

**Dual bitmaps** (`shared_state.rs` lines 40–42):
`GlobalSharedState` holds a `HashMap<bool, Vec<u8>>` initialised with two
zero-filled `Vec<u8>` of length `bitmap_size`:
- key `false` — coverage map for non-crashing executions
- key `true` — coverage map for crashing executions

**`new_bits()` detection** (`fuzzer.rs` lines 453–475):

```rust
pub fn new_bits(&mut self, is_crash: bool) -> Option<Vec<usize>> {
    let run_bitmap = self.forksrv.get_shared();
    let shared_bitmap = gstate_lock.bitmaps.get_mut(&is_crash);
    for (i, elem) in shared_bitmap.iter_mut().enumerate() {
        if (run_bitmap[i] != 0) && (*elem == 0) {
            *elem |= run_bitmap[i];
            res.push(i);
        }
    }
    if res.len() > 0 { Some(res) } else { None }
}
```

A bit position is "new" if the corresponding byte in the per-run bitmap is
non-zero while the global shared bitmap byte is still zero. On first discovery
the global byte is updated (`|=`), so subsequent identical paths do not
produce new bits. The function returns `None` (no interesting path) when
every active bit has been seen before.

The `bitmap_size` must match between the fuzzer and the harness (set by
`AFL_MAP_SIZE` env var and harness compile-time `MAP_SIZE`). Mismatches
cause false-positive new-bit detection.

---

## 5. Deterministic Validation

After `new_bits()` returns `Some(bits)` (and the exit reason is not a
timeout), `exec()` in `fuzzer.rs` runs five additional re-executions of the
same input to weed out non-deterministic edge hits:

**`check_deterministic_behaviour`** (`fuzzer.rs` lines 434–451):

```rust
fn check_deterministic_behaviour(
    &mut self,
    old_bitmap: &[u8],  // snapshot of shared bitmap before re-runs
    new_bits: &mut Vec<usize>,
    code: &[u8],
) -> Result<(), SubprocessError> {
    for _ in 0..5 {
        self.exec_raw(code)?;                             // re-execute
        let run_bitmap = self.forksrv.get_shared();
        new_bits.retain(|&i| run_bitmap[i] != 0);        // drop flaky bits
    }
}
```

A bit is retained only if it appears in **all five** re-runs
(`new_bits.retain(|&i| run_bitmap[i] != 0)`). Bits that fail any single run
are removed. If `new_bits` is empty after filtering, the input is discarded
(no queue entry). This costs 5× extra executions per genuinely new path but
prevents the queue from filling with jitter-induced entries.

The validated bitmap snapshot (`old_bitmap = forksrv.get_shared().to_vec()`)
is passed to `Queue::add()` as `all_bits` for the new `QueueItem`
(`fuzzer.rs` line 426).

---

## 6. Mutation Strategies

**`ExecutionReason` enum** (`fuzzer.rs` lines 23–31):

| Variant | `FuzzingState` method | Iterations | Mutation type |
|---|---|---|---|
| `Gen` | `generate_random("START")` | 1 per call | Fresh tree from grammar, weighted sampling |
| `Min` | `minimize()` via `mutator.minimize_tree()` | batch of 200 nodes | Shrink tree while preserving coverage bits |
| `MinRec` | `minimize()` via `mutator.minimize_rec()` | batch of 200 nodes | Recursive subtree shrink |
| `Det` | `deterministic_tree_mutation()` via `mutator.mut_rules()` | 1 node per call | Enumerate all alternative rules at each node |
| `Havoc` | `havoc()` via `mutator.mut_random()` | 100 per call | Random rule replacement anywhere in tree |
| `HavocRec` | `havoc_recursion()` via `mutator.mut_random_recursion()` | 20 per call | Recursive expansion of detected back-edges |
| `Splice` | `splice()` via `mutator.mut_splice()` | 100 per call | Graft a subtree from the chunkstore into the tree |

**Attribution counters** (`fuzzer.rs` fields lines 103–118, flushed in
`main.rs` lines 318–346): each thread tracks `bits_found_by_<strategy>` and
`asan_found_by_<strategy>` locally; they are aggregated into
`GlobalSharedState` on each loop iteration and displayed by the status thread.

**`InputState::Random` dispatch** (`main.rs` lines 90–173):
Runs all three strategies — `splice`, `havoc`, `havoc_recursion` — unconditionally.

**`InputState::Det` phase** (`main.rs` lines 74–88):
Runs deterministic mutations for `config.number_of_deterministic_mutations`
full cycles. Each cycle exhausts all tree nodes one by one (batch size 1).
After each Det step, `splice` + `havoc` + `havoc_recursion` are also run.
When all cycles complete, the item advances to `InputState::Random`.

---

## 7. Input Deduplication

Implemented in `Fuzzer` via two co-operating data structures (`fuzzer.rs`
lines 96–98):

```rust
last_tried_inputs: HashSet<Vec<u8>>,           // O(1) membership test
last_inputs_ring_buffer: VecDeque<Vec<u8>>,    // eviction order
```

**`input_is_known(code)`** (`fuzzer.rs` lines 347–363):
1. If `code` is in `last_tried_inputs`, return `true` immediately (duplicate).
2. Otherwise insert `code` into the `HashSet`.
3. If the ring buffer is at capacity (10,000 entries), pop the oldest entry
   from the back and remove it from the `HashSet`.
4. Push `code` to the front of the ring buffer.
5. Return `false` (novel input).

This gives an effective deduplication window of 10,000 inputs. Inputs further
back than 10,000 executions are forgotten and may re-enter the pipeline. The
dedup is **per-thread** — identical inputs generated by two different threads
can both reach `exec_raw`.

`run_on_with_dedup` (`fuzzer.rs` lines 170–182) is the only entry point that
checks dedup. `run_on_without_dedup` (`fuzzer.rs` lines 184–192) bypasses the
check and is used by `has_bits()` during minimization re-runs, where we
deliberately re-execute known inputs to check coverage.

---

## 8. Queue Management

**`QueueItem` structure** (`queue.rs` lines 23–33):

| Field | Type | Purpose |
|---|---|---|
| `id` | `usize` | Monotonically increasing ID (wraps at `usize::MAX`) |
| `tree` | `Tree` | Grammar derivation tree for this input |
| `fresh_bits` | `HashSet<usize>` | Bitmap indices first seen by this input |
| `all_bits` | `Vec<u8>` | Full bitmap snapshot at time of discovery |
| `exitreason` | `ExitReason` | Why execution ended |
| `state` | `InputState` | Current processing stage (Init/Det/Random) |
| `recursions` | `Option<Vec<RecursionInfo>>` | Detected tree back-edges (populated after minimization) |
| `execution_time` | `u32` | Nanoseconds for the first execution |

New items start in `InputState::Init(0)` (`queue.rs` line 49`).

**`Queue::add()`** (`queue.rs` lines 65–118):
1. Check whether all non-zero bits in `all_bits` are already in
   `bit_to_inputs`. If so, the input is subsumed — skip it (early exit at
   line 76–79).
2. Identify `fresh_bits`: indices where `all_bits[i] != 0` and
   `bit_to_inputs` does not yet contain `i`.
3. Update `bit_to_inputs[i].push(current_id)` for every active bit.
4. Write the unparsed SQL text to
   `$WORKDIR/outputs/queue/id:{id:09},er:{exitreason}`.
5. Push a new `QueueItem` onto `inputs`.

**`bit_to_inputs` reverse index** (`queue.rs` field line 59):
`HashMap<usize, Vec<usize>>` maps each bitmap bit position to the list of
queue item IDs that cover it. Used by `pop()` (lines 130–153) to clean up
stale references: when an item is popped for processing, its ID is removed
from every bit's coverage list; if a list becomes empty, the bit key itself
is removed.

**`Queue::finished()`** (`queue.rs` lines 155–186):
If after processing, all of the item's bits are already covered by other items
(`bit_to_inputs` contains all its active bits), the item's on-disk file is
deleted and the item is dropped. Otherwise the item is moved to the `processed`
list and the `bit_to_inputs` mapping is rebuilt for it.

**`Queue::new_round()`** (`queue.rs` lines 192–194):
Appends `processed` back onto `inputs` for the next round.
Called when `inputs` is empty (the thread has no work to pop).

**File naming convention:**

| Stage | Filename pattern | Example |
|---|---|---|
| Initial discovery | `id:{id:09},er:{exitreason}` | `id:000000042,er:Normal(0)` |
| After minimization | `id:{id:09},er:{exitreason}.min` | `id:000000042,er:Normal(0).min` |

The `.min` suffix is written by `state.rs` line 98 after minimization
completes; the original file is not explicitly deleted — it is superseded.

---

## 9. Grammar Bandit

Implemented in `fuzzer/src/grammar_bandit.rs`. Activated via `--policy bandit`
(or `config.policy = "bandit"`). One `GrammarBandit` is shared across all
threads behind `Arc<Mutex<GrammarBandit>>`.

**Rule groups** (`grammar_bandit.rs` lines 24–78):
Six semantic groups of grammar non-terminals are hardcoded:

| Index | `RuleGroup` variant | Non-terminals covered |
|---|---|---|
| 0 | `S1SchemaSetup` | `Schema-Setup`, `Create-Table-Stmt`, `Create-Index-Stmt`, `Create-View-Stmt`, `Create-Virtual-Table-Stmt`, `Create-Trigger-Stmt`, `Alter-Table-Stmt`, `Drop-Stmt`, `Col-Def-List-GenCol` |
| 1 | `S2DmlStress` | `Insert-Stmt`, `Update-Stmt`, `Delete-Stmt` |
| 2 | `S3QueryStress` | `Stress-Query`, `Select-Stmt`, `Select-Core` |
| 3 | `S4BoundaryPrintf` | `Boundary-Func-Call`, `Boundary-Int`, `Boundary-Float`, `Format-Spec`, `Printf-Fmt-Spec` |
| 4 | `S5FtsVirtual` | `Fts-Engine` |
| 5 | `S6Validation` | `Validation-Op`, `Pragma-Stmt`, `Analyze-Stmt` |

Non-terminals not in any group are unaffected by the bandit.

**Thompson Sampling (`select_group()`)** (`grammar_bandit.rs` lines 162–196):

Each group maintains Beta distribution parameters `(alpha, beta)`, initialised
to `(1.0, 1.0)` (uninformative uniform prior). On each call:

1. For each group sample `θ_i ~ Beta(alpha_i, beta_i)`.
2. Select the group with the highest sample: `best_group = argmax θ_i`.
3. Decay all current multipliers toward 1.0:
   `m_i = 1.0 + (m_i - 1.0) * DECAY_FACTOR` where `DECAY_FACTOR = 0.95`.
4. Boost selected group: `m[best] = clamp(m[best] * BOOST_MULTIPLIER, 0.01, 100.0)`
   where `BOOST_MULTIPLIER = 2.0`.
5. Increment `selection_count[best_group]` and `total_updates`.

**Reward and Beta update (`observe_reward()`)** (`grammar_bandit.rs` lines
199–218):

Called every `UPDATE_INTERVAL = 100` executions (main.rs lines 287–309) with:
- `coverage_delta` = new coverage edges seen since last update
- `crash_delta` = new crashes seen since last update

```
raw_reward = coverage_delta + 10.0 * crash_delta
reward_ema = 0.1 * raw_reward + 0.9 * reward_ema   // EMA alpha = 0.1

if reward_ema > 0.1:
    normalized = min(raw_reward / reward_ema, 2.0)
else:
    normalized = 1.0 if raw_reward > 0.0 else 0.0

alpha[active_group] += normalized
if raw_reward == 0.0:
    beta[active_group] += 1.0
```

The EMA baseline prevents reward inflation: a group must beat the running
average to earn `normalized > 1.0`. Crashes are weighted 10× heavier than
coverage edges.

**Applying multipliers to threads (`apply_multipliers()`)** (`grammar_bandit.rs`
lines 261–269):
Each thread re-applies multipliers from scratch on each bandit update:
`new_weight = clamp(base_weight * multiplier, 0.01, 100.0)`.
Using `base_weight` (stored at startup) prevents compounding.

**Logging**: every bandit update writes a CSV row to `$WORKDIR/bandit_log.csv`
with columns: `update, selected_group, alpha_*, beta_*, count_*, last_reward_*,
reward_ema, total_coverage` (`grammar_bandit.rs` lines 221–235).

---

## 10. Configuration Reference

All fields are defined in `fuzzer/src/config.rs`. Fields marked with
`#[serde(default)]` are optional in `config.ron` and backward-compatible with
configs that predate Phase 2.

| Field | Type | Default | Purpose |
|---|---|---|---|
| `path_to_bin_target` | `String` | (required) | Absolute path to the instrumented harness binary |
| `arguments` | `Vec<String>` | (required) | CLI arguments passed to target; `"@@"` is replaced with the path to the temp input file |
| `path_to_grammar` | `String` | (required) | Path to Python (`.py`) or JSON grammar file |
| `path_to_workdir` | `String` | (required) | Existing directory for outputs, logs, and config; must exist before launch |
| `number_of_threads` | `u8` | (required) | Number of parallel fuzzing threads; each thread runs its own fork server |
| `timeout_in_millis` | `u64` | (required) | Per-execution timeout in milliseconds; reads exceeding this trigger `ExitReason::Timeouted` |
| `bitmap_size` | `usize` | (required) | AFL coverage bitmap size in bytes; must match `AFL_MAP_SIZE` and harness `MAP_SIZE`; campaigns use `2097152` (2 MiB) |
| `thread_size` | `usize` | (required) | Stack size per fuzzing thread in bytes; `4194304` = 4 MiB |
| `number_of_generate_inputs` | `u16` | (required) | How many `generate_random("START")` calls per idle round (when queue is empty) |
| `max_tree_size` | `usize` | (required) | Maximum grammar derivation tree node count; caps recursive tree growth |
| `number_of_deterministic_mutations` | `usize` | (required) | Number of full Det cycles (each cycle covers all tree nodes once); `1` is the standard setting |
| `policy` | `String` | `"uniform"` | Grammar weight policy: `"uniform"` (static weights) or `"bandit"` (Thompson Sampling) |

### Configuration quick-start for a standard campaign

```
Config(
    path_to_bin_target: "./harness/afl/sqlite_harness_sqlite-3.31.1",
    arguments: ["@@"],
    path_to_grammar: "./grammars/sqlite.py",
    path_to_workdir: "/tmp/sqlite-3.31.1_run1",
    number_of_threads: 1,
    timeout_in_millis: 500,
    bitmap_size: 2097152,
    thread_size: 4194304,
    number_of_generate_inputs: 1000,
    max_tree_size: 300,
    number_of_deterministic_mutations: 1,
)
```

For a bandit-policy run, add `policy: "bandit"` (no other fields required).
