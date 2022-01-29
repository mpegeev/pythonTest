import numbers
from .Figure import Figure


class Rectangle(Figure):
    def __new__(cls, side1, side2):
        if side1 == None or side2 == None:
            return None

        if not isinstance(side1, numbers.Number) or not isinstance(side2, numbers.Number):
            return None

        if side1 <= 0 or side2 <= 0:
            return None

        return super().__new__(cls)

    def __init__(self, side1, side2):
        super().__init__("Rectangle")
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def perimeter(self):
        return 2 * (self.side1 + self.side2)
