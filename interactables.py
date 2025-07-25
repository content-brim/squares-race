import pygame as pg


class Interactable(pg.sprite.Sprite):
    def __init__(self, position, image_kwargs):
        super().__init__()
        self.init_image(**image_kwargs)
        self.rect = self.image.get_rect(center=position)

    def interact(self, other):
        pass
