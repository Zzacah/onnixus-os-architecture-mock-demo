#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
DEMO = ROOT / "demo"
ASSETS.mkdir(parents=True, exist_ok=True)
DEMO.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
BG = (11, 16, 32)
PANEL = (19, 27, 49)
ACCENT = (75, 164, 255)
TEXT = (230, 238, 255)
MUTED = (167, 185, 220)
GREEN = (73, 214, 124)


def font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
    ]
    for c in candidates:
        p = Path(c)
        if p.exists():
            return ImageFont.truetype(str(p), size=size)
    return ImageFont.load_default()


F_TITLE = font(66, bold=True)
F_SUB = font(34)
F_BODY = font(30)
F_MONO = font(26)


def round_rect(draw, xy, radius=22, fill=PANEL, outline=(46, 67, 110), width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def base_canvas(title: str, subtitle: str):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 110), fill=(8, 12, 25))
    d.text((56, 26), title, fill=TEXT, font=F_TITLE)
    d.text((58, 100), subtitle, fill=MUTED, font=F_SUB)
    d.text((W - 500, 28), "ONNIXUS OS MOCK DEMO", fill=ACCENT, font=F_MONO)
    d.text((W - 560, 70), "No production data. Recruiter-safe package.", fill=MUTED, font=F_MONO)
    return im, d


slides = []

# Slide 1
im, d = base_canvas("AI Operations Architecture", "Single heartbeat, unified decision queue, deterministic write-path")
round_rect(d, (70, 180, 1850, 980))
boxes = [
    (140, 250, 620, 420, "Heartbeat Engine", "mock_heartbeat.py\\n- sweeps backlog\\n- emits QUEUE.mock.md"),
    (700, 250, 1220, 420, "Decision Queue", "QUEUE.mock.md\\n- open decisions\\n- approval indicators"),
    (1300, 250, 1780, 420, "Planner Surface", "single review inbox\\nlow-noise daily ops"),
    (420, 560, 940, 880, "No-Deploy Pack Runner", "mock_pack_runner.py\\n--mode dry-run/execute\\n--confirm required"),
    (1030, 560, 1550, 880, "Release Output", "pack_run_report.mock.json\\ntrip + guide + social ready"),
]
for x1, y1, x2, y2, t, b in boxes:
    round_rect(d, (x1, y1, x2, y2), fill=(16, 35, 66), outline=(59, 108, 188))
    d.text((x1 + 24, y1 + 18), t, fill=TEXT, font=F_SUB)
    d.multiline_text((x1 + 24, y1 + 78), b, fill=MUTED, font=F_BODY, spacing=8)
slides.append(im)

# Slide 2
im, d = base_canvas("Mock Queue Snapshot", "Demonstrates approval-gated operations with synthetic IDs")
round_rect(d, (100, 210, 1820, 940), fill=(14, 24, 44))
lines = [
    "# QUEUE (Mock Demo)",
    "Generated: 2026-06-30",
    "",
    "## Open decisions",
    "- 🔒 backlog:mock001 [growth] Launch mock city trip + guide bundle",
    "- ✅ backlog:mock002 [operations] Refresh mission-control architecture map",
    "",
    "## Notes",
    "- This file uses mock data only.",
]
y = 250
for i, line in enumerate(lines):
    col = GREEN if line.startswith("- 🔒") else (TEXT if i in (0, 3) else MUTED)
    d.text((140, y), line, fill=col, font=F_MONO)
    y += 68 if i in (0, 3) else 56
slides.append(im)

# Slide 3
im, d = base_canvas("Deterministic Content Pack Flow", "Trip + guide + social bundled without deploy window")
round_rect(d, (140, 220, 1780, 900), fill=(17, 31, 57))
steps = [
    "1) Validate manifest and paths",
    "2) Dry-run checks for safe launch",
    "3) Execute with explicit --confirm",
    "4) Emit release report artifact",
    "5) Update queue state write-path",
]
y = 290
for s in steps:
    d.text((230, y), s, fill=TEXT, font=F_BODY)
    d.ellipse((170, y + 8, 198, y + 36), fill=ACCENT)
    y += 108
d.text((230, 840), "All values shown are synthetic placeholders", fill=MUTED, font=F_MONO)
slides.append(im)

# Slide 4
im, d = base_canvas("Cost / Latency Tradeoff", "Practical optimization for real operations")
round_rect(d, (120, 220, 900, 900), fill=(16, 35, 66))
round_rect(d, (1020, 220, 1800, 900), fill=(16, 35, 66))
d.text((170, 270), "High-frequency background work", fill=TEXT, font=F_SUB)
d.multiline_text((170, 340), "- deterministic scripts\n- lower-cost model tiers\n- silent heartbeat cadence", fill=MUTED, font=F_BODY, spacing=12)
d.text((1070, 270), "Human-facing decision synthesis", fill=TEXT, font=F_SUB)
d.multiline_text((1070, 340), "- stronger models\n- better recommendation quality\n- lower operator load", fill=MUTED, font=F_BODY, spacing=12)
d.text((130, 940), "Result: lower token spend and latency, while preserving decision quality where it matters.", fill=GREEN, font=F_MONO)
slides.append(im)

# Slide 5
im, d = base_canvas("Recruiter-Safe Artifact Package", "GitHub-ready deliverables with mock data only")
round_rect(d, (120, 230, 1800, 920), fill=(14, 24, 44))
items = [
    "README.md (architecture + workflow)",
    "mock_data/*.yaml (synthetic queue/backlog)",
    "scripts/mock_heartbeat.py",
    "scripts/mock_pack_runner.py",
    "demo/QUEUE.mock.md",
    "demo/pack_run_report.mock.json",
    "demo/onnixus-os-mock-demo.mp4",
]
y = 300
for it in items:
    d.text((180, y), f"• {it}", fill=TEXT, font=F_BODY)
    y += 78
d.text((180, 850), "This package demonstrates architecture and execution, without exposing real customer or business data.", fill=MUTED, font=F_MONO)
slides.append(im)

# save slides
for i, s in enumerate(slides, start=1):
    s.save(ASSETS / f"slide_{i:02d}.png")

# Render mp4 via ffmpeg
out = DEMO / "onnixus-os-mock-demo.mp4"
cmd = [
    "ffmpeg", "-y", "-framerate", "1/3", "-i", str(ASSETS / "slide_%02d.png"),
    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-pix_fmt", "yuv420p", str(out)
]
subprocess.run(cmd, check=True)
print(f"wrote {out}")
