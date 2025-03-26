from src.math_operations import suma, resta, multiplicacion, division

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 4) == -4

def test_multiplicacion():
    assert multiplicacion(4, 3) == 12
    assert multiplicacion(7, 0) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(9, 3) == 3
import pytest
from src.math_operations import suma, resta, multiplicacion, division

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(10, 10) == 0

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(0, 10) == 0

def test_division():
    assert division(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        division(5, 0)


