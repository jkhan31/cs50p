from plates import is_valid

def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("1234") == False
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("50CS50") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
