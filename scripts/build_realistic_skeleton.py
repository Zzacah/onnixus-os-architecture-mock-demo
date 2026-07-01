#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import json

ROOT = Path('/Users/zachscott/Claude/Projects/Onnixus Technologies/_ops/careers/smartcat-5838436004/onnixus-os-mock-demo')
CLAUDE_ROOT = Path('/Users/zachscott/Claude/Projects/Onnixus Technologies')
DOCS_ROOT = Path('/Users/zachscott/Documents/Ventures/Products')
OUT = ROOT / 'skeleton'


def sanitize(text: str) -> str:
    text = text.replace('/Users/zachscott', '~')
    text = re.sub(r'zachscottcs@gmail\.com', 'founder@example.com', text)
    return text


def write_excerpt(src: Path, dest: Path, max_lines: int = 180) -> dict:
    if not src.exists():
        return {'source': str(src), 'exists': False}
    raw = src.read_text(encoding='utf-8', errors='ignore').splitlines()
    excerpt = raw[:max_lines]
    body = ['# ' + src.name, '', f'Source: `{sanitize(str(src))}`', '', '```text']
    for i, line in enumerate(excerpt, start=1):
        body.append(f'{i:>4}| {sanitize(line)}')
    body.append('```')
    if len(raw) > max_lines:
        body += ['', f'_Truncated: showing first {max_lines} of {len(raw)} lines._']
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text('\n'.join(body) + '\n', encoding='utf-8')
    return {'source': str(src), 'exists': True, 'lines_total': len(raw), 'lines_shown': min(len(raw), max_lines)}


def extract_prompt_markers(src: Path) -> list[str]:
    if not src.exists():
        return []
    lines = src.read_text(encoding='utf-8', errors='ignore').splitlines()
    keep = []
    keys = ('You are', 'READ FIRST', 'INPUTS', 'OUTPUT', 'STEPS', 'CONSTRAINTS', 'Draft-to-approve', 'manifest', 'requires_approval')
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if any(k.lower() in s.lower() for k in keys):
            keep.append(sanitize(s))
    # de-dup preserve order
    seen = set()
    out = []
    for k in keep:
        if k not in seen:
            seen.add(k)
            out.append(k)
    return out[:24]


def safe_name(name: str) -> str:
    if re.search(r'(secret|password|token|key|pem|credential)', name, re.IGNORECASE):
        return '[REDACTED-sensitive-name]'
    return name


def mirror_product_context(product_name: str) -> dict:
    src = DOCS_ROOT / product_name
    dst = OUT / 'contexts' / product_name.replace(' ', '-')
    dst.mkdir(parents=True, exist_ok=True)

    if not src.exists():
        (dst / 'README.md').write_text(f'# {product_name}\n\nSource path not found on this machine.\n', encoding='utf-8')
        return {'product': product_name, 'exists': False}

    top_dirs = sorted([p for p in src.iterdir() if p.is_dir() and not p.name.startswith('.')], key=lambda p: p.name)
    rows = []
    for d in top_dirs:
        files = sorted([p for p in d.rglob('*') if p.is_file() and not p.name.startswith('.')])
        rows.append((safe_name(d.name), len(files)))

    md = [f'# {product_name} Context Skeleton', '', f'Source: `{sanitize(str(src))}`', '', '## Top-level map', '']
    for name, count in rows:
        md.append(f'- `{name}/` ({count} files)')
    md.append('')
    md.append('_File names only. No confidential file content copied._')
    (dst / 'README.md').write_text('\n'.join(md) + '\n', encoding='utf-8')

    # create thin folder skeleton
    for name, _ in rows:
        (dst / name / '.keep').parent.mkdir(parents=True, exist_ok=True)
        (dst / name / '.keep').write_text('', encoding='utf-8')

    return {'product': product_name, 'exists': True, 'sections': len(rows)}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)

    sources = {
        'config': CLAUDE_ROOT / '_ops/config.yaml',
        'agents_index': CLAUDE_ROOT / '_ops/AGENTS.md',
        'standard_preamble': CLAUDE_ROOT / '_ops/STANDARD_AGENT_PREAMBLE.md',
        'heartbeat_orchestrator': CLAUDE_ROOT / '_ops/dev/heartbeat.py',
        'router_harness': CLAUDE_ROOT / '_ops/agents/on-demand/onnixus-router.md',
        'daily_planner': Path('/Users/zachscott/Claude/Scheduled/onnixus-daily-planner/SKILL.md'),
        'content_engine': Path('/Users/zachscott/Claude/Scheduled/onnixus-content-engine/SKILL.md'),
        'strategy_research': Path('/Users/zachscott/Claude/Scheduled/onnixus-strategy-research/SKILL.md'),
    }

    manifest = {'onnixus_os_files': {}, 'prompt_markers': {}, 'contexts': []}

    for key, src in sources.items():
        dest = OUT / 'onnixus-os' / f'{key}.excerpt.md'
        manifest['onnixus_os_files'][key] = write_excerpt(src, dest)
        manifest['prompt_markers'][key] = extract_prompt_markers(src)

    products = ['TripGoGo', 'SplitGoGo', 'TripGoGo for Business']
    for p in products:
        manifest['contexts'].append(mirror_product_context(p))

    pm = ['# Agent Prompt Skeleton Index', '', 'Representative prompt/instruction markers from current Onnixus agent files.', '']
    for key, markers in manifest['prompt_markers'].items():
        pm.append(f'## {key}')
        if not markers:
            pm.append('- (no markers found)')
        else:
            for m in markers:
                pm.append(f'- {m}')
        pm.append('')
    (OUT / 'onnixus-os' / 'agent-prompt-markers.md').write_text('\n'.join(pm) + '\n', encoding='utf-8')

    readme = [
        '# Onnixus OS Real-Structure Skeleton (Sanitized)',
        '',
        'This skeleton mirrors the current architecture shape from `~/Claude/Projects/Onnixus Technologies` and references product-context structure under `~/Documents/Ventures/Products`.',
        '',
        '## Included',
        '- orchestrator and governance config skeletons',
        '- scheduled-agent prompt skeletons (daily planner, content engine, strategy research)',
        '- on-demand router harness skeleton',
        '- brand context folder skeletons for TripGoGo, SplitGoGo, and TripGoGo for Business (TG4B representation)',
        '',
        '## Safety',
        '- file names + structure are mirrored',
        '- sensitive absolute paths are sanitized to `~`',
        '- no private file contents from Documents are copied',
    ]
    (OUT / 'README.md').write_text('\n'.join(readme) + '\n', encoding='utf-8')

    (OUT / 'skeleton-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(f'wrote skeleton to {OUT}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
