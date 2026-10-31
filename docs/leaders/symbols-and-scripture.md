# Choose a symbol and write scripture

As founder, open `/faith settings` → **Identity**. Category changes stay in a draft until **Save**, which applies them together.

## Choose a symbol

1. Open **Symbol**.
2. Select a head or item from the gallery. Use **Previous**, **Next** or **Search** to find it.
3. Check the selected preview and the green checkbox after its name.
4. Choose **Save**.

The [catalogue](../reference/symbols.md) includes 22 heads and item symbols; your server may add more. Choosing a symbol does not set food rules, teachings or ceremonies.

<!-- Screenshot: Three-column symbol gallery with a selected symbol, navigation row and Save. -->

??? tip "Use a custom head or held item"

    Your main-hand item appears as an item-symbol choice. Choosing it clears the draft's head texture.

    For another head, choose **Custom head**, paste its `textures.minecraft.net` skin URL or texture value, then **Use head** and **Save**. **Back** keeps the typed text without applying it.

## Write scripture

1. Open the **Scripture** category.
2. Set **Book title (optional)**, such as “The River Book”.
3. Write your stories, principles or teachings in **Sacred text: stories and teachings**.
4. Choose **Save**.

Members read your text through **/faith → Scripture**. Gameplay rewards and restrictions belong in [Teachings and food rules](teachings-and-food.md).

Book titles allow 80 characters; scripture allows multiple lines and 6,000 characters. A blank title uses the faith's name followed by “teachings”. Title changes apply only to newly collected books.

## Let members collect the sacred book

Members choose **/faith → Scripture → Get sacred item**. The book uses your saved title and faith symbol. Right-clicking it opens its faith; using it on another player opens that person's information.

Collection has a 60-second default cooldown across all faiths, including after reconnects and restarts. A full inventory gives no book and uses no cooldown.

??? note "For server owners: catalogue updates"

    Preset heads load from `plugins/Beliefs/symbols.yml` at startup. Replacing the plugin JAR does not merge new entries into an existing file. Preserve custom entries when updating it, then restart.

    Agnostic's protected symbol uses the separate `agnostic.head-texture` setting. See [updates and backups](../server/updating.md).
