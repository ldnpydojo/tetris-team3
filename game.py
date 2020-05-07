import wasabi2d as w2d
from wasabi2d.keyboard import keys
from model import Piece, ALL_PIECES, TetrisBoard
from random import choice


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


b = TetrisBoard((10, 20))
active_piece_sprites = []
active_piece = None


COLOURS = [
    'red',
    'green',
    'blue',
    'yellow',
]


def create_piece():
    global active_piece
    type = choice(ALL_PIECES)
    active_piece = Piece("*", type, (4, 0), b)
    active_piece_sprites.clear()
    colour = choice(COLOURS)
    for p in active_piece:
        sprite = scene.layers[1].add_sprite(
            "tile",
            pos=grid_to_screen(*p),
            color=colour,
            scale=0.75
        )
        active_piece_sprites.append(sprite)


def update_active_piece():
    """Make the sprites for the active piece reflect their grid coordinates."""
    for sprite, pos in zip(active_piece_sprites, active_piece):
        w2d.animate(
            sprite,
            duration=0.1,
            pos=grid_to_screen(*pos)
        )


def drop_tick():
    if active_piece.can_drop():
        active_piece.drop()
        update_active_piece()
    else:
        for point in active_piece:
            b[point] = True
        create_piece()


w2d.clock.schedule_interval(drop_tick, 1)


@w2d.event
def on_key_down(key):
    updated = False
    if key == keys.Z:
        active_piece.rotate_left()
        updated = True
    elif key == keys.X:
        active_piece.rotate_right()
        updated = True
    if key == keys.LEFT and active_piece.can_go_left():
        active_piece.move_left()
        updated = True
    elif key == keys.RIGHT and active_piece.can_go_right():
        active_piece.move_right()
        updated = True
    elif key == key.DOWN:
        drop_tick()
        updated = True
    if updated:
        update_active_piece()


create_piece()
w2d.run()
