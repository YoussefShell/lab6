import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Fixture to provide a Calculator instance for tests."""
    return Calculator()


def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)


def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2


def test_multiply(calc):
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(5, 0) == 0


def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(5, 2) == 2.5
    
    with pytest.raises(ValueError, match="Division by zero"):
        calc.divide(5, 0)


def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1


def test_square_root(calc):
    assert calc.square_root(9) == 3
    assert calc.square_root(2) == pytest.approx(1.41421356)

    with pytest.raises(ValueError, match="Cannot calculate square root"):
        calc.square_root(-4)
