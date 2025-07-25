from solids import Solid
from surfaces import ColorSurfaceMixin
import colors


class Wall(Solid, ColorSurfaceMixin):
    is_dynamic = False

    def __init__(self, position, size):
        super().__init__(position, image_kwargs={"size": size, "color": colors.BLACK})
