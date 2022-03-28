import divisiblePytest
import pytest

@pytest.fixture
def input():
    num=10
    return num

def test_divisible_5(input):
    result=divisiblePytest.divisible_5(input)
    assert result == True

def test_divisible_7(input):
    result=divisiblePytest.divisible_7(input)
    assert result == False

def test_divisible_9(input):
    result=divisiblePytest.divisible_9(input)
    assert result == False

def test_divisible_10(input):
    result=divisiblePytest.divisible_10(input)
    assert result == True