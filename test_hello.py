from mylib.calculate import add, subtract, multiply, divide


def test_add():
    assert add(3, 5) == 8


# build a test for subtract
def test_subtract():
    assert subtract(10, 5) == 5


# build a test for multiply
def test_multiply():
    assert multiply(5, 5) == 25


# build a test for divide
def test_divide():
    assert divide(10, 2) == 5
