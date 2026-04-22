"""Pytest root conftest.

Anchors the project root on sys.path so `from triage import ...` resolves
to /triage/ at repo root rather than the nested tests/triage/ package.
"""
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
