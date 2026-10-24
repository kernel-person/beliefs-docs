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
| `/faith marry request <player>` | Ask to marry someone while holding a Marriage Ring. |
| `/faith marry consent <request-id>` | Give your consent to a marriage request. |
| `/faith marry decline <request-id>` | Decline a marriage request. |
| `/faith adopt request <parent> <child>` | Request adoption as a participant. The parent's current marriage group becomes the proposed parent set. |
| `/faith adopt consent <request-id>` | Give your consent to an adoption request. |
| `/faith adopt decline <request-id>` | Decline an adoption request. |
| `/faith divorce` | Leave your marriage; permanent parent–child relationships remain. |

Every required participant must consent. Sending or accepting a request does not complete it. Adoption makes its parent set permanent.

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
| `/faith marry complete <request-id>` | Authorized officiant: complete a fully consented marriage with the required ring and everyone nearby. |
| `/faith adopt propose <parent> <child>` | Clergy: propose adoption with the parent's current marriage group. |
| `/faith adopt complete <request-id>` | Authorized officiant: complete a fully consented adoption with everyone nearby. |
| `/faith settings` | Founder: manage identity, customs, food, teachings and rituals. `/faith manage` is an alias. |
| `/faith clergy <player> <true-or-false>` | Founder: appoint a current member as clergy with `true`, or return them to membership with `false`. |
| `/faith transfer <player>` | Founder: transfer leadership to another current member. You remain clergy. |
| `/faith scripture` | Founder: copy the held written book or book and quill into the sacred text. |
| `/faith disband` | Founder: archive the faith. Family and life history remain. |

An officiant must be authorized for that request and cannot be one of its participants. For priest help, open the family request and choose **Priest help**; its buttons use the current request state.

## Server administration

These require `beliefs.admin` (operators by default).

```text
/faithadmin status
/faithadmin clergy <faith> <player> <true|false>
/faithadmin nether
```

`status` reports the faith count and family-tree adapter state. `clergy` appoints or removes clergy for an existing member of a server-owned faith; it cannot appoint Agnostic clergy or edit player-founded leadership. Both work from the console without the leading slash.

`nether` must be run by a player standing at a safe Nether arrival point. It saves that position without changing personal respawn points. See [server configuration](../server/configuration.md).
