# RL-Nautilus Phase 2: Comprehensive Multi-Expert Audit

**Date:** 2026-04-30
**Auditors:** DBMS Fuzzing Expert, Security Researcher, Triage Pipeline Expert, Research Methodology Reviewer
**Scope:** Full repository audit — fuzzer engine, grammar, harness, triage, RL, scripts, research methodology

---

## Executive Summary

RL-Nautilus is a well-engineered grammar-based SQLite fuzzer with strong infrastructure (fork server, weighted grammar engine, triage pipeline, DQN skeleton). The **grammar evolution methodology** — data-driven weight tuning from per-rule attribution — is the project's strongest and most novel contribution. The E2 ablation produced an intellectually honest negative result (vocabulary breadth > distillation quality at 15 min).

However, the project has three critical gaps that must be addressed:

1. **Zero ASan/UBSan detections** across all campaigns — all 600+ crashes are debug assertions (SIGTRAP/SIGABRT), not memory safety violations. The harness binaries likely lack sanitizer instrumentation, undermining CVE rediscovery claims.
2. **RL (Phase 3) has never been run** — the DQN is fully implemented but `rl_enabled: true` has never been tested, and 3 of 12 state features are stubbed to zero.
3. **Insufficient statistical power** — N=2 runs, no RNG seeds, no statistical tests, no coverage-over-time data.

**Overall Score: 6.2 / 10** — Strong engineering, weak empirical validation.

---

## Dimension Scores

| Dimension | Score | Verdict |
|-----------|-------|---------|
| Grammar Quality & Design | 8/10 | Excellent decomposition, well-versioned evolution, minor coverage gaps |
| Mutation Strategy | 6/10 | Standard Nautilus pipeline; missing semantic mutations, byte-level havoc |
| Feedback Mechanism | 5/10 | Edge-presence only (no hit-count bucketing), no semantic validity feedback |
| Oracle & Detection | 3/10 | **Critical**: Zero sanitizer detections; debug asserts dominate; no differential/metamorphic oracle |
| Triage Pipeline | 6/10 | Solid classify.py but dedup fails on SIGTRAP crashes; CVE signatures unused in triage |
| Campaign Infrastructure | 6/10 | Working fork server; no multi-core scaling; no RNG seed control |
| RL Integration | 4/10 | Architecture ready but untested; 3/12 state features stubbed; no bandit baseline |
| Security (Code) | 5/10 | 3 HIGH findings (UB in forksrv, outdated deps); no sandbox on fork child |
| Research Methodology | 4/10 | No formal hypothesis; N=2; no related work; no paper draft |
| Documentation | 7/10 | Strong architecture docs, grammar changelog; stale README; missing paper figures |

---

## I. CRITICAL FINDINGS (Must Fix)

### C1. Harness binaries likely lack ASan/UBSan instrumentation
**Impact:** Invalidates all CVE rediscovery claims
**Evidence:** Zero exit-223 (ASan) or exit-1 (UBSan) across 600+ crashes in campaigns E4-E6. All crashes are SIGTRAP (signal-5, debug_assert) or SIGABRT (signal-6).
**Verification:**
```bash
nm harness/sqlite_harness_patterns_sqlite-3.31.1 | grep -c __asan
# If 0 → harness has no ASan
```
**Fix:** Recompile all 4 harness binaries with `-fsanitize=address,undefined`. The Makefile must pass these flags to both the harness and the SQLite amalgamation:
```makefile
CFLAGS += -fsanitize=address,undefined -fno-omit-frame-pointer
```
**Files:** `harness/Makefile`, all `harness/sqlite_harness_*` binaries

### C2. `CString::from_raw(strerror(...))` is undefined behavior
**Impact:** Heap corruption on every fork server error path
**Evidence:** `forksrv/src/lib.rs` lines 248, 255, 262 — `CString::from_raw()` takes ownership of a static/thread-local `strerror()` pointer and calls `free()` on it.
**Fix:** Replace `CString::from_raw(strerror(...))` with `CStr::from_ptr(strerror(...))` (borrows without ownership).

### C3. No formal research hypothesis
**Impact:** Thesis cannot be defended; no falsifiable claim to test
**Fix:** Write immediately:
> H1: DQN-guided mutation strategy selection discovers more unique root causes than uniform strategy selection within a 4-hour campaign on SQLite.
> H0: No significant difference.

---

## II. HIGH-PRIORITY FINDINGS

### H1. Shared memory leak — no `Drop` impl for `ForkServer`
**Severity:** HIGH (memory safety)
**File:** `forksrv/src/lib.rs:235-268`
**Issue:** `ForkServer` stores a raw `*mut [u8]` from `shmat()` but never calls `shmdt()`. On fork server restart (which happens on crash), old segments leak.
**Fix:** Implement `Drop` for `ForkServer` calling `shmdt(self.shared_data as *mut c_void)`.

### H2. Triage dedup produces zero deduplication for SIGTRAP crashes
**Severity:** HIGH (inflated crash counts)
**File:** `triage/classify.py:128-130`
**Issue:** classify.py extracts ASan/UBSan frames from stderr. SIGTRAP crashes produce no such frames, so every crash gets a unique content hash → 113 "unique" crashes that are likely 2-3 root causes.
**Fix:** Integrate GDB-based frame extraction from `stack_dedup.py` into classify.py's dedup path. When ASan frames are empty, fall back to `stack_dedup.run_gdb_on_crash()`.

### H3. Outdated `nix` crate with known soundness issues
**Severity:** HIGH (supply chain)
**File:** `forksrv/Cargo.toml` (nix 0.15), `fuzzer/Cargo.toml` (nix 0.17)
**Issue:** Versions before 0.22 have RUSTSEC-2021-0119 (uninitialized memory in `getpeereid`).
**Fix:** Update to `nix = "0.29"`.

### H4. `exec()` of arbitrary Python in grammar loading and analysis
**Severity:** HIGH (code execution, by design)
**Files:** `fuzzer/src/python_grammar_loader.rs:53-61`, `scripts/analyze_attribution.py:43`
**Issue:** Grammar files execute arbitrary Python via PyO3 `py.run()` and Python `exec()`.
**Mitigation:** Acceptable for thesis use. Document the risk. For any shared deployment, sandbox grammar execution.

### H5. Coverage bitmap lacks hit-count bucketing
**Severity:** HIGH (reduced fuzzing effectiveness)
**File:** `fuzzer/src/fuzzer.rs:462`
**Issue:** `new_bits()` only checks edge presence (`!= 0 && *elem == 0`). AFL-style bucketing (1, 2, 4-7, 8-15, ...) provides 8x finer coverage resolution.
**Fix:** Implement `classify_counts()` mapping: `{0→0, 1→1, 2→2, 3→4, 4-7→8, 8-15→16, 16-31→32, 32-127→64, 128+→128}`.

### H6. DQN state features partially stubbed
**Severity:** HIGH (RL cannot learn effectively)
**File:** `fuzzer/src/rl_hook.rs:45-48,103`
**Issue:** `coverage_velocity`, `crash_rate`, and all 5 `strategy_emas` are hardcoded to 0.0. The DQN operates on 4 real dimensions disguised as 12.
**Fix:** Wire EMAs: `ema = 0.99 * ema + 0.01 * reward` per strategy. Compute `coverage_velocity` as rolling window delta. Compute `crash_rate` as crashes/executions over last 1000 execs.

---

## III. MEDIUM-PRIORITY FINDINGS

### M1. `time 0.1` crate has RUSTSEC-2020-0071
**File:** `forksrv/Cargo.toml`, `fuzzer/Cargo.toml`
**Issue:** Segfault in multi-threaded programs using `localtime_r`. The fuzzer is multi-threaded.
**Fix:** Migrate to `time = "0.3"` or `chrono`.

### M2. Wildcard dependency versions
**File:** `fuzzer/Cargo.toml` — `libc = "*"`, `ron = "*"`
**Fix:** Pin to specific ranges: `libc = "0.2"`, `ron = "0.8"`.

### M3. Deprecated `compare_and_swap` spinlock
**File:** `fuzzer/src/state.rs:78-92`
**Issue:** Custom spinlock using deprecated API, no panic guard, 30s timeout that panics.
**Fix:** Remove the `AtomicBool` spinlock; rely on the existing `RwLock`. Replace `compare_and_swap` with `compare_exchange`.

### M4. Thread panics cascade via poisoned mutex
**File:** `fuzzer/src/main.rs:225-275`
**Issue:** All `.expect("RAND_...")` calls panic on poisoned mutex, cascading failure across threads.
**Fix:** Handle poisoned mutexes: `lock().unwrap_or_else(|e| e.into_inner())`. Replace random placeholder strings with descriptive messages.

### M5. Exit-code-0 unconditionally classified as `debug_assert`
**File:** `triage/classify.py:83-84`
**Issue:** Exit 0 = normal termination. Classifying it as `debug_assert` without stderr evidence means clean runs would be counted as crashes if the assumption breaks.
**Fix:** Require stderr evidence (e.g., "assert" substring) for exit-0 debug_assert classification.

### M6. UBSan `signed-integer-overflow` subtype is dead code
**File:** `triage/classify.py:73-80`
**Issue:** `"integer overflow"` check at line 73 matches before `"signed integer overflow"` at line 79 (substring match).
**Fix:** Swap order: check `"signed integer overflow"` first.

### M7. CVE signatures never used in triage output
**File:** `triage/cve_signatures.py` (defined but unused by `classify.py`)
**Issue:** No automatic CVE attribution. Signatures only feed fidelity_score.py for grammar evaluation.
**Fix:** Call `cve_signatures.missing_patterns()` in classify.py; add `cve_matches` field to `CrashCluster`.

### M8. Fork child has no LOAD_EXTENSION restriction
**File:** `harness/sqlite_harness.c`
**Issue:** A crafted input could call `LOAD_EXTENSION` to load arbitrary shared objects.
**Fix:** Add `sqlite3_db_config(db, SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 0, NULL)` after `sqlite3_open`.

### M9. Shell injection vectors in scripts
**Files:** `scripts/run_ablation.sh:84-85` (Python `-c` with unquoted `$WD`), `triage/stack_dedup.py:108` (GDB `--ex` with crash file path)
**Fix:** Pass paths via `sys.argv` instead of string interpolation. Quote GDB arguments.

### M10. No Python lockfile for cve2grammar
**File:** `cve2grammar/pyproject.toml`
**Fix:** Generate `requirements.txt` with pinned versions or use `uv lock`.

---

## IV. LOW-PRIORITY FINDINGS

| # | Finding | File | Fix |
|---|---------|------|-----|
| L1 | Predictable `/tmp/test_tree.ron` (symlink attack) | `fuzzer/src/generator.rs:106` | Use `tempfile::NamedTempFile` |
| L2 | Predictable `/tmp/sqlite_attack_v1.py` in ablation | `scripts/run_ablation.sh:39` | Use `mktemp` |
| L3 | ChunkStore max size 30 nodes drops large interesting subtrees | `grammartec/src/chunkstore.rs:57` | Raise to 50 or make configurable |
| L4 | Fixed havoc iteration count (100) regardless of tree size | `fuzzer/src/state.rs` | Scale with tree node count |
| L5 | `Table-Name` dead weight (t1/t2/t3 at weight=0.3 but no pre-loaded tables) | `grammars/active/sqlite_v3.py` | Remove or set weight=0 |
| L6 | All 65+ `Expr` rules at uniform weight=1.0 | `grammars/active/sqlite_v3.py` | Boost terminal Expr rules to weight=2.0 |
| L7 | Exec.log truncation destroys history at 10MB | `fuzzer/src/fuzzer.rs:76-86` | Implement log rotation |
| L8 | No resource limits (`setrlimit`) on forked children | `forksrv/src/lib.rs` | Cap `RLIMIT_NOFILE`, `RLIMIT_AS` |
| L9 | minimize.py has zero test coverage | `triage/minimize.py` | Write unit tests for `same_crash`, `split_statements` |
| L10 | `experiments.json` E3-E6 have null conclusions | `results/experiments.json` | Fill in from campaign data |

---

## V. ENHANCEMENT ROADMAP

### Tier 1: Immediate (1-3 days) — Unblock thesis

| # | Enhancement | Effort | Impact | Rationale |
|---|-------------|--------|--------|-----------|
| E1 | **Verify/fix ASan+UBSan in harness binaries** | 2h | CRITICAL | Without sanitizers, no memory safety CVE can be detected |
| E2 | **Fix `CString::from_raw` UB** | 15min | HIGH | Active undefined behavior in every error path |
| E3 | **Run DQN pilot** (`rl_enabled: true`, 1h campaign) | 4h | CRITICAL | Validates whether DQN learns anything at all — gates entire Phase 3 |
| E4 | **Wire 3 stubbed DQN state features** | 4h | HIGH | DQN needs actual signal to learn from |
| E5 | **Write formal hypothesis H0/H1** | 1h | CRITICAL | Anchors all subsequent experiments |

### Tier 2: Short-term (1-2 weeks) — Strengthen measurement

| # | Enhancement | Effort | Impact | Rationale |
|---|-------------|--------|--------|-----------|
| E6 | **Implement UCB1 bandit baseline** | 4h code | HIGH | Required comparison for DQN justification; `MutationPolicy` trait makes it trivial |
| E7 | **Add hit-count bucketing to coverage bitmap** | 6h | HIGH | 8x finer coverage resolution; standard in AFL++ |
| E8 | **Integrate GDB dedup into classify.py** | 4h | HIGH | Fix zero-dedup for SIGTRAP crashes (dominant category) |
| E9 | **Add coverage-over-time logging** (periodic dump every 10s) | 3h | HIGH | Standard fuzzing paper figure; currently impossible to generate |
| E10 | **Add CVE signature matching to triage output** | 3h | MEDIUM | Connect grammar fidelity to actual crash-level CVE attribution |
| E11 | **Run E7: DQN vs Default vs UCB1** (3.31.1, 1h, N=5) | compute | CRITICAL | Core thesis experiment |
| E12 | **Update `nix`, `time`, pin wildcards** | 2h | MEDIUM | Eliminate known soundness issues |

### Tier 3: Medium-term (3-4 weeks) — Publication readiness

| # | Enhancement | Effort | Impact | Rationale |
|---|-------------|--------|--------|-----------|
| E13 | **Run E8: Time budget sweep** (15m, 1h, 4h, N=5) | compute | HIGH | Tests whether weighted sampling advantages emerge at longer horizons |
| E14 | **Run E10: Full cross-version** (best config, 4 versions, N=5) | compute | HIGH | Generalization evidence |
| E15 | **Write related work section** | 3 days | CRITICAL | Survey Nautilus, Squirrel, SQLancer, EcoFuzz, MOpt, NEUZZ at minimum |
| E16 | **Add byte-level havoc** (5% probability after grammar mutation) | 6h | MEDIUM | Discovers parser bugs that grammar-only mutation misses |
| E17 | **Separate `debug_assert` tracking from signal crashes** in fuzzer | 2h | MEDIUM | Prevents debug assertions from inflating crash metrics |
| E18 | **Statistical analysis** — Mann-Whitney U + Vargha-Delaney A12 | 4h | HIGH | Non-negotiable for any publication |
| E19 | **Implement `Drop` for `ForkServer`** + shared memory cleanup | 3h | MEDIUM | Fix memory leak on fork server restart |

### Tier 4: Nice-to-have — Competitive with state-of-art

| # | Enhancement | Effort | Impact |
|---|-------------|--------|--------|
| E20 | Semantic mutations (type-aware column references) | 2 weeks | HIGH — closes gap with Squirrel |
| E21 | Differential testing oracle (same SQL on 2 SQLite versions) | 1 week | HIGH — detects logic bugs |
| E22 | Multi-core scaling (per-core processes, shared-memory bitmap) | 2 weeks | MEDIUM — 4-8x throughput |
| E23 | Prioritized experience replay for DQN | 4h | LOW — marginal RL improvement |
| E24 | Statement reordering mutation | 4h | LOW — tests statement caching bugs |
| E25 | Corpus import/export across campaigns | 6h | MEDIUM — enables ensemble fuzzing |

---

## VI. COMPARISON WITH STATE-OF-ART

| Dimension | RL-Nautilus | Squirrel (CCS'20) | SQLancer (FSE'20) | SQLsmith | EcoFuzz (SEC'20) |
|-----------|-------------|--------------------|--------------------|----------|------------------|
| Grammar | Manual, weighted, versioned | IR-based AST | Template-based | Grammar-based | N/A (byte-level) |
| Semantic validity | None | Type-aware repair | TLP/NoREC oracle | Scope-aware | N/A |
| Mutation | Grammar tree + splice + havoc | IR mutation + semantic repair | Pivot rows | Random walk | Byte-level + MAB scheduling |
| Bug class | Crashes (currently debug_assert only) | Crashes | Logic bugs | Crashes | Crashes |
| Feedback | Edge presence only | Edge coverage | None | None | Edge coverage + UCB1 |
| RL/ML | DQN (untested) | None | None | None | UCB1 bandit |
| Novelty | RL + grammar-based DBMS fuzzing | Semantic-aware SQL mutation | Metamorphic testing | Random SQL gen | Adaptive scheduling |

**RL-Nautilus's unique position:** First system combining RL-guided strategy selection with grammar-based DBMS fuzzing. No existing fuzzer does this. The fidelity scoring system and data-driven grammar evolution are additional novel contributions.

**Key gaps vs competition:**
- No semantic validity awareness (vs Squirrel)
- No logic bug detection (vs SQLancer)
- No hit-count bucketing (vs AFL++/EcoFuzz)
- No bandit baseline for comparison (vs EcoFuzz)

---

## VII. THESIS COMMITTEE QUESTIONS (Anticipated)

1. **"The title says RL — where are the RL results?"** → Must run DQN experiments (E3, E11)
2. **"N=2 with no seeds — how reproducible?"** → Must scale to N>=5 (E11, E13, E14)
3. **"All crashes are debug assertions — where are memory safety violations?"** → Must fix harness binaries (E1)
4. **"Why DQN instead of a simpler bandit?"** → Must implement UCB1 baseline (E6, E11)
5. **"How does this compare to vanilla AFL++ on the same targets?"** → Must run AFL++ baseline
6. **"Your negative result (weights don't matter) — longer horizons?"** → Must run time budget sweep (E13)
7. **"3 stubbed state features — is the state representation sufficient?"** → Must wire features (E4)

---

## VIII. PUBLICATION ASSESSMENT

| Venue Tier | Feasibility | Requirements |
|------------|-------------|--------------|
| Workshop (BAR, FUZZING) | **Achievable in 6-8 weeks** | RL results + UCB1 comparison + grammar evolution story |
| Mid-tier (ACSAC, AsiaCCS) | **Possible in 3-4 months** | Above + 24h campaigns + statistical analysis + related work |
| Top-tier (USENIX, CCS, S&P) | **Unlikely without novel positive results** | DQN must measurably outperform baselines on multiple targets |

**Strongest publishable contribution (regardless of RL results):** The grammar evolution methodology — data-driven weight tuning from per-rule attribution analysis — is novel, practical, and well-documented. This could be a standalone workshop paper.

---

## IX. RECOMMENDED CRITICAL PATH

```
Week 1:  E1 (harness fix) + E2 (UB fix) + E4 (stub features) + E5 (hypothesis)
         → E3 (DQN pilot, 1h) → Decision gate: does DQN learn?
              ├─ YES → E6 (UCB1) + E11 (DQN vs Default vs UCB1)
              └─ NO  → Reframe as negative result + grammar contribution
Week 2:  E7 (hit-count bucketing) + E8 (GDB dedup) + E9 (coverage logging)
Week 3:  E11 (core experiment, N=5) + E13 (time sweep) + E12 (dep updates)
Week 4:  E14 (cross-version) + E15 (related work) + E18 (statistical analysis)
Week 5-6: Paper draft
```

**Decision gate after Week 1:** The DQN pilot (E3) determines the entire thesis direction. If Q-values differentiate and action distribution shifts, invest in RL experiments. If not, pivot to "empirical evaluation of adaptive scheduling in grammar-based fuzzing" with an honest negative finding about DQN complexity.
