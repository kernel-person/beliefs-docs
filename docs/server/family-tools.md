# Family administration

Use `/faithadmin family [player]` to review a marriage, divorce, adoption or ended parent connection. These tools require `beliefs.admin`.

## View as a player

Run `/faithadmin tool`, then right-click an online player with the wand. Their Beliefs menus open on **your** screen, with an **Acting as** label; their own screen stays unchanged. `/faithadmin as <player>` opens the same view.

The view uses that player's faith and roles. Changes affect their profile, so use **Stop viewing** or `/faithadmin stop` when finished. Ordinary `/faith` commands also return to your identity. World rituals and item delivery require leaving the acting view.

## Edit a family

The family menu shows everyone affected before you confirm. For direct commands, see the [command reference](../reference/commands.md#family-tools).

- **Marry** includes every member of a selected existing marriage. Separate marriage groups cannot merge.
- **Divorce** removes one person. At least two remaining partners stay married.
- **Adopt** includes the parent's full current marriage group. The child must have no active parents.
- **End adoption** removes one direct parent–child link; other parents remain.

These explicit administrator edits skip consent, rings and ceremony presence, and award no religious deeds. Faith restrictions, the server's marriage limit, kinship and cycles still apply. Each change is audited; changed relationships invalidate affected pending requests.

Ending adoption removes the active link from the tree, but never erases its historical ancestry. A child may be adopted again after all active parent links end. Former relatives remain unable to marry.
