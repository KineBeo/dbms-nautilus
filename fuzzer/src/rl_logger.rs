// Phase 2: CSV logger for RL metrics
// Logs a row every LOG_INTERVAL steps to <workdir>/rl_metrics.csv

use std::fs::OpenOptions;
use std::io::Write;

pub const LOG_INTERVAL: u64 = 10;

pub struct RlLogger {
    path: String,
    // rolling buffers reset every LOG_INTERVAL steps
    action_counts: [u64; 5],
    q_sums: [f32; 5],
    reward_sum: f32,
    loss_sum: f32,
    loss_count: u64,
    step: u64,
}

impl RlLogger {
    /// Create (or resume) a logger writing to `<workdir>/rl_metrics.csv`.
    /// Writes the CSV header only when creating a new (empty) file.
    pub fn new(workdir: &str) -> Self {
        let path = format!("{}/rl_metrics.csv", workdir);

        let file = OpenOptions::new()
            .create(true)
            .append(true)
            .open(&path)
            .expect("RlLogger: failed to open rl_metrics.csv");

        let metadata = file.metadata().expect("RlLogger: cannot stat rl_metrics.csv");
        if metadata.len() == 0 {
            let mut file = file;
            writeln!(
                file,
                "step,epsilon,\
                 action_0_freq,action_1_freq,action_2_freq,action_3_freq,action_4_freq,\
                 q_0_avg,q_1_avg,q_2_avg,q_3_avg,q_4_avg,\
                 reward_avg,loss_avg"
            )
            .expect("RlLogger: failed to write CSV header");
        }

        RlLogger {
            path,
            action_counts: [0u64; 5],
            q_sums: [0.0f32; 5],
            reward_sum: 0.0,
            loss_sum: 0.0,
            loss_count: 0,
            step: 0,
        }
    }

    /// Record one RL step and flush a CSV row every LOG_INTERVAL steps.
    /// `epsilon` is the current exploration rate from the DqnWorker.
    pub fn record(&mut self, action: u8, q_values: &[f32; 5], reward: f32, epsilon: f32) {
        self.step += 1;
        if (action as usize) < 5 {
            self.action_counts[action as usize] += 1;
        }
        for i in 0..5 {
            self.q_sums[i] += q_values[i];
        }
        self.reward_sum += reward;

        if self.step % LOG_INTERVAL == 0 {
            self.flush(epsilon);
        }
    }

    /// Record a training loss value (called whenever train_step runs).
    pub fn record_loss(&mut self, loss: f32) {
        if loss > 0.0 {
            self.loss_sum += loss;
            self.loss_count += 1;
        }
    }

    /// Flush a CSV row and reset rolling buffers.
    fn flush(&mut self, epsilon: f32) {
        let total_actions: u64 = self.action_counts.iter().sum();
        let n = total_actions.max(1) as f32;

        let action_freqs: [f32; 5] = [
            self.action_counts[0] as f32 / n,
            self.action_counts[1] as f32 / n,
            self.action_counts[2] as f32 / n,
            self.action_counts[3] as f32 / n,
            self.action_counts[4] as f32 / n,
        ];

        let q_avgs: [f32; 5] = [
            self.q_sums[0] / n,
            self.q_sums[1] / n,
            self.q_sums[2] / n,
            self.q_sums[3] / n,
            self.q_sums[4] / n,
        ];

        let reward_avg = self.reward_sum / n;
        let loss_avg = if self.loss_count > 0 {
            self.loss_sum / self.loss_count as f32
        } else {
            0.0
        };

        let line = format!(
            "{},{:.6},{:.6},{:.6},{:.6},{:.6},{:.6},{:.6},{:.6},{:.6},{:.6},{:.6},{:.6},{:.6}\n",
            self.step,
            epsilon,
            action_freqs[0],
            action_freqs[1],
            action_freqs[2],
            action_freqs[3],
            action_freqs[4],
            q_avgs[0],
            q_avgs[1],
            q_avgs[2],
            q_avgs[3],
            q_avgs[4],
            reward_avg,
            loss_avg,
        );

        let mut file = OpenOptions::new()
            .append(true)
            .open(&self.path)
            .expect("RlLogger: failed to open rl_metrics.csv for append");
        file.write_all(line.as_bytes())
            .expect("RlLogger: failed to write CSV row");

        // Reset rolling buffers
        self.action_counts = [0u64; 5];
        self.q_sums = [0.0f32; 5];
        self.reward_sum = 0.0;
        self.loss_sum = 0.0;
        self.loss_count = 0;
    }
}
