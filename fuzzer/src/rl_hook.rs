// Phase 2 hook: MutationPolicy trait
// Phase 1: DefaultPolicy is a no-op. Phase 2 swaps in DqnPolicy.

pub struct PolicyContext {
    pub coverage_delta: usize,
    pub is_crash: bool,
}

/// RL mutation policy interface. Phase 2 implements this with a DQN agent.
pub trait MutationPolicy: Send + Sync {
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
