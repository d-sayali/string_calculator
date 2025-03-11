import pytest
from src.calculator import StringCalculator

def test_empty_string():
    assert StringCalculator.add("") == 0


def test_single_number():
    assert StringCalculator.add("1") == 1

