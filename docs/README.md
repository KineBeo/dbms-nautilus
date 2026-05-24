# Documentation

## Core (thesis-aligned)

| Document | Description |
|----------|-------------|
| [System Architecture](core/architecture.md) | System overview, component map, 5-layer pipeline diagram |
| [Grammar Engine](core/grammar-engine.md) | Weight system, PyO3 bridge, rule selection, grammar DSL |
| [Coverage & Mutation Loop](core/coverage-loop.md) | Bitmap feedback, queue management, mutation strategies |
| [Triage Pipeline](core/triage-pipeline.md) | Crash classification, dedup, CVE signatures, fidelity scoring |
| [Build & Run](core/build-and-run.md) | Build prereqs, harness compilation, campaign commands, config reference |

## Extensions

| Document | Description |
|----------|-------------|
| [Grammar Bandit (Thompson Sampling)](extensions/bandit.md) | Runtime grammar weight adaptation via Thompson Sampling |
| [DQN Agent (archived)](extensions/dqn-archived.md) | DQN mutation policy design (code removed 2026-05-14) |

## Experiments

| Document | Description |
|----------|-------------|
| [experiments/a1-manual-verification.md](experiments/a1-manual-verification.md) | Stack-dedup manual verification on sqlite-3.31.1 |
| [experiments/attack-grammar-pilot-sqlite-3.31.1.md](experiments/attack-grammar-pilot-sqlite-3.31.1.md) | Pilot eval: 219 crashes in 5 min on CVE-2020-13434 |
| [experiments/attack-grammar-ablation-sqlite-3.31.1.md](experiments/attack-grammar-ablation-sqlite-3.31.1.md) | E2 ablation: attack vs patterns vs uniform grammar |
| [experiments/attribution_deep_analysis_15m.md](experiments/attribution_deep_analysis_15m.md) | Signal type analysis (SIGNAL(5) vs SIGNAL(6)) |
| [experiments/crash-report-patterns-pilot.md](experiments/crash-report-patterns-pilot.md) | Crash pattern analysis from pilot campaigns |

## Audits

| Document | Description |
|----------|-------------|
| [audit/research-audit-en.md](audit/research-audit-en.md) | Research gap analysis (English) |
| [audit/research-audit-vi.md](audit/research-audit-vi.md) | Research gap analysis (Vietnamese) |
| [audit/grammar-strategy-landscape.md](audit/grammar-strategy-landscape.md) | Grammar mutation strategy inventory |
| [audit/input-journey-paper-vs-code.md](audit/input-journey-paper-vs-code.md) | Paper vs implementation flow mapping |
| [audit/2026-04-30-comprehensive-audit.md](audit/2026-04-30-comprehensive-audit.md) | Multi-expert comprehensive audit |
| [audit/thesis-completeness-checklist.md](audit/thesis-completeness-checklist.md) | Thesis readiness scorecard |

## Feedback

| Document | Description |
|----------|-------------|
| [feedbacks/mentor-feedback.md](feedbacks/mentor-feedback.md) | Thesis advisor feedback notes |

## Reference

| Document | Description |
|----------|-------------|
| [../reference/codebase-walkthrough.md](../reference/codebase-walkthrough.md) | Component-by-component thesis defense walkthrough |
| [../reference/graduate-thesis-policy/policy.md](../reference/graduate-thesis-policy/policy.md) | UET graduation requirements |

## Archive

| Document | Description |
|----------|-------------|
| [archive/phase1-progress-journal.md](archive/phase1-progress-journal.md) | Phase 1 weekly build log |
| [archive/system-guide-v1.md](archive/system-guide-v1.md) | System guide v1 (11-chapter fuzzing pedagogy) |
| [archive/architecture-v1.md](archive/architecture-v1.md) | Architecture v1 |
| [archive/architecture-v2.md](archive/architecture-v2.md) | Architecture v2 (pre-reorganization, DQN included) |
| [archive/plans/](archive/plans/) | 14 completed plan/spec pairs (Apr 22 — Apr 29) |
