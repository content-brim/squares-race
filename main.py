import pygame as pg

from squares import Square
from walls import Wall
import colors


TITLE = "Squares' Race"
FRAMERATE = 60
SCREEN_SIZE = (540, 860)


walls = (
    Wall((270, 860 + 50), pg.Vector2(540, 100)),
    Wall((270, -50), pg.Vector2(540, 100)),
    Wall((-50, 430), pg.Vector2(100, 860)),
    Wall((540 + 50, 430), pg.Vector2(100, 860)),
)
squares = (
    Square((150, 660), colors.RED),
    Square((200, 660), colors.RED),
    Square((250, 660), colors.GREEN),
    Square((300, 660), colors.GREEN),
    Square((350, 660), colors.BLUE),
    Square((400, 660), colors.BLUE),
)
solids_group = pg.sprite.Group(*squares, *walls)


if __name__ == "__main__":
    pg.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption(TITLE)

    clock = pg.time.Clock()

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
            for other in squares[i:]:
                if square.has_collision(other):
                    square.resolve_dynamic_collision(other)

        solids_group.update(delta)
        solids_group.draw(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False

        pg.display.flip()

    pg.quit()
