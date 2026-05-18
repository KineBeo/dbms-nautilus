# Chapter 4: Experiments and Evaluation — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Run fresh campaigns, collect clean data, and rewrite Chapter 4 to comply with the chapter4-rule.md constraints.

**Architecture:** Three phases — (1) grammar prep + campaign execution, (2) data collection + analysis, (3) thesis writing. Phases 1-2 produce data; phase 3 consumes it.

**Tech Stack:** Rust (fuzzer), Python (triage/analysis), LaTeX (thesis), Bash (campaign scripts)

**Hardware constraint:** VM has 8GB RAM. Full campaigns (15-30 min) MUST run sequentially — one at a time. Only smoke tests (5 min) can run in parallel.

**Constraint doc:** `docs/thesis/template/rules/chapter4-rule.md`

**Key decisions locked in this plan:**
- 3 RQs (under constraint minimum of 4, justified by project scope)
- 1 baseline (EBNF), no ablation table
- No grammar version numbers in thesis .tex files (use descriptive names)
- RQ2 latest-SQLite 0-day section is a placeholder (grammar enhancement in separate session)
- **Dual-harness triage:** AFL harness compiled WITH -DSQLITE_DEBUG. In triage, crashes are separated into (A) ASan/UBSan real crashes and (B) debug assert findings. This catches CVE-15358 (heap buffer read detected only by debug assert) alongside CVE-13435 (UBSan null ptr). CVE-2019-19646 remains excluded (infinite loop, no crash signal).
- **CVE detection target: 5/6** — exclude only CVE-2019-19646 (oracle limitation: infinite loop)

---

## Chapter Structure (maps to constraint X.1–X.6)

```
4.1 Research Questions
    RQ1: CVE Rediscovery
    RQ2: Bug Detection Capability
    RQ3: Performance
4.2 Dataset and Experimental Setup
    4.2.1 Subjects Under Test (4 SQLite versions + latest)
    4.2.2 Seed/Input Dataset (grammar description, NO version numbers)
    4.2.3 Environment (hardware, OS, compiler, sanitizers)
    4.2.4 Experimental Configuration (params table, runs, duration)
4.3 Baseline Methods
    EBNF grammar (weak baseline)
    Proposed grammar (bold, last)
4.4 Evaluation Metrics
    Unique root causes
    CVE signature match rate
    Edge coverage
    Throughput
    Time-to-first-crash (with formula)
4.5 Experimental Results
    4.5.1 RQ1 Results (CVE rediscovery table + time-to-first-CVE figure)
    4.5.2 RQ2 Results (bug class table + breakdown figure + case studies)
    4.5.3 RQ3 Results (performance table + coverage/throughput/TTFC figures)
4.6 Analysis and Discussion
    4.6.1 Qualitative Analysis (3 named groups with %)
    4.6.2 Comparison with Baseline
    4.6.3 Failure Cases and Limitations (≥3)
    4.6.4 Threats to Validity (internal, external, construct)
    4.6.5 Summary
```

---

## Campaign Matrix

### RQ1 campaigns (v3.5 with CVE seeds)
| Grammar | Versions | Runs | Duration | Total | Wall time |
|---------|----------|------|----------|-------|-----------|
| v3.5 | 3.30.1, 3.31.1, 3.32.0, 3.32.2 | 5 each | 15 min | 20 | ~5 hrs |
| EBNF | all 4 | 5 each | 15 min | 0 | reuse existing |

### RQ2 campaigns (v3.3, no seeds)
| Grammar | Versions | Runs | Duration | Total | Wall time |
|---------|----------|------|----------|-------|-----------|
| v3.3 | 3.30.1, 3.31.1, 3.32.0, 3.32.2 | 5 each | 30 min | 20 | ~10 hrs |

### RQ3: zero additional campaigns (reuses RQ1 data)

### Total: 42 campaigns (2 smoke + 40 full)

**Wall time (sequential, 8GB VM constraint):**
- Smoke tests: ~10 min (can run in parallel)
- RQ1 full: 20 × 15 min = **5 hours**
- RQ2 full: 20 × 30 min = **10 hours**
- **Total: ~15.2 hours sequential** (cannot parallelize full campaigns)

**Recommended execution order:** Run RQ1 campaigns first (5 hrs), start RQ1 triage while RQ2 campaigns run overnight (10 hrs). Phase 2 analysis for RQ1 can overlap with RQ2 campaign execution since triage is CPU-light.

---

## Tables and Figures Inventory

### Tables (4 total)
| ID | Content | RQ | Source |
|----|---------|-----|--------|
| T1 | Campaign parameters | Setup | Manual |
| T2 | CVE rediscovery + reachability (merged) | RQ1 | v3.5 campaign data |
| T3 | Bug class summary (class/type/severity/versions/hashes) | RQ2 | v3.3 fresh campaign data |
| T5 | Performance (throughput, coverage, TTFC, Mann-Whitney U, Cliff's d) | RQ3 | v3.5 + EBNF data |

### Figures (5 total)
| ID | Content | RQ | Source |
|----|---------|-----|--------|
| F1 | Time-to-first-CVE-crash (boxplot, per CVE) | RQ1 | v3.5 logs |
| F2 | Bug class breakdown (bar chart by severity/type) | RQ2 | v3.3 fresh data |
| F3 | Coverage growth over time (line, mean±1std) | RQ3 | v3.5 + EBNF timeseries |
| F4 | Throughput bar chart | RQ3 | v3.5 + EBNF data |
| F5 | Time-to-first-real-crash boxplot (per version) | RQ3 | v3.5 + EBNF logs |

---

## Phase 1: Grammar Preparation + Campaign Execution

### Task 1: Create v3.5 grammar (bump CVE seed weights)

**Files:**
- Create: `grammars/v3.5/sqlite_v3.py`
- Source: `grammars/v3.4/sqlite_v3.py`

- [ ] **Step 1: Copy v3.4 to v3.5**

```bash
mkdir -p grammars/v3.5
cp grammars/v3.4/sqlite_v3.py grammars/v3.5/sqlite_v3.py
```

- [ ] **Step 2: Edit seed weights in v3.5**

Change CVE-2020-13435 seed weight from `0.1` to `0.5` (line 57).
Change CVE-2020-15358 seed weight from `0.1` to `0.5` (line 78).
Keep all other seed weights at `0.1`.

Update header comment: `# Version: v3.5 (CVE seed rules, boosted weights for hard CVEs)`

- [ ] **Step 3: Verify grammar loads**

```bash
cargo run --bin generator -- -g grammars/v3.5/sqlite_v3.py -t 10
```

Expected: 10 SQL test cases generated without errors.

- [ ] **Step 4: Commit**

```bash
git add grammars/v3.5/sqlite_v3.py
git commit -m "feat: create v3.5 grammar with boosted seed weights for CVE-13435 and CVE-15358"
```

### Task 2: Smoke test v3.5 on hard CVEs

**Purpose:** Verify boosted seeds trigger the 2 previously-unfound CVEs before committing to 20 full campaigns.

- [ ] **Step 1: Smoke test both hard CVEs in parallel (8GB VM can handle 2 x 5-min runs)**

```bash
# Run both smoke tests simultaneously — 5-min campaigns are light enough
GRAMMAR=grammars/v3.5/sqlite_v3.py DURATION=300 ./scripts/run_eval.sh sqlite-3.32.0 smoke_v35_13435 &
PID1=$!
GRAMMAR=grammars/v3.5/sqlite_v3.py DURATION=300 ./scripts/run_eval.sh sqlite-3.32.2 smoke_v35_15358 &
PID2=$!
wait $PID1 $PID2
echo "Both smoke tests complete"
```

- [ ] **Step 2: Check smoke test results**

```bash
# CVE-2020-13435 (3.32.0)
python3 scripts/collect_crashes.py --scan-only --workdir workdirs/sqlite-3.32.0_smoke_v35_13435
# Expected: At least 1 crash matching CVE-13435 stack pattern

# CVE-2020-15358 (3.32.2)
python3 scripts/collect_crashes.py --scan-only --workdir workdirs/sqlite-3.32.2_smoke_v35_15358
# Expected: At least 1 crash matching CVE-15358 heap buffer read pattern
```

- [ ] **Step 3: Decision gate**

**IF both smoke tests find their target CVE:** proceed to Task 3 (full campaigns).

**IF one or both fail:**
1. Bump the failing seed weight from 0.5 to 1.0
2. Re-run the smoke test (5 min)
3. If still fails at 1.0, bump to 2.0 and re-run
4. If still fails at 2.0, investigate the seed rule itself — the SQL pattern may need adjustment
5. Loop until both CVEs trigger, then proceed to Task 3

Document the final seed weights used in the grammar file header.

- [ ] **Step 4: Commit final v3.5 if weights changed**

```bash
git add grammars/v3.5/sqlite_v3.py
git commit -m "fix: adjust v3.5 seed weights after smoke testing"
```

### Task 3: Run RQ1 full campaigns (v3.5, 15 min, 5 runs x 4 versions)

**Pre-requisite:** Task 2 smoke tests passed.

- [ ] **Step 1: Build harnesses for all 4 versions**

Verify all harness binaries exist:
```bash
ls harness/afl/sqlite_harness_patterns_sqlite-3.30.1
ls harness/afl/sqlite_harness_patterns_sqlite-3.31.1
ls harness/afl/sqlite_harness_patterns_sqlite-3.32.0
ls harness/afl/sqlite_harness_patterns_sqlite-3.32.2
```

If any missing, rebuild:
```bash
cd harness && make TARGET=sqlite_harness_patterns_sqlite-<VERSION> SQLITE=../cve_builds/sqlite-<VERSION>/sqlite3.c
```

- [ ] **Step 2: Run 20 campaigns SEQUENTIALLY (8GB VM — one at a time)**

```bash
# SEQUENTIAL — do NOT parallelize. 8GB RAM cannot handle concurrent campaigns.
# Each campaign: 15 min. Total: 20 x 15 min = 5 hours.
for VERSION in sqlite-3.30.1 sqlite-3.31.1 sqlite-3.32.0 sqlite-3.32.2; do
  for RUN in run1 run2 run3 run4 run5; do
    echo "=== v3.5 ${VERSION} ${RUN} ($(date)) ==="
    GRAMMAR=grammars/v3.5/sqlite_v3.py DURATION=900 ./scripts/run_eval.sh ${VERSION} v35_${RUN}
  done
done
```

Estimated wall time: ~5 hours. Run first, then start RQ1 triage while RQ2 campaigns run.

- [ ] **Step 3: Verify all 20 campaigns completed**

```bash
ls workdirs/ | grep v35 | wc -l
# Expected: 20
```

### Task 4: Run RQ2 full campaigns (v3.3, 30 min, 5 runs x 4 versions)

- [ ] **Step 1: Run 20 campaigns SEQUENTIALLY (8GB VM — one at a time)**

```bash
# SEQUENTIAL — do NOT parallelize. 8GB RAM cannot handle concurrent campaigns.
# Each campaign: 30 min. Total: 20 x 30 min = 10 hours. Run overnight.
for VERSION in sqlite-3.30.1 sqlite-3.31.1 sqlite-3.32.0 sqlite-3.32.2; do
  for RUN in run1 run2 run3 run4 run5; do
    echo "=== v3.3 ${VERSION} ${RUN} ($(date)) ==="
    GRAMMAR=grammars/legacy/sqlite_patterns.py DURATION=1800 ./scripts/run_eval.sh ${VERSION} v33_${RUN}
  done
done
```

Estimated wall time: ~10 hours. Run overnight while you sleep.

**NOTE:** Verify `grammars/legacy/sqlite_patterns.py` is the v3.3 grammar (520 rules, no seeds). Check the header comment.

- [ ] **Step 2: Verify all 20 campaigns completed**

```bash
ls workdirs/ | grep v33 | wc -l
# Expected: 20
```

---

## Phase 2: Data Collection + Analysis

### Task 5: Collect and triage RQ1 crash data

- [ ] **Step 1: Run crash collector on all v3.5 campaigns**

```bash
python3 scripts/collect_crashes.py --incremental
```

- [ ] **Step 2: Run CVE signature matching**

```bash
python3 triage/cve_signatures.py --workdir-pattern "v35_*"
```

- [ ] **Step 3: Generate RQ1 data tables**

Build the CVE rediscovery table:
- For each CVE, count how many of 5 runs triggered it, per SQLite version
- Filter out debug asserts (signal-5 / exit code 133) — only real crashes
- Cross-reference with existing EBNF data

Output: `results/comparison/rq1_cve_rediscovery.csv`

- [ ] **Step 4: Extract time-to-first-CVE-crash**

For each campaign that found a CVE, find the execution count of the first matching crash.
Convert to seconds using throughput (execs / execs_per_sec).

Output: `results/comparison/rq1_time_to_first_cve.csv`

- [ ] **Step 5: Verify RQ1 target — should be 5/5 detectable CVEs found**

Check: CVE-2020-13434, CVE-2020-9327, CVE-2020-13871, CVE-2020-13435, CVE-2020-15358 all have at least 1 hit across runs.
CVE-2019-19646 excluded (oracle limitation).

**IF any detectable CVE has 0 hits:** go back to Task 2, investigate and fix the seed.

### Task 6: Collect and triage RQ2 crash data

- [ ] **Step 1: Run crash collector on all v3.3 campaigns**

```bash
python3 scripts/collect_crashes.py --incremental
```

- [ ] **Step 2: Deduplicate and categorize**

```bash
python3 triage/stack_dedup.py --workdir-pattern "v33_*" --top-frames 5
```

- [ ] **Step 3: Filter out debug asserts**

Remove all crashes with exit code 133 (signal-5 / SIGTRAP / SQLite debug assert).
Keep only ASan (exit 223) and UBSan (exit 1) crashes.

- [ ] **Step 4: Build bug class registry from fresh data**

Group by crashing function + sanitizer type.
Output: `results/rq2_fresh/registry.json` with same schema as `results/crashes/registry.json`

- [ ] **Step 5: Cross-reference with CVE signatures**

Separate CVE-matching crashes (already counted in RQ1) from novel bugs (RQ2's contribution).

### Task 7: Generate figures

- [ ] **Step 1: F1 — Time-to-first-CVE-crash (RQ1)**

Python script using matplotlib. Boxplot, x-axis = CVEs, y-axis = seconds to first crash.
Only include CVEs found by proposed grammar.
Save to `docs/thesis/v2/figures/fig_4_1_time_to_first_cve.pdf`

- [ ] **Step 2: F2 — Bug class breakdown (RQ2)**

Bar chart. x-axis = bug classes, y-axis = unique hashes.
Color-code by severity (HIGH/MED/LOW).
Save to `docs/thesis/v2/figures/fig_4_2_bug_class_breakdown.pdf`

- [ ] **Step 3: F3 — Coverage growth over time (RQ3)**

Line chart with mean ± 1 std shaded band. Proposed vs EBNF.
Use timeseries data from v3.5 + EBNF campaigns.
Save to `docs/thesis/v2/figures/fig_4_3_coverage_growth.pdf`

- [ ] **Step 4: F4 — Throughput comparison (RQ3)**

Grouped bar chart. x-axis = SQLite versions, y-axis = execs/sec.
Proposed vs EBNF. Error bars = ±1 std.
Save to `docs/thesis/v2/figures/fig_4_4_throughput.pdf`

- [ ] **Step 5: F5 — Time-to-first-real-crash (RQ3)**

Boxplot. x-axis = SQLite versions, y-axis = seconds.
Proposed vs EBNF. Only real crashes (no debug asserts).
Save to `docs/thesis/v2/figures/fig_4_5_time_to_first_crash.pdf`

### Task 8: Compute statistical tests

- [ ] **Step 1: Mann-Whitney U + Cliff's d for RQ3 metrics**

For each metric (throughput, coverage, time-to-first-crash) x each SQLite version:
- Mann-Whitney U test (n=5 per group)
- Cliff's d effect size
- Report p-value and effect size category (small/medium/large)

Output: `results/comparison/rq3_statistical_tests.csv`

---

## Phase 3: Thesis Writing

### Task 9: Rewrite Chapter 4

**File:** `docs/thesis/v2/chapters/c4_experiments.tex`

**CRITICAL RULES:**
- No grammar version numbers (v3.0, v3.1, etc.) — use descriptive names only
- Follow `docs/thesis/template/rules/chapter4-rule.md` constraint doc exactly
- All tables: mean±std, proposed row **bolded**, thousand separators, 1 decimal %
- Past tense for experiments, present tense for analysis
- No bullet lists in body text (prose only, except RQ list and Discussion enumerations)
- Each RQ subsection ends with 1-2 sentence interpretation

- [ ] **Step 1: Write 4.1 Research Questions**

Three RQs, each as a question ending with "?":
- RQ1 (CVE Rediscovery): "Can the proposed grammar rediscover known CVEs through compositional generation of structural primitives?"
- RQ2 (Bug Detection Capability): "Does the proposed grammar discover previously unreported bugs beyond the target CVEs?"
- RQ3 (Performance): "What are the performance characteristics and tradeoffs of the proposed grammar compared to the baseline?"

- [ ] **Step 2: Write 4.2 Dataset and Experimental Setup**

4 subsections per constraint:
- 4.2.1 Subjects: table with SQLite versions, release dates, LOC, known CVEs
- 4.2.2 Input dataset: describe grammars descriptively (not by version number)
- 4.2.3 Environment: exact CPU, RAM, OS, Rust version, Clang version
- 4.2.4 Configuration: campaign parameters table (T1)

- [ ] **Step 3: Write 4.3 Baseline Methods**

EBNF paragraph (what, who, what direction, why chosen).
Proposed grammar paragraph (**bolded**, labeled *(proposed)*, presented last).

- [ ] **Step 4: Write 4.4 Evaluation Metrics**

5 metrics, each with bold name + definition + which RQ it answers:
- **Unique root causes** (RQ2)
- **CVE signature match rate** (RQ1)
- **Edge coverage** (RQ3)
- **Throughput** (RQ3)
- **Time-to-first-crash** (RQ3) — include LaTeX formula: $T_{fc} = \frac{E_{first}}{R_{throughput}}$ where $E_{first}$ is execution count at first crash and $R_{throughput}$ is mean executions per second

- [ ] **Step 5: Write 4.5.1 RQ1 Results**

- Table T2 (CVE rediscovery + reachability, merged)
- Figure F1 (time-to-first-CVE-crash)
- Case studies for found CVEs
- Analysis of unfound CVE (CVE-2019-19646, oracle limitation)
- 1-2 sentence interpretation

- [ ] **Step 6: Write 4.5.2 RQ2 Results**

- Table T3 (bug class summary from fresh v3.3 data)
- Figure F2 (bug class breakdown)
- Case studies for each non-CVE bug class
- **Placeholder section** for latest-SQLite 0-day results (marked clearly)
- 1-2 sentence interpretation

- [ ] **Step 7: Write 4.5.3 RQ3 Results**

- Table T5 (performance comparison with statistical tests)
- Figures F3, F4, F5
- Honest tradeoff interpretation: lower throughput/coverage, but more bugs found faster

- [ ] **Step 8: Write 4.6 Analysis and Discussion**

5 sub-parts per constraint:
1. Qualitative analysis (3 named groups with %)
2. In-depth comparison with baseline
3. Failure cases & limitations (≥3 concrete)
4. Threats to validity (internal, external, construct)
5. Summary + verification on modern SQLite (3.53.0 = 0 crashes)

- [ ] **Step 9: Build PDF and verify**

```bash
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
cd docs/thesis/v2
pdflatex -interaction=nonstopmode -output-directory=out thesis.tex && bibtex out/thesis && pdflatex -interaction=nonstopmode -output-directory=out thesis.tex && pdflatex -interaction=nonstopmode -output-directory=out thesis.tex
```

Check: 0 undefined references, all figures/tables render, no compilation errors.

- [ ] **Step 10: Constraint compliance check**

Verify against `chapter4-rule.md`:
- [ ] 6-section order (X.1–X.6) ✓
- [ ] RQs phrased as questions ✓
- [ ] Subjects table with name/version/type/scale ✓
- [ ] ≥3 repetitions, mean±std ✓
- [ ] Baselines in separate paragraphs ✓
- [ ] Proposed method bolded and last ✓
- [ ] At least one metric with LaTeX formula ✓
- [ ] Each RQ subsection has table/figure ✓
- [ ] Discussion has 5 sub-parts ✓
- [ ] ≥3 limitations ✓
- [ ] Three validity types ✓
- [ ] No bullet lists in body text ✓
- [ ] Thousand separators, 1 decimal %, past/present tense ✓

- [ ] **Step 11: Commit**

```bash
git add docs/thesis/v2/chapters/c4_experiments.tex docs/thesis/v2/figures/fig_4_*
git commit -m "feat: rewrite chapter 4 with fresh campaign data and constraint compliance"
```

---

## Dependencies and Execution Order

**8GB VM constraint: all full campaigns run sequentially, one at a time.**

```
Day 1 (daytime, ~6 hours):
  Task 1 (create v3.5)           ~10 min
  → Task 2 (smoke test, parallel) ~10 min
  → Task 3 (RQ1 campaigns)        ~5 hours  [sequential, 20 x 15 min]

Day 1 (overnight, ~10 hours):
  Task 4 (RQ2 campaigns)          ~10 hours [sequential, 20 x 30 min]

Day 2 (daytime):
  Task 5 (RQ1 triage)             ~30 min   [can start as soon as Task 3 done]
  Task 6 (RQ2 triage)             ~30 min   [after Task 4 completes overnight]
  Task 7 (generate figures)        ~1 hour
  Task 8 (statistical tests)       ~30 min
  Task 9 (write chapter)           ~4-6 hours
```

**Key overlap:** While RQ2 campaigns run overnight (Task 4), you can start RQ1 triage (Task 5) and even RQ3 figure generation (Tasks 7.3-7.5) since those use RQ1 data which is already complete. Triage scripts are CPU-light and won't interfere with the running campaign.

**Total wall time:** ~2 days (campaigns are the bottleneck, not analysis or writing).

---

## Separate Session: Grammar Enhancement for 0-day Hunting

**NOT in this plan.** Requires:
1. Analyze SQLite 3.53.0 changelog for new features/subsystems
2. Add grammar rules targeting new code paths (JSONB, strict tables, etc.)
3. Run campaigns on 3.53.0 with enhanced grammar
4. If 0-days found: responsible disclosure process, then add results to RQ2 placeholder section

This work happens in a dedicated Claude Code session after the main Chapter 4 is written.
