# Quick Reference Card — Defense Demo

## Commands You'll Need

| Action | Command |
|--------|---------|
| Generate SQL | `./target/release/generator -g grammars/active/sqlite_v3.py -t 10` |
| Run 60s campaign | `DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` |
| Run smoke tests | `./scripts/smoke_test.sh` |
| Reproduce crash | `cd results/crashes/BC003_.../1ca1c0159b42ae50 && ./reproduce.sh` |
| Build fuzzer | `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release` |
| Build all harnesses | `cd harness/src && make build-all` |
| Build one harness | `cd harness/src && make SQLITE=../../cve_builds/sqlite-3.31.1/sqlite3.c TARGET=sqlite_harness_sqlite-3.31.1` |
| Change timeout | `TIMEOUT_MS=1000 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` |
| Change threads | `THREADS=2 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` |
| Change tree size | `MAX_TREE_SIZE=500 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` |
| Count crash hashes | `find results/crashes -mindepth 2 -maxdepth 2 -type d \| wc -l` |
| Run full evaluation | `python3 scripts/ch4_pipeline.py` |
| Generate figures | `python3 scripts/generate_figures.py` |

## Key Numbers (from thesis Chapter 4)

| Metric | Value |
|--------|-------|
| CVEs rediscovered | 4/4 (100%) |
| Bug classes found | 13 (9 unique to DBMS-Nautilus, 4 shared with EBNF-Baseline) |
| Unique stack hashes | 48 (after cross-campaign dedup) |
| TTFC | ~1-2 seconds (no significant difference between grammars) |
| Root cause advantage | 108x (mean 205.6 vs 1.9 per campaign) |
| Throughput cost | 52.1% lower (90.8 vs 189.9 exec/s) |
| Edge coverage gap | 14.1% lower (20,182 vs 23,490 edges) |
| Grammar rules | 520 structural + 6 CVE seeds = 526 total |
| Total Rust LoC | ~6,200 across 3 crates |
| Total campaigns | 79 (20 RQ1 + 20 RQ2 + 39 RQ3) |
| Campaign duration | 15 min (900s) each |
| Statistical test | Mann-Whitney U, Cliff's d effect size |

## File Locations

| What | Where |
|------|-------|
| Fuzzer entry | `fuzzer/src/main.rs:233` (main), `:87` (fuzzing_thread), `:46` (process_input) |
| Execution loop | `fuzzer/src/fuzzer.rs:170` (run_on_with_dedup), `:453` (new_bits) |
| Config struct | `fuzzer/src/config.rs:9` |
| Queue pipeline | `fuzzer/src/queue.rs:56` (Init->Det->Random) |
| Shared state | `fuzzer/src/shared_state.rs:7` (GlobalSharedState) |
| Grammar engine | `grammartec/src/context.rs:393` (generate_tree_from_nt) |
| Rule sampling | `grammartec/src/context.rs:264` (get_random_rule_for_nt, O(n) linear scan) |
| Rule types | `grammartec/src/rule.rs:84` (Rule enum: Plain/Script/RegExp, weight field) |
| Mutations | `grammartec/src/mutator.rs:177` (mut_random), `:136` (mut_splice), `:103` (mut_rules), `:32` (minimize_tree) |
| Tree to SQL | `grammartec/src/tree.rs:167` (unparse) |
| ChunkStore | `grammartec/src/chunkstore.rs:51` (add_tree, stores subtrees <=30 nodes) |
| Fork server | `forksrv/src/lib.rs:192` (ForkServer::run) |
| ExitReason | `forksrv/src/exitreason.rs:7` (Normal/Timeouted/Signaled/Stopped) |
| Harness | `harness/src/sqlite_harness.c:68` (main), `:38` (setup_db) |
| PyO3 bridge | `fuzzer/src/python_grammar_loader.rs:10` (PyContext), `:28` (rule method) |
| Bandit (NOT thesis) | `fuzzer/src/grammar_bandit.rs:166` (select_group) -- experimental, unused |
| Grammar (active) | `grammars/active/sqlite_v3.py` (520+6 rules, weighted) |
| Grammar (uniform) | `grammars/active/sqlite_v3_uniform.py` (520 rules, no seeds) |
| Grammar (baseline) | `grammars/baseline/sqlite-ebnf.py` (EBNF-derived) |
| CVE signatures | `triage/cve_signatures.py:15` (_CVES list), `:85` (missing_patterns) |
| Stack dedup | `triage/stack_dedup.py:56` (hash_frames, GDB bt 5) |
| Crash classify | `triage/classify.py` (classify_crash, build_clusters) |
| Config template | `scripts/run_eval.sh:74` (config.ron generation) |
| Crash evidence | `results/crashes/BC*/` (trigger.sql, stderr.log, reproduce.sh) |
| Thesis data | `results/ch4_final/` (CSVs for all RQs) |

## 5 Mutation Operators (thesis Section 3.1)

1. **mut_rules** (line 103) -- deterministic: try every alternative production at each node
2. **mut_random** (line 177) -- random subtree regeneration (havoc)
3. **mut_random_recursion** (line 197) -- repeat recursive productions for deeper nesting
4. **mut_splice** (line 136) -- replace with same-type subtree from ChunkStore
5. **bulk random havoc** -- multiple random subtree replacements in succession

Minimization (minimize_tree line 32, minimize_rec line 72) is preprocessing, not a mutation.

## Dangerous Topics (handle carefully)

| Topic | What to say |
|-------|-------------|
| Thompson Sampling / bandit | "Experimental code for future work. All thesis experiments use fixed weights." |
| DQN / reinforcement learning | "Explored as future direction. Code was removed. Thesis conclusion mentions it." |
| Why only SQLite? | "Chosen for popularity, CVE diversity, and reproducibility. Cross-DBMS is future work." |
| Why only 15 min campaigns? | "Standard in fuzzing literature. Longer campaigns show diminishing returns in coverage-guided fuzzing." |
| Why N=5 runs? | "Balance between statistical power and compute budget. Mann-Whitney U is appropriate for small samples." |
