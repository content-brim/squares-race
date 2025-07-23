import pygame as pg
import math


def get_overlap(a, b):
    overlap = a.rect.clip(b.rect)
    if overlap.width > 0 and overlap.height > 0:
        return overlap


class StaticSolid(pg.sprite.Sprite):
    def __init__(self, position, size, color, *groups):
        super().__init__(*groups)
        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=position)
        self.velocity = 0.0


class DynamicSolid(StaticSolid):
    def __init__(self, position, size, color, *groups):
        super().__init__(position, size, color, *groups)
        self.vector = pg.Vector2(0, 0)

    def update(self, delta):
        if self.velocity > 0:
            self.rect.center += self.vector * self.velocity * delta

    def collide(self, other, is_handled=False):
        overlap = get_overlap(self, other)
        if not overlap:
            return

        if hasattr(other, "collide") and not is_handled:
            other.collide(self, is_handled=True)

        center_delta = pg.Vector2(self.rect.center) - pg.Vector2(other.rect.center)

        if overlap.width < overlap.height:
            normal = pg.Vector2(1, 0) if center_delta.x > 0 else pg.Vector2(-1, 0)
            self.rect.move_ip(normal * overlap.width)
        else:
            normal = pg.Vector2(0, 1) if center_delta.y > 0 else pg.Vector2(0, -1)
            self.rect.move_ip(normal * overlap.height)

        self.vector = (self.vector - 2 * self.vector.dot(normal) * normal).normalize()
