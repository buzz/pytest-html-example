def add(a, b):
    return a - b


def substract(a, b):
    return a - b


def test_add():
    foo = 10
    bar = 12
    assert add(foo, bar) == 22


def test_substract():
    foo = 10
    bar = 12
    assert add(foo, bar) == -2
