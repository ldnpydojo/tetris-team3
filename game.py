import wasabi2d as w2d
from wasabi2d.keyboard import keys
from model import Piece, l_positions

scene = w2d.Scene()

rect = scene.layers[0].add_line(
    vertices=[(50, 50), (50, 540), (300, 540), (300, 50)],
    color='red',
)

def grid_to_screen(x, y):
    return x*24+66, y*24+66


#for j in range(0, 20):
#    for i in range(0, 10):
#        x, y = grid_to_screen(i, j)
#        scene.layers[1].add_sprite("tile", pos=(x, y), color='green', scale=0.75)


active_piece_sprites = []
active_piece = None


def create_piece():
    global active_piece
    active_piece = Piece("*", l_positions)
    for p in active_piece.position():
        sprite = scene.layers[1].add_sprite(
            "tile",
            pos=grid_to_screen(*p),
            color='green',
            scale=0.75
        )
        active_piece_sprites.append(sprite)


def update_active_piece():
    """Make the sprites for the active piece reflect their grid coordinates."""
    for sprite, pos in zip(active_piece_sprites, active_piece.position()):
        w2d.animate(
            sprite,
            duration=0.1,
            pos=grid_to_screen(*pos)
        )


@w2d.event
def on_key_down(key):
    rotated = False
    if key == keys.LEFT:
        active_piece.rotate_left()
        rotated = True
    elif key == keys.RIGHT:
        active_piece.rotate_right()
        rotated = True
    if rotated:
        update_active_piece()

create_piece()
w2d.run()
