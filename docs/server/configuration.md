# Configure your server

`plugins/Beliefs/config.yml` sets server-wide limits and defaults. A faith's own name, teachings, food rules and rituals are saved in `beliefs.db` and managed through `/faith settings` by its founder.

Stop the server before editing configuration files, preserve a backup, then restart. The [configuration reference](../reference/configuration.md) contains every shipped setting and default.

## Settings to review first

| Setting | What it controls |
| --- | --- |
| `examples.enabled` | Installs missing bundled server-owned faiths at startup. `false` does not delete existing ones. |
| `limits.marriage-members` | Maximum marriage size a founder can choose; each faith may choose a smaller limit. |
| `limits.teaching-weight` | Maximum magnitude of a teaching's positive or negative points. |
| `limits.ceremony-distance` | How close family-ceremony participants must be to the officiant. |
| `limits.consent-seconds` | How long marriage and adoption requests remain open. |
| `community.timezone` | Timezone for real-world holy days. Use an IANA name such as `Europe/London`. |
| `worship.allowed-outcomes` | Ritual powers permitted on the server. An empty list disables all ceremony outcomes, including prayer. |
| `worship.allowed-weather-worlds` | World names or UUIDs allowed for weather rituals. An empty list allows normal Overworld environments. |
| `marriage-ring.recipe` | Whether rings can be crafted and which recipe is used. Recipe changes apply on restart; existing rings remain valid. |

Prayer timing, directional bonuses, sacred-item cooldowns, fasting and judgment also have server settings. Change the relevant values in the [full reference](../reference/configuration.md), rather than treating a faith's chosen custom as a server default.

## Give a server-owned faith clergy

First have the intended player join that faith. Then run:

```text
/faithadmin clergy <faith> <player> true
```

Use its full name or UUID for `<faith>`. Set the last argument to `false` to return that person to ordinary membership. This works from the console without the leading slash.

The command applies only to current members of server-owned faiths. Agnostic has no clergy. In player-founded faiths, the founder appoints clergy through the members menu or `/faith clergy <player> true`.

Appointing clergy does not create a player founder or unlock founder-only editing of a server-owned faith.

## Set a safe Nether arrival

If a faith uses afterlife judgment, prepare a safe arrival point for a Nether verdict. Stand in a Nether world on safe solid ground with two clear blocks of space, then run:

```text
/faithadmin nether
```

Beliefs saves the world, position and facing in `config.yml`. The command does not change personal respawn points. If the saved world is unavailable or the location becomes unsafe, a Nether verdict uses normal respawn and writes a warning to the server log.

## Symbols and access

The selectable faith symbols are stored in `plugins/Beliefs/symbols.yml`; Agnostic's texture is configured separately in `config.yml`. Preserve both files when updating. See [symbols](../reference/symbols.md) for the choices and [permissions](../reference/permissions.md) for access controls.
