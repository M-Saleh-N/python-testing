from calculator import calculator
def test_add():
    calc = calculator()

    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

