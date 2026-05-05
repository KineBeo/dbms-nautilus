# Thesis Writing Design Spec

**Date:** 2026-05-05
**Author:** Pham Trung Kien
**Supervisor:** PhD. Le Dinh Thanh
**Cohort:** K67CS

## Thesis Metadata

- **Title:** Grammar-based Greybox Fuzzing for DBMS Vulnerability Detection
- **Language:** 100% English
- **Template:** `docs/thesis/template/` (UET LaTeX template, `report` class, 13pt, a4paper)
- **Style reference:** `docs/thesis/reference/AKALLM1012-1.pdf` (code blocks via `lstlisting`, figures via `\includegraphics`, tables via `booktabs`, citations via `natbib/unsrt`)
- **Cover:** English only (single cover page, no Vietnamese covers)

## Chapter Structure

### Front Matter
- Cover page (English only): UET header, student name, thesis title, supervisor, HANOI - 2026
- Statement of Integrity
- Acknowledgements
- Abstract (English only)
- List of Figures
- List of Tables
- List of Abbreviations

### Chapter 1: Introduction (~4 pages)
- 1.1 Context and Motivation
  - Software vulnerabilities in DBMS, SQLite as critical infrastructure
  - CVEs as ground truth for evaluating fuzzers
  - Fuzzing as automated vulnerability discovery
- 1.2 Problem Statement
  - Grammar-based fuzzing generates valid inputs but uniform sampling wastes mutations
  - Can adaptive sampling (bandit) improve crash diversity over uniform?
- 1.3 Objectives and Scope
  - Build grammar-based greybox fuzzer targeting SQLite
  - Design CVE-aware structural grammar (no PoC contamination)
  - Compare bandit vs uniform sampling across 4 SQLite versions (6 CVEs)
- 1.4 Contributions
  1. Structural primitives grammar design methodology
  2. Multi-armed bandit integration for grammar rule selection
  3. Empirical comparison: 53 campaigns, Mann-Whitney U statistical analysis
- 1.5 Thesis Organization

### Chapter 2: Background (~8-10 pages)
- 2.1 Software Vulnerabilities and CVEs
- 2.2 Fuzzing (random, mutation-based, generation-based, greybox)
- 2.3 Grammar-Based Fuzzing (CFG, tree mutation, Nautilus)
- 2.4 Coverage-Guided Feedback (AFL fork server, shared bitmap, edge coverage)
- 2.5 Multi-Armed Bandit Algorithms (exploration vs exploitation, EXP3/UCB)
- 2.6 Sanitizers as Oracles (ASan, UBSan, debug assertions)
- 2.7 Related Work (Nautilus original, Superion, AFL, LibFuzzer, Grimoire)

### Chapter 3: Proposed Method (~10-12 pages)
- 3.1 System Overview (architecture diagram)
- 3.2 Grammar Design
  - Structural primitives philosophy (zero PoC contamination)
  - Layer decomposition: Schema-Setup, Stress-Query, Validation-Op, Boundary-Func
  - Grammar evolution: v3.0 → v3.1 → v3.2, 449 → 475 rules
- 3.3 Weighted Sampling with Bandit Policy
  - loaded_dice for O(1) weighted sampling
  - EXP3 reward from coverage feedback
  - Weight update mechanism
- 3.4 Harness Construction
  - AFL fork server mode (__AFL_INIT only, no persistent mode)
  - Pre-loaded schema (t1, t2, t3, fts_t1)
  - ASan + UBSan oracle, exit code classification
- 3.5 Triage Pipeline
  - Stack-hash dedup (gdb-based)
  - Fidelity scoring
  - CVE signature matching (regex-based structural patterns)
  - Crash minimization
- 3.6 CVE Target Selection
  - 4 versions: sqlite-3.30.1, 3.31.1, 3.32.0, 3.32.2
  - 6 CVEs with known PoCs
  - Structural pattern analysis per CVE

### Chapter 4: Experiments and Evaluation (~10-12 pages)
- 4.1 Experimental Setup
  - Hardware configuration
  - Campaign parameters: 30min duration, N=5 runs per (version, policy)
  - Grammar versions tested
  - 3 target SQLite versions in main comparison
- 4.2 RQ1: Crash Diversity (bandit vs uniform)
  - Metric: unique root causes per campaign (stack-hash dedup)
  - Result: uniform mean=8.6, bandit mean=4.2, p≈0.01 (Mann-Whitney U)
  - Per-version breakdown, only 3.32.0 individually significant
  - Tables + bar charts
- 4.3 RQ2: Crash Discovery Rate Over Time
  - Time-to-first-crash: both 1-2s, no difference
  - Crash rate decay: bandit -58%, uniform -51%
  - Crash accumulation table at 60s/300s/600s/900s/1800s
  - Line chart: crashes over time
- 4.4 RQ3: CVE Reachability
  - Gap analysis: 4 CVEs unreachable in v3.1 grammar
  - Missing primitives: window functions, self-ref generated columns, count() zero-arg
  - Grammar v3.2 additions: +23 rules, all 6 CVEs now structurally reachable
  - CVE signature matching table
- 4.5 RQ4: Grammar Evolution Effect
  - v3.0: 92% crashes from FTS5 (S5 weight too high)
  - v3.1: rebalanced, diverse crash portfolio
  - v3.2: window functions, self-ref columns, 475 rules
  - Before/after crash class distribution
- 4.6 Threats to Validity
  - Internal: N=5 small sample, no wall-clock timestamps for precise TTFC
  - External: SQLite-specific results, single grammar language
  - Construct: stack-hash dedup may over/under-count

### Conclusion (~1-2 pages)
- Summary of findings
- Key result: uniform outperforms bandit in crash diversity (2x), bandit converges to exploitation
- Contributions recap
- Limitations
- Future work: DQN agent (Phase 3), larger campaign durations, more DBMS targets

## Data Sources for Thesis

| Data | Location | Used In |
|------|----------|---------|
| Campaign results (53 campaigns) | `results/campaigns/*/campaign.json` | RQ1, RQ2 |
| Triage reports | `results/campaigns/*/triage_report.md` | RQ1 |
| Coverage CSVs | `workdirs/*/coverage.csv` | RQ2 |
| TTFC analysis | `results/time_to_first_crash.md` | RQ2 |
| CVE list + PoCs | `docs/cve-list.md` | RQ3 |
| CVE signatures | `triage/cve_signatures.py` | RQ3 |
| Grammar versions | `grammars/v3.0/`, `v3.1/`, `v3.2/`, `active/` | RQ4 |
| Grammar changelog | `grammars/CHANGELOG.md` | RQ4 |
| Architecture docs | `docs/architecture.md`, `CLAUDE.md` | Ch3 |

## LaTeX Conventions (from reference)

- Code blocks: `\lstlisting` with `basicstyle=\ttfamily\footnotesize`, line numbers, gray background
- Figures: `\includegraphics` inside `figure` float, caption below (`\captionpos=b`)
- Tables: `booktabs` style (`\toprule`, `\midrule`, `\bottomrule`), caption above
- Citations: `\cite{}` with `natbib`, `unsrt` bibliography style
- Definitions: `\textbf{Definition X.Y:}` in italics
- No bullet-point writing — continuous prose with proper argumentation flow
- All figures and tables must be referenced and explained in text

## Figures Planned

1. System architecture diagram (fuzzer → fork server → harness → bitmap → feedback loop)
2. Grammar rule tree example (showing Schema-Setup → Col-Def-List → GenCol-Expr decomposition)
3. Bandit weight update flow diagram
4. Crash diversity bar chart (bandit vs uniform, per version)
5. Crash accumulation over time (line chart)
6. Crash rate decay comparison (line chart)
7. CVE reachability matrix (before/after v3.2)
8. Grammar evolution timeline (v3.0 → v3.1 → v3.2 with rule counts)

## Tables Planned

1. CVE target versions and details
2. Experimental configuration
3. RQ1: Unique root causes per campaign (mean, std, p-value)
4. RQ2: Time-to-first-crash summary
5. RQ2: Crash accumulation at time checkpoints
6. RQ2: Crash rate by time window
7. RQ3: CVE signature pattern requirements vs grammar coverage
8. RQ4: Grammar version comparison (rules, crash distribution)
9. Abbreviations table

## Output Structure

```
docs/thesis/
├── template/          # Original template (untouched)
├── reference/         # Style reference PDF
└── content/           # NEW: thesis LaTeX files
    ├── thesis.tex     # Main document (modified from template)
    ├── cover.tex      # English-only cover
    ├── references.bib # Bibliography
    ├── figures/        # Generated figures
    │   └── uet.jpg    # Copied from template
    └── chapters/
        ├── abstract.tex
        ├── acknowledgement.tex
        ├── assurance.tex
        ├── glossary.tex
        ├── c1_introduction.tex
        ├── c2_background.tex
        ├── c3_method.tex
        ├── c4_experiments.tex
        └── conclusion.tex
```
