# Marriage recipe assets

The recipe uses the original Minecraft Java 26.2 gold ingot, diamond, crafting-table GUI, bitmap font and player-head GUI transform. These files were extracted unchanged from the official client archive with SHA-1 `2dc72797acbc1b63fc16a11c4ac393605f453754`. The client archive is not bundled or executed.

The ring skin is downloaded unchanged from the exact texture URL in Beliefs' `MarriageRings.TEXTURE_URL`:

https://textures.minecraft.net/texture/93af4b73349e723b8654b75f905bd38995ccbb1a434d470b06279678945ecbdb

`manifest.json` records each asset's source and SHA-256. The renderer validates every checksum. Regenerating references with `--source` also verifies that the plugin still uses this ring texture. No network access or Minecraft client is needed for builds.

## Rendering

`tools/recipe_render.py` reuses the head geometry and nearest-texel projection from the Cosmonautics wiki renderer. The head has an 8×8×8 model-unit base, a second layer inflated by 0.25 units per side, the native skull GUI transform and the player-head special model's orientation. Top, front and right skin faces and overlays retain their original UVs. Fixed per-face lighting approximates the native GPU lighting; textures and geometry are not redrawn.

The crafting panel retains the original top/side borders, slot positions, result slot and arrow. Its bottom border is moved up to omit the inventory. The bitmap “Crafting” label uses the native font. Sprites are enlarged at 3× with nearest-neighbor sampling. There is one result, so Minecraft's usual no-count-label presentation is retained.

The generated PNG is 528×246 pixels. It follows the recipe rows and material mapping in the checked-in public source snapshot. An unsupported new ingredient stops generation until its genuine texture is bundled; it never falls back to invented art.

```sh
python tools/generate_reference.py
python tools/generate_reference.py --check
```

Minecraft textures, GUI and font: Mojang AB / Microsoft. Ring skin: the original hosted texture selected by the plugin author; individual skin artist not identified in the plugin source. This is documentation artwork, not a captured in-game screenshot.
