from working import convert
import pytest

def test_time():
   assert convert("9 AM to 5 PM") == "09:00 to 17:00"
   assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
   assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
   assert convert("9:23 AM to 11:45 PM") ==  "09:23 to 23:45"

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

def test_wrong_hr():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("5 AM to 13 PM")

def test_wrong_min():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")