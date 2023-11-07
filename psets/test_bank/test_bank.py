from CS50X.w6.practice_prob.bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("HEY") == 20
    assert value("carrot") == 100
    assert value("Carrot") == 100
    assert value("CARROT") == 100