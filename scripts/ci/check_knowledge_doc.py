#!/usr/bin/env python3
"""Drift check: the local obsidian-gbrain doc must reference the canonical edition in
PUBLIC-PORT-DISTRIBUTION-MEMBRANE and must not reintroduce superseded semantics."""
import re
import sys
from pathlib import Path

DOC = Path(__file__).resolve().parents[2] / "docs" / "obsidian-gbrain-intelligence-layer.md"
CANONICAL = "AGENTROPOLIS-CITY-OF-AGENTS/PUBLIC-PORT-DISTRIBUTION-MEMBRANE:docs/obsidian-gbrain-intelligence-layer.md"
FORBIDDEN = [r"gbrain\.upsert_claim", r"Obsidian is the writable brain", r"Obsidian\s*\|\s*Source-of-truth"]
REQUIRED = [r"WikiVault\s*\|\s*Owns governed evidence and canon", r"gBRAIN\s*\|\s*Derived, rebuildable"]

text = DOC.read_text(encoding="utf-8")
errors = []
if CANONICAL not in text:
    errors.append("missing canonical edition reference")
errors += [f"forbidden pattern present: {p}" for p in FORBIDDEN if re.search(p, text, re.I)]
errors += [f"required pattern missing: {p}" for p in REQUIRED if not re.search(p, text)]
for e in errors:
    print(f"ERROR {e}")
print(f"Knowledge-doc drift check: {len(errors)} errors.")
sys.exit(1 if errors else 0)
