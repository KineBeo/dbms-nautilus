// Nautilus
// Copyright (C) 2024  Daniel Teuchert, Cornelius Aschermann, Sergej Schumilo

use queue::Queue;
use std::collections::HashMap;

pub struct GlobalSharedState {
    pub queue: Queue,
    //false for not crashing input. True for crashing inputs
    pub bitmaps: HashMap<bool, Vec<u8>>,
    pub execution_count: u64,
    pub average_executions_per_sec: u32,
    pub bits_found_by_havoc: u64,
    pub bits_found_by_havoc_rec: u64,
    pub bits_found_by_min: u64,
    pub bits_found_by_min_rec: u64,
    pub bits_found_by_splice: u64,
    pub bits_found_by_det: u64,
    pub bits_found_by_gen: u64,
    pub last_found_asan: String,
    pub last_found_sig: String,
    pub last_timeout: String,
    pub total_found_asan: u64,
    pub total_found_sig: u64,
    pub total_found_ubsan: u64,
}

impl GlobalSharedState {
    pub fn new(work_dir: String, bitmap_size: usize) -> Self {
        let queue = Queue::new(work_dir);
        //Initialize Empty bitmaps for crashes and normal executions
        let mut bitmaps = HashMap::new();
        bitmaps.insert(false, vec![0; bitmap_size]);
        bitmaps.insert(true, vec![0; bitmap_size]);
        return GlobalSharedState {
            queue,
            bitmaps,
            execution_count: 0,
            average_executions_per_sec: 0,
            bits_found_by_havoc: 0,
            bits_found_by_havoc_rec: 0,
            bits_found_by_min: 0,
            bits_found_by_min_rec: 0,
            bits_found_by_splice: 0,
            bits_found_by_det: 0,
            bits_found_by_gen: 0,
            last_found_asan: String::from("Not found yet."),
            last_found_sig: String::from("Not found yet."),
            last_timeout: String::from("No Timeout yet."),
            total_found_asan: 0,
            total_found_sig: 0,
            total_found_ubsan: 0,
        };
    }
}
