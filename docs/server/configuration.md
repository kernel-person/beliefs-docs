# Configure your server

`plugins/Beliefs/config.yml` sets server-wide limits and defaults. A faith's own name, teachings, food rules and rituals are saved in `beliefs.db` and managed through `/faith settings` by its founder.

Stop the server before editing configuration files, preserve a backup, then restart. The [configuration reference](../reference/configuration.md) contains the shipped `config.yml` settings and defaults.

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

## Review the setup checklist

Run `/faithadmin setup` and choose a faith, or use `/faithadmin setup <faith name or UUID>`. This requires `beliefs.admin` and also works from the console without the leading slash.

The guide shows saved clergy, registered temples, optional prayer direction, and saved/upcoming holy-day counts. **Refresh** reads the current saved state. **Commands in chat** supplies commands labelled with who can run them; clicking a suggestion fills the chat input for you to review and send.

Opening the guide changes nothing. An administrator appoints clergy for a server-owned faith after the player joins; a player faith's founder appoints its clergy. Temple and holy-place commands must be run in the world by that faith's clergy. A saved holy-place entry does not prove its lodestone still exists. Agnostic needs no religious setup.

## Give a server-owned faith clergy

First have the intended player join that faith. Then run:

```text
/faithadmin clergy <faith> <player> true
```

Use its full name or UUID for `<faith>`. Set the last argument to `false` to return that person to ordinary membership. This works from the console without the leading slash.

The command applies only to current members of server-owned faiths. Agnostic has no clergy. In player-founded faiths, the founder appoints clergy through the members menu or `/faith clergy <player> true`.

Appointing clergy does not create a player founder or unlock founder-only editing of a server-owned faith.

## Example holy days

`plugins/Beliefs/example-holy-days.yml` supplies observances for the protected Catholicism, Islam and Buddhism examples, including examples already installed before this feature. It does not add occasions to player-created faiths with matching names.

| Faith | Bundled observances | Date basis |
| --- | --- | --- |
| Catholicism | Christmas, All Saints, Easter Sunday | December 25, November 1, and Western Gregorian Easter calculated each year. |
| Islam | Eid al-Fitr, Eid al-Adha | First day of each festival in the Saudi Umm al-Qura calendar; local moon-sighting dates may differ. |
| Buddhism | Vesak (Singapore) | Published dates: May 31, 2026 and May 20, 2027. |

These are all-day entries in `community.timezone`, from local midnight to the next midnight. They start no worship, award no rewards and send no chat announcement by default. The civil-day display does not model sunset-based observance boundaries.

Set the file's `enabled: false`, or an entry's `enabled: false`, to remove only unchanged presets on restart. You can also change an entry's `title`, `date`, `repeat` and `announce`. Keep its key stable. Clergy edits and explicit removals are preserved across restarts; changing the file never overwrites them. Re-enabling a preset restores one disabled through configuration, but not one removed by clergy.

For a locally confirmed Eid date, use `repeat: ONCE` and its Gregorian `date: 'YYYY-MM-DD'`. Calculated repeats use `date` as their earliest allowed date. The Umm al-Qura calendar has a finite supported date range.

For future Vesak dates, add a new entry such as `vesak-2028` under `faiths.buddhism` once that region's date is published. Use `repeat: ONCE`, a region-labelled title, and the actual observance date rather than a substitute public holiday. The bundled Vesak schedule ends in 2027; do not use a fixed Gregorian yearly repeat. Existing configuration files are retained during upgrades, so add newly published dates yourself.

Date sources: [USCCB's 2027 liturgical calendar](https://www.usccb.org/resources/2027cal.pdf), the [Java Umm al-Qura calendar](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/time/chrono/HijrahChronology.html), and Singapore's official [2026](https://www.mom.gov.sg/newsroom/press-releases/2025/0616-public-holidays-for-2026) and [2027](https://www.mom.gov.sg/newsroom/press-releases/2026/0618-public-holidays-for-2027) calendars.

## Set a safe Nether arrival

If a faith uses afterlife judgment, prepare a safe arrival point for a Nether verdict. Stand in a Nether world on safe solid ground with two clear blocks of space, then run:

```text
/faithadmin nether
```

Beliefs saves the world, position and facing in `config.yml`. The command does not change personal respawn points. If the saved world is unavailable or the location becomes unsafe, a Nether verdict uses normal respawn and writes a warning to the server log.

## Symbols and access

The selectable faith symbols are stored in `plugins/Beliefs/symbols.yml`; Agnostic's texture is configured separately in `config.yml`. Preserve both files when updating. See [symbols](../reference/symbols.md) for the choices and [permissions](../reference/permissions.md) for access controls.
