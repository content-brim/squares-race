import pygame as pg

from interactables import Interactable


class Finish(Interactable):
    def __init__(self, position, size):
        tile = pg.image.load("assets/finish.png").convert_alpha()
        tile_width, tile_height = tile.get_size()
        image = pg.Surface(size, pg.SRCALPHA)
        for x in range(0, int(size[0]), tile_width):
            for y in range(0, int(size[1]), tile_height):
                image.blit(tile, (x, y))
        self.rect = image.get_rect(center=position)
        super().__init__(position, size, image)

    def interact(self, other):
        other.kill()
