# Chapter 3 Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite c3_method.tex to fix 12 verified errors while preserving correct content, all labels, refs, and citations.

**Architecture:** Section-by-section edits to existing LaTeX file, guided by the source-of-truth spec. Each task targets one logical section, applies only the corrections identified in the spec, then verifies compilation. No structural reorganization — only content fixes.

**Tech Stack:** LaTeX, latexmk (compilation), grep (verification against grammar source)

**Spec:** `docs/superpowers/specs/2026-05-17-chapter3-source-of-truth-design.md`
**Target:** `docs/thesis/v2/chapters/c3_method.tex`
**Grammar source:** `grammars/v3.3/sqlite_v3.py`

---

## File Map

| File | Action | What changes |
|------|--------|--------------|
| `docs/thesis/v2/chapters/c3_method.tex` | Modify | All 12 error corrections |
| `grammars/v3.3/sqlite_v3.py` | Read-only | Verify code snippets in listings |

---

### Task 1: Fix Chapter Introduction (lines 1–6)

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex:1-6`

**What to fix:** Remove version evolution narrative ("v3.0 through v3.3, growing from 449 to 520 production rules"). Replace with single version statement.

- [ ] **Step 1: Read current intro paragraph (line 5)**

Current text (line 5):
```
Section~\ref{sec:grammar-design} presents the grammar design methodology, which constitutes the core contribution of this work. The grammar was iteratively refined across four versions (v3.0 through v3.3, growing from 449 to 520 production rules), guided by root-cause analysis of known CVEs and experimental feedback from fuzzing campaigns.
```

- [ ] **Step 2: Replace with corrected version**

New text:
```latex
Section~\ref{sec:grammar-design} presents the grammar design methodology, which constitutes the core contribution of this work. The grammar contains 514 production rules organized into a two-layer architecture, designed through root-cause analysis of known CVEs and guided by experimental feedback from fuzzing campaigns.
```

- [ ] **Step 3: Verify no broken refs**

Run: `grep -n "\\\\ref{" docs/thesis/v2/chapters/c3_method.tex | head -5`
Expected: All refs still intact (sec:overview, sec:grammar-design)

- [ ] **Step 4: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "fix(thesis): correct grammar rule count in c3 intro (449-520 → 514)"
```

---

### Task 2: Fix Grammar Engine paragraph (line 22)

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex:22`

**What to fix:** Remove "loaded dice algorithm" reference. Replace with accurate description of weighted random selection.

- [ ] **Step 1: Identify the error string**

Current (line 22):
```
Rules can carry numeric weights that bias the sampling distribution via the loaded dice algorithm~\citep{loadeddice}, allowing the grammar designer to make certain SQL constructs more likely to appear than others.
```

- [ ] **Step 2: Replace with corrected version**

New text:
```latex
Rules can carry numeric weights that bias the sampling distribution: at each expansion step, the engine selects among applicable rules with probability proportional to their weights, allowing the grammar designer to make certain SQL constructs more likely to appear than others.
```

Note: Remove `\citep{loadeddice}` — the loaded_dice crate is used only for recursion depth bias (a separate internal mechanism), not for rule selection. If the citation must stay for the bibliography, move it to a footnote explaining the recursion depth mechanism, or remove entirely.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "fix(thesis): correct weighted sampling description (not loaded_dice algorithm)"
```

---

### Task 3: Fix Generation and Mutation paragraph (lines 25–26)

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex:25-26`

**What to fix:** Current text says "replacing a subtree, expanding or collapsing recursive productions, or splicing subtrees between two trees" — lists only 3 of 5 operators. Rewrite to accurately describe all 5.

- [ ] **Step 1: Identify current text**

Current (line 25):
```
...applies a structural mutation --- replacing a subtree, expanding or collapsing recursive productions, or splicing subtrees between two trees.
```

- [ ] **Step 2: Replace with corrected version listing all 5 operators**

New text:
```latex
...applies one of five structural mutations: deterministic rule substitution (trying every alternative production at a given node), random subtree regeneration (replacing a subtree with a fresh derivation from the grammar), random recursion expansion or collapse (adjusting recursive depth), splice mutation (replacing a subtree with a compatible fragment from the chunk store), or bulk random havoc (applying 100 random subtree replacements in succession).
```

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "fix(thesis): list all 5 mutation operators correctly in c3"
```

---

### Task 4: Fix figure caption (line 17)

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex:17`

**What to fix:** Caption says "four mutation operators" → change to "five mutation operators"

- [ ] **Step 1: Find and replace in caption**

Current fragment:
```
the mutation engine applies four mutation operators
```

Replace with:
```
the mutation engine applies five mutation operators
```

- [ ] **Step 2: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "fix(thesis): correct mutation operator count in fig caption (4 → 5)"
```

---

### Task 5: Fix Grammar Design section header stats (around line 105)

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex:105`

**What to fix:** "520 production rules" → 514. "approximately 350 in Layer~1 and 170 in Layer~2" → "over 460 in Layer~1 and approximately 50 in Layer~2"

- [ ] **Step 1: Find the error text**

Current (line 105):
```
In its final form (v3.3), the grammar contains 520 production rules: approximately 350 in Layer~1 (SQL atoms) and 170 in Layer~2 (composed shapes across the four pattern categories).
```

- [ ] **Step 2: Replace with corrected version**

New text:
```latex
In its final form, the grammar contains 514 production rules: over 460 in Layer~1 (SQL atoms) and approximately 50 in Layer~2 (composed vulnerability-targeting shapes across the four pattern categories).
```

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "fix(thesis): correct rule counts (520→514, fix Layer 1/2 split)"
```

---

### Task 6: Fix Stress-Query descriptions (Q4, Q7, Q8) — lines 171–199

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex:171-199`

**What to fix:** Three wrong Q descriptions and the accompanying rationale paragraph.

- [ ] **Step 1: Fix the Q listing paragraph (line 172)**

Current:
```
...correlated subqueries (Q4), compound queries with INTERSECT/EXCEPT (Q5), self-JOINs (Q6), window functions with OVER clauses (Q7), and aggregate queries with GROUP BY and HAVING (Q8).
```

Replace with:
```latex
...recursive CTEs (Q4), compound queries with INTERSECT/EXCEPT (Q5), self-JOINs (Q6), nested subquery chains (Q7), and EXPLAIN QUERY PLAN analysis (Q8).
```

- [ ] **Step 2: Fix the Listing code block (lst:stress-query)**

Current listing shows Q2, Q3, Q5, Q6. Update comment labels if any refer to "correlated subquery" or "window function". If the listing only shows representative alternatives (Q2, Q3, Q5, Q6), the listing itself may be correct — just fix the surrounding text.

Verify: The listing at lines 176-199 shows Q2, Q3, Q5, Q6 — these are all correct. No code change needed in the listing itself.

- [ ] **Step 3: Fix the rationale paragraph (around line 174)**

Current text mentions "NATURAL JOIN (Q3) is particularly effective..." (correct) but then may reference window functions or correlated subqueries. Find and fix any rationale that references the wrong Q4/Q7/Q8 patterns.

Update rationale to explain:
- Q4 (Recursive CTE): exercises the CTE resolution engine, which handles recursive query expansion with termination detection
- Q7 (Nested subquery chain): forces the query planner to handle derived tables and subquery flattening decisions
- Q8 (EXPLAIN QUERY PLAN): exercises the query plan explainer, which traverses the full AST and can trigger bugs in plan serialization

- [ ] **Step 4: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "fix(thesis): correct Q4/Q7/Q8 Stress-Query descriptions to match code"
```

---

### Task 7: Fix Validation-Op descriptions (line 226)

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex:226`

**What to fix:** Thesis says "integrity_check, foreign_key_check, quick_check, and REINDEX" → actual: "integrity_check, quick_check, ANALYZE, and EXPLAIN QUERY PLAN"

- [ ] **Step 1: Find the error text**

Current (line 226):
```
...generates PRAGMA statements and internal consistency checks that exercise SQLite's schema validation and integrity verification subsystems: \texttt{integrity\_check}, \texttt{foreign\_key\_check}, \texttt{quick\_check}, and \texttt{REINDEX}.
```

- [ ] **Step 2: Replace with corrected version**

New text:
```latex
...generates PRAGMA statements and internal consistency checks that exercise SQLite's schema validation and integrity verification subsystems: \texttt{integrity\_check}, \texttt{quick\_check}, \texttt{ANALYZE}, and \texttt{EXPLAIN QUERY PLAN}.
```

- [ ] **Step 3: Update the rationale paragraph**

Current rationale mentions "integrity checker walks every page" and "REINDEX" — replace REINDEX references with explanation of ANALYZE (updates statistics tables, traverses index metadata) and EXPLAIN QUERY PLAN (traverses AST for plan rendering).

- [ ] **Step 4: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "fix(thesis): correct Validation-Op alternatives (ANALYZE, EXPLAIN QUERY PLAN)"
```

---

### Task 8: Expand Boundary-Func-Call (lines 206–223)

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex:206-223`

**What to fix:** Thesis shows only 3 alternatives in listing. Code has 7. Expand listing and update text.

- [ ] **Step 1: Update the listing (lst:boundary-func)**

Replace current 3-alternative listing with all 7:

```latex
\begin{lstlisting}[language=Python, caption={Boundary-Func-Call alternatives targeting integer overflow and buffer boundary conditions.}, label=lst:boundary-func, basicstyle=\ttfamily\small, numbers=left]
ctx.rule("Boundary-Func-Call",
    "printf({Format-Spec}, {Boundary-Int}, {Boundary-Float})",
    weight=3.0)
ctx.rule("Boundary-Func-Call",
    "printf({Format-Spec}, {Boundary-Int})", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "printf({Printf-Fmt-Spec}, {Boundary-Int}, {Str-Literal})",
    weight=1.5)
ctx.rule("Boundary-Func-Call",
    "substr({Str-Literal}, {Boundary-Int})", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "substr({Str-Literal}, {Boundary-Int}, {Boundary-Int})",
    weight=1.5)
ctx.rule("Boundary-Func-Call",
    "hex(zeroblob({Boundary-Int}))", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "round({Boundary-Float}, {Boundary-Int})", weight=1.5)
\end{lstlisting}
```

- [ ] **Step 2: Update surrounding text**

Current text mentions "printf alternative pairs format specifiers..." — update to reflect all 7 alternatives covering three function families:
- `printf` variants (3 alternatives): target integer overflow in formatting
- `substr` variants (2 alternatives): exercise heap buffer boundary operations
- `hex(zeroblob(N))`: stresses memory allocation limits
- `round`: exercises float-to-int conversion edge cases

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "fix(thesis): expand Boundary-Func-Call to show all 7 alternatives"
```

---

### Task 9: Fix Two-Layer Architecture section (Section 3.2.1, around line 116)

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex:116`

**What to fix:** Update Layer 2 shape counts to include correct Boundary-Func-Call count (7 not implied 3). Verify figure caption about "required" vs "optional" shapes is accurate.

- [ ] **Step 1: Find Layer 2 description**

Current (line 116):
```
The \texttt{Boundary-Func-Call} non-terminal provides function calls with boundary values targeting integer overflow and buffer overread conditions.
```

- [ ] **Step 2: Update to reflect 7 alternatives**

New text:
```latex
The \texttt{Boundary-Func-Call} non-terminal provides seven function call alternatives with boundary values targeting integer overflow, buffer boundary, and numeric conversion edge cases.
```

- [ ] **Step 3: Verify figure caption (fig:two-layer) accuracy**

Check if figure caption mentions "required" and "optional" shapes. The Sql-Stmt dispatch rules show:
- Schema-Setup appears in 3/4 alternatives (dominant)
- Stress-Query appears in 2/4 alternatives
- Validation-Op appears in 1/4 alternatives
- Boundary-Func-Call appears in 1/4 alternatives

If caption says "required" for Schema-Setup and Stress-Query, and "optional" for Validation-Op and Boundary-Func-Call — this is approximately correct but imprecise. Leave as-is unless explicitly wrong.

- [ ] **Step 4: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "fix(thesis): update Boundary-Func-Call count in two-layer section"
```

---

### Task 10: Compilation verification

**Files:**
- Read: `docs/thesis/v2/thesis.tex` (main file)

- [ ] **Step 1: Compile the thesis**

Run:
```bash
cd docs/thesis/v2 && latexmk -pdf -interaction=nonstopmode thesis.tex 2>&1 | grep -E "Error|Warning|Undefined" | head -20
```

Expected: No new errors. Possible existing warnings about missing citations (acceptable).

- [ ] **Step 2: Check for broken cross-references**

Run:
```bash
grep -n "\\\\ref{" docs/thesis/v2/chapters/c3_method.tex | while read line; do echo "$line"; done
```

Verify all `\ref{}` targets still exist as `\label{}` in the document.

- [ ] **Step 3: Check for orphaned citations**

Run:
```bash
grep -oP '\\\\citep?\{[^}]+\}' docs/thesis/v2/chapters/c3_method.tex | sort -u
```

Verify `\citep{loadeddice}` is either removed or repositioned appropriately.

- [ ] **Step 4: Final commit if compilation clean**

```bash
git add docs/thesis/v2/
git commit -m "chore(thesis): verify c3 compiles cleanly after corrections"
```

---

### Task 11: Quality review with /proofread

- [ ] **Step 1: Run /proofread on the updated c3**

Invoke: `/proofread docs/thesis/v2/chapters/c3_method.tex`

Focus areas:
- Logic flow after Q4/Q7/Q8 corrections (do the rationale paragraphs still make sense?)
- Consistency between mutation operator count in all mentions
- No remaining references to "loaded dice" or wrong rule counts

- [ ] **Step 2: Fix any issues found**

Apply fixes, compile, commit.

---

### Task 12: Stress-test with /devils-advocate

- [ ] **Step 1: Run /devils-advocate on c3**

Invoke: `/devils-advocate docs/thesis/v2/chapters/c3_method.tex`

Challenge:
- "Does the claim about 5 mutation operators match what a reader would understand from the architecture figure?"
- "Is the weighted sampling description technically precise without naming an algorithm?"
- "Do the Q4 (Recursive CTE) and Q7 (nested subquery) rationale paragraphs accurately explain WHY these patterns stress the query planner?"

- [ ] **Step 2: Fix any issues found**

Apply fixes, compile, commit.

---

## Execution Notes

- **DO NOT touch** the state machine paragraph (Init→Det→Random in Coverage Feedback section) until separate verification is done
- **Preserve** all `\label{}`, `\ref{}`, `\cite{}` commands unless explicitly removing a wrong citation
- **Keep** existing good content — only fix what the spec identifies
- Tasks 1-9 are independent edits (can be done in any order)
- Tasks 10-12 must come after all edits are complete
