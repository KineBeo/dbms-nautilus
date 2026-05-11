# Thesis Writing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write the full LaTeX thesis "Grammar-based Greybox Fuzzing for DBMS Vulnerability Detection" for Pham Trung Kien, UET, K67CS.

**Architecture:** LaTeX `report` class based on UET template. English-only cover. 4 content chapters (Intro, Background, Method, Experiments) + Conclusion. All content in `docs/thesis/content/`, template untouched in `docs/thesis/template/`.

**Tech Stack:** LaTeX (pdflatex), natbib, booktabs, tikz, lstlisting, graphicx

**Spec:** `docs/superpowers/specs/2026-05-05-thesis-writing-design.md`

---

## File Structure

```
docs/thesis/content/
├── thesis.tex                  # Main document entry point
├── cover.tex                   # English-only cover page
├── references.bib              # Bibliography entries
├── figures/
│   └── uet.jpg                 # UET logo (copied from template)
└── chapters/
    ├── abstract.tex            # English abstract
    ├── acknowledgement.tex     # Acknowledgements
    ├── assurance.tex           # Statement of Integrity
    ├── glossary.tex            # Abbreviations table
    ├── c1_introduction.tex     # Chapter 1: Introduction
    ├── c2_background.tex       # Chapter 2: Background
    ├── c3_method.tex           # Chapter 3: Proposed Method
    ├── c4_experiments.tex      # Chapter 4: Experiments and Evaluation
    └── conclusion.tex          # Conclusion
```

---

### Task 1: Scaffold — thesis.tex, cover.tex, figures

**Files:**
- Create: `docs/thesis/content/thesis.tex`
- Create: `docs/thesis/content/cover.tex`
- Copy: `docs/thesis/template/figures/uet.jpg` → `docs/thesis/content/figures/uet.jpg`

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p docs/thesis/content/figures docs/thesis/content/chapters
cp docs/thesis/template/figures/uet.jpg docs/thesis/content/figures/uet.jpg
```

- [ ] **Step 2: Write `cover.tex` — English only**

```latex
\pagenumbering{gobble}
\begin{center}
	\begin{tikzpicture}[overlay,remember picture]
	    \draw [line width=3pt,rounded corners=0pt]
	        ($ (current page.north west) + (25mm,-25mm) $)
	        rectangle
	        ($ (current page.south east) + (-15mm,25mm) $);
	    \draw [line width=1pt,rounded corners=0pt]
	        ($ (current page.north west) + (26.5mm,-26.5mm) $)
	        rectangle
	        ($ (current page.south east) + (-16.5mm,26.5mm) $);
	\end{tikzpicture}
	\\[1mm]
	\textbf{VIETNAM NATIONAL UNIVERSITY, HANOI\\UNIVERSITY OF ENGINEERING AND TECHNOLOGY}
	\\[1cm]
	\includegraphics[width=0.2\linewidth]{figures/uet}
	\\[0.3cm]
	\textbf{Pham Trung Kien}
	\\[2cm]

	\large{\textbf{GRAMMAR-BASED GREYBOX FUZZING FOR\\DBMS VULNERABILITY DETECTION}}
	\\[2.6cm]
	\normalsize{\textbf{BACHELOR'S THESIS
		\\[2mm]
		Major: Information Technology}}
\end{center}
\vspace{16mm}
\hspace*{12mm}\textbf{Supervisor: PhD. Le Dinh Thanh}
\vfill
\begin{center}
	\textbf{HANOI - 2026}
	\vspace{4mm}
\end{center}
```

- [ ] **Step 3: Write `thesis.tex` — main document**

```latex
\documentclass[a4paper,13pt]{report}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{xspace}
\usepackage[font=small]{caption}
\usepackage{booktabs}
\usepackage[unicode]{hyperref}
\usepackage[left=3cm,right=2cm,top=2.5cm,bottom=3cm]{geometry}
\usepackage{titlesec}
\usepackage{scrextend}
\usepackage{enumerate}
\usepackage{url}
\usepackage{tikz}
\usepackage{float}
\usepackage{afterpage}
\usepackage{multirow}
\usepackage{sectsty}
\usepackage{tocloft,calc}
\usepackage{listings}
\usepackage{makecell}
\usepackage[sort&compress]{natbib}
\usetikzlibrary{calc}
\usepackage{algorithm}
\usepackage{algpseudocode}
\usepackage{subcaption}
\usepackage[flushleft]{threeparttable}
\usepackage{perpage}
\MakePerPage{footnote}
\PassOptionsToPackage{table}{xcolor}

\def\changemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}
\let\endchangemargin=\endlist

\changefontsizes{13pt}
\bibliographystyle{unsrt}

\makeatletter
\def\l@figure{\@dottedtocline{1}{1em}{2.2em}}
\def\l@table{\@dottedtocline{1}{1em}{2.2em}}
\makeatother

\sectionfont{\fontsize{15}{15}\selectfont}
\subsectionfont{\fontsize{13}{15}\selectfont}

\titleformat{\chapter}[display]
{\normalfont\huge\bfseries}{\chaptertitlename\ \thechapter}{0pt}{\LARGE}
\titlespacing*{\chapter}{0cm}{-\topskip}{0pt}[0pt]

\renewcommand{\baselinestretch}{1.3}
\renewcommand{\cftchappresnum}{Chapter }
\AtBeginDocument{\addtolength\cftchapnumwidth{\widthof{\bfseries Chapter }}}
\setlength{\parskip}{0.4em}
\setlength{\parindent}{0pt}

\title{Grammar-based Greybox Fuzzing for DBMS Vulnerability Detection}
\author{Pham Trung Kien}

\newcommand{\argmax}{\arg\!\max}

\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}
\definecolor{mauve}{rgb}{0.58,0,0.82}
\definecolor{darkblue}{rgb}{0.0,0.0,0.6}
\definecolor{lightblue}{rgb}{0.0,0.0,0.9}
\definecolor{cyan}{rgb}{0.0,0.6,0.6}
\definecolor{darkred}{rgb}{0.6,0.0,0.0}
\definecolor{bg_gray}{RGB}{242, 242, 235}

\lstset{
  basicstyle=\ttfamily\footnotesize,
  columns=fullflexible,
  showstringspaces=false,
  numbers=left,
  numberstyle=\small\color{gray},
  stepnumber=1,
  numbersep=5pt,
  backgroundcolor=\color{bg_gray},
  showspaces=false,
  showstringspaces=false,
  showtabs=false,
  frame=none,
  rulecolor=\color{black},
  tabsize=2,
  captionpos=b,
  breaklines=true,
  breakatwhitespace=false,
  title=\lstname,
  commentstyle=\color{gray}\upshape
}

\begin{document}
\input{cover}\newpage\cleardoublepage

\input{chapters/assurance}\newpage\cleardoublepage
\input{chapters/acknowledgement}\newpage\cleardoublepage
\input{chapters/abstract}\newpage\cleardoublepage

\addcontentsline{toc}{chapter}{Contents}
\tableofcontents\newpage\cleardoublepage

\newpage
\addcontentsline{toc}{chapter}{\listfigurename}
\listoffigures\cleardoublepage

\newpage
\addcontentsline{toc}{chapter}{\listtablename}
\listoftables

\newpage
\input{chapters/glossary}\newpage\cleardoublepage

\setcounter{page}{1}
\pagenumbering{arabic}

\input{chapters/c1_introduction}\newpage\cleardoublepage
\input{chapters/c2_background}\newpage\cleardoublepage
\input{chapters/c3_method}\newpage\cleardoublepage
\input{chapters/c4_experiments}\newpage\cleardoublepage
\input{chapters/conclusion}\newpage\cleardoublepage

\phantomsection
\addcontentsline{toc}{chapter}{References}
\bibliography{references}\newpage\cleardoublepage
\end{document}
```

- [ ] **Step 4: Commit scaffold**

```bash
git add -f docs/thesis/content/
git commit -m "docs(thesis): scaffold thesis.tex, cover.tex, figures"
```

---

### Task 2: Front Matter — assurance, acknowledgement, abstract, glossary

**Files:**
- Create: `docs/thesis/content/chapters/assurance.tex`
- Create: `docs/thesis/content/chapters/acknowledgement.tex`
- Create: `docs/thesis/content/chapters/abstract.tex`
- Create: `docs/thesis/content/chapters/glossary.tex`

- [ ] **Step 1: Write `assurance.tex`**

Statement of Integrity in English. Replace student name, thesis title, supervisor name.

- [ ] **Step 2: Write `acknowledgement.tex`**

Acknowledgements to UET Faculty of IT, supervisor PhD. Le Dinh Thanh, classmates in K67CS. Keep concise (1 page).

- [ ] **Step 3: Write `abstract.tex`**

English abstract (~200 words). Structure: problem (DBMS vulnerabilities), approach (grammar-based greybox fuzzing with bandit sampling), key results (uniform outperforms bandit 2x in crash diversity, p≈0.01; grammar v3.2 enables all 6 CVE patterns), keywords.

Keywords: Grammar-based Fuzzing, Greybox Fuzzing, DBMS Security, Vulnerability Detection, Multi-Armed Bandit

- [ ] **Step 4: Write `glossary.tex`**

Abbreviations table with these entries:

| Abbrev | Full | Description |
|--------|------|-------------|
| AFL | American Fuzzy Lop | Coverage-guided greybox fuzzer |
| ASan | AddressSanitizer | Memory error detector |
| CFG | Context-Free Grammar | Formal grammar for input generation |
| CVE | Common Vulnerabilities and Exposures | Vulnerability identifier |
| DBMS | Database Management System | Software for managing databases |
| DQN | Deep Q-Network | Deep reinforcement learning algorithm |
| FTS | Full-Text Search | SQLite text search extension |
| MAB | Multi-Armed Bandit | Online learning framework |
| RL | Reinforcement Learning | Machine learning paradigm |
| SQL | Structured Query Language | Database query language |
| TTFC | Time-To-First-Crash | Time until first crash found |
| UBSan | Undefined Behavior Sanitizer | Undefined behavior detector |

- [ ] **Step 5: Commit front matter**

```bash
git add -f docs/thesis/content/chapters/assurance.tex docs/thesis/content/chapters/acknowledgement.tex docs/thesis/content/chapters/abstract.tex docs/thesis/content/chapters/glossary.tex
git commit -m "docs(thesis): add front matter (assurance, acknowledgement, abstract, glossary)"
```

---

### Task 3: references.bib

**Files:**
- Create: `docs/thesis/content/references.bib`

- [ ] **Step 1: Write `references.bib`**

Key references needed (minimum set — add more during chapter writing):

1. **Nautilus** — Aschermann et al., "NAUTILUS: Fishing for Deep Bugs with Grammars", NDSS 2019
2. **AFL** — Zalewski, "American Fuzzy Lop", 2014
3. **Superion** — Wang et al., "Superion: Grammar-Aware Greybox Fuzzing", ICSE 2019
4. **Grimoire** — Blazytko et al., "GRIMOIRE: Synthesizing Structure while Fuzzing", USENIX Security 2019
5. **SQLite** — Hipp, "SQLite", official documentation
6. **ASan** — Serebryany et al., "AddressSanitizer: A Fast Address Sanity Checker", USENIX ATC 2012
7. **EXP3** — Auer et al., "The Nonstochastic Multiarmed Bandit Problem", SIAM 2002
8. **LibFuzzer** — LLVM Project, "libFuzzer"
9. **CVE-2020-13434** — NVD entry, sqlite printf integer overflow
10. **CVE-2020-9327** — NVD entry, sqlite generated column uninitialized pointer
11. **CVE-2020-13435** — NVD entry, sqlite NULL pointer
12. **CVE-2020-13871** — NVD entry, sqlite use-after-free
13. **CVE-2020-15358** — NVD entry, sqlite heap buffer overread
14. **CVE-2019-19646** — NVD entry, sqlite integrity_check infinite loop
15. **Mann-Whitney U** — Mann & Whitney, "On a Test of Whether One of Two Random Variables is Stochastically Larger than the Other", 1947
16. **Loaded Dice** — Smith & Tromble, "Sampling from the Unit Simplex", 2004 (alias method)
17. **Coverage-guided fuzzing survey** — Manès et al., "The Art, Science, and Engineering of Fuzzing: A Survey", IEEE TSE 2021
18. **Squirrel** — Zhong et al., "Squirrel: Testing Database Management Systems with Language Validity and Coverage Feedback", CCS 2020
19. **SQLsmith** — Seltenreich, "SQLsmith: A Random SQL Query Generator", 2015

- [ ] **Step 2: Commit references**

```bash
git add -f docs/thesis/content/references.bib
git commit -m "docs(thesis): add references.bib with core bibliography"
```

---

### Task 4: Chapter 1 — Introduction

**Files:**
- Create: `docs/thesis/content/chapters/c1_introduction.tex`

**Data sources:**
- `docs/cve-list.md` — CVE details
- `CLAUDE.md` — project overview

- [ ] **Step 1: Write Chapter 1**

Sections:
- **1.1 Context and Motivation** (~1.5 pages): Software vulnerabilities in DBMS systems. SQLite as most deployed database (billions of devices). CVEs as ground truth. Fuzzing as automated discovery. Grammar-based fuzzing advantage over byte-level mutation for structured inputs like SQL.
- **1.2 Problem Statement** (~0.5 page): Grammar-based fuzzers use uniform random sampling across production rules. This wastes mutations on low-value paths. Research question: can adaptive sampling via multi-armed bandit improve crash diversity?
- **1.3 Objectives and Scope** (~0.5 page): Three objectives. Scope: SQLite versions 3.30.1-3.32.2, 6 known CVEs, 30-minute campaigns.
- **1.4 Contributions** (~0.5 page): Three contributions listed.
- **1.5 Thesis Organization** (~0.5 page): Chapter roadmap paragraph.

Style: continuous prose, no bullet points. Cite references with `\cite{}`. Follow reference PDF style (see Introduction chapter pp.1-3).

- [ ] **Step 2: Commit**

```bash
git add -f docs/thesis/content/chapters/c1_introduction.tex
git commit -m "docs(thesis): write Chapter 1 — Introduction"
```

---

### Task 5: Chapter 2 — Background

**Files:**
- Create: `docs/thesis/content/chapters/c2_background.tex`

**Data sources:**
- Reference PDF pp.4-8 for style (Definition format, figure placement, subsection depth)

- [ ] **Step 1: Write Chapter 2**

Sections:
- **2.1 Software Vulnerabilities and CVEs** (~1 page): CVE system explanation. Vulnerability classes relevant to DBMS: buffer overflow, use-after-free, integer overflow, null pointer dereference, undefined behavior. SQLite vulnerability history.
- **2.2 Fuzzing** (~1.5 pages): Definition. Taxonomy: black-box (random), white-box (symbolic execution), greybox (coverage-guided). Mutation-based vs generation-based. Coverage feedback loop diagram concept.
- **2.3 Grammar-Based Fuzzing** (~2 pages): Context-free grammar definition (use `\textbf{Definition 2.1:}` format). Production rules, derivation trees. Grammar-guided input generation. Tree-level mutations (splice, replace subtree, random recursion). Nautilus architecture overview: grammar engine → tree generation → unparse → fork server → coverage feedback.
- **2.4 Coverage-Guided Feedback** (~1 page): AFL fork server model. Shared memory bitmap. Edge coverage (source→target basic block pairs). How coverage guides input selection.
- **2.5 Multi-Armed Bandit Algorithms** (~1.5 pages): Problem formulation. Exploration-exploitation tradeoff. UCB1 algorithm. EXP3 (Exponential-weight algorithm for Exploration and Exploitation) for adversarial settings. Application to rule selection: each grammar rule = arm, reward = new coverage.
- **2.6 Sanitizers as Oracles** (~1 page): ASan (heap overflow, use-after-free, stack overflow). UBSan (signed integer overflow, null pointer, shift). Debug assertions (SQLITE_DEBUG). How sanitizers transform silent bugs into detectable crashes with exit codes.
- **2.7 Related Work** (~2 pages): Nautilus (Aschermann et al., NDSS 2019) — original grammar fuzzer, context-free grammar, coverage feedback. Superion (Wang et al., ICSE 2019) — grammar-aware mutation for JavaScript/XML. Grimoire (Blazytko et al., USENIX 2019) — synthesizing structure without explicit grammar. Squirrel (Zhong et al., CCS 2020) — DBMS-specific fuzzing with SQL validity. SQLsmith — random SQL query generator. AFL/LibFuzzer — general-purpose coverage-guided fuzzers. Position this thesis: extends Nautilus with adaptive rule selection via bandit.

Use `lstlisting` for any code/SQL examples. Use `figure` for diagrams. Use `\cite{}` throughout.

- [ ] **Step 2: Commit**

```bash
git add -f docs/thesis/content/chapters/c2_background.tex
git commit -m "docs(thesis): write Chapter 2 — Background"
```

---

### Task 6: Chapter 3 — Proposed Method

**Files:**
- Create: `docs/thesis/content/chapters/c3_method.tex`

**Data sources:**
- `docs/architecture.md` — system architecture
- `CLAUDE.md` — component overview, build commands
- `grammars/active/sqlite_v3.py` — grammar rules
- `grammars/CHANGELOG.md` — grammar evolution
- `triage/cve_signatures.py` — CVE signature patterns
- `triage/stack_dedup.py` — dedup algorithm
- `harness/` — harness source code

- [ ] **Step 1: Write Chapter 3**

Sections:
- **3.1 System Overview** (~1.5 pages): Architecture diagram (TikZ or described for manual drawing). Components: Grammar Engine (grammartec, Rust, 2441 LOC) → Fuzzer Coordinator (fuzzer, Rust, 1658 LOC) → Fork Server (forksrv, Rust, 570 LOC) → Harness (C, ~200 LOC) → Triage Pipeline (Python, ~500 LOC). Data flow: grammar rules → weighted sampling → tree generation → unparse to SQL → fork+exec → coverage bitmap → feedback → weight update.

- **3.2 Grammar Design** (~3 pages):
  - Structural primitives philosophy: encode SQL *structural patterns* that trigger bug classes, not specific PoC inputs. Zero PoC contamination principle.
  - Layer 1 (SQL primitives): SELECT, Expr, Func-Call, Literal, Table-Name — 30+ Expr alternatives, window/frame/ordering.
  - Layer 2 (composed patterns): Schema-Setup (6 alternatives: single table, genCol, two tables, table+view, virtual table, table+index), Stress-Query (8 alternatives), Validation-Op (4 alternatives), Boundary-Func-Call.
  - Show grammar rule examples using `lstlisting` (Python DSL):
    ```
    ctx.rule("Schema-Setup",
        "CREATE TABLE IF NOT EXISTS p({Col-Def-List-GenCol})",
        weight=3.0)
    ```
  - Grammar evolution table: v3.0 (449 rules, FTS-dominated) → v3.1 (449 rules, S5 weight rebalanced) → v3.2 (475 rules, +window functions, +self-ref columns).

- **3.3 Weighted Sampling with Bandit Policy** (~2 pages):
  - `loaded_dice::Dice` for O(1) weighted categorical sampling (alias method).
  - Bandit formulation: each production rule for a non-terminal = one arm. Reward = new edge coverage discovered when the generated input uses that rule.
  - EXP3-style weight update: `w_i ← w_i × exp(η × r_i / p_i)` where r_i is normalized reward, p_i is sampling probability, η is learning rate.
  - Uniform baseline: all rules equal weight = 1.0.
  - Show pseudocode using `algorithm` + `algpseudocode` environment.

- **3.4 Harness Construction** (~1.5 pages):
  - AFL fork server protocol: `__AFL_INIT()` macro, child process per input.
  - NOT persistent mode (no `__AFL_LOOP`) — Nautilus doesn't implement that protocol.
  - Pre-loaded schema: tables t1(c1,c2,c3), t2(c1,c2), t3(c1,c2,c3), FTS table fts_t1.
  - Oracle classification: ASan crash → exit 223, UBSan → exit 1, SIGNAL(5) → SQLite debug assert, semantic SQL errors → ignored.
  - Show harness code snippet using `lstlisting` (C language).

- **3.5 Triage Pipeline** (~2 pages):
  - Stack-hash dedup: run crashing input under gdb, extract top 3 stack frames, SHA-256 hash → unique crash identifier.
  - Fidelity scoring: replay crash N times, measure reproducibility rate.
  - CVE signature matching: regex-based structural pattern matching. Each CVE has required SQL patterns (e.g., CVE-2020-13434 requires `printf` call + INT32 boundary value). Show signature example from `triage/cve_signatures.py`.
  - Crash minimization: remove SQL statements while preserving crash behavior.

- **3.6 CVE Target Selection** (~1 page):
  - Table of 4 SQLite versions, 6 CVEs, vulnerability type, affected component.
  - Selection criteria: versions with confirmed CVEs, available PoCs for validation, diverse vulnerability classes.

- [ ] **Step 2: Commit**

```bash
git add -f docs/thesis/content/chapters/c3_method.tex
git commit -m "docs(thesis): write Chapter 3 — Proposed Method"
```

---

### Task 7: Chapter 4 — Experiments and Evaluation

**Files:**
- Create: `docs/thesis/content/chapters/c4_experiments.tex`

**Data sources:**
- `results/campaigns/*/campaign.json` — campaign results
- `workdirs/*/coverage.csv` — coverage data
- `results/time_to_first_crash.md` — TTFC analysis
- `docs/cve-list.md` — CVE details
- `triage/cve_signatures.py` — signature patterns
- `grammars/CHANGELOG.md` — grammar versions

- [ ] **Step 1: Write Chapter 4**

Sections:
- **4.1 Experimental Setup** (~1.5 pages):
  - Hardware: document the machine specs (CPU, RAM, OS).
  - Campaign parameters table: duration=30min, N=5 runs per (version, policy), grammar=v3.2 (active), 3 target versions (3.30.1, 3.31.1, 3.32.0), max_tree_size=300, timeout_ms=500, threads=1, bitmap_size=2MB.
  - Policies compared: bandit (EXP3 weight updates) vs uniform (all weights=1.0).
  - Also: v3.4-fixed bandit and uniform variants on sqlite-3.31.1 (additional 5+5 runs).

- **4.2 RQ1: Does weighted (bandit) grammar sampling find more diverse crash classes than uniform?** (~2.5 pages):
  - Metric: unique root causes per campaign after stack-hash dedup.
  - Table 4.1: Per-version results:

    | Version | Policy | N | Mean | Std | Min | Max |
    |---------|--------|---|------|-----|-----|-----|
    | 3.30.1 | bandit | 5 | ... | ... | ... | ... |
    | 3.30.1 | uniform | 5 | ... | ... | ... | ... |
    | 3.31.1 | bandit | 5 | ... | ... | ... | ... |
    | ... | ... | ... | ... | ... | ... | ... |
    | ALL | bandit | 19 | 4.2 | 1.42 | ... | ... |
    | ALL | uniform | 20 | 8.6 | 6.37 | ... | ... |

  - Statistical test: Mann-Whitney U (non-parametric, robust for small N=5).
  - Result: overall p≈0.01, uniform significantly outperforms bandit in crash diversity.
  - Per-version: only sqlite-3.32.0 individually significant (p≤0.05).
  - Bar chart figure: unique root causes per version × policy.
  - Discussion: bandit converges to exploitation (low variance, std=1.42), uniform maintains exploration (high variance, std=6.37, some runs find 27 unique bugs).

- **4.3 RQ2: How does crash discovery rate change over time per policy?** (~2 pages):
  - Table 4.2: Time-to-first-crash (all 1-2 seconds, no difference).
  - Table 4.3: Crash accumulation at checkpoints (60s, 300s, 600s, 900s, 1800s).
  - Table 4.4: Crash rate by time window (0-5min, 5-10min, 10-15min, 15-30min).
  - Key finding: both crash in 1-2s, TTFC not a differentiator. Rate decay: bandit -58%, uniform -51%.
  - Line chart figure: crash rate over time windows.
  - Discussion: TTFC wrong metric for grammar-based CVE fuzzers. Structural diversity matters more.

- **4.4 RQ3: Does grammar structural coverage affect CVE reachability?** (~2 pages):
  - Table 4.5: CVE signature requirements vs grammar coverage (before v3.2 vs after v3.2).

    | CVE | Required Patterns | v3.1 Coverage | v3.2 Coverage |
    |-----|-------------------|---------------|---------------|
    | CVE-2020-9327 | GENERATED col, coalesce, JOIN, VIEW, self-ref | 2/5 | 5/5 |
    | CVE-2020-13435 | NATURAL JOIN, coalesce, window OVER, UNIQUE, IN subquery | 2/5 | 5/5 |
    | CVE-2020-13871 | EXCEPT, ORDER BY 3+, scalar subquery, count(), lead() | 1/5 | 5/5 |
    | CVE-2020-15358 | VIEW+ORDER BY, INTERSECT in WHERE, implicit JOIN | 1/3 | 3/3 |
    | CVE-2020-13434 | printf, INT32 boundary | 2/2 | 2/2 |
    | CVE-2019-19646 | GENERATED ALWAYS AS, PRAGMA integrity_check | 2/2 | 2/2 |

  - Gap analysis: 5 missing structural primitives (window functions, self-ref columns, count() zero-arg, ORDER BY 3-term, compound ops in scalar subqueries).
  - Grammar v3.2: +23 rules, all 6 CVEs now structurally reachable.
  - Discussion: CVEs encode structural patterns, not specific inputs. Grammar design must cover SQL feature space, not individual PoCs.

- **4.5 RQ4: What is the effect of grammar evolution on bug discovery?** (~1.5 pages):
  - Table 4.6: Grammar version comparison:

    | Version | Rules | Key Change | Crash Distribution |
    |---------|-------|------------|-------------------|
    | v3.0 | 449 | Initial structural primitives | 92% FTS5 crashes |
    | v3.1 | 449 | S5 weight 2.0→0.5 | Diverse portfolio |
    | v3.2 | 475 | +window funcs, +self-ref cols | All CVEs reachable |

  - Discussion: grammar evolution matters more than sampling policy for CVE reachability. Weight tuning (v3.0→v3.1) had bigger impact than bandit vs uniform.

- **4.6 Threats to Validity** (~1 page):
  - Internal: N=5 runs per cell (small sample), no wall-clock timestamps in exec.log (only execution count), bandit hyperparameters not tuned.
  - External: SQLite-only (results may not generalize to MySQL/PostgreSQL), single grammar language (SQL).
  - Construct: stack-hash dedup sensitivity (top-3 frames may over/under-count), fidelity scoring threshold.

- [ ] **Step 2: Commit**

```bash
git add -f docs/thesis/content/chapters/c4_experiments.tex
git commit -m "docs(thesis): write Chapter 4 — Experiments and Evaluation"
```

---

### Task 8: Conclusion

**Files:**
- Create: `docs/thesis/content/chapters/conclusion.tex`

- [ ] **Step 1: Write Conclusion**

Structure (~1.5 pages):
- **Summary:** Grammar-based greybox fuzzing system for SQLite vulnerability detection. Designed structural primitives grammar (475 rules, 3 versions). Compared bandit vs uniform sampling across 53 campaigns, 3 SQLite versions, 6 CVEs.
- **Key findings:**
  1. Uniform sampling discovers 2x more unique crash classes than bandit (p≈0.01).
  2. Bandit converges to exploitation, uniform maintains exploration — for CVE-class discovery where structural diversity matters, exploration wins.
  3. Grammar structural coverage is the bottleneck for CVE reachability — 4 of 6 CVEs required specific SQL primitives absent from the initial grammar.
  4. Grammar evolution (weight tuning, primitive additions) has larger effect on bug discovery than sampling policy.
- **Contributions recap:** Three contributions from Chapter 1.
- **Limitations:** Small N, SQLite-only, no RL agent yet, no persistent-mode harness.
- **Future work:** (1) DQN agent for learned mutation strategy (Phase 3), (2) larger campaign durations (hours/days), (3) additional DBMS targets (MySQL, PostgreSQL), (4) grammar composition from multiple sources.

- [ ] **Step 2: Commit**

```bash
git add -f docs/thesis/content/chapters/conclusion.tex
git commit -m "docs(thesis): write Conclusion"
```

---

### Task 9: Verify LaTeX Compilation

**Files:**
- All files in `docs/thesis/content/`

- [ ] **Step 1: Attempt compilation**

```bash
cd docs/thesis/content && pdflatex -interaction=nonstopmode thesis.tex
```

Check for errors. Common issues: missing packages, undefined references, broken `\cite{}` keys.

- [ ] **Step 2: Run bibtex + second pass**

```bash
cd docs/thesis/content && bibtex thesis && pdflatex -interaction=nonstopmode thesis.tex && pdflatex -interaction=nonstopmode thesis.tex
```

Two passes needed for references and TOC.

- [ ] **Step 3: Fix any compilation errors**

Address LaTeX errors one by one. Common fixes: escape special characters, fix figure paths, resolve missing bib entries.

- [ ] **Step 4: Commit fixes**

```bash
git add -f docs/thesis/content/
git commit -m "docs(thesis): fix LaTeX compilation issues"
```

---

### Task 10: Final Review and Polish

- [ ] **Step 1: Check all figures/tables referenced in text**

Every `\ref{}` and `\cite{}` must resolve. Every table/figure must be explained in surrounding prose.

- [ ] **Step 2: Check page count**

Target: ~35-45 pages total (excluding front matter). Ch1≈4, Ch2≈8-10, Ch3≈10-12, Ch4≈10-12, Conclusion≈1-2.

- [ ] **Step 3: Verify no bullet-point writing**

Template requirement: continuous prose, no `\begin{itemize}` in main chapters (allowed only in glossary and front matter).

- [ ] **Step 4: Final commit**

```bash
git add -f docs/thesis/content/
git commit -m "docs(thesis): final review and polish"
```
