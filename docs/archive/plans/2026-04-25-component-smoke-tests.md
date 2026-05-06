# Component Smoke Tests Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create `scripts/smoke_test.sh` — a single bash script that runs 11 tests validating every major component of RL-Nautilus works correctly.

**Architecture:** One self-contained bash script. No new dependencies. Uses the existing `generator` and `fuzzer` release binaries plus the 4 harness binaries. Creates temp files/dirs in `/tmp/smoke_*`, cleans up on exit.

**Tech Stack:** Bash, existing release binaries (`target/release/generator`, `target/release/fuzzer`), harness binaries (`harness/sqlite_harness_patterns_sqlite-3.*`)

---

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| `scripts/smoke_test.sh` | Create | All 11 tests, setup/teardown, result reporting |

One file. That's it.

---

### Task 1: Script Skeleton — Setup, Teardown, Result Tracking

**Files:**
- Create: `scripts/smoke_test.sh`

- [ ] **Step 1: Write the script skeleton**

```bash
#!/usr/bin/env bash
# smoke_test.sh — Validate every major RL-Nautilus component
# Usage: ./scripts/smoke_test.sh
# Exit: 0 if all pass, 1 if any fail

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="$(python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

GENERATOR="$ROOT/target/release/generator"
FUZZER="$ROOT/target/release/fuzzer"
GRAMMAR="$ROOT/grammars/sqlite_patterns.py"
HARNESS="$ROOT/harness/sqlite_harness_patterns_sqlite-3.31.1"

TMPDIR=$(mktemp -d /tmp/smoke_XXXXXX)
trap 'rm -rf "$TMPDIR"' EXIT

PASSED=0
FAILED=0
SKIPPED=0

pass() { echo "[T${1}] ${2} $(printf '.%.0s' $(seq 1 $((40 - ${#2})))).. PASS"; PASSED=$((PASSED + 1)); }
fail() { echo "[T${1}] ${2} $(printf '.%.0s' $(seq 1 $((40 - ${#2})))).. FAIL — ${3}"; FAILED=$((FAILED + 1)); }
skip() { echo "[T${1}] ${2} $(printf '.%.0s' $(seq 1 $((40 - ${#2})))).. SKIP — ${3}"; SKIPPED=$((SKIPPED + 1)); }

# Preflight checks
for bin in "$GENERATOR" "$FUZZER" "$HARNESS"; do
    if [[ ! -x "$bin" ]]; then
        echo "FATAL: binary not found or not executable: $bin"
        echo "Run: make setup   (or: PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release)"
        exit 2
    fi
done

echo ""
echo "=== RL-Nautilus Component Smoke Tests ==="
echo ""

# --- Tests go here (Tasks 2-6) ---

echo ""
TOTAL=$((PASSED + FAILED + SKIPPED))
echo "Result: ${PASSED}/${TOTAL} PASSED, ${FAILED} FAILED, ${SKIPPED} SKIPPED"

if [[ $FAILED -gt 0 ]]; then
    exit 1
fi
exit 0
```

- [ ] **Step 2: Make it executable and run the skeleton**

Run:
```bash
chmod +x scripts/smoke_test.sh
./scripts/smoke_test.sh
```

Expected: Preflight checks pass (all 3 binaries exist), prints the header and `Result: 0/0 PASSED, 0 FAILED, 0 SKIPPED`, exits 0.

- [ ] **Step 3: Commit**

```bash
git add scripts/smoke_test.sh
git commit -m "test: scaffold smoke_test.sh with setup, teardown, result tracking"
```

---

### Task 2: Tests T01–T03 — Grammar Loading and Tree Generation

**Files:**
- Modify: `scripts/smoke_test.sh`

- [ ] **Step 1: Add T01, T02, T03 between the "Tests go here" comment and the summary**

Insert the following after the `# --- Tests go here ---` comment:

```bash
# ======================================================================
# T01: Grammar Loading
# ======================================================================
T01_OUT=$("$GENERATOR" -g "$GRAMMAR" -t 1 2>&1) && T01_RC=$? || T01_RC=$?
if [[ $T01_RC -eq 0 ]] && [[ -n "$T01_OUT" ]]; then
    pass "01" "Grammar Loading"
else
    fail "01" "Grammar Loading" "exit=$T01_RC, output_len=${#T01_OUT}"
fi

# ======================================================================
# T02: Tree Generation — Variety
# ======================================================================
T02_DIR="$TMPDIR/t02"
mkdir -p "$T02_DIR"
for i in $(seq 1 50); do
    "$GENERATOR" -g "$GRAMMAR" -t 20 2>/dev/null > "$T02_DIR/$i.sql"
done
T02_UNIQUE=$(sort -u "$T02_DIR"/*.sql | wc -l)
if [[ $T02_UNIQUE -ge 40 ]]; then
    pass "02" "Tree Generation — Variety"
else
    fail "02" "Tree Generation — Variety" "only $T02_UNIQUE/50 unique (need >=40)"
fi

# ======================================================================
# T03: Tree Generation — Validity
# ======================================================================
T03_BAD=0
SQL_KW="SELECT\|CREATE\|INSERT\|PRAGMA\|WITH\|VALUES\|DROP\|ALTER\|EXPLAIN\|ANALYZE\|ATTACH\|DELETE\|UPDATE"
for f in "$T02_DIR"/*.sql; do
    if ! grep -qi "$SQL_KW" "$f"; then
        T03_BAD=$((T03_BAD + 1))
    fi
done
if [[ $T03_BAD -eq 0 ]]; then
    pass "03" "Tree Generation — Validity"
else
    fail "03" "Tree Generation — Validity" "$T03_BAD/50 outputs have no SQL keyword"
fi
```

- [ ] **Step 2: Run and verify T01–T03 pass**

Run:
```bash
./scripts/smoke_test.sh
```

Expected: T01 PASS, T02 PASS (>=40 unique), T03 PASS (0 bad).

- [ ] **Step 3: Commit**

```bash
git add scripts/smoke_test.sh
git commit -m "test(smoke): add T01-T03 grammar loading and tree generation"
```

---

### Task 3: Tests T04–T05 — Weighted Sampling and Depth Budget

**Files:**
- Modify: `scripts/smoke_test.sh`

- [ ] **Step 1: Add T04 and T05 after T03**

```bash
# ======================================================================
# T04: Weighted Sampling Bias
# ======================================================================
T04_DIR="$TMPDIR/t04"
mkdir -p "$T04_DIR"
for i in $(seq 1 200); do
    "$GENERATOR" -g "$GRAMMAR" -t 5 2>/dev/null >> "$T04_DIR/all.sql"
done
# High-weight patterns (weight 2.0-3.0): printf, WINDOW, RECURSIVE, INTERSECT, EXCEPT, integrity_check, GENERATED
T04_HI=$(grep -ci 'printf\|WINDOW\|RECURSIVE\|INTERSECT\|EXCEPT\|integrity_check\|GENERATED' "$T04_DIR/all.sql" || true)
# Low-weight patterns (weight 0.2): ATTACH, DROP, CREATE INDEX
T04_LO=$(grep -ci 'ATTACH\|CREATE INDEX' "$T04_DIR/all.sql" || true)
if [[ $T04_HI -gt $T04_LO ]]; then
    pass "04" "Weighted Sampling Bias"
else
    fail "04" "Weighted Sampling Bias" "high=$T04_HI <= low=$T04_LO"
fi

# ======================================================================
# T05: Mutation Budget (depth effect)
# ======================================================================
T05_SHORT=0
for i in $(seq 1 10); do
    LEN=$("$GENERATOR" -g "$GRAMMAR" -t 5 2>/dev/null | wc -c)
    T05_SHORT=$((T05_SHORT + LEN))
done
T05_LONG=0
for i in $(seq 1 10); do
    LEN=$("$GENERATOR" -g "$GRAMMAR" -t 50 2>/dev/null | wc -c)
    T05_LONG=$((T05_LONG + LEN))
done
T05_AVG_SHORT=$((T05_SHORT / 10))
T05_AVG_LONG=$((T05_LONG / 10))
if [[ $T05_AVG_LONG -gt $((T05_AVG_SHORT * 2)) ]]; then
    pass "05" "Mutation Budget (depth effect)"
else
    fail "05" "Mutation Budget (depth effect)" "avg_short=${T05_AVG_SHORT}B, avg_long=${T05_AVG_LONG}B (need 2x)"
fi
```

- [ ] **Step 2: Run and verify T04–T05 pass**

Run:
```bash
./scripts/smoke_test.sh
```

Expected: T04 PASS (high > low), T05 PASS (long > 2× short).

- [ ] **Step 3: Commit**

```bash
git add scripts/smoke_test.sh
git commit -m "test(smoke): add T04-T05 weighted sampling and depth budget"
```

---

### Task 4: Tests T06–T09 — Harness Tests

**Files:**
- Modify: `scripts/smoke_test.sh`

- [ ] **Step 1: Add T06, T07, T08, T09 after T05**

```bash
# ======================================================================
# T06: Harness — Normal Exit
# ======================================================================
T06_INPUT="$TMPDIR/t06.sql"
echo "SELECT 1;" > "$T06_INPUT"
"$HARNESS" "$T06_INPUT" >/dev/null 2>&1 && T06_RC=$? || T06_RC=$?
if [[ $T06_RC -eq 0 ]]; then
    pass "06" "Harness — Normal Exit"
else
    fail "06" "Harness — Normal Exit" "exit=$T06_RC (expected 0)"
fi

# ======================================================================
# T07: Harness — Error Tolerance
# ======================================================================
T07_INPUT="$TMPDIR/t07.sql"
echo 'THIS IS NOT SQL AT ALL !@#$%^&*()' > "$T07_INPUT"
"$HARNESS" "$T07_INPUT" >/dev/null 2>&1 && T07_RC=$? || T07_RC=$?
if [[ $T07_RC -eq 0 ]]; then
    pass "07" "Harness — Error Tolerance"
else
    fail "07" "Harness — Error Tolerance" "exit=$T07_RC (expected 0)"
fi

# ======================================================================
# T08: Harness — Crash Detection
# ======================================================================
T08_INPUT="$TMPDIR/t08.sql"
T08_CRASHED=false

# Candidate 1: CVE-2020-13434 integer overflow in printf
echo "SELECT printf('%.*c', 2147483647, 42);" > "$T08_INPUT"
"$HARNESS" "$T08_INPUT" >/dev/null 2>&1 && T08_RC=$? || T08_RC=$?
if [[ $T08_RC -ne 0 ]]; then
    T08_CRASHED=true
    T08_DETAIL="printf overflow → exit $T08_RC"
fi

# Candidate 2: zeroblob large allocation
if [[ "$T08_CRASHED" == false ]]; then
    echo "SELECT zeroblob(2147483647);" > "$T08_INPUT"
    "$HARNESS" "$T08_INPUT" >/dev/null 2>&1 && T08_RC=$? || T08_RC=$?
    if [[ $T08_RC -ne 0 ]]; then
        T08_CRASHED=true
        T08_DETAIL="zeroblob → exit $T08_RC"
    fi
fi

# Candidate 3: deep recursive CTE (stack pressure)
if [[ "$T08_CRASHED" == false ]]; then
    echo "WITH RECURSIVE c(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM c WHERE x<100000000) SELECT sum(x) FROM c;" > "$T08_INPUT"
    timeout 5 "$HARNESS" "$T08_INPUT" >/dev/null 2>&1 && T08_RC=$? || T08_RC=$?
    if [[ $T08_RC -ne 0 ]] && [[ $T08_RC -ne 124 ]]; then
        T08_CRASHED=true
        T08_DETAIL="deep CTE → exit $T08_RC"
    fi
fi

if [[ "$T08_CRASHED" == true ]]; then
    pass "08" "Harness — Crash Detection"
    echo "         detail: $T08_DETAIL"
else
    skip "08" "Harness — Crash Detection" "no candidate triggered non-zero exit; harness may lack ASan"
fi

# ======================================================================
# T09: Harness — Multi-Version
# ======================================================================
T09_INPUT="$TMPDIR/t09.sql"
echo "SELECT 1;" > "$T09_INPUT"
T09_ALL_OK=true
T09_DETAIL=""
for ver in sqlite-3.30.1 sqlite-3.31.1 sqlite-3.32.0 sqlite-3.32.2; do
    H="$ROOT/harness/sqlite_harness_patterns_${ver}"
    if [[ ! -x "$H" ]]; then
        T09_ALL_OK=false
        T09_DETAIL="missing: $H"
        break
    fi
    "$H" "$T09_INPUT" >/dev/null 2>&1 && rc=$? || rc=$?
    if [[ $rc -ne 0 ]]; then
        T09_ALL_OK=false
        T09_DETAIL="$ver exit=$rc"
        break
    fi
done
if [[ "$T09_ALL_OK" == true ]]; then
    pass "09" "Harness — Multi-Version"
else
    fail "09" "Harness — Multi-Version" "$T09_DETAIL"
fi
```

- [ ] **Step 2: Run and verify T06–T09**

Run:
```bash
./scripts/smoke_test.sh
```

Expected: T06 PASS, T07 PASS, T08 PASS or SKIP, T09 PASS.

- [ ] **Step 3: Commit**

```bash
git add scripts/smoke_test.sh
git commit -m "test(smoke): add T06-T09 harness normal exit, error tolerance, crash detection, multi-version"
```

---

### Task 5: Tests T10–T11 — Fork Server and Integration Campaign

**Files:**
- Modify: `scripts/smoke_test.sh`

- [ ] **Step 1: Add T10 and T11 after T09**

```bash
# ======================================================================
# T10: Fork Server + Coverage (10s)
# ======================================================================
T10_WORKDIR="$TMPDIR/t10_workdir"
mkdir -p "$T10_WORKDIR/outputs/signaled" "$T10_WORKDIR/outputs/queue" "$T10_WORKDIR/outputs/timeout" "$T10_WORKDIR/outputs/chunks"
T10_CONFIG="$TMPDIR/t10_config.ron"
cat > "$T10_CONFIG" <<EORON
Config(
    path_to_bin_target: "$HARNESS",
    arguments: ["@@"],
    path_to_grammar: "$GRAMMAR",
    path_to_workdir: "$T10_WORKDIR",
    number_of_threads: 1,
    timeout_in_millis: 500,
    bitmap_size: 65536,
    thread_size: 4194304,
    number_of_generate_inputs: 100,
    max_tree_size: 1000,
    number_of_deterministic_mutations: 1,
)
EORON

timeout 10 "$FUZZER" -c "$T10_CONFIG" >/dev/null 2>&1 || true

T10_LOG="$T10_WORKDIR/exec.log"
T10_QUEUE=$(find "$T10_WORKDIR/outputs/queue" -type f 2>/dev/null | wc -l)
if [[ -s "$T10_LOG" ]] && [[ $T10_QUEUE -ge 1 ]]; then
    pass "10" "Fork Server + Coverage (10s)"
else
    T10_LOG_SIZE=0
    [[ -f "$T10_LOG" ]] && T10_LOG_SIZE=$(wc -c < "$T10_LOG")
    fail "10" "Fork Server + Coverage (10s)" "exec.log=${T10_LOG_SIZE}B, queue_files=${T10_QUEUE}"
fi

# ======================================================================
# T11: Integration Campaign (60s)
# ======================================================================
T11_WORKDIR="$TMPDIR/t11_workdir"
mkdir -p "$T11_WORKDIR/outputs/signaled" "$T11_WORKDIR/outputs/queue" "$T11_WORKDIR/outputs/timeout" "$T11_WORKDIR/outputs/chunks"
T11_CONFIG="$TMPDIR/t11_config.ron"
cat > "$T11_CONFIG" <<EORON
Config(
    path_to_bin_target: "$HARNESS",
    arguments: ["@@"],
    path_to_grammar: "$GRAMMAR",
    path_to_workdir: "$T11_WORKDIR",
    number_of_threads: 1,
    timeout_in_millis: 500,
    bitmap_size: 65536,
    thread_size: 4194304,
    number_of_generate_inputs: 100,
    max_tree_size: 1000,
    number_of_deterministic_mutations: 1,
)
EORON

timeout 60 "$FUZZER" -c "$T11_CONFIG" >/dev/null 2>&1 || true

T11_LOG="$T11_WORKDIR/exec.log"
T11_LOG_LINES=0
[[ -f "$T11_LOG" ]] && T11_LOG_LINES=$(wc -l < "$T11_LOG")
T11_QUEUE=$(find "$T11_WORKDIR/outputs/queue" -type f 2>/dev/null | wc -l)
T11_CHUNKS=$(find "$T11_WORKDIR/outputs/chunks" -type f 2>/dev/null | wc -l)

T11_PROBLEMS=""
if [[ $T11_LOG_LINES -lt 100 ]]; then
    T11_PROBLEMS="exec.log only ${T11_LOG_LINES} lines (need >=100); "
fi
if [[ $T11_QUEUE -lt 5 ]]; then
    T11_PROBLEMS="${T11_PROBLEMS}queue only ${T11_QUEUE} files (need >=5); "
fi
if [[ $T11_CHUNKS -lt 10 ]]; then
    T11_PROBLEMS="${T11_PROBLEMS}chunks only ${T11_CHUNKS} files (need >=10); "
fi

if [[ -z "$T11_PROBLEMS" ]]; then
    pass "11" "Integration Campaign (60s)"
    echo "         log_lines=$T11_LOG_LINES queue=$T11_QUEUE chunks=$T11_CHUNKS"
else
    fail "11" "Integration Campaign (60s)" "$T11_PROBLEMS"
fi
```

- [ ] **Step 2: Run T01–T09 only first (quick sanity check)**

To avoid waiting 70s every iteration, first verify T01–T09 still work by temporarily commenting out T10+T11, or just run the full script if you're ready:

Run:
```bash
./scripts/smoke_test.sh
```

Expected: T01–T09 same as before, T10 PASS (exec.log non-empty, ≥1 queue file after 10s), T11 PASS (≥100 log lines, ≥5 queue, ≥10 chunks after 60s).

Note: T10+T11 take ~70 seconds total. If T10 fails, T11 will likely also fail for the same reason — diagnose T10 first.

- [ ] **Step 3: Commit**

```bash
git add scripts/smoke_test.sh
git commit -m "test(smoke): add T10-T11 fork server coverage and 60s integration campaign"
```

---

### Task 6: Final Polish and Full Run

**Files:**
- Modify: `scripts/smoke_test.sh`

- [ ] **Step 1: Add a timing header and total runtime measurement**

At the top, after the `echo "=== RL-Nautilus Component Smoke Tests ==="` line, add:

```bash
SMOKE_START=$(date +%s)
```

And before the final `Result:` line, add:

```bash
SMOKE_END=$(date +%s)
SMOKE_ELAPSED=$((SMOKE_END - SMOKE_START))
echo "Runtime: ${SMOKE_ELAPSED}s"
```

- [ ] **Step 2: Run the complete script end-to-end**

Run:
```bash
./scripts/smoke_test.sh
```

Expected output matches the format from the spec:
```
=== RL-Nautilus Component Smoke Tests ===

[T01] Grammar Loading ..................... PASS
[T02] Tree Generation — Variety ........... PASS
[T03] Tree Generation — Validity .......... PASS
[T04] Weighted Sampling Bias .............. PASS
[T05] Mutation Budget (depth effect) ...... PASS
[T06] Harness — Normal Exit ............... PASS
[T07] Harness — Error Tolerance ........... PASS
[T08] Harness — Crash Detection ........... PASS/SKIP
[T09] Harness — Multi-Version ............. PASS
[T10] Fork Server + Coverage (10s) ........ PASS
[T11] Integration Campaign (60s) .......... PASS

Runtime: ~100s
Result: 10/11 PASSED, 0 FAILED, 1 SKIPPED
```

Exit code 0 (or 1 if any real failures found — which means we've discovered a real issue).

- [ ] **Step 3: Final commit**

```bash
git add scripts/smoke_test.sh
git commit -m "test(smoke): complete 11-test component smoke suite with timing"
```
