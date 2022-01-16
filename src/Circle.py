from cmath import pi
import numbers
from .Figure import Figure


class Circle(Figure):
    def __new__(cls, radius):
        if radius == None:
            return None

        if not isinstance(radius, numbers.Number):
            return None

        if radius <= 0:
            return None

        return super().__new__(cls)

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius * self.radius

    @property
    def perimeter(self):
        return 2 * pi * self.radius
