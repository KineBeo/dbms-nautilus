# Thesis Completeness Checklist — RL-Nautilus

**Date:** 2026-04-24
**Rating Scale:** 0 (not started) | 1 (early draft / skeleton) | 2 (partial / has gaps) | 3 (functional but needs polish) | 4 (solid, minor revisions) | 5 (publication-ready)
**Priority:** P0 (blocker — thesis cannot proceed) | P1 (critical — must fix before submission) | P2 (important — weakens paper significantly) | P3 (nice to have)

---

## Summary Dashboard

| Category | Avg Rating | Status |
|----------|:----------:|--------|
| A. Problem & Motivation | 1.5 / 5 | Implicit only, not formalized |
| B. Literature Review | 0.8 / 5 | Nearly absent |
| C. System Design & Implementation | 3.7 / 5 | Strongest area |
| D. Experiment Design | 1.7 / 5 | Phase 2 partial, Phase 3 absent |
| E. Experiment Execution | 1.3 / 5 | Only short pilots run |
| F. Results & Analysis | 1.8 / 5 | Honest but incomplete |
| G. Writing & Presentation | 0.5 / 5 | No paper draft exists |
| H. Reproducibility & Artifacts | 2.3 / 5 | Scripts exist, build broken |
| **Overall** | **1.7 / 5** | **Not submittable** |

---

## A. Problem & Motivation

| # | Criterion | Rating | Priority | What Exists | What's Missing | Action |
|---|-----------|:------:|:--------:|-------------|----------------|--------|
| A1 | Clear problem statement | 2 | P0 | Implicit: "Can RL improve grammar-based fuzzing for CVE discovery?" in CLAUDE.md and docs | No formal 1-paragraph problem statement. Reader cannot extract the problem in 30 seconds. | Write a crisp problem statement: "Grammar-based fuzzers use static mutation schedules. We investigate whether RL-driven adaptive scheduling improves CVE rediscovery rate." |
| A2 | Research gap identification | 1 | P0 | Vague reference to "Nautilus uses uniform scheduling" | No analysis of WHY static scheduling is suboptimal. No quantitative evidence of the gap (e.g., "X% of mutations are wasted on low-value strategies"). No citation of prior work showing the gap. | Analyze mutation strategy effectiveness from existing ablation data. Show % of coverage gained per strategy to motivate adaptive selection. |
| A3 | Formal hypothesis | 0 | P0 | None | No H0/H1. No quantified prediction. | Write: "H1: DQN-guided mutation selection finds ≥20% more unique root causes than uniform scheduling in 4-hour campaigns. H0: No significant difference." |
| A4 | Claimed contributions (enumerated) | 1 | P0 | Scattered across CLAUDE.md, README, docs | No numbered list of contributions. Contribution shifts between grammar design, RL, measurement framework, and CVE2Grammar pipeline. | Commit to 3 contributions: (1) MutationPolicy framework + DQN integration, (2) Fidelity measurement pipeline, (3) Empirical evaluation on 4 SQLite versions. |
| A5 | Scope & limitations stated upfront | 1 | P1 | Some limitations in ablation report §6 | Not framed as thesis-level scope. Missing: "We target known CVEs (rediscovery, not 0-day)", "Single target program (SQLite)", "5-action discrete space". | Write a Scope section bounding claims. |
| A6 | Motivation example / running scenario | 2 | P2 | CVE-2020-13434 printf overflow used as example throughout | Not structured as a motivating example in paper format. Could be a strong opening. | Structure the CVE-13434 story as Section 1 motivating example: PoC → grammar rule → mutation → discovery. |

**Category average: 1.2 / 5**

---

## B. Literature Review & Related Work

| # | Criterion | Rating | Priority | What Exists | What's Missing | Action |
|---|-----------|:------:|:--------:|-------------|----------------|--------|
| B1 | Grammar-based fuzzing survey | 2 | P1 | Nautilus NDSS'19 paper referenced and understood deeply | Missing: Superion (ASE'19), Grimoire (USENIX'19), Gramatron (ISSTA'21), Arvada (PLDI'22), Polyglot. No comparison table. | Read and cite 5+ grammar-based fuzzing papers. Build comparison table: approach, grammar type, target, results. |
| B2 | Coverage-guided fuzzing baseline | 1 | P1 | AFL fork server used | Missing: AFL++ (USENIX'20), LibFuzzer, honggfuzz as comparison baselines. No discussion of why grammar-based > coverage-only for structured inputs. | Add AFL++ as experimental baseline or cite why grammar-based is necessary for SQL. |
| B3 | RL/ML for fuzzing survey | 0 | P0 | None | Missing entirely. Critical papers: NEUZZ (S&P'19), MTFuzz (ACSAC'20), FuzzFactory (OOPSLA'19), RLCheck (ICSE'20), EcoFuzz (USENIX'20), CUPID (ACSAC'20), Boosting Fuzzer Efficiency (ESEC/FSE'21), Lv et al. "RL-based mutation" (multiple). No justification for DQN vs. MAB vs. PPO. | Survey 8-10 RL+fuzzing papers. Build taxonomy: state space, action space, reward signal, algorithm, target, results. Position your work. |
| B4 | Multi-armed bandit for scheduling | 0 | P0 | None | MOpt (USENIX'19) uses PSO for mutation scheduling — directly comparable. AFLFast uses power schedules. HavocMAB. No discussion of why DQN over simpler bandit approaches. | Read MOpt, AFLFast, and justify DQN: "Unlike MAB which treats each strategy independently, DQN captures state-dependent policy..." or pivot to MAB if justification is weak. |
| B5 | SQLite security / fuzzing literature | 2 | P2 | CVE list well-documented, Manuel Rigger bugs referenced | Missing: SQLancer (ESEC/FSE'20, by Rigger), Squirrel (CCS'20), RIFF, other SQL/DB fuzzers. | Cite 3-4 SQL-specific fuzzing tools. Explain why grammar-based approach over their metamorphic/differential approaches. |
| B6 | Crash triage / dedup literature | 1 | P2 | Stack dedup implemented, fidelity scoring designed | No citations for crash bucketing: AFL's coverage-based dedup, RETracer, !Exploitable, BugReduce. Fidelity metric is novel but not positioned against prior metrics. | Cite 3-4 crash triage papers. Position fidelity score as novel contribution. |
| B7 | Related work comparison table | 0 | P1 | None | Standard for systems papers: table comparing your approach vs. 5-8 related systems on key dimensions. | Create table: System, Grammar, RL/ML, Target, Action Space, State Space, Metric, Result. |

**Category average: 0.9 / 5**

---

## C. System Design & Implementation

| # | Criterion | Rating | Priority | What Exists | What's Missing | Action |
|---|-----------|:------:|:--------:|-------------|----------------|--------|
| C1 | System architecture diagram | 4 | P3 | `docs/architecture.md` (36 KB) with component view, dataflow, module map | Not in paper-ready format (draw.io PNG exists but not publication quality). Needs vector diagram (TikZ/Graphviz). | Convert to TikZ for paper. |
| C2 | Fuzzer engine implementation | 5 | — | Fully functional: multi-threaded coordinator, state machine, mutation pipeline, fork server. 1658 LOC Rust. | Nothing missing. Production quality. | Done. |
| C3 | Grammar engine with weighted sampling | 5 | — | `grammartec/`: loaded_dice O(1) sampling, tree mutation, recursion tracking. 2441 LOC. | Nothing missing. | Done. |
| C4 | Fork server & instrumentation | 4 | P3 | AFL-compatible fork server, shared memory bitmap, exit reason handling. 570 LOC. | Minor: no AFL++ compatibility mode documented. | Low priority. |
| C5 | Harness design & build system | 4 | P3 | ASan+UBSan+SQLITE_DEBUG, pre-loaded schema, Makefile for 4 versions. | Could document harness design decisions more formally for the paper (why not persistent mode, schema choices). | Write 1 paragraph for paper. |
| C6 | Grammar definitions (SQLite) | 4 | P2 | 4 grammar files: patterns (weighted), attack_v1, attack_v2, uniform. Well-structured 3-layer design. | P9327 has fidelity=0% (spec gap: missing coalesce). Generated grammar not self-contained. | Fix P9327 coalesce gap. Compose generated grammar with base. |
| C7 | DQN agent implementation | 3 | P1 | `dqn.rs` (422 LOC): QNetwork, ReplayBuffer, DqnTrainer, DqnWorker, epsilon-greedy, reward function. Config integration. | **Never tested in a real campaign.** Build broken (gemm-f16). No validation that DQN converges on this problem. Unknown if state representation is informative. | Fix build. Run DQN for 1 hour. Analyze convergence. |
| C8 | RL policy abstraction | 4 | P2 | `MutationPolicy` trait with DefaultPolicy and DqnPolicy. Clean separation. `rl_hook.rs`, `rl_logger.rs`. | No MAB/UCB1 policy implemented for comparison. Only 2 policies exist. | Implement UcbPolicy (~50 LOC). |
| C9 | Triage pipeline | 4 | P2 | stack_dedup, minimize, cve_signatures, fidelity_score, report. Tested (4 test files). | CVE signature matching is regex-only (fragile). Fidelity scoring not integrated into fuzzer loop. | Consider AST-based signature matching for robustness. |
| C10 | CVE2Grammar pipeline | 3 | P3 | Scraper, generalizer, emitter, validator, CLI, dashboard. 9 test files. | Generated grammar not self-contained (panics without base). Pipeline is interesting but tangential to RL thesis. | Fix composition issue. Decide if this is a contribution or just tooling. |
| C11 | Configuration & extensibility | 4 | P3 | RON config with all RL hyperparameters, serde defaults, backward-compatible. | `config.ron` template doesn't show RL fields (they only exist as defaults in code). | Add RL fields to config.ron with comments. |

**Category average: 4.0 / 5**

---

## D. Experiment Design

| # | Criterion | Rating | Priority | What Exists | What's Missing | Action |
|---|-----------|:------:|:--------:|-------------|----------------|--------|
| D1 | Research questions operationalized | 1 | P0 | Implicit: "Does attack grammar beat patterns?" tested via ablation. | No operationalized RQs for RL. Need: RQ1 (Does RL beat static?), RQ2 (DQN vs. MAB?), RQ3 (Grammar × RL interaction?). Each needs metric, threshold, statistical test. | Write 3 RQs with measurable criteria. |
| D2 | Independent variables defined | 2 | P1 | Grammar variant (4 levels). | Missing: RL policy type (Default/UCB1/DQN), RL hyperparameters, campaign duration, target version. These are the Phase 3 IVs. | Define full IV list for Phase 3. |
| D3 | Dependent variables / metrics defined | 3 | P1 | Unique root causes (RC), total crashes, fidelity score, exec/sec, queue size. | Missing: coverage-over-time (area under curve), TTFC with CI, CVE hit rate (binary), action distribution entropy, Q-value convergence rate. | Add time-series metrics and RL-specific metrics. |
| D4 | Baseline selection justified | 2 | P1 | DefaultPolicy (all-three strategies) as implicit baseline. patterns vs. uniform vs. attack. | No justification for why DefaultPolicy is the right baseline. No external baseline (AFL++, Superion). No MAB baseline. | Add UCB1 as bandit baseline. Justify DefaultPolicy = "Nautilus default behavior." |
| D5 | Statistical test plan | 0 | P0 | None | No statistical tests specified. N=2 is too small for any test. Need: Mann-Whitney U (non-parametric, small N), Vargha-Delaney A12 (effect size), bootstrap CI for TTFC. | Specify tests. Increase N to ≥5 per config. |
| D6 | Sample size / power analysis | 0 | P0 | N=2, acknowledged as insufficient | No power analysis. Fuzzing papers typically use N=5-20 with 24h campaigns. Minimum viable: N=5 with 1h campaigns. | Commit to N=5, justify duration (1h or 4h) with pilot data. |
| D7 | Duration justified | 1 | P1 | 15-min pilots run. Spec mentions 3600s/24h but not executed. | 15 min is far below field standard (24h). Even 1h is short. Need pilot data showing coverage plateaus to justify shorter duration. | Run 4h pilot, plot coverage curve, identify plateau point. Use that to justify campaign duration. |
| D8 | Target selection justified | 2 | P2 | 4 SQLite versions with known CVEs. Rationale: confirmed CVEs enable ground-truth evaluation. | Only 1 version (3.31.1) actually tested. Need all 4. Should discuss why SQLite (large, well-studied, CVE-rich) and why these specific versions. | Write justification. Run experiments on all 4 versions. |
| D9 | Ablation plan (RL-specific) | 0 | P0 | Grammar ablation exists (E2). | No RL ablation: reward shaping variants, state representation variants, epsilon schedule variants, replay buffer size. These are standard for RL papers. | Design RL ablation: at minimum, test reward function variants and state representation sizes. |
| D10 | Threats to validity | 0 | P1 | None written | Must address: internal (RNG non-determinism, short duration, single target), external (SQLite-only, known CVEs only), construct (RC count vs. true bug count, fidelity != exploitability). | Write threats section identifying ≥3 per category. |

**Category average: 1.1 / 5**

---

## E. Experiment Execution

| # | Criterion | Rating | Priority | What Exists | What's Missing | Action |
|---|-----------|:------:|:--------:|-------------|----------------|--------|
| E1 | Baseline experiments (grammar comparison) | 3 | P1 | X2 ablation: 4 variants × 2 runs × 900s on sqlite-3.31.1. Detailed root-cause analysis. | N=2 insufficient. Only 1 version. Only 15 min. Need N≥5, all 4 versions, ≥1h. | Re-run with N=5, 1h, 4 versions. |
| E2 | RL experiments (DQN) | 0 | P0 | Code exists but `rl_enabled` never set to `true`. Build broken. | **Zero RL experiments have been run.** This is the thesis core. | Fix build. Run DQN. This is THE blocker. |
| E3 | RL experiments (MAB/bandit baseline) | 0 | P0 | Not implemented | No bandit policy exists. Needed as comparison to justify DQN complexity. | Implement UCB1. Run comparison. |
| E4 | Cross-version experiments | 0 | P1 | Harnesses built for all 4 versions. | Only sqlite-3.31.1 tested. 3 versions untouched. | Run best config on 3.30.1, 3.32.0, 3.32.2. |
| E5 | Hyperparameter sensitivity | 0 | P2 | Default hyperparameters defined in config.rs. | No sweep run. Unknown if results are sensitive to lr, gamma, epsilon_decay, batch_size. | Run grid search on 2-3 key hyperparameters after E2/E3. |
| E6 | Long-duration campaigns (≥1h) | 0 | P1 | Only 15-min campaigns exist | No campaign ≥1 hour. Field standard is 24h. Minimum for credibility: 4h. | Run 4h campaigns for headline results. |
| E7 | Coverage-over-time data collection | 0 | P1 | `capture_coverage.py` captures end-of-run snapshot only | No time-series coverage data. Cannot produce coverage-over-time plots (standard in every fuzzing paper). | Add periodic logging (every 10s) to fuzzer. Re-run experiments. |
| E8 | Experiment tracking system | 0 | P2 | Results in /tmp (ephemeral). Manual log analysis. | No wandb/mlflow/tensorboard. Results not version-controlled. Difficult to reproduce or compare runs. | Set up minimal tracking: save all workdirs to version-controlled location, log configs alongside results. |

**Category average: 0.4 / 5**

---

## F. Results & Analysis

| # | Criterion | Rating | Priority | What Exists | What's Missing | Action |
|---|-----------|:------:|:--------:|-------------|----------------|--------|
| F1 | Grammar comparison results | 3 | P1 | Ablation report with raw data, aggregates, root-cause breakdown, honest interpretation. | Needs longer duration, more runs, more versions to be publication-worthy. Currently a pilot, not a result. | Upgrade to full experiment, then polish analysis. |
| F2 | Fidelity measurement results | 3 | P2 | v1 and v2 JSON files with per-pattern scores. Delta analysis (10x improvement on P13435). | Not framed as a standalone contribution. No comparison to other grammar quality metrics. | Frame as contribution if keeping in paper. |
| F3 | RL training curves | 0 | P0 | None | No Q-value convergence plots, reward curves, epsilon decay visualization, action frequency over time. These are mandatory for any RL paper. | Run DQN, collect rl_metrics.csv, plot. |
| F4 | RL vs. baseline comparison | 0 | P0 | None | The core result of the thesis does not exist. | Run E3. |
| F5 | Statistical significance reported | 0 | P0 | None | No p-values, no confidence intervals, no effect sizes. | After running with N≥5, compute Mann-Whitney U + A12. |
| F6 | Coverage-over-time plots | 0 | P1 | None | Standard figure in every fuzzing paper. You have no time-series data at all. | Implement logging, run experiments, generate plots. |
| F7 | Negative results discussed honestly | 4 | P3 | Ablation report §5-6 is exceptionally honest about thesis-negative grammar results. | Need same honesty for RL results (if negative). | Maintain this standard. |
| F8 | CVE rediscovery table | 2 | P2 | Crash-to-CVE mapping attempted via regex signatures. Table in ablation report §5e. | Only counts crash frames, not actual CVE matches. P9327 never triggered. No TTFC-per-CVE. | Improve CVE matching. Add TTFC per CVE. |
| F9 | Action distribution analysis (RL) | 0 | P0 | rl_logger.rs designed to output this but never run | Cannot analyze what DQN learns without running it. | Run DQN, analyze action frequencies. Key question: does DQN learn to favor Generate for early exploration and Havoc for later exploitation? |
| F10 | Ablation of RL components | 0 | P2 | None | Standard for RL: ablate reward terms, state features, network architecture. | After E3, run minimal ablations. |

**Category average: 1.2 / 5**

---

## G. Writing & Presentation

| # | Criterion | Rating | Priority | What Exists | What's Missing | Action |
|---|-----------|:------:|:--------:|-------------|----------------|--------|
| G1 | Paper draft (any format) | 0 | P1 | None | No LaTeX, no Overleaf, no Google Doc. Zero words of paper. | Create paper.tex with section structure. |
| G2 | Abstract (150-250 words) | 0 | P1 | None | Cannot write until results exist. But structure can be prepared. | Write abstract shell: problem, approach, [results TBD], contribution. |
| G3 | Introduction with motivation | 1 | P1 | CVE-13434 example exists in docs. Problem implicit. | Not written as paper introduction. | Draft 2-page intro using CVE-13434 as hook. |
| G4 | Related work section | 0 | P0 | None | Completely absent. Blocks submission. | Survey 15-20 papers across B1-B6 categories. Write 3-4 page related work. |
| G5 | System design section | 2 | P2 | architecture.md has content, but in internal doc format. | Needs rewriting for paper audience. Diagrams need paper formatting. | Distill architecture.md into 4-5 page design section. |
| G6 | Evaluation section | 0 | P0 | Ablation report exists as internal doc. | No paper-format evaluation. Needs: setup, methodology, RQs, results per RQ, discussion. | Write after experiments complete. |
| G7 | Figures & tables (publication quality) | 0 | P1 | Raw data exists. No plots generated. | Need: system architecture (TikZ), coverage-over-time (matplotlib), RC comparison (bar chart), action distribution (stacked area), fidelity comparison (grouped bar). Minimum 6-8 figures. | Generate after experiments. Use matplotlib + pgfplots. |
| G8 | Conclusion & future work | 0 | P3 | None | Cannot write until results exist. | Write last. |
| G9 | References / bibliography | 0 | P1 | Only Nautilus NDSS'19 cited anywhere | Need 30-50 references for a systems security venue. | Build .bib file as you read papers for B1-B6. |
| G10 | Target venue identified | 0 | P1 | None stated | Unclear if targeting top venue (USENIX Security, CCS, S&P), mid-tier (ACSAC, RAID, AsiaCCS), or workshop (FUZZING, BAR). Venue determines page limit, evaluation expectations, and timeline. | Decide venue. This determines everything else. |

**Category average: 0.3 / 5**

---

## H. Reproducibility & Artifacts

| # | Criterion | Rating | Priority | What Exists | What's Missing | Action |
|---|-----------|:------:|:--------:|-------------|----------------|--------|
| H1 | Build instructions | 3 | P2 | CLAUDE.md, README, Makefile with build commands | Build currently broken (gemm-f16). No CI. Instructions assume specific local paths. | Fix build. Add Dockerfile or CI for reproducibility. |
| H2 | Experiment scripts | 4 | P3 | run_eval.sh, run_ablation.sh, capture_coverage.py, analyze.py, smoke test. Well-structured. | Scripts use /tmp for results (ephemeral). No experiment config versioning. | Save configs + results to persistent location. |
| H3 | RNG seed control | 0 | P0 | Documented as missing (Task 0 finding b). 11+ unseeded thread_rng() call sites. | Cannot reproduce any experiment exactly. | Wire seed field through config.ron → SeedableRng. |
| H4 | Data/results archived | 1 | P1 | Fidelity JSONs in docs/. Ablation report text. | Raw workdir data in /tmp (lost on reboot). No persistent archive of crash files, coverage maps, queue contents. | Archive experiment artifacts to docs/results/ or external storage. |
| H5 | Test suite | 3 | P2 | 4 triage test files + 9 cve2grammar test files + dqn_test.rs. conftest.py configured. | No integration tests for full pipeline (grammar → fuzzer → triage → report). Rust build broken blocks DQN tests. | Fix build. Add 1-2 integration smoke tests. |
| H6 | Documentation | 4 | P3 | Extensive: architecture.md, CLAUDE.md, README, specs, plans, ablation reports. | Oriented toward developers, not paper reviewers or artifact evaluators. | Reformat key docs for artifact submission if venue requires it. |

**Category average: 2.5 / 5**

---

## Priority-Sorted Action List

### P0 — Blockers (thesis cannot proceed without these)

| # | Action | Criterion | Est. Effort | Impact |
|---|--------|-----------|:-----------:|:------:|
| 1 | **Fix gemm-f16 build error** — resolve Candle dependency so `cargo build` succeeds | C7, E2 | 2-4 hours | Unblocks ALL RL work |
| 2 | **Run DQN for 1 hour** — set `rl_enabled: true`, run on sqlite-3.31.1, check if it converges at all | E2, F3, F4 | 2 hours (after build fix) | Moment of truth for thesis |
| 3 | **Write formal hypothesis** — H0/H1 with quantified prediction and statistical test | A3, D1, D5 | 1 hour | Anchors everything |
| 4 | **Implement UCB1 bandit policy** — ~50 LOC Rust, `MutationPolicy` impl | E3, D4, B4 | 3-4 hours | Needed to justify DQN |
| 5 | **Add RNG seed control** — wire config.ron seed → SeedableRng across 11 call sites | H3, D6 | 4-6 hours | Reproducibility requirement |
| 6 | **Survey RL+fuzzing literature** — read 10 papers, write related work | B3, B4, G4 | 2-3 days | Cannot submit without this |
| 7 | **Design RL experiment matrix** — define IVs, DVs, configs, N, duration, statistical tests | D1-D6, D9 | 1 day | Prerequisite for all Phase 3 experiments |

### P1 — Critical (must fix before submission)

| # | Action | Criterion | Est. Effort | Impact |
|---|--------|-----------|:-----------:|:------:|
| 8 | **Run full baseline experiments** — N=5, 1h+, all 4 versions | E1, E4, E6 | 1-2 weeks compute | Statistical credibility |
| 9 | **Add coverage-over-time logging** — periodic CSV dump every 10s | E7, F6 | 4 hours code + re-run | Standard fuzzing paper figure |
| 10 | **Run DQN vs. UCB1 vs. Default comparison** — N=5, 1h, all 4 versions | E2, E3, F4 | 1-2 weeks compute | Core thesis result |
| 11 | **Create paper skeleton** — LaTeX with all sections, abstract shell, bib file | G1-G3, G9 | 1-2 days | Writing framework |
| 12 | **Generate publication-quality figures** — coverage curves, RC bars, action distributions | G7 | 2-3 days (after data) | Paper requires ≥6 figures |
| 13 | **Write threats to validity** | D10 | 3-4 hours | Reviewer expectation |
| 14 | **Archive experiment data** — persistent storage, not /tmp | H4 | 2 hours | Reproducibility |
| 15 | **Decide target venue** — determines page limit, eval expectations, timeline | G10 | 1 hour decision | Frames all writing |
| 16 | **Survey grammar-based fuzzing** — 5+ papers, comparison table | B1, B7 | 1-2 days | Related work section |
| 17 | **Enumerate contributions** — commit to 3 numbered contributions | A4 | 1 hour | Paper framing |
| 18 | **Increase N to ≥5 and duration to ≥1h** | D6, D7 | Folded into #8, #10 | Statistical minimum |

### P2 — Important (weakens paper significantly if absent)

| # | Action | Criterion | Est. Effort | Impact |
|---|--------|-----------|:-----------:|:------:|
| 19 | Fix P9327 fidelity gap (add coalesce to tight NTs) | C6, F8 | 2-3 hours | Completes grammar coverage |
| 20 | RL hyperparameter sensitivity analysis | E5, F10 | 1 week compute | Shows robustness |
| 21 | SQLite/SQL fuzzing literature survey | B5 | 1 day | Positions work |
| 22 | Crash triage literature survey | B6 | 0.5 day | Positions fidelity contribution |
| 23 | Rewrite architecture.md as paper design section | G5 | 2-3 days | Paper section |
| 24 | TTFC-per-CVE analysis | F8 | 4 hours (after data) | Stronger CVE-level claims |
| 25 | Experiment tracking setup (minimal: config + results in git) | E8 | 3-4 hours | Reviewers check this |
| 26 | Integration smoke test for full pipeline | H5 | 4-6 hours | Catches regressions |

### P3 — Nice to Have

| # | Action | Criterion | Est. Effort | Impact |
|---|--------|-----------|:-----------:|:------:|
| 27 | TikZ system architecture diagram | C1, G7 | 3-4 hours | Polish |
| 28 | Compose generated grammar with base grammar | C10 | 2-3 hours | Tooling completeness |
| 29 | Dockerfile for reproducible builds | H1 | 3-4 hours | Artifact evaluation |
| 30 | Add AFL++ as external baseline | B2 | 1-2 days | Stronger comparison |

---

## Critical Path

```
Fix build (#1)
    ├─→ Run DQN 1h (#2) ─→ Analyze: does RL help?
    │       ├─ YES → Full experiment matrix (#10) → Figures (#12) → Paper (#11)
    │       └─ NO  → Investigate why / pivot contribution
    │
    ├─→ Implement UCB1 (#4) ─→ Run comparison (#10)
    │
    └─→ Add seed control (#5) ─→ Reproducible experiments (#8)

In parallel:
    Literature survey (#6, #16) ─→ Related work (#11)
    Write hypothesis (#3) + contributions (#17) ─→ Intro (#11)
    Add coverage logging (#9) ─→ Re-run experiments ─→ Plots (#12)
```

**Estimated time to submittable draft:** 6-8 weeks from today, assuming full-time effort and no major RL-negative surprise requiring a pivot.

---

## Version History

| Date | Change |
|------|--------|
| 2026-04-24 | Initial audit |
