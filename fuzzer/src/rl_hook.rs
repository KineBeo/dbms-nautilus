// Phase 2 hook: MutationPolicy trait + DqnPolicy implementation
// Phase 1: DefaultPolicy is a no-op. Phase 2 swaps in DqnPolicy.

use std::sync::{Arc, Mutex};

use crate::dqn::{compute_reward, DqnConfig, DqnState, DqnTrainer, DqnWorker, STATE_DIM};
use crate::rl_logger::RlLogger;

pub struct PolicyContext {
    pub coverage_delta: usize,
    pub is_crash: bool,
    pub is_timeout: bool,
    pub total_coverage: usize,
    pub exec_count: u64,
    pub queue_size: usize,
    pub strategy_emas: [f32; 5], // per-strategy reward EMAs
    pub last_action: Option<u8>,
}

/// RL mutation policy interface. Phase 2 implements this with a DQN agent.
pub trait MutationPolicy: Send {
    /// Select an action (mutation strategy index). Returns None for default behaviour.
    fn select_action(&mut self, _ctx: &PolicyContext) -> Option<u8> {
        None
    }

    /// Observe the outcome of the last action for RL learning.
    fn observe(&mut self, _action: u8, _ctx: &PolicyContext) {}
}

/// Phase 1: no-op policy — Nautilus uses its normal mutation pipeline.
pub struct DefaultPolicy;

impl MutationPolicy for DefaultPolicy {}

// ---------------------------------------------------------------------------
// Phase 2: DQN-backed policy
// ---------------------------------------------------------------------------

/// Converts a `PolicyContext` to the `DqnState` used by the neural network.
fn ctx_to_dqn_state(ctx: &PolicyContext) -> DqnState {
    DqnState {
        coverage_delta: ctx.coverage_delta as f32 / 100.0,
        total_coverage: ctx.total_coverage as f32 / 262144.0,
        coverage_velocity: 0.0, // Phase 2 stub; wired in P2-13
        is_crash: if ctx.is_crash { 1.0 } else { 0.0 },
        crash_rate: 0.0, // Phase 2 stub
        queue_size_norm: ctx.queue_size as f32 / 10000.0,
        exec_count_norm: if ctx.exec_count > 0 {
            (ctx.exec_count as f32).log10() / 7.0
        } else {
            0.0
        },
        havoc_ema: ctx.strategy_emas[0],
        havocrec_ema: ctx.strategy_emas[1],
        splice_ema: ctx.strategy_emas[2],
        det_ema: ctx.strategy_emas[3],
        generate_ema: ctx.strategy_emas[4],
    }
}

pub struct DqnPolicy {
    worker: DqnWorker,
    last_state: Option<[f32; STATE_DIM]>,
    last_action: Option<u8>,
    last_q_values: [f32; 5],
    logger: RlLogger,
}

impl DqnPolicy {
    pub fn new(trainer: Arc<Mutex<DqnTrainer>>, workdir: &str, cfg: &DqnConfig) -> Self {
        Self {
            worker: DqnWorker::new(trainer, cfg),
            last_state: None,
            last_action: None,
            last_q_values: [0.0f32; 5],
            logger: RlLogger::new(workdir),
        }
    }
}

impl MutationPolicy for DqnPolicy {
    fn select_action(&mut self, ctx: &PolicyContext) -> Option<u8> {
        let state = ctx_to_dqn_state(ctx);
        let state_arr = state.to_array();

        // Fetch Q-values for logging before select_action (epsilon-greedy may pick random).
        let q_vals: [f32; 5] = {
            let trainer = self.worker.trainer.lock().unwrap();
            match trainer.q_values(&state_arr) {
                Ok(ref qs) if qs.len() == 5 => [qs[0], qs[1], qs[2], qs[3], qs[4]],
                _ => [0.0f32; 5],
            }
        };
        self.last_q_values = q_vals;

        let action = self.worker.select_action(&state_arr);
        self.last_state = Some(state_arr);
        self.last_action = Some(action);
        Some(action)
    }

    fn observe(&mut self, action: u8, ctx: &PolicyContext) {
        if let Some(prev_state) = self.last_state {
            let reward = compute_reward(ctx.coverage_delta, ctx.is_crash, ctx.is_timeout);
            let next_state = ctx_to_dqn_state(ctx).to_array();

            // snapshot epsilon before observe() decays it
            let epsilon = self.worker.epsilon;

            let loss = self.worker
                .observe(prev_state, action, reward, next_state, false);

            if let Some(l) = loss {
                self.logger.record_loss(l);
            }
            // record after training so loss (if any) has been captured
            self.logger.record(action, &self.last_q_values, reward, epsilon);
        }
    }
}
