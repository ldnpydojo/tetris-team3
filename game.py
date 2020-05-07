from wasabi2d import Scene, run

scene = Scene()

circle = scene.layers[0].add_circle(
    radius=30,
    pos=(scene.width / 2, scene.height / 2),
    color='green',
)

run()
