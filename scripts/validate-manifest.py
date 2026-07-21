#!/usr/bin/env python3
"""Validates manifest.json has the fields Obsidian requires to load the
theme, and that version numbers are valid semver. Run locally or in CI
after editing manifest.json."""
import json
import re
import sys
from pathlib import Path

MANIFEST_PATH = Path(__file__).resolve().parent.parent / "manifest.json"
REQUIRED_FIELDS = ["name", "version", "minAppVersion", "author", "authorUrl", "description"]
SEMVER = re.compile(r"\d+\.\d+\.\d+")

errors = []

try:
    data = json.loads(MANIFEST_PATH.read_text())
except json.JSONDecodeError as e:
    print(f"manifest.json is not valid JSON. {e}", file=sys.stderr)
    sys.exit(1)

missing = [field for field in REQUIRED_FIELDS if not str(data.get(field, "")).strip()]
if missing:
    errors.append(f"missing or empty required fields, {', '.join(missing)}")

for field in ("version", "minAppVersion"):
    value = data.get(field, "")
    if value and not SEMVER.fullmatch(value):
        errors.append(f"{field} {value!r} is not valid semver (expected x.y.z)")

if errors:
    for error in errors:
        print(f"manifest.json: {error}", file=sys.stderr)
    sys.exit(1)

print("manifest.json OK")
