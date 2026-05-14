# Grammar Bandit — Thompson Sampling Weight Adaptation

Runtime adaptation of grammar rule weights using Thompson Sampling, boosting the
non-terminal groups most associated with coverage gains and crash discovery.

---

## What It Does

`GrammarBandit` (in `fuzzer/src/grammar_bandit.rs`) treats the six semantic
groups of grammar non-terminals as arms of a multi-armed bandit. Every
`UPDATE_INTERVAL` (100) executions it samples Beta distributions to select
the most promising group, boosts that group's weights in the thread-local
`Context`, and updates the Beta parameters based on observed coverage and crash
reward. This shifts the fuzzer's generative distribution toward the grammar
regions that produce interesting behavior, without manual tuning.

---

## How to Activate

Pass `--policy bandit` on the fuzzer CLI, or set `policy: "bandit"` in
`config.ron`. No other fields are required.

```bash
timeout "$DURATION" ./target/release/fuzzer -c config.ron --policy bandit
```

One `GrammarBandit` instance is created at startup and shared across all fuzzing
threads behind `Arc<Mutex<GrammarBandit>>`.

---

## Rule Groups

Six semantic groups are hardcoded in `classify_nonterminal()`. Non-terminals not
listed in any group are unaffected by the bandit (their weights remain at their
grammar-defined values).

| Index | `RuleGroup` variant | Non-terminals covered |
|-------|--------------------|-----------------------|
| 0 | `S1SchemaSetup` | `Schema-Setup`, `Create-Table-Stmt`, `Create-Index-Stmt`, `Create-View-Stmt`, `Create-Virtual-Table-Stmt`, `Create-Trigger-Stmt`, `Alter-Table-Stmt`, `Drop-Stmt`, `Col-Def-List-GenCol` |
| 1 | `S2DmlStress` | `Insert-Stmt`, `Update-Stmt`, `Delete-Stmt` |
| 2 | `S3QueryStress` | `Stress-Query`, `Select-Stmt`, `Select-Core` |
| 3 | `S4BoundaryPrintf` | `Boundary-Func-Call`, `Boundary-Int`, `Boundary-Float`, `Format-Spec`, `Printf-Fmt-Spec` |
| 4 | `S5FtsVirtual` | `Fts-Engine` |
| 5 | `S6Validation` | `Validation-Op`, `Pragma-Stmt`, `Analyze-Stmt` |

---

## Thompson Sampling Algorithm

### Beta distribution state

Each group maintains `(alpha, beta)` parameters, initialised to `(1.0, 1.0)` —
an uninformative uniform prior. The Beta mean `alpha / (alpha + beta)` represents
the estimated success probability for that group.

A `BETA_DECAY` factor of `0.995` is applied to both `alpha` and `beta` each
update, decaying parameters toward the prior `(1.0, 1.0)`. This handles
non-stationarity: a group that was good earlier does not dominate indefinitely.

### `select_group()`

Called every `UPDATE_INTERVAL` executions (`grammar_bandit.rs` lines 166–200).

```
for each group i:
    θ_i ~ Beta(alpha_i, beta_i)

best_group = argmax θ_i

for each multiplier m_i:
    m_i = 1.0 + (m_i - 1.0) * DECAY_FACTOR    # DECAY_FACTOR = 0.95

m[best_group] = clamp(m[best_group] * BOOST_MULTIPLIER, 0.01, 100.0)
                                                # BOOST_MULTIPLIER = 2.0
```

All multipliers decay toward `1.0` on every call. The selected group's
multiplier is then boosted by `2.0×`. Clamping to `[0.01, 100.0]` prevents
extreme values from breaking the grammar sampling budget.

### `observe_reward()`

Called immediately before `select_group()` with:
- `coverage_delta` — new coverage edges seen since the last update
- `crash_delta` — new crashes seen since the last update

```
raw_reward = coverage_delta + 10.0 * crash_delta

reward_ema = 0.1 * raw_reward + 0.9 * reward_ema    # EMA α = 0.1

if reward_ema > 0.1:
    normalized = min(raw_reward / reward_ema, 2.0)
else:
    normalized = 1.0 if raw_reward > 0.0 else 0.0

alpha[active_group] += normalized

if reward_ema > 0.1 and raw_reward < reward_ema * 0.5:
    beta[active_group] += 1.0
```

The EMA baseline normalizes reward relative to recent history. A group must
exceed the running average to earn `normalized > 1.0`; below-average performance
(`< 50% of EMA`) also increments `beta`, actively penalizing the group.
Crashes are weighted `10×` heavier than coverage edges.

---

## Reward Formula

```
raw_reward = coverage_delta + 10 * crash_delta
```

EMA normalization (alpha = 0.1) smooths spikes and gives a running baseline.
The `normalized` value fed into Beta update is capped at `2.0` to prevent
a single high-reward round from dominating.

---

## `apply_multipliers()` — Non-Compounding Weight Update

After `select_group()` returns, each fuzzing thread calls
`apply_multipliers(&mut ctx, &bandit, &mults)` (`grammar_bandit.rs` lines
272–283) to update its thread-local `Context`.

The key design decision is **non-compounding**: each rule weight is reset to
`base_weight * multiplier`, not to the previous weight times the multiplier.
`base_weight` is captured at startup from the grammar file and stored in
`GroupState.base_weights`.

```rust
for &(rid, base_w) in bandit.group_base_weights(gi) {
    let new_w = (base_w * m).clamp(WEIGHT_MIN, WEIGHT_MAX);
    ctx.set_weight(rid, new_w);
}
```

This prevents weight runaway: regardless of how many boost steps have
accumulated, a rule can never exceed `base_weight * WEIGHT_MAX` (`100.0`).

---

## Logging — `bandit_log.csv`

Every update writes one row to `$WORKDIR/bandit_log.csv`. The file is created
at `GrammarBandit::new()` with a header line.

CSV columns:
```
update, selected_group,
alpha_S1_Schema, beta_S1_Schema, count_S1_Schema, last_reward_S1_Schema, mean_S1_Schema,
alpha_S2_DML,    beta_S2_DML,    count_S2_DML,    last_reward_S2_DML,    mean_S2_DML,
... (repeated for all 6 groups) ...,
reward_ema, total_coverage
```

`mean` is `alpha / (alpha + beta)` — the current Beta posterior mean for that
group. `count` is the total number of times that group has been selected.

---

## Integration — Threading Model

`GrammarBandit` is created once in `main.rs` when `policy == "bandit"` and
wrapped in `Arc<Mutex<GrammarBandit>>`. Each fuzzing thread holds a clone of
the `Arc`.

The per-thread update loop (in `fuzzing_thread()`, `main.rs` lines 287–309):

```
if exec_count >= last_bandit_exec + UPDATE_INTERVAL:
    bandit_locked = bandit.lock()
    bandit_locked.observe_reward(cov_delta, crash_delta)
    mults = bandit_locked.select_group()
    bandit_locked.log_state(mults.selected, total_coverage)
    drop(bandit_locked)                      # release mutex before weight apply
    apply_multipliers(&mut local_ctx, &bandit_arc.lock(), &mults)
    last_bandit_exec = exec_count
```

The mutex is held only for the `observe_reward` + `select_group` + `log_state`
calls. Weight application operates on the thread's own `Context` copy and does
not require the lock.
