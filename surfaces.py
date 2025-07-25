from abc import ABC, abstractmethod
from enum import Enum

import pygame as pg


class ImageMode(str, Enum):
    REPEAT = "repeat"
    RESCALE = "rescale"


class SurfaceMixin(ABC):
    @abstractmethod
    def init_image(self, size):
        pass


class ColorSurfaceMixin:
    def init_image(self, size, color):
        self.image = pg.Surface(size)
        self.image.fill(color)


class ImageSurfaceMixin:
    def init_image(self, size, image_path, mode: ImageMode):
        original_image = pg.image.load(image_path).convert_alpha()
        if mode == ImageMode.RESCALE:
            self.image = pg.transform.smoothscale(original_image)
        elif mode == ImageMode.REPEAT:
            width, height = original_image.get_size()
            self.image = pg.Surface(size, pg.SRCALPHA)
            for x in range(0, size[0], width):
                for y in range(0, size[1], height):
                    self.image.blit(original_image, (x, y))
