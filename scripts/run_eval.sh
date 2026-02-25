#!/usr/bin/env bash
# run_eval.sh — Launch a Nautilus fuzzing campaign against a specific SQLite version
#
# Usage:
#   ./scripts/run_eval.sh <sqlite_version> [run_id]
#
# Example:
#   ./scripts/run_eval.sh sqlite-3.31.1
#   ./scripts/run_eval.sh sqlite-3.31.1 run2
#
# Environment variables (override defaults):
#   WORKDIR_BASE   base directory for workdirs (default: /tmp/nautilus_eval)
#   GRAMMAR        grammar file (default: grammars/sqlite.py)
#   MAX_TREE_SIZE  Nautilus max_tree_size (default: 300)
#   TIMEOUT_MS     per-execution timeout in ms (default: 500)
#   DURATION       fuzzing duration in seconds (default: 86400 = 24h)
#   THREADS        number of Nautilus threads (default: 1)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

VERSION="${1:-}"
RUN_ID="${2:-run1}"

if [[ -z "$VERSION" ]]; then
    echo "Usage: $0 <sqlite_version> [run_id]"
    echo "Example: $0 sqlite-3.31.1 run1"
    exit 1
fi

HARNESS_BIN="$ROOT/harness/sqlite_harness_${VERSION}"
if [[ ! -f "$HARNESS_BIN" ]]; then
    echo "Error: harness binary not found: $HARNESS_BIN"
    echo "Build it first: cd harness && make SQLITE=../cve_builds/${VERSION}/sqlite3.c TARGET=sqlite_harness_${VERSION}"
    exit 1
fi

WORKDIR_BASE="${WORKDIR_BASE:-/tmp/nautilus_eval}"
GRAMMAR="${GRAMMAR:-$ROOT/grammars/sqlite.py}"
MAX_TREE_SIZE="${MAX_TREE_SIZE:-300}"
TIMEOUT_MS="${TIMEOUT_MS:-500}"
THREADS="${THREADS:-1}"
DURATION="${DURATION:-86400}"

WORKDIR="$WORKDIR_BASE/${VERSION}_${RUN_ID}"
mkdir -p "$WORKDIR"

echo "=============================================="
echo " Nautilus SQLite Fuzzing Campaign"
echo "=============================================="
echo " Version:      $VERSION"
echo " Run ID:       $RUN_ID"
echo " Harness:      $HARNESS_BIN"
echo " Workdir:      $WORKDIR"
echo " Grammar:      $GRAMMAR"
echo " max_tree_size: $MAX_TREE_SIZE"
echo " Timeout:      ${TIMEOUT_MS}ms"
echo " Duration:     ${DURATION}s"
echo "=============================================="

# Write a config.ron for this run
CONFIG="$WORKDIR/config.ron"
cat > "$CONFIG" <<EOF
Config(
    path_to_bin_target: "$HARNESS_BIN",
    arguments: ["@@"],
    path_to_grammar: "$GRAMMAR",
    path_to_workdir: "$WORKDIR",
    number_of_threads: $THREADS,
    timeout_in_millis: $TIMEOUT_MS,
    bitmap_size: 65536,
    thread_size: 4194304,
    number_of_generate_inputs: 100,
    max_tree_size: $MAX_TREE_SIZE,
    number_of_deterministic_mutations: 1,
    rl_enabled: false,
)
EOF

echo "Config written to: $CONFIG"
echo "Starting fuzzer... (Ctrl+C to stop)"
echo ""

# Set sanitizer env so child process inherits them
export ASAN_OPTIONS="exitcode=223,abort_on_error=1,detect_leaks=0"
export UBSAN_OPTIONS="halt_on_error=1,exitcode=1"
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/home/linuxbrew/.linuxbrew/lib}"

START_TIME=$(date +%s)

# Run with timeout if DURATION is set
if command -v timeout &>/dev/null; then
    timeout "$DURATION" \
        "$ROOT/target/release/fuzzer" -c "$CONFIG" \
        || true
else
    "$ROOT/target/release/fuzzer" -c "$CONFIG"
fi

END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo ""
echo "=============================================="
echo " Campaign finished after ${ELAPSED}s"
echo " Crashes: $(ls "$WORKDIR/crashes/" 2>/dev/null | wc -l)"
echo " Queue:   $(ls "$WORKDIR/queue/" 2>/dev/null | wc -l)"
echo "=============================================="
echo ""
echo "Run triage:"
echo "  python3 triage/dedup.py $WORKDIR --harness $HARNESS_BIN --output $WORKDIR/dedup"
echo "  python3 triage/minimize.py <crash> --harness $HARNESS_BIN"
echo "  python3 triage/report.py $WORKDIR/dedup --harness $HARNESS_BIN --output $WORKDIR/report.md"
