from src.helpers.Calculator import Calculator
import pytest

class TestCalculator:
    def test_addition(self):
        c = Calculator("5.5 + 10 + 30 + 13.7")
        assert c.sum() == 59.2

    def test_subtraction(self):
        assert 1
        
    def test_divisor(self):
        c = Calculator("5.5 + 10 + 30 + 13.7")
        with pytest.raises(ZeroDivisionError):
            c.divisor(1, 0)
