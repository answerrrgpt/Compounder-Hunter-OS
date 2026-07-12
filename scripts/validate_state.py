#!/usr/bin/env python3
"""Validate Compounder Hunter OS JSON state without third-party packages."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state"
REQUIRED = {
    "investor_profile.json": ["schema_version", "as_of", "objective", "risk"],
    "portfolio.json": ["schema_version", "as_of", "positions", "cash"],
    "watchlist.json": ["schema_version", "as_of", "priority", "secondary"],
    "decisions.json": ["schema_version", "append_only", "decisions"],
    "strategy_versions.json": ["schema_version", "current_version", "versions"],
}


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("root must be a JSON object")
    return value


def main() -> int:
    errors: list[str] = []
    for name, keys in REQUIRED.items():
        path = STATE / name
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
            continue
        try:
            data = load(path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"invalid {path.relative_to(ROOT)}: {exc}")
            continue
        for key in keys:
            if key not in data:
                errors.append(f"{path.relative_to(ROOT)} missing key: {key}")

    decisions_path = STATE / "decisions.json"
    if decisions_path.exists():
        try:
            decisions = load(decisions_path).get("decisions", [])
            ids = [item.get("decision_id") for item in decisions]
            if None in ids or len(ids) != len(set(ids)):
                errors.append("decision_id values must be present and unique")
        except Exception:
            pass

    for path in (STATE / "companies").glob("*.json"):
        try:
            data = load(path)
            for key in ("schema_version", "ticker", "name", "as_of", "status"):
                if key not in data:
                    errors.append(f"{path.relative_to(ROOT)} missing key: {key}")
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"invalid {path.relative_to(ROOT)}: {exc}")

    if errors:
        print("State validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("State validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
