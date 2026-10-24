# Design and lead ceremonies

Founders design rituals in `/faith settings` → **Ceremonies**. Members use the faith's ordinary **Ceremonies** view to read requirements and join. A ritual can allow any member to lead or require clergy.

## Create a ritual

1. Choose **New ritual** and an example: **Simple prayer**, **Shared meal**, **Baptism**, **Rain prayer**, **Blessing**, **Holy water**, or **Custom ritual**.
2. Enter its name and **Minimum people, leader included**.
3. Use **Change result** to choose what completion does. The preview explains the result and requirements.
4. Choose **Add step**, configure its action and amount, then select **Add step to draft**. Select an existing step to edit or reorder it.
5. Review **More settings**, then select **Save ritual**.

Choosing an example creates only a draft. **Save ritual** saves the settings and steps together. Finish or discard an open step before saving. **Back** inside a step or settings screen keeps the ritual draft; **Cancel** on the main editor discards unsaved edits.

## Choose actions and limits

Prayer, offering, consumption and blessing amounts are shared group totals. **Stay underwater** uses continuous seconds for each recipient:

| Action | What participants do |
| --- | --- |
| **Gather** | Nearby people join the ceremony |
| **Pray** | Hold sneak and stand still when the step begins |
| **Offer** | Throw the selected item; punch the floating offering to cancel |
| **Consume** | Eat or drink the selected item normally |
| **Bless** | Choose **Bless**, meeting the clergy and item requirements |
| **Stay underwater** | Each joined recipient except the leader stays fully underwater for 1–300 continuous seconds |

**More settings** controls minimum duration, repeat wait, clergy leadership/blessing, and registered-temple requirements. Server limits still apply: by default, rituals last at least five seconds and weather ceremonies need at least three participants. The [configuration reference](../reference/configuration.md) covers additional limits.

Blessing and forgiveness results require a **Bless** step using this faith's holy water. Check the preview before telling members what to bring.

## Add baptism

New player-created faiths include **Baptism**. For a saved faith, open **Settings → Ceremonies → New ritual → Baptism**, then **Save ritual**. The starter requires a priest and at least one recipient, with a five-second underwater hold and no temple requirement. Select its **Stay underwater** step to change the duration.

The priest starts beside water, and recipients explicitly join through **Ceremonies → Nearby / active**. Each recipient has their own shimmering progress bar; surfacing resets an unfinished hold. The priest stays nearby while all recipients complete their holds. Joining closes after an underwater step is completed, so gather everyone first.

You can add **Stay underwater** to any custom ritual. It requires at least two people, including the leader, and does not use an item. Baptism uses the **Worship service** result and normal teaching rules; it does not change anyone's faith membership.

## Lead a gathering

Save changes first, then choose **Start ceremony**. Invite participants to use **Ceremonies** → **Nearby / active** and follow the in-world guidance. See the [participant guide](../players/ceremonies.md) for completion, items, and cooldowns.

Marriage and adoption have their own consent workflows under **Families** in `/faith settings`. Use [marriage](../players/marriage.md) and [adoption](../players/adoption.md) when officiating those events.

??? note "Advanced design"

    A ritual supports up to 16 steps. The server can disable individual outcomes and restrict weather effects by world and cooldown. Scheduling a ritual as a holy day does not bypass those rules.
