from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("CS50") == "CS50"
    assert shorten("cs50") == "cs50"
    assert shorten("twitter50") == "twttr50"
    assert shorten("twitter.com") == "twttr.cm"