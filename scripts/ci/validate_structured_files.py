#!/usr/bin/env python3
"""Baseline CI: every tracked JSON/YAML file parses, and every JSON Schema is a valid schema
for the dialect it declares. Read-only; exits non-zero on any failure."""
import json
import subprocess
import sys
from pathlib import Path

import yaml
from jsonschema.validators import validator_for

ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", "node_modules"}


def tracked_files():
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, check=True, capture_output=True, text=True).stdout
        return [ROOT / p for p in out.splitlines() if p]
    except Exception:
        return [p for p in ROOT.rglob("*") if p.is_file() and not SKIP_DIRS.intersection(p.parts)]


def is_schema(path, doc):
    if not isinstance(doc, dict):
        return False
    return path.name.endswith(".schema.json") or "json-schema.org" in str(doc.get("$schema", ""))


def main():
    errors, counts, ids = [], {"json": 0, "yaml": 0, "schema": 0}, {}
    for path in sorted(tracked_files()):
        rel = path.relative_to(ROOT).as_posix()
        suffix = path.suffix.lower()
        try:
            if suffix == ".json":
                doc = json.loads(path.read_text(encoding="utf-8"))
                counts["json"] += 1
                if is_schema(path, doc):
                    validator_for(doc).check_schema(doc)
                    counts["schema"] += 1
                    sid = doc.get("$id")
                    if sid:
                        if sid in ids:
                            errors.append(f"{rel}: duplicate $id {sid} (also in {ids[sid]})")
                        ids[sid] = rel
            elif suffix in (".yaml", ".yml"):
                list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
                counts["yaml"] += 1
        except Exception as exc:  # noqa: BLE001 - report every failure
            errors.append(f"{rel}: {type(exc).__name__}: {str(exc).splitlines()[0][:300]}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"Structured-file validation: {counts['json']} JSON, {counts['yaml']} YAML, "
          f"{counts['schema']} JSON Schemas checked, {len(errors)} errors.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
