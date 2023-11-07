from seasons import age_to_minutes, minutes_to_words
from datetime import date

def test_age_to_minutes():
    assert age_to_minutes(date.fromisoformat('2022-09-11')) == 525600
    assert age_to_minutes(date.fromisoformat('2021-09-11')) == 1051200


def test_minutes_to_words():
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"