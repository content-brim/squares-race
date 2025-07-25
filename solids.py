import pygame as pg


class Solid(pg.sprite.Sprite):
    is_dynamic: bool

    def __init__(self, position, image_kwargs):
        super().__init__()
        self.init_image(**image_kwargs)
        self.rect = self.image.get_rect(center=position)
        self.velocity = pg.Vector2(0, 0)

    def update(self, delta):
        if self.velocity.length() == 0:
            return

        self.rect.move_ip(self.velocity * delta)

    def has_collision(self, other):
        return self.rect.colliderect(other.rect)

    def resolve_static_collision(self, other):
        assert not other.is_dynamic

    def resolve_dynamic_collision(self, other):
        assert other.is_dynamic

    def get_overlap(self, other):
        overlap = self.rect.clip(other.rect)
        if overlap.width > 0 and overlap.height > 0:
            return overlap
