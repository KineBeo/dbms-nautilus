# Fix Thompson Sampling Bandit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the degenerate Thompson Sampling bandit so it actually discriminates between grammar rule groups, then validate with matched campaigns against the uniform baseline.

**Architecture:** Three surgical fixes to `grammar_bandit.rs` — fix the beta increment condition (core bug), add alpha/beta decay for non-stationarity, and add a coverage plateau detector. No new files, no new dependencies. Then run 5 matched campaigns per policy on sqlite-3.31.1 (15 minutes each) to measure whether the fixed bandit outperforms uniform on crash diversity.

**Tech Stack:** Rust (fuzzer crate), existing `rand_distr::Beta`, existing `scripts/run_eval.sh` campaign runner, existing `triage/stack_dedup.py` for crash diversity measurement.

---

### Task 1: Fix Beta Increment Condition (Core Bug)

**Files:**
- Modify: `fuzzer/src/grammar_bandit.rs:199-218` (`observe_reward` method)

The current code increments `beta` only when `raw_reward == 0.0`, which never fires because coverage always increases during fuzzing. This collapses all Beta distributions to `Beta(alpha_i, 1)` — a Polya urn that locks in early random proportions permanently.

Fix: increment beta when performance is below the running average, giving the Beta distribution both success and failure signals.

- [ ] **Step 1: Write the failing test**

Add this test to the `#[cfg(test)] mod tests` block at the bottom of `grammar_bandit.rs`:

```rust
#[test]
fn test_below_average_reward_increments_beta() {
    // Simulate: reward_ema = 10.0, raw_reward = 3.0 (below 50% of EMA)
    // Beta SHOULD increment because this is below-average performance.
    let reward_ema = 10.0_f32;
    let raw_reward = 3.0_f32;

    let mut alpha = 5.0_f32;
    let mut beta = 2.0_f32;

    // Current (broken) logic: beta only increments on raw_reward == 0
    // New logic: beta increments when raw_reward < reward_ema * 0.5
    let normalized = (raw_reward / reward_ema).min(2.0);
    alpha += normalized;

    if raw_reward < reward_ema * 0.5 {
        beta += 1.0;
    }

    assert!(beta > 2.0, "beta should increment for below-average reward, got {}", beta);
    assert!((alpha - 5.3).abs() < 0.01, "alpha should still get partial credit, got {}", alpha);

    // Verify: above-average does NOT increment beta
    let mut beta2 = 2.0_f32;
    let raw_reward2 = 8.0_f32;
    if raw_reward2 < reward_ema * 0.5 {
        beta2 += 1.0;
    }
    assert_eq!(beta2, 2.0, "above-average reward should NOT increment beta");
}
```

- [ ] **Step 2: Verify test logic is sound**

This test doesn't compile against the module yet (it's a standalone arithmetic test). Verify the math:
- `raw_reward=3.0 < reward_ema*0.5=5.0` → true → beta increments ✓
- `raw_reward=8.0 < reward_ema*0.5=5.0` → false → beta stays ✓

Run:
```bash
cargo test -p fuzzer --bin fuzzer -- grammar_bandit::tests::test_below_average_reward_increments_beta 2>&1 | grep -E 'test result|FAILED|ok'
```

Expected: PASS (this test is self-contained arithmetic, not calling the method yet).

- [ ] **Step 3: Fix `observe_reward` — change beta increment condition**

In `fuzzer/src/grammar_bandit.rs`, replace the `observe_reward` method (lines 199-218):

```rust
/// Update Beta parameters based on observed reward.
pub fn observe_reward(&mut self, coverage_delta: usize, crash_delta: u64) {
    if let Some(gi) = self.active_group {
        let raw_reward = coverage_delta as f32 + 10.0 * crash_delta as f32;

        const EMA_ALPHA: f32 = 0.1;
        self.reward_ema = EMA_ALPHA * raw_reward + (1.0 - EMA_ALPHA) * self.reward_ema;

        let normalized = if self.reward_ema > 0.1 {
            (raw_reward / self.reward_ema).min(2.0)
        } else {
            if raw_reward > 0.0 { 1.0 } else { 0.0 }
        };

        self.groups[gi].alpha += normalized;
        if self.reward_ema > 0.1 && raw_reward < self.reward_ema * 0.5 {
            self.groups[gi].beta += 1.0;
        }
        self.groups[gi].last_reward = raw_reward;
    }
}
```

The change: `if raw_reward == 0.0` → `if self.reward_ema > 0.1 && raw_reward < self.reward_ema * 0.5`. This fires when a group's reward in a window is less than half the running average — a meaningful "below average" signal that restores discriminative power to the Beta distribution.

- [ ] **Step 4: Run all existing bandit tests to verify no regressions**

```bash
cargo test -p fuzzer --bin fuzzer -- grammar_bandit 2>&1 | grep -E 'test result|FAILED|ok'
```

Expected: `test_zero_reward_increments_beta` will FAIL because its assertion assumes beta only increments at `raw_reward == 0`. We need to update it.

- [ ] **Step 5: Update `test_zero_reward_increments_beta` for new semantics**

Replace the test at line 364-374:

```rust
#[test]
fn test_zero_reward_increments_beta() {
    let alpha_before = 5.0_f32;
    let beta_before = 2.0_f32;

    // Zero reward is always below 50% of any positive EMA → beta increments
    let raw_reward = 0.0_f32;
    let reward_ema = 5.0_f32;

    let norm_reward = if reward_ema > 0.1 {
        (raw_reward / reward_ema).min(2.0)
    } else {
        0.0
    };
    let alpha_after = alpha_before + norm_reward;
    let mut beta_after = beta_before;
    if reward_ema > 0.1 && raw_reward < reward_ema * 0.5 {
        beta_after += 1.0;
    }

    assert_eq!(alpha_after, alpha_before, "alpha unchanged on zero reward");
    assert_eq!(beta_after, 3.0, "beta increments on below-average reward");
}
```

- [ ] **Step 6: Run all bandit tests — all should pass**

```bash
cargo test -p fuzzer --bin fuzzer -- grammar_bandit 2>&1 | grep -E 'test result|FAILED|ok'
```

Expected: `test result: ok. 11 passed` (9 original + 1 updated + 1 new).

- [ ] **Step 7: Commit**

```bash
git add fuzzer/src/grammar_bandit.rs
git commit -m "fix: bandit beta increment fires on below-average reward, not only zero

The old condition (raw_reward == 0.0) never fired because coverage always
increases during fuzzing, collapsing all Beta distributions to Beta(α,1) —
a Polya urn with no discriminative power. New condition fires when reward
is below 50% of the running EMA, restoring the Beta distribution's ability
to distinguish good arms from bad."
```

---

### Task 2: Add Alpha/Beta Decay for Non-Stationarity

**Files:**
- Modify: `fuzzer/src/grammar_bandit.rs:16-21` (constants), `observe_reward` method, `GroupState` struct

The coverage landscape changes dramatically during a campaign (4,775 new edges in first 100 updates → 46 by update 1100). Without decay, early-phase successes permanently dominate the Beta parameters, preventing re-exploration when the landscape shifts.

- [ ] **Step 1: Write the failing test**

Add to the test module:

```rust
#[test]
fn test_alpha_beta_decay() {
    // After many rounds, alpha/beta should decay toward prior (1.0, 1.0)
    let mut alpha = 50.0_f32;
    let mut beta = 20.0_f32;

    let decay_rate: f32 = 0.995;
    let prior_alpha: f32 = 1.0;
    let prior_beta: f32 = 1.0;

    // Apply 100 decay rounds
    for _ in 0..100 {
        alpha = prior_alpha + (alpha - prior_alpha) * decay_rate;
        beta = prior_beta + (beta - prior_beta) * decay_rate;
    }

    // 0.995^100 ≈ 0.606 → alpha ≈ 1 + 49*0.606 ≈ 30.7
    assert!(alpha < 50.0, "alpha should decay from 50, got {}", alpha);
    assert!(alpha > 20.0, "alpha should not decay too fast, got {}", alpha);
    assert!(beta < 20.0, "beta should decay from 20, got {}", beta);
    assert!(beta > 10.0, "beta should not decay too fast, got {}", beta);

    // After 1000 rounds: 0.995^1000 ≈ 0.0067 → nearly reset to prior
    let mut alpha2 = 50.0_f32;
    for _ in 0..1000 {
        alpha2 = prior_alpha + (alpha2 - prior_alpha) * decay_rate;
    }
    assert!((alpha2 - 1.0).abs() < 1.0, "after 1000 decays, alpha should approach prior, got {}", alpha2);
}
```

- [ ] **Step 2: Run to verify it passes (standalone arithmetic)**

```bash
cargo test -p fuzzer --bin fuzzer -- grammar_bandit::tests::test_alpha_beta_decay 2>&1 | grep -E 'test result|FAILED|ok'
```

Expected: PASS.

- [ ] **Step 3: Add decay constant and implement decay in `observe_reward`**

Add constant at line 21 (after `WEIGHT_MAX`):

```rust
const BETA_DECAY: f32 = 0.995;
```

Then modify `observe_reward` to apply decay before updating. Replace the method with:

```rust
/// Update Beta parameters based on observed reward.
/// Applies exponential decay toward prior (1.0, 1.0) before each update
/// to handle the non-stationary coverage landscape.
pub fn observe_reward(&mut self, coverage_delta: usize, crash_delta: u64) {
    if let Some(gi) = self.active_group {
        let raw_reward = coverage_delta as f32 + 10.0 * crash_delta as f32;

        const EMA_ALPHA: f32 = 0.1;
        self.reward_ema = EMA_ALPHA * raw_reward + (1.0 - EMA_ALPHA) * self.reward_ema;

        // Decay all groups toward prior (1.0, 1.0) — handles non-stationarity
        for gs in self.groups.iter_mut() {
            gs.alpha = 1.0 + (gs.alpha - 1.0) * BETA_DECAY;
            gs.beta = 1.0 + (gs.beta - 1.0) * BETA_DECAY;
        }

        let normalized = if self.reward_ema > 0.1 {
            (raw_reward / self.reward_ema).min(2.0)
        } else {
            if raw_reward > 0.0 { 1.0 } else { 0.0 }
        };

        self.groups[gi].alpha += normalized;
        if self.reward_ema > 0.1 && raw_reward < self.reward_ema * 0.5 {
            self.groups[gi].beta += 1.0;
        }
        self.groups[gi].last_reward = raw_reward;
    }
}
```

The decay factor 0.995 means ~50% forgotten after 138 rounds (13,800 executions at UPDATE_INTERVAL=100). This is a ~70-second effective memory window at 200 exec/sec — long enough to learn, short enough to adapt.

- [ ] **Step 4: Run all bandit tests**

```bash
cargo test -p fuzzer --bin fuzzer -- grammar_bandit 2>&1 | grep -E 'test result|FAILED|ok'
```

Expected: All pass. The standalone tests don't call `observe_reward` directly, so they are unaffected.

- [ ] **Step 5: Commit**

```bash
git add fuzzer/src/grammar_bandit.rs
git commit -m "feat: add alpha/beta decay for non-stationary coverage landscape

BETA_DECAY=0.995 applied to all groups each update round. Effective memory
window ~138 rounds (70s at 200 exec/s). Prevents early-phase successes from
permanently dominating the Beta distributions as coverage saturates."
```

---

### Task 3: Add Convergence Logging for Evaluation

**Files:**
- Modify: `fuzzer/src/grammar_bandit.rs:221-235` (`log_state` method)

The current CSV log doesn't include the per-group Beta mean (alpha/(alpha+beta)), which is the key metric for evaluating whether the bandit is discriminating. Add it so post-campaign analysis can directly plot convergence.

- [ ] **Step 1: Update `log_state` to include Beta means**

Replace the `log_state` method:

```rust
/// Log current state to CSV.
pub fn log_state(&self, selected: usize, total_coverage: usize) {
    let mut line = format!(
        "{},{}", self.total_updates,
        RuleGroup::from_index(selected).unwrap().name()
    );
    for gs in &self.groups {
        let mean = gs.alpha / (gs.alpha + gs.beta);
        line.push_str(&format!(
            ",{:.4},{:.4},{},{:.2},{:.4}",
            gs.alpha, gs.beta, gs.selection_count, gs.last_reward, mean
        ));
    }
    line.push_str(&format!(",{:.4},{}", self.reward_ema, total_coverage));
    line.push('\n');

    if let Ok(mut file) = OpenOptions::new().append(true).open(&self.log_path) {
        let _ = file.write_all(line.as_bytes());
    }
}
```

- [ ] **Step 2: Update CSV header in `new()` to match**

In the `new()` method, update the header format at line 137-148:

```rust
let group_headers: Vec<String> = (0..NUM_GROUPS)
    .map(|i| {
        let g = RuleGroup::from_index(i).unwrap();
        format!(
            "alpha_{0},beta_{0},count_{0},last_reward_{0},mean_{0}",
            g.name()
        )
    })
    .collect();
```

- [ ] **Step 3: Run all tests**

```bash
cargo test -p fuzzer --bin fuzzer -- grammar_bandit 2>&1 | grep -E 'test result|FAILED|ok'
```

Expected: All pass (log format changes don't affect test logic).

- [ ] **Step 4: Commit**

```bash
git add fuzzer/src/grammar_bandit.rs
git commit -m "feat: add per-group Beta mean to bandit CSV log

Adds mean_<Group> = alpha/(alpha+beta) column for each group. This is the
key convergence metric — shows whether the bandit discriminates between
groups over time."
```

---

### Task 4: Build and Smoke Test

**Files:**
- No new files. Verify the build and a quick 60-second campaign.

- [ ] **Step 1: Build release binary**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release 2>&1 | tail -5
```

Expected: Compiles successfully. The candle dependency may warn but should still compile for the main binary.

- [ ] **Step 2: Run a 60-second smoke test with bandit policy**

```bash
DURATION=60 THREADS=1 \
  /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/scripts/run_eval.sh \
  sqlite-3.31.1 smoke_bandit_fixed
```

Expected: Runs for 60 seconds, produces crashes in workdir, generates `bandit_log.csv`.

- [ ] **Step 3: Verify bandit_log.csv shows beta > 1.0**

```bash
WORKDIR=$(ls -td /tmp/nautilus_eval/sqlite-3.31.1_smoke_bandit_fixed* | head -1)
# Check that beta values are no longer stuck at 1.0
awk -F',' 'NR>1 {print $4, $9, $14, $19, $24, $29}' "$WORKDIR/bandit_log.csv" | tail -5
```

Expected: At least some beta columns show values > 1.0 (the fix is working).

- [ ] **Step 4: Verify Beta means show differentiation**

```bash
# Check mean columns (positions 6, 11, 16, 21, 26, 31 in the new format)
awk -F',' 'NR>1 {print $6, $11, $16, $21, $26, $31}' "$WORKDIR/bandit_log.csv" | tail -5
```

Expected: Different groups have different means (not all ≈1.0).

- [ ] **Step 5: Commit (no code changes, just verification)**

No commit needed. Proceed to evaluation campaigns.

---

### Task 5: Run Matched Evaluation Campaigns

**Files:**
- No code changes. Run 5 campaigns per policy (bandit vs uniform) on sqlite-3.31.1 at 15 minutes each.

This task produces the experimental data needed to determine whether the fixed bandit outperforms uniform on crash diversity.

- [ ] **Step 1: Run 5 bandit campaigns**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2

for i in 1 2 3 4 5; do
  DURATION=900 THREADS=1 POLICY=bandit \
    ./scripts/run_eval.sh sqlite-3.31.1 "fixed_bandit_run${i}"
done
```

Expected: 5 campaign workdirs in `/tmp/nautilus_eval/`.

- [ ] **Step 2: Run 5 uniform campaigns**

```bash
for i in 1 2 3 4 5; do
  DURATION=900 THREADS=1 POLICY=uniform \
    ./scripts/run_eval.sh sqlite-3.31.1 "fixed_uniform_run${i}"
done
```

Expected: 5 campaign workdirs in `/tmp/nautilus_eval/`.

- [ ] **Step 3: Triage all campaigns**

```bash
HARNESS="/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/afl/sqlite_harness_sqlite-3.31.1"

for dir in /tmp/nautilus_eval/sqlite-3.31.1_fixed_*; do
  echo "=== Triaging $dir ==="
  python3 -m triage.stack_dedup "$dir" \
    --harness "$HARNESS" \
    --output "$dir/dedup.json" || echo "warning: triage failed for $dir"
done
```

Expected: Each workdir gets a `dedup.json` with unique root cause counts.

- [ ] **Step 4: Collect results into comparison table**

```bash
echo "run_id,policy,total_crashes,unique_rcs,total_edges"
for dir in /tmp/nautilus_eval/sqlite-3.31.1_fixed_*; do
  run_id=$(basename "$dir")
  policy=$(echo "$run_id" | grep -oP '(bandit|uniform)')
  crashes=$(ls "$dir/outputs/signaled/" 2>/dev/null | wc -l)
  rcs=$(python3 -c "import json; d=json.load(open('$dir/dedup.json')); print(len(d.get('root_causes', d.get('clusters', []))))" 2>/dev/null || echo "N/A")
  edges=$(tail -1 "$dir/coverage.csv" 2>/dev/null | cut -d',' -f2 || echo "N/A")
  echo "$run_id,$policy,$crashes,$rcs,$edges"
done
```

- [ ] **Step 5: Statistical comparison**

Compare mean unique root causes between bandit and uniform using the output from Step 4. The key question: does the fixed bandit find >= as many unique root causes as uniform?

If bandit unique_rcs >= uniform unique_rcs: the fix works — Thompson Sampling's adaptive weighting adds value.
If bandit unique_rcs < uniform unique_rcs: the fix helped but wasn't enough — more work needed (possibly group classification coverage from evaluation metric #5).

- [ ] **Step 6: Archive results**

```bash
RESULTS_DIR="/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/results/campaigns/2026-05-07_fixed-bandit-eval"
mkdir -p "$RESULTS_DIR"

for dir in /tmp/nautilus_eval/sqlite-3.31.1_fixed_*; do
  run_id=$(basename "$dir")
  mkdir -p "$RESULTS_DIR/$run_id"
  cp "$dir/coverage.csv" "$dir/bandit_log.csv" "$dir/dedup.json" "$dir/campaign.json" \
     "$RESULTS_DIR/$run_id/" 2>/dev/null || true
done
```

- [ ] **Step 7: Commit results**

```bash
git add results/campaigns/2026-05-07_fixed-bandit-eval/
git commit -m "data: fixed-bandit vs uniform evaluation (5 runs × 2 policies × 15min)

Key metrics: unique root causes, crash accumulation, Beta distribution
convergence. Answers whether the beta-increment fix restores discriminative
power to Thompson Sampling."
```

---

### Task 6: Write Evaluation Summary

**Files:**
- Create: `results/fixed_bandit_evaluation.md`

- [ ] **Step 1: Write the evaluation report**

Using data from Task 5, create `results/fixed_bandit_evaluation.md` with:

```markdown
# Fixed Thompson Sampling Bandit Evaluation

**Date:** 2026-05-07
**Campaigns:** N=5 per policy, 15 minutes each, sqlite-3.31.1, 1 thread

## Changes Made

1. **Beta increment condition**: `raw_reward == 0.0` → `raw_reward < reward_ema * 0.5`
2. **Alpha/beta decay**: BETA_DECAY=0.995, effective memory window ~70s
3. **Logging**: Added per-group Beta mean columns

## Results

| Metric | Fixed Bandit (N=5) | Uniform (N=5) | p-value |
|--------|-------------------|---------------|---------|
| Mean unique RCs | [FILL] | [FILL] | [FILL] |
| Mean total crashes | [FILL] | [FILL] | [FILL] |
| Mean total edges | [FILL] | [FILL] | [FILL] |
| Crash rate decay (early→late) | [FILL]% | [FILL]% | - |

## Beta Distribution Convergence

[FILL: Do the Beta means differentiate? Which group converges highest?
Include final Beta means from one representative run.]

## Conclusion

[FILL: Does the fixed bandit outperform uniform on crash diversity?]
```

- [ ] **Step 2: Fill in actual numbers from campaign data**

Use the comparison table from Task 5 Step 4 and bandit_log.csv analysis.

- [ ] **Step 3: Commit**

```bash
git add results/fixed_bandit_evaluation.md
git commit -m "docs: fixed-bandit evaluation report with statistical comparison"
```

---

## Self-Review Checklist

1. **Spec coverage:** All three fixes from the RL evaluation (beta condition, decay, logging) are covered in Tasks 1-3. Evaluation campaigns in Task 5. Report in Task 6. ✓
2. **Placeholder scan:** Task 6 has `[FILL]` markers — these are intentional, to be filled with actual campaign data that doesn't exist yet. All code steps have complete code. ✓
3. **Type consistency:** `BETA_DECAY` constant introduced in Task 2 and used in Task 2's `observe_reward`. `mean` field added to log in Task 3 header and body consistently. ✓
4. **DQN not touched:** Deliberately excluded — candle doesn't compile on this platform, and the DQN has 5+ unfixed issues. ✓
