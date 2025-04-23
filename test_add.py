from calculator import calculator

def test_add():
    calc = calculator()

    assert calc.add(1, 2) == 3
    assert calc.add(0, 0) == 0
    assert calc.add(-1, 1) == 0

