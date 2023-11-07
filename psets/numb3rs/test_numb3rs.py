from numb3rs import validate

def test_format():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3.4.") == False
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False
    assert validate("cat") == False

def test_range():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.256") == False