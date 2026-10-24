# Choose a symbol and write scripture

The founder edits both through `/faith settings` → **Identity**. Changes remain in the settings draft until **Save**.

## Choose a symbol

1. Open the **Symbol** category.
2. Select a head from the catalogue or an item symbol. The picker includes common items and the item you hold in your main hand.
3. Check the **Selected** preview and choose **Save**.

The bundled [symbol catalogue](../reference/symbols.md) contains 22 heads. Your server's choices may differ. Choosing an item symbol clears the draft's custom head choice.

For another head, choose **Custom head**, paste a `textures.minecraft.net` skin URL or its texture value, and select **Use head**. This updates the draft; you still need **Save**. **Back** from the custom-head form does not apply the typed head.

## Write scripture

Open **Scripture** within the same settings editor. Enter stories, principles, or teachings in **Sacred text: stories and teachings**, then select **Save**. The text supports multiple lines and up to 6,000 characters.

Members and visitors read it from the faith's **Scripture** page. A founder's scripture is descriptive text: change gameplay effects separately under [Teachings and food rules](teachings-and-food.md).

## Give members a way back

Members can open **Scripture** → **Get sacred item**. Right-clicking the item opens its faith; using it on a player inspects them. It uses the faith's head texture when one is configured, otherwise a book.

The default collection wait is 60 seconds, shared across faiths and preserved through reconnects and restarts. See [configuration](../reference/configuration.md) if the server uses a different wait.

??? note "For server owners: catalogue updates"

    Beliefs loads `plugins/Beliefs/symbols.yml` at startup and creates it only when absent. Updating the plugin does not merge new bundled symbols into an existing file; review catalogue changes and restart after editing it.

    Agnostic's protected symbol is configured separately with `agnostic.head-texture` in `config.yml`. It is not a normal founder setting. See [installation and updates](../server/installation.md).
