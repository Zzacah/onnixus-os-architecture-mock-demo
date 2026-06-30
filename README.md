# Onnixus OS Mock Architecture Demo

This repository is a recruiter-safe artifact package that demonstrates the Onnixus OS architecture and execution model using **mock data only**.

## What it demonstrates
- Single-heartbeat queue generation flow
- Unified decision queue pattern
- Deterministic content-pack write-path with explicit execute confirmation
- Practical cost/latency tradeoff design for AI-assisted operations

## Data safety
- No production records
- No PII
- No partner/customer data
- Synthetic IDs and synthetic task content only

## Run locally

```bash
python3 scripts/mock_heartbeat.py
python3 scripts/mock_pack_runner.py --pack-id chicago-groups-v1 --mode dry-run
python3 scripts/mock_pack_runner.py --pack-id chicago-groups-v1 --mode execute --confirm
python3 scripts/make_demo_video.py
```

## Key files
- `mock_data/backlog.mock.yaml`
- `mock_data/queue_state.mock.yaml`
- `scripts/mock_heartbeat.py`
- `scripts/mock_pack_runner.py`
- `scripts/make_demo_video.py`
- `demo/QUEUE.mock.md`
- `demo/pack_run_report.mock.json`
- `demo/onnixus-os-mock-demo.mp4`

## Why this artifact
This package gives a concrete, inspectable demonstration of architecture and working outputs without exposing any sensitive operational context.
