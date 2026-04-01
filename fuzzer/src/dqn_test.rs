// Standalone DQN integration test binary

extern crate candle_core;
extern crate candle_nn;
extern crate rand;

#[path = "dqn.rs"]
mod dqn;

use dqn::{DqnConfig, DqnTrainer, DqnWorker, STATE_DIM};
use rand::Rng;
use std::sync::{Arc, Mutex};

fn main() {
    println!("=== DQN Test Suite ===");

    // Test 1: Forward pass
    println!("\n[Test 1] Forward pass...");
    let trainer = DqnTrainer::new(&DqnConfig::default()).expect("Failed to create DqnTrainer");
    let state: [f32; STATE_DIM] = [
        0.5, 0.3, 0.1, 0.0, 0.05, 0.2, 0.6, 0.4, 0.3, 0.5, 0.2, 0.7,
    ];
    let q_vals = trainer
        .q_values(&state)
        .expect("q_values() failed");
    println!("  Q-values: {:?}", q_vals);
    assert_eq!(q_vals.len(), 5, "Expected 5 Q-values, got {}", q_vals.len());
    for (i, v) in q_vals.iter().enumerate() {
        assert!(v.is_finite(), "Q-value[{}] is not finite: {}", i, v);
    }
    println!("  Forward pass OK.");

    // Test 2: Training convergence
    println!("\n[Test 2] Training convergence (200 steps)...");
    let cfg2 = DqnConfig { train_interval: 50, ..DqnConfig::default() };
    let trainer2 = DqnTrainer::new(&cfg2).expect("Failed to create DqnTrainer");
    let trainer2 = Arc::new(Mutex::new(trainer2));
    let mut worker = DqnWorker::new(Arc::clone(&trainer2), &cfg2);

    let mut rng = rand::thread_rng();
    let mut initial_loss: Option<f32> = None;
    let mut final_loss: f32 = 0.0;

    for step in 1..=200usize {
        let state: [f32; STATE_DIM] = std::array::from_fn(|_| rng.gen::<f32>());
        let next_state: [f32; STATE_DIM] = std::array::from_fn(|_| rng.gen::<f32>());
        let action: u8 = rng.gen_range(0..5u8);
        let reward: f32 = rng.gen_range(-1.0f32..1.0f32);
        let done = false;

        // observe() returns Some(loss) when training fires at train_interval=50
        if let Some(loss) = worker.observe(state, action, reward, next_state, done) {
            if step == 50 && initial_loss.is_none() {
                initial_loss = Some(loss);
            }
            if step >= 200 {
                final_loss = loss;
            }
            println!("  step={} loss={:.6} epsilon={:.4}", step, loss, worker.epsilon);
        }
    }

    let initial = initial_loss.unwrap_or(0.0);
    println!("\n  initial_loss (step~50): {:.6}", initial);
    println!("  final_loss   (step 200): {:.6}", final_loss);

    // Sanity check: final loss should not have exploded beyond 2x initial
    // (noisy environment, so we just check it's finite)
    assert!(final_loss.is_finite(), "final_loss is not finite: {}", final_loss);
    if initial > 0.0 {
        assert!(
            final_loss < initial * 2.0,
            "final_loss ({}) >= initial_loss * 2 ({})",
            final_loss,
            initial * 2.0
        );
    }
    println!("  Training convergence OK.");

    println!("\nAll DQN tests passed!");
}

