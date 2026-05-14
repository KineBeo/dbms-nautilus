// MutationPolicy trait for pluggable mutation strategy selection.
// DefaultPolicy: Nautilus uses its normal mutation pipeline (all strategies).
// The trait is preserved for future RL integration.

pub struct PolicyContext {
    pub coverage_delta: usize,
    pub is_crash: bool,
    pub is_timeout: bool,
    pub total_coverage: usize,
    pub exec_count: u64,
    pub queue_size: usize,
    pub strategy_emas: [f32; 5],
    pub last_action: Option<u8>,
}

pub trait MutationPolicy: Send {
    fn select_action(&mut self, _ctx: &PolicyContext) -> Option<u8> {
        None
    }

    fn observe(&mut self, _action: u8, _ctx: &PolicyContext) {}
}

pub struct DefaultPolicy;

impl MutationPolicy for DefaultPolicy {}
