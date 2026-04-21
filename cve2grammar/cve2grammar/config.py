"""Configuration constants for cve2grammar."""

from __future__ import annotations

MANUELRIGGER_URL = "https://www.manuelrigger.at/dbms-bugs/"

# Grammar weight assigned per oracle type. Higher = more often picked by Nautilus.
ORACLE_WEIGHTS: dict[str, float] = {
    "crash": 3.0,    # memory corruption — highest priority
    "hang":  2.5,    # DoS / infinite loop
    "error": 2.0,    # unexpected error
    "PQS":   2.0,    # Pivoted Query Synthesis (logic bug)
    "NoREC": 2.0,    # Non-optimizing Reference Engine Construction
    "TLP":   2.0,    # Ternary Logic Partitioning
}
DEFAULT_WEIGHT = 1.5

SUPPORTED_DBMS: tuple[str, ...] = (
    "sqlite", "postgresql", "mysql", "mariadb",
    "cockroachdb", "tidb", "duckdb", "tdengine", "h2",
)

SUPPORTED_SECTIONS: tuple[str, ...] = ("fixed", "confirmed", "open", "closed", "all")
