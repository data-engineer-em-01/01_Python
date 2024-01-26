import pytest 
from src.helpers.utils import reverse
"""
input et expected sont les valeurs du tuple respectivement la première et deuxième valeur de chaque tuple.
ic vous avez deux tests ('abc', 'cba'), ('bonjour', 'ruojnob')
"""
@pytest.mark.parametrize("input, expected", [('abc', 'cba'), ('bonjour', 'ruojnob')])
def test_should_reverse_string(input, expected):
    assert reverse(input) == expected
    
    

