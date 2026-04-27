#!/usr/bin/env bash
# deep_test.sh — Run a diagnostic campaign and produce a per-component health report
# Usage: ./scripts/deep_test.sh
# Exit: 0 if all mutation strategies verified, 1 if any silent

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="$(python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

FUZZER="$ROOT/target/release/fuzzer"
GRAMMAR="$ROOT/grammars/sqlite_v3.py"
HARNESS="$ROOT/harness/sqlite_harness_patterns_sqlite-3.31.1"
CAMPAIGN_DURATION=90

for bin in "$FUZZER" "$HARNESS"; do
    if [[ ! -x "$bin" ]]; then
        echo "FATAL: binary not found: $bin"
        exit 2
    fi
done

WORKDIR=$(mktemp -d /tmp/deep_XXXXXX)
trap 'rm -rf "$WORKDIR"' EXIT
mkdir -p "$WORKDIR/outputs/signaled" "$WORKDIR/outputs/queue" "$WORKDIR/outputs/timeout" "$WORKDIR/outputs/chunks"

CONFIG="$WORKDIR/config.ron"
cat > "$CONFIG" <<EORON
Config(
    path_to_bin_target: "$HARNESS",
    arguments: ["@@"],
    path_to_grammar: "$GRAMMAR",
    path_to_workdir: "$WORKDIR",
    number_of_threads: 1,
    timeout_in_millis: 500,
    bitmap_size: 65536,
    thread_size: 4194304,
    number_of_generate_inputs: 100,
    max_tree_size: 1000,
    number_of_deterministic_mutations: 1,
)
EORON

echo "==============================================================="
echo " RL-Nautilus Deep Component Test — Diagnostic Report"
echo " Campaign: ${CAMPAIGN_DURATION}s, 1 thread, sqlite-3.31.1"
echo " Workdir: $WORKDIR"
echo "==============================================================="
echo ""
echo "Running ${CAMPAIGN_DURATION}s campaign..."
START_TIME=$(date +%s)
timeout "$CAMPAIGN_DURATION" "$FUZZER" -c "$CONFIG" >/dev/null 2>&1 || true
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))
echo "Campaign finished in ${ELAPSED}s."
echo ""

LOG="$WORKDIR/exec.log"
if [[ ! -s "$LOG" ]]; then
    echo "FATAL: exec.log is empty — fuzzer produced no output."
    echo "Check that the fuzzer binary was rebuilt with strategy labels."
    exit 2
fi

FAILURES=0

# ======================================================================
# S1–S5: Mutation Strategy Sections
# ======================================================================

check_strategy() {
    local num="$1"
    local title="$2"
    local grep_key="$3"
    local var_name="$4"
    local required="${5:-yes}"

    echo "--- S${num}: ${title} ---"
    local count
    count=$(grep -c "${grep_key}:NEW_COV" "$LOG" 2>/dev/null || true)
    local example=""
    if [[ $count -gt 0 ]]; then
        example=$(grep "${grep_key}:NEW_COV" "$LOG" | head -1 | cut -f3 | head -c 120)
    fi

    echo "New coverage events: $count"
    if [[ $count -gt 0 ]]; then
        echo "Example: $example"
        echo "Verdict: VERIFIED"
    else
        if [[ "$required" == "yes" ]]; then
            echo "Verdict: NOT OBSERVED"
            FAILURES=$((FAILURES + 1))
        else
            echo "Verdict: NOT OBSERVED (optional — low yield expected in short runs)"
        fi
    fi
    echo ""

    eval "${var_name}=${count}"
}

check_strategy "1" "HAVOC MUTATION" "Havoc" "S1_COUNT"
check_strategy "2" "HAVOC RECURSION" "HavocRec" "S2_COUNT"
check_strategy "3" "SPLICE MUTATION" "Splice" "S3_COUNT"
check_strategy "4" "DETERMINISTIC MUTATION" "Det" "S4_COUNT" "no"
check_strategy "5" "GENERATE (FRESH)" "Gen" "S5_COUNT"

# ======================================================================
# S6: Coverage Feedback
# ======================================================================
echo "--- S6: COVERAGE FEEDBACK ---"
S6_NEW_COV=$(grep -c "NEW_COV" "$LOG" 2>/dev/null || true)
S6_QUEUE=$(find "$WORKDIR/outputs/queue" -type f 2>/dev/null | wc -l)
S6_CHUNKS=$(find "$WORKDIR/outputs/chunks" -type f 2>/dev/null | wc -l)
echo "Total NEW_COV events: $S6_NEW_COV"
echo "Queue files: $S6_QUEUE (inputs that found new paths)"
echo "Chunk files: $S6_CHUNKS (subtrees harvested for splice)"
if [[ $S6_QUEUE -gt 0 ]] && [[ $S6_CHUNKS -gt 0 ]]; then
    echo "Queue growth proves bitmap → new_bits() → queue.add() pipeline works."
    echo "Verdict: VERIFIED"
    S6_VERDICT="VERIFIED"
else
    echo "Verdict: NOT OBSERVED"
    FAILURES=$((FAILURES + 1))
    S6_VERDICT="NOT OBSERVED"
fi
echo ""

# ======================================================================
# S7: Crash Detection
# ======================================================================
echo "--- S7: CRASH DETECTION ---"
S7_SIGNALED=$(find "$WORKDIR/outputs/signaled" -type f 2>/dev/null | wc -l)
S7_CRASH_LOG=$(grep -c 'ASAN\|UBSAN\|SIGNAL' "$LOG" 2>/dev/null || true)
echo "Signaled files: $S7_SIGNALED"
echo "Crash log entries: $S7_CRASH_LOG"
if [[ $S7_SIGNALED -gt 0 ]] || [[ $S7_CRASH_LOG -gt 0 ]]; then
    S7_EXAMPLE=$(grep 'ASAN\|UBSAN\|SIGNAL' "$LOG" | head -1 | cut -f2-3 | head -c 120)
    echo "Example: $S7_EXAMPLE"
    echo "Verdict: VERIFIED"
    S7_VERDICT="VERIFIED ($S7_SIGNALED files, $S7_CRASH_LOG log entries)"
else
    echo "NOT OBSERVED (0 crashes in ${ELAPSED}s — normal for short runs)"
    echo "The crash detection pipeline (ASan->exit 223->save) is wired correctly"
    echo "per smoke_test.sh T06-T09."
    S7_VERDICT="NOT OBSERVED (expected for ${ELAPSED}s)"
fi
echo ""

# ======================================================================
# S8: CVE PoC Crash Verification (deterministic)
# ======================================================================
echo "--- S8: CVE-2020-9327 PoC CRASH VERIFICATION ---"
POC_GRAMMAR="$ROOT/grammars/cve_2020_9327_poc.py"
if [[ ! -f "$POC_GRAMMAR" ]]; then
    echo "Verdict: SKIPPED (grammar file missing)"
    S8_VERDICT="SKIPPED"
else
    POC_WORKDIR="$WORKDIR/poc_verify"
    mkdir -p "$POC_WORKDIR/outputs/signaled" "$POC_WORKDIR/outputs/queue" "$POC_WORKDIR/outputs/timeout" "$POC_WORKDIR/outputs/chunks"
    POC_CONFIG="$WORKDIR/poc_config.ron"
    cat > "$POC_CONFIG" <<EOPOC
Config(
    path_to_bin_target: "$HARNESS",
    arguments: ["@@"],
    path_to_grammar: "$POC_GRAMMAR",
    path_to_workdir: "$POC_WORKDIR",
    number_of_threads: 1,
    timeout_in_millis: 2000,
    bitmap_size: 65536,
    thread_size: 4194304,
    number_of_generate_inputs: 100,
    max_tree_size: 1000,
    number_of_deterministic_mutations: 1,
)
EOPOC
    echo "Running 10s CVE PoC campaign..."
    timeout 10 "$FUZZER" -c "$POC_CONFIG" >/dev/null 2>&1 || true

    POC_LOG="$POC_WORKDIR/exec.log"
    POC_SIGNALED=$(find "$POC_WORKDIR/outputs/signaled" -type f 2>/dev/null | wc -l)
    POC_SIGNAL_LOG=$(grep -c 'SIGNAL' "$POC_LOG" 2>/dev/null || true)

    echo "Signaled files: $POC_SIGNALED"
    echo "SIGNAL log entries: $POC_SIGNAL_LOG"

    if [[ $POC_SIGNALED -gt 0 ]] && [[ $POC_SIGNAL_LOG -gt 0 ]]; then
        POC_EXAMPLE=$(grep 'SIGNAL' "$POC_LOG" | head -1 | cut -f2-3 | head -c 120)
        echo "Example: $POC_EXAMPLE"
        POC_FILE=$(ls "$POC_WORKDIR/outputs/signaled/" | head -1)
        echo "Crash file: $POC_FILE"
        echo "Pipeline: grammar -> tree -> unparse -> fork server -> harness -> SIGTRAP -> saved"
        echo "Verdict: VERIFIED"
        S8_VERDICT="VERIFIED ($POC_SIGNALED files)"
    else
        echo "Verdict: FAILED — CVE PoC did not trigger crash through fork server"
        S8_VERDICT="FAILED"
        FAILURES=$((FAILURES + 1))
    fi
fi
echo ""

# ======================================================================
# SUMMARY
# ======================================================================
echo "==============================================================="
echo " SUMMARY"
echo "==============================================================="

verdict() {
    local count="$1"
    local label="$2"
    if [[ $count -gt 0 ]]; then
        printf "%-22s VERIFIED (%d new paths)\n" "$label" "$count"
    else
        printf "%-22s NOT OBSERVED\n" "$label"
    fi
}

verdict "$S1_COUNT" "Havoc .............."
verdict "$S2_COUNT" "Havoc Recursion ...."
verdict "$S3_COUNT" "Splice ............."
verdict "$S4_COUNT" "Deterministic ......"
verdict "$S5_COUNT" "Generate ..........."
printf "%-22s %s (%d events, %d queue, %d chunks)\n" "Coverage Feedback .." "$S6_VERDICT" "$S6_NEW_COV" "$S6_QUEUE" "$S6_CHUNKS"
printf "%-22s %s\n" "Crash Detection ...." "$S7_VERDICT"
printf "%-22s %s\n" "CVE PoC Verify ....." "$S8_VERDICT"

TOTAL_LOG_LINES=$(wc -l < "$LOG")
echo ""
echo "Total exec.log lines: $TOTAL_LOG_LINES"
echo "Runtime: ${ELAPSED}s"
echo "==============================================================="

if [[ $FAILURES -gt 0 ]]; then
    exit 1
fi
exit 0
