// Nautilus
// Copyright (C) 2024  Daniel Teuchert, Cornelius Aschermann, Sergej Schumilo

extern crate time as othertime;
use othertime::strftime;

use std::collections::HashSet;
use std::collections::VecDeque;
use std::fs::{File, OpenOptions};
use std::io::{stdout, BufWriter, Write};
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Instant;

use forksrv::exitreason::ExitReason;
use forksrv::newtypes::SubprocessError;
use forksrv::ForkServer;
use grammartec::context::Context;
use grammartec::newtypes::NodeID;
use grammartec::tree::TreeLike;
use shared_state::GlobalSharedState;

pub enum ExecutionReason {
    Havoc,
    HavocRec,
    Min,
    MinRec,
    Splice,
    Det,
    Gen,
}

fn reason_label(r: &ExecutionReason) -> &'static str {
    match r {
        ExecutionReason::Havoc => "Havoc",
        ExecutionReason::HavocRec => "HavocRec",
        ExecutionReason::Min => "Min",
        ExecutionReason::MinRec => "MinRec",
        ExecutionReason::Splice => "Splice",
        ExecutionReason::Det => "Det",
        ExecutionReason::Gen => "Gen",
    }
}

// Logs interesting events (crashes, timeouts, new coverage) to workdir/exec.log.
// Uses BufWriter for low overhead; log lines written only on interesting events (~1-5% of execs).
// File is capped at ~10MB: when size exceeds limit, file is truncated and restarted.
const EXEC_LOG_SIZE_LIMIT: u64 = 10 * 1024 * 1024; // 10 MB

struct ExecLogger {
    writer: BufWriter<File>,
    bytes_written: u64,
    log_path: String,
}

impl ExecLogger {
    fn new(work_dir: &str) -> Self {
        let log_path = format!("{}/exec.log", work_dir);
        let file = OpenOptions::new()
            .create(true)
            .append(true)
            .open(&log_path)
            .expect("Failed to open exec.log");
        ExecLogger {
            writer: BufWriter::new(file),
            bytes_written: 0,
            log_path,
        }
    }

    fn log(&mut self, exec_count: u64, exit_reason: &str, rule_id: &str, sql: &[u8]) {
        let snippet = String::from_utf8_lossy(&sql[..sql.len().min(200)]);
        let snippet = snippet.replace('\n', " ").replace('\r', "");
        let line = format!("{}\t{}\t{}\t{}\n", exec_count, exit_reason, rule_id, snippet);
        let line_bytes = line.len() as u64;

        if self.bytes_written + line_bytes > EXEC_LOG_SIZE_LIMIT {
            let file = OpenOptions::new()
                .create(true)
                .write(true)
                .truncate(true)
                .open(&self.log_path)
                .expect("Failed to rotate exec.log");
            self.writer = BufWriter::new(file);
            self.bytes_written = 0;
        }

        let _ = self.writer.write_all(line.as_bytes());
        let _ = self.writer.flush();
        self.bytes_written += line_bytes;
    }
}

pub struct Fuzzer {
    forksrv: ForkServer,
    last_tried_inputs: HashSet<Vec<u8>>,
    last_inputs_ring_buffer: VecDeque<Vec<u8>>,
    pub global_state: Arc<Mutex<GlobalSharedState>>,
    pub target_path: String,
    pub target_args: Vec<String>,
    pub execution_count: u64,
    pub average_executions_per_sec: f32,
    pub bits_found_by_havoc: u64,
    pub bits_found_by_havoc_rec: u64,
    pub bits_found_by_min: u64,
    pub bits_found_by_min_rec: u64,
    pub bits_found_by_splice: u64,
    pub bits_found_by_det: u64,
    pub bits_found_by_gen: u64,
    work_dir: String,
    exec_logger: ExecLogger,
}

impl Fuzzer {
    pub fn new(
        path: String,
        args: Vec<String>,
        global_state: Arc<Mutex<GlobalSharedState>>,
        work_dir: String,
        timeout_in_millis: u64,
        bitmap_size: usize,
    ) -> Result<Self, SubprocessError> {
        let fs = ForkServer::new(
            path.clone(),
            args.clone(),
            true,
            timeout_in_millis,
            bitmap_size,
        );
        let exec_logger = ExecLogger::new(&work_dir);
        return Ok(Fuzzer {
            forksrv: fs,
            last_tried_inputs: HashSet::new(),
            last_inputs_ring_buffer: VecDeque::new(),
            global_state,
            target_path: path,
            target_args: args,
            execution_count: 0,
            average_executions_per_sec: 0.0,
            bits_found_by_havoc: 0,
            bits_found_by_havoc_rec: 0,
            bits_found_by_min: 0,
            bits_found_by_min_rec: 0,
            bits_found_by_splice: 0,
            bits_found_by_det: 0,
            bits_found_by_gen: 0,
            work_dir: work_dir,
            exec_logger,
        });
    }

    pub fn run_on_with_dedup<T: TreeLike>(
        &mut self,
        tree: &T,
        exec_reason: ExecutionReason,
        ctx: &Context,
    ) -> Result<bool, SubprocessError> {
        let code: Vec<u8> = tree.unparse_to_vec(ctx);
        if self.input_is_known(&code) {
            return Ok(false);
        }
        self.run_on(&code, tree, exec_reason, ctx)?;
        return Ok(true);
    }

    pub fn run_on_without_dedup<T: TreeLike>(
        &mut self,
        tree: &T,
        exec_reason: ExecutionReason,
        ctx: &Context,
    ) -> Result<(), SubprocessError> {
        let code = tree.unparse_to_vec(ctx);
        return self.run_on(&code, tree, exec_reason, ctx);
    }

    fn run_on<T: TreeLike>(
        &mut self,
        code: &Vec<u8>,
        tree: &T,
        exec_reason: ExecutionReason,
        ctx: &Context,
    ) -> Result<(), SubprocessError> {
        let strategy = reason_label(&exec_reason);
        let (new_bits, term_sig) = self.exec(code, tree, ctx, strategy)?;
        match term_sig {
            ExitReason::Normal(223) => {
                if new_bits.is_some() {
                    //ASAN
                    self.global_state
                        .lock()
                        .expect("RAND_3390206382")
                        .total_found_asan += 1;
                    self.global_state
                        .lock()
                        .expect("RAND_202860771")
                        .last_found_asan = strftime("[%Y-%m-%d] %H:%M:%S", &othertime::now())
                        .expect("RAND_2888070412");
                    let mut file = File::create(format!(
                        "{}/outputs/signaled/ASAN_{:09}_{}",
                        self.work_dir,
                        self.execution_count,
                        thread::current().name().expect("RAND_4086695190")
                    ))
                    .expect("RAND_3096222153");
                    tree.unparse_to(ctx, &mut file);
                }
            }
            ExitReason::Normal(1) => {
                // UBSan — save every unique crash (new_bits = new coverage path)
                if new_bits.is_some() {
                    self.global_state
                        .lock()
                        .expect("RAND_ubsan_count")
                        .total_found_ubsan += 1;
                    self.global_state
                        .lock()
                        .expect("RAND_ubsan_time")
                        .last_found_asan = strftime("[%Y-%m-%d] %H:%M:%S", &othertime::now())
                        .expect("RAND_ubsan_fmt");
                    let mut file = File::create(format!(
                        "{}/outputs/signaled/UBSAN_{:09}_{}",
                        self.work_dir,
                        self.execution_count,
                        thread::current().name().expect("RAND_ubsan_thread")
                    ))
                    .expect("RAND_ubsan_file");
                    tree.unparse_to(ctx, &mut file);
                }
            }
            ExitReason::Normal(_) => {
                if new_bits.is_some() {
                    match exec_reason {
                        ExecutionReason::Havoc => {
                            self.bits_found_by_havoc += 1; /*print!("Havoc+")*/
                        }
                        ExecutionReason::HavocRec => {
                            self.bits_found_by_havoc_rec += 1; /*print!("HavocRec+")*/
                        }
                        ExecutionReason::Min => {
                            self.bits_found_by_min += 1; /*print!("Min+")*/
                        }
                        ExecutionReason::MinRec => {
                            self.bits_found_by_min_rec += 1; /*print!("MinRec+")*/
                        }
                        ExecutionReason::Splice => {
                            self.bits_found_by_splice += 1; /*print!("Splice+")*/
                        }
                        ExecutionReason::Det => {
                            self.bits_found_by_det += 1; /*print!("Det+")*/
                        }
                        ExecutionReason::Gen => {
                            self.bits_found_by_gen += 1; /*print!("Gen+")*/
                        }
                    }
                }
            }
            ExitReason::Timeouted => {
                self.global_state
                    .lock()
                    .expect("RAND_1706238230")
                    .last_timeout =
                    strftime("[%Y-%m-%d] %H:%M:%S", &othertime::now()).expect("RAND_1894162412");
                let mut file = File::create(format!(
                    "{}/outputs/timeout/{:09}",
                    self.work_dir, self.execution_count
                ))
                .expect("RAND_452993103");
                tree.unparse_to(ctx, &mut file);
            }
            ExitReason::Signaled(sig) => {
                if new_bits.is_some() {
                    self.global_state
                        .lock()
                        .expect("RAND_1858328446")
                        .total_found_sig += 1;
                    self.global_state
                        .lock()
                        .expect("RAND_4287051369")
                        .last_found_sig =
                        strftime("[%Y-%m-%d] %H:%M:%S", &othertime::now()).expect("RAND_76391000");
                    let mut file = File::create(format!(
                        "{}/outputs/signaled/{:?}_{:09}",
                        self.work_dir, sig, self.execution_count
                    ))
                    .expect("RAND_3690294970");
                    tree.unparse_to(ctx, &mut file);
                }
            }
            ExitReason::Stopped(_sig) => {}
        }
        stdout().flush().expect("RAND_2937475131");
        return Ok(());
    }

    pub fn has_bits<T: TreeLike>(
        &mut self,
        tree: &T,
        bits: &HashSet<usize>,
        exec_reason: ExecutionReason,
        ctx: &Context,
    ) -> Result<bool, SubprocessError> {
        self.run_on_without_dedup(tree, exec_reason, ctx)?;
        let run_bitmap = self.forksrv.get_shared();
        let mut found_all = true;
        for bit in bits.iter() {
            if run_bitmap[*bit] == 0 {
                //TODO: handle edge counts properly
                found_all = false;
            }
        }
        return Ok(found_all);
    }

    pub fn exec_raw<'a>(&'a mut self, code: &[u8]) -> Result<(ExitReason, u32), SubprocessError> {
        self.execution_count += 1;

        let start = Instant::now();

        let exitreason = self.forksrv.run(&code)?;

        let execution_time = start.elapsed().subsec_nanos();

        self.average_executions_per_sec = self.average_executions_per_sec * 0.9
            + ((1.0 / (execution_time as f32)) * 1000000000.0) * 0.1;

        return Ok((exitreason, execution_time));
    }

    fn input_is_known(&mut self, code: &[u8]) -> bool {
        if self.last_tried_inputs.contains(code) {
            return true;
        } else {
            self.last_tried_inputs.insert(code.to_vec());
            if self.last_inputs_ring_buffer.len() == 10000 {
                self.last_tried_inputs.remove(
                    &self
                        .last_inputs_ring_buffer
                        .pop_back()
                        .expect("No entry in last_inputs_ringbuffer"),
                );
            }
            self.last_inputs_ring_buffer.push_front(code.to_vec());
        }
        return false;
    }

    fn exec<T: TreeLike>(
        &mut self,
        code: &[u8],
        tree_like: &T,
        ctx: &Context,
        strategy: &str,
    ) -> Result<(Option<Vec<usize>>, ExitReason), SubprocessError> {
        let (exitreason, execution_time) = self.exec_raw(&code)?;

        let tree_size = tree_like.size();
        let rule_tag = if tree_size > 2 {
            let stmt_rule: usize = tree_like.get_rule_id(NodeID::from(2)).into();
            format!("R{}", stmt_rule)
        } else {
            let root_rule: usize = tree_like.get_rule_id(NodeID::from(0)).into();
            format!("R{}", root_rule)
        };

        let is_crash = match exitreason {
            ExitReason::Normal(223) => true,   // ASan
            ExitReason::Normal(1) => true,     // UBSan
            ExitReason::Signaled(_) => true,
            _ => false,
        };

        match exitreason {
            ExitReason::Normal(223) => {
                let label = format!("{}:ASAN(223)", strategy);
                self.exec_logger.log(self.execution_count, &label, &rule_tag, code);
            }
            ExitReason::Normal(1) => {
                let label = format!("{}:UBSAN(1)", strategy);
                self.exec_logger.log(self.execution_count, &label, &rule_tag, code);
            }
            ExitReason::Signaled(sig) => {
                let label = format!("{}:SIGNAL({:?})", strategy, sig);
                self.exec_logger.log(self.execution_count, &label, &rule_tag, code);
            }
            ExitReason::Timeouted => {
                let label = format!("{}:TIMEOUT", strategy);
                self.exec_logger.log(self.execution_count, &label, &rule_tag, code);
            }
            _ => {}
        }

        let mut final_bits = None;
        if let Some(mut new_bits) = self.new_bits(is_crash) {
            //Only if not Timeout
            if exitreason != ExitReason::Timeouted {
                //Check for non deterministic bits
                let old_bitmap: Vec<u8> = self.forksrv.get_shared().to_vec();
                self.check_deterministic_behaviour(&old_bitmap, &mut new_bits, &code)?;
                if new_bits.len() > 0 {
                    final_bits = Some(new_bits);
                    let tree = tree_like.to_tree(ctx);
                    let cov_label = format!("{}:NEW_COV", strategy);
                    self.exec_logger.log(self.execution_count, &cov_label, &rule_tag, code);
                    self.global_state
                        .lock()
                        .expect("RAND_2835014626")
                        .queue
                        .add(tree, old_bitmap, exitreason, ctx, execution_time);
                    //println!("Entry added to queue! New bits: {:?}", bits.clone().expect("RAND_2243482569"));
                }
            }
        }
        return Ok((final_bits, exitreason));
    }

    fn check_deterministic_behaviour(
        &mut self,
        _old_bitmap: &[u8],
        new_bits: &mut Vec<usize>,
        code: &[u8],
    ) -> Result<(), SubprocessError> {
        for _ in 0..5 {
            let (_, _) = self.exec_raw(code)?;
            let run_bitmap = self.forksrv.get_shared();
            new_bits.retain(|&i| run_bitmap[i] != 0);
        }
        return Ok(());
    }

    pub fn new_bits(&mut self, is_crash: bool) -> Option<Vec<usize>> {
        let mut res = vec![];
        let run_bitmap = self.forksrv.get_shared();
        let mut gstate_lock = self.global_state.lock().expect("RAND_2040280272");
        let shared_bitmap = gstate_lock
            .bitmaps
            .get_mut(&is_crash)
            .expect("Bitmap missing! Maybe shared state was not initialized correctly?");

        for (i, elem) in shared_bitmap.iter_mut().enumerate() {
            if (run_bitmap[i] != 0) && (*elem == 0) {
                *elem |= run_bitmap[i];
                res.push(i);
                //println!("Added new bit to bitmap. Is Crash: {:?}; Added bit: {:?}", is_crash, i);
            }
        }

        if res.len() > 0 {
            //print!("New path found:\nNew bits: {:?}\n", res);
            return Some(res);
        }
        return None;
    }
}
