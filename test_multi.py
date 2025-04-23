from calculator import Calculator

def test_multi():
    calc = Calculator()

    assert calc.multi(1, 2) == 2
    assert calc.multi(15, 0) == 0
    assert calc.multi(9, 9) == 81
