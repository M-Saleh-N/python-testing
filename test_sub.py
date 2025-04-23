from calculator import calculator

def test_sub():
    calc = calculator()
    
    assert calc.sub(5, 2) == 3
    assert calc.sub(0, 0) == 0
    assert calc.sub(10, 1) == 9

