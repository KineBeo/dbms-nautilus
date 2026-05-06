# Research Project Audit: RL-Nautilus

**Date:** 2026-04-24
**Auditor:** Claude (Senior Research Advisor)
**Branch:** phase-2
**Scope:** End-to-end project audit mapped against a standard research paper framework

---

## 1. Project Summary

RL-Nautilus is a grammar-based coverage-guided fuzzer (fork of Nautilus 2.0, Rust) enhanced with weighted grammar sampling and a DQN reinforcement learning agent for adaptive mutation strategy selection, targeting automated rediscovery of known CVEs in SQLite. The project fuzzes 4 CVE-bearing SQLite versions (3.30.1, 3.31.1, 3.32.0, 3.32.2) and includes a secondary pipeline (`cve2grammar`) that scrapes known DBMS bug reports, generalizes them via LLM into grammar rules, and renders Nautilus-compatible Python grammars.

---

## 2. Framework Status Table

| Phase | Status | What Exists | What's Missing |
|-------|--------|-------------|----------------|
| **1 — Research Question** | Partial | Implicit hypothesis: RL-guided mutation strategy selection improves CVE discovery over static weighted/uniform sampling. Clear target domain (SQLite fuzzing). | **No formal hypothesis statement.** The Phase 2 ablation *disproved* the intermediate hypothesis ("distilled grammar quality beats vocabulary breadth"). The RL hypothesis is untested. No crisp claim statement suitable for a paper abstract. |
| **2 — Literature/Baseline** | Weak | Nautilus NDSS'19 paper referenced. AFL++ as baseline fork server. Manual comparison to uniform sampling. | **No systematic related work.** Missing comparisons to: AFL++ alone (no grammar), Superion, Grimoire, Squirrel (SQL-aware fuzzer), LMQL, FuzzGPT, ChatFuzz, other RL-fuzz papers (NEUZZ, MTFuzz, FuzzRL). No literature review document. |
| **3 — Experiment Design** | Moderate | E2 ablation (4 variants x 2 seeds x 15 min) with stack_dedup root-cause counting. Fidelity scoring (A3) with regex-based CVE signatures. Coverage capture (A2). | **N=2 per variant (far too low for statistical claims).** No statistical tests. No train/val/test split concept (this is fuzzing, not ML — but the RL agent *is* ML and has no eval protocol). No time budget sweep. Only 1 of 4 target versions tested. 15-min horizon likely too short. No ablation on RL hyperparameters. |
| **4 — Execution & Results** | Moderate | One complete E2 ablation on sqlite-3.31.1 with honest analysis. Fidelity v1/v2 deltas recorded. DQN code complete and integration-tested (dqn_test.rs). | **RL has never been run in a fuzzing campaign** (`rl_enabled: false` in all configs). No RL results whatsoever. No experiment tracking (no wandb/mlflow). No saved seeds (Nautilus has no RNG seed control). Coverage.json sometimes fails extraction. |
| **5 — Writing & Submission** | Early | Good README, architecture doc, ablation report, CVE list. Mermaid diagrams. CLAUDE.md is thorough. | **No paper draft.** No LaTeX. No abstract. No figures/plots. No statistical tables suitable for a paper. The ablation report is honest but reads like internal notes, not a paper section. |

---

## 3. Top 3 Critical Gaps

### Gap 1: The RL component has never been evaluated

The entire thesis title is "Grammar-Based Fuzzer with **RL** for CVE Discovery" but `rl_enabled` has never been set to `true` in a real campaign. The DQN agent compiles and passes a unit test with random data, but there are zero results showing whether it helps, hurts, or is neutral. **This is the core contribution and it is completely untested.** Until you run RL campaigns and compare them to baselines, you have no paper.

### Gap 2: Insufficient statistical rigor (N=2, no significance tests)

The E2 ablation uses 2 runs per variant with no RNG seed control. This is explicitly acknowledged in the report ("should be read as a floor on run-to-run spread, not a true CI") but 2 data points cannot support any statistical claim. For a paper you need at minimum N=10 per variant with Mann-Whitney U or similar non-parametric tests, plus confidence intervals on TTFC and RC counts.

### Gap 3: No paper draft or formal hypothesis

There is no LaTeX document, no abstract, no formal problem statement. The ablation report is intellectually honest but the findings are negative (distilled grammar worse than full library, weights don't matter at 15 min). Without a reframed hypothesis that the RL agent overcomes the static-weight limitation, there is no positive thesis claim to defend.

---

## 4. Proposed Experiment Plan

| # | Experiment | Goal | Baseline | Dataset/Target | Metric | Expected Outcome |
|---|-----------|------|----------|----------------|--------|-----------------|
| **E1** | **RL vs Default** (core experiment) | Test whether DQN-guided mutation selection finds more unique root causes or faster TTFC than default Nautilus | DefaultPolicy (rl_enabled=false) | sqlite-3.31.1, 1-hour runs, N=10 per arm | Unique root causes (RC), TTFC, coverage growth curve, total crashes | RL finds same or +1-2 RC faster, or does not differ (null result — still publishable as empirical finding) |
| **E2** | **RL vs Random Policy** | Disentangle "single-strategy selection" from "learned selection" — does the DQN learn anything or is random action selection equivalent? | UniformRandomPolicy (randomly picks one of 5 strategies each round) | sqlite-3.31.1, 1h, N=10 | RC, TTFC, action distribution over time, Q-value convergence | RL should show action distribution shift and Q-value differentiation; if not, DQN architecture needs rethinking |
| **E3** | **Time budget sweep** | Test whether weighted grammar / RL advantages emerge at longer horizons (15 min was too short for fidelity-to-crash conversion) | patterns_uniform @ 15m, 1h, 4h | sqlite-3.31.1, N=5 per time point | RC ceiling vs wall time curve | Longer budgets should show divergence if weight/RL effects exist |
| **E4** | **Cross-version generalization** | Does the grammar + RL approach transfer across SQLite versions, or is it overfit to 3.31.1? | Same config run on 3.30.1, 3.32.0, 3.32.2 | All 4 CVE versions, 1h, N=5 | RC per version, CVE-specific crash detection | At least 2/4 versions should yield CVE-matching crashes |
| **E5** | **RL hyperparameter sensitivity** | Which hyperparams matter? (epsilon decay, replay size, train interval) | Default DQN config | sqlite-3.31.1, 1h, N=5 per config | RC, loss convergence, action entropy | Identify which hyperparams have measurable impact — needed for reproducibility section |
| **E6** | **Grammar vocabulary ablation** (extend E2) | Add the full `sqlite_generated.py` (42 cve2grammar rules composed with patterns) as a 5th variant | patterns, uniform, attack_v1, attack_v2, generated_composed | sqlite-3.31.1, 1h, N=5 | RC, fidelity, coverage | Generated grammar should match or exceed patterns RC ceiling if vocabulary-is-king holds |

---

## 5. Next 2-Week Action Plan

### Week 1: Make RL runnable + first results

| Day | Task | Deliverable |
|-----|------|-------------|
| **Day 1** | Fix the `rl_enabled: true` pipeline end-to-end. Run a 15-min smoke test with DQN enabled. Verify `rl_metrics.csv` is written and contains sane data. | Smoke test passes, rl_metrics.csv produced |
| **Day 2** | Compose `sqlite_generated.py` + `sqlite_patterns.py` into one self-contained grammar (the "known next step" in CLAUDE.md). Test it loads without "Broken Grammar" panic. | `grammars/sqlite_composed.py` works |
| **Day 3** | Write the `UniformRandomPolicy` (trivial: random strategy each round, no learning) for E2 baseline. Write `scripts/run_rl_ablation.sh` that runs 3 arms: Default, DQN, Random. | New ablation script, 3-arm design |
| **Day 4-5** | Run E1 pilot: 1-hour runs, N=3 per arm (Default, DQN, Random) on sqlite-3.31.1. Analyze rl_metrics.csv: does epsilon decay? Do Q-values differentiate? Any crashes? | First RL results, even if preliminary |

### Week 2: Statistical rigor + paper skeleton

| Day | Task | Deliverable |
|-----|------|-------------|
| **Day 6-7** | Scale E1 to N=10 per arm (can batch overnight). Write analysis script that computes Mann-Whitney U on RC counts and bootstrap CI on TTFC. | `scripts/analyze_rl.py` with statistical tests |
| **Day 8** | Run E4 cross-version: 1h x 3 arms x 4 versions x N=3 (36 runs). This validates generalization. | Cross-version results |
| **Day 9** | Create LaTeX skeleton: title, abstract (with placeholder numbers), intro (problem + hypothesis), related work (list 10 papers to cite), method (3 sections: Nautilus base, grammar design, RL integration), experiments, results, conclusion. | `paper/main.tex` compiles with section stubs |
| **Day 10** | Write the Method section from existing code/docs. Generate coverage growth curves (matplotlib) and RC-count bar charts. Fill in results tables with actual numbers. | Paper method section + 3-4 figures |

### Critical decision point (end of Week 1):

If the DQN agent shows **no learning signal** (Q-values don't differentiate, action distribution stays uniform, no improvement over random), you need to decide:

- **(a)** Reframe as negative result paper ("RL does not help grammar-based fuzzing because...") — still publishable
- **(b)** Redesign the state/reward/action space before scaling experiments
- **(c)** Try a simpler RL approach (multi-armed bandit, UCB) instead of DQN

Do **not** spend 2 weeks scaling experiments on an architecture that shows no learning signal in the pilot.

---

## 6. Honest Assessment

### What's solid

- **Engineering quality is high.** The Rust codebase is well-structured (5.5k LOC across 3 crates), the RL integration is cleanly architected (MutationPolicy trait, DqnPolicy/DefaultPolicy split), the harness/fork-server work correctly, and the triage pipeline (dedup, fidelity scoring, CVE signatures) is thoughtful.
- **The E2 ablation is intellectually honest.** The report openly states that the distilled grammar hypothesis failed and that weights don't matter at 15-min horizon. This kind of honesty is rare and valuable — use it in the paper.
- **The fidelity scoring system is novel.** Regex-based CVE signature matching on generated samples, with per-pattern scoring, is a meaningful contribution to grammar-fuzzing evaluation methodology.

### What's vague or risky

- **The RL contribution is vaporware.** Code exists but has never been evaluated. You cannot submit a paper with "Phase 3: Not started" as the status of your core contribution.
- **Statistical claims are unsupported.** N=2 with no significance tests. The ablation report correctly hedges but a paper requires rigor.
- **The research question is unclear.** Is it "RL improves fuzzing"? "Grammar design matters"? "CVE-aware grammars beat generic ones"? The Phase 2 results suggest the answer to the latter two is "no" at short horizons. You need to decide what the paper is *about*.
- **cve2grammar is half-integrated.** The generated grammar can't run standalone, the composition step is a TODO, and the 42 LLM-generalized rules have never been evaluated as a fuzzing grammar.
- **No comparison to external tools.** Without running Squirrel, AFL++, or at minimum vanilla Nautilus with a generic SQL grammar as baselines, reviewers will ask "why not just use X?"

---

## 7. Codebase Inventory

### Core Components (Rust, 5,577 LOC total)

| Component | Files | LOC | Status |
|-----------|-------|-----|--------|
| `fuzzer/src/main.rs` | 1 | 309 | Production — RL integration wired but untested with `rl_enabled: true` |
| `fuzzer/src/dqn.rs` | 1 | 422 | Complete — DQN with replay buffer, target network, AdamW optimizer via candle |
| `fuzzer/src/rl_hook.rs` | 1 | 122 | Complete — MutationPolicy trait, DqnPolicy, DefaultPolicy |
| `fuzzer/src/rl_logger.rs` | 1 | 141 | Complete — CSV logger for RL metrics (action freq, Q-values, reward, loss) |
| `fuzzer/src/config.rs` | 1 | 88 | Complete — All RL hyperparameters exposed via config.ron |
| `fuzzer/src/dqn_test.rs` | 1 | 82 | Complete — Standalone forward pass + convergence test |
| `grammartec/` | 10 | 2,441 | Production — Grammar engine with weighted sampling |
| `forksrv/` | 4 | 426 | Production — AFL fork server |

### Grammars (Python)

| Grammar | Rules | Status |
|---------|-------|--------|
| `sqlite_patterns.py` | ~99 NTs | Production baseline |
| `sqlite_patterns_uniform.py` | ~99 NTs | Weight-stripped variant |
| `sqlite_attack.py` | ~30 NTs | Distilled attack grammar (v2) |
| `sqlite_generated.py` | 42 rules | NOT self-contained — references 24 undefined NTs |

### Triage Pipeline (Python)

| Module | LOC | Purpose |
|--------|-----|---------|
| `triage/stack_dedup.py` | — | GDB-based stack-frame deduplication |
| `triage/dedup.py` | 147 | ASan frame-hash deduplication |
| `triage/fidelity_score.py` | 119 | Per-pattern structural fidelity scoring |
| `triage/cve_signatures.py` | 92 | Regex-based CVE signature definitions (6 CVEs) |
| `triage/report.py` | 192 | Markdown crash report generator |
| `triage/minimize.py` | — | SQL crash minimization |

### Scripts

| Script | Purpose |
|--------|---------|
| `scripts/run_eval.sh` | Single campaign launcher |
| `scripts/run_ablation.sh` | 4-variant ablation orchestrator |
| `scripts/analyze.py` | TTFC + coverage analysis |
| `scripts/capture_coverage.py` | Coverage extraction from exec.log |

### Experiment Results (on disk)

| Artifact | Location | Content |
|----------|----------|---------|
| E2 ablation report | `docs/attack-grammar-ablation-sqlite-3.31.1.md` | 4 variants x 2 runs, full root-cause breakdown |
| Fidelity v1 baseline | `docs/fidelity-baseline-attack-v1.json` | Pre-B2 fidelity scores |
| Fidelity v2 post-B2 | `docs/fidelity-postB2-attack-v2.json` | Post-B2 fidelity scores (P13435: 18.6%, P19646: 19.1%) |
| Raw run data | `/tmp/nautilus_eval/` (ephemeral) | Not persisted to git |

---

## 8. Key Findings from Existing Experiments

### E2 Ablation Results (sqlite-3.31.1, 15 min, N=2)

| Variant | Total Crashes | Unique Root Causes | Exec/sec |
|---------|--------------|-------------------|----------|
| attack_v1 (distilled, pre-B2) | 185 | 4 | ~230 |
| attack_v2 (distilled, post-B2) | 53 | 2 | ~224 |
| patterns (full library, weighted) | 590 | 6 | ~99 |
| uniform (full library, no weights) | 592 | 6 | ~112 |

### Key takeaways

1. **Vocabulary breadth > distillation quality** at 15-min horizon (patterns/uniform: 6 RC vs attack: 2-4 RC)
2. **Weights do not matter** at this horizon (patterns and uniform find identical RC set)
3. **Fidelity improvements don't convert to crashes** (attack_v2 has 10x better fidelity on P13435 but finds fewer RCs)
4. **Attack grammar is 2x faster** in exec/sec but still finds fewer unique bugs
