# Measurement + Pattern Fidelity — Design Spec

**Date:** 2026-04-22
**Status:** Draft — awaiting review before implementation plan
**Supersedes:** Neither (complements `docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md`)
**Produces:**
- `triage/stack_dedup.py` — gdb-backtrace root-cause dedup (new)
- Changes to `scripts/run_eval.sh` and `exec.log` parsing for coverage capture
- `triage/fidelity_score.py` — per-pattern structural fidelity scorer (new)
- `grammars/sqlite_attack.py` — tightened per-pattern bodies + split loose/tight NTs
- `docs/attack-grammar-ablation-sqlite-3.31.1.md` — E2 ablation report

**Thesis claims served:**
1. *Attack-pattern grammars outperform full EBNF grammars on unique-root-cause bugs per CPU-hour* (needs A1 dedup to be measurable).
2. *Branch coverage scales with grammar fidelity, not grammar size* (needs A2 coverage capture).
3. *Tightening structural fidelity (B2) isolates the fidelity effect from the size effect* (needs A3 fidelity scorer + ablation E2).

---

## 1. Motivation

The 15-minute pilot (`docs/attack-grammar-pilot-sqlite-3.31.1.md`) surfaced three blocking problems:

1. **Dedup is blind.** `triage/dedup.py` fell back to SQL-byte hashing because crashes are SIGTRAP (SQLITE_DEBUG asserts) / SIGABRT without ASan frames. Visual inspection of the surviving 3-min attack workdir showed 12/12 crashes were `printf` variants of the *same* bug, but dedup reported 12 "unique." Every crash-count number in the thesis is currently meaningless.
2. **Coverage is invisible.** `scripts/run_eval.sh` does not capture Nautilus's `bits_found_by_*` counters. The pilot report has no coverage column, so the continuous proxy for grammar quality is absent.
3. **Patterns are structurally loose.** `Pattern-P13435` delegates its critical expression to `{Scalar-Subquery}` (6 alternatives, most wrong shapes). Probability of generating a CVE-13435-isomorphic SQL from this pattern is ~5%, which explains 0 CVE-13435 crashes in 15 min despite the pattern being nominally "present."

This spec fixes all three in parallel. **Track α** fixes measurement (A1 dedup, A2 coverage, A3 fidelity scorer). **Track β** fixes fidelity via B2 (loose/tight non-terminal split). **Track E** evaluates both via E2 (4-variant × 3-seed × 1-hour ablation).

---

## 2. Track α — Measurement fixes

### 2.1 A1 — Stack-level dedup (`triage/stack_dedup.py`)

**Input:** a workdir `outputs/signaled/` containing raw SQL crash files.

**Method:**
1. For each crash file, spawn `gdb --batch --ex "set args <crash-file>" --ex run --ex "bt 5" --ex quit <harness-binary>`.
2. Parse gdb's backtrace output to extract the top 5 frames. Each frame → `"<function-name>:<source-file>:<line>"`. Skip frames in libc, libasan, gdb itself, and the harness wrapper (keep only SQLite-library frames).
3. Compute `sha256(joined-frames)` as the crash's root-cause hash.
4. Group crashes by hash. One representative per group.

**Fallback for SIGTRAP from SQLITE_DEBUG asserts:**
SQLite `SQLITE_DEBUG` builds fire `abort()` via `NEVER()` / `ALWAYS()` macros. Stack frames include the assertion source line (`sqlite3.c:LINE_NUMBER`), which IS the root-cause signature we want — even without an ASan frame. So the gdb path works even for SIGTRAP crashes; it just requires a debug-info-enabled harness binary.

**Prerequisite:** harness binaries must be compiled with `-g` (debug info) and `-O0` or `-O1` (inlining-free for accurate frames). Current `harness/Makefile` targets already use `-g -O0` per prior inspection — the implementation plan's first task must verify this before writing the dedup script.

**Output:** a JSON file written to the workdir:
```json
{
  "total_crashes": 18,
  "unique_root_causes": 2,
  "clusters": [
    {
      "hash": "abc123...",
      "count": 14,
      "representative": "5_000018093",
      "top_frame": "sqlite3_str_vappendf:sqlite3.c:28528",
      "example_sql": "SELECT printf('abc', -2147483648, ...);"
    }
  ]
}
```

**CLI:**
```bash
python3 triage/stack_dedup.py <workdir> --harness <harness-binary> [--output <json-path>]
```

**Correctness tests:**
- Unit test: feed 3 synthetic crash files that all crash at the same source line. Assert `unique_root_causes == 1`.
- Integration test: run against the 12-crash 3-min workdir if still available. Assert `unique_root_causes` ∈ {1, 2} (either all printf, or printf-plus-group_concat arity variant).

### 2.2 A2 — Coverage capture in `run_eval.sh`

**Current state:** Nautilus writes `exec.log` to the workdir. The log contains periodic `Execution Count: NNN` lines. Whether it writes `bits_found_by_*` counters is the open question the implementation plan's first task must resolve via `grep -rn "bits_found" fuzzer/src/`.

**Fix:** extend `run_eval.sh` to:
1. At run start, capture timestamp.
2. At run end (after `timeout` kills the fuzzer), parse `exec.log` for the last line containing Nautilus's end-of-run summary.
3. Write `coverage.json` to workdir with:
   ```json
   {
     "total_executions": 180234,
     "duration_seconds": 3600,
     "exec_per_sec": 50.06,
     "bits_found": 1847,
     "bits_found_new": 1203,
     "bits_found_mutation": 644,
     "bits_found_deterministic": 0,
     "queue_final": 942,
     "signaled_final": 18,
     "timeout_final": 6
   }
   ```

**Minimum-viable fallback:** if the Nautilus log does not already contain per-type bitmap counts, capture only `total_executions` + queue/signaled/timeout file counts for v1 of A2. Coverage-over-time is the ideal but requires fuzzer-source changes — deferred.

**Scope boundary:** per-checkpoint coverage (the time-series curve) requires modifying `fuzzer/src/fuzzer.rs` to dump every N seconds. That is explicitly deferred to a follow-up spec. v1 captures end-of-run coverage only.

### 2.3 A3 — Per-pattern fidelity scorer (`triage/fidelity_score.py`)

**Purpose:** given an attack pattern in `grammars/sqlite_attack.py`, measure "what fraction of the SQL it generates structurally matches the source CVE PoC."

**Method:**
1. Parse the source CVE PoC (from `docs/cve-list.md`) to extract its *structural signature* — a set of required AST node types. For CVE-13435:
   ```
   required_nodes = {
     "CREATE_TABLE_with_UNIQUE_column",
     "SELECT_with_JOIN",
     "NATURAL_JOIN",
     "IN_subquery",
     "nested_SELECT",
     "coalesce_call",
     "window_function_over",
     "aggregate_function_sum",
   }
   ```
2. For each pattern, drive the Nautilus generator to produce N=500 samples biased toward that pattern's Sql-Stmt alternative. Implementation: temporarily weight the pattern's Sql-Stmt dispatch rule to 100.0, all other Sql-Stmt alternatives to 0.0, and call the existing `target/release/generator` binary.
3. Parse each sample with `tree-sitter-sqlite`. The repo already has `docs/tree-sitter-sqlite.ebnf`; A3 requires the `tree-sitter` Python package at runtime.
4. For each sample, count how many of the pattern's required nodes are present.
5. Fidelity score = `(samples where all required nodes present) / N`.

**Output JSON:**
```json
{
  "patterns": [
    {
      "name": "Pattern-P13435",
      "cve": "CVE-2020-13435",
      "samples_generated": 500,
      "required_nodes": ["CREATE_TABLE_with_UNIQUE_column", "NATURAL_JOIN", "coalesce_call", "window_function_over"],
      "fidelity_score": 0.048,
      "samples_with_all_required": 24,
      "samples_missing_node": {
        "NATURAL_JOIN": 317,
        "coalesce_call": 421,
        "window_function_over": 438
      }
    }
  ]
}
```

**Integration with B2:** after B2 ships, A3 reports fidelity for each pattern TWICE — once with the tight NT in use, and once with the corresponding loose NT substituted (by temporarily editing the grammar file). This produces the ablation headline: "Tight-NT pattern fidelity is X%, loose-NT fidelity is Y% — tight reaches CVE isomorphism reliably, loose preserves cross-pattern splice combination."

**CLI:**
```bash
python3 triage/fidelity_score.py \
  --grammar grammars/sqlite_attack.py \
  --pattern-spec docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md \
  --samples 500 \
  --output docs/fidelity-report.json
```

**Dependency fallback:** if `tree-sitter` Python package installation is blocked in the target environment, fallback to a regex-based structural matcher — less precise, but no deps. The plan's task 1 verifies the dependency path before committing to tree-sitter.

---

## 3. Track β — Pattern fidelity fix (B2)

### 3.1 Design principle

For each attack pattern with low fidelity, split its critical structural expressions into:

- **Tight non-terminal** (pattern-specific): matches the CVE PoC's structural signature with ≥80% fidelity on synthesis.
- **Loose shared non-terminal** (cross-pattern reusable): the original general-purpose NT, kept for splice mutation across patterns.

The pattern rule in §6 references the tight NT directly. The loose NT remains in §5 so other patterns and mutation can use it. Tight NTs have exactly ONE production each — they're skeletons, not composition points. Composition happens INSIDE them via the vocabulary NTs (`{Window-Func-Call}`, `{Agg-Func-Call}`, `{Col-Ref}`) which remain shared and loose.

### 3.2 Specific NT splits required

Mapped from the 15-minute pilot's 0-crash classes (P13435, P9327) and the corpus CVE PoCs:

| Pattern | Currently delegates to (loose) | Add tight variant |
|---|---|---|
| `Pattern-P13435` | `Scalar-Subquery` | `Scalar-Subquery-CoalesceWindow` — strictly `SELECT (SELECT coalesce({Window-Func-Call}, {Agg-Func-Call})) FROM {Table-Name} {Alias} WHERE {Col-Ref}` |
| `Pattern-P13435` | `Join-Chain` | `Join-Chain-NaturalPair` — strictly `JOIN {Table-Name} {Alias} ON {Expr} NATURAL JOIN {Table-Name}` |
| `Pattern-P9327` | `Join-Chain` | `Join-Chain-CommaJoin-Pair` — strictly `, {Table-Name}` (comma-join suffix; prepended to `FROM {View-Name}` in the pattern body to form a two-table comma-join) |
| `Pattern-P9327` | `GenCol-Def` | `GenCol-Def-SelfRef` — strictly `{Col-Name} AS ({Col-Name}) UNIQUE` (generated column referencing itself; corpus-exact from CVE-9327) |
| `Pattern-P19646` | `GenCol-Def` | `GenCol-Def-NotNull` — strictly `{Col-Name} NOT NULL GENERATED ALWAYS AS ({Boolean-Expr})` (corpus-exact from CVE-19646) |
| `Pattern-P15358` | `View-Def` | `View-Def-OrderedSelect` — strictly `CREATE VIEW {View-Name} AS SELECT {Col-Name} FROM {Table-Name} ORDER BY {Col-Name}` (the VIEW shape that triggers the INTERSECT read-past) |
| `Pattern-P13871` | `Scalar-Subquery` | `Scalar-Subquery-HavingWindow` — strictly `SELECT {Col-Ref} FROM {Table-Name} GROUP BY {Col-Ref} HAVING ({Coalesce-Window-Expr})` (the HAVING + window shape from CVE-13871) |

### 3.3 Example rewrite — Pattern-P13435

BEFORE:
```python
ctx.rule("Pattern-P13435",
    "CREATE TABLE {Table-Name}({Col-Name} UNIQUE);\n"
    "SELECT {Col-Ref} FROM {Table-Name} {Join-Chain} "
    "WHERE {Col-Ref} IN (({Scalar-Subquery}))")
```

AFTER:
```python
ctx.rule("Pattern-P13435",
    "CREATE TABLE {Table-Name}({Col-Name} UNIQUE);\n"
    "SELECT {Col-Ref} FROM {Table-Name} {Join-Chain-NaturalPair} "
    "WHERE {Col-Ref} IN (({Scalar-Subquery-CoalesceWindow}))")

ctx.rule("Join-Chain-NaturalPair",
    "JOIN {Table-Name} {Alias} ON {Expr} NATURAL JOIN {Table-Name}")

ctx.rule("Scalar-Subquery-CoalesceWindow",
    "SELECT (SELECT coalesce({Window-Func-Call}, {Agg-Func-Call})) "
    "FROM {Table-Name} {Alias} WHERE {Col-Ref}")
```

### 3.4 Cost and line budget

~7 tight NT definitions × 3-5 lines each = ~25 new grammar lines. 7 pattern-body edits × 0 line delta = 0 net new lines in §6.

Current file: 426 lines. Post-B2 projection: ~450-460 lines. The attack-pattern-grammar-design spec §9 line budget was ~365 + 20% tolerance = ~438. **B2 will overrun §9's original budget by ~20 lines.** Acceptable — the original budget didn't anticipate the tight/loose split. The implementation plan updates §9's line budget to ~460 as a non-behavioral spec amendment commit.

### 3.5 What B2 does NOT do

- Does NOT change §4 vocabulary (literals, identifiers stay as-is).
- Does NOT change §7 target symbols (Builtin-Func etc.).
- Does NOT add weights.
- Does NOT change `Sql-Stmt` dispatch — each pattern is still equally likely under Nautilus's uniform scheduler.
- Does NOT touch `grammars/sqlite_patterns.py` or `grammars/sqlite_patterns_uniform.py` — those are the ablation baselines, and modifying them invalidates the control.

---

## 4. Track E — Evaluation (E2 ablation)

### 4.1 Variants under test

| Variant | File / ref | Purpose |
|---|---|---|
| **attack_v1** | `grammars/sqlite_attack.py` at commit `2298743` (tagged `attack-v1-frozen`) | Baseline — the loose grammar from the first plan |
| **attack_v2** | `grammars/sqlite_attack.py` at HEAD after B2 | The tight-NT grammar |
| **patterns** | `grammars/sqlite_patterns.py` | Existing 1009-line baseline (weighted EBNF + patterns) |
| **uniform** | `grammars/sqlite_patterns_uniform.py` | Existing flood baseline (same rules as patterns, flat weights) |

Before E2 runs, tag `git tag attack-v1-frozen 2298743` so attack_v1 is reproducible across sessions.

### 4.2 Matrix

**4 variants × 3 seeds × 1 target (sqlite-3.31.1) × 1 duration (3600s) = 12 runs.**

Seeds: `{2026, 2027, 2028}`. If Nautilus has no seed-control surface, fall back to 3 independent runs as a variance-estimate floor (weaker but still better than n=1).

**Seed-control investigation:** implementation plan task 1 must `grep -rn "seed\|rng" fuzzer/src/ grammartec/src/` and decide between (a) adding seed support to `config.ron`, (b) wrapping the fuzzer with `RNG_SEED=N` env var, or (c) accepting independent-runs variance.

### 4.3 Metrics captured per run

From A1 (`dedup.json`) + A2 (`coverage.json`) + existing file counts:
- `total_executions`
- `exec_per_sec`
- `bits_found` (total coverage bits; end-of-run per A2 v1 scope)
- `signaled_crashes_total`
- **`unique_root_causes`** ← new headline metric enabled by A1
- `timeouts`
- `queue_final`
- Per-CVE-class hit (Y/N per 6 corpus CVEs; keeps regex classifier with known limitations)

Plus from A3 (once per grammar variant, not per seed):
- Per-pattern fidelity score (8 patterns)

### 4.4 Statistical analysis

For each metric × variant × 3 seeds, compute:
- mean
- standard deviation
- min/max

Primary comparison: Mann-Whitney U test on `unique_root_causes` between attack_v1 and attack_v2 (n=3 each). Report effect size as median difference.

**Honest caveat to publish in the report:** n=3 seeds is underpowered for strong statistical claims. The ablation's purpose is to *detect direction*, not *prove significance*. If attack_v2 ≥ 2× attack_v1 on `unique_root_causes` in all 3 seeds, thesis can claim improvement. If direction is noisy, follow-up spec bumps seeds to 10+.

### 4.5 Acceptance criteria

Thesis-positive if all four hold:

1. **attack_v2 finds ≥ 5 of 6 CVE classes** (up from 4/6 at 15 min).
2. **attack_v2 unique_root_causes > attack_v1 unique_root_causes** in all 3 seeds (median ≥ 2× improvement).
3. **Per-pattern fidelity scores from A3 show tight-NT patterns ≥ 50% fidelity** (vs ~5% for loose).
4. **Coverage (`bits_found`) for attack_v2 ≥ 90% of patterns-baseline coverage** — demonstrating tightening didn't over-constrain the grammar into a narrow corner.

Outcome branches:
- Criterion 1 fails but 2+3 hold → partial win; next spec adds weights to steer under-covered patterns.
- Criterion 2 fails → tightening didn't help; next deliverable is a post-mortem spec, not a weights spec.
- Criterion 3 fails → A3 is measuring wrong OR tight NTs still too loose; fix A3 first.
- Criterion 4 fails → over-constrained; roll back to B1-style partial tightening.

### 4.6 E2 is NOT the final evaluation

E2 gates the decision to run E3 (full 24h × 4 SQLite versions). E3 is explicitly deferred to a follow-up spec contingent on E2 being thesis-positive.

---

## 5. Execution sequencing

Tracks α and β run **mostly in parallel** with one dependency (A3 after B2's grammar changes land):

```
Day 1:  A2 coverage capture (parallel)   |   B2 NT splits + pattern rewrites (parallel)
Day 2:  A1 stack dedup      (parallel)   |   B2 smoke test + commit (parallel)
Day 3:  A3 fidelity scorer  (sequential after B2 — reports on both tight and loose NTs)
Day 4:  Tag attack-v1-frozen; run E2 (~12 hrs wall time on 1 CPU; ~4 hrs on 3 cores)
Day 5:  Analyze E2; write ablation report
```

Total ~5 working days.

**A3 depends on B2's grammar changes:** A3 parses samples from individual patterns. If B2 introduces `Scalar-Subquery-CoalesceWindow`, A3 must test fidelity of BOTH the tight NT in isolation AND the pattern that uses it. The implementation plan sequences A3 strictly after B2's grammar changes land.

**A3 does NOT depend on A1:** fidelity measurement is structural parsing, not crash outcome. They can ship in any order.

---

## 6. Open questions / deferrals

- **Weights.** Explicitly not in this spec. If E2 fails criterion 1 (coverage breadth), the follow-up is a weights spec.
- **Coverage-over-time curves.** Requires fuzzer-source changes (periodic dump). Deferred.
- **Harness debug info.** Assumed present (`-g -O0`); verify in plan task 1. If absent, rebuilding all 4 harness binaries is in-scope.
- **tree-sitter-sqlite dependency.** A3 needs it. Plan task 1 verifies installability; if blocked, fallback to regex-structural matcher.
- **E3 full campaign.** Deferred; scheduled only after E2 is positive.
- **cve2grammar LLM auto-generation integration.** Separate thesis contribution; not part of this spec.

---

## 7. References

- Pilot report: `docs/attack-grammar-pilot-sqlite-3.31.1.md` — the 15-min result motivating this spec.
- Grammar spec: `docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md` — §5, §6, §7; this spec's B2 updates those sections' line budgets.
- Attack grammar: `grammars/sqlite_attack.py` at commit `2298743` (to be tagged `attack-v1-frozen`).
- Nautilus paper: `docs/NDSS19_Nautilus.pdf` — §VI coverage-first evaluation methodology (A2's justification).
- CVE corpus: `docs/cve-list.md` — A3's ground-truth for required structural nodes per CVE.
- Existing dedup: `triage/dedup.py` — A1 replaces its fallback hashing with stack-based hashing.
- Tree-sitter grammar: `docs/tree-sitter-sqlite.ebnf` — A3's parser source.

---

**End of design spec. Awaiting user review before implementation plan.**
