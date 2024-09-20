from src.math_operations import add,subtract

def test_add():
    assert add(1,2)==3
    assert add(3,4)==7
    assert add(-1,1)==0

def test_subtract():
    assert subtract(1,2)== -1
    assert subtract(3,4)== -1
    assert subtract(-1,1)== -2
