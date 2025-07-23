import pygame as pg

from squares import Square
from walls import Wall
import colors


TITLE = "Squares' Race"
FRAMERATE = 24
SCREEN_SIZE = (540, 860)


walls = pg.sprite.Group(
    Wall((0, 810), pg.Vector2(540, 50)),
    Wall((0, 0), pg.Vector2(540, 50)),
    Wall((0, 0), pg.Vector2(50, 860)),
    Wall((490, 0), pg.Vector2(50, 860)),
)
squares = pg.sprite.Group(
    Square((150, 660), colors.RED),
    Square((250, 660), colors.GREEN),
    Square((350, 660), colors.BLUE),
)
all_sprites = pg.sprite.Group(*walls, *squares)


if __name__ == "__main__":
    pg.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption(TITLE)

    clock = pg.time.Clock()

    is_running = True
    while is_running:
        delta = clock.tick(FRAMERATE) / 1_000
        screen.fill(colors.WHITE)
        all_sprites.update(delta)
        all_sprites.draw(screen)
        for obj in squares:
            obj.check_collisions(all_sprites)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False

        pg.display.flip()

    pg.quit()
