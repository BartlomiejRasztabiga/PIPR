from main import add


def test_add_regular1():
    assert(add(1, 2) == 3)

def test_fail():
    assert(False)