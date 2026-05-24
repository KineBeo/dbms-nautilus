# rl-nautilus-phase-2 — unified entrypoint.
#
# Targets:
#   setup        — build the Rust fuzzer (PyO3 needs ABI3 forward-compat for Py3.13)
#   test         — cargo test
#   smoke        — 60s fuzz run against sqlite-3.31.1
#   clean        — remove Rust build artifacts

.PHONY: setup test smoke clean

REPO_ROOT := $(shell pwd)

setup:
	PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release

test:
	PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo test --release

smoke:
	DURATION=60 $(REPO_ROOT)/scripts/run_eval.sh sqlite-3.31.1 smoke

clean:
	cargo clean
