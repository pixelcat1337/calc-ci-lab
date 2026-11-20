import pytest

from calc import add, divide, multiply, power, subtract, to_roman


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 4) == 3


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_power():
    assert power(2, 3) == 8.0
    assert power(2, -1) == 0.5
    with pytest.raises(TypeError):
        power(2, 1.5)


def test_to_roman_valid():
    assert to_roman(1) == "I"
    assert to_roman(4) == "IV"
    assert to_roman(9) == "IX"
    assert to_roman(1994) == "MCMXCIV"
    assert to_roman(3999) == "MMMCMXCIX"


def test_to_roman_invalid():
    with pytest.raises(ValueError):
        to_roman(0)
    with pytest.raises(ValueError):
        to_roman(4000)
    with pytest.raises(ValueError):
        to_roman(True)
    with pytest.raises(ValueError):
        to_roman("1994")
