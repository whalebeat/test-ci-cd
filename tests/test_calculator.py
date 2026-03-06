import pytest

from src.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(3, 5) == 8


def test_subtract(calc):
    assert calc.subtract(10, 4) == 6


def test_multiply(calc):
    assert calc.multiply(4, 5) == 20


def test_divide(calc):
    assert calc.divide(10, 2) == 5
