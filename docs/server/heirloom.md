# Use Beliefs with Heirloom

Heirloom is optional. Beliefs starts and evaluates vanilla foods without it. With a compatible Heirloom installation, it can also read custom food identities, ingredients, categories, tags and dietary facts, and show available custom foods in the food catalogue.

Install and configure Heirloom according to its own instructions, then restart the server with both plugins present. Beliefs has no integration switch or Heirloom license field in its configuration.

## What food information Beliefs uses

Beliefs prefers **Food Facts V2**, from Heirloom's API or the facts stored on the actual item. If V2 is unavailable or unsupported, it falls back to V1 and then legacy item metadata. The dish a player actually consumes matters: a catalogue preview may lack its final ingredients.

Logical food identity is separate from appearance. A custom dish using another provider's artwork keeps its food identity; a missing identity is not guessed from its icon. Preserve the namespace and case of custom IDs when creating rules.

Food results have three meanings:

| Result | Meaning |
| --- | --- |
| **Permitted** | The available facts satisfy the faith's food rules. |
| **Forbidden** | There is positive evidence of a forbidden item, ingredient, category or tag, or a required dietary property is explicitly false. |
| **Unknown** | Required evidence is missing or incomplete. Unknown alone does not record a food-rule violation. |

Incomplete facts do not erase known forbidden ingredients. Positive alcohol evidence also remains relevant even when other information is unknown. V2 unknown facts are not promoted to a certification by older positive labels.

## Check your installation

Confirm Heirloom enabled successfully, then inspect the food catalogue and a representative actual dish under the relevant faith's food rules. Check the startup log if placed-food consumption is unavailable. `/faithadmin status` reports Beliefs' faith count and family-tree adapter; it is not an integration health check.

The tested pairing is **Paper 26.2 build 71 / Java 25** with an updated **Heirloom 2.10.1 build that implements Food Facts V2**. Some earlier builds with that version lack V2. Confirm your build supports it, and try actual custom dishes and placed servings with your server's addons before opening to players.

If an older item lacks ingredient information, an **Unknown** result can be expected. See [troubleshooting](troubleshooting.md) before changing its food rules.
