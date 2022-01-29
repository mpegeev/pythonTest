class Figure:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def area(self):
        return 0

    @property
    def perimeter(self):
        return 0

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Can sum only objects of class Figure")
        return self.area + figure.area

    def __str__(self) -> str:
        return "{0}, area: {1}, perimiter: {2}".format(
            self.name, self.area, self.perimeter
        )
