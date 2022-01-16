from cmath import sqrt
import numbers
from .Figure import Figure


class Triangle(Figure):
    def __new__(cls, side1, side2, side3):
        if side1 == None or side2 == None or side3 == None:
            return None

        if not isinstance(side1, numbers.Number) or not isinstance(side2, numbers.Number) or not isinstance(side3, numbers.Number):
            return None
            
        if side1 + side2 <= side3 or side2 + side3 <= side1 or side3 + side1 <= side2:
            return None

        return super().__new__(cls)

    def __init__(self, side1, side2, side3):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    @property
    def area(self):
        d = self.perimeter / 2
        return sqrt(d * (d - self.side1) * (d - self.side2) * (d - self.side3))
