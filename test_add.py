from calculator import Calculator

def test_add():
    calc = Calculator()

    assert calc.add(1, 2) == 3
    assert calc.add(0, 0) == 0
    assert calc.add(-1, 1) == 0

