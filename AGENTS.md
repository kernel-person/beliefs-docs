# Beliefs wiki

This is the standalone public documentation repository, not the plugin source.

- Keep guides concise and task-oriented. Separate Players, Faith leaders and Server owners.
- Match current source behavior and exact labels. The plugin README may include obsolete UI descriptions.
- Use the brass/gold theme with white and gray secondary text. Relationships remain gender-neutral.
- Never publish server data, credentials, private diagnostics, test-character controls or unimplemented promises.
- Never launch Minecraft or a launcher unless the user explicitly asks.
- Maintain generated references with `tools/generate_reference.py`; do not hand-edit their output.
- The default sibling source path is `../beliefs`. CI builds from the checked-in public snapshot.
- Before a push, run the reference check, strict MkDocs build and `tools/check_site.py site`.
- Verify the live page after authorized publication. Use the repository owner’s configured GitHub account without changing unrelated active accounts.
