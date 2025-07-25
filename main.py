import pygame as pg

from squares import Square
from walls import Wall
from finishes import Finish
import colors


TITLE = "Squares' Race"
FRAMERATE = 60
SCREEN_SIZE = (540, 860)

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()


walls = (
    Wall((270, 910), (540, 100)),
    Wall((270, -50), (540, 100)),
    Wall((-50, 430), (100, 860)),
    Wall((590, 430), (100, 860)),
    Wall((135, 25), (270, 50)),
    Wall((135, 430), (270, 100)),
    Wall((405, 215), (270, 100)),
    Wall((405, 645), (270, 100)),
)
interactables_group = pg.sprite.Group(
    Finish((405, 25), (270, 50)),
)
squares = (
    Square((150, 800), colors.RED),
    Square((200, 800), colors.YELLOW),
    Square((250, 800), colors.GREEN),
    Square((300, 800), colors.CYAN),
    Square((350, 800), colors.BLUE),
    Square((400, 800), colors.PINK),
)
solids_group = pg.sprite.Group(*squares, *walls)


for square in squares:
    import random

    speedx = random.uniform(-200, 200)
    speedy = random.uniform(-200, 200)
    square.velocity = pg.Vector2(speedx, speedy)

is_running = True
while is_running:
    delta = clock.tick(FRAMERATE) / 1_000.0
    screen.fill(colors.WHITE)

    for i, square in enumerate(squares, start=1):
        for wall in walls:
            if square.has_collision(wall):
                square.resolve_static_collision(wall)
        for interactable in interactables_group.sprites():
            if square.has_collision(interactable):
                interactable.interact(square)
        for other in squares[i:]:
            if square.has_collision(other):
                square.resolve_dynamic_collision(other)

    interactables_group.update(delta)
    interactables_group.draw(screen)
    solids_group.update(delta)
    solids_group.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    pg.display.flip()

pg.quit()
