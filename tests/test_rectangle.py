import pytest
from src.Rectangle import Rectangle


def test_rectangle_empty_side1():
    t = Rectangle(None, 3)
    assert t == None


def test_rectangle_empty_side2():
    t = Rectangle(3, None)
    assert t == None

    
def test_rectangle_zero_side1():
    t = Rectangle(None, 0)
    assert t == None


def test_rectangle_zero_side2():
    t = Rectangle(0, None)
    assert t == None

    
def test_rectangle_incorrect_type_side1():
    t = Rectangle("a", 3)
    assert t == None


def test_rectangle_incorrect_type_side2():
    t = Rectangle(3, "a")
    assert t == None


def test_rectangle_float_type_side1():
    t = Rectangle(3.1, 3)
    assert t.perimeter == 12.2


def test_rectangle_float_type_side2():
    t = Rectangle(3, 3.1)
    assert t.perimeter == 12.2

    
def test_rectangle_zero_sides():
    t = Rectangle(0, 0)
    assert t == None


def test_rectangle_negative_sides():
    t = Rectangle(-1, -3)
    assert t == None


def test_rectangle_perimeter():
    t = Rectangle(3, 4)
    assert t.perimeter == 14


def test_rectangle_area():
    t = Rectangle(3, 4)
    assert t.area == 12


def test_rectangle_add_area():
    t1 = Rectangle(3, 4)
    t2 = Rectangle(5, 6)
    assert t1.add_area(t2) == t1.area + t2.area
