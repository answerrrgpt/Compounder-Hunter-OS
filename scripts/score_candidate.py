#!/usr/bin/env python3
"""Calculate a weighted Compounder Hunter score from a JSON file."""

from __future__ import annotations

import json
import sys
from pathlib import Path

WEIGHTS = {
    "business_quality": 20,
    "reinvestment_runway": 15,
    "management_allocation": 10,
    "financial_quality": 10,
    "valuation": 20,
    "catalysts": 10,
    "right_side_confirmation": 5,
    "risk_clarity": 10,
}


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} scores.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot read scores: {exc}", file=sys.stderr)
        return 2
    errors = []
    for key in WEIGHTS:
        value = data.get(key)
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0 <= value <= 5:
            errors.append(f"{key} must be a number from 0 to 5")
    unknown = sorted(set(data) - set(WEIGHTS))
    if unknown:
        errors.append("unknown keys: " + ", ".join(unknown))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    total = round(sum(data[key] / 5 * weight for key, weight in WEIGHTS.items()), 2)
    band = "priority candidate" if total >= 80 else "core watchlist" if total >= 70 else "research or wait" if total >= 60 else "reject or archive"
    print(json.dumps({"weighted_score": total, "band": band}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
