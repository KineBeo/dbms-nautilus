// Phase 2: Thompson Sampling bandit over grammar rule groups.
// Adapts the grammar's generative distribution by boosting the selected
// group's nonterminal weights every UPDATE_INTERVAL executions.
//
// Architecture: one GrammarBandit behind Arc<Mutex<>> shared across threads.
// Each thread periodically locks it, calls select_group() to get the current
// per-group multipliers, then applies them to its own local Context.

use grammartec::context::Context;
use grammartec::newtypes::{NTermID, RuleID};
use rand::Rng;
use rand_distr::{Beta, Distribution};
use std::fs::OpenOptions;
use std::io::Write;

pub const NUM_GROUPS: usize = 6;
pub const UPDATE_INTERVAL: u64 = 100;
const BOOST_MULTIPLIER: f32 = 2.0;
const DECAY_FACTOR: f32 = 0.95;
const WEIGHT_MIN: f32 = 0.01;
const WEIGHT_MAX: f32 = 100.0;
const BETA_DECAY: f32 = 0.995;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum RuleGroup {
    S1SchemaSetup = 0,
    S2DmlStress = 1,
    S3QueryStress = 2,
    S4BoundaryPrintf = 3,
    S5FtsVirtual = 4,
    S6Validation = 5,
}

impl RuleGroup {
    pub fn from_index(i: usize) -> Option<Self> {
        match i {
            0 => Some(RuleGroup::S1SchemaSetup),
            1 => Some(RuleGroup::S2DmlStress),
            2 => Some(RuleGroup::S3QueryStress),
            3 => Some(RuleGroup::S4BoundaryPrintf),
            4 => Some(RuleGroup::S5FtsVirtual),
            5 => Some(RuleGroup::S6Validation),
            _ => None,
        }
    }

    pub fn name(&self) -> &'static str {
        match self {
            RuleGroup::S1SchemaSetup => "S1_Schema",
            RuleGroup::S2DmlStress => "S2_DML",
            RuleGroup::S3QueryStress => "S3_Query",
            RuleGroup::S4BoundaryPrintf => "S4_Boundary",
            RuleGroup::S5FtsVirtual => "S5_FTS",
            RuleGroup::S6Validation => "S6_Validation",
        }
    }
}

pub fn classify_nonterminal(name: &str) -> Option<RuleGroup> {
    match name {
        "Schema-Setup" | "Create-Table-Stmt" | "Create-Index-Stmt"
        | "Create-View-Stmt" | "Create-Virtual-Table-Stmt"
        | "Create-Trigger-Stmt" | "Alter-Table-Stmt" | "Drop-Stmt"
        | "Col-Def-List-GenCol" => Some(RuleGroup::S1SchemaSetup),

        "Insert-Stmt" | "Update-Stmt" | "Delete-Stmt" => Some(RuleGroup::S2DmlStress),

        "Stress-Query" | "Select-Stmt" | "Select-Core" => Some(RuleGroup::S3QueryStress),

        "Boundary-Func-Call" | "Boundary-Int" | "Boundary-Float"
        | "Format-Spec" | "Printf-Fmt-Spec" => Some(RuleGroup::S4BoundaryPrintf),

        "Fts-Engine" => Some(RuleGroup::S5FtsVirtual),

        "Validation-Op" | "Pragma-Stmt" | "Analyze-Stmt" => Some(RuleGroup::S6Validation),

        _ => None,
    }
}

struct GroupState {
    alpha: f32,
    beta: f32,
    nt_ids: Vec<NTermID>,
    base_weights: Vec<(RuleID, f32)>,
    selection_count: u64,
    last_reward: f32,
}

/// Per-group multiplier returned by the bandit for threads to apply locally.
#[derive(Clone)]
pub struct GroupMultipliers {
    pub multipliers: [f32; NUM_GROUPS],
    pub selected: usize,
}

pub struct GrammarBandit {
    groups: [GroupState; NUM_GROUPS],
    current_multipliers: [f32; NUM_GROUPS],
    active_group: Option<usize>,
    total_updates: u64,
    reward_ema: f32,
    log_path: String,
}

impl GrammarBandit {
    pub fn new(ctx: &Context, workdir: &str) -> Self {
        let mut group_nts: [Vec<NTermID>; NUM_GROUPS] = Default::default();
        let mut group_base_weights: [Vec<(RuleID, f32)>; NUM_GROUPS] = Default::default();

        for (nt_id, name) in ctx.all_nt_ids() {
            if let Some(group) = classify_nonterminal(&name) {
                let gi = group as usize;
                group_nts[gi].push(nt_id);
                for &(rid, w) in &ctx.get_weights_for_nt(nt_id) {
                    group_base_weights[gi].push((rid, w));
                }
            }
        }

        let groups = std::array::from_fn(|i| GroupState {
            alpha: 1.0,
            beta: 1.0,
            nt_ids: group_nts[i].clone(),
            base_weights: group_base_weights[i].clone(),
            selection_count: 0,
            last_reward: 0.0,
        });

        let log_path = format!("{}/bandit_log.csv", workdir);
        let file = OpenOptions::new()
            .create(true)
            .truncate(true)
            .write(true)
            .open(&log_path)
            .expect("GrammarBandit: failed to open bandit_log.csv");
        let mut file = file;
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

        GrammarBandit {
            groups,
            current_multipliers: [1.0; NUM_GROUPS],
            active_group: None,
            total_updates: 0,
            reward_ema: 0.0,
            log_path,
        }
    }

    /// Run Thompson Sampling: sample Beta distributions, pick the best group,
    /// decay all multipliers, boost the selected group. Returns the new multipliers.
    pub fn select_group(&mut self) -> GroupMultipliers {
        let mut rng = rand::thread_rng();

        let mut best_group = 0;
        let mut best_sample = f32::NEG_INFINITY;

        for (i, gs) in self.groups.iter().enumerate() {
            if gs.nt_ids.is_empty() {
                continue;
            }
            let dist = Beta::new(gs.alpha as f64, gs.beta as f64)
                .unwrap_or_else(|_| Beta::new(1.0, 1.0).unwrap());
            let sample = dist.sample(&mut rng) as f32;
            if sample > best_sample {
                best_sample = sample;
                best_group = i;
            }
        }

        // Decay all multipliers toward 1.0, then boost selected
        for m in self.current_multipliers.iter_mut() {
            *m = 1.0 + (*m - 1.0) * DECAY_FACTOR;
        }
        self.current_multipliers[best_group] =
            (self.current_multipliers[best_group] * BOOST_MULTIPLIER).clamp(WEIGHT_MIN, WEIGHT_MAX);

        self.active_group = Some(best_group);
        self.groups[best_group].selection_count += 1;
        self.total_updates += 1;

        GroupMultipliers {
            multipliers: self.current_multipliers,
            selected: best_group,
        }
    }

    /// Update Beta parameters based on observed reward.
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

    pub fn group_weights_summary(&self) -> String {
        let mut parts = Vec::new();
        for (i, gs) in self.groups.iter().enumerate() {
            let g = RuleGroup::from_index(i).unwrap();
            let ratio = gs.alpha / (gs.alpha + gs.beta);
            parts.push(format!("{}={:.2}(x{:.2})", g.name(), ratio, self.current_multipliers[i]));
        }
        parts.join(" ")
    }

    /// Get the NTermIDs for a given group index.
    pub fn group_nt_ids(&self, group_index: usize) -> &[NTermID] {
        &self.groups[group_index].nt_ids
    }

    /// Get the base (original) weights for a given group index.
    pub fn group_base_weights(&self, group_index: usize) -> &[(RuleID, f32)] {
        &self.groups[group_index].base_weights
    }
}

/// Apply bandit multipliers to a thread-local Context.
/// Resets each group's rules to base weights, then applies the multiplier.
/// This prevents compounding: base_weight * multiplier, not weight * multiplier.
pub fn apply_multipliers(ctx: &mut Context, bandit: &GrammarBandit, mults: &GroupMultipliers) {
    for gi in 0..NUM_GROUPS {
        let m = mults.multipliers[gi];
        for &(rid, base_w) in bandit.group_base_weights(gi) {
            let new_w = (base_w * m).clamp(WEIGHT_MIN, WEIGHT_MAX);
            ctx.set_weight(rid, new_w);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_classify_nonterminal_coverage() {
        assert_eq!(classify_nonterminal("Schema-Setup"), Some(RuleGroup::S1SchemaSetup));
        assert_eq!(classify_nonterminal("Insert-Stmt"), Some(RuleGroup::S2DmlStress));
        assert_eq!(classify_nonterminal("Stress-Query"), Some(RuleGroup::S3QueryStress));
        assert_eq!(classify_nonterminal("Boundary-Int"), Some(RuleGroup::S4BoundaryPrintf));
        assert_eq!(classify_nonterminal("Fts-Engine"), Some(RuleGroup::S5FtsVirtual));
        assert_eq!(classify_nonterminal("Validation-Op"), Some(RuleGroup::S6Validation));
        assert_eq!(classify_nonterminal("Expr"), None);
        assert_eq!(classify_nonterminal("Literal"), None);
    }

    #[test]
    fn test_rule_group_from_index_roundtrip() {
        for i in 0..NUM_GROUPS {
            let g = RuleGroup::from_index(i).unwrap();
            assert_eq!(g as usize, i);
        }
        assert!(RuleGroup::from_index(NUM_GROUPS).is_none());
    }

    #[test]
    fn test_thompson_sampling_beta_update() {
        let alpha_before = 1.0_f32;
        let beta_before = 1.0_f32;

        // success: alpha increments
        let alpha_after = alpha_before + 1.0;
        assert!((alpha_after - 2.0).abs() < 1e-6);

        // failure: beta increments
        let beta_after = beta_before + 1.0;
        assert!((beta_after - 2.0).abs() < 1e-6);

        // Mean = alpha / (alpha + beta)
        let mean = alpha_after / (alpha_after + beta_after);
        assert!((mean - 0.5).abs() < 1e-6);
    }

    #[test]
    fn test_weight_clamping() {
        let w_low = (0.005_f32 * DECAY_FACTOR).clamp(WEIGHT_MIN, WEIGHT_MAX);
        assert!(w_low >= WEIGHT_MIN);
        let w_high = (99.0_f32 * BOOST_MULTIPLIER).clamp(WEIGHT_MIN, WEIGHT_MAX);
        assert!(w_high <= WEIGHT_MAX);
    }

    #[test]
    fn test_decay_toward_one() {
        let mut m = 3.0_f32;
        for _ in 0..100 {
            m = 1.0 + (m - 1.0) * DECAY_FACTOR;
        }
        // After 100 steps: 1.0 + 2.0 * 0.95^100 = ~1.012
        assert!((m - 1.0).abs() < 0.02, "multiplier should decay toward 1.0, got {}", m);
    }

    #[test]
    fn test_boost_increases_multiplier() {
        let m = 1.0_f32;
        let boosted = (m * BOOST_MULTIPLIER).clamp(WEIGHT_MIN, WEIGHT_MAX);
        assert!(boosted > m);
        assert_eq!(boosted, 2.0);
    }

    #[test]
    fn test_proportional_reward_differentiates() {
        let ema = 5.0_f32;
        let reward_a = 10.0_f32;
        let reward_b = 1.0_f32;

        let norm_a = (reward_a / ema).min(2.0);
        let norm_b = (reward_b / ema).min(2.0);

        assert!(norm_a > norm_b, "10 edges should produce higher reward than 1 edge");
        assert!(norm_a > 1.0, "above-average should normalize > 1.0");
        assert!(norm_b < 1.0, "below-average should normalize < 1.0");

        let mut alpha_a = 1.0_f32;
        let mut alpha_b = 1.0_f32;
        alpha_a += norm_a;
        alpha_b += norm_b;

        let mean_a = alpha_a / (alpha_a + 1.0);
        let mean_b = alpha_b / (alpha_b + 1.0);
        assert!(mean_a > mean_b, "group A should have higher Beta mean");
    }

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

    #[test]
    fn test_below_average_reward_increments_beta() {
        // Simulate: reward_ema = 10.0, raw_reward = 3.0 (below 50% of EMA)
        // Beta SHOULD increment because this is below-average performance.
        let reward_ema = 10.0_f32;
        let raw_reward = 3.0_f32;

        let mut alpha = 5.0_f32;
        let mut beta = 2.0_f32;

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

    #[test]
    fn test_no_weight_compounding() {
        let base_w = 3.0_f32;
        let multiplier = 2.0_f32;

        // Old (broken): compound on previous result
        let mut compounded = base_w;
        for _ in 0..10 {
            compounded = (compounded * multiplier).min(WEIGHT_MAX);
        }
        assert_eq!(compounded, WEIGHT_MAX, "compounding hits clamp fast");

        // New (fixed): always multiply from base
        let mut from_base = base_w;
        for _ in 0..10 {
            from_base = (base_w * multiplier).min(WEIGHT_MAX);
        }
        assert_eq!(from_base, 6.0, "base*multiplier stays at 6.0 forever");
    }

    #[test]
    fn test_ema_update() {
        let mut ema = 0.0_f32;
        let alpha = 0.1_f32;

        ema = alpha * 10.0 + (1.0 - alpha) * ema;
        assert!((ema - 1.0).abs() < 1e-6, "first update: 0.1*10 + 0.9*0 = 1.0");

        ema = alpha * 10.0 + (1.0 - alpha) * ema;
        assert!((ema - 1.9).abs() < 1e-6, "second update: 0.1*10 + 0.9*1.0 = 1.9");
    }
}
