# Documentation Cleanup & Standardization — Design Spec

**Date:** 2026-05-05
**Status:** Draft
**Scope:** Restructure, archive, fix, and rewrite the project documentation tree

---

## Problem

The project has 172 markdown files with no master index, 4 duplicates, 1 broken file, heavy overlap between 3 "how the fuzzer works" documents, stale content, and inconsistent git tracking. Finding the right doc requires tribal knowledge.

## Audiences

1. **Thesis advisor / defense committee** — needs system architecture, installation guide, research methodology
2. **Project owner (you)** — needs both big-picture and detail-level operational reference for decision-making across sessions

## Approach: Three-Phase Cleanup

Each phase is independently reviewable and committable.

---

## Phase 1 — File Operations (no content changes)

### Deletions

| File | Reason |
|------|--------|
| `docs/audit/research-audit-EN.md` | Duplicate of `research-audit-en.md` |
| `docs/audit/research-audit-VI.md` | Duplicate of `research-audit-vi.md` |

### Moves

| Source | Destination | Reason |
|--------|-------------|--------|
| `README.md` (root) | `docs/archive/phase1-progress-journal.md` | Archive the 794-line Phase 1 build log (root README) |
| `docs/a1-manual-verification.md` | `docs/experiments/a1-manual-verification.md` | Group with experiments |
| `docs/system-guide.md` | `docs/archive/system-guide-v1.md` | Archive before rewrite |
| `docs/architecture.md` | `docs/archive/architecture-v1.md` | Archive before rewrite |
| `docs/ONBOARDING.md` | `docs/onboarding.md` | Lowercase rename |
| `docs/attack-grammar-pilot-sqlite-3.31.1.md` | `docs/experiments/attack-grammar-pilot-sqlite-3.31.1.md` | Group experiments |
| `docs/attack-grammar-ablation-sqlite-3.31.1.md` | `docs/experiments/attack-grammar-ablation-sqlite-3.31.1.md` | Group experiments |
| `docs/attribution_deep_analysis_15m.md` | `docs/experiments/attribution_deep_analysis_15m.md` | Group experiments |
| `docs/crash-report-patterns-pilot.md` | `docs/experiments/crash-report-patterns-pilot.md` | Group experiments |
| `docs/nautilus-legacy-cve-analyze/` | `reference/legacy-analysis/` | Reference material, not core docs |

### Archive completed plan/spec pairs

Move to `docs/archive/plans/`:

| Plan | Spec | Feature |
|------|------|---------|
| `2026-04-22-attack-pattern-grammar.md` | `2026-04-22-attack-pattern-grammar-design.md` | Grammar v1 |
| `2026-04-22-measurement-and-fidelity.md` | `2026-04-22-measurement-and-fidelity-design.md` | Measurement framework |
| `2026-04-25-component-smoke-tests.md` | `2026-04-25-component-smoke-tests-design.md` | Smoke tests |
| `2026-04-25-deep-component-test.md` | `2026-04-25-deep-component-test-design.md` | Deep component tests |
| `2026-04-27-grammar-v3-structural-primitives.md` | `2026-04-27-grammar-v3-structural-primitives-design.md` | Grammar v3 |
| `2026-04-28-campaign-results-grammar-versioning.md` | `2026-04-28-campaign-results-grammar-versioning-design.md` | Campaign archive system |
| `2026-04-29-oracle-classification.md` | `2026-04-29-oracle-classification-design.md` | Triage classifier |

### Stays in place (in-progress)

- `docs/superpowers/plans/2026-05-02-proportional-reward-bandit.md`
- `docs/superpowers/plans/2026-05-05-thesis-writing.md`
- `docs/superpowers/specs/2026-05-05-thesis-writing-design.md`

### Untouched

- `CLAUDE.md` — AI context, current
- `AGENTS.md` — GitNexus directives, keep
- `docs/feedbacks/mentor-feedback.md` — keep in place
- `docs/audit/*` — keep as timeline (minus deleted duplicates)
- `grammars/CHANGELOG.md` — grammar-specific, keep
- `reference/codebase-walkthrough.md` — thesis defense reference, keep
- `reference/graduate-thesis-policy/` — static, keep
- `cve2grammar/` — self-contained subtree, leave alone
- `results/` — experiment data, keep
- `workdirs/` — campaign outputs, keep

---

## Phase 2 — Fix Existing Content

### 2a. Fix `docs/cve-list.md`

Rebuild the broken 7-line file into the authoritative CVE reference. Content:

- Table: Version | CVE ID | Type | PoC SQL | Affected Range | Fix Version | Harness Status
- All 6 CVEs from the authoritative list
- Source data: `CLAUDE.md` CVE table + `docs/archive/phase1-progress-journal.md` CVE difficulty section

Target: ~80-100 lines.

### 2b. Create new `README.md`

The original 794-line root README is archived in Phase 1. Create a fresh concise project overview. Content:

- Project name + one-paragraph description
- Quick start: prerequisites, build, run first campaign
- Phase status table (Phase 1 complete, Phase 2 complete, Phase 3 not started)
- CVE targets summary (4 versions, 6 CVEs)
- Key results (TTFC ~1-2s, uniform > bandit on crash diversity)
- Links to `docs/` for detailed documentation

Target: ~100-150 lines.

### 2c. Create `CHANGELOG.md`

New file at project root. Per-feature entries organized by date, covering the full project lifetime:

- Format: `## [YYYY-MM-DD] Section header` with bulleted entries
- Categories: Grammar, Harness, Fuzzer Core, Triage, Scripts, RL Infrastructure
- Covers: grammar v1→v3.x, harness builds for 4 versions, triage pipeline, bandit integration, campaign results
- Source data: git log, `grammars/CHANGELOG.md`, archived plans, `CLAUDE.md` phase status

Target: ~100-150 lines.

### 2d. Create `docs/README.md` (docs index)

Master table of contents for the documentation tree. Content:

```markdown
# Documentation

## Core
| Document | Description |
|----------|-------------|
| [architecture.md](architecture.md) | System design, component diagrams, data flow |
| [workflow-deep-dive.md](workflow-deep-dive.md) | Fuzzer internals, execution loop, config reference |
| [onboarding.md](onboarding.md) | Build, install, run your first campaign |
| [cve-list.md](cve-list.md) | CVE targets with PoC SQL and harness status |

## Experiments
| Document | Description |
|----------|-------------|
| ... | ... |

## Audits
| Document | Description |
|----------|-------------|
| ... | ... |

## Reference
| Document | Description |
|----------|-------------|
| ... | ... |

## Archive
| Document | Description |
|----------|-------------|
| ... | ... |
```

Target: ~60-80 lines.

---

## Phase 3 — Rewrite from Scratch

### 3a. `docs/architecture.md` — System Design

Audience: both (thesis committee + project owner).
Target: ~400-500 lines.

Sections:
1. **System Overview** — Mermaid diagram of the full pipeline: grammar → fuzzer → harness → triage
2. **Component Map** — table of components (fuzzer, grammartec, forksrv, harness, triage, cve2grammar) with language, LoC, purpose
3. **Data Flow** — how a SQL input is generated, mutated, executed, and classified
4. **Coverage Feedback Loop** — Mermaid diagram showing bitmap → new_bits → queue → mutation cycle
5. **Grammar Weight System** — loaded_dice, weighted sampling, ctx.rule() DSL, PyO3 bridge
6. **Build Architecture** — Cargo workspace structure, AFL instrumentation, harness compilation
7. **CVE-to-Grammar Pipeline** — tree-sitter → pattern_generalizer → grammar rules

Source material: archived `architecture-v1.md`, `system-guide-v1.md`, current codebase (read Rust/Python sources directly for accuracy).

### 3b. `docs/workflow-deep-dive.md` — Fuzzer Internals

Audience: project owner (operational reference).
Target: ~500-600 lines.

Sections:
1. **Campaign Lifecycle** — `run_eval.sh` → config.ron → fuzzer binary → workdir → triage → results
2. **Execution Loop** — step-by-step: generate → mutate → fork → classify → queue
3. **Exit Code Classification** — table: ExitReason → is_crash → action → output path
4. **Coverage Bitmap** — bitmap size, new_bits detection, dual bitmap (crash/clean)
5. **Deterministic Validation** — 5x re-run filter for non-deterministic coverage
6. **Mutation Strategies** — Havoc/HavocRec/Min/MinRec/Splice/Det/Gen with attribution counters
7. **Input Deduplication** — ring buffer (10k), HashSet lookup
8. **Queue Management** — QueueItem lifecycle, bit_to_inputs reverse index
9. **Grammar Bandit** — UCB1 selection, EMA reward, observe_reward flow
10. **Configuration Reference** — table of all config.ron parameters with types, defaults, purpose

Source material: archived `system-guide-v1.md`, `phase1-progress-journal.md` fuzzer deep dive section, current Rust sources (`fuzzer/src/*.rs`, `forksrv/src/lib.rs`, `grammartec/src/*.rs`).

---

## Target File Tree (final state)

```
rl-nautilus-phase-2/
├── README.md                                    # Rewritten — concise overview
├── CHANGELOG.md                                 # NEW — project changelog
├── CLAUDE.md                                    # Unchanged
├── AGENTS.md                                    # Unchanged
│
├── docs/
│   ├── README.md                                # NEW — docs index
│   ├── architecture.md                          # REWRITTEN — system design
│   ├── workflow-deep-dive.md                    # REWRITTEN — fuzzer internals
│   ├── onboarding.md                            # MOVED from ONBOARDING.md
│   ├── cve-list.md                              # FIXED — complete CVE table
│   │
│   ├── experiments/                             # NEW subdir
│   │   ├── a1-manual-verification.md
│   │   ├── attack-grammar-pilot-sqlite-3.31.1.md
│   │   ├── attack-grammar-ablation-sqlite-3.31.1.md
│   │   ├── attribution_deep_analysis_15m.md
│   │   └── crash-report-patterns-pilot.md
│   │
│   ├── audit/                                   # Cleaned (duplicates removed)
│   │   ├── research-audit-en.md
│   │   ├── research-audit-vi.md
│   │   ├── grammar-strategy-landscape.md
│   │   ├── input-journey-paper-vs-code.md
│   │   ├── 2026-04-30-comprehensive-audit.md
│   │   └── thesis-completeness-checklist.md
│   │
│   ├── feedbacks/
│   │   └── mentor-feedback.md
│   │
│   ├── archive/
│   │   ├── phase1-progress-journal.md
│   │   ├── system-guide-v1.md
│   │   ├── architecture-v1.md
│   │   └── plans/
│   │       └── (14 archived plan/spec files)
│   │
│   └── superpowers/
│       ├── plans/   (only in-progress)
│       └── specs/   (only in-progress + this spec)
│
├── reference/
│   ├── codebase-walkthrough.md
│   ├── graduate-thesis-policy/
│   └── legacy-analysis/
│       ├── mruby-analyze/
│       └── php-analyze/
│
├── grammars/
│   └── CHANGELOG.md
├── results/
├── workdirs/
└── cve2grammar/                                 # Self-contained, untouched
```

## Commit Strategy

- **Phase 1 commit:** `docs: reorganize documentation tree (move/archive/delete)`
- **Phase 2 commit:** `docs: fix cve-list, rewrite README, create CHANGELOG and docs index`
- **Phase 3 commit:** `docs: rewrite architecture.md and workflow-deep-dive.md from scratch`

## Out of Scope

- `cve2grammar/` internal docs — self-contained subtree
- `results/` and `workdirs/` content — auto-generated campaign data
- `.claude/skills/` — tooling config, not project docs
- Thesis LaTeX content — separate plan (`2026-05-05-thesis-writing.md`)
- `CLAUDE.md` content updates — will naturally follow once docs stabilize
