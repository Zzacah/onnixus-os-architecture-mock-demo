#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess

ROOT = Path('/Users/zachscott/Claude/Projects/Onnixus Technologies/_ops/careers/smartcat-5838436004/onnixus-os-mock-demo')
SRC = ROOT / 'assets' / 'gui_walkthrough'
OUT = ROOT / 'demo'
OUT.mkdir(parents=True, exist_ok=True)

W,H=1920,1080

def fnt(size=34,bold=False):
    cands=[
        '/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf',
        '/Library/Fonts/Arial Bold.ttf' if bold else '/Library/Fonts/Arial.ttf',
    ]
    for c in cands:
        p=Path(c)
        if p.exists():
            return ImageFont.truetype(str(p),size=size)
    return ImageFont.load_default()

FT=fnt(42,True)
FS=fnt(26,False)

captions={
 'frame_01_overview.png':'1) Overview: real-structure skeleton KPIs and safety boundary',
 'frame_02_queue_open.png':'2) Decision Queue tab with synthetic IDs and approval gates',
 'frame_03_queue_approve.png':'3) Mock approve action updates queue state in GUI',
 'frame_04_queue_snooze.png':'4) Mock snooze action demonstrates temporal deferral behavior',
 'frame_05_packs.png':'5) No-deploy content pack panel with confirm-before-execute pattern',
 'frame_06_skeleton.png':'6) Code Skeleton tab: prompts, orchestrator files, per-brand context mapping',
 'frame_07_architecture.png':'7) Architecture map from Claude OS kernel to Documents brand contexts',
 'frame_08_overview_return.png':'8) Return to single control portal for reviewer walkthrough',
}

ordered=[
 'frame_01_overview.png','frame_02_queue_open.png','frame_03_queue_approve.png',
 'frame_04_queue_snooze.png','frame_05_packs.png','frame_06_skeleton.png','frame_07_architecture.png','frame_08_overview_return.png'
]

annot=ROOT/'assets'/'gui_walkthrough_annotated'
annot.mkdir(parents=True,exist_ok=True)

for name in ordered:
    im=Image.open(SRC/name).convert('RGB')
    d=ImageDraw.Draw(im)
    d.rectangle((0,H-120,W,H),fill=(5,8,16,220))
    d.text((32,H-92),'Onnixus OS Mock GUI Walkthrough',fill=(230,240,255),font=FT)
    d.text((34,H-48),captions[name],fill=(163,190,238),font=FS)
    d.text((W-430,H-48),'Mock data only • Recruiter-safe',fill=(112,211,150),font=FS)
    im.save(annot/name)

out=OUT/'onnixus-os-gui-walkthrough.mp4'
lst=annot/'frames.txt'
with open(lst,'w',encoding='utf-8') as f:
    for name in ordered:
        f.write(f"file '{(annot/name).as_posix()}'\n")
        f.write('duration 2.4\n')
    f.write(f"file '{(annot/ordered[-1]).as_posix()}'\n")

subprocess.run(['ffmpeg','-y','-f','concat','-safe','0','-i',str(lst),'-vf','fps=30,format=yuv420p','-c:v','libx264','-pix_fmt','yuv420p',str(out)],check=True)
print(f'wrote {out}')
