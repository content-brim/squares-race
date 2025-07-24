import pygame as pg

from solids import Solid


class Square(Solid):
    is_dynamic = True

    def __init__(self, position, color):
        size = (40, 40)
        super().__init__(position, size, color)

    def resolve_overlap(self, other, overlap):
        if overlap.width < overlap.height:
            axis = pg.Vector2(1, 0)
            sign = -1 if self.rect.centerx < other.rect.centerx else 1
            magnitude = overlap.width
        else:
            axis = pg.Vector2(0, 1)
            sign = -1 if self.rect.centery < other.rect.centery else 1
            magnitude = overlap.height

        move_vector = sign * axis * magnitude
        self.rect.move_ip(move_vector)

    def resolve_static_collision(self, other):
        super().resolve_static_collision(other)
        overlap = self.get_overlap(other)
        if not overlap:
            return
        self.resolve_overlap(other, overlap)

        if overlap.width < overlap.height:
            self.velocity.x *= -1
        else:
            self.velocity.y *= -1

    def resolve_dynamic_collision(self, other):
        super().resolve_dynamic_collision(other)
        overlap = self.get_overlap(other)
        if not overlap:
            return

        self.resolve_overlap(other, overlap)

        direction = pg.Vector2(self.rect.center) - pg.Vector2(other.rect.center)
        normal = direction.normalize()

        velocity_normal1 = self.velocity.dot(normal)
        velocity_normal2 = other.velocity.dot(normal)

        self.velocity += (velocity_normal2 - velocity_normal1) * normal
        other.velocity += (velocity_normal1 - velocity_normal2) * normal
