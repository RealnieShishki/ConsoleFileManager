import math

num = (1,2,3,4,5)

def test_filter():
    assert list(filter(lambda x: x > 3, num)) == [4, 5]

def test_map():
    assert list(map(lambda x: x * x, num)) == [1, 4, 9, 16, 25]

def test_sorted():
    assert list(sorted(num, reverse=True)) == [5, 4, 3, 2, 1]

def test_math():
    assert math.pi * 4 ** 2 == 50.26548245743669
    assert math.sqrt(16) == 4
    assert math.pow(2, 5) == 32
    assert math.hypot(4, 3) == 5




