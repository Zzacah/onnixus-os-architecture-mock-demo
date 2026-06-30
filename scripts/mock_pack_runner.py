#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "mock_data"
OUT = ROOT / "demo"


def load_yaml(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def dump_yaml(path: Path, data) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)


def main() -> int:
    ap = argparse.ArgumentParser(description="Mock content pack runner")
    ap.add_argument("--pack-id", required=True)
    ap.add_argument("--mode", choices=["dry-run", "execute"], default="dry-run")
    ap.add_argument("--confirm", action="store_true")
    args = ap.parse_args()

    state = load_yaml(DATA / "queue_state.mock.yaml")
    OUT.mkdir(parents=True, exist_ok=True)

    if args.mode == "execute" and not args.confirm:
        raise SystemExit("Refusing execute without --confirm")

    report = {
        "pack_id": args.pack_id,
        "mode": args.mode,
        "result": "validated" if args.mode == "dry-run" else "executed",
        "trip_created": True,
        "guide_created": True,
        "social_payload_ready": True,
        "uses_mock_data_only": True,
    }

    if args.mode == "execute":
        # Move one mock item to approved to simulate write-path
        if "backlog:mock001" in state:
            state["backlog:mock001"]["status"] = "approved"
            state["backlog:mock001"]["approved_at"] = "2026-06-30"
            dump_yaml(DATA / "queue_state.mock.yaml", state)

    out_json = OUT / "pack_run_report.mock.json"
    out_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
