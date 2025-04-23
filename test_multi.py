def test_multi():

    assert multi(1, 2) == 2
    assert multi(15, 0) == 0
    assert multi(9, 9) == 81

def multi(a,b):
    return a * b