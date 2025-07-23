from solids import StaticSolid
import colors


class Wall(StaticSolid):
    def __init__(self, position, size):
        super().__init__(position, size, colors.BLACK)
