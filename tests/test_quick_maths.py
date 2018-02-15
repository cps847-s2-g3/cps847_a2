import sys
sys.path.insert(0, './')
import pytest
from quick_maths import two_plus_two, four_minus_one

def test_2_plus_2():
    assert(two_plus_two() == 4)

def test_4_minus_1():
    assert(four_minus_one() == 3)