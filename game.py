from wasabi2d import Scene, run

scene = Scene()

rect = scene.layers[0].add_line(
    vertices=[(50, 50), (50, 540), (300, 540), (300, 50)],
    color='red',
)

def grid_to_screen(x, y):
    return x*24+66, y*24+66


for j in range(0, 20):
    for i in range(0, 10):
        x, y = grid_to_screen(i, j)
        scene.layers[1].add_sprite("tile", pos=(x, y), color='green', scale=0.75)


run()
