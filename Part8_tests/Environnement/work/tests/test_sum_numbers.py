import pytest
import os,json

path =  os.path.join(os.path.dirname(__file__), 'data')
file =  os.path.join(path, "numbers.json")

with open(file, 'r') as file:
    data = json.load(file)

prepare = []
for d in data :
    prepare.append( tuple( d.values() ) )
    
@pytest.mark.parametrize("input, expected", prepare)
def test_sum_list(input, expected):
    s = sum(input)
    
    assert s == expected