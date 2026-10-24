#!/usr/bin/env python3
"""Check built HTML page links, fragments and local assets without network access."""
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.ids, self.urls = set(), []
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('src', 'href', 'poster'):
            if key in attrs:
                self.urls.append(attrs[key])


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else 'site').resolve()
    pages = {path: Page(path.read_text()) for path in root.rglob('*.html')}
    errors, checked = [], 0
    for path, page in pages.items():
        for url in page.urls:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not url:
                continue
            target = path if not parts.path else (path.parent / unquote(parts.path)).resolve()
            if parts.path.startswith('/'):
                relative = parts.path.removeprefix('/beliefs-docs/').lstrip('/')
                target = root / relative
            if not target.is_relative_to(root):
                errors.append(f'{path.relative_to(root)}: link escapes site: {url}')
                continue
            if target.is_dir():
                target /= 'index.html'
            if not target.exists():
                errors.append(f'{path.relative_to(root)}: missing {url}')
            elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
                errors.append(f'{path.relative_to(root)}: missing anchor {url}')
            checked += 1
    if not pages:
        errors.append('No HTML pages found.')
    if errors:
        sys.exit('\n'.join(errors))
    print(f'Site check passed: {len(pages)} HTML pages, {checked} local links/assets/fragments.')


if __name__ == '__main__':
    main()
