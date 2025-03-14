import pytest
from src.calculator import StringCalculator

def test_empty_string():
    assert StringCalculator.add("") == 0


def test_single_number():
    assert StringCalculator.add("1") == 1


def test_two_numbers():
    assert StringCalculator.add("1,2") == 3


def test_multiple_numbers():
    assert StringCalculator.add("1,2,3,4,5") == 15


def test_newline_as_delimiter():
    assert StringCalculator.add("1\n2,3") == 6


def test_custom_single_char_delimiter():
    assert StringCalculator.add("//;\n1;2") == 3


def test_custom_multi_char_delimiter():
    assert StringCalculator.add("//[***]\n1***2***3") == 6


def test_multiple_custom_delimiters():
    assert StringCalculator.add("//[*][%]\n1*2%3") == 6


def test_multiple_custom_delimiters_with_multi_length():
    assert StringCalculator.add("//[***][%%%]\n1***2%%%3") == 6


def test_ignore_numbers_greater_than_1000():
    assert StringCalculator.add("2,1001") == 2


def test_negative_numbers_raise_exception():
    with pytest.raises(ValueError, match=r"Negative numbers not allowed: -1"):
        StringCalculator.add("-1,2,3")


def test_multiple_negative_numbers_raise_exception():
    with pytest.raises(ValueError, match=r"Negative numbers not allowed: -1, -5"):
        StringCalculator.add("1,-1,2,-5")
