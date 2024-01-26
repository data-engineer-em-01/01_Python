import pytest

def test_exception_handling():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0