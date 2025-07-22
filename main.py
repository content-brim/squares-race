import pygame as pg

from squares import Square
from walls import Wall


TITLE = "Squares' Race"
FRAMERATE = 24
SCREEN_SIZE = (540, 860)
WHITE_COLOR = pg.Color(255, 255, 255)


squares_group = pg.sprite.Group(
    Square((150, 660), pg.Color(255, 0, 0)),
    Square((250, 660), pg.Color(0, 255, 0)),
    Square((350, 660), pg.Color(0, 0, 255)),
)

walls_group = pg.sprite.Group(
    Wall((0, 810), pg.Vector2(540, 50)),
    Wall((0, 0), pg.Vector2(540, 50)),
    Wall((0, 0), pg.Vector2(50, 860)),
    Wall((490, 0), pg.Vector2(50, 860)),
)
all_groups = walls_group, squares_group

if __name__ == "__main__":
    pg.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption(TITLE)

    clock = pg.time.Clock()

    is_running = True
    for square in squares_group:
        square.push(45)

    while is_running:
        delta = clock.tick(FRAMERATE) / 1_000
        screen.fill(WHITE_COLOR)
        for group in all_groups:
            group.update(delta, walls_group)
            group.draw(screen)

        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False

    pg.quit()
