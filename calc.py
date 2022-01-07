def add(a, b):
    return a + b

def subtract(a, b):
    return a - b 

def multiplication(a, b):
    return a * b

def division(a, b):
    return a/b

def equal(a,b):
    return a == b

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(2, 3) == -1

def test_multiplication():
    assert multiplication(2, 3) == 6

def test_division():
    assert division(4, 2) == 2

def test_equal():
    assert equal(2, 2) == True

def test_notEqual():
    assert equal(2, 3) == False

def test_multiplicationZero():
    assert multiplication(100, 0) == 0

def test_divisionZero():
    assert division(0, 100) == 0

def test_subtractAdd():
    assert (subtract(3,4) + add(3,4)) == 6

def test_subtractAdd():
    assert (equal((subtract(3,4) + add(3,4)),6) == True


