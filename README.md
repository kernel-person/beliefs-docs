# Beliefs Docs

The public player, faith-leader and server-owner wiki for Beliefs.

- Site: <https://kernel-person.github.io/beliefs-docs/>
- Repository: <https://github.com/kernel-person/beliefs-docs>
- Documented plugin: **0.1.0-SNAPSHOT**, Paper **26.2 build 71**, Java **25**.

## Preview locally

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000/`. No Minecraft client or server is required.

## Update the wiki with the plugin

Keep player instructions aligned with current menu labels and behavior. The plugin README contains historical feature notes, so check the implementation when a flow has changed. Keep draft features, internal test reports and debug controls out of public guides.

Configuration, permissions, the symbol catalogue and ring recipe illustration are generated from a small public snapshot of bundled plugin resources:

```sh
python tools/generate_reference.py --source ../beliefs
python tools/generate_reference.py --source ../beliefs --check
python tools/generate_reference.py --check
mkdocs build --strict
python tools/check_site.py site
```

The source snapshot records resource checksums and plugin version. It contains only public defaults, permission definitions and symbol metadata. Regeneration never reads a running server’s data folder. If the catalogue adds a symbol, copy its finished face artwork into `docs/images/symbols/` before regeneration.

The snapshot and generated files are committed, so contributors and CI can build the complete site without the plugin repository, Minecraft, credentials or an asset download.

## Publishing

The GitHub Actions workflow checks references, builds in strict mode and validates page links. Pull requests only run checks. A successful push to `main` uploads the built site and publishes it with GitHub’s Pages deployment action.

GitHub Pages settings: **Build and deployment → Source → GitHub Actions**. The publishing job uses the `github-pages` environment; no deploy key or separate publishing branch is needed.

Before publishing a gameplay change:

1. Update the affected short guide and regenerate any changed resource reference.
2. Run the checks above.
3. Check desktop and phone-sized layouts, especially the symbol gallery and recipe.
4. Verify the Actions deployment and the public page after pushing.

## Artwork

Symbol faces are the user-provided artwork registered in Beliefs’ catalogue. The book mark is a local SVG. The recipe image uses genuine Minecraft textures and the exact Beliefs ring-head skin, rendered offline using the bundled native GUI transform. Its recipe follows the plugin configuration; it is not a game screenshot. See [credits](docs/reference/credits.md). Add genuine screenshots only when their controls match the documented build.
