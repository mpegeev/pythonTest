from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle


def test_area():
    t1 = Circle(3)
    t2 = Rectangle(3, 4)
    t3 = Square(3)
    t4 = Triangle(3, 4, 5)

    assert t1.add_area(t2) == t1.area + t2.area
    assert t1.add_area(t3) == t1.area + t3.area
    assert t1.add_area(t4) == t1.area + t4.area
    
    assert t2.add_area(t3) == t2.area + t3.area
    assert t2.add_area(t4) == t2.area + t4.area
    assert t2.add_area(t1) == t2.area + t1.area

    assert t3.add_area(t4) == t3.area + t4.area
    assert t3.add_area(t1) == t3.area + t1.area
    assert t3.add_area(t2) == t3.area + t2.area

    assert t4.add_area(t1) == t4.area + t1.area
    assert t4.add_area(t2) == t4.area + t2.area
    assert t4.add_area(t3) == t4.area + t3.area
