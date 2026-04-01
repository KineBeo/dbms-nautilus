// Nautilus
// Copyright (C) 2024  Daniel Teuchert, Cornelius Aschermann, Sergej Schumilo

// ---- default helpers for RL hyperparameters ----

fn default_rl_epsilon_start() -> f32 {
    1.0
}
fn default_rl_epsilon_end() -> f32 {
    0.05
}
fn default_rl_epsilon_decay() -> u64 {
    50_000
}
fn default_rl_batch_size() -> usize {
    32
}
fn default_rl_replay_size() -> usize {
    3000
}
fn default_rl_gamma() -> f32 {
    0.99
}
fn default_rl_lr() -> f32 {
    0.001
}
fn default_rl_target_update() -> u64 {
    1000
}
fn default_rl_train_interval() -> u64 {
    100
}

#[derive(Deserialize, Clone)]
pub struct Config {
    pub number_of_threads: u8,
    pub thread_size: usize,
    pub number_of_generate_inputs: u16,
    pub number_of_deterministic_mutations: usize,
    pub max_tree_size: usize,
    pub bitmap_size: usize,
    pub timeout_in_millis: u64,
    pub path_to_bin_target: String,
    pub path_to_grammar: String,
    pub path_to_workdir: String,
    pub arguments: Vec<String>,
    // Phase 2 hook: when true, RL policy controls mutation selection
    #[serde(default)]
    pub rl_enabled: bool,

    // ---- RL hyperparameters (all optional; backward-compatible with existing .ron configs) ----

    /// Starting epsilon for epsilon-greedy exploration (default 1.0)
    #[serde(default = "default_rl_epsilon_start")]
    pub rl_epsilon_start: f32,

    /// Final epsilon after decay (default 0.05)
    #[serde(default = "default_rl_epsilon_end")]
    pub rl_epsilon_end: f32,

    /// Number of steps over which epsilon decays from start to end (default 50 000)
    #[serde(default = "default_rl_epsilon_decay")]
    pub rl_epsilon_decay: u64,

    /// Mini-batch size for DQN training steps (default 32)
    #[serde(default = "default_rl_batch_size")]
    pub rl_batch_size: usize,

    /// Replay buffer capacity (default 3 000)
    #[serde(default = "default_rl_replay_size")]
    pub rl_replay_size: usize,

    /// Discount factor γ (default 0.99)
    #[serde(default = "default_rl_gamma")]
    pub rl_gamma: f32,

    /// AdamW learning rate (default 0.001)
    #[serde(default = "default_rl_lr")]
    pub rl_lr: f32,

    /// How often (in train steps) to copy online → target network (default 1 000)
    #[serde(default = "default_rl_target_update")]
    pub rl_target_update: u64,

    /// How often (in exec steps) to run a training step (default 100)
    #[serde(default = "default_rl_train_interval")]
    pub rl_train_interval: u64,
}
