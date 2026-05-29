# test_dict_sum.py
import pytest
from dict_sum import sum_dict_values

def test_sum_dict_values():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    assert sum_dict_values(dict1) == 6

def test_sum_dict_values_empty():
    dict1 = {}
    assert sum_dict_values(dict1) == 0

def test_sum_dict_values_negative():
    dict1 = {'a': -1, 'b': 2, 'c': -3}
    assert sum_dict_values(dict1) == -2

def test_sum_dict_values_float():
    dict1 = {'a': 1.5, 'b': 2.5, 'c': 3.5}
    assert sum_dict_values(dict1) == 7.5
