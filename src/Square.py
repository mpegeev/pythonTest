import numbers
from .Rectangle import Rectangle
from .Figure import Figure


class Square(Rectangle):
    def __new__(cls, side):
        return super().__new__(cls, side, side)

    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self._name = "Square"
