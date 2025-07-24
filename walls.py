from solids import Solid
import colors


class Wall(Solid):
    is_dynamic = False

    def __init__(self, position, size):
        super().__init__(position, size, colors.BLACK)
