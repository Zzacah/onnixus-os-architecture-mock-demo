#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "mock_data"
OUT = ROOT / "demo"


def load_yaml(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate mock QUEUE.md from mock backlog/state")
    ap.add_argument("--date", default=dt.date.today().isoformat())
    args = ap.parse_args()

    backlog = load_yaml(DATA / "backlog.mock.yaml")["items"]
    state = load_yaml(DATA / "queue_state.mock.yaml")

    open_items = []
    for item in backlog:
        sid = item["id"]
        st = state.get(sid, {})
        status = st.get("status", item.get("status", "open"))
        if status == "open":
            open_items.append((sid, item["stream"], item["title"], bool(item.get("requires_approval", False))))

    OUT.mkdir(parents=True, exist_ok=True)
    queue_path = OUT / "QUEUE.mock.md"
    lines = [
        "# QUEUE (Mock Demo)",
        "",
        f"Generated: {args.date}",
        "",
        "## Open decisions",
        "",
    ]
    if not open_items:
        lines.append("- No open decisions.")
    else:
        for sid, stream, title, req in open_items:
            gate = "🔒" if req else "✅"
            lines.append(f"- {gate} `{sid}` [{stream}] {title}")

    lines += [
        "",
        "## Notes",
        "- This file uses mock data only.",
        "- No production customer, partner, or PII data included.",
    ]

    queue_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {queue_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
