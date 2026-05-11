# Proportional Reward Bandit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the bandit reward signal from binary (0/1) to proportional (number of new edges), fix the crash-tracking bug, and add a normalized reward with EMA smoothing so the bandit can differentiate productive groups at 30-minute timescales.

**Architecture:** Three changes to `grammar_bandit.rs` (reward computation, Beta update scaling, CSV logging) and one bugfix in `main.rs` (crash delta tracking). The Beta distribution update switches from `alpha += 1.0` to `alpha += normalized_reward` where the reward is the edge delta normalized by a running EMA of recent rewards. This makes the Beta parameters reflect actual productivity differences, not just "did anything happen."

**Tech Stack:** Rust (fuzzer crate), no new dependencies.

---

## Problem Analysis

Three issues found in the current implementation:

1. **Binary reward** (`grammar_bandit.rs:190`): `observe_reward` converts coverage_delta to binary 0/1. When every group finds at least 1 new edge per 100 execs, all groups look identical to the bandit. It can't tell "S4 found 12 edges" from "S1 found 1 edge."

2. **Crash tracking bug** (`main.rs:295`): `is_crash` is `total_crashes > 0`, which is always true after the first crash. Should be a delta (new crashes since last update), like coverage.

3. **No reward normalization**: Raw edge counts vary wildly (0-50+ per interval). Beta distributions need rewards in [0, 1] range to update meaningfully. We need to normalize by dividing by a running EMA of recent rewards.

## File Structure

```
fuzzer/src/grammar_bandit.rs  — Modify: reward computation, Beta update, CSV logging
fuzzer/src/main.rs            — Modify: crash delta tracking, pass raw edge count
```

No new files. No dependency changes.

---

### Task 1: Fix crash delta tracking in main.rs

**Files:**
- Modify: `fuzzer/src/main.rs:227-307` (bandit integration block)

- [ ] **Step 1: Add `last_bandit_crashes` tracking variable**

In `main.rs`, find the bandit tracking variables at line 227-228:

```rust
    let mut last_bandit_exec = 0_u64;
    let mut last_bandit_coverage = 0_usize;
```

Change to:

```rust
    let mut last_bandit_exec = 0_u64;
    let mut last_bandit_coverage = 0_usize;
    let mut last_bandit_crashes = 0_u64;
```

- [ ] **Step 2: Fix crash delta computation and pass raw coverage_delta**

Find the bandit update block (around line 286-307). Replace this section:

```rust
                let cov_delta = total_cov.saturating_sub(last_bandit_coverage);
                let is_crash = total_crashes > 0;

                let mut bandit = bandit_arc.lock().expect("bandit_lock");
                bandit.observe_reward(cov_delta, is_crash);
                let mults = bandit.select_group();
                let reward = if cov_delta > 0 || is_crash { 1.0 } else { 0.0 };
                bandit.log_state(mults.selected, reward, total_cov);

                // Apply multipliers to this thread's local Context
                grammar_bandit::apply_multipliers(&mut state.ctx, &bandit, &mults);

                last_bandit_exec = exec;
                last_bandit_coverage = total_cov;
```

With:

```rust
                let cov_delta = total_cov.saturating_sub(last_bandit_coverage);
                let crash_delta = total_crashes.saturating_sub(last_bandit_crashes);

                let mut bandit = bandit_arc.lock().expect("bandit_lock");
                bandit.observe_reward(cov_delta, crash_delta);
                let mults = bandit.select_group();
                bandit.log_state(mults.selected, total_cov);

                // Apply multipliers to this thread's local Context
                grammar_bandit::apply_multipliers(&mut state.ctx, &bandit, &mults);

                last_bandit_exec = exec;
                last_bandit_coverage = total_cov;
                last_bandit_crashes = total_crashes;
```

- [ ] **Step 3: Verify it compiles**

Run: `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo check -p fuzzer 2>&1 | grep -E "error|warning.*grammar_bandit|warning.*main"`

Expected: Errors about `observe_reward` and `log_state` signature mismatch (we haven't updated those yet). That's correct -- Task 2 fixes them.

---

### Task 2: Change observe_reward to proportional with EMA normalization

**Files:**
- Modify: `fuzzer/src/grammar_bandit.rs:80-86` (GroupState struct)
- Modify: `fuzzer/src/grammar_bandit.rs:94-100` (GrammarBandit struct)
- Modify: `fuzzer/src/grammar_bandit.rs:112` (GrammarBandit::new initializer)
- Modify: `fuzzer/src/grammar_bandit.rs:187-194` (observe_reward method)

- [ ] **Step 1: Write the failing test for proportional reward**

Add this test at the end of the `mod tests` block in `grammar_bandit.rs` (before the closing `}`):

```rust
    #[test]
    fn test_proportional_reward_differentiates() {
        // Simulate: group A finds 10 edges, group B finds 1 edge
        // After normalization, group A should have higher alpha
        let ema = 5.0_f32; // running average
        let reward_a = 10.0_f32;
        let reward_b = 1.0_f32;

        let norm_a = (reward_a / ema).min(2.0);
        let norm_b = (reward_b / ema).min(2.0);

        assert!(norm_a > norm_b, "10 edges should produce higher reward than 1 edge");
        assert!(norm_a > 1.0, "above-average should normalize > 1.0");
        assert!(norm_b < 1.0, "below-average should normalize < 1.0");

        // Simulate Beta updates
        let mut alpha_a = 1.0_f32;
        let mut alpha_b = 1.0_f32;
        alpha_a += norm_a;
        alpha_b += norm_b;

        let mean_a = alpha_a / (alpha_a + 1.0); // beta stays at 1.0 for simplicity
        let mean_b = alpha_b / (alpha_b + 1.0);
        assert!(mean_a > mean_b, "group A should have higher Beta mean");
    }

    #[test]
    fn test_zero_reward_increments_beta() {
        let alpha_before = 5.0_f32;
        let beta_before = 2.0_f32;

        // Zero coverage delta and zero crashes
        let norm_reward = 0.0_f32;
        let alpha_after = alpha_before + norm_reward;
        let beta_after = beta_before + 1.0;

        assert_eq!(alpha_after, alpha_before, "alpha unchanged on zero reward");
        assert_eq!(beta_after, 3.0, "beta increments on zero reward");
    }

    #[test]
    fn test_ema_update() {
        let mut ema = 0.0_f32;
        let alpha = 0.1_f32;

        // First observation: 10 edges
        ema = alpha * 10.0 + (1.0 - alpha) * ema;
        assert!((ema - 1.0).abs() < 1e-6, "first update: 0.1*10 + 0.9*0 = 1.0");

        // Second observation: 10 edges
        ema = alpha * 10.0 + (1.0 - alpha) * ema;
        assert!((ema - 1.9).abs() < 1e-6, "second update: 0.1*10 + 0.9*1.0 = 1.9");
    }
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo test -p fuzzer --release -- grammar_bandit::tests::test_proportional 2>&1 | tail -5`

Expected: PASS (these are pure math tests, no dependency on implementation yet). They validate the math we're about to implement.

- [ ] **Step 3: Add reward_ema field to GrammarBandit struct and last_reward to GroupState**

Replace the `GroupState` struct (line 80-85):

```rust
struct GroupState {
    alpha: f32,
    beta: f32,
    nt_ids: Vec<NTermID>,
    selection_count: u64,
}
```

With:

```rust
struct GroupState {
    alpha: f32,
    beta: f32,
    nt_ids: Vec<NTermID>,
    selection_count: u64,
    last_reward: f32,
}
```

Add `reward_ema` to the `GrammarBandit` struct (line 94-100):

```rust
pub struct GrammarBandit {
    groups: [GroupState; NUM_GROUPS],
    current_multipliers: [f32; NUM_GROUPS],
    active_group: Option<usize>,
    total_updates: u64,
    reward_ema: f32,
    log_path: String,
}
```

- [ ] **Step 4: Update the initializer**

In `GrammarBandit::new`, update the `GroupState` initializer (inside `std::array::from_fn`) to include `last_reward: 0.0`:

```rust
        let groups = std::array::from_fn(|i| GroupState {
            alpha: 1.0,
            beta: 1.0,
            nt_ids: group_nts[i].clone(),
            selection_count: 0,
            last_reward: 0.0,
        });
```

And update the `GrammarBandit` return to include `reward_ema: 0.0`:

```rust
        GrammarBandit {
            groups,
            current_multipliers: [1.0; NUM_GROUPS],
            active_group: None,
            total_updates: 0,
            reward_ema: 0.0,
            log_path,
        }
```

- [ ] **Step 5: Rewrite observe_reward with proportional + EMA normalization**

Replace the `observe_reward` method (line 187-194):

```rust
    /// Update Beta parameters based on observed reward.
    pub fn observe_reward(&mut self, coverage_delta: usize, is_crash: bool) {
        if let Some(gi) = self.active_group {
            let reward = if coverage_delta > 0 || is_crash { 1.0 } else { 0.0 };
            self.groups[gi].alpha += reward;
            self.groups[gi].beta += 1.0 - reward;
        }
    }
```

With:

```rust
    /// Update Beta parameters with proportional reward.
    /// Raw reward = coverage_delta + 10*crash_delta (crashes are rare and valuable).
    /// Normalized by a running EMA so the Beta update stays in a useful range.
    pub fn observe_reward(&mut self, coverage_delta: usize, crash_delta: u64) {
        if let Some(gi) = self.active_group {
            let raw_reward = coverage_delta as f32 + 10.0 * crash_delta as f32;

            // Update EMA (exponential moving average of raw rewards)
            const EMA_ALPHA: f32 = 0.1;
            self.reward_ema = EMA_ALPHA * raw_reward + (1.0 - EMA_ALPHA) * self.reward_ema;

            // Normalize: reward / EMA, clamped to [0, 2.0]
            // Above-average performance -> normalized > 1.0 -> alpha grows faster
            // Below-average -> normalized < 1.0 -> alpha grows slower
            let normalized = if self.reward_ema > 0.1 {
                (raw_reward / self.reward_ema).min(2.0)
            } else {
                if raw_reward > 0.0 { 1.0 } else { 0.0 }
            };

            self.groups[gi].alpha += normalized;
            if raw_reward == 0.0 {
                self.groups[gi].beta += 1.0;
            }
            self.groups[gi].last_reward = raw_reward;
        }
    }
```

- [ ] **Step 6: Run tests to verify everything passes**

Run: `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo test -p fuzzer --release -- grammar_bandit 2>&1 | tail -10`

Expected: All 9 tests pass.

- [ ] **Step 7: Commit**

```bash
git add fuzzer/src/grammar_bandit.rs fuzzer/src/main.rs
git commit -m "fix(bandit): proportional reward with EMA normalization, fix crash delta bug

Changes binary reward (0/1) to proportional (edge_delta + 10*crash_delta),
normalized by running EMA. Groups that find more new edges get higher
alpha increments. Zero-reward intervals now properly increment beta.

Fixes: crash tracking used cumulative total instead of delta, so
is_crash was always true after the first crash."
```

---

### Task 3: Update CSV logging to show the new reward fields

**Files:**
- Modify: `fuzzer/src/grammar_bandit.rs:197-211` (log_state method)

- [ ] **Step 1: Update log_state signature and CSV header**

The `log_state` method currently takes `reward: f32` from the caller. Change it to read from internal state so the caller doesn't need to compute it.

Replace the CSV header in `GrammarBandit::new` (the `writeln!` block around line 133-138):

```rust
        let group_headers: Vec<String> = (0..NUM_GROUPS)
            .map(|i| {
                let g = RuleGroup::from_index(i).unwrap();
                format!("alpha_{0},beta_{0},count_{0},last_reward_{0}", g.name())
            })
            .collect();
        writeln!(
            file,
            "update,selected_group,{},reward_ema,total_coverage",
            group_headers.join(",")
        )
        .expect("GrammarBandit: failed to write CSV header");
```

- [ ] **Step 2: Update log_state method**

Replace the `log_state` method:

```rust
    /// Log current state to CSV.
    pub fn log_state(&self, selected: usize, total_coverage: usize) {
        let mut line = format!(
            "{},{}", self.total_updates,
            RuleGroup::from_index(selected).unwrap().name()
        );
        for gs in &self.groups {
            line.push_str(&format!(",{:.4},{:.4},{},{:.2}", gs.alpha, gs.beta, gs.selection_count, gs.last_reward));
        }
        line.push_str(&format!(",{:.4},{}", self.reward_ema, total_coverage));
        line.push('\n');

        if let Ok(mut file) = OpenOptions::new().append(true).open(&self.log_path) {
            let _ = file.write_all(line.as_bytes());
        }
    }
```

- [ ] **Step 3: Build and verify**

Run: `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release 2>&1 | grep -E "error|Finished"`

Expected: `Finished` with no errors.

- [ ] **Step 4: Run all tests**

Run: `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo test -p fuzzer --release -- grammar_bandit 2>&1 | tail -5`

Expected: `test result: ok. 9 passed; 0 failed`

- [ ] **Step 5: Commit**

```bash
git add fuzzer/src/grammar_bandit.rs
git commit -m "feat(bandit): update CSV logging with per-group last_reward and reward_ema"
```

---

### Task 4: Smoke test to verify differentiation

**Files:**
- No code changes. Validation only.

- [ ] **Step 1: Run 15-min bandit smoke test**

```bash
DURATION=900 POLICY=bandit GRAMMAR=$(pwd)/grammars/active/sqlite_v3.py \
  GRAMMAR_VERSION=v3.3-proportional \
  bash scripts/run_eval.sh sqlite-3.31.1 smoke_proportional \
  > /tmp/smoke_proportional.log 2>&1
```

- [ ] **Step 2: Check that beta values are no longer all 1.0**

```bash
WORKDIR=workdirs/sqlite-3.31.1_smoke_proportional
echo "=== Last 5 bandit log rows ==="
tail -5 "$WORKDIR/bandit_log.csv"
echo ""
echo "=== Coverage ==="
tail -1 "$WORKDIR/coverage.csv"
```

Expected: Beta columns should show values > 1.0 for at least some groups (meaning the bandit detected zero-reward intervals). Alpha values should differ between groups (meaning the bandit is giving proportionally more credit to productive groups).

Success criteria:
- Alpha values across groups differ by at least 2x between highest and lowest
- At least one group has beta > 5.0 (experienced zero-reward intervals)
- Coverage is within 10% of previous smoke test (~20,000 edges)

- [ ] **Step 3: Compare bandit log with old binary reward**

```bash
echo "=== OLD (binary reward) ==="
tail -1 workdirs/sqlite-3.31.1_smoke_bandit/bandit_log.csv
echo ""
echo "=== NEW (proportional reward) ==="
tail -1 "$WORKDIR/bandit_log.csv"
```

The old log should show all alpha >> beta (everything rewarded). The new log should show differentiation between groups.

---

### Task 5: Run comparison campaigns (N=5, 30 min, 2 versions)

**Files:**
- No code changes. Campaign runs only.

- [ ] **Step 1: Run campaigns on sqlite-3.31.1 (most data for comparison)**

```bash
for RUN in 1 2 3 4 5; do
  DURATION=1800 POLICY=bandit GRAMMAR=$(pwd)/grammars/active/sqlite_v3.py \
    GRAMMAR_VERSION=v3.3-proportional \
    bash scripts/run_eval.sh sqlite-3.31.1 "proportional_run${RUN}" \
    > "/tmp/campaign_3.31.1_proportional_run${RUN}.log" 2>&1
  echo "Run $RUN done: $(tail -1 workdirs/sqlite-3.31.1_proportional_run${RUN}/coverage.csv)"
done
```

- [ ] **Step 2: Run campaigns on sqlite-3.32.0 (second version)**

```bash
for RUN in 1 2 3 4 5; do
  DURATION=1800 POLICY=bandit GRAMMAR=$(pwd)/grammars/active/sqlite_v3.py \
    GRAMMAR_VERSION=v3.3-proportional \
    bash scripts/run_eval.sh sqlite-3.32.0 "proportional_run${RUN}" \
    > "/tmp/campaign_3.32.0_proportional_run${RUN}.log" 2>&1
  echo "Run $RUN done: $(tail -1 workdirs/sqlite-3.32.0_proportional_run${RUN}/coverage.csv)"
done
```

- [ ] **Step 3: Compare three-way: uniform vs binary-bandit vs proportional-bandit**

Collect final edge counts from all three:

```bash
echo "=== sqlite-3.31.1 comparison ==="
echo "Uniform (existing):"
for d in workdirs/sqlite-3.31.1_uniform_run*/coverage.csv; do tail -1 "$d" | cut -d, -f2; done | paste -sd' '
echo "Binary bandit (existing):"
for d in workdirs/sqlite-3.31.1_bandit_run*/coverage.csv; do tail -1 "$d" | cut -d, -f2; done | paste -sd' '
echo "Proportional bandit (new):"
for d in workdirs/sqlite-3.31.1_proportional_run*/coverage.csv; do tail -1 "$d" | cut -d, -f2; done | paste -sd' '
```

Success criteria for the proportional bandit:
- Mean edges >= uniform mean edges (ideally 1-3% higher)
- OR: mean edges comparable but mean crashes higher
- OR: coverage velocity faster in first 10 minutes (visible in coverage.csv time series)
- If none of the above: negative result is still defensible for thesis

---

## Summary of Changes

| File | What changes | Lines affected |
|------|-------------|----------------|
| `fuzzer/src/grammar_bandit.rs` | Proportional reward, EMA normalization, CSV logging, 3 new tests | ~40 lines modified |
| `fuzzer/src/main.rs` | Crash delta tracking, pass raw values to observe_reward | ~10 lines modified |

Total: ~50 lines of code changes + 3 new tests + campaign runs.
