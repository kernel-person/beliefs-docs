"""Native-texture crafting diagram; head projection reused from Cosmonautics' wiki renderer."""
import hashlib
from io import BytesIO
import json
import math
from pathlib import Path
from PIL import Image

ASSETS = Path(__file__).resolve().parent / 'recipe-assets'
SCALE = 3
SIZE = (176, 82)


def texture(name):
    return Image.open(ASSETS / name).convert('RGBA')


def validate_assets():
    manifest = json.loads((ASSETS / 'manifest.json').read_text())
    recorded = {entry['file'] for entry in manifest['assets']}
    actual = {p.name for p in ASSETS.iterdir() if p.suffix in ('.png', '.json') and p.name != 'manifest.json'}
    if recorded != actual:
        raise ValueError('Recipe asset inventory differs from its provenance manifest.')
    for entry in manifest['assets']:
        if hashlib.sha256((ASSETS / entry['file']).read_bytes()).hexdigest() != entry['sha256']:
            raise ValueError('Changed recipe source asset: ' + entry['file'])
    for name in ('gold_ingot.png', 'diamond.png'):
        if texture(name).size != (16, 16):
            raise ValueError('Expected the native 16-pixel item texture: ' + name)
    if texture('marriage-ring-skin.png').size not in ((64, 32), (64, 64)):
        raise ValueError('Expected a native player-head skin.')


def draw_text(image, value, x, y):
    atlas = texture('ascii.png')
    for char in value:
        n = ord(char)
        glyph = atlas.crop(((n % 16) * 8, (n // 16) * 8, (n % 16 + 1) * 8, (n // 16 + 1) * 8))
        bounds = glyph.getchannel('A').getbbox()
        ink = Image.new('RGBA', glyph.size, (64, 64, 64, 255))
        ink.putalpha(glyph.getchannel('A'))
        image.alpha_composite(ink.resize((8 * SCALE, 8 * SCALE), Image.Resampling.NEAREST), (x * SCALE, y * SCALE))
        x += (bounds[2] if bounds else 3) + 1

def rotate(point, angles):
    """Minecraft ItemTransform.rotationXYZ: R_x * R_y * R_z."""
    x, y, z = point
    rx, ry, rz = map(math.radians, angles)
    x, y = x * math.cos(rz) - y * math.sin(rz), x * math.sin(rz) + y * math.cos(rz)
    x, z = x * math.cos(ry) + z * math.sin(ry), -x * math.sin(ry) + z * math.cos(ry)
    y, z = y * math.cos(rx) - z * math.sin(rx), y * math.sin(rx) + z * math.cos(rx)
    return x, y, z

def face(image, bitmap, vertices, brightness):
    """Nearest-texel orthographic rasterization of one planar cuboid face."""
    origin, right, _, bottom = vertices
    ax, ay = right[0] - origin[0], right[1] - origin[1]
    bx, by = bottom[0] - origin[0], bottom[1] - origin[1]
    determinant = ax * by - ay * bx
    layer = Image.new('RGBA', image.size)
    for y in range(max(0, math.floor(min(v[1] for v in vertices))),
                   min(image.height, math.ceil(max(v[1] for v in vertices)))):
        for x in range(max(0, math.floor(min(v[0] for v in vertices))),
                       min(image.width, math.ceil(max(v[0] for v in vertices)))):
            dx, dy = x + .5 - origin[0], y + .5 - origin[1]
            u = (dx * by - dy * bx) / determinant
            v = (ax * dy - ay * dx) / determinant
            if 0 <= u < 1 and 0 <= v < 1:
                r, g, b, a = bitmap.getpixel((int(u * bitmap.width), int(v * bitmap.height)))
                layer.putpixel((x, y), (round(r * brightness), round(g * brightness),
                                        round(b * brightness), a))
    image.alpha_composite(layer)

def head_faces(half):
    # Converted from the native SkullModel's -4..4, -8..0, -4..4 box,
    # after the player_head special model's 180-degree X rotation.
    h = half
    return {
        'top': [(-h, h, -h), (h, h, -h), (h, h, h), (-h, h, h)],
        'right': [(-h, h, -h), (-h, h, h), (-h, -h, h), (-h, -h, -h)],
        'front': [(-h, h, h), (h, h, h), (h, -h, h), (-h, -h, h)],
    }

def projected(vertices, display, center_offset=(0, 0, 0)):
    result = []
    for vertex in vertices:
        scaled = tuple((v + offset) * scale for v, offset, scale in
                       zip(vertex, center_offset, display['scale']))
        x, y, z = rotate(scaled, display['rotation'])
        tx, ty, tz = display['translation']
        result.append(((8 + x + tx) * SCALE, (8 - y - ty) * SCALE, z + tz))
    return result

def ring_head():
    skin = texture('marriage-ring-skin.png')
    display = json.loads((ASSETS / 'template_skull.json').read_text())['display']['gui']
    icon = Image.new('RGBA', (16 * SCALE, 16 * SCALE))
    crops = {'top': (8, 0, 16, 8), 'right': (0, 8, 8, 16), 'front': (8, 8, 16, 16)}
    for half, uv_offset in [(4, 0), (4.25, 32)]:
        for name, vertices in head_faces(half).items():
            box = crops[name]
            box = (box[0] + uv_offset, box[1], box[2] + uv_offset, box[3])
            face(icon, skin.crop(box), projected(vertices, display, (0, -4, 0)),
                 {'top': 1.0, 'right': .80, 'front': .92}[name])
    return icon


def render_recipe(configuration):
    validate_assets()
    recipe = configuration['marriage-ring']['recipe']
    rows = recipe['shape']
    if len(rows) != 3 or any(len(row) != 3 for row in rows):
        raise ValueError('Recipe diagram requires the configured three-by-three grid.')
    native = texture('crafting_table.png')
    panel = native.crop((0, 0, SIZE[0], SIZE[1]))
    panel.paste(native.crop((0, 162, SIZE[0], 166)), (0, SIZE[1] - 4))
    image = panel.resize((SIZE[0] * SCALE, SIZE[1] * SCALE), Image.Resampling.NEAREST)
    draw_text(image, 'Crafting', 28, 6)
    icons = {'GOLD_INGOT': 'gold_ingot.png', 'DIAMOND': 'diamond.png'}
    for row_index, row in enumerate(rows):
        for col_index, token in enumerate(row):
            if token == ' ':
                continue
            material = recipe['ingredients'][token]
            if material not in icons:
                raise ValueError('Bundle the real Minecraft texture before rendering: ' + material)
            icon = texture(icons[material]).resize((16 * SCALE, 16 * SCALE), Image.Resampling.NEAREST)
            image.alpha_composite(icon, ((30 + col_index * 18) * SCALE, (17 + row_index * 18) * SCALE))
    image.alpha_composite(ring_head(), (124 * SCALE, 35 * SCALE))
    result = BytesIO()
    image.save(result, format='PNG')
    return result.getvalue()
