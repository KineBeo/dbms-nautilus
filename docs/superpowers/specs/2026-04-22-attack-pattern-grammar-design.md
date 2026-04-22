# Attack-Pattern Grammar for SQLite — Design Spec

**Date:** 2026-04-22
**Status:** Draft — awaiting review before implementation plan
**Supersedes:** Neither (complements `grammars/sqlite_patterns.py`)
**Produces:** `grammars/sqlite_attack.py` (new artifact, ~365 lines, 8 attack patterns)
**Thesis claim served:** *Small, CVE-distilled attack-pattern grammars outperform full EBNF grammars in DBMS fuzzing, measured in unique bugs per CPU-hour.*

---

## 1. Motivation

The Nautilus NDSS '19 paper [1, §VI-B "Case Study: Finding CVEs"] documents a specific
grammar-design procedure that produced CVEs in mruby. The procedure is:

1. Start from a general public grammar of the target language.
2. Inspect the target's CVE history.
3. Observe which language features are actually responsible for bugs (versus
   which add variance without contributing to crashes).
4. Aggressively shrink the grammar — small identifier pool, small integer
   pool, small string pool, one canonical form per syntactic construct.
5. Add target-specific symbols (class names, method names, built-ins) from
   documentation as explicit terminals.
6. Let coverage feedback + grammar-aware mutation (splicing, subtree,
   random-recursive) handle depth and combination — do not encode depth in the
   grammar.

The current `grammars/sqlite_patterns.py` (1009 lines, 159 rules) already
encodes CVE-derived structural patterns (P1–P7), but still contains the "flood"
layer Nautilus shrinks away — 11 table identifiers, 15 integer literals, 7
Select-Stmt variants, redundant join forms, hand-coded nesting rules, etc.

`sqlite_patterns_uniform.py` is the same rule set with flat weights — the
ablation baseline, not a shrink.

**This spec defines a new grammar file, `grammars/sqlite_attack.py`, produced
by applying the Nautilus-mruby procedure to our 6-CVE SQLite corpus end-to-end.**
Every rule in the resulting file traces to either a CVE PoC, a boundary
condition in a CVE, or a documented SQLite module with CVE history.

---

## 2. Corpus

The 6 CVEs from `docs/cve-list.md`, with the simplified PoC used as vocabulary
source. (Full PoCs retained in `docs/cve-list.md`; excerpts here are the
minimum reproducers used for token extraction.)

### CVE-2020-15358 — heap read-past (affects ≤3.32.2)

```sql
CREATE TABLE t1(c1); INSERT INTO t1 VALUES(12),(123),(1234),(NULL),('abc');
CREATE TABLE t2(c2); INSERT INTO t2 VALUES(44),(55),(123);
CREATE TABLE t3(c3,c4); INSERT INTO t3 VALUES(66,1),(123,2),(77,3);
CREATE VIEW t5 AS SELECT c3 FROM t3 ORDER BY c4;
SELECT * FROM t1, t2 WHERE c1=(SELECT 123 INTERSECT SELECT c2 FROM t5) AND c1=123;
```

### CVE-2020-13871 — use-after-free (affects 3.32.2)

```sql
CREATE TABLE a(b);
SELECT (SELECT b FROM a GROUP BY b
        HAVING (NULL AND b IN (
          (SELECT COUNT() OVER(ORDER BY b) =
                  lead(b) OVER(ORDER BY 3.100000 * SUM(DISTINCT
                    CASE WHEN b LIKE 'SM PACK' THEN b*b ELSE 0 END) / b))))
       ) FROM a
EXCEPT SELECT b FROM a ORDER BY b,b,b;
```

### CVE-2020-13435 — NULL ptr deref (affects ≤3.32.0)

```sql
CREATE TABLE a(c UNIQUE);
SELECT a.c FROM a JOIN a b ON 3 = a.c NATURAL JOIN a
 WHERE a.c IN ((SELECT (SELECT coalesce(lead(2) OVER(), SUM(c)))
                FROM a d WHERE a.c));
```

### CVE-2020-13434 — integer overflow in printf (affects all since 3.8.3)

Original PoC (as reported, fuzz-found shape with noise):
```sql
CREATE TABLE a(b DOUBLE CHECK( NOT CASE WHEN printf(b, b) THEN 0 END) UNIQUE ON CONFLICT REPLACE);
CREATE TRIGGER c INSERT ON a BEGIN INSERT INTO a SELECT group_concat(b, 2147483647) FROM a; END;
INSERT INTO a(b, b, b) VALUES (NULL, 9, 3);
UPDATE a SET b = 0;
INSERT INTO a VALUES ('GERMANY''s%'), ('Y'), ('Brand#23');
```

Simplified PoC (drh, 2020-05-23 — root-cause isolation):
```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

**Two distinct code paths** this CVE exercises:
1. **SELECT-time boundary-int sink** — drh's one-liner; fault is in
   `sqlite3_str_vappendf` when precision argument is `INT32_MAX`.
2. **INSERT-time boundary-int sink via TRIGGER+group_concat** — original PoC;
   `group_concat(b, 2147483647)` inside a trigger body exercises the
   trigger-compiler path and aggregate argument path separately.

Both paths are encoded as separate patterns (see §6: `P-BOUNDARY-FUNC` and
`P-TRIGGER-GROUPCONCAT`). Extracting two patterns from one CVE strengthens
the attack-pattern-family claim — the grammar should find the bug via
either code path.

### CVE-2020-9327 — uninitialized pointer read (affects ≤3.31.1)

```sql
CREATE TABLE v0(v3, v1 AS (v1) UNIQUE);
CREATE TABLE v5(v6 UNIQUE, v7 UNIQUE);
CREATE VIEW v8(v9) AS SELECT coalesce(v3, v1) FROM v0 WHERE v1 IN ('MED BOX');
SELECT * FROM v8 JOIN v5 WHERE 0 > v7 AND v9 OR v6 = 's%';
```

### CVE-2019-19646 — infinite loop on integrity_check (affects ≤3.30.1)

```sql
CREATE TABLE t0 (c0, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0));
INSERT INTO t0(c0) VALUES (0);
PRAGMA integrity_check;
```

---

## 3. Six-Step Derivation Procedure

The grammar is derived by executing these six steps in order against the
corpus. Each step is deterministic given the corpus; re-running with an
expanded corpus produces an expanded grammar.

### Step 1 — Token extraction

For each PoC, extract identifiers, literals, SQL keywords, function names,
pragmas, and column types. Record provenance (which CVE the token came from).

### Step 2 — Vocabulary shrink

For each token class, keep the minimum set that (a) covers the corpus and
(b) adds documented boundary values (e.g., `INT32_MAX`, `INT32_MIN`, `NULL`,
LIKE metachars). Delete everything else.

### Step 3 — Canonical-form selection

For each SQL syntactic construct with multiple equivalent forms
(`INNER JOIN` vs `JOIN`, `CREATE TABLE` vs `CREATE TEMP TABLE`, etc.), keep
only the form(s) that appear in the corpus. Delete redundant synonyms.

### Step 4 — Attack-pattern abstraction

For each CVE, abstract its PoC into a structural skeleton — replace concrete
table names, column names, literal values with non-terminals. The skeleton is
the pattern; the non-terminals expand to shrunk vocabulary from Step 2.

### Step 5 — Shared non-terminal decomposition

Factor common sub-expressions out of patterns into shared non-terminals
(`Coalesce-Window-Expr`, `Join-Chain`, `Scalar-Subquery`, etc.) so that
Nautilus's splice mutator can recombine sub-expressions *across* patterns —
producing structural hybrids that no single CVE covers.

### Step 6 — Target-specific symbol injection

Add terminals drawn from SQLite documentation for modules with CVE history:
FTS5, JSON1, RTree, Geopoly, specific PRAGMAs, specific built-in functions.
These expand the reachable code surface beyond the corpus without bloating
grammatical variance.

---

## 4. Final Vocabulary (Steps 1–2)

Every entry has provenance. Tokens without provenance are boundary values
justified by SQLite internals (e.g., INT32 limits, LIKE metachars, NULL).

### 4.1 Identifiers

| Non-terminal | Values | Provenance |
|---|---|---|
| `Table-Name` | `a`, `t1`, `t2`, `t3` | `a` ∈ {13434, 13435, 13871, 19646}; `t1/t2/t3` ∈ {15358} |
| `Col-Name` | `b`, `c`, `c1`, `c2` | `b` ∈ {13434, 13871, 19646}; `c` ∈ {13435}; `c1/c2/c3` ∈ {15358}; `c2` kept as second-col alias |
| `View-Name` | `v1`, `v2` | `v8` ∈ {9327}; `t5` ∈ {15358} — kept minimal |
| `Alias` | `x`, `y` | For `FROM t AS x`; not in corpus but needed for non-trivial JOIN aliasing (e.g., 13435's `JOIN a b`) |

### 4.2 Literals

| Non-terminal | Values | Provenance |
|---|---|---|
| `Int-Lit` | `0`, `1`, `2`, `3`, `9`, `123`, `2147483647`, `-2147483648`, `-1` | `0/1/2` generic; `3`/`9` ∈ {13434 original PoC `VALUES(NULL,9,3)`}; `3` also ∈ {13435 `ON 3 = a.c`}; `123` ∈ {15358}; INT32 boundaries ∈ {13434 printf/group_concat arg} |
| `Real-Lit` | `0.01`, `3.1` | `0.01` ∈ {13434}; `3.1` ∈ {13871 `3.100000`} |
| `Str-Lit` | `'abc'`, `'SM PACK'`, `'s%'`, `'Y'`, `'MED BOX'`, `'GERMANY''s%'`, `'Brand#23'` | Corpus-exact from {15358, 13871, 9327, 13434 original PoC}; `'s%'`/`'GERMANY''s%'` exercise LIKE metachar + embedded single-quote escape |
| `Blob-Lit` | `x'00'`, `x'ff'`, `x'4142'` | Not in corpus; SQLite BLOB boundary values for FTS5/encoding code paths |
| `Null-Lit` | `NULL` | {15358, 13434, 13871} |

### 4.3 Types and collations

| Non-terminal | Values | Provenance |
|---|---|---|
| `Type-Name` | `INTEGER`, `DOUBLE`, `TEXT`, `BLOB` | `DOUBLE` ∈ {13434}; `INTEGER` implicit in 15358; `TEXT/BLOB` minimum for affinity coverage |
| `Collation-Name` | `BINARY`, `NOCASE`, `RTRIM` | SQLite built-ins; documented bugs in BINARY/NOCASE |

---

## 5. Canonical-Form Cuts (Step 3)

The following redundant or unused forms are **deleted** from the grammar.
Each cut is justified by absence from the corpus and absence from SQLite's
recent CVE history.

| Construct | Variants SQL allows | Kept | Deleted | Reason |
|---|---|---|---|---|
| Create table | `CREATE TABLE`, `CREATE TEMP TABLE`, `CREATE TEMPORARY TABLE`, `IF NOT EXISTS`, `WITHOUT ROWID` | plain `CREATE TABLE` | TEMP, IF NOT EXISTS, WITHOUT ROWID | No corpus evidence |
| Join op | `JOIN`, `INNER JOIN`, `CROSS JOIN`, `LEFT [OUTER] JOIN`, `NATURAL JOIN`, `,` | `JOIN`, `NATURAL JOIN`, `,` | INNER/CROSS/LEFT/OUTER | Only corpus forms kept (13435 uses JOIN and NATURAL JOIN; 15358/9327 use `,`) |
| Compound op | `UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT` | `INTERSECT`, `EXCEPT` | UNION, UNION ALL | Only I/E in corpus (15358, 13871) |
| Select variants | 7 Select-Stmt × 4 Select-Core = 28 combos | 1 canonical with optional clauses | 27 redundant combos | One form admits all corpus shapes via optional non-terminals |
| Column alias | `AS name`, `name` (implicit) | `AS name` | implicit | Corpus uses `AS` |
| Not-null | `NOT NULL`, `NOT NULL DEFAULT x` | `NOT NULL` | DEFAULT | 19646 uses plain form |
| Generated col storage | `STORED`, `VIRTUAL`, (none) | (none) | STORED, VIRTUAL | 19646 and 9327 both use no explicit storage |
| Statements (unused) | `ATTACH`, `DETACH`, `ANALYZE`, `REINDEX`, `VACUUM` | — | All | No CVE evidence |
| Statements (kept) | `CREATE TRIGGER ... INSERT ON T BEGIN ... END` | plain form (INSERT trigger) | `BEFORE`/`AFTER`/`INSTEAD OF`, `FOR EACH ROW`, `WHEN {Expr}` qualifiers | 13434 original PoC uses plain `CREATE TRIGGER c INSERT ON a BEGIN ... END` |
| Column constraints (kept) | `CHECK({Expr})`, `UNIQUE`, `UNIQUE ON CONFLICT REPLACE` | these three | `PRIMARY KEY`, `DEFAULT`, `REFERENCES`, `COLLATE`, `NOT NULL DEFAULT x` | 13434 uses `CHECK` + `UNIQUE ON CONFLICT REPLACE`; 13435 uses `UNIQUE`; 9327 uses `UNIQUE` |
| Hand-coded nesting | `Deep-Nested-Select`, `Long-Join-Chain`, `Recursive-CTE-Heavy`, `Window-Func-Complex` | — | All | Let Nautilus Random Recursive Mutation amplify simple recursive rules instead |
| PRAGMAs | ~40 available | `integrity_check`, `foreign_key_check`, `writable_schema`, `encoding`, `journal_mode`, `schema_version` | Other 34 | CVE-19646 + SQLite PRAGMAs with historical bugs |

**Expected reduction:** 1009 lines → ~350 lines. 159 rules → ~55 rules.

---

## 6. Attack Pattern Catalog (Step 4)

Each CVE becomes one named pattern. Patterns are multi-statement skeletons
that expand to vocabulary from §4. Internal expressions expand to shared
non-terminals from §7.

| Pattern ID | CVE | Structural skeleton (informal) |
|---|---|---|
| `P-INTERSECT-VIEW` | CVE-2020-15358 | `CREATE TABLE T(C); CREATE TABLE U(D); CREATE VIEW V AS SELECT C FROM T ORDER BY C; SELECT * FROM T, U WHERE C = (SELECT lit INTERSECT SELECT D FROM V) AND C = lit` |
| `P-HAVING-WINDOW` | CVE-2020-13871 | `CREATE TABLE T(C); SELECT (SELECT C FROM T GROUP BY C HAVING {Boolean-Expr with Coalesce-Window-Expr}) FROM T EXCEPT SELECT C FROM T ORDER BY C,C,C` |
| `P-JOIN-WINDOW-COALESCE` | CVE-2020-13435 | `CREATE TABLE T(C UNIQUE); SELECT T.C FROM T JOIN T {Alias} ON {Expr} NATURAL JOIN T WHERE T.C IN (({Scalar-Subquery with Coalesce-Window-Expr}))` |
| `P-BOUNDARY-FUNC` | CVE-2020-13434 simplified PoC (generalized) | `SELECT {Builtin-Func}({Boundary-Int}, {Expr})` — generalizes printf/zeroblob/substr/group_concat; SELECT-time boundary-int sink |
| `P-TRIGGER-GROUPCONCAT` | CVE-2020-13434 original PoC | `CREATE TABLE T(C {Type-Name} CHECK({Boolean-Expr-with-printf}) UNIQUE ON CONFLICT REPLACE); CREATE TRIGGER {Name} INSERT ON T BEGIN INSERT INTO T SELECT group_concat(C, {Boundary-Int}) FROM T; END; INSERT INTO T VALUES ({Literal-List}); UPDATE T SET C = {Literal}` — INSERT-time boundary-int sink via trigger+aggregate |
| `P-GENCOL-JOIN-COALESCE` | CVE-2020-9327 | `CREATE TABLE T(C, D AS (D) UNIQUE); CREATE TABLE U(E UNIQUE, F UNIQUE); CREATE VIEW V(G) AS SELECT coalesce(C, D) FROM T WHERE D IN (Str); SELECT * FROM V JOIN U WHERE {Boolean-Expr}` |
| `P-GENCOL-INTEGRITY` | CVE-2019-19646 | `CREATE TABLE T(C, D NOT NULL GENERATED ALWAYS AS (C = 0)); INSERT INTO T(C) VALUES (lit); PRAGMA integrity_check` |
| `P-COMPOUND-MIX` | *derived* | `{DDL-sequence}; SELECT ... {Compound-Op} SELECT ... ORDER BY {Col-List}` — combines INTERSECT and EXCEPT usage from 15358 + 13871 into one template |

**Note on P-COMPOUND-MIX:** This is a *synthesized* pattern, not from a
single CVE. It's included to exercise the compound-operator code region
with the corpus's structural tricks combined. Derived patterns are explicit
and kept rare — the grammar stays evidence-anchored, but this one encodes
the "combination hypothesis" directly.

---

## 7. Shared Non-Terminals (Step 5)

These factor common sub-expressions so splice mutation can recombine them
across patterns. **This is the step that enables "CVE A + CVE B → new
crash."**

| Non-terminal | Expands to | Used by patterns |
|---|---|---|
| `Coalesce-Window-Expr` | `coalesce({Window-Func-Call}, {Agg-Func-Call})` | 13435, 13871, 9327 |
| `Window-Func-Call` | `lead({Expr}) OVER ()`, `lag({Expr}) OVER ({Order-By})`, `COUNT() OVER ({Order-By})` | 13871, 13435 |
| `Agg-Func-Call` | `SUM({Expr})`, `COUNT()`, `AVG({Expr})`, `group_concat({Expr}, {Int-Lit})` | 13434, 13435, 13871 |
| `Scalar-Subquery` | `SELECT {Expr}`, `SELECT {Expr} FROM {Table-Ref}`, `SELECT ({Scalar-Subquery}) FROM {Table-Ref}` | 13435, 15358, 13871 |
| `Join-Chain` | `{Join-Op} {Table-Ref}`, `{Join-Chain} {Join-Op} {Table-Ref}` | 13435, 9327 |
| `GenCol-Def` | `{Col-Name} AS ({Expr})`, `{Col-Name} NOT NULL GENERATED ALWAYS AS ({Expr})`, `{Col-Name} AS ({Expr}) UNIQUE` | 19646, 9327 |
| `View-Def` | `CREATE VIEW {View-Name} AS {Select-Stmt}`, `CREATE VIEW {View-Name}({Col-Name}) AS {Select-Stmt}` | 15358, 9327 |
| `Boolean-Expr` | `{Expr} {Compare-Op} {Expr}`, `{Expr} IN ({Expr-List})`, `{Boolean-Expr} AND {Boolean-Expr}`, `NOT {Boolean-Expr}`, etc. | All |
| `Col-Ref` | `{Col-Name}`, `{Table-Name}.{Col-Name}`, `{Alias}.{Col-Name}` | All |
| `Expr` (core) | `{Literal}`, `{Col-Ref}`, `({Expr})`, `{Expr} {Bin-Op} {Expr}`, `{Scalar-Subquery}`, `{Case-Expr}`, `{Builtin-Func-Call}` | All — **recursive, shallow; depth comes from mutation** |
| `Order-By` | `ORDER BY {Expr}`, `ORDER BY {Expr} , {Expr}`, `ORDER BY {Expr} , {Expr} , {Expr}` | 13871, 15358 |

**Recursion discipline:** only `Expr`, `Scalar-Subquery`, `Join-Chain`, and
`Boolean-Expr` are recursive. All four recurse on themselves directly, no
more than one level deep per rule. Nautilus's Random Recursive Mutation
amplifies these into deep-nested shapes at runtime (per the paper's own
finding: CVE-2018-10191 in PHP was found *only* by Random Recursive
Mutation on shallow recursive rules, never by the grammar itself).

---

## 8. Target-Specific Symbols (Step 6)

Terminals drawn from SQLite documentation for modules with CVE history.
Every symbol traces to either (a) a built-in function/pragma in SQLite
source or (b) a documented extension with historical bug reports.

| Non-terminal | Values | Source |
|---|---|---|
| `Builtin-Func` | `printf`, `format`, `zeroblob`, `hex`, `substr`, `quote`, `typeof`, `likelihood`, `ifnull`, `coalesce`, `iif`, `random`, `randomblob` | `sqlite3_stmt.c` core builtins + CVE corpus |
| `Agg-Func-Name` | `sum`, `count`, `avg`, `group_concat`, `max`, `min`, `total` | Aggregate list + CVE corpus |
| `Window-Func-Name` | `lead`, `lag`, `row_number`, `rank`, `dense_rank`, `first_value`, `last_value`, `nth_value` | SQLite window functions |
| `PRAGMA-Name` | `integrity_check`, `foreign_key_check`, `writable_schema`, `encoding`, `journal_mode`, `schema_version`, `cache_size`, `page_size` | PRAGMAs with documented historical bugs |
| `Module-Name` | `fts5`, `fts4`, `rtree`, `geopoly`, `zipfile` | Virtual-table modules with CVE history (reserved for future `Pattern-Virtual-Table`) |

**Intentionally excluded:** generic string-manipulation functions (`lower`,
`upper`, `trim`, `replace`, `length`) without CVE evidence. Can be added
when corpus expands.

---

## 9. Grammar File Structure

`grammars/sqlite_attack.py` will be organized as:

```
# Header: provenance, date, source commit
# ─────────────────────────────────────────────────

# SECTION 1: START + statement list                 (~15 lines)
# SECTION 2: Vocabulary — literals, identifiers     (~50 lines)
# SECTION 3: Types and collations                   (~15 lines)
# SECTION 4: Canonical SQL forms                    (~60 lines)
#   - Select-Stmt (1 canonical with optionals)
#   - Create-Table (1 canonical)
#   - Insert-Stmt, Update-Stmt, Delete-Stmt
#   - Pragma-Stmt
# SECTION 5: Shared non-terminals                   (~100 lines)
#   - Expr family (recursive base)
#   - Coalesce-Window-Expr, Window-Func-Call
#   - Agg-Func-Call, Scalar-Subquery
#   - Join-Chain, GenCol-Def, View-Def
#   - Boolean-Expr, Col-Ref, Order-By
# SECTION 6: Attack patterns (8 patterns)           (~95 lines)
#   - Pattern-P15358, Pattern-P13871, Pattern-P13435
#   - Pattern-P13434-Boundary-Func (SELECT-time sink)
#   - Pattern-P13434-Trigger-GroupConcat (INSERT-time sink via trigger)
#   - Pattern-P9327, Pattern-P19646
#   - Pattern-Compound-Mix (derived)
# SECTION 7: Target-specific terminals              (~30 lines)
#   - Builtin-Func, Agg-Func-Name, Window-Func-Name
#   - PRAGMA-Name, Module-Name
# ─────────────────────────────────────────────────
# Total: ~460 lines, ~237 rules (amended 2026-04-22 by measurement-and-fidelity spec §3.4 for B2 tight NTs)
```

**Line budget discipline:** if any section exceeds its budget by more than
20%, the plan reviewer should flag it — bloat in the artifact defeats the
purpose.

**No weights in v1:** rules use Nautilus default uniform selection at
first. A separate spec (`2026-04-??-attack-pattern-weights.md`) will
introduce weights once the RL design nails down state/action/reward. This
keeps the grammar spec and the RL spec cleanly separable.

---

## 10. Evaluation Plan

The grammar is an ablation-ready artifact. It is compared against two
existing grammars on identical infrastructure (same harness, same
Nautilus build, same campaign duration per target).

### 10.1 Grammars under test

| Name | File | Role |
|---|---|---|
| `attack` | `sqlite_attack.py` (new) | Shrunk, CVE-distilled |
| `patterns` | `sqlite_patterns.py` | Current — patterns + full EBNF (weighted) |
| `uniform` | `sqlite_patterns_uniform.py` | Flood baseline (uniform weights) |

### 10.2 Targets

All 4 CVE-vulnerable SQLite versions:
- `sqlite-3.30.1` (CVE-2019-19646)
- `sqlite-3.31.1` (CVE-2020-13434, CVE-2020-9327)
- `sqlite-3.32.0` (CVE-2020-13435)
- `sqlite-3.32.2` (CVE-2020-15358, CVE-2020-13871)

### 10.3 Metrics

For each (grammar, target) pair, measure:

1. **Time-to-first-crash (TTFC)** per CVE class (seconds).
2. **Unique crash hashes** over 1-hour pilot, 24-hour full.
3. **Unique CVE classes** hit (did we find all 6?).
4. **Crashes per million executions** (normalizes for exec-rate differences).
5. **Branch coverage** (via `gcov` on harness instrumentation).
6. **Grammar-rule efficiency**: for each grammar-rule, count how often it
   appears in a crash-causing input → ranks rules by bug-finding value.

### 10.4 Pilot (fast signal, 1-hour)

Per grammar × per target × 3 seeds = 36 runs × 1 hour = 36 CPU-hours.
Outputs a pilot table with TTFC, crash count, and CVE classes hit.

### 10.5 Full campaign (24-hour)

Run after pilot passes acceptance:
- Pilot acceptance: `attack` grammar must hit ≥3 of 6 CVE classes in 1
  hour (proves the shrink didn't break anything).
- Full campaign: 12 runs (3 grammars × 4 targets) × 24 hours = 288 CPU-hours.

### 10.6 Acceptance criteria

**Thesis-positive outcome:** `attack` finds CVE classes at higher rate
(per CPU-hour) than `patterns`, and `patterns` beats `uniform`. This
directly supports the "quality > size" thesis claim.

**Thesis-neutral outcome:** `attack` matches `patterns` — still a win
(same results, smaller grammar, auditable provenance).

**Thesis-negative outcome:** `attack` misses CVE classes `patterns` finds
— investigate which vocabulary/canonical-form cut over-shrunk, revise, re-pilot.

---

## 11. Open Questions / Deferrals

- **Weights (Phase 2 RL):** Not in this spec. Grammar ships weight-free;
  RL design spec adds weight annotations.
- **cve2grammar integration:** `sqlite_generated.py` (LLM-rendered from 42
  Manuel Rigger bug reports) is complementary but separate. A later spec
  will reconcile the two — likely by feeding cve2grammar's output through
  the same 6-step procedure as a *grammar-augmentation pipeline*.
- **Cross-DBMS portability:** The 6-step procedure is DBMS-agnostic. A
  follow-up spec may apply it to DuckDB or MySQL as external validity
  evidence for the thesis.
- **Unparsing scripts:** Not needed — no CVE in the 6-corpus requires
  non-CF constructs (matching identifiers, checksums, length-prefixed
  fields). Revisit if corpus expansion introduces one.
- **Blob literals source:** `x'00'`, `x'ff'`, `x'4142'` are boundary
  picks, not corpus-derived. If pilots show FTS5/encoding bugs, expand;
  otherwise leave as documented boundary set.

---

## 12. References

[1] Aschermann et al., "NAUTILUS: Fishing for Deep Bugs with Grammars,"
    NDSS 2019. `docs/NDSS19_Nautilus.pdf`. §VI-B CVE case study,
    §IV-A Random Recursive Mutation, §VIII limitations on important symbols.

[2] SQLite CVE corpus: `docs/cve-list.md` (6 CVEs, 2019–2020).

[3] Current grammars:
    - `grammars/sqlite_patterns.py` (weighted, 1009 lines)
    - `grammars/sqlite_patterns_uniform.py` (uniform baseline, 1002 lines)
    - `grammars/sqlite_generated.py` (cve2grammar-rendered, 328 lines — not self-contained)

[4] Pilot data supporting thesis claim: `docs/crash-report-patterns-pilot.md`
    — 144 crashes / 5 min, 4 CVE classes hit with `sqlite_patterns.py`.

---

**End of design spec. Awaiting user review before implementation plan.**
