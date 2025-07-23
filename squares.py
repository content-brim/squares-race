from solids import DynamicSolid


class Square(DynamicSolid):
    def __init__(self, position, color):
        size = (40, 40)
        super().__init__(position, size, color)
