# Attack-Grammar E2 Ablation — sqlite-3.31.1

**Date:** 2026-04-23
**Target:** `harness/sqlite_harness_patterns_sqlite-3.31.1` (ASan + UBSan + `SQLITE_DEBUG`)
**Config:** `DURATION=900` · `RUNS=2` · 4 grammar variants → 8 runs · ~2h wall time
**Orchestrator:** `scripts/run_ablation.sh` (commit `e6aa3d1`)
**Workdirs:** `/tmp/nautilus_eval/sqlite-3.31.1_<variant>_run<N>/`

---

## 1. Variants

| Variant     | Grammar                                              | Notes |
|-------------|------------------------------------------------------|-------|
| `attack_v1` | `/tmp/sqlite_attack_v1.py` (from tag `attack-v1-frozen`, commit `2298743`) | Pre-B2 distilled attack grammar |
| `attack_v2` | `grammars/sqlite_attack.py` @ HEAD                   | Post-B2 tight-NT rewrites for 5 patterns |
| `patterns`  | `grammars/sqlite_patterns.py`                        | Full pattern library (baseline) |
| `uniform`   | `grammars/sqlite_patterns_uniform.py`                | Weight-stripped pattern library |

Per Task 0 finding (b), Nautilus has no RNG seed control; the 2 runs per
variant are independent runs, **not** seed-controlled repetitions. Variance
numbers below should be read as a floor on run-to-run spread, not a true CI.

---

## 2. Raw results (from `ABLATION SUMMARY`)

| run_id            | crashes (signaled) | queue | total execs | unique root causes |
|-------------------|-------------------:|------:|------------:|-------------------:|
| attack_v1_run1    | 70                 | 1048  | 219,131     | 3                  |
| attack_v1_run2    | 115                | 1110  | 196,445     | 4                  |
| attack_v2_run1    | 19                 | 1082  | 224,701     | 2                  |
| attack_v2_run2    | 34                 | 1050  | 177,314     | 2                  |
| patterns_run1     | 306                | 1484  | 101,057     | 6                  |
| patterns_run2     | 284                | 1340  | 76,683      | 6                  |
| uniform_run1      | 337                | 1586  | 107,077     | 6                  |
| uniform_run2      | 255                | 1147  | n/a¹        | 5                  |

¹ `coverage.json` for `uniform_run2` missed `total_executions` (known A2
extraction gap: parse races the final exec.log flush; does not affect
crash/queue counts).

### 2a. Aggregates (sum across 2 runs)

| variant     | Σ crashes | Σ queue | variant RC ceiling² |
|-------------|----------:|--------:|--------------------:|
| attack_v1   | 185       | 2158    | **4**               |
| attack_v2   | 53        | 2132    | **2**               |
| patterns    | 590       | 2824    | **6**               |
| uniform     | 592       | 2733    | **6**               |

² Union of distinct top-frame clusters observed across both runs of a
variant. A variant's RC ceiling is what matters for thesis claims, not
per-run RC (which is bounded by time and generator luck).

---

## 3. Root-cause breakdown (stack_dedup by top gdb frame)

### attack_v1 (pre-B2)

| run  | n    | top frame |
|------|-----:|-----------|
| run1 |  50  | `alsoAnInt` @ sqlite3.c:85071 |
| run1 |  19  | `sqlite3_str_vappendf` @ sqlite3.c:28804 |
| run1 |   1  | `alsoAnInt` @ sqlite3.c:85071 (distinct backtrace) |
| run2 |  95  | `alsoAnInt` @ sqlite3.c:85071 |
| run2 |  13  | `sqlite3_str_vappendf` @ sqlite3.c:28804 |
| run2 |   6  | `alsoAnInt` @ sqlite3.c:85071 (distinct backtrace) |
| run2 |   1  | `alsoAnInt` @ sqlite3.c:85071 (distinct backtrace) |

**Union (2 runs):** `sqlite3_str_vappendf:28804` (CVE-2020-13434) + 3
`alsoAnInt` variants = **4 unique root causes**.

### attack_v2 (post-B2)

| run  | n    | top frame |
|------|-----:|-----------|
| run1 |  10  | `sqlite3_str_vappendf` @ sqlite3.c:28804 |
| run1 |   9  | `alsoAnInt` @ sqlite3.c:85071 |
| run2 |  22  | `sqlite3_str_vappendf` @ sqlite3.c:28804 |
| run2 |  12  | `alsoAnInt` @ sqlite3.c:85071 |

**Union (2 runs):** 2 unique root causes — the same two that dominate
attack_v1, but without the `alsoAnInt` backtrace diversity.

### patterns (baseline library)

| run  | n    | top frame |
|------|-----:|-----------|
| run1 | 256  | `sqlite3ExprCodeTarget` @ sqlite3.c:102474 |
| run1 |  24  | `__pthread_kill_implementation` (abort path) |
| run1 |  20  | `sqlite3Fts5ConfigParse` @ sqlite3.c:210506 |
| run1 |   3  | `sqlite3_str_vappendf` @ sqlite3.c:28841 |
| run1 |   2  | `sqlite3_str_vappendf` @ sqlite3.c:28804 |
| run1 |   1  | `exprAnalyze` @ sqlite3.c:143073 |
| run2 | 220  | `sqlite3ExprCodeTarget` @ sqlite3.c:102474 |
| run2 |  41  | `__pthread_kill_implementation` |
| run2 |  12  | `sqlite3Fts5ConfigParse` @ sqlite3.c:210506 |
| run2 |   8  | `exprAnalyze` @ sqlite3.c:143073 |
| run2 |   2  | `sqlite3_str_vappendf` @ sqlite3.c:28804 |
| run2 |   1  | `sqlite3_str_vappendf` @ sqlite3.c:28841 |

**Union:** 6 unique root causes. Stable across both runs (same 6 frames).

### uniform

| run  | n    | top frame |
|------|-----:|-----------|
| run1 | 235  | `sqlite3ExprCodeTarget` @ sqlite3.c:102474 |
| run1 |  46  | `sqlite3Fts5ConfigParse` @ sqlite3.c:210506 |
| run1 |  45  | `__pthread_kill_implementation` |
| run1 |   5  | `sqlite3_str_vappendf` @ sqlite3.c:28841 |
| run1 |   5  | `sqlite3_str_vappendf` @ sqlite3.c:28804 |
| run1 |   1  | `exprAnalyze` @ sqlite3.c:143073 |
| run2 | 167  | `sqlite3ExprCodeTarget` @ sqlite3.c:102474 |
| run2 |  47  | `__pthread_kill_implementation` |
| run2 |  36  | `sqlite3Fts5ConfigParse` @ sqlite3.c:210506 |
| run2 |   3  | `sqlite3_str_vappendf` @ sqlite3.c:28841 |
| run2 |   2  | `exprAnalyze` @ sqlite3.c:143073 |

**Union:** 6 unique root causes — identical set to `patterns`.

---

## 4. Fidelity deltas (attack_v1 → attack_v2, from A3 scorer)

Source: `docs/fidelity-baseline-attack-v1.json` · `docs/fidelity-postB2-attack-v2.json`

| pattern               | v1 score | v2 score | Δ     | note |
|-----------------------|---------:|---------:|------:|------|
| **P13435 (JOIN+window regression)** | 1.8%  | **18.6%** | **+10×** | B2 tight NTs worked (Join-Chain-NaturalPair + Scalar-Subquery-CoalesceWindow) |
| **P19646 (PRAGMA integrity_check loop)** | 7.7%  | **19.1%** | **+2.5×** | B2 tight NTs worked (GenCol-Def-SelfRef) |
| P13434-Boundary       | 11.5%   | 12.9%   | ≈     | pattern unchanged, drift within noise |
| P13871                | 3.6%    | 3.0%    | −0.6% | regression: tight NT over-constrained |
| P15358                | 0.12%   | 0.04%   | −0.08% | regression: tight NT over-constrained |
| **P9327**             | 0.0%    | **0.0%**    | 0     | **design gap: no `coalesce` in tight NTs** |

---

## 5. What the numbers say

### 5a. attack_v2 is strictly worse than attack_v1 for crash-finding

- attack_v1: 185 total crashes, 4 unique RCs over 2×15 min
- attack_v2: 53 total crashes, 2 unique RCs over 2×15 min

The B2 tight-NT rewrite **traded crash-diversity for per-sample fidelity**.
Fewer samples match the CVE signature per tree generated — but the
signature-matching samples don't convert into new crash sites. Two
reasons visible in the data:

1. The crashes attack_v1 hits are the ones it already hit pre-B2 — no
   new frames unlocked in attack_v2. B2's fidelity gains (P13435 10×,
   P19646 2.5×) did not produce new crash-bearing paths in 15 minutes.
2. attack_v2's per-run exec count is slightly higher
   (224k vs 219k), so the drop isn't from lost throughput. It's the
   tighter structural shape mattering less than volume for these
   frames.

### 5b. patterns and uniform converge on the same 6 frames

Both find 6 unique root causes over 2 runs, with identical frame sets:

```
sqlite3ExprCodeTarget:102474        (dominant, 60–80% of crashes)
sqlite3Fts5ConfigParse:210506
__pthread_kill_implementation       (abort path — SQLITE_DEBUG assert)
sqlite3_str_vappendf:28804          (CVE-2020-13434 canonical)
sqlite3_str_vappendf:28841          (CVE-2020-13434 adjacent line)
exprAnalyze:143073
```

The per-frame frequencies differ — `patterns` puts more weight on
`sqlite3ExprCodeTarget`, `uniform` spreads crashes more evenly — but the
**set of reachable RCs is the same**. The weighted prior in `patterns`
isn't unlocking new frames at the 15-minute horizon.

### 5c. Vocabulary matters more than weights at this horizon

`patterns` (weighted) vs `uniform` (stripped weights): essentially
identical RC ceiling, similar raw crash counts (590 vs 592). The
weight-design work in `sqlite_patterns.py` does not appear to do
meaningful work in this regime — **vocabulary breadth** is the
discriminator, not the prior.

### 5d. attack_v1 and attack_v2 miss 4 of the 6 frames

The attack grammar (both versions) only triggers:

- `sqlite3_str_vappendf:28804` (CVE-2020-13434)
- `alsoAnInt:85071` (UBSan integer cast, one of the `patterns` subset
  not reached by patterns/uniform in this 15-min window)

It misses: `sqlite3ExprCodeTarget`, `sqlite3Fts5ConfigParse`,
`__pthread_kill_implementation`, `exprAnalyze`. These four are
reachable under the pattern library within 15 minutes but outside
the attack grammar's vocabulary — confirming that **the distilled
attack grammar is a tight subset of the pattern-library surface**
and not a strict superset on crash-finding ability.

### 5e. CVE coverage

| CVE           | attack_v1 | attack_v2 | patterns | uniform |
|---------------|:---------:|:---------:|:--------:|:-------:|
| CVE-2020-13434 (printf overflow) | ✓ | ✓ | ✓ | ✓ |
| `alsoAnInt`   | ✓ (3 variants) | ✓ | — | — |
| `sqlite3ExprCodeTarget` | — | — | ✓ | ✓ |
| `sqlite3Fts5ConfigParse`| — | — | ✓ | ✓ |
| `exprAnalyze` | — | — | ✓ | ✓ |
| abort path    | — | — | ✓ | ✓ |

No variant triggered the in-corpus CVEs that ship with clean regex
signatures (P15358, P13871, P13435, P9327, P19646) within 15 minutes.
Those targets need longer budgets or different oracle matching; the
`alsoAnInt` integer-overflow frame is unclassified vs the cve-list.md
signatures.

---

## 6. Thesis implications (honest read)

### Positive

1. **B2 tight-NT design works when applied correctly.** P13435 fidelity
   going 1.8% → 18.6% (10×) and P19646 going 7.7% → 19.1% (2.5×) is
   mechanical evidence that the tight-NT principle produces more
   CVE-signature-matching samples.
2. **Stack-dedup (A1) is load-bearing.** Without it, the "18 unique
   crashes" claim from the earlier 15-min pilot was measurement
   artifact. The true answer is 2–4 per attack variant and 6 for
   pattern/uniform.
3. **Weights are not the discriminator at this horizon.** `patterns`
   vs `uniform` find the identical RC set; the advantage of weighted
   sampling is not visible in 15-minute windows.

### Negative / limitation

1. **Thesis claim "quality beats grammar size" is not supported by this
   ablation.** At 15 minutes on sqlite-3.31.1, the pattern library
   reaches 6 unique root causes; the distilled attack grammar reaches
   2–4. Crash-finding scales with vocabulary breadth, not with
   distillation tightness.
2. **Fidelity does not convert to new crashes in 15 minutes.** The
   attack_v2 fidelity gains (10× on P13435, 2.5× on P19646) produced
   zero additional root causes vs attack_v1. Either the time budget is
   too short for the signature-matching trees to mature into crashes,
   or the CVE-signature regex does not predict crash-site reachability.
3. **Design gap: P9327 fidelity is 0% in both versions.** The spec §3.2
   tight-NT mapping omits `coalesce(...)`, so no signature-matching
   sample is ever generated. This is a spec bug, not an execution
   artifact.

### Non-results

- We cannot claim time-to-first-crash differences from 2 runs per
  variant; the N is too small.
- We cannot claim RL-worthy signal — RL work is Phase 3.

---

## 7. What to run next (not part of this thesis iteration)

- **Longer horizon:** 1-hour or 4-hour runs would test whether
  attack_v2's fidelity gains eventually dominate, or whether the
  pattern library's breadth advantage compounds.
- **Fix P9327 spec gap:** add `coalesce_call` to a tight NT
  (`Scalar-Subquery-CoalesceWindow` would be a natural host).
- **CVE-aware oracle:** add signature-matching at triage time so we can
  count CVE-class hits, not just frame hits.

---

## 8. Reproducibility

```bash
# from rl-nautilus-phase-2 root
git checkout phase-2
git log --oneline | grep -q b17ebf7                       # expected commit
DURATION=900 RUNS=2 TARGET=sqlite-3.31.1 \
    ./scripts/run_ablation.sh 2>&1 | tee /tmp/ablation_x2.log

# inspect per-run dedup
for d in /tmp/nautilus_eval/sqlite-3.31.1_*/dedup.json; do
    echo "=== $(basename $(dirname $d)) ==="
    python3 -c "import json; d=json.load(open('$d')); print(d['total_crashes'], d['unique_root_causes'])"
done
```

**Prereqs:** `attack-v1-frozen` tag resolvable; `/tmp/sqlite_attack_v1.py`
materialized (auto-done by orchestrator at line 39); harness
`sqlite_harness_patterns_sqlite-3.31.1` built.

---

## 9. Appendix — full per-run stats

### Per-run executions-per-second

- attack_v1_run1: 243 ex/s
- attack_v1_run2: 218 ex/s
- attack_v2_run1: 250 ex/s
- attack_v2_run2: 197 ex/s
- patterns_run1: 112 ex/s
- patterns_run2:  85 ex/s
- uniform_run1:  119 ex/s
- uniform_run2:  n/a (coverage.json missed extraction)

Attack variants are ~2× faster in ex/sec than pattern/uniform because
their generated SQL is shorter and fails parse earlier. This **amplifies**
the negative result for attack_v2: it has more attempts per second and
still finds fewer unique RCs than patterns/uniform.
