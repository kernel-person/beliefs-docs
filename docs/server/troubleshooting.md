# Troubleshooting

Start with the startup log and `faithadmin status` in the console. The status command reports the number of active faiths and whether the family-tree adapter initialized.

## Beliefs does not start or `/faith` is missing

Confirm the server uses the known target: **Paper 26.2 build 71 and Java 25**, with one Beliefs JAR in `plugins`. Look for `Beliefs could not start` and the first error that follows it.

If the error mentions configuration or symbols, check the edited YAML against the [configuration](../reference/configuration.md) and [symbols](../reference/symbols.md) references. If it mentions the database, check filesystem access and the full error; do not delete `beliefs.db` to make startup succeed.

## The family tree is unavailable

Read the adapter detail from `/faithadmin status`. `Family tree unavailable` points to a server compatibility or initialization problem. The adapter uses Paper internals, so a different server build may need a matching Beliefs update.

If the adapter is ready but the view is unexpected, reopen `/faith family`. A view has a selected person and depth; `/faith family <player> <depth>` accepts depths from `0` to `8`. A ready adapter is a server check, not proof that every client displays the view correctly.

## A player cannot create, edit or officiate

Check the [permission reference](../reference/permissions.md), then the player's role in that faith. Founding requires `beliefs.create`; editing a player-founded faith requires its founder. Clergy powers and founder powers are different. Operator status does not replace the family-ceremony consent and role checks.

For server-owned faiths, use `/faithadmin clergy <faith> <player> true` after the player joins. Agnostic has no clergy.

For a marriage or adoption, open `/faith pending`. Every required participant must consent, the request must still be valid, and an authorized officiant who is not a participant must complete it with the participants nearby. Marriage also needs its recorded ring giver online with a Marriage Ring.

## Prayer or a ceremony will not progress

Use `/faith worship` to see the current ceremony step and fast timer. Start prayer explicitly with `/faith pray`; merely sneaking does not start a prayer. Follow the current step, stay within the ceremony's required area and check that enough participants have joined.

For a directional bonus, check `/faith holyplace info`. A missing lodestone or a destination in another world can make the bonus unavailable while ordinary prayer still works. Cooldowns and a disabled outcome can also block an action; check the feedback and [server settings](../reference/configuration.md).

Use `/faith cancel` to cancel an active ceremony or fast. Cancelling a shared ceremony ends that session for its participants.

## Food shows Unknown or a custom dish is missing

Inspect the actual dish. A preview, older item or incomplete ingredient history may not contain enough evidence. Unknown alone causes no food-rule violation. Known forbidden ingredients can still make a dish forbidden.

If you use Heirloom, confirm it enabled successfully and that its build supplies the expected food API. See the [Heirloom guide](heirloom.md) for fallback behavior and compatibility scope.

## A Nether verdict uses normal respawn

Set the arrival again with `/faithadmin nether` while standing in a safe Nether location. Beliefs checks the saved world and the safety of the destination before using it. Personal respawn points remain unchanged.

## A holy day appears at the wrong time

Check `community.timezone` and the date and recurrence saved for that holy day. Invalid timezone names produce a warning and fall back to `Europe/London`. Restart after changing the server setting.

## Report an unresolved problem

Include the Beliefs version, Paper build, Java version, exact action, expected result, actual result and relevant log excerpt. Add Heirloom's exact build if food integration is involved. Remove credentials, license data and private player information before sharing. Keep backups locally; do not post your database as a first troubleshooting step.
