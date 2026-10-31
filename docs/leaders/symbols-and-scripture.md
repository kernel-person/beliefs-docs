# Choose a symbol and write scripture

**Start here:** `/faith settings → Identity`. The founder edits these settings. Moving between categories keeps a draft; **Save** applies your changes together.

## Choose a symbol

1. Open **Symbol**.
2. Select a head or item from the gallery. Use **Previous**, **Next** or **Search** to find it.
3. Check the selected preview and the green checkbox after its name.
4. Choose **Save**.

The bundled [catalogue](../reference/symbols.md) has 22 heads, alongside item symbols. Your server may add its own. A symbol is artwork: choosing it does not set food rules, teachings or ceremonies.

<!-- Screenshot: Three-column symbol gallery with a selected symbol, navigation row and Save. -->

??? tip "Use a custom head or held item"

    The item you hold in your main hand is available as an item-symbol choice. Choosing an item clears the active head texture in your draft.

    For another head, choose **Custom head**, paste its `textures.minecraft.net` skin URL or texture value, and select **Use head**. You still need **Save**. **Back** keeps the typed text for later but does not apply it.

## Write scripture

1. Open the **Scripture** category.
2. Set **Book title (optional)**, such as “The River Book”.
3. Write your stories, principles or teachings in **Sacred text: stories and teachings**.
4. Choose **Save**.

Members read this through **/faith → Scripture**. Scripture explains the faith in your own words; use [Teachings and food rules](teachings-and-food.md) to change gameplay rewards or restrictions.

The book title allows 80 characters; scripture allows multiple lines and up to 6,000 characters. A blank title uses the faith's name followed by “teachings”. Changing the title affects newly collected books, not books already in inventories.

## Let members collect the sacred book

Members choose **/faith → Scripture → Get sacred item**. The book uses your saved title and faith symbol. Right-clicking it opens its faith; using it on another player opens that person's information.

The default collection cooldown is 60 seconds, shared across faiths and retained after reconnects and restarts. A full inventory grants no item and consumes no cooldown.

??? note "For server owners: catalogue updates"

    Preset heads load from `plugins/Beliefs/symbols.yml` at startup. Replacing the plugin JAR does not merge new entries into an existing file. Preserve custom entries when updating it, then restart.

    Agnostic's protected symbol uses the separate `agnostic.head-texture` setting. See [updates and backups](../server/updating.md).
