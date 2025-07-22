import math
from typing import Tuple
import pygame as pg
from pygame.sprite import Sprite, spritecollide


class Square(Sprite):
    size = (50, 50)
    speed = 70.0

    def __init__(self, position: Tuple[int, int], color: pg.Color):
        super().__init__()
        self.image = pg.Surface(self.size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def push(self, angle: float):
        self.angle = angle
        self.vector = pg.Vector2(
            math.cos(math.radians(angle)), math.sin(math.radians(angle))
        )

    def update(self, delta: int, group: pg.sprite.Group):
        self.rect.center += self.vector * self.speed * delta
        collisions = spritecollide(self, group, False)
        angle = len(collisions) * 90
        self.push(self.angle + angle)
