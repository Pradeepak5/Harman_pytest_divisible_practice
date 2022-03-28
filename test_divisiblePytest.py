import divisiblePytest

def test_divisible_5():
    num=5
    result=divisiblePytest.divisible_5(num)
    assert result == True

def test_divisible_7():
    num=3
    result=divisiblePytest.divisible_7(num)
    assert result == False

def test_divisible_9():
    num=9
    result=divisiblePytest.divisible_9(num)
    assert result == True

def test_divisible_10():
    num=8
    result=divisiblePytest.divisible_10(num)
    assert result == False