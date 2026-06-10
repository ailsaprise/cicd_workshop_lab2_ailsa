import pytest

from useful_package import add, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 5) == 5


def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6


def test_subtract_negative_numbers():
    assert subtract(-5, -2) == -3


def test_subtract_zero():
    assert subtract(5, 0) == 5


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 2),
        (100, 200, 300),
        (-10, 5, -5),
    ],
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 2, 3),
        (0, 0, 0),
        (-10, -5, -5),
    ],
)
def test_subtract_parametrized(a, b, expected):
    assert subtract(a, b) == expected
