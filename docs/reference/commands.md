# Commands

Use `/faith` for guided menus. `/beliefs` and `/religion` are aliases. Player commands require `beliefs.use`; additional permissions and faith roles are noted below. See [permissions](permissions.md).

`<value>` is required, `[value]` is optional. Replace the brackets with your value. Faith names can contain spaces; commands that choose a faith also accept its UUID. Request and ceremony IDs come from the relevant menu or chat link.

## Open a screen

| Command | Opens |
| --- | --- |
| `/faith` | Your home menu. |
| `/faith list` | Faith discovery. `/faith browse` does the same. |
| `/faith view [faith]` | The selected faith, or your own. |
| `/faith guide` | First Steps. |
| `/faith members` | Your faith's members. |
| `/faith teachings` | Your faith's teachings. |
| `/faith food` | Your faith's food rules and catalogue. |
| `/faith rituals` | Available rituals and ceremonies. |
| `/faith relationships` | Family actions. |
| `/faith pending` | Family requests you participate in or can officiate. |
| `/faith inspect [player]` | A person's details; defaults to you. |
| `/faith family [player] [depth]` | Family tree; defaults to you and depth `3`. Depth may be `0`–`8`. |
| `/faith report` | Your latest completed life report, available after your first death. |
| `/faith calendar` | Your faith's holy days. |
| `/faith memorial` | Memorials and available actions. |

## Membership and practice

| Command | Action |
| --- | --- |
| `/faith create <name>` | Found a faith, then configure it. Requires `beliefs.create` and eligibility to found one. |
| `/faith join <faith>` | Join or apply according to that faith's membership policy. |
| `/faith leave` | Return to Agnostic. A founder with other members must transfer leadership first. |
| `/faith book` | Request your faith's sacred text, subject to the shared sacred-item cooldown. |
| `/faith pray` | Begin prayer, or begin the prayer step in your current ceremony. |
| `/faith ritual start <ritual-id>` | Start a ritual if its requirements permit. |
| `/faith ritual join <ceremony-id>` | Join an active ceremony. |
| `/faith offer` | Reserve the required held offering for the current ceremony step. |
| `/faith bless` | Perform the current blessing step. In a clergy-led ceremony, the leader must do this. |
| `/faith fast` | Start a voluntary fast using your faith's duration. |
| `/faith worship` | Show ceremony progress and any active fast timer. |
| `/faith cancel` | Cancel your active ceremony or fast; a shared ceremony ends for everyone in it. |
| `/faith holyplace info` | Check your faith's directional-prayer destination and current guidance. |
| `/faith compass` | Bind an ordinary, unbound compass held in your main hand to your faith's holy place. |
| `/faith memorial nearby` | Show nearby memorial gatherings. |
| `/faith memorial cancel` | Leave your memorial gathering. |

## Family requests

Prefer `/faith relationships` and `/faith pending` when choosing people or reviewing consent. The command equivalents are:

| Command | Action |
| --- | --- |
| `/faith marry request <player> [ceremony]` | Ask to marry someone while holding a Marriage Ring. |
| `/faith marry consent <request-id>` | Accept the full group; an ordinary request completes once everyone accepts and the ring is available. |
| `/faith marry decline <request-id>` | Decline a marriage request. |
| `/faith adopt request <parent> <child> [ceremony]` | Request adoption as a participant. The parent's current marriage group becomes the proposed parent set. |
| `/faith adopt consent <request-id>` | Accept the parent group; an ordinary request completes on the final consent. |
| `/faith adopt decline <request-id>` | Decline an adoption request. |
| `/faith divorce` | Leave your marriage; parent–child connections remain. |
| `/faith unadopt [player]` | Choose and review one of your direct parent–child connections to end. |
| `/faith marry complete <request-id>` | Finish an accepted ordinary request when its ring is available; a ceremony requires an authorized officiant and everyone nearby. |
| `/faith adopt complete <request-id>` | Complete an accepted request; a ceremony requires an authorized officiant and everyone nearby. |

Every required participant must consent. Ordinary requests complete after the final acceptance; marriage also requires the sender’s ring. Add `ceremony` to request a priest-led completion instead. Ending a parent connection is separate from divorce; historical ancestry remains protected.

In a joined ceremony, sneak and stand still to pray, or drop the required offering. These actions need no command.

## Clergy and founders

| Command | Role and action |
| --- | --- |
| `/faith invite <player>` | Clergy: invite a player. |
| `/faith approve <player>` | Clergy: accept a membership application. |
| `/faith decline <player>` | Clergy: remove a membership application or invitation. |
| `/faith temple <name> <radius>` | Clergy: register a worship area at your position. |
| `/faith holyplace set <name>` | Clergy: register the lodestone you are looking at within six blocks. |
| `/faith holyplace clear` | Clergy: remove the holy destination and restore unrestricted prayer. |
| `/faith calendar manage` | Clergy: manage your faith's holy days. |
| `/faith calendar new` | Clergy: open the new holy-day form. |
| `/faith marry propose <players>` | Clergy: propose a marriage; separate player names with spaces or commas. |
| `/faith adopt propose <parent> <child>` | Clergy: propose adoption with the parent's current marriage group. |
| `/faith settings` | Founder: manage identity, customs, food, teachings and rituals. `/faith manage` is an alias. |
| `/faith clergy <player> <true-or-false>` | Founder: appoint a current member as clergy with `true`, or return them to membership with `false`. |
| `/faith transfer <player>` | Founder: transfer leadership to another current member. You remain clergy. |
| `/faith scripture` | Founder: copy the held written book or book and quill into the sacred text. |
| `/faith disband` | Founder: archive the faith. Family and life history remain. |

Ordinary requests need no officiant. For ceremony requests, the officiant must be authorized and cannot be a participant. For priest help, open the family request and choose **Priest help**; its buttons use the current request state.

## Server administration

These require `beliefs.admin` (operators by default).

```text
/faithadmin setup [faith]
/faithadmin status
/faithadmin clergy <faith> <player> <true|false>
/faithadmin nether
```

`setup` opens a read-only checklist for clergy, temples, optional prayer direction and holy days. Choose a faith, or supply its full name or UUID. **Commands in chat** provides suggestions to review and send; opening the guide changes nothing.

`status` reports the faith count and family-tree adapter state. `clergy` appoints or removes clergy for an existing member of a server-owned faith; it cannot appoint Agnostic clergy or edit player-founded leadership. These commands also work from the console without the leading slash.

`nether` must be run by a player standing at a safe Nether arrival point. It saves that position without changing personal respawn points. See [server configuration](../server/configuration.md).

### Family tools

| Command | Action |
| --- | --- |
| `/faithadmin family [player]` | Open the family tools and review a change. |
| `/faithadmin tool` | Receive the wand; right-click a player to view their Beliefs menus. |
| `/faithadmin as <player>` | View an online player's menus as that player. |
| `/faithadmin stop` | End the acting session and return to your own menu. |
| `/faithadmin marry <player> <player> [...]` | Marry the chosen people, including their existing group. Separate marriage groups cannot merge. |
| `/faithadmin divorce <player>` | Remove that person from their marriage. `/faithadmin breakup` is an alias. |
| `/faithadmin adopt <parent> <child>` | Adopt with the parent's full current marriage group, or that parent alone. |
| `/faithadmin unadopt <parent> <child>` | End exactly this direct parent–child connection. |

Explicit family-edit commands apply immediately. They skip consent, rings and ceremony presence, award no deeds, and retain faith, size, kinship and cycle checks. Names with spaces need quotes; UUIDs are also accepted. Read [Family administration](../server/family-tools.md) before editing.
