import pytest
import cmath
from src.Circle import Circle


def test_circle_empty_side():
    t = Circle(None)
    assert t == None


def test_circle_zero_side():
    t = Circle(0)
    assert t == None


def test_circle_incorrect_type_side():
    t = Circle("a")
    assert t == None


def test_circle_float_type_side():
    t = Circle(3.1)
    assert t.area / t.perimeter == 3.1 / 2


def test_circle_negative_sides():
    t = Circle(-1)
    assert t == None


def test_circle_perimeter():
    t = Circle(3)
    assert t.perimeter == 2 * cmath.pi * 3


def test_circle_area():
    t = Circle(3)
    assert t.area == cmath.pi * 3 * 3


def test_circle_add_area():
    t1 = Circle(3)
    t2 = Circle(4)
    assert t1.add_area(t2) == t1.area + t2.area
