# Configuration defaults

Bundled defaults for **Beliefs 0.1.0-SNAPSHOT**. Your server’s file may differ.

Edit `plugins/Beliefs/config.yml` and restart. For guidance, see [Configure your server](../server/configuration.md).

Existing configuration files are retained on upgrades. These tables are generated from the plugin’s default resources.

## Examples

| Setting | Default |
| --- | --- |
| `examples.enabled` | `true` |

## Agnostic

| Setting | Default |
| --- | --- |
| `agnostic.head-texture` | `"http://textures.minecraft.net/texture/910e92e0258d70ec132b69664f5f7f292bfec7e0f727685a1d7970d12249"` |

## Marriage ring

| Setting | Default |
| --- | --- |
| `marriage-ring.recipe.enabled` | `true` |
| `marriage-ring.recipe.shape` | `["GDG", "G G", "GGG"]` |
| `marriage-ring.recipe.ingredients.G` | `"GOLD_INGOT"` |
| `marriage-ring.recipe.ingredients.D` | `"DIAMOND"` |

## Sacred items

| Setting | Default |
| --- | --- |
| `sacred-items.cooldown-seconds` | `60` |

## Limits

| Setting | Default |
| --- | --- |
| `limits.marriage-members` | `8` |
| `limits.teaching-weight` | `20` |
| `limits.ceremony-distance` | `32` |
| `limits.consent-seconds` | `300` |

## Judgment

| Setting | Default |
| --- | --- |
| `judgment.blessing-threshold` | `20` |
| `judgment.penance-threshold` | `-20` |
| `judgment.nether-threshold` | `-100` |
| `judgment.serious-transgressions` | `5` |
| `judgment.blessing-seconds` | `120` |
| `judgment.penance-seconds` | `60` |

## Afterlife

| Setting | Default |
| --- | --- |
| `afterlife.nether.world` | `""` |
| `afterlife.nether.x` | `0.5` |
| `afterlife.nether.y` | `64` |
| `afterlife.nether.z` | `0.5` |
| `afterlife.nether.yaw` | `0` |
| `afterlife.nether.pitch` | `0` |

## Community

| Setting | Default |
| --- | --- |
| `community.timezone` | `"Europe/London"` |

## Worship

| Setting | Default |
| --- | --- |
| `worship.allowed-outcomes` | `["PRAYER", "SERVICE", "BLESSING", "FORGIVE", "HOLY_WATER", "RAIN", "CLEAR", "THUNDER", "CALM"]` |
| `worship.max-temple-radius` | `64` |
| `worship.max-session-seconds` | `3600` |
| `worship.minimum-ritual-seconds` | `5` |
| `worship.minimum-weather-participants` | `3` |
| `worship.weather-cooldown-seconds` | `1800` |
| `worship.allowed-weather-worlds` | `[]` |
| `worship.fasting-cooldown-seconds` | `1800` |
| `worship.fast-max-minutes` | `1440` |
| `worship.blessing-seconds` | `120` |
| `worship.holy-water-amount` | `1` |
| `worship.prayer.sneak-hold-seconds` | `3` |
| `worship.directional-prayer.angle-degrees` | `20` |
| `worship.directional-prayer.hold-seconds` | `10` |
| `worship.directional-prayer.bonus-cooldown-seconds` | `300` |
| `worship.directional-prayer.effect` | `"SPEED"` |
| `worship.directional-prayer.effect-seconds` | `30` |

## Full default file

```yaml
examples:
  enabled: true
agnostic:
  head-texture: http://textures.minecraft.net/texture/910e92e0258d70ec132b69664f5f7f292bfec7e0f727685a1d7970d12249
marriage-ring:
  recipe:
    enabled: true
    shape:
    - GDG
    - G G
    - GGG
    ingredients:
      G: GOLD_INGOT
      D: DIAMOND
sacred-items:
  cooldown-seconds: 60
limits:
  marriage-members: 8
  teaching-weight: 20
  ceremony-distance: 32
  consent-seconds: 300
judgment:
  blessing-threshold: 20
  penance-threshold: -20
  nether-threshold: -100
  serious-transgressions: 5
  blessing-seconds: 120
  penance-seconds: 60
afterlife:
  nether:
    world: ''
    x: 0.5
    y: 64
    z: 0.5
    yaw: 0
    pitch: 0
community:
  timezone: Europe/London
worship:
  allowed-outcomes:
  - PRAYER
  - SERVICE
  - BLESSING
  - FORGIVE
  - HOLY_WATER
  - RAIN
  - CLEAR
  - THUNDER
  - CALM
  max-temple-radius: 64
  max-session-seconds: 3600
  minimum-ritual-seconds: 5
  minimum-weather-participants: 3
  weather-cooldown-seconds: 1800
  allowed-weather-worlds: []
  fasting-cooldown-seconds: 1800
  fast-max-minutes: 1440
  blessing-seconds: 120
  holy-water-amount: 1
  prayer:
    sneak-hold-seconds: 3
  directional-prayer:
    angle-degrees: 20
    hold-seconds: 10
    bonus-cooldown-seconds: 300
    effect: SPEED
    effect-seconds: 30
```
