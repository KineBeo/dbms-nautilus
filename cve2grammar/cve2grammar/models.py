"""Single data model: Bug — one entry from Manuel Rigger's DBMS bugs page."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Bug:
    """A single curated DBMS bug with a minimal SQL test case."""

    id: str               # "MR-SQLITE-0001"
    dbms: str             # "sqlite", "postgresql", ...
    section: str          # "fixed" | "confirmed" | "open" | "closed"
    number: int           # bug number within DBMS+section
    title: str            # human-readable title
    sql: str              # full test case SQL (multi-statement allowed)
    oracle: str           # "PQS" | "NoREC" | "TLP" | "crash" | "error" | "hang" | ""
    status: str           # "fixed" | "fixed in documentation" | "confirmed" | ...
    date_found: str       # ISO date "2019-05-28"; empty when unparseable
    bugtracker_url: str   # may be empty
    email_url: str        # may be empty
    fix_url: str          # may be empty
