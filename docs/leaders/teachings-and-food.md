# Set teachings and food rules

The founder controls these choices through `/faith settings`. Teachings determine how deeds affect standing. Food rules determine which foods the faith permits.

## Add a teaching

1. Open **Teachings** → **Add teaching**.
2. Choose an action, such as prayer, eating, killing, or fasting.
3. Choose its target when offered: a particular creature, food, ceremony, or completed/broken fast. Use the general option to cover matching events broadly.
4. Set the standing change and explain why the deed matters.
5. Select **Save**.

Negative values penalize standing; positive values reward it. Only negative teachings can be marked **Serious transgression**. The default server limit is −20 to +20 per teaching.

Selecting targets and moving through the editor keeps a draft. **Cancel** discards it. Open an existing teaching to edit it, or choose **Remove** and confirm removal.

New player-founded faiths include starter teachings: prayer gives +1 standing, a food violation gives −5, and killing a player gives −20 with a serious transgression. Review these defaults before inviting people.

## Choose permitted foods

Open **Food rules** and use these tabs:

| Tab | What a founder changes |
| --- | --- |
| **Foods** | Explicit bans on individual foods |
| **Ingredients** | Bans on ingredients |
| **Diets** | Dietary requirements and the listed food restrictions |
| **Rules** | Review and remove active rules |

**Food tiles apply changes immediately.** Read the tile's action before clicking. Removing an individual ban can leave the food forbidden by another rule. The food-rules name is a label; naming it “Vegetarianism” does not enable a diet.

New player-founded faiths start without food restrictions. When [optional Heirloom integration](../server/installation.md) is available, the catalogue can include its foods and ingredient information. Some dishes depend on their actual ingredients; unknown information is shown as uncertain.

??? note "Specific teachings and future deeds"

    A teaching for a specific target takes priority over the general teaching for that action. Removing a teaching changes how future deeds are evaluated. Food restrictions and the standing penalty for violating them are separate settings.

Point members to [food and fasting](../players/food.md) and [prayer](../players/prayer.md).
