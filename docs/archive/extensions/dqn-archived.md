# DQN Agent — Archived Design Reference

> **Archived:** DQN code was removed on 2026-05-14. This document preserves
> the design for reference. The `MutationPolicy` trait remains in
> `fuzzer/src/rl_hook.rs` for future RL integration.

The DQN agent was a neural-network-backed mutation strategy selector. It was
included in Phase 2 to validate the RL integration architecture but was never
used in thesis campaigns (all campaigns ran under `uniform` or `bandit` policy).
Code was removed to reduce build times and narrow the thesis scope.

---

## `MutationPolicy` Trait

The trait remains in `fuzzer/src/rl_hook.rs` and is implemented by any policy
that selects mutation strategies at runtime.

```rust
pub trait MutationPolicy {
    /// Select a mutation action. Returns None to run all strategies (default),
    /// or Some(action_index) to run exactly one.
    fn select_action(&mut self, ctx: &PolicyContext) -> Option<u8>;

    /// Observe the outcome of the last action for learning.
    fn observe(&mut self, action: u8, ctx: &PolicyContext);
}
```

`DefaultPolicy` implements this trait by always returning `None`, causing
`process_input()` to run all three strategies (splice, havoc, havoc_recursion)
unconditionally.

`PolicyContext` carries the snapshot of fuzzer state available at decision
time: `coverage_delta`, `crash_delta`, `queue_size`, `exec_count`.

---

## `DqnPolicy` — Removed Design

`DqnPolicy` (in `fuzzer/src/rl_hook.rs`) wrapped a `DqnWorker` backed by a
shared `DqnTrainer` (in `fuzzer/src/dqn.rs`).

### State vector — `DqnState` (12 dimensions)

| Index | Feature |
|-------|---------|
| 0 | Coverage delta (edges discovered this step) |
| 1 | Total coverage (all edges discovered so far) |
| 2 | Crash indicator (1.0 if crash, 0.0 otherwise) |
| 3 | Queue size |
| 4 | Exec count |
| 5–11 | Per-strategy reward EMAs (one per mutation strategy) |

The state was normalized before passing to the network.

### Action space — 5 Q-values

| Action index | Mutation strategy |
|---|---|
| 0 | `havoc` (`Mutator::mut_random()`) |
| 1 | `havoc_recursion` (`Mutator::mut_random_recursion()`) |
| 2 | `splice` (`Mutator::mut_splice()`) |
| 3 | `deterministic_tree_mutation` (`Mutator::mut_rules()`) |
| 4 | `generate_random` (fresh tree from grammar) |

`select_action()` fed the 12-dimensional `DqnState` through the online network
and returned `argmax Q(s, a)` — or a random action index during exploration.

### Training — epsilon-greedy with experience replay

Exploration used a linear epsilon schedule: `ε` decayed from `epsilon_start`
(1.0, fully random) to `epsilon_end` (0.05) over `epsilon_decay` steps.

Transitions `(state, action, reward, next_state)` were stored in a circular
replay buffer of capacity `rl_replay_size` (3000). Every `rl_train_interval`
(100) executions, a mini-batch of `rl_batch_size` (32) transitions was sampled
and used to update the online network via AdamW (from `candle-nn`) with
learning rate `rl_lr` (0.001).

The Bellman target used a separate frozen target network, copied from the online
network every `rl_target_update` (1000) training steps:

```
Q_target = r + γ * max_a' Q_target(s', a')    # γ = rl_gamma = 0.99
```

### Reward — `compute_reward()`

```
reward = coverage_delta + 10.0 * crash_delta
```

Same formula as `GrammarBandit.observe_reward()`, but fed directly into the
Bellman target rather than into a Beta distribution.

---

## Config Fields (removed from `config.rs`)

These fields no longer exist in `Config`. They are documented here for
reproducing the original DQN design if needed.

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `rl_enabled` | `bool` | `false` | Enable DQN policy; skips Det phase when true |
| `rl_epsilon_start` | `f32` | `1.0` | Initial exploration rate |
| `rl_epsilon_end` | `f32` | `0.05` | Final exploration rate |
| `rl_epsilon_decay` | `u64` | `50000` | Decay steps |
| `rl_batch_size` | `usize` | `32` | Mini-batch size per training step |
| `rl_replay_size` | `usize` | `3000` | Replay buffer capacity |
| `rl_gamma` | `f32` | `0.99` | Bellman discount factor |
| `rl_lr` | `f32` | `0.001` | AdamW learning rate |
| `rl_target_update` | `u64` | `1000` | Steps between target network sync |
| `rl_train_interval` | `u64` | `100` | Execs between training calls |

---

## Why It Was Removed

- No thesis campaigns used `--policy dqn`. All Phase 2 evaluation results are
  from `uniform` and `bandit` policies.
- `candle-core` and `candle-nn` (0.9) added significant build time with no
  campaign benefit.
- GitNexus impact analysis confirmed zero upstream dependencies and zero
  execution flows affected by removal (all DQN symbols had `LOW` risk).
- The `MutationPolicy` trait and `DefaultPolicy` were preserved. A future RL
  agent can implement `MutationPolicy` and plug in without modifying the
  fuzzer core.
