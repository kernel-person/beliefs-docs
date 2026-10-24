# Install Beliefs

Beliefs is currently a **`0.1.0-SNAPSHOT` preview**. The known target is **Paper 26.2 build 71 with Java 25**. Other server versions and forks are not established compatibility targets.

Beliefs uses native Minecraft menus, items and advancements. **No resource pack is required.** [Heirloom](heirloom.md) is optional; vanilla food support works without it.

## Install the JAR

1. Stop the server cleanly. For an existing server, make a [backup](updating.md#back-up-and-update) first.
2. Put the supplied `Beliefs.jar` in the server's `plugins` directory. Keep only one Beliefs JAR there.
3. Start the server with Java 25. Check the console for `Beliefs ready.` and any startup errors.
4. Run `faithadmin status` in the console, or `/faithadmin status` as an administrator in game. It reports the faith count and family-tree adapter state; the expected adapter message is `Paper 26.2 advancement packets ready`.
5. Run `/faithadmin setup` to review clergy, temples, optional prayer direction and holy days for each faith. Console users can run `faithadmin setup` or `faithadmin setup <faith>`.
6. Open `/faith` in game to begin.

The first successful start creates `plugins/Beliefs/config.yml`, `symbols.yml`, `example-holy-days.yml` and the SQLite database `beliefs.db`. Beliefs does not need a separate database server.

Keep player data saving enabled. Offerings and memorial deliveries depend on saved inventories and player records.

By default, players can use Beliefs and found a faith. Administration is operator-only unless your permissions plugin grants it. See the [permission reference](../reference/permissions.md).

## Choose your starting communities

New players begin in **Agnostic**, the neutral starting faith. The default configuration also installs bundled server-owned example faiths.

To omit the examples on a fresh installation, create `plugins/Beliefs/config.yml` from the [default configuration](../reference/configuration.md) and set `examples.enabled: false` **before the first start**. Turning it off later prevents installation of missing examples; it does not remove communities already saved in the database.

The protected examples also receive configurable [holy-day calendars](configuration.md#example-holy-days). Their observances use real-world dates and start no ceremonies or rewards.

Continue with [server configuration](configuration.md) to set your limits, appoint clergy for server-owned faiths and configure a safe Nether arrival.
