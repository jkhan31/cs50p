import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("0/2") == 0
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(67) == "67%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")