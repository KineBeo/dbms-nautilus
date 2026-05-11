#!/usr/bin/env bash
# fetch_sqlite.sh — Download SQLite amalgamation for CVE-vulnerable versions
#
# Each version corresponds to a known CVE targetted in Phase 1.
#
# CVE → SQLite version mapping (corrected 2026-03-02):
#   CVE-2018-20346  3.26.0   FTS3 heap corruption
#   CVE-2019-5018   3.27.2   Window function UAF
#   CVE-2019-19646  3.30.1   WITH RECURSIVE triggers assertion
#   CVE-2020-13434  3.31.1   printf integer overflow in sqlite3_str_vappendf (UBSan)
#                            — CVE affects through 3.32.0, fixed in 3.32.1
#                            — 3.31.1 also has CVE-2020-11655 (AggInfo window NULL deref)
#   CVE-2020-15358  3.32.2   SELECT subquery heap overflow (skiplist)
#                            — 3.32.2 is patched for CVE-2020-13434 and CVE-2020-11655
#                            — CVE-2020-15358 may affect 3.32.2 (reported in 3.32.3, boundaries unconfirmed)
#   CVE-2020-15358  3.32.3   SELECT subquery heap overflow (canonical affected version)
#   CVE-2021-20227  3.34.0   CTE UNION ALL assertion / use-after-free
#   CVE-2022-35737  3.39.1   printf large-precision buffer overflow (stack)
#
# CORRECTION HISTORY:
#   Original (incorrect): CVE-2020-13434 → 3.32.2, CVE-2020-11655 → 3.31.1
#   Corrected: CVE-2020-13434 → 3.31.1 (3.32.2 is PATCHED — fix landed in 3.32.1)
#              CVE-2020-11655 also affects 3.31.1 (AggInfo window bug, fixed in ~3.32.0)
#
# Usage:
#   ./cve_builds/fetch_sqlite.sh           # download all
#   ./cve_builds/fetch_sqlite.sh 3.32.2    # download one specific version

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# version → year mapping for SQLite download URL
declare -A YEAR=(
    ["3.26.0"]="2018"
    ["3.27.2"]="2019"
    ["3.30.1"]="2019"
    ["3.31.1"]="2020"
    ["3.32.2"]="2020"
    ["3.32.3"]="2020"
    ["3.34.0"]="2020"
    ["3.39.1"]="2022"
)

# version → CVE label (corrected mapping — see header comment for details)
declare -A CVE=(
    ["3.26.0"]="CVE-2018-20346"
    ["3.27.2"]="CVE-2019-5018"
    ["3.30.1"]="CVE-2019-19646"
    ["3.31.1"]="CVE-2020-13434+CVE-2020-11655"
    ["3.32.2"]="CVE-2020-15358-candidate"
    ["3.32.3"]="CVE-2020-15358"
    ["3.34.0"]="CVE-2021-20227"
    ["3.39.1"]="CVE-2022-35737"
)

version_to_num() {
    # 3.32.2 → 3320200
    local ver="$1"
    IFS='.' read -r major minor patch <<< "$ver"
    printf "%d%02d%02d00" "$major" "$minor" "${patch:-0}"
}

download_version() {
    local ver="$1"
    local year="${YEAR[$ver]:-}"
    if [[ -z "$year" ]]; then
        echo "Unknown version: $ver" >&2
        return 1
    fi

    local num
    num=$(version_to_num "$ver")
    local dir="$SCRIPT_DIR/sqlite-${ver}"
    local url="https://www.sqlite.org/${year}/sqlite-amalgamation-${num}.zip"

    if [[ -f "$dir/sqlite3.c" ]]; then
        echo "[skip] $ver — already downloaded"
        return 0
    fi

    echo "[fetch] $ver (${CVE[$ver]:-}) from $url"
    mkdir -p "$dir"

    local zip="$dir/amalgamation.zip"
    if ! wget -q -O "$zip" "$url"; then
        echo "  ERROR: download failed for $ver ($url)" >&2
        rm -f "$zip"
        return 1
    fi

    # Extract sqlite3.c and sqlite3.h
    unzip -q -j "$zip" "*/sqlite3.c" "*/sqlite3.h" -d "$dir"
    rm -f "$zip"
    echo "  OK: $dir/sqlite3.c ($(wc -c < "$dir/sqlite3.c") bytes)"
}

VERSIONS_TO_FETCH=("${!YEAR[@]}")

if [[ $# -ge 1 ]]; then
    VERSIONS_TO_FETCH=("$@")
fi

echo "Fetching ${#VERSIONS_TO_FETCH[@]} SQLite version(s)..."
echo ""

failed=0
for ver in "${VERSIONS_TO_FETCH[@]}"; do
    download_version "$ver" || ((failed++))
done

echo ""
echo "Done. Failed: $failed"
echo ""
echo "Next step — build harnesses:"
echo "  cd harness && make build-all"
