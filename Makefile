# rl-nautilus-phase-2 — unified entrypoint.
#
# Targets:
#   setup        — build the Rust fuzzer (PyO3 needs ABI3 forward-compat for Py3.13)
#   grammar      — render grammars/sqlite_generated.py from cve2grammar cache
#   fuzz-smoke   — 30s fuzz run against sqlite-3.31.1 using sqlite_generated.py
#   fuzz-compare — 1h per grammar (baseline vs generated), emit comparison workdirs
#   dashboard    — render cve2grammar/out/dashboard.html from the bugs corpus
#   test         — cargo test + pytest cve2grammar/
#   clean        — remove generated grammar file and Rust build artifacts
#
# Convenience wrapper over cargo, pytest, and scripts/build_grammar.sh.

.PHONY: setup grammar fuzz-smoke fuzz-compare dashboard test clean

REPO_ROOT := $(shell pwd)
CVE2GRAMMAR_DIR := $(REPO_ROOT)/cve2grammar
GENERATED_GRAMMAR := $(REPO_ROOT)/grammars/sqlite_generated.py
HARNESS := $(REPO_ROOT)/harness/sqlite_harness_sqlite-3.31.1

setup:
	PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release

grammar:
	$(REPO_ROOT)/scripts/build_grammar.sh

fuzz-smoke:
	@test -f $(GENERATED_GRAMMAR) || (echo "run 'make grammar' first" && exit 1)
	@test -f $(HARNESS) || (echo "harness missing: $(HARNESS)" && exit 1)
	DURATION=30 GRAMMAR=$(GENERATED_GRAMMAR) $(REPO_ROOT)/scripts/run_eval.sh sqlite-3.31.1 smoke

fuzz-compare:
	@test -f $(GENERATED_GRAMMAR) || (echo "run 'make grammar' first" && exit 1)
	DURATION=3600 GRAMMAR=$(REPO_ROOT)/grammars/sqlite.py \
		$(REPO_ROOT)/scripts/run_eval.sh sqlite-3.31.1 compare_baseline
	DURATION=3600 GRAMMAR=$(GENERATED_GRAMMAR) \
		$(REPO_ROOT)/scripts/run_eval.sh sqlite-3.31.1 compare_generated
	@echo "compare outputs at /tmp/nautilus_eval/sqlite-3.31.1_compare_{baseline,generated}"

dashboard:
	cd $(CVE2GRAMMAR_DIR) && python3 -m cve2grammar dashboard --section all -o out/dashboard.html
	@echo "dashboard at $(CVE2GRAMMAR_DIR)/out/dashboard.html"

test:
	PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo test --release
	cd $(CVE2GRAMMAR_DIR) && python3 -m pytest

clean:
	rm -f $(GENERATED_GRAMMAR)
	cargo clean
