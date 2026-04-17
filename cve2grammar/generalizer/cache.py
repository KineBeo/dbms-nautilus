"""Content-addressed on-disk cache for agent-produced template payloads.

One file per unique bug SQL at ``cache/generalizer/{sha256(sql)[:16]}.json``.
Committed to git for reproducibility.

Entries carry a ``prompt_version`` field. When the skill's rules change in
a way that should invalidate the cache, bump ``PROMPT_VERSION`` in the
package ``__init__.py``: entries whose stored version differs are treated
as misses without any file mutation. This means a single constant bump
invalidates the entire cache without deleting anything.

Writes are atomic: we write a ``.tmp`` file next to the target and then
``os.replace`` it into place, so a crashed run cannot leave a half-written
JSON file at the final path.
"""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from pathlib import Path

from cve2grammar.generalizer import PROMPT_VERSION

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CACHE_ROOT = _REPO_ROOT / "cache" / "generalizer"


@dataclass(frozen=True)
class CacheConfig:
    """Immutable per-invocation settings — useful for tests that redirect root."""
    root: Path
    prompt_version: int


_config = CacheConfig(root=CACHE_ROOT, prompt_version=PROMPT_VERSION)


def cache_key(sql: str) -> str:
    """Stable 16-char content-addressed key for a bug's SQL test case."""
    digest = hashlib.sha256(sql.encode("utf-8")).hexdigest()
    return digest[:16]


def _cache_path(key: str) -> Path:
    return _config.root / f"{key}.json"


def cache_get(key: str) -> dict | None:
    """Return the cached entry, or ``None`` on miss / corrupt / version drift."""
    path = _cache_path(key)
    if not path.exists():
        return None
    try:
        raw = path.read_text(encoding="utf-8")
        entry = json.loads(raw)
    except (OSError, json.JSONDecodeError):
        return None
    stored = entry.get("prompt_version")
    if stored != _config.prompt_version:
        return None
    return entry


def cache_put(key: str, payload: dict) -> None:
    """Write ``payload`` to cache atomically. Creates the root dir if missing."""
    _config.root.mkdir(parents=True, exist_ok=True)
    target = _cache_path(key)
    tmp = target.with_suffix(".tmp")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, target)
