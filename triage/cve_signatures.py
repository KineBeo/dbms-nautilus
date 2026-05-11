"""Required-node signatures per corpus CVE.

Each signature is a list of labeled regex patterns. A SQL string "matches" a
signature iff every pattern finds at least one occurrence. Patterns are
lenient on whitespace/identifier choice; they encode structural requirements
(NATURAL JOIN present, coalesce with window arg present, etc.) not byte-level
identity.

Reference: docs/cve-list.md for the original PoCs.
"""
from __future__ import annotations

import re

_CVES: list[dict] = [
    {
        "cve": "CVE-2020-15358",
        "pattern_name": "Pattern-P15358",
        "required_patterns": [
            ("CREATE_VIEW_with_ORDER_BY", re.compile(r"CREATE\s+VIEW\s+\w+.*?ORDER\s+BY", re.IGNORECASE | re.DOTALL)),
            ("INTERSECT_in_WHERE", re.compile(r"WHERE[^;]+INTERSECT", re.IGNORECASE | re.DOTALL)),
            ("SELECT_with_implicit_JOIN", re.compile(r"SELECT[^;]+FROM\s+\w+\s*,\s*\w+", re.IGNORECASE | re.DOTALL)),
        ],
    },
    {
        "cve": "CVE-2020-13871",
        "pattern_name": "Pattern-P13871",
        "required_patterns": [
            ("EXCEPT_present", re.compile(r"\bEXCEPT\b", re.IGNORECASE)),
            ("ORDER_BY_multi", re.compile(r"ORDER\s+BY\s+\w+\s*(,\s*\w+\s*){1,}", re.IGNORECASE)),
            ("Scalar_subquery", re.compile(r"SELECT\s*\(\s*SELECT", re.IGNORECASE)),
        ],
    },
    {
        "cve": "CVE-2020-13435",
        "pattern_name": "Pattern-P13435",
        "required_patterns": [
            ("NATURAL_JOIN", re.compile(r"\bNATURAL\s+JOIN\b", re.IGNORECASE)),
            ("coalesce_call", re.compile(r"\bcoalesce\s*\(", re.IGNORECASE)),
            ("window_over", re.compile(r"\b(lead|lag|row_number|rank|dense_rank|first_value|last_value|nth_value|COUNT)\s*\([^)]*\)\s*OVER\s*\(", re.IGNORECASE)),
            ("UNIQUE_column", re.compile(r"\bUNIQUE\b", re.IGNORECASE)),
            ("IN_subquery", re.compile(r"\bIN\s*\(\s*\(", re.IGNORECASE)),
        ],
    },
    {
        "cve": "CVE-2020-13434",
        "pattern_name": "Pattern-P13434-Boundary",
        "required_patterns": [
            ("printf_call", re.compile(r"\bprintf\s*\(", re.IGNORECASE)),
            ("INT32_boundary", re.compile(r"-?214748364[7-8]")),
        ],
    },
    {
        "cve": "CVE-2020-9327",
        "pattern_name": "Pattern-P9327",
        "required_patterns": [
            ("GENERATED_column", re.compile(r"GENERATED\s+ALWAYS\s+AS|\bAS\s*\([^)]*\)\s*(UNIQUE|NOT\s+NULL)", re.IGNORECASE)),
            ("coalesce_call", re.compile(r"\bcoalesce\s*\(", re.IGNORECASE)),
            ("JOIN_or_commajoin", re.compile(r"\bJOIN\b|FROM\s+\w+\s*,\s*\w+", re.IGNORECASE)),
            ("CREATE_VIEW", re.compile(r"CREATE\s+VIEW", re.IGNORECASE)),
        ],
    },
    {
        "cve": "CVE-2019-19646",
        "pattern_name": "Pattern-P19646",
        "required_patterns": [
            ("GENERATED_column", re.compile(r"GENERATED\s+ALWAYS\s+AS", re.IGNORECASE)),
            ("PRAGMA_integrity", re.compile(r"PRAGMA\s+integrity_check", re.IGNORECASE)),
        ],
    },
]


def all_cves() -> list[dict]:
    return list(_CVES)


def get_cve(cve_id: str) -> dict:
    for c in _CVES:
        if c["cve"] == cve_id:
            return c
    raise KeyError(cve_id)


def missing_patterns(sql: str, signature: dict) -> list[str]:
    """Return labels of patterns that do NOT match `sql`."""
    missing: list[str] = []
    for label, regex in signature["required_patterns"]:
        if not regex.search(sql):
            missing.append(label)
    return missing
