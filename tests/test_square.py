import pytest
from src.Square import Square


def test_square_empty_side():
    t = Square(None)
    assert t == None

    
def test_square_zero_side():
    t = Square(0)
    assert t == None

    
def test_square_incorrect_type_side():
    t = Square("a")
    assert t == None


def test_square_float_type_side():
    t = Square(3.1)
    assert t.perimeter == 12.4


def test_square_negative_sides():
    t = Square(-1)
    assert t == None


def test_square_perimeter():
    t = Square(3)
    assert t.perimeter == 12


def test_square_area():
    t = Square(3)
    assert t.area == 9


def test_square_add_area():
    t1 = Square(3)
    t2 = Square(4)
    assert t1.add_area(t2) == t1.area + t2.area
