# Updates and backups

Beliefs is a preview. Test a new build against a separate copy of your server before using it for an established community.

## Back up and update

1. Stop the server cleanly and wait for it to finish saving.
2. Back up the **whole server at that stopped point**. In particular, keep the entire `plugins/Beliefs` directory and the worlds' player data together. Keep the old Beliefs JAR too.
3. Replace the Beliefs JAR with the new build. Preserve `config.yml`, `symbols.yml` and `beliefs.db`; do not replace them with empty defaults.
4. Compare your settings with the new build's configuration reference and release notes. Add or adjust settings deliberately.
5. Start the server and check the startup log and `faithadmin status`.
6. Check that existing faiths, family relationships and life reports still appear before reopening the server to everyone.

The database and player data form one backup set. Offerings and memorial deliveries keep related records in both places. Restoring only `beliefs.db`, or only player inventories, can leave those records out of sync. Keep any SQLite sidecar files that remain in the plugin directory with the stopped-server backup.

## Roll back as one set

Stop the server, then restore the old JAR and its matching stopped-server backup together. A rollback discards changes made after that backup, so preserve the failed installation separately for diagnosis first.

Do not assume an older JAR can read data written by a newer build. Beliefs refuses a database whose schema version is newer than it understands.

## After a problem

Keep the full error and the build versions. Use [troubleshooting](troubleshooting.md) to narrow the cause before changing saved data. A clean restart is the supported workflow described here for plugin and configuration changes.
