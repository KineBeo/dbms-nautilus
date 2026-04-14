"""Scraper for Manuel Rigger's DBMS bugs page.

The page (manuelrigger.at/dbms-bugs) is structured as:
    <h2>{section title}</h2>      ← Unique fixed | confirmed | open | closed
      <h3>{DBMS name}</h3>        ← SQLite | PostgreSQL | MySQL | ...
        <ul>
          <li>
            <b>#{N} {title}</b>
            <details>
              <b>Links</b>: <a>[bugtracker]</a> <a>[email]</a> <a>[fix]</a>
              <b>Date found</b>: DD/MM/YYYY
              <b>Status</b>: fixed | ...
              <b>Test case:</b>
              <pre>{SQL}</pre>
              <b>Test case LOC:</b> N
              <b>Oracle:</b> PQS | NoREC | TLP | crash | error | hang
            </details>
          </li>
          ...

This module walks that DOM and produces a list[Bug].
"""

from __future__ import annotations

import re

import requests
from bs4 import BeautifulSoup, Tag

from cve2grammar.config import MANUELRIGGER_URL
from cve2grammar.models import Bug

# Maps the page's DBMS heading text to the slug we use everywhere else.
DBMS_HEADINGS: dict[str, str] = {
    "SQLite": "sqlite",
    "PostgreSQL": "postgresql",
    "MySQL": "mysql",
    "MariaDB": "mariadb",
    "CockroachDB": "cockroachdb",
    "TiDB": "tidb",
    "DuckDB": "duckdb",
    "TDEngine": "tdengine",
    "H2": "h2",
}

# Maps the page's section heading text to a slug.
SECTION_LABEL: dict[str, str] = {
    "Unique fixed bugs": "fixed",
    "Unique confirmed bugs": "confirmed",
    "Unconfirmed/Open bug reports": "open",
    "Closed/Duplicate bug reports": "closed",
}

_TITLE_RE = re.compile(r"#(\d+)\s+(.+)")
_DATE_RE = re.compile(r"(\d{1,2})[/.](\d{1,2})[/.](\d{4})")
_LINK_LABEL_RE = re.compile(r"^\[([a-z]+)(?:\s*\d+)?\]$")  # [bugtracker], [email], [fix]


def fetch(html: str | None = None, timeout: int = 30) -> list[Bug]:
    """Scrape Manuel Rigger's DBMS bugs page.

    Args:
        html: Optional pre-fetched HTML. If None, fetches from MANUELRIGGER_URL.
        timeout: HTTP timeout in seconds (only used when html is None).

    Returns:
        Flat list of Bug records across all sections and DBMS.
    """
    if html is None:
        resp = requests.get(MANUELRIGGER_URL, timeout=timeout)
        resp.raise_for_status()
        html = resp.text

    soup = BeautifulSoup(html, "html.parser")
    bugs: list[Bug] = []
    current_section = ""
    current_dbms = ""

    for tag in soup.find_all(["h2", "h3", "li"]):
        if tag.name == "h2":
            current_section = SECTION_LABEL.get(tag.get_text(strip=True), "")
            current_dbms = ""  # reset on new section
        elif tag.name == "h3":
            current_dbms = DBMS_HEADINGS.get(tag.get_text(strip=True), "")
        elif tag.name == "li" and current_dbms and current_section:
            bug = _parse_li(tag, current_dbms, current_section)
            if bug is not None:
                bugs.append(bug)

    return bugs


def _parse_li(li: Tag, dbms: str, section: str) -> Bug | None:
    """Parse a single <li> bug entry. Returns None if it lacks a usable test case."""
    title_b = li.find("b")
    if title_b is None:
        return None

    m = _TITLE_RE.match(title_b.get_text(strip=True))
    if m is None:
        return None
    number = int(m.group(1))
    title = m.group(2)

    details = li.find("details")
    if details is None:
        return None

    pre = details.find("pre")
    if pre is None:
        return None
    sql = pre.get_text().strip()
    if not sql:
        return None  # no test case → useless for grammar

    fields, links = _parse_fields_and_links(details)

    return Bug(
        id=f"MR-{dbms.upper()}-{number:04d}",
        dbms=dbms,
        section=section,
        number=number,
        title=title,
        sql=sql,
        oracle=fields.get("Oracle", ""),
        status=fields.get("Status", ""),
        date_found=_parse_date(fields.get("Date found", "")),
        bugtracker_url=links.get("bugtracker", ""),
        email_url=links.get("email", ""),
        fix_url=links.get("fix", ""),
    )


def _parse_fields_and_links(details: Tag) -> tuple[dict[str, str], dict[str, str]]:
    """Walk <b>Label</b>: text pairs (fields) and <a>[name]</a> tags (links)."""
    fields: dict[str, str] = {}
    for b in details.find_all("b"):
        label = b.get_text(strip=True).rstrip(":").strip()
        if not label:
            continue
        sibling = b.next_sibling
        if sibling is None:
            continue
        value = str(sibling).strip().lstrip(":").strip()
        if value:
            fields[label] = value

    links: dict[str, str] = {}
    for a in details.find_all("a"):
        href = a.get("href", "")
        text = a.get_text(strip=True)
        m = _LINK_LABEL_RE.match(text)
        if m and href:
            kind = m.group(1)
            # First match wins for repeated labels (e.g. [email] [email 2])
            links.setdefault(kind, href)

    return fields, links


def _parse_date(s: str) -> str:
    """Parse '28/5/2019' or '02/07/2019' → ISO '2019-05-28'. Returns '' on failure."""
    m = _DATE_RE.match(s.strip())
    if m is None:
        return ""
    d, mo, y = m.groups()
    return f"{y}-{int(mo):02d}-{int(d):02d}"
