# Grammar Strategy Landscape: RL-Nautilus

**Date:** 2026-04-24
**Scope:** Comprehensive inventory of current grammar strategies, mutation strategies, and learnable ideas from external grammar fuzzers
**Sources:** GitNexus codebase scan + WebSearch across Nautilus, Superion, Gramatron, Grimoire, Squirrel, Griffin, G2Fuzz, ParserFuzz, EcoFuzz, AFL-RL, FuzzySQL, T-Scheduler

---

## 1. Current Grammar Strategy Arsenal

### A. Mutation Strategies (5 actions the DQN selects from)

| # | Strategy | Code location | What it does | Iterations/call |
|---|----------|--------------|--------------|----------------|
| 0 | **Havoc** | `state.rs:131` -> `mutator.rs:177 (mut_random)` | Pick random node, regenerate its subtree from same non-terminal | 100 |
| 1 | **HavocRec** | `state.rs:145` -> `mutator.rs:197 (mut_random_recursion)` | Find recursive structure in tree, replicate it N times (depth explosion) | 20 |
| 2 | **Splice** | `state.rs:167` -> `mutator.rs:136 (mut_splice)` | Pick random node, replace with same-typed subtree from ChunkStore (cross-pollination from queue) | 100 |
| 3 | **Det** | `state.rs:109` -> `mutator.rs:103 (mut_rules)` | For each node, try every alternative rule for that non-terminal (exhaustive) | All alternatives |
| 4 | **Generate** | `state.rs:191` | Generate completely fresh tree from START | 1 |

### B. Grammar-Level Strategies (how grammars are designed)

| Strategy | Grammar file | Description |
|----------|-------------|-------------|
| **Weighted sampling** | `sqlite_patterns.py` | `loaded_dice` O(1) sampling -- Layer 2 stress patterns get 2.0-3.5x weight vs 0.2-1.0 for base SQL |
| **Uniform sampling** | `sqlite_patterns_uniform.py` | Same vocabulary, all weights stripped to 1.0 |
| **Distilled attack** | `sqlite_attack.py` | Minimal vocabulary (~30 NTs), one canonical form per CVE pattern, no weights |
| **LLM-generated** | `sqlite_generated.py` | 42 crash-oracle rules from cve2grammar, NOT self-contained (broken) |

### C. What's NOT implemented but the code has hooks for

| Feature | Status | Where |
|---------|--------|-------|
| **RL weight tuning** | Comment only | `sqlite_patterns.py:21-22` mentions `ctx.set_weight()` / `ctx.get_weights_for_nt()` but these APIs don't exist in `context.rs` |
| **Script rules** | API exists | `context.rs:83 (add_script)` -- Python callbacks for non-CFG rules, unused in current grammars |
| **Regex terminals** | API exists | `context.rs:100 (add_regex)` -- regex-based terminal generation, unused |

---

## 2. What Other Grammar Fuzzers Do (That We Don't)

### D. Tree-Level Mutation Strategies We're Missing

| Strategy | Used by | Idea | Difficulty |
|----------|---------|------|-----------|
| **Subtree crossover** | Superion, Gramatron | Take two trees from queue, swap compatible subtrees (like genetic crossover) | Medium -- Splice is similar but only pulls from ChunkStore, not paired from queue |
| **Grammar-aware trimming** | Superion | Systematically prune subtrees to find minimal triggering input at tree level | Low -- we have `minimize_tree` but it's only used in Init stage, not as an ongoing strategy |
| **Walk-based splice** | Gramatron | Replace not just a subtree but the entire suffix (everything right of splice point) -- explores more radically different structures | Medium |
| **Subtree deletion** | Multiple | Simply delete optional subtrees (WHERE clause, ORDER BY, etc.) | Low |
| **Subtree duplication** | Multiple | Clone a subtree to a sibling position | Low |

### E. Semantic-Aware Strategies We're Missing

| Strategy | Used by | Idea | Difficulty |
|----------|---------|------|-----------|
| **Data dependency analysis** | Squirrel | Ensure generated SQL references existing tables/columns -- semantic correctness | High -- requires runtime schema tracking |
| **Type-aware mutation** | Squirrel | Only substitute values/expressions of compatible SQL types | Medium |
| **Semantic feedback** | Recent LLM-hybrid fuzzers | Track not just coverage but program state changes, exception types, output semantics | High |
| **Logic-shifting mutation** | FuzzySQL (2025) | Negate conditions, restructure execution logic to explore alternative control paths | Medium |

### F. Grammar Evolution Strategies We're Missing

| Strategy | Used by | Idea | Difficulty |
|----------|---------|------|-----------|
| **Coverage-guided rule traversal** | ParserFuzz (2025) | Track which grammar rules have been exercised; prioritize unexplored rules | Medium -- need per-rule coverage bitmap |
| **On-demand grammar expansion** | G2Fuzz | When coverage plateaus, use LLM to generate new grammar rules/features | Medium -- already have cve2grammar pipeline |
| **Rare-feature directed mutation** | G2Fuzz | Track which grammar features appear rarely in queue; bias toward them | Low -- can be done with rule-usage counters |
| **Grammar automaton** | Gramatron | Pre-compile grammar into automaton for unbiased sampling (eliminates context-free bias) | High -- fundamentally different architecture |

### G. RL/Scheduling Strategies We're Missing

| Strategy | Used by | Idea | Our current approach |
|----------|---------|------|-----------------------|
| **Multi-armed bandit (MAB)** | EcoFuzz, AFL-Hier | UCB1/Thompson sampling for mutation operator selection -- simpler than DQN, proven effective | We use DQN which is heavier; MAB might outperform for 5 actions |
| **Power scheduling** | AFL++, EcoFuzz | Allocate more mutation budget to seeds that discovered new coverage | Our queue is FIFO, no energy scheduling |
| **Seed scheduling** | T-Scheduler | MAB over seeds in queue -- which seed to mutate next | Not implemented -- queue.pop() is round-robin |
| **Hierarchical RL** | Research | Two-level: macro selects strategy, micro selects parameters within strategy | We have single-level (strategy only) |
| **Reward shaping** | Multiple | More nuanced reward than coverage_delta + crash bonus -- e.g., rare edge bonus, coverage velocity | Our reward is simple (`dqn.rs:85-97`) |

---

## 3. The Big Picture: 27 Possible Things We Could Do With Our Grammar

### Category 1: Quick wins with current architecture (days)

1. Enable RL and run it (`rl_enabled: true`)
2. Add MAB baseline (UCB1 over 5 strategies)
3. Add subtree deletion mutation
4. Add subtree duplication mutation
5. Compose `sqlite_generated.py` into self-contained grammar
6. Track per-rule usage frequency (which grammar rules fire)
7. Seed energy scheduling (prioritize seeds that found new coverage)

### Category 2: Medium effort, high potential (1-2 weeks)

8. Subtree crossover from two queue items
9. Coverage-guided rule prioritization
10. Rare-feature directed sampling
11. Grammar-aware trimming as ongoing strategy
12. Walk-based (suffix) splice
13. Hierarchical RL (macro strategy + micro parameters)
14. Richer reward shaping (rare edge bonus, coverage velocity)
15. Runtime weight adjustment API (`ctx.set_weight()`)

### Category 3: High effort, novel contribution (weeks-months)

16. Semantic-aware data dependency (Squirrel-style)
17. On-demand LLM grammar expansion
18. Logic-shifting mutation
19. Grammar automaton (Gramatron-style)
20. Type-aware SQL mutation
21. Semantic feedback signals (beyond coverage)

---

## 4. Three Natural Thesis Directions

### Direction A: RL-focused

Stay with the DQN but add MAB comparison, power scheduling, and richer reward shaping. This makes the paper about "does RL help mutation selection in grammar fuzzing?" with proper baselines.

**Involves:** Items 1, 2, 7, 13, 14

### Direction B: Grammar evolution

Add runtime weight tuning, coverage-guided rule prioritization, rare-feature sampling, and compose the generated grammar. This makes the paper about "adaptive grammar strategies for CVE discovery."

**Involves:** Items 5, 6, 9, 10, 15

### Direction C: Hybrid

Pick 2-3 quick wins from Category 1 + one medium from Category 2, run them all as ablation variants. This gives the broadest experiment table for the paper.

**Involves:** Items 1, 2, 5, 6 + one of {8, 9, 10}

---

## 5. Sources

- [Gramatron: Effective Grammar-Aware Fuzzing (ISSTA 2021)](https://www.nebelwelt.net/files/21ISSTA.pdf)
- [Superion: Grammar-Aware Greybox Fuzzing (ICSE 2019)](https://arxiv.org/abs/1812.01197)
- [G2Fuzz: LLM-Enhanced Grammar-Aware Fuzzing](https://arxiv.org/html/2501.19282v1)
- [Squirrel: Testing DBMS with Language Validity](https://huhong789.github.io/papers/zhong:squirrel.pdf)
- [ParserFuzz: Coverage-Guided Grammar-Rule Traversal (2025)](https://arxiv.org/html/2503.03893)
- [EcoFuzz: Adaptive Energy-Saving via Multi-Armed Bandit](https://dl.acm.org/doi/10.5555/3489212.3489342)
- [AFL-RL: RL-Based Mutation Scheduling](https://dl.acm.org/doi/fullHtml/10.1145/3606043.3606050)
- [FuzzySQL: LLM-Driven DBMS Fuzzing (2026)](https://arxiv.org/html/2602.19490)
- [Griffin: Grammar-Free DBMS Fuzzing](https://dl.acm.org/doi/fullHtml/10.1145/3551349.3560431)
- [Fuzzing With Optimized Grammar-Aware Mutation Strategies](https://scispace.com/pdf/fuzzing-with-optimized-grammar-aware-mutation-strategies-59h8runcnp.pdf)
- [T-Scheduler: MAB-Based Seed Scheduling](https://arxiv.org/html/2312.04749v1)
- [Hybrid Fuzzing with LLM-Guided Input Mutation](https://arxiv.org/html/2511.03995v1)
