# Onnixus OS Real-Structure Skeleton Demo (Sanitized)

This repository is a recruiter-safe artifact package that mirrors the **current Onnixus OS architecture shape** from:
- `~/Claude/Projects/Onnixus Technologies` (OS config/orchestration/agents)
- `~/Documents/Ventures/Products/*` (brand context references)

It is intentionally sanitized for public review.

## What it demonstrates
- Real-structure kernel-orchestration skeleton (`_ops/config.yaml`, `_ops/dev/heartbeat.py`, `_ops/AGENTS.md`)
- Real agent prompt skeletons from scheduled + on-demand agent files
- Per-brand context skeleton mapping for:
  - TripGoGo
  - SplitGoGo
  - TripGoGo for Business (TG4B “built” representation)
- Interactive artifact GUI that shows queue, packs, skeleton, and architecture views

## Data safety
- No production records
- No PII
- No partner/customer data
- Documents-side content is represented as **structure only**
- Sensitive names are redacted where needed

## Run locally

```bash
python3 scripts/build_realistic_skeleton.py
node scripts/capture_gui_walkthrough.js
python3 scripts/make_gui_walkthrough_video.py
python3 scripts/mock_heartbeat.py
python3 scripts/mock_pack_runner.py --pack-id chicago-groups-v1 --mode dry-run
python3 scripts/mock_pack_runner.py --pack-id chicago-groups-v1 --mode execute --confirm
```

## Key files
- `gui-artifact.html` (primary interactive artifact HTML)
- `skeleton/README.md` (high-level skeleton package overview)
- `skeleton/onnixus-os/*.excerpt.md` (sanitized architecture/prompt excerpts)
- `skeleton/onnixus-os/agent-prompt-markers.md` (prompt marker index)
- `skeleton/contexts/TripGoGo/README.md`
- `skeleton/contexts/SplitGoGo/README.md`
- `skeleton/contexts/TripGoGo-for-Business/README.md`
- `scripts/build_realistic_skeleton.py`
- `scripts/capture_gui_walkthrough.js`
- `scripts/make_gui_walkthrough_video.py`
- `demo/onnixus-os-gui-walkthrough.mp4`

## GUI walkthrough focus
The walkthrough video captures real interactions in `gui-artifact.html`:
- Overview tab (proof summary + safety boundary)
- Decision Queue actions (approve + snooze)
- Content Packs tab
- Code Skeleton tab (prompt/orchestration/context references)
- Architecture Web tab

## Why this artifact
It provides an inspectable, public-safe skeleton of how Onnixus OS is currently structured, including agent prompts/orchestration and brand-context references, without exposing private operational data.
