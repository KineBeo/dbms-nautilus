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
#   # CVE-2020-13434 targeted harness (pre-loads PoC schema with trigger)
#   HARNESS_SUFFIX=cve13434_ ./scripts/run_eval.sh sqlite-3.31.1 cve13434_pilot
#
# Environment variables (override defaults):
#   WORKDIR_BASE    base directory for workdirs (default: /tmp/nautilus_eval)
#   GRAMMAR         grammar file (default: grammars/sqlite.py)
#   MAX_TREE_SIZE   Nautilus max_tree_size (default: 300)
#   TIMEOUT_MS      per-execution timeout in ms (default: 500)
#   DURATION        fuzzing duration in seconds (default: 86400 = 24h)
#   THREADS         number of Nautilus threads (default: 1)
#   HARNESS_SUFFIX  prefix before version in harness binary name
#                   default: "" → sqlite_harness_<version>
#                   "cve13434_" → sqlite_harness_cve13434_<version>

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

HARNESS_SUFFIX="${HARNESS_SUFFIX:-}"
HARNESS_BIN="$ROOT/harness/sqlite_harness_${HARNESS_SUFFIX}${VERSION}"
if [[ ! -f "$HARNESS_BIN" ]]; then
    echo "Error: harness binary not found: $HARNESS_BIN"
    if [[ "$HARNESS_SUFFIX" == "patterns_" ]]; then
        echo "Build it first:"
        echo "  cd harness && make patterns-build SQLITE=../cve_builds/${VERSION}/sqlite3.c TARGET=sqlite_harness_${HARNESS_SUFFIX}${VERSION}"
    elif [[ -n "$HARNESS_SUFFIX" ]]; then
        echo "Build it first:"
        echo "  cd harness && make cve13434-build SQLITE=../cve_builds/${VERSION}/sqlite3.c TARGET=sqlite_harness_${HARNESS_SUFFIX}${VERSION}"
    else
        echo "Build it first: cd harness && make SQLITE=../cve_builds/${VERSION}/sqlite3.c TARGET=sqlite_harness_${VERSION}"
    fi
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
    bitmap_size: 2097152,
    thread_size: 4194304,
    number_of_generate_inputs: 1000,
    max_tree_size: $MAX_TREE_SIZE,
    number_of_deterministic_mutations: 1,
    rl_enabled: false,
)
EOF

echo "Config written to: $CONFIG"

# Dump grammar weights for this run (observability)
echo "Dumping grammar weights..."
"$SCRIPT_DIR/weight_dump.sh" "$WORKDIR" 2>&1

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
echo " Crashes: $(ls "$WORKDIR/outputs/signaled/" 2>/dev/null | wc -l) (in outputs/signaled/)"
echo " Queue:   $(ls "$WORKDIR/outputs/queue/" 2>/dev/null | wc -l) (in outputs/queue/)"
echo "=============================================="
echo ""
echo "Run triage:"
echo "  python3 triage/dedup.py $WORKDIR --harness $HARNESS_BIN --output $WORKDIR/dedup"
echo "  python3 triage/minimize.py <crash> --harness $HARNESS_BIN"
echo "  python3 triage/report.py $WORKDIR/dedup --harness $HARNESS_BIN --output $WORKDIR/report.md"
