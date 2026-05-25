# Defense Demo — Feature List

## 1. Grammar Engine (grammartec/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Grammar loading via PyO3 | `./target/release/generator -g grammars/active/sqlite_v3.py -t 10` | Python DSL → Rust rules via PyO3 bridge |
| Weighted sampling | Run generator 100x, count high-weight vs low-weight patterns | `weight=3.0` rules appear ~3x more than `weight=1.0` |
| Tree generation | `./target/release/generator -g grammars/active/sqlite_v3.py -t 5 -s` | Generates corpus/ folder with SQL files |
| Rule types | Open `grammars/active/sqlite_v3.py` | Plain rules, regex rules, weighted rules |

## 2. Fuzzer Core (fuzzer/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Full fuzzing campaign (default grammar) | `DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` | 60s campaign with active/sqlite_v3.py (default) |
| Campaign with specific grammar | `GRAMMAR=grammars/active/sqlite_v3_uniform.py DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo_uniform` | Run with uniform grammar (no CVE seeds) |
| Campaign with EBNF baseline | `GRAMMAR=grammars/baseline/sqlite-ebnf.py DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo_ebnf` | Run with EBNF-Baseline for comparison |
| Config system | `cat workdirs/sqlite-3.31.1_demo/config.ron` | RON config: threads, timeout, bitmap size, grammar path |
| Execution logging | `head -20 workdirs/sqlite-3.31.1_demo/exec.log` | Per-execution: strategy, new_bits, exit_reason |
| Multi-threaded mode | `THREADS=2 DURATION=30 ./scripts/run_eval.sh sqlite-3.31.1 mt_demo` | Shared bitmap, thread-safe queue |
| Smoke test suite | `./scripts/smoke_test.sh` | 11 component tests in ~90s |

## 3. Harness (harness/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Single SQL execution | `./harness/afl/sqlite_harness_sqlite-3.31.1 input.sql` | Fork-server mode, ASan+UBSan oracle |
| Crash reproduction | `cd results/crashes/BC003_.../1ca1c0159b42ae50 && ./reproduce.sh` | Trigger SQL → ASan output |
| Multi-version builds | `ls harness/afl/` | 4 CVE-bearing versions built |
| Build a harness | `cd harness/src && make SQLITE=../../cve_builds/sqlite-3.31.1/sqlite3.c TARGET=sqlite_harness_sqlite-3.31.1` | AFL instrumentation + sanitizers |

## 4. Triage Pipeline (triage/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Crash collection | `python3 scripts/collect_crashes.py --scan-only` | Scans all campaigns, dedup by stack hash |
| CVE signature matching | `python3 -c "from triage.cve_signatures import _CVES; print(_CVES)"` | 6 CVE patterns as regex lists |
| Bug class registry | `cat results/crashes/registry.md` | 13 bug classes, 48 unique stack hashes |

## 5. Evaluation Pipeline (scripts/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Single campaign | `DURATION=120 ./scripts/run_eval.sh sqlite-3.31.1 demo_run` | End-to-end: config → fuzz → triage |
| Statistics | `python3 scripts/ch4_pipeline.py` | Mann-Whitney U test, Cliff's d effect size |
| Figure generation | `python3 scripts/generate_figures.py` | Matplotlib plots for thesis |

## 6. Grammar Design (grammars/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Active grammar (v3.4) | `head -50 grammars/active/sqlite_v3.py` | CVE seed rules, weighted dispatch |
| Uniform grammar (v3.3) | `diff grammars/active/sqlite_v3.py grammars/active/sqlite_v3_uniform.py \| head -30` | Same structure, no CVE seeds |
| EBNF baseline | `head -50 grammars/baseline/sqlite-ebnf.py` | Spec-derived, no attack patterns |

## 7. Key Results (can show from results/)

| Result | Evidence |
|--------|----------|
| 4/4 CVEs rediscovered | `results/ch4_final/rq1_cve_hits.csv` |
| 13 bug classes found | `results/crashes/registry.md` |
| TTFC ~1-2 seconds | `results/ch4_final/rq1_ttfc_per_cve.csv` |
| 108x more root causes vs baseline | `results/ch4_final/rq3_summary.csv` |
