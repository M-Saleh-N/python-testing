from calculator import Calculator

def test_divi():
    calc = Calculator()

    try:

        assert calc.divi(2, 2) == 1
        assert calc.divi(15, 5) == 3
        assert calc.divi(12, 1) == 12
    except ValueError as e :
        assert str(e) == "Cannot divide by zero"

