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
from recipe_render import render_recipe

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / 'tools/source-snapshot.json'


def snapshot(source):
    resources = source / 'src/main/resources'
    paths = {name: resources / name for name in ('config.yml', 'plugin.yml', 'symbols.yml')}
    parsed = {name: yaml.safe_load(path.read_text()) for name, path in paths.items()}
    ring_source = source / 'src/main/java/ke/ric/beliefs/runtime/MarriageRings.java'
    ring_url = re.search(r'https?://textures\.minecraft\.net/texture/[a-f0-9]+', ring_source.read_text()).group(0).replace('http:', 'https:')
    manifest = json.loads((ROOT / 'tools/recipe-assets/manifest.json').read_text())
    if ring_url != manifest['ring_texture_url']:
        raise ValueError('Ring texture changed: update the bundled skin and provenance before generating.')
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


def outputs(data):
    return {'docs/reference/configuration.md': configuration(data),
            'docs/reference/permissions.md': permissions(data),
            'docs/reference/symbols.md': symbols(data),
            'docs/images/marriage-ring.png': render_recipe(data['configuration'])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, help='Beliefs plugin checkout; refresh the public snapshot.')
    parser.add_argument('--check', action='store_true', help='Fail if generated files or the source snapshot differ; write nothing.')
    args = parser.parse_args()
    data = snapshot(args.source) if args.source else json.loads(SNAPSHOT.read_text())
    files = outputs(data)
    if args.source:
        files['tools/source-snapshot.json'] = json.dumps(data, indent=2, ensure_ascii=False) + '\n'
    files = {name: value.encode('utf-8') if isinstance(value, str) else value for name, value in files.items()}
    stale = [name for name, value in files.items() if not (ROOT/name).is_file() or (ROOT/name).read_bytes() != value]
    if args.check:
        if stale:
            sys.exit('Outdated generated files: ' + ', '.join(stale))
        print(f'Generated reference check passed ({len(files)} files).')
    else:
        for name in stale:
            (ROOT/name).write_bytes(files[name])
        print(f'Generated {len(files)} references; {len(stale)} updated.')


if __name__ == '__main__':
    main()
