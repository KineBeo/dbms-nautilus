# Deep Component Test Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add strategy labels to exec.log for observability, then create `scripts/deep_test.sh` that runs a 90s campaign and produces a per-component health report proving every mutation strategy and coverage feedback actually works.

**Architecture:** Two deliverables — (1) a small Rust change adding a `reason_label` string to `exec()` logging, (2) a bash script that runs the fuzzer and parses the enriched log. The Rust change is permanent (pure observability, no perf impact).

**Tech Stack:** Rust (fuzzer/src/fuzzer.rs), Bash (scripts/deep_test.sh), existing release binaries

---

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| `fuzzer/src/fuzzer.rs` | Modify | Add `reason_label()` helper, pass strategy label to `exec()`, prepend to log entries |
| `scripts/deep_test.sh` | Create | 90s campaign + parse exec.log + 7-section diagnostic report |

---

### Task 1: Add Strategy Labels to exec.log

**Files:**
- Modify: `fuzzer/src/fuzzer.rs`

The logging happens in `exec()` (line 351-406), but `exec()` doesn't receive `ExecutionReason`. The caller `run_on()` (line 181) has it. Simplest fix: add a `reason_label: &str` parameter to `exec()` and prepend it to every log call.

- [ ] **Step 1: Add `reason_label()` helper function**

Add this function right after the `ExecutionReason` enum (after line 30, before the `ExecLogger` comment):

```rust
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
```

- [ ] **Step 2: Update `exec()` signature to accept a strategy label**

Change `exec()` at line 351 from:

```rust
    fn exec<T: TreeLike>(
        &mut self,
        code: &[u8],
        tree_like: &T,
        ctx: &Context,
    ) -> Result<(Option<Vec<usize>>, ExitReason), SubprocessError> {
```

To:

```rust
    fn exec<T: TreeLike>(
        &mut self,
        code: &[u8],
        tree_like: &T,
        ctx: &Context,
        strategy: &str,
    ) -> Result<(Option<Vec<usize>>, ExitReason), SubprocessError> {
```

- [ ] **Step 3: Prepend strategy label to all 5 log calls inside `exec()`**

Replace the logging block (lines 366-382) from:

```rust
        // Log crashes and timeouts immediately (always interesting)
        match exitreason {
            ExitReason::Normal(223) => {
                self.exec_logger.log(self.execution_count, "ASAN(223)", code);
            }
            ExitReason::Normal(1) => {
                self.exec_logger.log(self.execution_count, "UBSAN(1)", code);
            }
            ExitReason::Signaled(sig) => {
                let label = format!("SIGNAL({:?})", sig);
                self.exec_logger.log(self.execution_count, &label, code);
            }
            ExitReason::Timeouted => {
                self.exec_logger.log(self.execution_count, "TIMEOUT", code);
            }
            _ => {}
        }
```

To:

```rust
        match exitreason {
            ExitReason::Normal(223) => {
                let label = format!("{}:ASAN(223)", strategy);
                self.exec_logger.log(self.execution_count, &label, code);
            }
            ExitReason::Normal(1) => {
                let label = format!("{}:UBSAN(1)", strategy);
                self.exec_logger.log(self.execution_count, &label, code);
            }
            ExitReason::Signaled(sig) => {
                let label = format!("{}:SIGNAL({:?})", strategy, sig);
                self.exec_logger.log(self.execution_count, &label, code);
            }
            ExitReason::Timeouted => {
                let label = format!("{}:TIMEOUT", strategy);
                self.exec_logger.log(self.execution_count, &label, code);
            }
            _ => {}
        }
```

And replace the NEW_COV log call (line 395) from:

```rust
                    self.exec_logger.log(self.execution_count, "NEW_COV", code);
```

To:

```rust
                    let label = format!("{}:NEW_COV", strategy);
                    self.exec_logger.log(self.execution_count, &label, code);
```

- [ ] **Step 4: Update `run_on()` to pass the label to `exec()`**

In `run_on()` at line 188, change:

```rust
        let (new_bits, term_sig) = self.exec(code, tree, ctx)?;
```

To:

```rust
        let strategy = reason_label(&exec_reason);
        let (new_bits, term_sig) = self.exec(code, tree, ctx, strategy)?;
```

- [ ] **Step 5: Build and verify compilation**

Run:
```bash
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release 2>&1 | tail -5
```

Expected: compilation succeeds (warnings are OK, errors are not).

- [ ] **Step 6: Quick verification — run fuzzer for 5 seconds and check log format**

```bash
TMPDIR=$(mktemp -d /tmp/verify_XXXXXX)
mkdir -p "$TMPDIR/outputs/signaled" "$TMPDIR/outputs/queue" "$TMPDIR/outputs/timeout" "$TMPDIR/outputs/chunks"

cat > "$TMPDIR/config.ron" <<'EOF'
Config(
    path_to_bin_target: "harness/sqlite_harness_patterns_sqlite-3.31.1",
    arguments: ["@@"],
    path_to_grammar: "grammars/sqlite_patterns.py",
    path_to_workdir: "WORKDIR_PLACEHOLDER",
    number_of_threads: 1,
    timeout_in_millis: 500,
    bitmap_size: 65536,
    thread_size: 4194304,
    number_of_generate_inputs: 100,
    max_tree_size: 1000,
    number_of_deterministic_mutations: 1,
)
EOF
sed -i "s|WORKDIR_PLACEHOLDER|$TMPDIR|" "$TMPDIR/config.ron"

export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="$(python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

timeout 5 ./target/release/fuzzer -c "$TMPDIR/config.ron" >/dev/null 2>&1 || true

head -20 "$TMPDIR/exec.log"
```

Expected: log lines now contain strategy prefixes like `Gen:NEW_COV`, `Havoc:NEW_COV`, `Det:NEW_COV`, etc. The second tab-separated field should match `{Strategy}:{Event}`.

- [ ] **Step 7: Commit**

```bash
git add fuzzer/src/fuzzer.rs
git commit -m "feat(fuzzer): add strategy labels to exec.log for per-mutation observability"
```

---

### Task 2: Create deep_test.sh — Campaign + Report Skeleton

**Files:**
- Create: `scripts/deep_test.sh`

- [ ] **Step 1: Write the script with Phase 1 (campaign) and report header/footer**

```bash
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
GRAMMAR="$ROOT/grammars/sqlite_patterns.py"
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

# --- Report sections go here (Task 3) ---

echo ""
echo "==============================================================="
echo " SUMMARY"
echo "==============================================================="

# --- Summary goes here (Task 4) ---

TOTAL_LOG_LINES=$(wc -l < "$LOG")
echo ""
echo "Total exec.log lines: $TOTAL_LOG_LINES"
echo "Runtime: ${ELAPSED}s"
echo "==============================================================="

if [[ $FAILURES -gt 0 ]]; then
    exit 1
fi
exit 0
```

- [ ] **Step 2: Make executable and test the skeleton**

```bash
chmod +x scripts/deep_test.sh
```

Don't run it yet — it will run a 90s campaign. We'll test after adding the report sections.

- [ ] **Step 3: Commit**

```bash
git add scripts/deep_test.sh
git commit -m "test: scaffold deep_test.sh with campaign runner"
```

---

### Task 3: Add Report Sections S1–S7

**Files:**
- Modify: `scripts/deep_test.sh`

- [ ] **Step 1: Add S1–S5 (mutation strategy sections) and S6–S7 after the `# --- Report sections go here ---` comment**

Replace `# --- Report sections go here (Task 3) ---` with:

```bash
# Helper: check a mutation strategy in exec.log
check_strategy() {
    local num="$1"
    local title="$2"
    local grep_key="$3"
    local var_name="$4"

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
        echo "Verdict: NOT OBSERVED"
        FAILURES=$((FAILURES + 1))
    fi
    echo ""

    # Export count for summary
    eval "${var_name}=${count}"
}

check_strategy "1" "HAVOC MUTATION" "Havoc" "S1_COUNT"
check_strategy "2" "HAVOC RECURSION" "HavocRec" "S2_COUNT"
check_strategy "3" "SPLICE MUTATION" "Splice" "S3_COUNT"
check_strategy "4" "DETERMINISTIC MUTATION" "Det" "S4_COUNT"
check_strategy "5" "GENERATE (FRESH)" "Gen" "S5_COUNT"

# --- S6: Coverage Feedback ---
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

# --- S7: Crash Detection ---
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
    echo "The crash detection pipeline (ASan→exit 223→save) is wired correctly"
    echo "per smoke_test.sh T06-T09."
    S7_VERDICT="NOT OBSERVED (expected for ${ELAPSED}s)"
fi
echo ""
```

- [ ] **Step 2: Commit**

```bash
git add scripts/deep_test.sh
git commit -m "test(deep): add S1-S7 report sections for mutation, coverage, crash"
```

---

### Task 4: Add Summary Section and Exit Logic

**Files:**
- Modify: `scripts/deep_test.sh`

- [ ] **Step 1: Replace `# --- Summary goes here (Task 4) ---` with the summary block**

```bash
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
```

- [ ] **Step 2: Commit**

```bash
git add scripts/deep_test.sh
git commit -m "test(deep): add summary section and exit logic"
```

---

### Task 5: Full End-to-End Run

**Files:**
- No changes — just run and verify

- [ ] **Step 1: Run the deep test**

```bash
./scripts/deep_test.sh
```

This takes ~100 seconds. Expected: all 5 mutation strategies show VERIFIED with count > 0, coverage feedback VERIFIED, crash detection NOT OBSERVED. Exit code 0.

If any strategy shows NOT OBSERVED, that's a real bug — investigate which strategy is silent and why.

- [ ] **Step 2: Also re-run smoke_test.sh to verify we didn't break anything**

```bash
./scripts/smoke_test.sh
```

Expected: same results as before (10/11 PASS, 0 FAIL, 1 SKIP). The enriched logging shouldn't change behavior.

- [ ] **Step 3: Final commit if any fixes were needed**

```bash
git add scripts/deep_test.sh scripts/smoke_test.sh
git commit -m "test(deep): verified full end-to-end run, all strategies active"
```
