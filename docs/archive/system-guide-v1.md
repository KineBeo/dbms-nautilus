# RL-Nautilus System Guide

A comprehensive guide to the RL-Nautilus grammar-based fuzzer. Written for someone with no prior knowledge of grammar-based fuzzing. Chapters progress from foundational concepts to deep implementation details.

---

## Table of Contents

1. [What is Fuzzing?](#1-what-is-fuzzing)
2. [What is Grammar-Based Fuzzing?](#2-what-is-grammar-based-fuzzing)
3. [System Overview — The Big Picture](#3-system-overview--the-big-picture)
4. [The Grammar Engine (grammartec)](#4-the-grammar-engine-grammartec)
5. [Trees — The Internal Representation](#5-trees--the-internal-representation)
6. [Mutation Strategies](#6-mutation-strategies)
7. [The Fork Server — Executing Inputs](#7-the-fork-server--executing-inputs)
8. [The Harness — What We're Testing](#8-the-harness--what-were-testing)
9. [Coverage Feedback — How We Know What's New](#9-coverage-feedback--how-we-know-whats-new)
10. [The Fuzzer Core — Orchestrating Everything](#10-the-fuzzer-core--orchestrating-everything)
11. [The Queue — Managing Interesting Inputs](#11-the-queue--managing-interesting-inputs)
12. [The ChunkStore — Reusing Subtrees](#12-the-chunkstore--reusing-subtrees)
13. [The State Machine — Input Processing Pipeline](#13-the-state-machine--input-processing-pipeline)
14. [Multi-Threading Architecture](#14-multi-threading-architecture)
15. [Python Grammars — Writing Rules](#15-python-grammars--writing-rules)
16. [RL Integration — Adaptive Mutation (Phase 2+)](#16-rl-integration--adaptive-mutation-phase-2)
17. [File Map — Where Everything Lives](#17-file-map--where-everything-lives)
18. [Data Flow Diagram — End to End](#18-data-flow-diagram--end-to-end)
19. [Troubleshooting Guide](#19-troubleshooting-guide)
20. [Glossary](#20-glossary)

---

## 1. What is Fuzzing?

Fuzzing is a software testing technique where you throw random (or semi-random) inputs at a program to find bugs. The idea is simple:

```
Generate input → Feed to program → Did it crash?
                                    ├── Yes → Found a bug!
                                    └── No  → Try another input
```

**Why it works:** Programmers think about "normal" inputs. Fuzzers generate millions of "weird" inputs that no human would type. These weird inputs expose edge cases, buffer overflows, and logic errors.

**Example:** Imagine testing a calculator. A human tests `2+2`. A fuzzer tests `99999999999999999*-0.000000001/0` — and might find that the calculator crashes on division by zero.

### Types of Fuzzers

| Type | How it generates inputs | Pros | Cons |
|------|------------------------|------|------|
| **Dumb/Random** | Random bytes | Simple, fast | Most inputs rejected by parser |
| **Mutation-based** | Modify existing valid inputs | Good at finding shallow bugs | Can't create structurally new inputs |
| **Grammar-based** | Generate from language rules | Inputs are always syntactically valid | Need to write a grammar |
| **Coverage-guided** | Use code coverage to guide mutations | Finds deep bugs systematically | Slower per execution |

**RL-Nautilus is grammar-based AND coverage-guided** — it combines the best of both approaches.

---

## 2. What is Grammar-Based Fuzzing?

### The Problem with Random Fuzzing

If you fuzz a SQL database with random bytes, 99.99% of inputs are rejected at the parser:

```
Random: "x\x00\xffabc"  → Parser says "syntax error" → Useless
Random: "SELCT FROM"     → Parser says "syntax error" → Useless  
Valid:  "SELECT * FROM t" → Parser accepts → Now we test real logic
```

### The Grammar Solution

A **grammar** describes the structure of valid inputs. It's a set of rules that say "a valid SQL statement looks like this":

```
Sql-Stmt    → Select-Stmt | Insert-Stmt | ...
Select-Stmt → "SELECT" Result-Cols "FROM" Table-Name
Result-Cols → "*" | Col-Name
Table-Name  → "t1" | "t2" | ...
```

Given these rules, the fuzzer generates inputs that are **always syntactically valid**:

```
SELECT * FROM t1           ← valid, tests basic SELECT
SELECT a, b FROM t2        ← valid, tests column list
SELECT * FROM t1 JOIN t2   ← valid, tests JOINs
```

Every generated input passes the parser and reaches the **deep logic** — where the real bugs hide.

### How Rules Work

Each rule says "this symbol can be replaced by this string". The string can contain:
- **Literal text:** `SELECT`, `FROM`, `,`
- **References to other symbols:** `{Table-Name}`, `{Expr}`

The curly braces `{}` mean "pick a random expansion for this symbol."

Example rule chain:
```
START         → {Sql-Stmt};
Sql-Stmt      → {Select-Stmt}
Select-Stmt   → SELECT {Result-Col} FROM {Table-Name}
Result-Col    → *
Table-Name    → t1

Final output: "SELECT * FROM t1;"
```

---

## 3. System Overview — The Big Picture

RL-Nautilus has 5 major components. Here's how they connect:

```
┌─────────────────────────────────────────────────────────────┐
│                        NAUTILUS FUZZER                       │
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Grammar  │───>│  Tree    │───>│  SQL     │              │
│  │ Engine   │    │ (AST)    │    │  Text    │              │
│  │(grammartec)   │          │    │          │              │
│  └──────────┘    └──────────┘    └────┬─────┘              │
│       ▲               ▲              │                     │
│       │               │              ▼                     │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Mutator  │    │ Chunk    │    │  Fork    │              │
│  │          │    │ Store    │    │  Server  │              │
│  └──────────┘    └──────────┘    └────┬─────┘              │
│                                      │                     │
│                                      ▼                     │
│                                ┌──────────┐                │
│                                │ Harness  │                │
│                                │ (SQLite) │                │
│                                └────┬─────┘                │
│                                     │                      │
│                                     ▼                      │
│                           ┌──────────────────┐             │
│                           │ Coverage Bitmap  │             │
│                           │ (shared memory)  │             │
│                           └──────────────────┘             │
│                                     │                      │
│                                     ▼                      │
│                              New coverage?                 │
│                              ├── Yes → Add to Queue        │
│                              └── No  → Discard             │
└─────────────────────────────────────────────────────────────┘
```

| Component | Language | Source | Purpose |
|-----------|----------|--------|---------|
| **grammartec** | Rust | `grammartec/src/` | Grammar engine: rules, trees, mutations, weighted sampling |
| **fuzzer** | Rust | `fuzzer/src/` | Main loop, state machine, queue, threading, DQN agent |
| **forksrv** | Rust | `forksrv/src/` | AFL-compatible fork server, shared memory bitmap |
| **harness** | C | `harness/` | SQLite test wrapper with ASan/UBSan crash detection |
| **grammars** | Python | `grammars/` | Grammar definitions written in Python DSL |

---

## 4. The Grammar Engine (grammartec)

**Source:** `grammartec/src/context.rs`, `grammartec/src/rule.rs`

The grammar engine is the heart of Nautilus. It manages all the rules and knows how to generate valid trees from them.

### 4.1 The Context — Central Registry

The `Context` struct (`grammartec/src/context.rs:16-28`) is the central registry for all grammar rules. It stores:

```rust
struct Context {
    rules: Vec<Rule>,                              // All rules, indexed by RuleID
    nts_to_rules: HashMap<NTermID, Vec<RuleID>>,   // "Which rules produce symbol X?"
    nt_ids_to_name: HashMap<NTermID, String>,       // NTermID → "Select-Stmt"
    names_to_nt_id: HashMap<String, NTermID>,       // "Select-Stmt" → NTermID
    rules_to_min_size: HashMap<RuleID, usize>,      // Minimum tree nodes this rule needs
    nts_to_min_size: HashMap<NTermID, usize>,        // Minimum tree nodes for this symbol
    max_len: usize,                                  // Maximum allowed tree size
}
```

**Key insight:** Every nonterminal name (like `Select-Stmt`) gets a numeric ID (`NTermID`). Every rule gets a numeric ID (`RuleID`). This makes lookups fast — we work with integers, not strings.

### 4.2 Rules — The Building Blocks

**Source:** `grammartec/src/rule.rs`

There are three types of rules:

#### Plain Rules — Template-based

The most common type. A format string with literal text and nonterminal references:

```python
ctx.rule("Select-Stmt", "SELECT {Result-Col} FROM {Table-Name}")
```

Internally parsed into a `PlainRule`:
```rust
PlainRule {
    nonterm: NTermID(7),     // "Select-Stmt"
    children: [
        Term("SELECT "),     // literal bytes
        NTerm(NTermID(3)),   // reference to "Result-Col"  
        Term(" FROM "),      // literal bytes
        NTerm(NTermID(5)),   // reference to "Table-Name"
    ],
    weight: 1.0,             // sampling weight (for biased selection)
}
```

The format string uses `{SymbolName}` for nonterminal references. Literal `{` and `}` are escaped as `\{` and `\}`.

#### Script Rules — Python callbacks

For complex transformations that can't be expressed as templates:

```python
ctx.script("Formatted-Int", ["Int-Value"], lambda v: f"'{int(v):010d}'")
```

During unparsing, the child nonterminals are generated first, their output is buffered, and then the Python callback is called with the buffers as arguments.

#### RegExp Rules — Regex-based generation

For generating values matching a pattern:

```python
ctx.regex("Col-Alias", "[a-z][a-z0-9_]*")
```

Uses the `regex_mutator` crate to generate random strings matching the regex.

### 4.3 Weighted Sampling — Biasing What We Generate

**Source:** `grammartec/src/context.rs:264-337`

When the fuzzer needs to pick a rule for a nonterminal, it doesn't pick uniformly at random. Each rule has a **weight** that controls how often it's selected:

```python
ctx.rule("Sql-Stmt", "{Select-Stmt}", weight=1.0)         # Normal
ctx.rule("Sql-Stmt", "{Pattern-Boundary-Func}", weight=3.0) # 3x more likely
ctx.rule("Sql-Stmt", "{Drop-Stmt}", weight=0.2)            # Rarely chosen
```

The selection algorithm (`dumb_get_random_rule_for_nt`, context.rs:283-337):

1. Filter rules that fit within the remaining tree size budget
2. Sum up all weights of applicable rules → `total_weight`
3. Pick a random float in `[0, total_weight)`
4. Walk through rules, subtracting each weight, pick the first that makes the threshold go negative

This is **weighted roulette wheel selection**. Higher weight = proportionally more likely.

### 4.4 Initialization — calc_min_len

**Source:** `grammartec/src/context.rs:160-196`

Before generation can start, `Context::initialize()` computes:

1. **Minimum tree size for each rule and nonterminal** — "How many nodes minimum to fully expand this?" This is computed by fixed-point iteration: start with terminal rules (size 1), then propagate upward.

2. **Rule ordering** — Within each nonterminal, rules are sorted by minimum size (smallest first). This ensures that when we're running low on budget, we can always find a terminating rule.

If any nonterminal has no way to terminate (all rules are recursive with no base case), `calc_min_len` panics with `"Broken Grammar"`. This is the most common grammar authoring error.

### 4.5 Tree Generation

**Source:** `grammartec/src/rule.rs:316-387`, `grammartec/src/context.rs:368-376`

Generation works top-down:

```
generate_tree_from_nt(START, max_len=100)
  → pick a random rule for START (weighted)
  → generate_from_rule(rule, max_len-1)
    → for each child nonterminal in the rule:
        → divide remaining length budget among children
        → pick a random rule for child (weighted, constrained by budget)
        → recursively generate subtree
```

The length budget system prevents infinite recursion. Each level consumes at least 1 from the budget. When budget is tight, only rules with small minimum sizes are eligible, which forces termination.

---

## 5. Trees — The Internal Representation

**Source:** `grammartec/src/tree.rs`

### 5.1 Tree Structure

The `Tree` struct stores a parse tree as three parallel arrays:

```rust
struct Tree {
    rules: Vec<RuleIDOrCustom>,  // Which rule was applied at each node
    sizes: Vec<usize>,           // Subtree size rooted at each node
    paren: Vec<NodeID>,          // Parent node of each node
}
```

Nodes are numbered 0, 1, 2, ... in **pre-order** (depth-first, parent before children). This is critical — the entire mutation system relies on pre-order indexing.

**Example:** For the grammar `S → a{B}c`, `B → b{A}b`, `A → x`:

```
Tree (conceptual):        Pre-order array:
       S                  [0] S→a{B}c   size=3  parent=0
      / \                 [1] B→b{A}b   size=2  parent=0
     B   (c)              [2] A→x       size=1  parent=1
    / \
  (b)  A
       |
      (x)

Output: "abxbc"
```

The `sizes` array enables O(1) subtree extraction: node `n`'s subtree is `rules[n .. n + sizes[n]]`.

### 5.2 Unparsing — Tree to Text

**Source:** `grammartec/src/tree.rs:20-151`

"Unparsing" converts a tree back to text (the actual SQL we feed to SQLite). It's a stack-based iterative process:

```
Stack: [Nonterm(S)]
 → pop Nonterm(S), rule is "a{B}c"
 → push Term("c"), Nonterm(B), Term("a") [reversed for stack order]

Stack: [Term("a"), Nonterm(B), Term("c")]
 → pop Term("a") → write "a"

Stack: [Nonterm(B), Term("c")]
 → pop Nonterm(B), rule is "b{A}b"
 → push Term("b"), Nonterm(A), Term("b")

... and so on until stack is empty
Output: "abxbc"
```

For **Script rules**, child nonterminals are unparsed into temporary buffers first, then the Python callback receives the buffers and returns the final text.

### 5.3 TreeMutation — Efficient Splicing

**Source:** `grammartec/src/tree.rs:392-443`

When we mutate a tree (replace a subtree), we don't copy the entire tree. Instead, we create a `TreeMutation` that virtually concatenates three slices:

```rust
struct TreeMutation<'a> {
    prefix:  &'a [RuleIDOrCustom],  // nodes before the replaced subtree
    repl:    &'a [RuleIDOrCustom],  // the replacement subtree
    postfix: &'a [RuleIDOrCustom],  // nodes after the replaced subtree
}
```

```
Original:  [A B C D E F G]
                 ^^^
            Replace nodes C,D,E with X,Y

TreeMutation:
  prefix  = [A, B]         (original[0..2])
  repl    = [X, Y]         (from another tree)
  postfix = [F, G]         (original[5..7])

Virtual tree: [A, B, X, Y, F, G]
```

`TreeMutation` implements the `TreeLike` trait, so it can be unparsed and executed without ever allocating a full copy. Only if the mutation is "interesting" (finds new coverage) do we materialize it into a real `Tree`.

---

## 6. Mutation Strategies

**Source:** `grammartec/src/mutator.rs`, `fuzzer/src/state.rs`

Nautilus uses 5 mutation strategies, each approaching the problem differently:

### 6.1 Havoc (Random Subtree Replacement)

**Source:** `mutator.rs:177-195`, `state.rs:131-143`

Pick a random node in the tree. Generate a completely new subtree for that node's nonterminal. Replace it.

```
Original: SELECT * FROM t1 WHERE x > 5
                               ^^^^^^^^
                         Random node: Expr (x > 5)

New subtree for Expr: count(y) < 10

Result:   SELECT * FROM t1 WHERE count(y) < 10
```

Called **100 times per input** in the main loop. This is the workhorse mutation — high throughput, explores widely.

### 6.2 Havoc Recursion (Recursive Expansion)

**Source:** `mutator.rs:197-268`, `state.rs:145-165`

Find recursive structures in the tree (e.g., nested expressions), and duplicate the recursive part multiple times:

```
Original: SELECT a+b FROM t1
          Recursion found: Expr → a+{Expr}
          
After 4x recursion:
          SELECT a+(a+(a+(a+b))) FROM t1
```

This is powerful for finding bugs in recursive parsers and deeply nested structures. Called **20 times per input**.

The `RecursionInfo` struct (`grammartec/src/recursion_info.rs`) pre-computes all recursive pairs in a tree. It builds an "inverted recursion tree" where each node points to its closest ancestor with the same nonterminal. Sampling is weighted by recursion depth using a `LoadedDiceSampler` for uniformity.

### 6.3 Splice (Cross-pollination)

**Source:** `mutator.rs:136-153`, `state.rs:167-189`

Take a subtree from a **different** interesting input and splice it into the current tree:

```
Input A: SELECT * FROM t1 WHERE x > 5
Input B: INSERT INTO t2 VALUES (1, 'hello')

Splice B's Expr into A's Expr slot:
Result:  SELECT * FROM t1 WHERE 'hello'
```

The `ChunkStore` (see Section 12) stores subtrees from all interesting inputs, indexed by nonterminal. Called **100 times per input**.

### 6.4 Deterministic (Exhaustive Rule Substitution)

**Source:** `mutator.rs:103-134`, `state.rs:109-129`

For each node in the tree, try **every alternative rule** for that node's nonterminal:

```
Node: Table-Name = "t1"
Alternative rules for Table-Name: "t2", "t3", "fts_t1"

Generate mutations:
  SELECT * FROM t2 WHERE ...
  SELECT * FROM t3 WHERE ...  
  SELECT * FROM fts_t1 WHERE ...
```

This is slower but systematic — it ensures we don't miss obvious alternatives. Run in cycles controlled by `number_of_deterministic_mutations` in config.

### 6.5 Generate (Fresh Input)

**Source:** `state.rs:191-198`

Generate a completely new tree from scratch, starting from the `START` nonterminal. Used when the queue is empty (all existing inputs have been processed).

### Strategy Summary

| Strategy | What it does | Times per input | Best for |
|----------|-------------|-----------------|----------|
| Havoc | Random subtree replacement | 100 | Wide exploration |
| Havoc Rec | Multiply recursive structures | 20 | Deep nesting bugs |
| Splice | Cross-pollinate subtrees | 100 | Combining interesting fragments |
| Deterministic | Try all alternative rules | All nodes × all rules | Systematic coverage |
| Generate | Fresh random tree | When queue empty | Diversity |

---

## 7. The Fork Server — Executing Inputs

**Source:** `forksrv/src/lib.rs`

### 7.1 What is a Fork Server?

Normally, to test an input you'd:
1. Start the program
2. Load libraries
3. Initialize state
4. Feed the input
5. Check the result
6. Kill the program
7. Repeat

Steps 1-3 take ~10ms each time. When you're doing millions of executions, this adds up to hours of wasted time.

A **fork server** does steps 1-3 **once**, then uses the `fork()` system call to create cheap copies:

```
[Parent Process]
    │
    ├── fork() → [Child 1] → execute input 1 → exit
    ├── fork() → [Child 2] → execute input 2 → exit
    ├── fork() → [Child 3] → execute input 3 → exit
    ...
```

`fork()` creates a copy of the process in ~0.1ms (vs ~10ms for full startup). This gives us **~100x speedup**.

### 7.2 How it Works (forksrv/src/lib.rs:50-190)

The fork server setup:

1. **Create shared memory** (`create_shm`) — A bitmap in shared memory (default 65536 bytes) where the target records which code paths it executes.

2. **Create pipes** — Two pipes for communication:
   - `ctl_pipe`: Parent → Child (sends "start" commands)
   - `st_pipe`:  Child → Parent (sends child PID and exit status)

3. **Fork** — Parent forks, child `execve`s the target binary with environment variables:
   - `__AFL_SHM_ID=<id>` — tells AFL runtime where the shared bitmap is
   - `AFL_MAP_SIZE=<size>` — bitmap size negotiation
   - `ASAN_OPTIONS=exitcode=223,...` — ASan crash = exit code 223
   - `UBSAN_OPTIONS=halt_on_error=1,exitcode=1` — UBSan = exit code 1

4. **Handshake** — The target's AFL runtime sends a hello message. For AFL++ 4.x, this is `0x41464c00..0x41464cff`, and we respond with the XOR. For old AFL 2.x, it's just `0`.

### 7.3 Running an Input (forksrv/src/lib.rs:192-233)

For each execution:
1. Clear the shared bitmap (zero all bytes)
2. Write the SQL input to a temp file
3. Send 4 zero bytes to `ctl_pipe` ("go!")
4. Read the child PID from `st_pipe`
5. Read the exit status from `st_pipe`
   - If read times out → kill the child → `ExitReason::Timeouted`
6. Return `ExitReason` and the shared bitmap (which now has coverage data)

---

## 8. The Harness — What We're Testing

**Source:** `harness/sqlite_harness_patterns.c`

The harness is a small C program that wraps SQLite. It's compiled with ASan (AddressSanitizer) and UBSan (UndefinedBehaviorSanitizer) to detect memory bugs.

### 8.1 What it Does

```c
// 1. Open an empty in-memory SQLite database (done once at startup)
setup_db()  →  sqlite3_open(":memory:", &db)

// 2. AFL fork server initialization point
__AFL_INIT()  // After this, every fork() creates a child

// 3. Read SQL from input file
sql = read_input(argv[1])

// 4. Execute the SQL
sqlite3_exec(db, sql, NULL, NULL, &errmsg)

// 5. Clean up and exit
sqlite3_close(db)
```

### 8.2 Crash Detection

The harness doesn't need to do anything special for crash detection — the sanitizers handle it:

| Condition | How it's detected | Exit code |
|-----------|-------------------|-----------|
| **Memory bug (buffer overflow, use-after-free)** | ASan aborts | 223 |
| **Undefined behavior (integer overflow, null deref)** | UBSan halts | 1 |
| **Signal (SIGSEGV, SIGABRT)** | OS delivers signal | Signal number |
| **Timeout** | Fork server kills child | N/A (special case) |
| **Normal exit** | Program returns 0 | 0 |

### 8.3 Harness Variants

| Harness | File | Pre-loaded schema | Use case |
|---------|------|-------------------|----------|
| `sqlite_harness_patterns.c` | Blank DB | No tables | Pattern grammar (self-contained DDL→DQL) |
| `sqlite_harness.c` | Pre-loaded | t1, t2, t3, fts_t1, indices, views | Attack grammar (assumes tables exist) |

**Important:** Nautilus uses fork-server mode only (NOT AFL persistent/`__AFL_LOOP`). Each forked child executes one SQL input and exits.

---

## 9. Coverage Feedback — How We Know What's New

**Source:** `fuzzer/src/fuzzer.rs:351-449`

### 9.1 The Bitmap

The coverage bitmap is a byte array in shared memory (default 65536 bytes). Each byte corresponds to a **branch** in the target program. When the target executes a branch, the AFL instrumentation increments the corresponding byte.

```
Bitmap: [0, 0, 3, 0, 1, 0, 0, 2, 0, ...]
              ^        ^        ^
         Branch 2    Branch 4  Branch 7
         hit 3x      hit 1x   hit 2x
```

### 9.2 New Bits Detection (fuzzer.rs:427-449)

After each execution, the fuzzer compares the run's bitmap against the **global bitmap** (cumulative coverage from all executions):

```rust
fn new_bits(&mut self, is_crash: bool) -> Option<Vec<usize>> {
    let run_bitmap = self.forksrv.get_shared();
    let shared_bitmap = global_state.bitmaps.get_mut(&is_crash);
    
    for (i, elem) in shared_bitmap.iter_mut().enumerate() {
        if run_bitmap[i] != 0 && *elem == 0 {
            // This branch was never hit before!
            *elem |= run_bitmap[i];
            res.push(i);
        }
    }
}
```

**New bits = new code paths explored.** If an input triggers new bits, it's "interesting" and gets added to the queue.

Note: There are **separate bitmaps** for crashing and non-crashing inputs (`bitmaps: HashMap<bool, Vec<u8>>`). A crash that exercises the same paths as a previous crash is still tracked.

### 9.3 Deterministic Check (fuzzer.rs:408-425)

Not all new bits are real. Some programs have non-deterministic behavior (timing, randomness). To filter these out, the fuzzer re-runs the input **5 more times** and only keeps bits that appear consistently:

```rust
fn check_deterministic_behaviour(&mut self, ...) {
    for _ in 0..5 {
        self.exec_raw(code)?;
        // Remove any bit that wasn't set in this re-run
        new_bits.retain(|&i| run_bitmap[i] != 0);
    }
}
```

### 9.4 Deduplication (fuzzer.rs:333-349)

To avoid re-executing the same SQL, the fuzzer keeps a ring buffer of the last 10,000 inputs (by raw bytes). If an input matches one we've already tried, skip it:

```rust
fn input_is_known(&mut self, code: &[u8]) -> bool {
    if self.last_tried_inputs.contains(code) {
        return true;  // Skip — we've already tried this exact SQL
    }
    // Add to ring buffer, evicting oldest if full
    self.last_tried_inputs.insert(code.to_vec());
}
```

---

## 10. The Fuzzer Core — Orchestrating Everything

**Source:** `fuzzer/src/fuzzer.rs`

The `Fuzzer` struct ties the fork server to the coverage tracking:

```rust
struct Fuzzer {
    forksrv: ForkServer,              // Executes inputs
    global_state: Arc<Mutex<GlobalSharedState>>,  // Shared coverage + queue
    last_tried_inputs: HashSet<Vec<u8>>,          // Dedup ring buffer
    execution_count: u64,                          // Total executions
    bits_found_by_*: u64,                          // Stats per strategy
}
```

### 10.1 The Execution Pipeline (fuzzer.rs:181-297)

When `run_on()` is called with an input:

```
1. Execute the SQL via fork server
2. Check exit reason:
   ├── Normal(223)  → ASan crash → save to outputs/signaled/ASAN_*
   ├── Normal(1)    → UBSan crash → save to outputs/signaled/UBSAN_*
   ├── Normal(other)→ Normal exit → check for new coverage bits
   ├── Signaled(sig)→ Signal crash → save to outputs/signaled/{sig}_*
   ├── Timeouted    → Timeout → save to outputs/timeout/*
   └── Stopped      → (ignored)
3. If new bits found (for normal exits):
   → Increment strategy-specific counter (bits_found_by_havoc, etc.)
4. If new bits found (for any exit):
   → Add tree to queue with coverage bitmap
```

### 10.2 `has_bits` — Minimization Helper (fuzzer.rs:299-316)

During minimization, we need to check "does this smaller tree still exercise the same code paths?" The `has_bits` method executes a tree and checks if specific bitmap positions are still set:

```rust
fn has_bits(&mut self, tree, bits, ...) -> Result<bool> {
    self.run_on_without_dedup(tree, ...)?;
    let run_bitmap = self.forksrv.get_shared();
    for bit in bits {
        if run_bitmap[*bit] == 0 {
            return Ok(false);  // Lost a bit — minimization went too far
        }
    }
    return Ok(true);
}
```

---

## 11. The Queue — Managing Interesting Inputs

**Source:** `fuzzer/src/queue.rs`

### 11.1 Queue Structure

```rust
struct Queue {
    inputs: Vec<QueueItem>,              // Unprocessed items (waiting for mutation)
    processed: Vec<QueueItem>,           // Already mutated (waiting for next round)
    bit_to_inputs: HashMap<usize, Vec<usize>>,  // Which inputs cover each bit
    current_id: usize,                   // Auto-incrementing ID
}
```

Each `QueueItem` (queue.rs:23-32) contains:

```rust
struct QueueItem {
    id: usize,                          // Unique ID
    tree: Tree,                         // The parse tree
    fresh_bits: HashSet<usize>,         // Bitmap positions this input first discovered
    all_bits: Vec<u8>,                  // Full bitmap snapshot
    exitreason: ExitReason,             // How the execution ended
    state: InputState,                  // Current processing stage (Init/Det/Random)
    recursions: Option<Vec<RecursionInfo>>,  // Pre-computed recursion info
    execution_time: u32,                // How long it took (nanoseconds)
}
```

### 11.2 Queue Lifecycle

```
New coverage found
    │
    ▼
Queue::add()
    │ Creates QueueItem with state = Init(0)
    │ Saves SQL to outputs/queue/id:000000001,er:Normal(0)
    ▼
Queue::pop()
    │ Removes item from inputs list
    │ Removes item's bits from bit_to_inputs
    ▼
[FuzzingState processes it through Init → Det → Random stages]
    │
    ▼
Queue::finished()
    │ Checks if item still has unique bits
    ├── Still unique → Move to processed list
    └── No unique bits → Delete file, discard
    
Queue::new_round()
    │ Moves all processed items back to inputs
    │ Called when inputs list is empty
    ▼
[Cycle repeats]
```

### 11.3 Bit Accounting

The `bit_to_inputs` map tracks which inputs are responsible for each bitmap position. This enables **input culling** — when a new input covers the same bits as an old one, the old one can be discarded (in `finished()`).

---

## 12. The ChunkStore — Reusing Subtrees

**Source:** `grammartec/src/chunkstore.rs`

### 12.1 What it Does

The ChunkStore is a library of interesting subtrees harvested from inputs that found new coverage. When splice mutation needs a replacement subtree, it draws from the ChunkStore.

### 12.2 How Subtrees are Collected (chunkstore.rs:51-81)

When a new input is minimized, `add_tree()` walks every node in the tree:

```rust
fn add_tree(&mut self, tree: Tree, ctx: &Context) {
    for i in 0..tree.size() {
        if tree.sizes[i] > 30 { continue; }  // Skip large subtrees
        
        let output = tree.unparse_node(i, ctx);
        if !self.seen_outputs.contains(&output) {
            self.seen_outputs.insert(output);
            // Index by nonterminal type
            self.nts_to_chunks[nonterminal].push((tree_id, node_id));
        }
    }
}
```

Only subtrees with **30 or fewer nodes** are collected (larger ones would dominate mutations).

### 12.3 How Subtrees are Retrieved (chunkstore.rs:83-96)

When splice mutation wants an alternative for a node:

```rust
fn get_alternative_to(&self, rule_id, ctx) -> Option<(&Tree, NodeID)> {
    // Find all chunks with the same nonterminal
    let chunks = self.nts_to_chunks.get(nonterminal);
    // Filter out chunks using the same rule (we want diversity)
    let alternatives = chunks.filter(|c| c.rule_id != rule_id);
    // Pick one at random
    alternatives.choose(&mut rng)
}
```

The ChunkStore is wrapped in `ChunkStoreWrapper` with a `RwLock` and `AtomicBool` for thread-safe access (only one thread can modify it at a time).

---

## 13. The State Machine — Input Processing Pipeline

**Source:** `fuzzer/src/main.rs:48-173`, `fuzzer/src/queue.rs:17-21`

Each queue item progresses through three stages:

```
                    ┌─────────┐
                    │  Init   │  Minimize the input (make it smaller
                    │  (0)    │  while keeping the same coverage)
                    └────┬────┘
                         │ minimization complete
                         ▼
                    ┌─────────┐
                    │   Det   │  Try every alternative rule at every
                    │ (cyc,i) │  node (systematic exploration)
                    └────┬────┘
                         │ all cycles complete
                         ▼
                    ┌─────────┐
                    │ Random  │  Run havoc, splice, and havoc_recursion
                    │         │  mutations (forever, until next round)
                    └─────────┘
```

### 13.1 Init Stage — Minimization

```rust
InputState::Init(start_index)
```

The input is minimized in batches of 200 nodes at a time. For each node, try replacing its subtree with the smallest possible tree for that nonterminal. If the replacement still triggers the same coverage bits, keep it (the input is now smaller).

Two types of minimization happen:
- **minimize_tree** — Replace subtrees with minimal-size alternatives
- **minimize_rec** — If a node has an ancestor with the same nonterminal, try replacing the ancestor's subtree with just the descendant's subtree (collapsing recursion)

When done, the minimized tree is added to the ChunkStore, and recursion info is computed.

### 13.2 Det Stage — Deterministic Mutation

```rust
InputState::Det((cycle, start_index))
```

For each node, try every alternative rule. This runs for `number_of_deterministic_mutations` cycles. Between deterministic steps, splice, havoc, and havoc_recursion also run.

When RL is enabled (`config.rl_enabled`), the Det stage is **skipped** — the DQN agent can choose Det as action=3 during the Random stage.

### 13.3 Random Stage — Ongoing Mutation

```rust
InputState::Random
```

The input stays here forever (until the next queue round). Each time it's processed:

**Without RL:** Run splice (100x), havoc (100x), and havoc_recursion (20x).

**With RL:** The DQN agent picks ONE strategy per processing step:
- Action 0: Havoc
- Action 1: Havoc Recursion
- Action 2: Splice
- Action 3: Deterministic (1 step)
- Action 4: Generate (new random input)

---

## 14. Multi-Threading Architecture

**Source:** `fuzzer/src/main.rs:312-637`

### 14.1 Thread Layout

```
┌─────────────────────────────────────────────┐
│                  main()                      │
│                                             │
│  1. Load config (config.ron)                │
│  2. Load grammar (Python → Context)         │
│  3. Initialize context (calc_min_len, etc.) │
│  4. Create shared state (GlobalSharedState) │
│  5. Create shared ChunkStore                │
│  6. Optionally create DqnTrainer            │
│  7. Spawn N fuzzing threads                 │
│  8. Spawn 1 status thread                   │
└─────────────────────────────────────────────┘
         │
         ├── Thread "fuzzer_1" ──→ fuzzing_thread()
         ├── Thread "fuzzer_2" ──→ fuzzing_thread()
         ├── ...
         ├── Thread "fuzzer_N" ──→ fuzzing_thread()
         └── Thread "status"   ──→ prints dashboard every 1s
```

### 14.2 Shared State

All threads share:
- `Arc<Mutex<GlobalSharedState>>` — Queue, bitmaps, counters
- `Arc<ChunkStoreWrapper>` — ChunkStore with RwLock
- `Context` (cloned per thread — each thread has its own copy)
- `Arc<Mutex<DqnTrainer>>` (when RL enabled — shared replay buffer + network)

Each thread has its own:
- `ForkServer` — its own subprocess
- `Fuzzer` — its own execution counter and dedup buffer
- `FuzzingState` — its own mutator scratchpad
- `DqnWorker` (when RL enabled — its own epsilon, exec counter)

### 14.3 The Fuzzing Loop (main.rs:224-309)

```
loop {
    item = global_state.queue.pop()
    
    if item exists:
        process_input(item)  // Init → Det → Random
        if subprocess died:
            restart fork server
        global_state.queue.finished(item)
    else:
        // Queue empty — generate fresh inputs
        for _ in 0..number_of_generate_inputs:
            state.generate_random("START")
        global_state.queue.new_round()  // recycle processed items
    
    // Update global stats from thread-local counters
    global_state.execution_count += delta
    global_state.bits_found_by_* += local.bits_found_by_*
}
```

---

## 15. Python Grammars — Writing Rules

**Source:** `fuzzer/src/python_grammar_loader.rs`, `grammars/sqlite_patterns.py`

### 15.1 How Python Grammars are Loaded

The fuzzer loads grammars through PyO3 (Python-Rust bridge):

1. `python_grammar_loader.rs` creates a `PyContext` Python object
2. It executes the Python grammar file with `ctx` as a local variable
3. The Python code calls `ctx.rule(...)`, `ctx.script(...)`, `ctx.regex(...)` — each call registers a rule in the Rust `Context`
4. After execution, the Rust `Context` is extracted and used by the fuzzer

### 15.2 Grammar API

```python
# ctx is automatically provided — it's a PyContext instance

# Plain rule: template with nonterminal references in {Curly-Braces}
ctx.rule("Nonterminal-Name", "literal text {Other-Nonterminal} more text")

# Weighted rule: higher weight = more likely to be selected
ctx.rule("Sql-Stmt", "{Select-Stmt}", weight=3.0)

# Script rule: Python callback for complex transformations
ctx.script("Formatted", ["Raw-Value"], lambda v: f"({v.decode()})")

# Regex rule: generate strings matching a regex pattern
ctx.regex("Identifier", "[a-z][a-z0-9_]{0,15}")
```

### 15.3 Nonterminal Naming Rules

Nonterminal names must:
- Start with a capital letter: `Select-Stmt` (good), `select-stmt` (bad)
- Contain only: `[A-Za-z0-9_-]`
- Be enclosed in `{}` when referenced: `{Select-Stmt}`

### 15.4 Grammar Design Principles

**1. START is required:**
Every grammar must have a `START` nonterminal. This is the root of every generated tree.

**2. Every nonterminal must be reachable and terminable:**
- Reachable: there must be a path from `START` to every nonterminal
- Terminable: every nonterminal must have at least one rule that doesn't recurse (a "base case")

```python
# BROKEN — Expr has no base case, infinite recursion
ctx.rule("Expr", "{Expr} + {Expr}")

# FIXED — add a terminal rule
ctx.rule("Expr", "{Expr} + {Expr}")
ctx.rule("Expr", "1")  # base case!
```

**3. Use weights to guide generation:**

```python
# CVE-related patterns get high weights (generated more often)
ctx.rule("Sql-Stmt", "{Pattern-Boundary-Func}", weight=3.0)

# Boring statements get low weights (generated less often)
ctx.rule("Sql-Stmt", "{Drop-Stmt}", weight=0.2)
```

### 15.5 The sqlite_patterns.py Grammar Structure

```
START
  └── Sql-Stmt-List (semicolon-separated statements)
       └── Sql-Stmt (dispatches to one of ~25 statement types)
            ├── Layer 1: Base SQL (weight 0.2-1.0)
            │    ├── Select-Stmt, Insert-Stmt, Update-Stmt, ...
            │    ├── Create-Table-Stmt, Create-Index-Stmt, ...
            │    └── Pragma-Stmt, Analyze-Stmt, ...
            │
            ├── Layer 2: Stress templates (weight 1.5-3.0)
            │    ├── Deep-Nested-Select (5-level nesting)
            │    ├── Long-Join-Chain (4-table JOIN)
            │    ├── Recursive-CTE-Heavy
            │    ├── Window-Func-Complex
            │    └── Aggregate-Complex
            │
            └── CVE Patterns (weight 2.0-3.0)
                 ├── Pattern-DDL-DQL (CREATE → SELECT)
                 ├── Pattern-GenCol-Op (generated columns)
                 ├── Pattern-Compound (INTERSECT/EXCEPT)
                 ├── Pattern-Schema-Pragma (DDL → PRAGMA)
                 └── Pattern-Boundary-Func (edge-case args)
```

---

## 16. RL Integration — Adaptive Mutation (Phase 2+)

**Source:** `fuzzer/src/rl_hook.rs`, `fuzzer/src/dqn.rs`

### 16.1 The Problem

The five mutation strategies (havoc, havoc_rec, splice, det, generate) have different effectiveness at different points in a fuzzing campaign:
- Early on, **generate** finds lots of new coverage
- Mid-campaign, **splice** is effective (combines interesting fragments)
- Late campaign, **havoc_rec** might find deep bugs that others miss

A fixed strategy mix wastes time on strategies that aren't currently productive.

### 16.2 The Solution — DQN Agent

A Deep Q-Network (DQN) agent learns **which strategy to use** based on the current fuzzing state. It observes the fuzzer's state, picks a strategy, observes the outcome, and updates its neural network.

### 16.3 State Space (12 dimensions)

```rust
struct DqnState {
    coverage_delta: f32,      // New bits from last execution (normalized)
    total_coverage: f32,      // Total bitmap coverage fraction
    coverage_velocity: f32,   // EMA of coverage gain
    is_crash: f32,            // 1.0 if last exec crashed
    crash_rate: f32,          // EMA crash rate
    queue_size_norm: f32,     // Queue size / 10000
    exec_count_norm: f32,     // log10(exec_count) / 7
    havoc_ema: f32,           // Per-strategy reward EMAs
    havocrec_ema: f32,
    splice_ema: f32,
    det_ema: f32,
    generate_ema: f32,
}
```

### 16.4 Action Space (5 actions)

| Action | Strategy | Description |
|--------|----------|-------------|
| 0 | Havoc | Random subtree replacement (100x) |
| 1 | Havoc Rec | Recursive expansion (20x) |
| 2 | Splice | Cross-pollinate from ChunkStore (100x) |
| 3 | Det | One deterministic mutation step |
| 4 | Generate | Fresh random tree from START |

### 16.5 Reward Signal

```rust
fn compute_reward(coverage_delta, is_crash, is_timeout) -> f32 {
    let mut r = coverage_delta as f32;  // +1 per new bit
    if is_crash    { r += 10.0; }       // Crashes are very valuable
    if is_timeout  { r -= 1.0; }        // Timeouts waste time
    if coverage_delta == 0 && !is_crash { r -= 0.1; }  // Small penalty for no progress
    r
}
```

### 16.6 Neural Network Architecture

```
Input (12) → Dense(64, ReLU) → Dense(32, ReLU) → Output(5)
```

A small fully-connected network. Trained with:
- **Experience replay** — Ring buffer of 3000 transitions, sampled in mini-batches of 32
- **Target network** — Separate copy updated every 1000 training steps (stabilizes learning)
- **Epsilon-greedy exploration** — Starts at 100% random, decays to 5% over 50,000 steps
- **AdamW optimizer** — Learning rate 0.001

### 16.7 How it Integrates

```
fuzzing_thread() creates:
├── DefaultPolicy (when rl_enabled=false)
│   └── select_action() returns None → run all strategies
└── DqnPolicy (when rl_enabled=true)
    └── select_action() returns Some(action) → run only that strategy
    └── observe(action, outcome) → train the DQN
```

The DqnTrainer is shared across all threads via `Arc<Mutex<DqnTrainer>>`. Each thread has its own `DqnWorker` with its own epsilon and execution counter.

### 16.8 Enabling RL

In `config.ron`:
```ron
(
    rl_enabled: true,
    rl_epsilon_start: 1.0,
    rl_epsilon_end: 0.05,
    rl_epsilon_decay: 50000,
    rl_batch_size: 32,
    rl_replay_size: 3000,
    rl_gamma: 0.99,
    rl_lr: 0.001,
    rl_target_update: 1000,
    rl_train_interval: 100,
)
```

---

## 17. File Map — Where Everything Lives

```
rl-nautilus-phase-2/
├── fuzzer/src/                    # Main fuzzer binary
│   ├── main.rs                    # Entry point, fuzzing loop, threading
│   ├── config.rs                  # Config struct (deserialized from .ron)
│   ├── fuzzer.rs                  # Fuzzer struct — execution + coverage tracking
│   ├── state.rs                   # FuzzingState — mutation strategy dispatch
│   ├── queue.rs                   # Queue + QueueItem — manages interesting inputs
│   ├── shared_state.rs            # GlobalSharedState — thread-shared data
│   ├── python_grammar_loader.rs   # PyO3 bridge — loads Python grammars
│   ├── dqn.rs                     # DQN neural network + replay buffer
│   ├── rl_hook.rs                 # MutationPolicy trait + DqnPolicy
│   ├── rl_logger.rs               # RL training metrics logger
│   ├── generator.rs               # Standalone tree generator binary
│   ├── mutation_tester.rs         # Standalone mutation test binary
│   └── dqn_test.rs                # DQN unit test binary
│
├── grammartec/src/                # Grammar engine library
│   ├── context.rs                 # Central registry — rules, nonterminals, generation
│   ├── rule.rs                    # Rule types (Plain, Script, RegExp) + tokenizer
│   ├── tree.rs                    # Tree struct, unparsing, TreeMutation
│   ├── mutator.rs                 # Mutation algorithms (havoc, splice, det, minimize)
│   ├── chunkstore.rs              # Subtree library for splice mutations
│   ├── recursion_info.rs          # Pre-computed recursion pairs for havoc_rec
│   ├── newtypes.rs                # NTermID, RuleID, NodeID type wrappers
│   └── lib.rs                     # Crate root
│
├── forksrv/src/                   # Fork server library
│   ├── lib.rs                     # ForkServer — process management + shared memory
│   ├── exitreason.rs              # ExitReason enum (Normal, Signaled, Timeouted)
│   └── newtypes.rs                # SubprocessError type
│
├── regex_mutator/src/             # Regex-based string generator
│   └── lib.rs                     # generate() — random strings from regex HIR
│
├── harness/                       # C harness binaries
│   ├── sqlite_harness_patterns.c  # Blank-DB harness for pattern grammar
│   ├── sqlite_harness.c           # Pre-loaded-schema harness
│   ├── sqlite_harness_cve13434.c  # CVE-specific harness variant
│   └── Makefile                   # Build rules for harness binaries
│
├── grammars/                      # Python grammar definitions
│   ├── sqlite_patterns.py         # Main weighted pattern grammar (CVE-targeted)
│   ├── sqlite_patterns_uniform.py # Same patterns, uniform weights (ablation control)
│   ├── sqlite_attack.py           # Direct CVE attack grammar
│   ├── sqlite_generated.py        # Auto-generated grammar (from cve2grammar)
│   └── *.py                       # Other language grammars (JS, Lua, PHP, Ruby)
│
├── triage/                        # Post-fuzzing crash analysis (Python)
│   ├── stack_dedup.py             # Stack-trace-based deduplication
│   ├── fidelity_score.py          # Crash reproduction fidelity scoring
│   ├── cve_signatures.py          # CVE signature matching
│   ├── dedup.py                   # General deduplication
│   ├── minimize.py                # Input minimization
│   └── report.py                  # Report generation
│
├── scripts/                       # Evaluation and analysis scripts
│   ├── run_eval.sh                # Run a single fuzzing campaign
│   ├── run_ablation.sh            # Run ablation study (4 variants × 2 seeds)
│   ├── capture_coverage.py        # Extract coverage data from runs
│   └── analyze.py                 # Parse Nautilus logs + generate stats
│
├── cve_builds/                    # Pre-compiled SQLite versions with CVEs
│   ├── sqlite-3.30.1/sqlite3.c
│   ├── sqlite-3.31.1/sqlite3.c
│   ├── sqlite-3.32.0/sqlite3.c
│   └── sqlite-3.32.2/sqlite3.c
│
├── cve2grammar/                   # Grammar-building pipeline (vendored subtree)
│   ├── cve2grammar/               # Python package
│   └── tests/                     # Package tests
│
├── config.ron                     # Default fuzzer configuration
└── docs/                          # Documentation
```

---

## 18. Data Flow Diagram — End to End

```
┌──────────────────────────────────────────────────────────────────────┐
│                         STARTUP                                      │
│                                                                      │
│  config.ron ──parse──> Config                                        │
│  grammar.py ──PyO3───> Context ──initialize()──> Context (ready)    │
│                                                                      │
│  GlobalSharedState created (queue, bitmaps, counters)               │
│  ChunkStoreWrapper created                                           │
│  DqnTrainer created (if rl_enabled)                                 │
│  N fuzzing threads spawned                                           │
└──────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    EACH FUZZING THREAD                                │
│                                                                      │
│  ForkServer created (forks target binary, sets up shared mem)       │
│  FuzzingState created (holds Fuzzer + Mutator)                      │
│  MutationPolicy created (DefaultPolicy or DqnPolicy)               │
│                                                                      │
│  MAIN LOOP:                                                          │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ item = queue.pop()                                           │    │
│  │                                                              │    │
│  │ if item:                                                     │    │
│  │   ┌──────────────────────────────────────────────────────┐  │    │
│  │   │ process_input(item):                                  │  │    │
│  │   │                                                       │  │    │
│  │   │ Init: minimize(item) ──────────────────────────────> │  │    │
│  │   │   │ minimize_tree: try smaller subtrees              │  │    │
│  │   │   │ minimize_rec: collapse recursions                │  │    │
│  │   │   │ if done: add to ChunkStore, compute recursions  │  │    │
│  │   │   ▼                                                   │  │    │
│  │   │ Det: deterministic_tree_mutation(item) ────────────> │  │    │
│  │   │   │ for each node: try every alternative rule        │  │    │
│  │   │   │ also runs splice, havoc, havoc_rec between      │  │    │
│  │   │   ▼                                                   │  │    │
│  │   │ Random:                                               │  │    │
│  │   │   │ Without RL: splice(100) + havoc(100) + hrec(20) │  │    │
│  │   │   │ With RL:    policy.select_action() → one strat  │  │    │
│  │   │   │             policy.observe(action, outcome)      │  │    │
│  │   └──────────────────────────────────────────────────────┘  │    │
│  │                        │                                     │    │
│  │                        ▼                                     │    │
│  │   EACH MUTATION generates a TreeMutation                    │    │
│  │     │                                                        │    │
│  │     ▼                                                        │    │
│  │   tree.unparse_to_vec(ctx) → SQL bytes                      │    │
│  │     │                                                        │    │
│  │     ▼                                                        │    │
│  │   fuzzer.run_on_with_dedup(tree, reason, ctx)               │    │
│  │     │                                                        │    │
│  │     ├── input_is_known? → skip (dedup)                      │    │
│  │     │                                                        │    │
│  │     ▼                                                        │    │
│  │   forksrv.run(sql_bytes)                                    │    │
│  │     │ write sql to temp file                                │    │
│  │     │ send "go" to fork server                              │    │
│  │     │ fork server forks child                               │    │
│  │     │ child reads sql, runs sqlite3_exec(sql)               │    │
│  │     │ child exits (normal/crash/signal/timeout)             │    │
│  │     │ shared memory bitmap now has coverage data            │    │
│  │     ▼                                                        │    │
│  │   ExitReason                                                │    │
│  │     ├── Normal(223): ASan crash → save + count              │    │
│  │     ├── Normal(1): UBSan crash → save + count               │    │
│  │     ├── Signaled: signal crash → save + count               │    │
│  │     ├── Timeouted: → save                                   │    │
│  │     └── Normal(0): check for new coverage bits              │    │
│  │                       │                                      │    │
│  │                       ▼                                      │    │
│  │                 new_bits()?                                  │    │
│  │                   │                                          │    │
│  │                   ├── No new bits → done, next mutation      │    │
│  │                   │                                          │    │
│  │                   └── Yes! New coverage found!               │    │
│  │                         │                                    │    │
│  │                         ▼                                    │    │
│  │                 check_deterministic(5 re-runs)              │    │
│  │                         │                                    │    │
│  │                         ▼                                    │    │
│  │                 queue.add(tree, bitmap, exit_reason)         │    │
│  │                   │ saved to outputs/queue/                  │    │
│  │                   │ QueueItem starts in Init(0) state       │    │
│  │                                                              │    │
│  │ else (queue empty):                                          │    │
│  │   generate_random("START") × N                              │    │
│  │   queue.new_round() → recycle processed items               │    │
│  │                                                              │    │
│  │ Update global stats (execution_count, bits_found_by_*)      │    │
│  └─────────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 19. Troubleshooting Guide

### "Broken Grammar" panic at startup

**Cause:** A nonterminal has no base case (all rules are recursive).

**Fix:** Add a terminal rule:
```python
# BROKEN
ctx.rule("Expr", "{Expr} + {Expr}")

# FIXED
ctx.rule("Expr", "{Expr} + {Expr}")
ctx.rule("Expr", "1")  # <-- add this
```

**How to find it:** The error message lists the unproductive rules. Check which nonterminal they belong to.

### "no such nonterminal: X" panic

**Cause:** A rule references `{X}` but no rules define nonterminal `X`.

**Fix:** Add rules for the missing nonterminal, or fix the typo in the reference.

### Fork server hangs / "couldn't read child hello"

**Cause:** The target binary doesn't have AFL instrumentation, or it crashes during initialization.

**Fix:**
1. Compile with `afl-clang-fast`: `CC=afl-clang-fast make`
2. Check that the binary runs standalone: `./target_binary < /dev/null`
3. Increase startup timeout if ASan is slow to initialize

### 0 executions per second

**Cause:** Every execution is timing out.

**Fix:**
1. Increase `timeout_in_millis` in config.ron
2. Check if the harness is stuck (infinite loop in SQLite)
3. Test with a simple input: `echo "SELECT 1" | ./harness /dev/stdin`

### "minimize starved!" / "splice starved!" panic

**Cause:** The ChunkStore lock is held for >30 seconds. Usually means a thread crashed while holding the lock.

**Fix:** This is a bug — check for panics in other threads. Look at the full backtrace.

### No crashes found after hours

This is normal — not every campaign finds crashes. Try:
1. Verify the grammar generates valid SQL: `cargo run --bin generator -- -g grammars/your_grammar.py -t 10`
2. Check you're using a CVE-bearing SQLite version
3. Increase CVE-pattern weights in the grammar
4. Let it run longer (some CVEs need 12+ hours)

---

## 20. Glossary

| Term | Definition |
|------|-----------|
| **ASan** | AddressSanitizer — compiler tool that detects memory bugs (buffer overflow, use-after-free). Exits with code 223 when triggered. |
| **Bitmap** | Shared memory byte array where AFL instrumentation records which code branches execute. Each byte = one branch. |
| **ChunkStore** | Library of interesting subtrees harvested from coverage-increasing inputs. Used by splice mutation. |
| **Context** | Central grammar registry. Stores all rules, manages nonterminal IDs, handles tree generation. |
| **Coverage-guided** | Fuzzing approach that uses code coverage feedback to guide input generation toward new code paths. |
| **CVE** | Common Vulnerabilities and Exposures — publicly disclosed security bug. |
| **DQN** | Deep Q-Network — a reinforcement learning algorithm that learns an action-value function using a neural network. |
| **Fork server** | Optimization: start the target once, then `fork()` for each execution. ~100x faster than restarting. |
| **Grammar** | Set of rules describing the syntax of valid inputs. Used to generate structurally correct test cases. |
| **Harness** | Wrapper program that feeds fuzzer-generated input to the target (SQLite) and detects crashes. |
| **Havoc** | Mutation strategy: randomly replace subtrees with fresh random ones. |
| **Minimization** | Reducing input size while preserving the same coverage. Makes inputs easier to understand and store. |
| **Nonterminal** | A named symbol in a grammar (e.g., `Select-Stmt`). Can be expanded by applying rules. |
| **NodeID** | Index of a node in the pre-order tree array. |
| **NTermID** | Numeric ID for a nonterminal name. |
| **Pre-order** | Tree traversal: visit parent before children, left before right. Used for array-based tree storage. |
| **Replay buffer** | Circular buffer storing (state, action, reward, next_state) transitions for DQN training. |
| **RuleID** | Numeric ID for a grammar rule. |
| **Splice** | Mutation strategy: replace a subtree with one from a different interesting input. |
| **Terminal** | Literal text in a rule (e.g., `SELECT`, `FROM`). Not expanded further. |
| **Tree** | Internal representation of a generated input. Array of rules in pre-order, with sizes and parents. |
| **TreeMutation** | Zero-copy view of a tree with a subtree replaced. Avoids allocation for mutations that aren't interesting. |
| **UBSan** | UndefinedBehaviorSanitizer — compiler tool that detects undefined behavior (integer overflow, null deref). Exits with code 1. |
| **Unparse** | Convert a tree back to text (the actual input bytes). |
| **Weight** | Numeric value controlling how likely a rule is to be selected during generation. Higher = more likely. |
