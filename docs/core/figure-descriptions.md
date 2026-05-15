# Figure Descriptions for Chapter 3

Official reference for thesis figures. Based on source code analysis (2026-05-15).

---

## Figure 3.1: System Architecture Overview

**Components (from source code):**

1. **Grammar** (external input) — Python script (`.py` file) defining weighted production rules via `ctx.rule(nt, format, weight)`. Loaded by `python_grammar_loader::load_python_grammar()`.

2. **Context** (grammar engine) — `grammartec/src/context.rs::Context`. Stores all `Rule`s, NT→Rule mappings, weight tables. Performs weighted random rule selection via `get_random_rule_for_nt()`. Thread-local copy per fuzzing thread.

3. **Tree Generation** — `Context::generate_tree_from_nt("START", max_len)` → builds a `Tree` (pre-order DFS rule sequence) by recursively expanding NTs with weighted sampling.

4. **Mutation** — `grammartec/src/mutator.rs::Mutator`. Four operations:
   - `mut_splice` — replaces subtree with stored chunk from ChunkStore (same NT, different rule)
   - `mut_random` (havoc) — regenerates random subtree
   - `mut_random_recursion` — unrolls recursive NT pairs 2-1024×
   - `mut_rules` (deterministic) — tries every alternative rule for each node

5. **Minimization** — `minimize_tree` + `minimize_rec`. Shrinks each subtree to minimum derivation preserving fresh coverage bits. Only runs on newly discovered inputs (state `Init`).

6. **ChunkStore** — `grammartec/src/chunkstore.rs`. Stores minimized subtrees (size ≤ 30 nodes) indexed by NT. Fed exclusively from minimized trees. Used by `mut_splice` to find alternative subtrees.

7. **Queue** — `fuzzer/src/queue.rs::Queue`. Stores `QueueItem`s (tree + fresh_bits + bitmap + exit_reason + state). State machine per item: `Init → Det → Random`. `pop()` returns next item; `add()` only accepts inputs with genuinely new edges.

8. **Fuzzer** — `fuzzer/src/fuzzer.rs::Fuzzer`. One per thread. Owns a `ForkServer`. Core method `exec()`: unparses tree → writes to temp file → fork server runs target → reads SHM bitmap → compares against global bitmap → if new bits, adds to queue.

9. **ForkServer** — `forksrv/src/lib.rs::ForkServer`. AFL fork protocol over fds 198/199. Creates SHM bitmap (`shmget`), shares via `__AFL_SHM_ID` env var. Each `run()`: zeros bitmap → writes input to temp file → signals fork server → reads exit status.

10. **Instrumented SQLite** (external target) — Compiled with ASan (`exitcode=223`) + UBSan (`exitcode=1`). Reads SQL from stdin via AFL fork protocol.

11. **Global Shared State** — `shared_state.rs::GlobalSharedState`. `Arc<Mutex<>>`. Contains queue, accumulated bitmaps (normal + crash), crash counters. Status thread writes `coverage.csv` every second.

12. **Triage Pipeline** (post-campaign, external Python) — `triage/classify.py` + `triage/stack_dedup.py`. Replays crashes through test harness, stack-hash dedup, CVE signature matching.

**Fuzzing loop (per thread):**

```
loop {
  item = queue.pop()
  if item exists:
    match item.state:
      Init    → minimize (200 nodes/batch)
      Det     → deterministic mutations + splice×100 + havoc×100 + havoc_rec×20
      Random  → splice×100 + havoc×100 + havoc_rec×20
    queue.finished(item)
  else (queue empty):
    generate 1000 fresh inputs from grammar
    queue.new_round()  // recycle processed items
}
```

**Data flow:**

- Grammar `.py` → `load_python_grammar()` → `Context` (rules + weights)
- `Context` → `generate_tree_from_nt()` → `Tree`
- `Tree` → `unparse_to_vec()` → SQL bytes
- SQL bytes → `ForkServer::run()` → exit status + SHM bitmap
- Bitmap → `Fuzzer::new_bits()` → compare against `GlobalSharedState.bitmaps`
- New edges → `Queue::add()` → item enters at `Init(0)`
- `Init` → minimize → `ChunkStore::add_tree()` → `Det`
- `Det`/`Random` → `Mutator` operations → new `TreeMutation`s → `Fuzzer::exec()`
- Crashes → `outputs/signaled/` → post-campaign triage

---

## Figure 3.2: Two-Layer Grammar Architecture

**Start symbol:** `START` → `Sql-Stmt-List` → one or more `Sql-Stmt`

**Sql-Stmt composition:**

```
Sql-Stmt → Schema-Setup ; Insert-Data ; Stress-Query
Sql-Stmt → Schema-Setup ; Insert-Data ; Stress-Query ; Validation-Op
Sql-Stmt → Schema-Setup ; Insert-Data ; Boundary-Func-Call
```

Schema-Setup and a query are always present. Validation-Op and Boundary-Func-Call are alternative third components.

**Layer 2 — Composed Shapes:**

| Non-terminal | Alternatives | Weight range | Purpose |
|---|---|---|---|
| `Schema-Setup` | S1-S6 (6 rules) | 0.5 - 3.0 | Database schema construction |
| `Stress-Query` | Q1-Q8 (8 rules) | 2.0 - 3.0 | Complex query patterns |
| `Validation-Op` | V1-V4 (4 rules) | 1.0 - 2.0 | Integrity/consistency checks |
| `Boundary-Func-Call` | B1-B3 (3 rules) | 1.5 - 3.0 | Boundary value function calls |

**Layer 1 — SQL Atoms (30+ non-terminals):**

`Expr`, `Table-Name`, `Col-Def`, `Col-Name`, `Col-Def-List`, `Col-Def-List-GenCol`, `Func-Call`, `Join-Clause`, `Window-Func`, `Window-Frame`, `Literal`, `Select-Stmt`, `Result-Col-List`, `Compound-Op`, `Format-Spec`, `Boundary-Int`, `Boundary-Float`, `Fts-Engine`, `Json-Key`, `Json-Path`, `Json-Literal`, ...

**Composition:**

- Sql-Stmt → Layer 2 shapes → Layer 1 atoms → terminals
- Solid arrows: required composition (Schema-Setup, Stress-Query)
- Dashed arrows: optional composition (Validation-Op, Boundary-Func-Call)
- Each Layer 2 shape references specific Layer 1 atoms
