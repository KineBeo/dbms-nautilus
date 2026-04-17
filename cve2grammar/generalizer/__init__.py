"""Grammar generalizer package — LLM-driven rewriting of bug SQL to Nautilus templates.

The pipeline is orchestrated by the `/generalize` Claude Code slash command
(see `.claude/commands/generalize.md`). This package provides the stateless
Python helpers the slash command invokes via its Bash tool: whitelist
extraction, template validation, content-addressed caching, and grammar
file rendering.

`PROMPT_VERSION` is the cache-bust knob. Incrementing it invalidates every
existing cache entry without deleting any file — entries whose stored
`prompt_version` differs from this constant are treated as misses.
"""

from __future__ import annotations

PROMPT_VERSION: int = 1
"""Bumped whenever the skill's rules, examples, or output schema change in a way
that should invalidate the cache. Entries with older versions are re-queried."""
