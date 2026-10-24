# Design and lead ceremonies

Founders design rituals in `/faith settings` → **Ceremonies**. Members use the faith's ordinary **Ceremonies** view to read requirements and join. A ritual can allow any member to lead or require clergy.

## Create a ritual

1. Choose **New ritual** and an example: **Simple prayer**, **Shared meal**, **Rain prayer**, **Blessing**, **Holy water**, or **Custom ritual**.
2. Enter its name and **Minimum people, leader included**.
3. Use **Change result** to choose what completion does. The preview explains the result and requirements.
4. Choose **Add step**, configure its action and amount, then select **Add step to draft**. Select an existing step to edit or reorder it.
5. Review **More settings**, then select **Save ritual**.

Choosing an example creates only a draft. **Save ritual** saves the settings and steps together. Finish or discard an open step before saving. **Back** inside a step or settings screen keeps the ritual draft; **Cancel** on the main editor discards unsaved edits.

## Choose actions and limits

Step amounts are shared group totals:

| Action | What participants do |
| --- | --- |
| **Gather** | Nearby people join the ceremony |
| **Pray** | Begin prayer, then hold sneak |
| **Offer** | Hold the selected item and choose **Offer item** |
| **Consume** | Eat or drink the selected item normally |
| **Bless** | Choose **Bless**, meeting the clergy and item requirements |

**More settings** controls minimum duration, repeat wait, clergy leadership/blessing, and registered-temple requirements. Server limits still apply: by default, rituals last at least five seconds and weather ceremonies need at least three participants. The [configuration reference](../reference/configuration.md) covers additional limits.

Blessing and forgiveness results require a **Bless** step using this faith's holy water. Check the preview before telling members what to bring.

## Lead a gathering

Save changes first, then choose **Start ceremony**. Invite participants to use **Ceremonies** → **Nearby / active** and follow the in-world guidance. See the [participant guide](../players/ceremonies.md) for completion, items, and cooldowns.

Marriage and adoption have their own consent workflows under **Families** in `/faith settings`. Use [marriage](../players/marriage.md) and [adoption](../players/adoption.md) when officiating those events.

??? note "Advanced design"

    A ritual supports up to 16 steps. The server can disable individual outcomes and restrict weather effects by world and cooldown. Scheduling a ritual as a holy day does not bypass those rules.
