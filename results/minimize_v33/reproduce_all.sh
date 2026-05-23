#!/bin/bash
# reproduce_all.sh — Reproduce all 13 bug classes and 5 CVE PoCs in one run.
# Each entry: BC/CVE name, harness version, trigger SQL file, expected crash type.
# Output: one line per test with PASS/FAIL and crash signature.
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
DIR="$(cd "$(dirname "$0")" && pwd)"
HARNESS_TEST="$ROOT/harness/test"
HARNESS_NOSANIT="$ROOT/harness/nosanit"
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

run_one() {
    local label="$1" version="$2" sqlfile="$3" harness_type="${4:-test}"
    local harness

    if [ "$harness_type" = "nosanit" ]; then
        harness="$HARNESS_NOSANIT/sqlite_harness_sqlite-${version}_nosanit"
    else
        harness="$HARNESS_TEST/sqlite_harness_sqlite-${version}_test"
    fi

    if [ ! -f "$harness" ]; then
        printf "  ${YELLOW}%-45s${NC} %-8s %-8s ${YELLOW}SKIP (no harness)${NC}\n" "$label" "$version" "$harness_type"
        return
    fi
    if [ ! -f "$sqlfile" ]; then
        printf "  ${YELLOW}%-45s${NC} %-8s %-8s ${YELLOW}SKIP (no sql)${NC}\n" "$label" "$version" "$harness_type"
        return
    fi

    local out exitcode
    out=$(timeout 5 "$harness" "$sqlfile" 2>&1) || true
    exitcode=$?

    local sig=""
    local asan_type=$(echo "$out" | grep -oP 'ERROR: AddressSanitizer: \K\S+' | head -1)
    local asan_func=$(echo "$out" | grep -oP '#0 .* in \K\w+' | head -1)
    local ubsan_err=$(echo "$out" | grep -oP 'runtime error: \K[^,]+' | head -1 | cut -c1-50)
    local ubsan_line=$(echo "$out" | grep -oP 'sqlite3\.c:\K\d+' | head -1)

    if [ -n "$asan_type" ]; then
        sig="ASan:${asan_type} in ${asan_func} L${ubsan_line:-?}"
    elif [ -n "$ubsan_err" ]; then
        sig="UBSan:${ubsan_err} L${ubsan_line}"
    elif [ $exitcode -eq 139 ]; then
        sig="SEGV (signal 11)"
    elif [ $exitcode -eq 134 ]; then
        sig="SIGABRT (signal 6)"
    elif [ $exitcode -gt 128 ]; then
        sig="signal $((exitcode - 128))"
    elif [ $exitcode -eq 0 ] && [ -z "$out" ]; then
        sig="OK (no crash)"
    else
        sig="exit=$exitcode"
    fi

    if [ "$sig" = "OK (no crash)" ]; then
        printf "  ${GREEN}%-45s${NC} %-8s %-8s ${GREEN}%s${NC}\n" "$label" "$version" "$harness_type" "$sig"
    else
        printf "  ${RED}%-45s${NC} %-8s %-8s ${RED}%s${NC}\n" "$label" "$version" "$harness_type" "$sig"
    fi
}

echo ""
echo -e "${BOLD}================================================================${NC}"
echo -e "${BOLD}  BUG CLASS REPRODUCTION — $(date '+%Y-%m-%d %H:%M:%S')${NC}"
echo -e "${BOLD}================================================================${NC}"
echo ""

# ── Bug Classes (test harness = ASan+UBSan+SQLITE_DEBUG) ──────────────
echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  BUG CLASSES on sanitizer harness (test)                   ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""
printf "  ${BOLD}%-45s %-8s %-8s %s${NC}\n" "Label" "Version" "Type" "Result"
echo "  ─────────────────────────────────────────────────────────────────────────────────"

# BC001 — found on 3.30.1, 3.31.1, 3.32.0
run_one "BC001 null_ptr sqlite3ExprCodeTarget"    3.30.1 "$DIR/BC001_null_pointer_in_sqlite3ExprCodeTarget.sql"
run_one "BC001 null_ptr sqlite3ExprCodeTarget"    3.31.1 "$DIR/BC001_null_pointer_in_sqlite3ExprCodeTarget.sql"
run_one "BC001 null_ptr sqlite3ExprCodeTarget"    3.32.0 "$DIR/BC001_null_pointer_in_sqlite3ExprCodeTarget.sql"
run_one "BC001 (should be fixed)"                 3.32.2 "$DIR/BC001_null_pointer_in_sqlite3ExprCodeTarget.sql"

# BC002 — found on all 4 versions
run_one "BC002 null_ptr sqlite3Fts5GetTokenizer"  3.30.1 "$DIR/BC002_null_pointer_in_sqlite3Fts5GetTokenizer.sql"
run_one "BC002 null_ptr sqlite3Fts5GetTokenizer"  3.32.2 "$DIR/BC002_null_pointer_in_sqlite3Fts5GetTokenizer.sql"

# BC003 — found on 3.30.1, 3.31.1, 3.32.0
run_one "BC003 int_overflow sqlite3_str_vappendf" 3.30.1 "$DIR/BC003_signed_integer_overflow_in_sqlite3_str_vappendf.sql"
run_one "BC003 int_overflow sqlite3_str_vappendf" 3.31.1 "$DIR/BC003_signed_integer_overflow_in_sqlite3_str_vappendf.sql"
run_one "BC003 (should be fixed)"                 3.32.2 "$DIR/BC003_signed_integer_overflow_in_sqlite3_str_vappendf.sql"

# BC004 — found on 3.30.1
run_one "BC004 misaligned WindowUnlinkFromSelect" 3.30.1 "$DIR/BC004_misaligned_access_in_sqlite3WindowUnlinkFromSelect.sql"
run_one "BC004 (should be fixed)"                 3.31.1 "$DIR/BC004_misaligned_access_in_sqlite3WindowUnlinkFromSelect.sql"

# BC005 — found on 3.31.1, 3.32.0, 3.32.2
run_one "BC005 float_cast alsoAnInt"              3.31.1 "$DIR/BC005_float_cast_overflow_in_alsoAnInt.sql"
run_one "BC005 float_cast alsoAnInt"              3.32.2 "$DIR/BC005_float_cast_overflow_in_alsoAnInt.sql"

# BC006 — found on 3.31.1 only
run_one "BC006 null_ptr isAuxiliaryVtabOperator"  3.31.1 "$DIR/BC006_null_pointer_in_isAuxiliaryVtabOperator.sql"
run_one "BC006 (should be fixed)"                 3.32.0 "$DIR/BC006_null_pointer_in_isAuxiliaryVtabOperator.sql"

# BC007 — found on 3.30.1
run_one "BC007 misaligned resetAccumulator"       3.30.1 "$DIR/BC007_misaligned_access_in_resetAccumulator.sql"
run_one "BC007 (should be fixed)"                 3.31.1 "$DIR/BC007_misaligned_access_in_resetAccumulator.sql"

# BC008 — found on 3.31.1
run_one "BC008 misaligned sqlite3ExprCodeTarget"  3.31.1 "$DIR/BC008_misaligned_access_in_sqlite3ExprCodeTarget.sql"
run_one "BC008 (should be fixed)"                 3.32.2 "$DIR/BC008_misaligned_access_in_sqlite3ExprCodeTarget.sql"

# BC009 — found on 3.32.2
run_one "BC009 float_cast VdbeMemNumerify"        3.32.2 "$DIR/BC009_float_cast_overflow_in_sqlite3VdbeMemNumerify.sql"

# BC010 — found on 3.31.1, 3.32.0
run_one "BC010 null_ptr sqlite3Select"            3.31.1 "$DIR/BC010_null_pointer_in_sqlite3Select.sql"
run_one "BC010 null_ptr sqlite3Select"            3.32.0 "$DIR/BC010_null_pointer_in_sqlite3Select.sql"
run_one "BC010 null_ptr sqlite3Select"            3.32.2 "$DIR/BC010_null_pointer_in_sqlite3Select.sql"

# BC011 — found on 3.30.1
run_one "BC011 heap-UAF sqlite3WindowListDelete"  3.30.1 "$DIR/BC011_signal_6_in_sqlite3WindowListDelete.sql"
run_one "BC011 (should be fixed)"                 3.31.1 "$DIR/BC011_signal_6_in_sqlite3WindowListDelete.sql"

# BC012 — found on 3.30.1
run_one "BC012 null_ptr sqlite3Atoi64"            3.30.1 "$DIR/BC012_null_pointer_in_sqlite3Atoi64.sql"

# BC013 — found on 3.30.1
run_one "BC013 segfault sqlite3ExprCodeTarget"    3.30.1 "$DIR/BC013_signal_6_in_sqlite3ExprCodeTarget.sql"
run_one "BC013 (should be fixed)"                 3.32.2 "$DIR/BC013_signal_6_in_sqlite3ExprCodeTarget.sql"

echo ""

# ── Bug Classes on production harness (nosanit) ───────────────────────
echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  BUG CLASSES on production harness (nosanit)               ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""
printf "  ${BOLD}%-45s %-8s %-8s %s${NC}\n" "Label" "Version" "Type" "Result"
echo "  ─────────────────────────────────────────────────────────────────────────────────"

for bc in BC001 BC004 BC006 BC008 BC010 BC011 BC013; do
    sqlfile=$(ls "$DIR"/${bc}_*.sql 2>/dev/null | head -1)
    [ -z "$sqlfile" ] && continue
    for ver in 3.30.1 3.31.1 3.32.0 3.32.2; do
        run_one "$bc production" "$ver" "$sqlfile" nosanit
    done
done

echo ""

# ── CVE PoCs ──────────────────────────────────────────────────────────
echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  CVE PoCs on sanitizer harness (test)                      ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""
printf "  ${BOLD}%-45s %-8s %-8s %s${NC}\n" "Label" "Version" "Type" "Result"
echo "  ─────────────────────────────────────────────────────────────────────────────────"

for ver in 3.30.1 3.31.1 3.32.0 3.32.2; do
    run_one "CVE-2020-13434 (int overflow printf)" "$ver" "$DIR/CVE-2020-13434_poc.sql"
done
echo ""
for ver in 3.30.1 3.31.1 3.32.0 3.32.2; do
    run_one "CVE-2020-9327 (null ptr gen col+view)" "$ver" "$DIR/CVE-2020-9327_poc.sql"
done
echo ""
for ver in 3.30.1 3.31.1 3.32.0 3.32.2; do
    run_one "CVE-2020-13435 (null ptr join+window)" "$ver" "$DIR/CVE-2020-13435_poc.sql"
done
echo ""
for ver in 3.30.1 3.31.1 3.32.0 3.32.2; do
    run_one "CVE-2020-13871 (UAF window+except)" "$ver" "$DIR/CVE-2020-13871_poc.sql"
done
echo ""
for ver in 3.30.1 3.31.1 3.32.0 3.32.2; do
    run_one "CVE-2020-15358 (heap overread intersect)" "$ver" "$DIR/CVE-2020-15358_poc.sql"
done

echo ""
echo -e "${BOLD}================================================================${NC}"
echo -e "${BOLD}  DONE${NC}"
echo -e "${BOLD}================================================================${NC}"
