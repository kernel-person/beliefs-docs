#!/usr/bin/env python3
"""Refresh public references from a reviewed resource snapshot; never contacts a server."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / 'tools/source-snapshot.json'


def snapshot(source):
    resources = source / 'src/main/resources'
    paths = {name: resources / name for name in ('config.yml', 'plugin.yml', 'symbols.yml')}
    parsed = {name: yaml.safe_load(path.read_text()) for name, path in paths.items()}
    version = re.search(r'<version>([^<]+)</version>', (source / 'pom.xml').read_text()).group(1)
    return {
        'plugin_version': version,
        'sources': {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in paths.items()},
        'configuration': parsed['config.yml'],
        'permissions': parsed['plugin.yml']['permissions'],
        'symbols': [{'id': key, 'name': val['name'], 'texture_url': val['url']}
                    for key, val in parsed['symbols.yml']['symbols'].items()],
    }


def flatten(mapping, prefix=''):
    for key, value in mapping.items():
        name = f'{prefix}.{key}' if prefix else key
        if isinstance(value, dict) and value:
            yield from flatten(value, name)
        else:
            yield name, value


def cell(value):
    return json.dumps(value, ensure_ascii=False, separators=(', ', ': ')).replace('|', '&#124;')


def configuration(data):
    text = ['# Configuration defaults', '',
            f"Bundled defaults for **Beliefs {data['plugin_version']}**. Your server’s file may differ.", '',
            'Edit `plugins/Beliefs/config.yml` and restart. For guidance, see [Configure your server](../server/configuration.md).', '',
            'Existing configuration files are retained on upgrades. These tables are generated from the plugin’s default resources.', '']
    for section, settings in data['configuration'].items():
        text += [f'## {section.replace("-", " ").capitalize()}', '', '| Setting | Default |', '| --- | --- |']
        values = flatten(settings, section) if isinstance(settings, dict) else [(section, settings)]
        for key, value in values:
            text.append(f'| `{key}` | `{cell(value)}` |')
        text += ['']
    text += ['## Full default file', '', '```yaml', yaml.safe_dump(data['configuration'], sort_keys=False, allow_unicode=True).rstrip(), '```', '']
    return '\n'.join(text)


def permissions(data):
    text = ['# Permissions', '', 'These are the permission nodes declared by Beliefs.', '',
            '| Permission | Default | Allows |', '| --- | --- | --- |']
    notes = {'beliefs.use': 'Use Beliefs commands and menus.',
             'beliefs.create': 'Create a faith (also requires `beliefs.use`).',
             'beliefs.admin': 'Use `/faithadmin` administration commands.'}
    for key, value in data['permissions'].items():
        default = value.get('default', 'op')
        label = {True: 'Everyone', False: 'Nobody by default', 'op': 'Operators', 'not op': 'Non-operators'}.get(default, str(default))
        text.append(f'| `{key}` | {label} | {notes.get(key, value.get("description", "See the plugin permission definition."))} |')
    text += ['', 'Faith roles are separate from server permissions. Being an operator does not make you a faith’s founder or clergy. Founders edit doctrine; clergy handle their permitted community tasks.', '',
             'Use your server’s permission manager to grant or deny these nodes. See [Commands](commands.md) and [People & places](../leaders/people-and-places.md).', '']
    return '\n'.join(text)


def symbols(data):
    text = ['# Symbol gallery', '', f"The bundled catalogue has **{len(data['symbols'])} symbols**. Choose one in **Settings → Identity → Symbol**, then save.", '',
            'These are the pixel-art faces used by the player-head items. Symbols are artwork; choosing one does not apply teachings or membership rules.', '',
            '<div class="symbol-gallery">']
    for symbol in data['symbols']:
        key, name = symbol['id'], html.escape(symbol['name'])
        if not re.fullmatch(r'[a-z0-9_]+', key):
            raise ValueError(f'Unsafe symbol filename: {key}')
        if not (ROOT / f'docs/images/symbols/{key}.png').is_file():
            raise ValueError(f'Missing local symbol artwork: {key}')
        text.append(f'<div class="symbol-card"><img src="../../images/symbols/{key}.png" alt="{name}" width="64" height="64" loading="lazy"><span>{name}</span><code>{key}</code></div>')
    text += ['</div>', '', '## Customize the catalogue', '',
            'Edit `plugins/Beliefs/symbols.yml`, keep entries under its `symbols:` mapping, and restart to reload the picker. Preserve your custom entries when adding new built-in symbols; replacing the JAR does not merge the existing catalogue.', '',
            'An empty `symbols: {}` disables preset heads. Custom-head entry remains available. The protected Agnostic community uses the separate `agnostic.head-texture` setting.', '',
            '[Use a symbol or custom head](../leaders/symbols-and-scripture.md) · [Configuration defaults](configuration.md)', '']
    return '\n'.join(text)


def material_icon(material, x, y):
    if material == 'GOLD_INGOT':
        return f'<g transform="translate({x} {y})"><path d="m4 23 8-12h22l8 12-6 10H10z" fill="#e5bb4c" stroke="#76551d" stroke-width="2"/><path d="m4 23 10 3h18l10-3M12 11l2 15-4 7M34 11l-2 15 4 7" fill="none" stroke="#fff0a1" stroke-width="2"/></g>'
    if material == 'DIAMOND':
        return f'<g transform="translate({x} {y})"><path d="m4 15 8-8h24l8 8-20 25z" fill="#83d8dc" stroke="#335b65" stroke-width="2"/><path d="M4 15h40M12 7l5 8 7 25 7-25 5-8" fill="none" stroke="#d9ffff" stroke-width="2"/></g>'
    label = html.escape(material.replace('_', ' ').title())
    return f'<text x="{x+24}" y="{y+25}" fill="#eee9df" font-size="8" text-anchor="middle">{label}</text>'


def recipe(data):
    recipe = data['configuration']['marriage-ring']['recipe']
    rows = recipe['shape']
    if len(rows) != 3 or any(len(row) != 3 for row in rows):
        raise ValueError('Recipe diagram requires the configured three-by-three grid.')
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 550 244" role="img" aria-labelledby="title desc">',
             '<title id="title">Default marriage ring recipe</title>',
             '<desc id="desc">Three by three crafting grid. ' + html.escape('; '.join(', '.join(recipe['ingredients'][ch].replace('_', ' ').lower() if ch != ' ' else 'empty' for ch in row) for row in rows)) + '. Makes one marriage ring.</desc>',
             '<rect x="1" y="1" width="548" height="242" rx="10" fill="#24201b" stroke="#65543b"/>',
             '<g font-family="system-ui, sans-serif"><text x="30" y="30" fill="#c7ad73" font-size="14">CRAFTING TABLE</text>']
    for row_index, row in enumerate(rows):
        for col_index, token in enumerate(row):
            x, y = 30 + col_index * 56, 44 + row_index * 56
            parts.append(f'<rect x="{x}" y="{y}" width="52" height="52" rx="3" fill="#171512" stroke="#77654a"/>')
            if token != ' ':
                parts.append(material_icon(recipe['ingredients'][token], x + 2, y + 2))
    parts += ['<path d="M226 122h63m-18-14 18 14-18 14" fill="none" stroke="#c7ad73" stroke-width="5" stroke-linejoin="round"/>',
              '<rect x="322" y="72" width="92" height="92" rx="5" fill="#171512" stroke="#77654a"/>',
              '<ellipse cx="368" cy="126" rx="23" ry="25" fill="none" stroke="#9d7331" stroke-width="12"/>',
              '<ellipse cx="368" cy="123" rx="23" ry="25" fill="none" stroke="#e1bd64" stroke-width="6"/>',
              '<path d="m353 94 6-8h18l6 8-15 17z" fill="#aadfe7" stroke="#eafcff" stroke-width="2"/>',
              '<text x="368" y="194" fill="#eee9df" font-size="16" text-anchor="middle">Marriage ring ×1</text>',
              '<text x="30" y="228" fill="#bab3a7" font-size="12">Default recipe · Your server may use different ingredients.</text>',
              '</g></svg>']
    return '\n'.join(parts) + '\n'


def outputs(data):
    return {'docs/reference/configuration.md': configuration(data),
            'docs/reference/permissions.md': permissions(data),
            'docs/reference/symbols.md': symbols(data),
            'docs/images/marriage-ring.svg': recipe(data)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, help='Beliefs plugin checkout; refresh the public snapshot.')
    parser.add_argument('--check', action='store_true', help='Fail if generated files or the source snapshot differ; write nothing.')
    args = parser.parse_args()
    data = snapshot(args.source) if args.source else json.loads(SNAPSHOT.read_text())
    files = outputs(data)
    if args.source:
        files['tools/source-snapshot.json'] = json.dumps(data, indent=2, ensure_ascii=False) + '\n'
    stale = [name for name, value in files.items() if not (ROOT/name).is_file() or (ROOT/name).read_text() != value]
    if args.check:
        if stale:
            sys.exit('Outdated generated files: ' + ', '.join(stale))
        print(f'Generated reference check passed ({len(files)} files).')
    else:
        for name in stale:
            (ROOT/name).write_text(files[name])
        print(f'Generated {len(files)} references; {len(stale)} updated.')


if __name__ == '__main__':
    main()
