import pygame as pg


class Interactable(pg.sprite.Sprite):
    def __init__(self, position, size, image, *groups):
        super().__init__(*groups)
        self.image = image

    def interact(self, other):
        pass
