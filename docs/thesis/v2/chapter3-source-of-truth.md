# Chapter 3: Proposed Method — Source of Truth

> **Purpose:** Complete readable version of what Chapter 3 says. Every claim, every number, every description. Read this to catch errors that automated checking missed. Mark issues inline with `[ISSUE]` tags.
>
> **Verification basis:** GitNexus call graph + direct reading of `grammars/v3.3/sqlite_v3.py`, `grammartec/src/context.rs`, `fuzzer/src/main.rs`, `fuzzer/src/state.rs`, `forksrv/src/lib.rs`, `harness/src/sqlite_harness.c`
>
> **Grammar version:** v3.3 (file: `grammars/v3.3/sqlite_v3.py`, 514 `ctx.rule()` calls)

---

## System Data Flow Diagram (Single Source of Truth for Figure 3.1)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        DBMS-Nautilus Fuzzer Core                           │
│                                                                           │
│  ┌──────────────┐    load_python_grammar()    ┌──────────────────────┐     │
│  │ ① Grammar    │ ──────────────────────────→ │ ② Context            │     │
│  │   (.py file) │    ctx.rule(nt, pattern,    │   (Rule Engine)      │     │
│  │              │     weight) × 514 rules     │   rules: Vec<Rule>   │     │
│  │  sqlite_v3.py│                             │   nts_to_rules: Map  │     │
│  └──────────────┘                             └──────────┬───────────┘     │
│                                                          │                │
│                                    ctx.generate_tree_    │ weighted       │
│                                    from_nt("Sql-Stmt")   │ random         │
│                                                          │ selection      │
│                                                          ▼                │
│                                               ┌──────────────────┐        │
│                                               │ ③ Tree Generation│        │
│                                               │  (Weighted       │        │
│                                               │   Sampling)      │        │
│                                               │  Output: Tree    │        │
│                                               └────────┬─────────┘        │
│                                                        │ tree             │
│                                                        ▼                  │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ ④ Mutation Engine                                                  │    │
│  │                                                                    │    │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐               │    │
│  │  │ mut_rules    │ │ mut_random   │ │mut_random_   │               │    │
│  │  │(deterministic│ │(random sub-  │ │recursion     │               │    │
│  │  │ substitution)│ │ tree regen)  │ │(expand/      │               │    │
│  │  └──────────────┘ └──────────────┘ │collapse)     │               │    │
│  │  ┌──────────────┐ ┌──────────────┐ └──────────────┘               │    │
│  │  │ mut_splice   │ │ havoc        │                                │    │
│  │  │(ChunkStore   │ │(100× random  │                                │    │
│  │  │ subtree)     │ │ subtree)     │                                │    │
│  │  └──────┬───────┘ └──────────────┘                                │    │
│  │         │ reads                                                    │    │
│  └─────────┼──────────────────────────────────────────────────────────┘    │
│            │                                                              │
│            ▼                                                              │
│  ┌──────────────────┐          ┌──────────────────┐                       │
│  │ ⑥ ChunkStore     │◄─────── │ ⑤ Minimization   │                       │
│  │  (subtree index) │  add    │  minimize() +    │                       │
│  │  get_alternative_ │  tree   │  minimize_rec()  │                       │
│  │  to(rule_id)     │         │  shrink tree     │                       │
│  └──────────────────┘         │  preserving bits │                       │
│                               └──────────────────┘                       │
│                                        ▲                                  │
│                                        │ input (Init state)               │
│                                        │                                  │
│  ┌───────────────────────────────────────────────────────────────────┐     │
│  │ ⑦ Queue                                                          │     │
│  │  State machine: Init ──→ Det ──→ Random     [RESOLVED: our customization, original has init→det→detafl→random]     │     │
│  │                                                                   │     │
│  │  Init:   minimize + minimize_rec → add to ChunkStore             │     │
│  │  Det:    mut_rules + splice + havoc + havoc_recursion            │     │
│  │  Random: splice + havoc + havoc_recursion                        │     │
│  │                                                                   │     │
│  │  pop() → process_input() → finished(item)                        │     │
│  │  new_round() when queue empty → generate_random("START")         │     │
│  └──────────────────────────┬────────────────────────────────────────┘     │
│                             │ mutated tree                                │
│                             ▼                                             │
│                   tree.unparse_to_vec(ctx) → SQL bytes                    │
│                             │                                             │
│                             ▼                                             │
│  ┌──────────────────────────────────────────────────┐                     │
│  │ ⑧ Fork Server (forksrv/src/lib.rs)              │                     │
│  │                                                  │                     │
│  │  1. Write SQL to temp file                       │                     │
│  │  2. Send "fork" command via ctl_pipe             │                     │
│  │  3. Child: reads SQL → sqlite3_exec() → exits    │                     │
│  │  4. Parent: reads exit status via st_pipe         │                     │
│  │  5. Read shared memory bitmap (65536 bytes)       │                     │
│  └─────────────────────┬────────────────────────────┘                     │
│                        │ (exit_reason, bitmap)                            │
│                        ▼                                                  │
│  ┌──────────────────────────────────────────────────┐                     │
│  │ ⑨ Fuzzer (Executor, per thread)                  │                     │
│  │    fuzzer/src/fuzzer.rs                           │                     │
│  │                                                  │                     │
│  │  exec() → reads bitmap → new_bits() check:       │                     │
│  │    • Compare run bitmap vs global bitmap          │                     │
│  │    • If new edges found:                          │                     │
│  │        - check_deterministic_behaviour (5 reruns) │                     │
│  │        - queue.add(tree, bitmap, exit_reason)     │ ←── feedback to ⑦  │
│  │                                                  │                     │
│  │  Exit handling:                                   │                     │
│  │    223 → ASan crash → save ASAN_* file           │                     │
│  │    1   → UBSan     → save UBSAN_* file           │                     │
│  │    Sig → Signal    → save to signaled/           │                     │
│  │    Timeout         → save to timeout/            │                     │
│  │    Normal + new bits → add to queue              │                     │
│  └─────────────────────┬────────────────────────────┘                     │
│                        │ new_bits                                         │
│                        ▼                                                  │
│  ┌──────────────────────────────────────────────────┐                     │
│  │ ⑩ Shared State (GlobalSharedState)               │                     │
│  │    fuzzer/src/shared_state.rs                     │                     │
│  │                                                  │                     │
│  │  • bitmaps: HashMap<bool, Vec<u8>>               │                     │
│  │    - false → normal execution bitmap (65536)     │                     │
│  │    - true  → crash execution bitmap              │                     │
│  │  • execution_count, avg_exec/sec                  │                     │
│  │  • bits_found_by_{gen,min,det,splice,havoc,...}   │                     │
│  │  • total_found_{asan,sig,ubsan}                   │                     │
│  │  • queue: Queue (shared across threads)           │                     │
│  └──────────────────────────────────────────────────┘                     │
└─────────────────────────────────────────────────────────────────────────────┘
        │                                           │
        │ instrumented binary                       │ crashes saved to
        ▼                                           │ outputs/signaled/
┌──────────────────────────┐                        ▼
│ ⑪ Instrumented SQLite    │              ┌──────────────────────────┐
│                          │              │ ⑫ Triage Pipeline        │
│  • Compiled with ASan    │              │    (Python, post-campaign)│
│    + UBSan + AFL coverage│              │                          │
│  • harness/src/          │              │  • stack_dedup.py        │
│    sqlite_harness.c      │              │  • cve_signatures.py    │
│  • __AFL_INIT() only     │              │  • fidelity_score.py    │
│  • Empty in-memory DB    │              │  • minimize.py          │
│  • One exec per fork     │              │                          │
└──────────────────────────┘              └──────────────────────────┘
```

### Data Flow Summary (linear path)

```
Grammar (.py)
  → [load] Context (rules + weights)
  → [generate] Tree (weighted random selection from START)
  → [unparse] SQL bytes
  → [write] Temp file
  → [fork] Child process (instrumented SQLite)
  → [exec] sqlite3_exec(SQL)
  → [exit] Exit code (223=ASan, 1=UBSan, Signal, Normal)
  → [read] Shared memory bitmap (65536 bytes)
  → [compare] New bits vs global bitmap
  → [if new] Add tree to Queue → back to mutation loop
  → [if crash] Save to outputs/signaled/ → triage later
```

### Feedback Loop

```
Queue.pop()
  → process_input(item)
    → match item.state:
        Init:   minimize(tree) → add to ChunkStore → state = Det
        Det:    mut_rules + splice + havoc + havoc_rec → state = Random
        Random: splice + havoc + havoc_rec
    → each mutation:
        → unparse → exec → bitmap check
        → new bits? → queue.add(new_tree) as Init(0)
  → Queue.finished(item)

Queue empty?
  → generate_random("START") × N
  → Queue.new_round()
```

### Thread Architecture

```
main()
  ├── load_python_grammar() → Context (shared via clone)
  ├── GlobalSharedState (Arc<Mutex>, shared across threads)
  │     └── Queue, bitmaps, counters
  ├── ChunkStoreWrapper (Arc, shared across threads)
  ├── spawn N fuzzing_thread() instances
  │     Each owns: FuzzingState { ctx (clone), mutator, fuzzer (with ForkServer) }
  │     Each has: own ForkServer → own child process fork
  └── spawn 1 status_thread()
        └── prints stats, writes coverage.csv every second
```

---

## 3.0 Chapter Introduction

**Opening argument:** Byte-level fuzzers fail on database engines because random mutations produce parser-rejected inputs. Grammar-based fuzzers solve syntactic validity but treat all SQL constructs equally. DBMS-Nautilus combines Nautilus-style coverage-guided generation with a domain-specific SQL grammar targeting vulnerability-triggering code paths in SQLite.

**Chapter roadmap:**
- Section 3.1: System overview
- Section 3.2: Grammar design methodology (core contribution)

**Key claim:** "The grammar contains 514 production rules organized into a two-layer architecture, designed through root-cause analysis of known CVEs and guided by experimental feedback from fuzzing campaigns."

> **Verified:** 514 = `grep -c "ctx.rule" grammars/v3.3/sqlite_v3.py`

---

## 3.1 System Overview

### Core description

DBMS-Nautilus = grammar-based greybox fuzzer for database engines. Combines:
- Coverage-guided fuzzing loop from Nautilus
- Domain-specific SQL grammar with weighted production rules

**Key differentiator vs prior work:**
- SQLsmith: random queries against pre-populated database
- Squirrel: internal schema model for semantic validity
- DBMS-Nautilus: grammar generates **self-contained** SQL programs (create schema + insert data + query) starting from **empty in-memory database**

**Self-contained advantage:** Every test case independently reproducible, no external state needed, replay in isolation.

### 12 Components (Figure 3.1)

Components 1–10 = fuzzer core:

| # | Component | Role |
|---|-----------|------|
| 1 | Grammar (.py) | Defines input space |
| 2 | Context (Rule Engine) | Weighted rule selection |
| 3 | Tree Generation | Constructs derivation trees |
| 4 | Mutation Engine | Applies 5 structural mutations |
| 5 | Minimization | Shrinks inputs preserving coverage |
| 6 | ChunkStore | Indexes subtrees for splice |
| 7 | Queue | Manages inputs: Init→Det→Random |
| 8 | Fork Server | AFL protocol execution |
| 9 | Fuzzer (Executor) | Per-thread coordination |
| 10 | Shared State | Global coverage bitmaps, counters |
| 11 | Instrumented SQLite | Target under test (external) |
| 12 | Triage Pipeline | Post-campaign crash analysis (external) |

> **[RESOLVED]** Component 7 Queue state machine (Init→Det→Random): **Confirmed as our customization.** Original Nautilus has 4 states (init→det→detafl→random). We removed `detafl` (AFL byte-level mutations) because they produce parser-invalid SQL. Thesis must explicitly state this modification.

### Grammar Engine

Loads context-free grammar from Python script. Each production rule maps non-terminal → string pattern with terminal symbols and non-terminal references.

**Weighted sampling mechanism:**
- Rules carry numeric weights
- At each expansion: engine selects among applicable rules with **probability proportional to their weights**
- Implementation: linear scan in `context.rs:314-336` (sum weights → random threshold → iterate)

> **Verified:** No "loaded dice" algorithm for rule selection. `LoadedDiceSampler` only used in `recursion_info.rs` for recursion depth bias (separate mechanism).

### Generation and Mutation

**5 structural mutation operators:**

| Operator | Code function | Description |
|----------|--------------|-------------|
| Deterministic substitution | `mut_rules` | Try every alternative rule at each tree node |
| Random subtree | `mut_random` | Pick random node, regenerate subtree from grammar |
| Random recursion | `mut_random_recursion` | **Expand only** — repeat a recursive pair 2^n times (n ∈ [1,11]) |
| Splice | `mut_splice` | Pick random node → find ChunkStore subtree with **same non-terminal** (different rule) → replace |
| Bulk random havoc | `mut_random` ×100 + `mut_random_recursion` ×20 | 100 random subtree replacements + 20 recursion expansions |

> **Verified from code:**
> - `mut_random_recursion` (mutator.rs:197-268): ONLY expands. Picks random recursion pair, repeats it `2^n` times. No collapse logic — collapsing is done by `minimize_rec` (separate).
> - `mut_splice` (mutator.rs:136-153): Matches by **non-terminal** via `ctx.get_nt()`, NOT by rule_id. Filters out chunks with same rule_id (wants different derivation of same NT).
> - `havoc()` (state.rs:131-143): calls `mut_random` in loop of 100.
> - `havoc_recursion()` (state.rs:145-165): calls `mut_random_recursion` in loop of 20.
> - `splice()` (state.rs:167-189): calls `mut_splice` in loop of 100.
> - ChunkStore `add_tree` (chunkstore.rs:51-80): only indexes subtrees with ≤30 nodes (small fragments only).

> **Note on original Nautilus:** The original paper (NDSS'19) defines 5 mutations: Random, Rules, Random Recursive, Splicing, and AFL Mutation. Our implementation drops AFL Mutation (byte-level bit flips/arithmetic) because it produces parser-invalid SQL. We add bulk havoc (100× random subtree) instead. The original paper has a 4-state queue (init→det→detafl→random); we use 3 states (Init→Det→Random) because we removed the `detafl` stage that applied AFL mutations.

#### Mutation Examples (need figures in thesis, like Nautilus paper Examples IV.2–IV.5)

Each example below needs a **tree diagram figure** showing before→after transformation. The original Nautilus paper uses Examples IV.2–IV.5 with derivation tree visualizations. We need equivalent SQL-domain examples.

---

**Example M1: Subtree Minimization** (`minimize`)

Shrink tree while preserving coverage bits. Replace each subtree with smallest possible derivation of same non-terminal.

```
BEFORE tree (input: "SELECT a + b FROM p WHERE a > 1"):

        Sql-Stmt
           |
      Stress-Query
           |
       Select-Stmt
      /     |      \
  Result   FROM    WHERE
  Col-List Table   Expr
    |       |       |
   Expr     p    Expr > Expr
  / + \          |      |
Expr  Expr      Col    Num
 |     |         |      |
Col   Col        a      1
 |     |
 a     b

AFTER minimization (replace Expr "a + b" with minimal Expr "a"):

        Sql-Stmt
           |
      Stress-Query
           |
       Select-Stmt
      /     |      \
  Result   FROM    WHERE
  Col-List Table   Expr
    |       |       |
   Expr     p    Expr > Expr
    |               |      |
   Col             Col    Num
    |               |      |
    a               a      1

Output: "SELECT a FROM p WHERE a > 1"
```

Coverage bits preserved → minimized version replaces original. Smaller tree = faster mutations later.

---

**Example M2: Deterministic Rule Substitution** (`mut_rules`)

At each node, systematically try every alternative production rule for that non-terminal.

```
Input tree derives: "SELECT a FROM p WHERE a > 1"

Node targeted: Expr (the "a > 1" comparison)
Non-terminal: Expr
Alternative rules for Expr include:
  - Expr → Col                    (column reference)
  - Expr → Expr + Expr            (arithmetic)
  - Expr → Expr AND Expr          (logical)
  - Expr → Func-Call              (function call)
  - Expr → (Select-Stmt)          (subquery)
  - ... (30+ alternatives)

Mutation tries EACH alternative:
  Try 1: "SELECT a FROM p WHERE a"           (Expr → Col)
  Try 2: "SELECT a FROM p WHERE a + b"       (Expr → Expr + Expr)
  Try 3: "SELECT a FROM p WHERE a AND b > 0" (Expr → Expr AND Expr)
  Try 4: "SELECT a FROM p WHERE coalesce(a)"  (Expr → Func-Call)
  ...each executed against SQLite, coverage checked
```

This is deterministic and exhaustive — every rule alternative is tried exactly once per node.

---

**Example M3: Random Subtree Regeneration** (`mut_random`)

Pick a random node, regenerate its entire subtree from the grammar.

```
Input: "SELECT a FROM p WHERE a > 1"

Random node selected: WHERE clause's Expr node
Non-terminal at that node: Expr

Grammar regenerates a fresh Expr subtree:
  New Expr → Expr IN (Select-Stmt)
           → Col IN (SELECT Col FROM Table-Name)
           → a IN (SELECT b FROM q)

RESULT: "SELECT a FROM p WHERE a IN (SELECT b FROM q)"
```

The new subtree is completely fresh — may produce SQL patterns the fuzzer hasn't tried before.

---

**Example M4: Random Recursive Mutation** (`mut_random_recursion`)

Find a recursive non-terminal (one that can derive itself) and **expand** it by repeating the recursive pattern 2^n times (n randomly chosen from [1,11]).

> **Important:** This mutation ONLY expands. It does NOT collapse. Collapsing recursion is done by `minimize_rec` during the minimization phase (Example M1), not during mutation.

```
Input: "SELECT a + b FROM p"

Recursive non-terminal found: Expr (rule: Expr → Expr + Expr)
The recursion pair is: parent Expr (at "a + b") and child Expr (at "b")
The "pre" part is: Expr → Expr + [child]
Repeat this pre-part 2 times (2^1):

BEFORE:                    AFTER:
    Expr                      Expr
   / + \                    / + \
 Expr  Expr               Expr   Expr
  |     |                / + \     |
 Col   Col             Expr  Expr  Col
  |     |               |   / + \   |
  a     b              Col Expr Expr b
                        |    |    |
                        a   Col  Col
                             |    |
                             a    b

Output: "SELECT a + a + b + b FROM p"
(exact output depends on which child subtree is the recursion endpoint)
```

Higher values of n (up to 2^11 = 2048) create extremely deep nested expressions, stressing stack depth and recursion limits in SQLite's parser and evaluator.

---

**Example M5: Splice Mutation** (`mut_splice`)

Pick a random node, look up its **non-terminal** in the ChunkStore, find a subtree with the **same non-terminal but different rule**, and replace. ChunkStore only stores subtrees ≤30 nodes (small fragments from minimized interesting inputs).

```
Current input: "SELECT a FROM p WHERE a > 1"
ChunkStore contains subtree from previous interesting input:
  Non-terminal: Expr
  Subtree: "printf('%.*g', 2147483647, 0.01)"  (≤30 nodes, from minimized input)

Random node selected: Expr node at "a > 1"
Splice lookup: get_alternative_to(rule_id_of_current_Expr)
  → finds Expr chunks with DIFFERENT rule_id (wants different derivation)
  → selects printf subtree (Expr→Func-Call, different from Expr→Expr>Expr)

BEFORE:                              AFTER:
   Select-Stmt                         Select-Stmt
  /     |      \                      /     |      \
Result FROM   WHERE                Result  FROM   WHERE
  |     |      |                     |      |      |
 Col    p    Expr>Expr              Col     p   Func-Call
  |          |     |                 |           /   |   \
  a         Col   Num                a       printf  Fmt  Int
             |     |                         |       |     |
             a     1                        '%.*g'  ↑  2147483647
                                              Boundary-Int

Output: "SELECT a FROM p WHERE printf('%.*g', 2147483647, 0.01)"
```

Splice combines structural elements from different interesting inputs — this is how patterns from one code path get combined with patterns from another, enabling cross-pollination.

---

**Example M6: Bulk Random Havoc** (100× `mut_random` + 20× `mut_random_recursion`)

In the Det and Random queue states, each input gets: 100 random subtree replacements (`havoc`), 20 recursion expansions (`havoc_recursion`), and 100 splice attempts (`splice`). Each individual mutation produces a **separate** candidate that is independently executed and coverage-checked — they are NOT stacked sequentially on one tree.

```
Input: "SELECT a FROM p WHERE a > 1"

havoc() — 100 independent mut_random calls on the ORIGINAL tree:
  Attempt 1:  Random node=WHERE Expr → "SELECT a FROM p WHERE EXISTS (SELECT b FROM q)"
  Attempt 2:  Random node=FROM Table → "SELECT a FROM q WHERE a > 1"
  Attempt 3:  Random node=Result-Col → "SELECT coalesce(a,b) FROM p WHERE a > 1"
  ...each attempt starts from the ORIGINAL tree, not from previous attempt's output
  ...each is executed → coverage checked → if new bits, added to queue

havoc_recursion() — 20 independent mut_random_recursion calls:
  Attempt 1:  Expand Expr recursion → "SELECT a + a + b FROM p WHERE a > 1"
  Attempt 2:  Expand deeper → "SELECT a + a + a + a + b FROM p WHERE a > 1"
  ...

splice() — 100 independent mut_splice calls:
  Attempt 1:  Splice ChunkStore Expr → "SELECT printf('%.*g',2147483647) FROM p WHERE a > 1"
  ...
```

> **Key detail:** Each mutation call produces ONE candidate from the original tree. They don't chain. This is why 100+20+100 = 220 executions per queue item per round (in Det/Random states).

---

#### Figures Needed in Thesis

Each example above should have a corresponding figure showing the **derivation tree before and after** the mutation, similar to Nautilus paper Examples IV.2–IV.5. Recommended figure set:

| Figure | Content | Maps to |
|--------|---------|---------|
| Fig 3.X | Subtree minimization: SQL tree shrinks while preserving coverage | Example M1 |
| Fig 3.X | Deterministic substitution: one Expr node → multiple alternatives tried | Example M2 |
| Fig 3.X | Random subtree: Expr node replaced with fresh grammar derivation | Example M3 |
| Fig 3.X | Recursive expansion: Expr→Expr+Expr repeated, tree grows deeper | Example M4 |
| Fig 3.X | Splice: ChunkStore subtree (from prior interesting input) replaces node | Example M5 |

> **Note:** Havoc (M6) doesn't need its own figure — it's just 100× of M3. Can be described textually.
> These figures should use **SQL non-terminals** (Sql-Stmt, Expr, Select-Stmt, Table-Name, etc.) not the generic PROG/STMT/VAR from the Nautilus paper.

**Minimize (separate from mutations):**
- `minimize` + `minimize_rec`: shrink tree preserving coverage bits
- Runs during Init state before deterministic mutations
- After minimization: tree added to ChunkStore for splice material
- See Example M1 above for visualization

### Fork Server and Harness

- AFL fork-server protocol: `__AFL_INIT()` only (no `__AFL_LOOP`)
- Harness opens empty in-memory SQLite database **before** `__AFL_INIT()`
- Each fork: reads SQL from temp file → `sqlite3_exec()` → exits
- SQLite compiled with ASan + UBSan instrumentation
- ASan: memory safety (buffer overflow, use-after-free)
- UBSan: undefined behavior (integer overflow, null pointer dereference)

**Exit code handling (from `fuzzer/src/fuzzer.rs:204-307`):**

| Exit | Meaning | Action |
|------|---------|--------|
| 223 | ASan crash | Save to `outputs/signaled/ASAN_*` |
| 1 | UBSan | Save to `outputs/signaled/UBSAN_*` |
| Signal | Crash (SIGTRAP, SIGSEGV) | Save to `outputs/signaled/` |
| Normal (other) | No crash → check bitmap | If new coverage bits → add to queue |
| Timeout | Execution exceeded limit | Save to `outputs/timeout/` |

> **Verified:** `harness/src/sqlite_harness.c:74` — `__AFL_INIT()` only. `fuzzer/src/fuzzer.rs:204` — exit 223 = ASan.

### Coverage Feedback and Queue

- Greybox: checks whether input exercised previously unseen control-flow edges
- New edges → input classified as "interesting" → added to queue as seed for mutations
- Feedback loop steers generation toward unexplored program regions
- Without feedback: uniform generation from grammar (strictly less efficient — demonstrated in Chapter 4)

### Triage Pipeline

- Post-campaign: processes crashing inputs
- Determines: distinct bug count, CVE correspondence, reproduction reliability
- Transforms raw crash data → actionable vulnerability reports
- Details in Chapter 4

### Self-Contained Test Cases

**Structure of each generated SQL program:**
1. **Schema-Setup** — CREATE TABLE/VIEW/INDEX/VIRTUAL TABLE
2. **Data-Insert** — INSERT statements populate tables with random rows
3. **Stress-Query** or **Validation-Op** — exercise target code paths

**Ordering guarantee:** Schema-Setup → Data-Insert → Stress-Query ensures referential consistency (tables exist and have data before queries).

**Semantic error handling:** SQLite's error-tolerant execution produces error return codes (not crashes) for type mismatches etc. → filtered by crash-detection oracle naturally.

### 5 Functional Subsystems (Table 3.1)

| Component | Language | Module | Role |
|-----------|----------|--------|------|
| Grammar Engine | Rust + Python | `grammartec/` | Load grammar, weighted rule sampling |
| Generation + Mutation | Rust | `fuzzer/` | Build and mutate derivation trees |
| Fork Server + Harness | Rust + C | `forksrv/`, `harness/` | Execute SQL against instrumented SQLite |
| Coverage Feedback | Rust | `fuzzer/` | Track edges, maintain queue |
| Triage Pipeline | Python | `triage/` | Crash dedup, CVE matching, reporting |

---

## 3.1.1 Positioning Among DBMS Fuzzers

**Comparison table (Table 3.2):**

| Feature | SQLsmith | Squirrel | DBMS-Nautilus |
|---------|----------|----------|---------------|
| Generation | Random grammar | Validity-preserving mutation | Weighted grammar with derivation trees |
| Schema | External pre-populated database | Internal evolving schema model | Self-contained per test case |
| Mutation | Random re-generation | Semantic-aware tree mutation | Structure-preserving tree mutation |
| Coverage | No | Yes (edge coverage) | Yes (shared memory bitmap) |
| Targeting | No | No | Yes (weighted production rules) |
| Isolation | No (requires external state) | No (requires schema model) | Yes (empty database per input) |

**Key distinction:** How each tool allocates fuzzing effort across SQL input space.
- SQLsmith: uniform sampling, equal probability to all constructs
- Squirrel: semantic mutation + coverage, but no vulnerability bias
- DBMS-Nautilus: bias embedded in grammar weights → concentrates on structural patterns associated with known CVEs (generated columns, NATURAL JOINs, boundary-value function calls)

---

## 3.2 Grammar Design

### Zero PoC Contamination Principle

Grammar encodes structural patterns that trigger vulnerability **classes**, not specific proof-of-concept inputs.

**Example:** CVE-2020-13434 (integer overflow) requires `printf` + INT32 boundary value. Grammar does NOT encode `SELECT printf('%.*g', 2147483647, 0.01)`. Instead provides independent non-terminals: `Format-Spec`, `Boundary-Int`, `Boundary-Func-Call`. Fuzzer must compose them.

**Three design constraints:**
- **(a)** No grammar rule may contain a complete CVE PoC as a fixed string
- **(b)** Every structural pattern needed to reach a target CVE must exist as a composable non-terminal
- **(c)** Grammar must preserve sufficient compositional freedom for novel discoveries beyond known CVEs

**Circularity defense:** CVEs = ground truth for evaluation. Zero PoC contamination ensures rediscovery is non-trivial (building blocks, not recipes). Chapter 4 validates by showing grammar also discovers bugs beyond known CVEs.

**Central design tension:** (b) vs (c) — too few non-terminals → can't reach targets; too many → probability of assembling right combination drops below useful threshold.

### Grammar stats

- **514 production rules** total
- **Over 460 in Layer 1** (SQL atoms)
- **Approximately 50 in Layer 2** (composed vulnerability-targeting shapes)
- 4 pattern categories in Layer 2

> **Verified:** Lines 1-644 = 465 rules (Layer 1 + START). Lines 645+ = 49 rules (Layer 2).

---

## 3.2.1 Two-Layer Architecture

### Layer 1: SQL Atoms (~465 rules)

SQL primitives:
- Over 30 expression alternatives (arithmetic, comparison, logical, string, subquery)
- SELECT/FROM/WHERE/JOIN clauses
- Window functions with frame specifications
- Common table expressions (CTEs)
- DML: INSERT, UPDATE, DELETE
- DDL: CREATE TABLE, VIEW, INDEX, TRIGGER
- Function calls: aggregate, scalar, window-specific
- Terminal literals: integers, floats, strings, blobs, boundary values

### Layer 2: Composed Shapes (~49 rules)

4 high-level shapes composing Layer 1 atoms:

| Shape | Alternatives | Weight range |
|-------|-------------|-------------|
| Schema-Setup | 6 | 0.5–3.0 |
| Stress-Query | 8 | 1.5–3.0 |
| Validation-Op | 4 | 1.5–3.0 |
| Boundary-Func-Call | 7 | 1.5–3.0 |

**Start symbol `Sql-Stmt` dispatch (4 top-level rules):**

| Rule | Weight | Composition |
|------|--------|-------------|
| `{Schema-Setup};\n{Stress-Query}` | 3.0 | Schema + query |
| `{Schema-Setup};\n{Insert-Stmt};\n{Stress-Query}` | 2.5 | Schema + data + query |
| `{Schema-Setup};\n{Insert-Stmt};\n{Validation-Op}` | 2.0 | Schema + data + validation |
| `SELECT {Boundary-Func-Call}` | 2.0 | Standalone boundary call |

> **Note:** Schema-Setup appears in 3/4 alternatives. Boundary-Func-Call only in 1/4.
> Figure 3.2 caption says Schema-Setup and Stress-Query are "required" and Validation-Op and Boundary-Func-Call are "optional" — this is approximately correct but imprecise (Stress-Query only in 2/4).

> **[PENDING]** Figure 3.2 (`fig_3_2_grammar_layers.pdf`) shows "Boundary-Func-Call 3 rules" — should be "7 rules". Needs figure update.

---

## 3.2.2 Structural Pattern Categories

### Schema Topology Patterns (S1–S6)

| ID | SQL Pattern | Weight | Target Subsystem |
|----|-------------|--------|------------------|
| S1 | `CREATE TABLE p(Col-Def-List)` | 1.5 | Base schema |
| S2 | `CREATE TABLE p(Col-Def-List-GenCol)` | 3.0 | Generated column processor |
| S3 | `CREATE TABLE p(...); CREATE TABLE q(...)` | 2.5 | Join optimizer (enables JOINs) |
| S4 | `CREATE TABLE p(...); CREATE VIEW v1 AS ...` | 2.0 | View materializer |
| S5 | `CREATE VIRTUAL TABLE fts_t1 USING fts5/fts3(...)` | 0.5 | FTS subsystem |
| S6 | `CREATE TABLE p(...); CREATE INDEX idx1 ON p(...)` | 1.0 | Index maintenance |

**Why S2 has highest weight (3.0):** Generated columns activate the generated column processor, which resolves column expressions that may reference other columns in the same table — recursive process prone to null pointer dereferences and infinite loops from circular dependencies. Participates in 2/6 target CVEs (CVE-2020-9327, CVE-2019-19646).

> **Verified:** Exact match with `grammars/v3.3/sqlite_v3.py:649-680`

### Query Stress Patterns (Q1–Q8)

| ID | SQL Pattern | Weight | Target |
|----|-------------|--------|--------|
| Q1 | `{Select-Stmt}` (base SELECT) | 2.0 | Compositional freedom |
| Q2 | `SELECT ... WHERE EXISTS ({Select-Stmt})` | 3.0 | Subquery engine |
| Q3 | `SELECT ... NATURAL JOIN ... WHERE {Expr}` | 3.0 | Column name matching |
| Q4 | `WITH RECURSIVE {Cte-Def} SELECT ...` | 2.5 | CTE resolution engine |
| Q5 | `{Select-Stmt} {Compound-Op} {Select-Stmt}` | 2.5 | INTERSECT/EXCEPT alignment |
| Q6 | `SELECT ... JOIN ... ON {Expr}` | 2.0 | Self-join optimization |
| Q7 | `SELECT ... FROM (SELECT ... ) AS sub1` | 1.5 | Derived table / subquery flattening |
| Q8 | `EXPLAIN QUERY PLAN {Select-Stmt}` | 1.5 | Plan serialization |

**Why these patterns stress the query planner:**
- Query planner performs most complex AST transformations: join reordering, subquery flattening, compound query optimization, recursive CTE expansion
- Each transformation involves pointer manipulation + column name resolution across multiple table scopes
- Off-by-one errors, null dereferences, use-after-free bugs frequent in these operations

**Per-pattern rationale:**
- **Q3 (NATURAL JOIN):** Forces column matching by name across tables → stresses name resolution logic implicated in CVE-2020-13435
- **Q4 (Recursive CTE):** CTE resolution must handle recursive expansion with termination detection — pointer-heavy tree traversal where off-by-one errors and infinite loops occur
- **Q5 (Compound):** INTERSECT/EXCEPT must align result columns across independently optimized subqueries → CVE-2020-15358, CVE-2020-13871
- **Q7 (Nested subquery):** Forces query planner to handle derived tables and subquery flattening decisions, exercising optimization paths that manipulate internal AST nodes
- **Q8 (EXPLAIN QUERY PLAN):** Plan serialization traverses full optimized AST to produce human-readable output

> **Verified:** `grammars/v3.3/sqlite_v3.py:703-748`. Listing 3.2 in thesis shows Q2, Q3, Q5, Q6 (representative subset — correct).

### Boundary Value Patterns (7 alternatives)

| # | SQL Pattern | Weight | Target |
|---|-------------|--------|--------|
| 1 | `printf({Format-Spec}, {Boundary-Int}, {Boundary-Float})` | 3.0 | Integer overflow in printf |
| 2 | `printf({Format-Spec}, {Boundary-Int})` | 2.0 | Printf with fewer args |
| 3 | `printf({Printf-Fmt-Spec}, {Boundary-Int}, {Str-Literal})` | 1.5 | Printf with string arg |
| 4 | `substr({Str-Literal}, {Boundary-Int})` | 2.0 | Heap buffer boundary |
| 5 | `substr({Str-Literal}, {Boundary-Int}, {Boundary-Int})` | 1.5 | Heap buffer with length |
| 6 | `hex(zeroblob({Boundary-Int}))` | 2.0 | Memory allocation limits |
| 7 | `round({Boundary-Float}, {Boundary-Int})` | 1.5 | Float-to-int conversion |

**Three function families:**
1. **printf** (3 alternatives): format specifiers + boundary integers → integer overflow in string formatting (CVE-2020-13434)
2. **substr** (2 alternatives): boundary-value offsets/lengths → heap buffer boundaries
3. **hex/zeroblob + round** (2 alternatives): memory allocation limits + float-to-int conversion

**Supporting non-terminals:**
- `Format-Spec`: `%.*g` (w=3.0), `%.*f` (w=2.0), `%.*e` (w=2.0), `%.*d` (w=1.0), `%.*s` (w=1.0)
- `Printf-Fmt-Spec`: `%d`, `%u`, `%x`, `%f`, `%s`, `%lld` (w=3.0), `%lli` (w=2.0)
- `Boundary-Int`: 2147483647 (INT32_MAX), 2147483648 (INT32_MAX+1), -2147483648 (INT32_MIN), 9223372036854775807 (INT64_MAX) — all w=3.0

**Why effective:** SQLite's C implementation performs many 32↔64-bit integer width conversions in formatting and string functions. Boundary values systematically probe conversion points where truncation or sign extension errors → buffer overflows or undefined behavior.

> **Verified:** `grammars/v3.3/sqlite_v3.py:758-787`

### Validation Operations (4 alternatives)

| # | SQL Pattern | Weight | Target |
|---|-------------|--------|--------|
| 1 | `PRAGMA integrity_check` | 3.0 | Full page walk, structural invariant validation |
| 2 | `PRAGMA quick_check` | 2.0 | Subset of integrity_check |
| 3 | `ANALYZE {Table-Name}` | 1.5 | Index metadata traversal, statistics collection |
| 4 | `EXPLAIN QUERY PLAN {Select-Stmt}` | 1.5 | AST traversal for plan serialization |

**Why important:** Traverse internal data structures (B-trees, schema tables, index metadata) using code paths distinct from normal query execution. Integrity checker walks every database page and validates structural invariants — triggers bugs in page cache, B-tree traversal, or column type checking when schema has unusual constructs (generated columns, virtual tables). Connected to CVE-2019-19646.

> **Verified:** `grammars/v3.3/sqlite_v3.py:750-755`

### Pattern-to-Subsystem Summary (Table 3.3)

| Pattern Category | Target Subsystem | Vulnerability Mechanism |
|------------------|------------------|------------------------|
| Schema Topology (S1–S6) | Column resolver, generated column processor, view materializer | Circular dependencies, null dereferences in column resolution |
| Query Stress (Q1–Q8) | Query planner, join optimizer, compound query engine | Name resolution errors, use-after-free in AST transforms |
| Boundary Values | printf, substr, zeroblob implementations | Integer overflow, buffer overread, allocation failures |
| Validation Ops | Integrity checker, B-tree traversal, schema validator | Page cache errors, type checking failures on unusual schemas |

---

## 3.2.3 Cross-Pollination of Structural Patterns

### Concept

Structural patterns are **not labeled or isolated per CVE**. Each non-terminal encodes a SQL structural affordance without indicating which vulnerability it targets. Grammar captures structural categories, not individual instances.

### Mechanism

Cross-pollination arises from **independence of Layer 2 selections**:
- Each input: independently selects Schema-Setup variant + Stress-Query variant + optionally Boundary-Func-Call or Validation-Op
- Independent weighted distributions → fuzzer samples from **Cartesian product** of all Layer 2 shapes
- Produces combinations designer never explicitly planned

**Example:** Single input might combine S2 (generated columns) + Q3 (NATURAL JOIN) + printf boundary call → exercises intersection of generated column processor, join optimizer, and printf implementation simultaneously.

### CVE-to-Pattern Mapping (Table 3.4)

| CVE | # Patterns | Required Structural Elements |
|-----|-----------|------------------------------|
| CVE-2019-19646 | 2 | Generated column, PRAGMA integrity_check |
| CVE-2020-13434 | 2 | printf() call, INT32 boundary value |
| CVE-2020-9327 | 4 | Generated column, coalesce(), JOIN, CREATE VIEW |
| CVE-2020-13435 | 5 | NATURAL JOIN, coalesce(), window OVER(), UNIQUE column, IN subquery |
| CVE-2020-13871 | 3 | EXCEPT, multi-column ORDER BY, scalar subquery |
| CVE-2020-15358 | 3 | CREATE VIEW with ORDER BY, INTERSECT, implicit JOIN (comma-separated FROM) |

> **[PENDING]** This table needs cross-checking against actual crash triggers in `results/crashes/`. Particularly CVE-2020-13435 lists "window OVER()" but Q7 is NOT window functions (it's nested subquery). Does 13435 use window functions from elsewhere in Layer 1?

### Key properties

- No structural pattern unique to single CVE
- Every CVE requires 2–5 patterns from different non-terminal groups
- Generated columns participate in 2 CVEs; JOIN patterns serve 3; coalesce appears in 2
- **Multiplicative benefit:** Improving one pattern's reach simultaneously improves reach for other CVEs

### Consequences

1. CVE rediscovery = genuine compositional achievement (must select correct combination from large combinatorial space)
2. Grammar discovers bugs beyond design targets — 7 non-CVE bug classes found (FTS tokenizer null dereferences, float cast overflows, window function lifecycle errors) because patterns for specific CVEs also exercise adjacent code paths

---

## 3.2.4 Analysis of the Grammar Design Approach

### Advantages

- **Cross-pollination:** Each new pattern participates in combinations with all existing patterns → combinatorial expansion (not additive)
- **Zero PoC contamination:** Grammar remains genuine testing tool, not regression suite
- **Methodological contribution:** Fuzzing engine (Nautilus) is reused; the grammar design methodology is what enables effective vulnerability discovery
- **Composability:** Add Layer 1 atom → available to all Layer 2 shapes. Add Layer 2 shape → composes with all Layer 1 atoms. Local changes → global effects.

### Comparison with automated approaches

- Skyfire, IFuzzer: learn syntactic structure from existing inputs, no domain expertise needed
- But cannot encode vulnerability-specific knowledge (which subsystems to stress, which patterns reach vulnerable code)
- Manual approach trades scalability for targeting precision
- Experiments show targeting precision = dominant factor for CVE rediscovery
- Methodology generalizable: identify vulnerability-prone subsystems → encode structural patterns → assign weights proportional to vulnerability density. Applicable to any DBMS with documented internals.

### Limitations (3)

1. **Manual domain expertise required.** Must trace CVE root cause → SQL constructs that exercise relevant code path. Cannot be fully automated.

2. **Weight sensitivity.** Bad weights → concentrate on shallow bug space region, starve others. Example: overweighting FTS schemas in early versions → 92% crashes were FTS bugs. Initial weights set proportional to CVE count per pattern, then adjusted by crash diversity in pilot campaigns. Chicken-and-egg: must run grammar to assess weights, but bad weights waste campaign time.

3. **Reachability ceiling.** Grammar can only discover bugs whose structural prerequisites exist as non-terminals. Missing construct (e.g., recursive CTE, ATTACH DATABASE) → no amount of campaign time or weight tuning triggers it. Grammar = hard boundary; coverage feedback navigates within it but cannot expand it.

> **Note on limitation 3:** The thesis text mentions "recursive common table expression" as an example of a missing construct, but Q4 IS a recursive CTE. This is a leftover from an earlier grammar version where recursive CTEs were not included. The example should be changed to something the grammar genuinely does NOT encode (e.g., ATTACH DATABASE, ALTER TABLE, or UPSERT ON CONFLICT).

---

## Open Issues for Human Review

1. **[RESOLVED] State machine Init→Det→Random** — **Confirmed: our customization.** Original Nautilus has 4 states: `init→det→detafl→random` (paper Fig. 2, page 7). We removed `detafl` because we don't use AFL byte-level mutations (bit flips, arithmetic) — they produce parser-invalid SQL. Thesis should explicitly note this as a modification: "DBMS-Nautilus uses a simplified three-state pipeline (Init→Det→Random) that omits the AFL mutation stage from the original Nautilus, since byte-level mutations produce parser-rejected SQL inputs."

2. **[PENDING] CVE-2020-13435 structural requirements** — Table 3.4 says "window OVER()" but Q7 = nested subquery chain, not window functions. Does 13435 actually need window functions from Layer 1 non-terminals?

3. **[PENDING] Figure 3.2 (`fig_3_2_grammar_layers.pdf`)** — Shows "Boundary-Func-Call 3 rules" → should be "7 rules w 1.5-3.0"

4. **[PENDING] Figure 3.1 (`fig_3_1_architecture.pdf`)** — Verify matches the 5-subsystem grouping and 12 components described in text.

5. **[ISSUE?] Limitation 3 example** — Text says "recursive common table expression" as example of missing construct, but Q4 IS a recursive CTE. Pick different example.

6. **[ISSUE?] Figure 3.2 caption accuracy** — Says Schema-Setup and Stress-Query are "required" in every statement, but Stress-Query only appears in 2/4 Sql-Stmt alternatives, not all 4.

7. **[CHECK] Abstract (page ii)** — Still says "520 rules" and "v3.0 to v3.3, from 449 to 520 rules". Chapter 1 introduction (page 1) also says "449 to 520 rules". These are in different .tex files and were NOT fixed in this session.

8. **[ISSUE] c3_method.tex line 26** — Says "random recursion expansion or collapse" but `mut_random_recursion` ONLY expands (repeats recursive pair 2^n times). Collapse is done by `minimize_rec` during minimization, not mutation. Fix: change to "random recursion expansion (repeating recursive productions to increase nesting depth)".
