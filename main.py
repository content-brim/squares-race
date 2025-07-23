import pygame as pg

from squares import Square
from walls import Wall
import colors


TITLE = "Squares' Race"
FRAMERATE = 24
SCREEN_SIZE = (540, 860)


walls = pg.sprite.Group(
    Wall((270, 835), pg.Vector2(540, 50)),
    Wall((270, 25), pg.Vector2(540, 50)),
    Wall((25, 430), pg.Vector2(50, 860)),
    Wall((515, 430), pg.Vector2(50, 860)),
)
squares = pg.sprite.Group(
    Square((150, 660), colors.RED),
    Square((200, 660), colors.RED),
    Square((250, 660), colors.GREEN),
    Square((300, 660), colors.GREEN),
    Square((350, 660), colors.BLUE),
    Square((400, 660), colors.BLUE),
)
all_sprites = pg.sprite.Group(*walls, *squares)


if __name__ == "__main__":
    pg.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption(TITLE)

    clock = pg.time.Clock()

    for square in squares:
        import random

        direction = pg.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        square.vector = direction
        square.velocity = 150

    is_running = True
    while is_running:
        delta = clock.tick(FRAMERATE) / 1_000
        screen.fill(colors.WHITE)
        all_sprites.update(delta)
        all_sprites.draw(screen)
        collisions = pg.sprite.groupcollide(squares, all_sprites, False, False)
        for square, others in collisions.items():
            for other in others:
                if square is not other:
                    square.collide(other)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False

        pg.display.flip()

    pg.quit()
