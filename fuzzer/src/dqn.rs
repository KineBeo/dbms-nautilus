// Phase 2: DQN agent for adaptive mutation strategy selection

use candle_core::{Device, Result as CandleResult, Tensor};
use candle_nn::{linear, AdamW, Linear, Module, Optimizer, ParamsAdamW, VarBuilder, VarMap};
use rand::Rng;
use std::sync::{Arc, Mutex};

// Architectural constants — not tunable at runtime
pub const STATE_DIM: usize = 12;
pub const ACTION_DIM: usize = 5;

/// Runtime hyperparameters sourced from config.ron (rl_* fields).
pub struct DqnConfig {
    pub batch_size: usize,
    pub replay_size: usize,
    pub gamma: f32,
    pub lr: f64,
    pub target_update_freq: u64,
    pub train_interval: u64,
    pub epsilon_start: f32,
    pub epsilon_end: f32,
    pub epsilon_decay: f32,
}

impl Default for DqnConfig {
    fn default() -> Self {
        Self {
            batch_size: 32,
            replay_size: 3000,
            gamma: 0.99,
            lr: 0.001,
            target_update_freq: 1000,
            train_interval: 100,
            epsilon_start: 1.0,
            epsilon_end: 0.05,
            epsilon_decay: 50_000.0,
        }
    }
}

/// State representation for the DQN agent
pub struct DqnState {
    /// New bits from last execution, normalized
    pub coverage_delta: f32,
    /// Bitmap fraction (total coverage)
    pub total_coverage: f32,
    /// EMA of coverage gain (last 100)
    pub coverage_velocity: f32,
    /// 1.0 if crashed
    pub is_crash: f32,
    /// EMA crash rate (last 1000)
    pub crash_rate: f32,
    /// queue_size / 10000
    pub queue_size_norm: f32,
    /// log10(exec_count) / 7
    pub exec_count_norm: f32,
    /// Per-strategy reward EMAs
    pub havoc_ema: f32,
    pub havocrec_ema: f32,
    pub splice_ema: f32,
    pub det_ema: f32,
    pub generate_ema: f32,
}

impl DqnState {
    pub fn to_array(&self) -> [f32; STATE_DIM] {
        [
            self.coverage_delta,
            self.total_coverage,
            self.coverage_velocity,
            self.is_crash,
            self.crash_rate,
            self.queue_size_norm,
            self.exec_count_norm,
            self.havoc_ema,
            self.havocrec_ema,
            self.splice_ema,
            self.det_ema,
            self.generate_ema,
        ]
    }
}

/// Compute reward signal from execution outcome
pub fn compute_reward(coverage_delta: usize, is_crash: bool, is_timeout: bool) -> f32 {
    let mut r = coverage_delta as f32;
    if is_crash {
        r += 10.0;
    }
    if is_timeout {
        r -= 1.0;
    }
    if coverage_delta == 0 && !is_crash {
        r -= 0.1;
    }
    r
}

/// Simple fully-connected Q-network: 12 -> 64 -> 32 -> 5
struct QNetwork {
    fc1: Linear,
    fc2: Linear,
    fc3: Linear,
}

impl QNetwork {
    fn new(vs: VarBuilder) -> CandleResult<Self> {
        let fc1 = linear(STATE_DIM, 64, vs.pp("fc1"))?;
        let fc2 = linear(64, 32, vs.pp("fc2"))?;
        let fc3 = linear(32, ACTION_DIM, vs.pp("fc3"))?;
        Ok(Self { fc1, fc2, fc3 })
    }

    fn forward(&self, x: &Tensor) -> CandleResult<Tensor> {
        let h1 = self.fc1.forward(x)?.relu()?;
        let h2 = self.fc2.forward(&h1)?.relu()?;
        self.fc3.forward(&h2)
    }
}

/// Experience tuple for replay buffer
#[derive(Clone)]
struct Experience {
    state: [f32; STATE_DIM],
    action: u8,
    reward: f32,
    next_state: [f32; STATE_DIM],
    done: bool,
}

/// Ring-buffer replay memory
pub struct ReplayBuffer {
    buffer: Vec<Experience>,
    capacity: usize,
    head: usize,
    size: usize,
}

impl ReplayBuffer {
    pub fn new(capacity: usize) -> Self {
        Self {
            buffer: Vec::with_capacity(capacity),
            capacity,
            head: 0,
            size: 0,
        }
    }

    pub fn push(
        &mut self,
        state: [f32; STATE_DIM],
        action: u8,
        reward: f32,
        next_state: [f32; STATE_DIM],
        done: bool,
    ) {
        let exp = Experience {
            state,
            action,
            reward,
            next_state,
            done,
        };
        if self.size < self.capacity {
            self.buffer.push(exp);
            self.size += 1;
        } else {
            self.buffer[self.head] = exp;
            self.head = (self.head + 1) % self.capacity;
        }
    }

    pub fn len(&self) -> usize {
        self.size
    }

    pub fn sample(&self, batch_size: usize) -> Vec<Experience> {
        let mut rng = rand::thread_rng();
        (0..batch_size)
            .map(|_| {
                let idx = rng.gen_range(0..self.size);
                self.buffer[idx].clone()
            })
            .collect()
    }
}

/// DQN trainer holding online and target networks
pub struct DqnTrainer {
    online_varmap: VarMap,
    target_varmap: VarMap,
    online_net: QNetwork,
    target_net: QNetwork,
    optimizer: AdamW,
    pub replay: ReplayBuffer,
    pub step_count: u64,
    device: Device,
    batch_size: usize,
    gamma: f32,
    target_update_freq: u64,
}

impl DqnTrainer {
    pub fn new(cfg: &DqnConfig) -> CandleResult<Self> {
        let device = Device::Cpu;

        let online_varmap = VarMap::new();
        let online_vs = VarBuilder::from_varmap(&online_varmap, candle_core::DType::F32, &device);
        let online_net = QNetwork::new(online_vs)?;

        let target_varmap = VarMap::new();
        let target_vs = VarBuilder::from_varmap(&target_varmap, candle_core::DType::F32, &device);
        let target_net = QNetwork::new(target_vs)?;

        let params = ParamsAdamW {
            lr: cfg.lr,
            ..Default::default()
        };
        let optimizer = AdamW::new(online_varmap.all_vars(), params)?;

        let mut trainer = Self {
            online_varmap,
            target_varmap,
            online_net,
            target_net,
            optimizer,
            replay: ReplayBuffer::new(cfg.replay_size),
            step_count: 0,
            device,
            batch_size: cfg.batch_size,
            gamma: cfg.gamma,
            target_update_freq: cfg.target_update_freq,
        };

        trainer.sync_target()?;
        Ok(trainer)
    }

    /// Copy online network weights to target network
    pub fn sync_target(&mut self) -> CandleResult<()> {
        // Collect (name, tensor) pairs from online varmap
        let online_data: Vec<(String, Tensor)> = self
            .online_varmap
            .data()
            .lock()
            .unwrap()
            .iter()
            .map(|(name, var)| (name.clone(), var.as_tensor().clone()))
            .collect();

        // Apply to target varmap
        let target_data = self.target_varmap.data();
        let mut target_lock = target_data.lock().unwrap();
        for (name, tensor) in online_data {
            if let Some(var) = target_lock.get_mut(&name) {
                var.set(&tensor)?;
            }
        }
        Ok(())
    }

    /// Run inference to get Q-values for a given state
    pub fn q_values(&self, state: &[f32; STATE_DIM]) -> CandleResult<Vec<f32>> {
        let state_tensor =
            Tensor::from_slice(state.as_ref(), (1, STATE_DIM), &self.device)?;
        let q = self.online_net.forward(&state_tensor)?;
        // q shape: (1, ACTION_DIM)
        let values: Vec<f32> = q.squeeze(0)?.to_vec1()?;
        Ok(values)
    }

    /// Perform one gradient update step; returns MSE loss
    pub fn train_step(&mut self) -> CandleResult<f32> {
        if self.replay.len() < self.batch_size {
            return Ok(0.0);
        }

        let batch = self.replay.sample(self.batch_size);
        let n = batch.len();

        // Build flat state and next_state vectors
        let mut states_vec: Vec<f32> = Vec::with_capacity(n * STATE_DIM);
        let mut next_states_vec: Vec<f32> = Vec::with_capacity(n * STATE_DIM);
        for exp in &batch {
            states_vec.extend_from_slice(&exp.state);
            next_states_vec.extend_from_slice(&exp.next_state);
        }

        let states_tensor =
            Tensor::from_slice(&states_vec, (n, STATE_DIM), &self.device)?;
        let next_states_tensor =
            Tensor::from_slice(&next_states_vec, (n, STATE_DIM), &self.device)?;

        // Compute target Q-values using target network (no gradient)
        let target_q_all = self.target_net.forward(&next_states_tensor)?;
        let target_q_vec: Vec<Vec<f32>> = target_q_all.to_vec2()?;

        let mut targets: Vec<f32> = Vec::with_capacity(n);
        for (i, exp) in batch.iter().enumerate() {
            let max_next_q = target_q_vec[i]
                .iter()
                .cloned()
                .fold(f32::NEG_INFINITY, f32::max);
            let target = if exp.done {
                exp.reward
            } else {
                exp.reward + self.gamma * max_next_q
            };
            targets.push(target);
        }
        let targets_tensor =
            Tensor::from_slice(&targets, (n,), &self.device)?;

        // Forward online network
        let q_online = self.online_net.forward(&states_tensor)?; // (n, ACTION_DIM)

        // Build one-hot mask to select Q(s, a)
        let mut one_hot_vec: Vec<f32> = vec![0.0; n * ACTION_DIM];
        for (i, exp) in batch.iter().enumerate() {
            let a = exp.action as usize;
            if a < ACTION_DIM {
                one_hot_vec[i * ACTION_DIM + a] = 1.0;
            }
        }
        let one_hot =
            Tensor::from_slice(&one_hot_vec, (n, ACTION_DIM), &self.device)?;

        // q_sa = sum(q_online * one_hot, dim=1)
        let q_sa = (q_online * one_hot)?.sum(1)?; // (n,)

        // MSE loss
        let diff = (q_sa - targets_tensor)?;
        let loss = (diff.powf(2.0)?.mean_all())?;

        self.optimizer.backward_step(&loss)?;

        self.step_count += 1;
        if self.step_count % self.target_update_freq == 0 {
            self.sync_target()?;
        }

        let loss_val: f32 = loss.to_scalar()?;
        Ok(loss_val)
    }
}

/// Per-worker DQN interface (wraps shared trainer behind Arc<Mutex>)
pub struct DqnWorker {
    pub trainer: Arc<Mutex<DqnTrainer>>,
    pub epsilon: f32,
    pub exec_count: u64,
    epsilon_start: f32,
    epsilon_end: f32,
    epsilon_decay: f32,
    train_interval: u64,
}

impl DqnWorker {
    pub fn new(trainer: Arc<Mutex<DqnTrainer>>, cfg: &DqnConfig) -> Self {
        Self {
            trainer,
            epsilon: cfg.epsilon_start,
            exec_count: 0,
            epsilon_start: cfg.epsilon_start,
            epsilon_end: cfg.epsilon_end,
            epsilon_decay: cfg.epsilon_decay,
            train_interval: cfg.train_interval,
        }
    }

    /// Epsilon-greedy action selection
    pub fn select_action(&self, state: &[f32; STATE_DIM]) -> u8 {
        let mut rng = rand::thread_rng();
        if rng.gen::<f32>() < self.epsilon {
            rng.gen_range(0..ACTION_DIM) as u8
        } else {
            let trainer = self.trainer.lock().unwrap();
            match trainer.q_values(state) {
                Ok(qs) => {
                    qs.iter()
                        .enumerate()
                        .max_by(|(_, a), (_, b)| a.partial_cmp(b).unwrap())
                        .map(|(i, _)| i as u8)
                        .unwrap_or(0)
                }
                Err(_) => rng.gen_range(0..ACTION_DIM) as u8,
            }
        }
    }

    /// Record transition, decay epsilon, and trigger training at train_interval steps.
    /// Returns Some(loss) when a training step ran and produced a positive loss, None otherwise.
    pub fn observe(
        &mut self,
        state: [f32; STATE_DIM],
        action: u8,
        reward: f32,
        next_state: [f32; STATE_DIM],
        done: bool,
    ) -> Option<f32> {
        self.exec_count += 1;

        let loss = {
            let mut trainer = self.trainer.lock().unwrap();
            trainer.replay.push(state, action, reward, next_state, done);

            if self.exec_count % self.train_interval == 0 {
                trainer.train_step().ok().filter(|&l| l > 0.0)
            } else {
                None
            }
        };

        // Decay epsilon
        self.epsilon = self.epsilon_end
            + (self.epsilon_start - self.epsilon_end)
                * (-(self.exec_count as f32) / self.epsilon_decay).exp();

        loss
    }
}
