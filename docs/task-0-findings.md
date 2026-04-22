# Task 0 Findings — Nautilus coverage, seed, harness flags

**Date:** 2026-04-22
**Spec reference:** `docs/superpowers/specs/2026-04-22-measurement-and-fidelity-design.md` §6

## (a) Coverage logging

Fields `bits_found_by_havoc`, `bits_found_by_havoc_rec`, `bits_found_by_min`, `bits_found_by_min_rec`, `bits_found_by_splice`, `bits_found_by_det`, `bits_found_by_gen` are defined in `fuzzer/src/shared_state.rs:13-19` and `fuzzer/src/fuzzer.rs:90-96` as in-memory u64 counters. Grep finds no code path writing them to disk.

Consequence: A2 captures end-of-run proxies only — file counts in `outputs/{queue,signaled,timeout}/` plus the last `Execution Count: N` line from `exec.log`. Adding a `bits_found_by_*` dump would require a fuzzer-source change; that is out of scope for this spec.

## (b) RNG seed control

`grammartec/` and `fuzzer/` use `rand::thread_rng()` throughout. Found at least 11 call sites in `grammartec/src/context.rs`, `grammartec/src/mutator.rs`, `grammartec/src/tree.rs`, `fuzzer/src/dqn.rs`. No seed field in `config.ron` is wired to a `SeedableRng::from_seed` constructor.

Consequence: E2's "3 seeds × 4 variants" matrix uses 3 independent runs per variant as a variance-estimate floor. The ablation report must document this.

## (c) Harness debug flags

`harness/Makefile:18` sets `CFLAGS = -O1 -g $(ASAN_FLAGS) $(EXTRA_CFLAGS)`. Debug info is present. Inlining at `-O1` is mild; gdb can recover source-line frames inside `sqlite3.c` on SIGTRAP.

Consequence: A1's gdb-based stack dedup works without rebuilding harnesses.
