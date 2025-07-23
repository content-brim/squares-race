from typing import Tuple
import pygame as pg
from pygame.sprite import Sprite

import colors


class Wall(Sprite):
    color = colors.BLACK

    def __init__(self, position: Tuple[int, int], size: pg.Vector2):
        super().__init__()
        self.image = pg.Surface(size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
