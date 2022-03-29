__all__ = ['test_one', 'test_two']


import numpy as np



def test_one(data1, data2):
    c = data1 + data2
    return c

def test_two(a, b, c):
    result = test_one(a, b)
    final = result + c
    return final
