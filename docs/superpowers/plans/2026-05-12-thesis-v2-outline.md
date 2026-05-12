# Thesis v2 Outline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite thesis v2 chapters to match the approved outline design — Ch3 as pure proposed method (grammar only), related work in Ch2.4, clean Ch4, all figures.

**Architecture:** Chapter-by-chapter rewrite following approved spec. Ch3 is gutted of implementation sections (harness, oracle, triage) and rebuilt around grammar cross-pollination narrative. Ch2 gains related work section and 2 figures. Ch4 and Conclusion rewritten for consistency. Each task = one section or figure, built on PDF after every .tex change.

**Tech Stack:** LaTeX (pdflatex + bibtex), TikZ for figures, `docs/thesis/v2/` directory

**Build command:** `cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/docs/thesis/v2 && pdflatex -interaction=nonstopmode thesis.tex && bibtex thesis && pdflatex -interaction=nonstopmode thesis.tex && pdflatex -interaction=nonstopmode thesis.tex && pdflatex -interaction=nonstopmode thesis.tex`

**Key files:**
- `docs/thesis/v2/chapters/c2_background.tex` (66 lines, add 2.4 + figures)
- `docs/thesis/v2/chapters/c3_method.tex` (454 lines, gut sections 3.4-3.7, rewrite 3.2)
- `docs/thesis/v2/chapters/c4_experiments.tex` (264 lines, rewrite for consistency)
- `docs/thesis/v2/chapters/conclusion.tex` (14 lines, rewrite)
- `docs/thesis/v2/references.bib` (23 entries, add missing refs)

**Spec:** `docs/superpowers/specs/2026-05-12-thesis-v2-outline-design.md`

---

### Task 1: Gut Ch3 — Remove implementation sections

Remove Harness Construction (3.5), Oracle Classification (3.6), and Triage Pipeline (3.7) from c3_method.tex. These are implementation artifacts, not proposed method. Keep only: 3.1 System Overview (done), Structural Primitives Philosophy, Layer Decomposition, Grammar Evolution.

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex:310-475` (delete sections 3.5-3.7)

- [ ] **Step 1: Delete Harness Construction, Oracle Classification, and Triage Pipeline sections**

Delete lines 310-475 of c3_method.tex — everything from `\section{Harness Construction}` through the end of `\subsection{Crash Minimization}`. This removes:
- Section: Harness Construction (AFL Fork Server Protocol, Compilation, Three Harness Types)
- Section: Oracle Classification (oracle table)
- Section: Triage Pipeline (Stack-Hash Dedup, CVE Signature Matching, Fidelity Scoring, Crash Minimization)

The `sec:crash-pipeline` label referenced by the chapter intro must be redirected. Update chapter intro paragraph to remove reference to crash pipeline section.

- [ ] **Step 2: Update chapter intro paragraph**

Current chapter intro (line 6) references 3 sections: overview, grammar design, crash pipeline. Update to reference only 3 sections matching new structure: overview, grammar design, grammar evolution.

Replace:
```latex
Section~\ref{sec:overview} provides a high-level overview of the system and its components. Section~\ref{sec:grammar-design} presents the grammar design methodology, which constitutes the core contribution of this work. Section~\ref{sec:crash-pipeline} covers the crash analysis pipeline.
```

With:
```latex
Section~\ref{sec:overview} provides a high-level overview of the system and its components. Section~\ref{sec:grammar-design} presents the grammar design methodology, which constitutes the core contribution of this work. Section~\ref{sec:grammar-evolution} describes the evidence-driven grammar evolution process.
```

- [ ] **Step 3: Build PDF and verify**

Run build command. Verify:
- No undefined references (sec:grammar-evolution label already exists at line 241)
- No orphaned labels
- Chapter 3 now has: 3.1 Overview, 3.2 Primitives, 3.3 Layer Decomposition, 3.4 Grammar Evolution
- Page count decreased (implementation sections removed)

- [ ] **Step 4: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "docs(thesis-v2): remove implementation sections from Chapter 3

Drop Harness Construction, Oracle Classification, and Triage Pipeline.
Chapter 3 now contains only proposed method: system overview,
grammar design, and grammar evolution per UET template requirements."
```

---

### Task 2: Restructure Ch3 — Merge into 3 clean sections

Current Ch3 has 4 sections after gutting: Overview, Primitives Philosophy, Layer Decomposition, Grammar Evolution. Spec says 3 sections: 3.1 Overview, 3.2 Grammar Design (merge primitives + layers + add cross-pollination), 3.3 Grammar Evolution. Merge sections 3.2 and 3.3 into a single 3.2 Grammar Design section.

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex`

- [ ] **Step 1: Convert "Structural Primitives Philosophy" from section to subsection**

Change `\section{Structural Primitives Philosophy}` to `\section{Grammar Design}` with label `sec:grammar-design`. Make the primitives content the opening of this section (no subsection header for it — it flows as the section introduction).

- [ ] **Step 2: Convert "Layer Decomposition" from section to subsection**

Change `\section{Layer Decomposition}` to `\subsection{Two-Layer Architecture}`. It now lives under 3.2 Grammar Design.

- [ ] **Step 3: Convert "Grammar Evolution" from section to section 3.3**

Keep `\section{Grammar Evolution}` as-is — it becomes section 3.3. Update label to `sec:grammar-evolution` (already exists).

- [ ] **Step 4: Verify section numbering**

After changes, Ch3 structure should be:
```
3.1 System Overview (sec:overview)
3.2 Grammar Design (sec:grammar-design)
    3.2.1 Two-Layer Architecture
    3.2.2 ... (code listings subsections if any)
3.3 Grammar Evolution (sec:grammar-evolution)
    3.3.1 v3.0: Initial Design
    3.3.2 v3.0 to v3.1: Weight Rebalancing
    ...
```

- [ ] **Step 5: Build PDF and verify**

Run build command. Check TOC has 3 sections in Chapter 3. No undefined references.

- [ ] **Step 6: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "docs(thesis-v2): restructure Chapter 3 into 3 sections

3.1 System Overview, 3.2 Grammar Design (merged primitives + layers),
3.3 Grammar Evolution. Matches approved outline."
```

---

### Task 3: Write Section 3.2 — Cross-Pollination narrative

The core contribution section. Add cross-pollination subsection and CVE reachability analysis to section 3.2 Grammar Design. This is new content that doesn't exist yet.

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex` (add after primitives philosophy, before two-layer architecture)

- [ ] **Step 1: Write cross-pollination subsection**

Add `\subsection{Cross-Pollination of Structural Patterns}` after the three constraints paragraph and before two-layer architecture. Content (~1.5 pages):

1. Grammar contains patterns extracted from CVE root-cause analysis, but patterns are NOT labeled per CVE
2. Schema-Setup has generated columns (needed for CVE-2020-9327 AND CVE-2019-19646, but also general)
3. Stress-Query has NATURAL JOIN (needed for CVE-2020-13435, but general query planner exercise)
4. Boundary-Func-Call has printf+boundary (needed for CVE-2020-13434, but tests other functions too)
5. Power: fuzzer freely combines across Layer 2 shapes → discovers unplanned compositions
6. Example walkthrough: Schema-Setup(generated cols) + Stress-Query(NATURAL JOIN) + Boundary-Func-Call(printf)
7. Conclusion: any CVE rediscovery = genuine compositional achievement

Write as flowing prose, no bullet points (template requirement).

- [ ] **Step 2: Write CVE reachability analysis subsection**

Add `\subsection{CVE Reachability Analysis}` after code listings, before pros/cons. Content (~0.5 page):

Reference the CVE reachability matrix figure (Fig 3.3, to be created in Task 7). Explain: rows = structural patterns, columns = 6 CVEs, cells = checkmark. Each CVE needs 2-5 patterns. Patterns are shared across CVEs — visual proof of cross-pollination.

Move `tab:cve-signatures` table from old triage section here (it was deleted in Task 1, so recreate it in this location).

- [ ] **Step 3: Write pros/cons analysis subsection**

Add `\subsection{Analysis}` at end of 3.2. Content (~0.5 page):

Pros:
- Genuine discovery — no hardcoded PoCs
- Cross-pollination — patterns serve multiple CVEs simultaneously
- Composable — new non-terminals extend reach without modifying existing rules
- Grammar-version-independent — same methodology works across Nautilus versions

Cons:
- Manual domain expertise required for grammar design
- Weight sensitivity — wrong weights cause region saturation (FTS problem in v3.0)
- Reachability ceiling — can only find bugs whose structural prerequisites exist as non-terminals

Write as flowing prose with analysis, not a list.

- [ ] **Step 4: Build PDF and verify**

Run build command. Verify new subsections appear in TOC under 3.2. Check page count ~6 pages for 3.2.

- [ ] **Step 5: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "docs(thesis-v2): write cross-pollination, reachability, and analysis for Section 3.2

Core contribution narrative: grammar encodes CVE patterns without labeling,
enabling genuine compositional discovery through cross-pollination."
```

---

### Task 4: Add missing bib entries for Related Work

Ch2.4 will reference CSmith, LangFuzz, IFuzzer, Skyfire, NoREC, TLP. Need bib entries before writing the section.

**Files:**
- Modify: `docs/thesis/v2/references.bib`

- [ ] **Step 1: Add bib entries**

Add entries for: CSmith, LangFuzz, IFuzzer, Skyfire, NoREC, TLP, BuzzFuzz. Use proper citation format matching existing entries (inproceedings style).

Key references:
- CSmith: Yang et al., "Finding and understanding bugs in C compilers", PLDI 2011
- LangFuzz: Holler et al., "Fuzzing with code fragments", USENIX Security 2012
- Skyfire: Wang et al., "Skyfire: Data-driven seed generation for fuzzing", S&P 2017
- NoREC: Rigger & Su, "Detecting optimization bugs in database engines via non-optimizing reference engine construction", ESEC/FSE 2020
- TLP: Rigger & Su, "Testing database engines via pivoted query synthesis", OSDI 2020

- [ ] **Step 2: Build PDF to verify bib compiles**

Run build command. No bibtex errors.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/references.bib
git commit -m "docs(thesis-v2): add bib entries for related work section

CSmith, LangFuzz, Skyfire, NoREC, TLP and supporting references."
```

---

### Task 5: Write Section 2.4 — Related Work

New section at end of Chapter 2. Position our work against existing tools.

**Files:**
- Modify: `docs/thesis/v2/chapters/c2_background.tex` (append after line 66)

- [ ] **Step 1: Write Related Work section**

Add `\section{Related Work}` with label `sec:bg-related` after the Fuzzing section. Content (~2 pages):

Structure as flowing prose (no bullet points per template), organized by approach:

**Mutation-based fuzzers** (~0.5 page): AFL as the dominant paradigm. Strengths: fast, general-purpose, effective on binary formats. Weakness: byte-level mutations produce parser-rejected inputs on structured targets like SQL. Cite AFL.

**Grammar-based fuzzers** (~0.5 page): CSmith (C programs, no feedback, no corpus — pure generation), LangFuzz (JavaScript, corpus-dependent, grammar fragments), Skyfire (learns probabilistic grammar from corpus, seed generation only). Nautilus as the first to combine grammar + coverage feedback. Cite each.

**DBMS-specific testing** (~0.5 page): SQLsmith (random SQL against existing DB, no coverage feedback, no grammar weights), Squirrel (IR-based mutation with semantic awareness, requires custom IR). Differential testing: NoREC, TLP — different goal (correctness bugs, not crashes). Cite each.

**Positioning paragraph** (~0.5 page): DBMS-Nautilus combines Nautilus's grammar+feedback architecture with a domain-specific SQL grammar engineered for vulnerability-triggering patterns. Unlike SQLsmith, it starts from an empty database. Unlike Squirrel, it uses a standard CFG rather than a custom intermediate representation. Unlike Nautilus, it uses weighted sampling biased toward vulnerability-relevant constructs. The key differentiator is cross-pollination of structural patterns.

- [ ] **Step 2: Add comparison table**

Add Table (comparison matrix) at end of section. Columns: Tool, Grammar, Feedback, Corpus-free, Domain-specific, Weighted. Rows: AFL, CSmith, SQLsmith, Squirrel, Nautilus, DBMS-Nautilus.

- [ ] **Step 3: Build PDF and verify**

Run build command. Verify 2.4 appears in TOC. All citations resolve. Table renders correctly.

- [ ] **Step 4: Commit**

```bash
git add docs/thesis/v2/chapters/c2_background.tex
git commit -m "docs(thesis-v2): add Section 2.4 Related Work

Position DBMS-Nautilus against AFL, CSmith, SQLsmith, Squirrel,
Nautilus, NoREC, TLP with comparison table."
```

---

### Task 6: Create Fig 2.1 — SQL Derivation Tree

TikZ derivation tree showing SQL generation from grammar rules, similar to Nautilus Example II.1 but with SQL non-terminals.

**Files:**
- Modify: `docs/thesis/v2/chapters/c2_background.tex` (insert in section 2.2 after derivation explanation)

- [ ] **Step 1: Design and insert TikZ derivation tree**

Insert after the derivation example paragraph (after the `\begin{center}...\end{center}` block showing the derivation steps). Show the tree for:

```
Sql-Stmt → Stmt ";" Stmt
         → SELECT Func(Expr) FROM Table ";" ...
         → SELECT printf(c1) FROM t1 ";" ...
```

Use TikZ `forest` or manual tree with nodes. Non-terminal nodes in boxes, terminal nodes as leaf text.

- [ ] **Step 2: Build PDF and verify figure renders**

Run build command. Figure appears in correct location with caption and label.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c2_background.tex
git commit -m "docs(thesis-v2): add SQL derivation tree figure to Section 2.2"
```

---

### Task 7: Create Fig 3.2 — Two-Layer Grammar Architecture

TikZ diagram showing Layer 1 (SQL atoms) feeding into Layer 2 (composed shapes) composing into Sql-Stmt.

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex` (insert in two-layer architecture subsection)

- [ ] **Step 1: Design and insert TikZ layer diagram**

Show two horizontal bands:
- Layer 1 (bottom): boxes for Expr, Table-Name, Col-Def, Func-Call, Join-Clause, Window-Func, etc.
- Layer 2 (top): boxes for Schema-Setup, Stress-Query, Validation-Op, Boundary-Func-Call
- Top: Sql-Stmt node connecting to Layer 2
- Arrows from Layer 1 boxes up to Layer 2 boxes showing composition

Color-code: Layer 1 = blue tint, Layer 2 = green tint, Sql-Stmt = orange.

- [ ] **Step 2: Build PDF and verify**

Run build command. Figure renders correctly in 3.2.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "docs(thesis-v2): add two-layer grammar architecture diagram to Section 3.2"
```

---

### Task 8: Create Fig 3.3 — CVE Reachability Matrix

TikZ heatmap/grid showing structural patterns × CVEs with checkmarks.

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex` (insert in CVE reachability analysis subsection)

- [ ] **Step 1: Design and insert CVE reachability matrix figure**

This can be a table-figure or TikZ grid. Rows = structural patterns: Generated Columns, NATURAL JOIN, Window Functions, printf + Boundary Int, Compound Queries (INTERSECT/EXCEPT), coalesce(), CREATE VIEW, PRAGMA integrity_check. Columns = 6 CVEs. Cells = filled circle or checkmark if pattern required.

Key visual: show that patterns are shared across CVEs (cross-pollination visible). For example, "Generated Columns" row has checkmarks for both CVE-2020-9327 and CVE-2019-19646.

- [ ] **Step 2: Build PDF and verify**

Run build command. Figure renders in correct location.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "docs(thesis-v2): add CVE reachability matrix figure to Section 3.2"
```

---

### Task 9: Create Fig 3.4 — Grammar Evolution Visualization

TikZ timeline or chart showing grammar versions, rule counts, and key changes.

**Files:**
- Modify: `docs/thesis/v2/chapters/c3_method.tex` (insert in section 3.3)

- [ ] **Step 1: Design and insert grammar evolution figure**

Timeline style: horizontal axis = versions (v3.0, v3.1, v3.2, v3.3). For each:
- Rule count (449, 449, 475, 520)
- Key change label
- CVE reachability fraction (2/6, 2/6, 6/6, 6/6)

Alternative: stacked bar chart showing rule count breakdown by category.

- [ ] **Step 2: Build PDF and verify**

Run build command. Figure renders in 3.3.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c3_method.tex
git commit -m "docs(thesis-v2): add grammar evolution visualization to Section 3.3"
```

---

### Task 10: Create Fig 2.2 — Fuzzing Taxonomy

TikZ diagram classifying fuzzers along two axes.

**Files:**
- Modify: `docs/thesis/v2/chapters/c2_background.tex` (insert in section 2.3)

- [ ] **Step 1: Design and insert fuzzing taxonomy diagram**

2D grid or tree. Axes:
- Horizontal: Generation method (mutation-based, generation-based)
- Vertical: Analysis depth (black-box, grey-box, white-box)

Place known tools: AFL (mutation + greybox), CSmith (generation + blackbox), Nautilus (generation + greybox), DBMS-Nautilus (generation + greybox, highlighted). Symbolic execution tools in white-box row.

- [ ] **Step 2: Build PDF and verify**

Run build command. Figure renders in 2.3 with proper caption.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/c2_background.tex
git commit -m "docs(thesis-v2): add fuzzing taxonomy diagram to Section 2.3"
```

---

### Task 11: Rewrite Chapter 4 — Experiments

Current Ch4 (264 lines) has good content but needs restructuring: remove Coverage Analysis section (not in spec), remove references to Ch3 crash pipeline, ensure triage is described inline in methodology.

**Files:**
- Modify: `docs/thesis/v2/chapters/c4_experiments.tex`

- [ ] **Step 1: Update chapter intro**

Remove reference to `sec:coverage` (Coverage Analysis section being removed). Update to reference only: setup, RQ1, RQ2, threats.

- [ ] **Step 2: Update Section 4.1 — Experimental Setup**

Add brief inline description of harness and oracle (moved from Ch3):
- "SQLite compiled with ASan+UBSan. Crashes classified by exit code: ASan (exit 223), UBSan (exit 1), debug assertions (SIGTRAP)."
- "Crashes deduplicated by top-5 stack frame hash, matched against structural CVE signatures."

Remove reference to "Chapter~\ref{chap:method}" for triage pipeline (no longer there). Describe inline instead.

- [ ] **Step 3: Remove Section "Coverage Analysis"**

Delete the entire Coverage Analysis section (sec:coverage, lines ~208-235). This data can be mentioned briefly in RQ1/RQ2 discussion if relevant, but doesn't need a standalone section per the spec's 2-RQ design.

- [ ] **Step 4: Review RQ1 and RQ2 sections**

Check for references to deleted Ch3 sections (sec:crash-pipeline, sec:triage-cve, etc.). Replace with inline explanations where needed. Ensure `tab:cve-signatures` reference either points to the new location in Ch3.2 or the table is included locally.

- [ ] **Step 5: Build PDF and verify**

Run build command. No undefined references. Ch4 has: 4.1 Setup, 4.2 RQ1, 4.3 RQ2, 4.4 Threats.

- [ ] **Step 6: Commit**

```bash
git add docs/thesis/v2/chapters/c4_experiments.tex
git commit -m "docs(thesis-v2): restructure Chapter 4 — remove coverage section, inline triage

Ch4 now has: Setup, RQ1, RQ2, Threats. Harness/oracle described
inline in setup. Coverage data folded into RQ analysis."
```

---

### Task 12: Rewrite Conclusion

Current conclusion (14 lines) is well-written but references triage pipeline and coverage analysis. Update for consistency with new structure.

**Files:**
- Modify: `docs/thesis/v2/chapters/conclusion.tex`

- [ ] **Step 1: Rewrite conclusion**

Keep same structure but:
- Remove references to triage pipeline as a system component
- Focus on grammar methodology as central contribution
- Highlight cross-pollination as key finding
- Keep: 3/6 CVEs rediscovered, 7 new bug classes, 89 unique crashes
- Keep: limitations and future work paragraphs (update to match spec)
- Ensure ~1 page length

- [ ] **Step 2: Build PDF and verify**

Run build command. Conclusion renders clean. No undefined references.

- [ ] **Step 3: Commit**

```bash
git add docs/thesis/v2/chapters/conclusion.tex
git commit -m "docs(thesis-v2): rewrite Conclusion for consistency with new structure"
```

---

### Task 13: Create experiment figures (Ch4)

Add Fig 4.1 (CVE rediscovery) and Fig 4.2 (bug class distribution) to Chapter 4.

**Files:**
- Modify: `docs/thesis/v2/chapters/c4_experiments.tex`

- [ ] **Step 1: Create CVE rediscovery results figure**

Insert in RQ1 Results subsection. TikZ bar chart or enhanced table-figure showing: 6 CVEs on x-axis, found/not-found as colored bars, with version annotations. Alternative: use existing `tab:cve-rediscovery` and add a visual figure version alongside it.

- [ ] **Step 2: Create bug class distribution figure**

Insert in RQ2 Results subsection. TikZ bar chart: 10 bug classes on x-axis, unique hash count on y-axis, colored by severity (HIGH/MEDIUM/LOW). Reference existing `tab:all-bugs` data.

- [ ] **Step 3: Build PDF and verify**

Run build command. Both figures render in correct locations with captions.

- [ ] **Step 4: Commit**

```bash
git add docs/thesis/v2/chapters/c4_experiments.tex
git commit -m "docs(thesis-v2): add CVE rediscovery and bug class distribution figures to Chapter 4"
```

---

### Task 14: Final consistency check

Verify entire thesis compiles clean, all references resolve, TOC correct, page count in range.

**Files:**
- All thesis .tex files (read-only verification)

- [ ] **Step 1: Full 5-pass build**

Run full build command. Check:
- 0 undefined references
- 0 multiply-defined labels
- All figures numbered correctly
- All tables numbered correctly
- TOC matches expected structure

- [ ] **Step 2: Verify page count**

Target: 40-50 pages. If under 40, note which sections can be expanded. If over 50, note what to trim.

- [ ] **Step 3: Verify chapter structure in TOC**

Expected:
```
Chapter 1: Introduction
Chapter 2: Background
  2.1 DBMS
  2.2 Context-Free Grammars
  2.3 Fuzzing
  2.4 Related Work
Chapter 3: Proposed Method
  3.1 System Overview
  3.2 Grammar Design
    3.2.1 Cross-Pollination...
    3.2.2 Two-Layer Architecture
    3.2.3 CVE Reachability...
    3.2.4 Analysis
  3.3 Grammar Evolution
    3.3.1 v3.0...
    3.3.2 v3.0 to v3.1...
    3.3.3 v3.1 to v3.2...
    3.3.4 v3.2 to v3.3...
    3.3.5 Key Insight...
Chapter 4: Experiments and Evaluation
  4.1 Experimental Setup
  4.2 RQ1: CVE Rediscovery
  4.3 RQ2: New Bug Discovery
  4.4 Threats to Validity
Conclusion
References
```

- [ ] **Step 4: Cross-reference check**

Grep for all `\ref{` and verify each target label exists. Grep for all `\cite{` and verify each bib key exists.

- [ ] **Step 5: Commit final state**

```bash
git add docs/thesis/v2/
git commit -m "docs(thesis-v2): final consistency check — all refs resolved, structure verified"
```

---

## Execution Order

Tasks must be executed in this order due to dependencies:

1. **Task 1** → gut Ch3 (removes code that later tasks assume is gone)
2. **Task 2** → restructure Ch3 sections (depends on Task 1)
3. **Task 3** → write cross-pollination narrative (depends on Task 2 structure)
4. **Task 4** → add bib entries (no dependency, but needed before Task 5)
5. **Task 5** → write related work (depends on Task 4 bib entries)
6. **Task 6** → Fig 2.1 derivation tree (independent)
7. **Task 7** → Fig 3.2 two-layer architecture (depends on Task 2)
8. **Task 8** → Fig 3.3 CVE reachability matrix (depends on Task 3)
9. **Task 9** → Fig 3.4 grammar evolution (depends on Task 2)
10. **Task 10** → Fig 2.2 fuzzing taxonomy (independent)
11. **Task 11** → rewrite Ch4 (depends on Task 1 removing crash-pipeline refs)
12. **Task 12** → rewrite Conclusion (depends on Tasks 1-3)
13. **Task 13** → Ch4 figures (depends on Task 11)
14. **Task 14** → final check (depends on all above)

**Parallelizable groups:**
- Tasks 4+6+10 can run in parallel (independent)
- Tasks 7+8+9 can run in parallel after Task 3
- Tasks 11+12 can run in parallel after Task 3
