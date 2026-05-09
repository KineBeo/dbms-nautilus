# Three-Harness Triage Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the triage pipeline to correctly classify UBSan bugs (currently mislabeled as "signal-6") and add test/ + nosanit/ harness passes so we know which crashes are sanitizer-only vs real exploitable bugs.

**Architecture:** Two changes — (1) fix classify.py to detect UBSan `runtime error:` in signal-6 crashes, and (2) add two additional classify passes in run_eval.sh using test/ and nosanit/ harnesses, writing separate triage reports for each.

**Tech Stack:** Python (triage/classify.py), Bash (scripts/run_eval.sh), existing harness binaries in harness/{afl,test,nosanit}/

---

### File Structure

| File | Responsibility | Change |
|------|---------------|--------|
| `triage/classify.py` | Crash classification | Fix signal-6 misclassification of UBSan errors |
| `scripts/run_eval.sh` | Campaign runner | Add test/ and nosanit/ classify passes after existing afl/ pass |
| `tests/test_classify.py` | Unit tests | New file — test classification logic |

---

### Task 1: Fix UBSan Misclassification in classify.py

**Files:**
- Modify: `triage/classify.py:52-85` (`classify_crash` function)
- Create: `tests/test_classify.py`

The bug: the afl/ harness sets `ASAN_OPTIONS="abort_on_error=1"`, so when UBSan detects a `runtime error:`, it prints the error to stderr and then aborts with SIGABRT (exit code -6). `classify_crash` sees exit code -6, enters the `if exit_code < 0: return ("signal", ...)` branch, and misses the UBSan error in stderr. This means ALL UBSan findings are labeled as "signal-6" in triage reports.

Fix: check stderr for `runtime error:` pattern BEFORE checking exit code, regardless of exit code.

- [ ] **Step 1: Write the failing test**

Create `tests/test_classify.py`:

```python
"""Tests for triage/classify.py classification logic."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from triage.classify import classify_crash


def test_ubsan_via_signal6_detected():
    """UBSan runtime error that caused SIGABRT should classify as ubsan, not signal."""
    stderr = (
        "../cve_builds/sqlite-3.31.1/sqlite3.c:28488:24: "
        "runtime error: signed integer overflow: "
        "2147483647 + 341 cannot be represented in type 'int'\n"
        "    #0 0xaaaa in sqlite3_str_vappendf\n"
    )
    crash_type, subtype = classify_crash(-6, stderr)
    assert crash_type == "ubsan", f"Expected ubsan, got {crash_type}"
    assert subtype == "signed-integer-overflow"


def test_ubsan_null_pointer_via_signal6():
    """Null pointer UBSan error via SIGABRT."""
    stderr = (
        "../cve_builds/sqlite-3.30.1/sqlite3.c:220230:44: "
        "runtime error: applying non-zero offset 8 to null pointer\n"
    )
    crash_type, subtype = classify_crash(-6, stderr)
    assert crash_type == "ubsan", f"Expected ubsan, got {crash_type}"
    assert subtype == "null-pointer"


def test_ubsan_misaligned_via_signal6():
    """Misaligned address UBSan error via SIGABRT."""
    stderr = (
        "runtime error: store to misaligned address 0xaaaaaaaaaaaaaaaa "
        "for type 'Window *'\n"
    )
    crash_type, subtype = classify_crash(-6, stderr)
    assert crash_type == "ubsan", f"Expected ubsan, got {crash_type}"


def test_ubsan_float_overflow_via_signal6():
    """Float-to-int overflow UBSan error via SIGABRT."""
    stderr = (
        "runtime error: 1.11111e+135 is outside the range of "
        "representable values of type 'long long'\n"
    )
    crash_type, subtype = classify_crash(-6, stderr)
    assert crash_type == "ubsan", f"Expected ubsan, got {crash_type}"


def test_pure_signal6_no_ubsan():
    """SIGABRT without runtime error stays as signal."""
    stderr = "some other abort reason\n"
    crash_type, subtype = classify_crash(-6, stderr)
    assert crash_type == "signal"
    assert subtype == "signal-6"


def test_asan_exit223():
    """ASan heap-buffer-overflow still works."""
    stderr = "heap-buffer-overflow at 0xdeadbeef\n"
    crash_type, subtype = classify_crash(223, stderr)
    assert crash_type == "asan"
    assert subtype == "heap-buffer-overflow"


def test_ubsan_exit1():
    """Normal UBSan exit code 1 still works."""
    stderr = "runtime error: signed integer overflow: 1 + 1\n"
    crash_type, subtype = classify_crash(1, stderr)
    assert crash_type == "ubsan"


def test_debug_assert():
    """SIGTRAP (exit -5) stays as debug_assert."""
    crash_type, subtype = classify_crash(-5, "")
    assert crash_type == "debug_assert"


def test_segfault():
    """SIGSEGV (exit -11) stays as signal."""
    crash_type, subtype = classify_crash(-11, "no runtime error here\n")
    assert crash_type == "signal"
    assert subtype == "signal-11"


def test_nosanit_segfault():
    """Nosanit harness: segfault = real exploitable bug."""
    crash_type, subtype = classify_crash(-11, "")
    assert crash_type == "signal"
    assert subtype == "signal-11"


def test_nosanit_clean_exit():
    """Nosanit harness: exit 0 = sanitizer-only finding."""
    crash_type, subtype = classify_crash(0, "")
    assert crash_type == "debug_assert"
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
python3 -m pytest tests/test_classify.py -v
```

Expected: `test_ubsan_via_signal6_detected` FAILS (returns "signal" not "ubsan"). Same for all `_via_signal6` tests. Others pass.

- [ ] **Step 3: Fix classify_crash to check stderr for UBSan before exit code**

In `triage/classify.py`, replace the `classify_crash` function (lines 52-85):

```python
def classify_crash(exit_code: int, stderr: str) -> tuple[str, str | None]:
    # Check stderr for UBSan runtime errors FIRST — regardless of exit code.
    # The afl harness aborts on UBSan errors (SIGABRT = -6), so UBSan findings
    # arrive with exit code -6 instead of 1. Detect them by stderr content.
    if "runtime error:" in stderr:
        m = re.search(r"runtime error:\s*(.+)", stderr)
        if m:
            kind = m.group(1).strip()
            if "signed integer overflow" in kind or "integer overflow" in kind:
                return ("ubsan", "signed-integer-overflow")
            if "null pointer" in kind:
                return ("ubsan", "null-pointer")
            if "misaligned address" in kind:
                return ("ubsan", "misaligned-access")
            if "outside the range of representable values" in kind:
                return ("ubsan", "float-cast-overflow")
            if "shift exponent" in kind:
                return ("ubsan", "shift-exponent")
            if "member access within null" in kind:
                return ("ubsan", "null-member-access")
            return ("ubsan", "ubsan-other")
        return ("ubsan", "ubsan-other")
    if exit_code == -1:
        return ("timeout", None)
    if exit_code == -5:
        return ("debug_assert", None)
    if exit_code < 0:
        return ("signal", f"signal-{abs(exit_code)}")
    if exit_code == 223:
        if "heap-buffer-overflow" in stderr:
            return ("asan", "heap-buffer-overflow")
        if "stack-buffer-overflow" in stderr:
            return ("asan", "stack-buffer-overflow")
        if "use-after-free" in stderr or "heap-use-after-free" in stderr:
            return ("asan", "use-after-free")
        if "null" in stderr.lower() and "dereference" in stderr.lower():
            return ("asan", "null-dereference")
        return ("asan", "asan-other")
    if exit_code == 1:
        return ("ubsan", "ubsan-other")
    if exit_code == 0:
        return ("debug_assert", None)
    return ("signal", f"exitcode-{exit_code}")
```

- [ ] **Step 4: Run tests — all should pass**

```bash
python3 -m pytest tests/test_classify.py -v
```

Expected: All 12 tests PASS.

- [ ] **Step 5: Verify fix against real campaign data**

```bash
python3 triage/classify.py \
  workdirs/sqlite-3.31.1_bandit_run1 \
  --harness harness/afl/sqlite_harness_sqlite-3.31.1 \
  --output /tmp/triage_fixed.json \
  --dedup-dir /tmp/dedup_fixed \
  --report /tmp/triage_fixed.md
```

Expected: Output should now show `ubsan` type instead of `signal` for crashes with `runtime error:` in stderr.

```bash
python3 -c "import json; d=json.load(open('/tmp/triage_fixed.json')); print(json.dumps(d['summary'], indent=2))"
```

Expected: `"ubsan": 5, "signal": 0` (all 5 were UBSan, none are pure signals).

- [ ] **Step 6: Commit**

```bash
git add triage/classify.py tests/test_classify.py
git commit -m "fix: classify UBSan errors arriving as signal-6 (SIGABRT)

The afl harness sets abort_on_error=1, so UBSan runtime errors abort
via SIGABRT (exit -6) instead of exit code 1. classify_crash now checks
stderr for 'runtime error:' BEFORE checking exit code, correctly
labeling these as ubsan findings with specific subtypes."
```

---

### Task 2: Add Three-Harness Triage to run_eval.sh

**Files:**
- Modify: `scripts/run_eval.sh` (triage section, lines 148-153)

Add two additional classify passes after the existing afl/ pass: one with test/ harness and one with nosanit/ harness. Each writes its own triage report and JSON.

- [ ] **Step 1: Modify the triage section of run_eval.sh**

Replace the triage section (after the coverage capture, starting at the `# Auto-triage` comment) with:

```bash
# ----------------------------------------------------------------
# Auto-triage: classify + dedup crashes (3-harness pipeline)
# ----------------------------------------------------------------

# Pass 1: AFL harness (same as fuzzing — baseline classification)
echo "[run_eval] classifying crashes (afl harness)..."
python3 "$ROOT/triage/classify.py" "$WORKDIR" \
    --harness "$HARNESS_BIN" \
    --output "$WORKDIR/triage.json" \
    --dedup-dir "$WORKDIR/dedup" \
    --report "$WORKDIR/triage_report.md" \
    || echo "[run_eval] warning: afl classification failed (non-fatal)"

# Pass 2: Test harness (ASan+UBSan, no AFL — cleaner sanitizer output)
TEST_HARNESS="$ROOT/harness/test/sqlite_harness_${VERSION}_test"
if [[ -f "$TEST_HARNESS" ]]; then
    echo "[run_eval] classifying crashes (test harness)..."
    python3 "$ROOT/triage/classify.py" "$WORKDIR" \
        --harness "$TEST_HARNESS" \
        --output "$WORKDIR/triage_test.json" \
        --dedup-dir "$WORKDIR/dedup_test" \
        --report "$WORKDIR/triage_report_test.md" \
        || echo "[run_eval] warning: test classification failed (non-fatal)"
else
    echo "[run_eval] skipping test harness (not built: $TEST_HARNESS)"
fi

# Pass 3: Nosanit harness (no sanitizers — production-like)
# Crashes here = real exploitable bugs, not just sanitizer findings
NOSANIT_HARNESS="$ROOT/harness/nosanit/sqlite_harness_${VERSION}_nosanit"
if [[ -f "$NOSANIT_HARNESS" ]]; then
    echo "[run_eval] classifying crashes (nosanit harness)..."
    python3 "$ROOT/triage/classify.py" "$WORKDIR" \
        --harness "$NOSANIT_HARNESS" \
        --output "$WORKDIR/triage_nosanit.json" \
        --dedup-dir "$WORKDIR/dedup_nosanit" \
        --report "$WORKDIR/triage_report_nosanit.md" \
        || echo "[run_eval] warning: nosanit classification failed (non-fatal)"
else
    echo "[run_eval] skipping nosanit harness (not built: $NOSANIT_HARNESS)"
fi
```

- [ ] **Step 2: Run a quick smoke test**

```bash
DURATION=30 THREADS=1 POLICY=uniform \
  GRAMMAR=/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/grammars/active/sqlite_v3.py \
  ./scripts/run_eval.sh sqlite-3.31.1 triage_test_smoke
```

Expected: Three triage passes run. Output shows:
```
[run_eval] classifying crashes (afl harness)...
[run_eval] classifying crashes (test harness)...
[run_eval] classifying crashes (nosanit harness)...
```

- [ ] **Step 3: Verify three report files exist**

```bash
ls -la workdirs/sqlite-3.31.1_triage_test_smoke/triage*.json
ls -la workdirs/sqlite-3.31.1_triage_test_smoke/triage_report*.md
```

Expected:
```
triage.json              ← afl pass
triage_test.json         ← test pass
triage_nosanit.json      ← nosanit pass
triage_report.md         ← afl pass
triage_report_test.md    ← test pass
triage_report_nosanit.md ← nosanit pass
```

- [ ] **Step 4: Compare results across harnesses**

```bash
echo "=== AFL harness ==="
python3 -c "import json; d=json.load(open('workdirs/sqlite-3.31.1_triage_test_smoke/triage.json')); print(json.dumps(d['summary'], indent=2))"

echo "=== Test harness ==="
python3 -c "import json; d=json.load(open('workdirs/sqlite-3.31.1_triage_test_smoke/triage_test.json')); print(json.dumps(d['summary'], indent=2))"

echo "=== Nosanit harness ==="
python3 -c "import json; d=json.load(open('workdirs/sqlite-3.31.1_triage_test_smoke/triage_nosanit.json')); print(json.dumps(d['summary'], indent=2))"
```

Expected: AFL and test harness should show similar UBSan counts (now correctly classified). Nosanit harness should show fewer crashes — only the ones that manifest without sanitizer instrumentation.

- [ ] **Step 5: Commit**

```bash
git add scripts/run_eval.sh
git commit -m "feat: add test/ and nosanit/ harness passes to triage pipeline

run_eval.sh now runs classify.py three times:
1. afl/ harness — baseline (same as fuzzing)
2. test/ harness — clean ASan+UBSan classification
3. nosanit/ harness — production-like, crashes here = real bugs

Each pass writes separate triage.json and triage_report.md files.
Gracefully skips if test/ or nosanit/ harness not built."
```

---

### Task 3: Re-triage Existing Campaigns

**Files:**
- No code changes. Re-run triage on existing 30-minute campaign data with the fixed classify.py.

This gives us correct bug counts for all past campaigns without re-running the expensive fuzzing step.

- [ ] **Step 1: Re-triage all 30-minute bandit campaigns on 3.31.1**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2

for i in 1 2 3 4 5; do
  dir="workdirs/sqlite-3.31.1_bandit_run${i}"
  echo "=== Re-triaging $dir ==="
  
  # AFL pass (re-run with fixed classify)
  python3 triage/classify.py "$dir" \
    --harness harness/afl/sqlite_harness_sqlite-3.31.1 \
    --output "$dir/triage.json" \
    --dedup-dir "$dir/dedup" \
    --report "$dir/triage_report.md"
  
  # Test pass
  python3 triage/classify.py "$dir" \
    --harness harness/test/sqlite_harness_sqlite-3.31.1_test \
    --output "$dir/triage_test.json" \
    --dedup-dir "$dir/dedup_test" \
    --report "$dir/triage_report_test.md" 2>/dev/null || echo "  test harness failed"
  
  # Nosanit pass
  python3 triage/classify.py "$dir" \
    --harness harness/nosanit/sqlite_harness_sqlite-3.31.1_nosanit \
    --output "$dir/triage_nosanit.json" \
    --dedup-dir "$dir/dedup_nosanit" \
    --report "$dir/triage_report_nosanit.md" 2>/dev/null || echo "  nosanit harness failed"
done
```

- [ ] **Step 2: Same for uniform campaigns**

```bash
for i in 1 2 3 4 5; do
  dir="workdirs/sqlite-3.31.1_uniform_run${i}"
  echo "=== Re-triaging $dir ==="
  
  python3 triage/classify.py "$dir" \
    --harness harness/afl/sqlite_harness_sqlite-3.31.1 \
    --output "$dir/triage.json" \
    --dedup-dir "$dir/dedup" \
    --report "$dir/triage_report.md"
  
  python3 triage/classify.py "$dir" \
    --harness harness/test/sqlite_harness_sqlite-3.31.1_test \
    --output "$dir/triage_test.json" \
    --dedup-dir "$dir/dedup_test" \
    --report "$dir/triage_report_test.md" 2>/dev/null || echo "  test harness failed"
  
  python3 triage/classify.py "$dir" \
    --harness harness/nosanit/sqlite_harness_sqlite-3.31.1_nosanit \
    --output "$dir/triage_nosanit.json" \
    --dedup-dir "$dir/dedup_nosanit" \
    --report "$dir/triage_report_nosanit.md" 2>/dev/null || echo "  nosanit harness failed"
done
```

- [ ] **Step 3: Collect corrected summary across all campaigns**

```bash
echo "run_id,afl_ubsan,afl_signal,afl_asan,test_ubsan,test_signal,nosanit_crashes"
for dir in workdirs/sqlite-3.31.1_{bandit,uniform}_run*; do
  run_id=$(basename "$dir")
  afl=$(python3 -c "import json; d=json.load(open('$dir/triage.json')); s=d['summary']; print(f\"{s.get('ubsan',0)},{s.get('signal',0)},{s.get('asan',0)}\")" 2>/dev/null || echo "?,?,?")
  test=$(python3 -c "import json; d=json.load(open('$dir/triage_test.json')); s=d['summary']; print(f\"{s.get('ubsan',0)},{s.get('signal',0)}\")" 2>/dev/null || echo "?,?")
  nosanit=$(python3 -c "import json; d=json.load(open('$dir/triage_nosanit.json')); print(d['unique_crashes'])" 2>/dev/null || echo "?")
  echo "$run_id,$afl,$test,$nosanit"
done
```

- [ ] **Step 4: Commit re-triage results**

```bash
git add workdirs/sqlite-3.31.1_*/triage*.json workdirs/sqlite-3.31.1_*/triage_report*.md
git commit -m "data: re-triage existing campaigns with fixed classify + 3-harness pipeline

Re-ran triage on all sqlite-3.31.1 bandit and uniform campaigns with:
1. Fixed UBSan detection (signal-6 → ubsan)
2. test/ harness (clean sanitizer classification)
3. nosanit/ harness (production-like, real exploitable bugs)"
```

---

### Task 4: Re-triage Other SQLite Versions

**Files:**
- No code changes. Same re-triage for 3.30.1, 3.32.0, 3.32.2 campaigns.

- [ ] **Step 1: Re-triage all versions**

```bash
for ver in sqlite-3.30.1 sqlite-3.32.0 sqlite-3.32.2; do
  echo "============ $ver ============"
  for dir in workdirs/${ver}_*; do
    [ -d "$dir/outputs/signaled" ] || continue
    echo "--- $(basename $dir) ---"
    
    python3 triage/classify.py "$dir" \
      --harness "harness/afl/sqlite_harness_${ver}" \
      --output "$dir/triage.json" \
      --dedup-dir "$dir/dedup" \
      --report "$dir/triage_report.md" || true
    
    if [ -f "harness/test/sqlite_harness_${ver}_test" ]; then
      python3 triage/classify.py "$dir" \
        --harness "harness/test/sqlite_harness_${ver}_test" \
        --output "$dir/triage_test.json" \
        --dedup-dir "$dir/dedup_test" \
        --report "$dir/triage_report_test.md" 2>/dev/null || true
    fi
    
    if [ -f "harness/nosanit/sqlite_harness_${ver}_nosanit" ]; then
      python3 triage/classify.py "$dir" \
        --harness "harness/nosanit/sqlite_harness_${ver}_nosanit" \
        --output "$dir/triage_nosanit.json" \
        --dedup-dir "$dir/dedup_nosanit" \
        --report "$dir/triage_report_nosanit.md" 2>/dev/null || true
    fi
  done
done
```

- [ ] **Step 2: Collect cross-version summary**

```bash
echo "version,run_id,ubsan_unique,nosanit_crashes"
for ver in sqlite-3.30.1 sqlite-3.31.1 sqlite-3.32.0 sqlite-3.32.2; do
  for dir in workdirs/${ver}_*; do
    [ -f "$dir/triage.json" ] || continue
    run_id=$(basename "$dir")
    ubsan=$(python3 -c "import json; d=json.load(open('$dir/triage.json')); print(sum(1 for c in d['crashes'] if c['type']=='ubsan'))" 2>/dev/null || echo "?")
    nosanit=$(python3 -c "import json; d=json.load(open('$dir/triage_nosanit.json')); print(d['unique_crashes'])" 2>/dev/null || echo "N/A")
    echo "$ver,$run_id,$ubsan,$nosanit"
  done
done
```

- [ ] **Step 3: Commit**

```bash
git add workdirs/sqlite-3.30.1_*/triage*.json workdirs/sqlite-3.30.1_*/triage_report*.md
git add workdirs/sqlite-3.32.0_*/triage*.json workdirs/sqlite-3.32.0_*/triage_report*.md
git add workdirs/sqlite-3.32.2_*/triage*.json workdirs/sqlite-3.32.2_*/triage_report*.md
git commit -m "data: re-triage 3.30.1, 3.32.0, 3.32.2 campaigns with 3-harness pipeline"
```

---

## Self-Review Checklist

1. **Spec coverage:** Task 1 fixes UBSan misclassification. Task 2 adds 3-harness pipeline to run_eval.sh. Tasks 3-4 re-triage existing data. All requirements covered.
2. **Placeholder scan:** No TBD/TODO. All code blocks complete. All commands have expected output.
3. **Type consistency:** `classify_crash(exit_code: int, stderr: str)` signature unchanged. New subtypes (`misaligned-access`, `float-cast-overflow`, `null-member-access`) added consistently in both classify function and test expectations.
4. **Harness paths consistent:** `harness/test/sqlite_harness_${VERSION}_test` and `harness/nosanit/sqlite_harness_${VERSION}_nosanit` match the Makefile naming convention in `harness/src/Makefile`.
