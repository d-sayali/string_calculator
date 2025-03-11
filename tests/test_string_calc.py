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

