from calculator import Calculator

def test_divi():
    calc = Calculator()

    assert calc.divi(2, 2) == 1
    assert calc.divi(15, 5) == 3
    assert calc.divi(12, 1) == 12

