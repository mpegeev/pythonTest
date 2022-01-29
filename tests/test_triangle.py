import pytest
from multiprocessing.sharedctypes import Value
from src.Triangle import Triangle


def test_triangle_empty_side1():
    t = Triangle(None, 3, 3)
    assert t == None


def test_triangle_empty_side2():
    t = Triangle(3, None, 3)
    assert t == None


def test_triangle_empty_side3():
    t = Triangle(3, 3, None)
    assert t == None


def test_triangle_zero_side1():
    t = Triangle(0, 3, 3)
    assert t == None


def test_triangle_zero_side2():
    t = Triangle(3, 0, 3)
    assert t == None


def test_triangle_zero_side3():
    t = Triangle(3, 3, 0)
    assert t == None


def test_triangle_incorrect_type_side1():
    t = Triangle("a", 3, 3)
    assert t == None


def test_triangle_incorrect_type_side2():
    t = Triangle(3, "a", 3)
    assert t == None


def test_triangle_incorrect_type_side3():
    t = Triangle(3, 3, "a")
    assert t == None


def test_triangle_float_type_side1():
    t = Triangle(3.1, 3, 3)
    assert t.perimeter == 9.1


def test_triangle_float_type_side2():
    t = Triangle(3, 3.1, 3)
    assert t.perimeter == 9.1


def test_triangle_float_type_side3():
    t = Triangle(3, 3, 3.1)
    assert t.perimeter == 9.1


def test_triangle_zero_sides():
    t = Triangle(0, 0, 0)
    assert t == None


def test_triangle_negative_sides():
    t = Triangle(-1, -1, -3)
    assert t == None


def test_triangle_short_side1():
    t = Triangle(4, 2, 2)
    assert t == None


def test_triangle_short_side2():
    t = Triangle(2, 4, 2)
    assert t == None


def test_triangle_short_side3():
    t = Triangle(2, 2, 4)
    assert t == None


def test_triangle_long_sides():
    t = Triangle(4294967295, 4294967295, 4294967295)
    assert t.perimeter == 4294967295 * 3


def test_triangle_perimeter():
    t = Triangle(3, 4, 5)
    assert t.perimeter == 12


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert t.area == 6


def test_triangle_add_area():
    t1 = Triangle(3, 4, 5)
    t2 = Triangle(6, 7, 8)
    assert t1.add_area(t2) == t1.area + t2.area


def test_triangle_add_area_none():
    t1 = Triangle(3, 4, 5)
    t2 = Triangle(4, 2, 2)
    with pytest.raises(ValueError):
        sum = t1.add_area(t2)
