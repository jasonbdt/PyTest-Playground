import pytest
from main import upper_lower


def test_only_lower_letters():
    assert upper_lower("lowlow") == False


def test_capital_letter_at_middle():
    assert upper_lower("blaBla") == True


def test_capital_and_lower_letter_at_end():
    assert upper_lower("blabLa") == True


def test_capital_letter_at_end():
    assert upper_lower("byE") == False


def test_capital_letter_at_beginning():
    assert upper_lower("Hello") == True


def test_only_capitals():
    assert upper_lower("BOOM") == False


def test_empty_string():
    assert upper_lower("") == False


pytest.main()
