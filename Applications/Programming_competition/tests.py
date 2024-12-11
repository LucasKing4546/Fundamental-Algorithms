from feature_1 import *
from feature_2 import *
from feature_3 import *
from feature_4 import *
from feature_5 import *

def test_add():
    assert add([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5, 6]
    assert add([1, 2, 3, 4, 5], -1) == [1, 2, 3, 4, 5]
    assert add([1, 2, 3, 4, 5], 'dadadw') == [1, 2, 3, 4, 5]

def test_insert():
    assert insert([1, 2, 3, 4, 5], 3, 6) == [1, 2, 3, 6, 4, 5]
    assert insert([1, 2, 3, 4, 5], 0, 3) == [3, 1, 2, 3, 4, 5]
    assert insert([1, 2, 3, 4, 5], -1, 3) == [1, 2, 3, 4, 5]

def test_replace():
    assert replace([1, 2, 3, 4, 5], 3, 6) == [1, 2, 3, 6, 5]
    assert replace([1, 2, 3, 4, 5], 0, 3) == [3, 2, 3, 4, 5]
    assert replace([1, 2, 3, 4, 5], -1, 3) == [1, 2, 3, 4, 5]

def test_remove():
    assert remove([1, 2, 3, 4, 5], 3) == [1, 2, 3, 5]
    assert remove([1, 2, 3, 4, 5], 0) == [2, 3, 4, 5]
    assert remove([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

def test_remove_multiple():
    assert remove_multiple([1, 2, 3, 4, 5], 3, 4) == [1, 2, 3]
    assert remove_multiple([1, 2, 3, 4, 5], 0, 3) == [5]
    assert remove_multiple([1, 2, 3, 4, 5], 0, 5) == [1, 2, 3, 4, 5]

def test_less():
    assert less([1, 2, 3, 4, 5], 3) == [1, 2]
    assert less([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4]
    assert less([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]

def test_sorted():
    assert sorted([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sorted([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sorted([1, 4, 2, 3, 5]) == [1, 2, 3, 4, 5]

def test_sorted_by_higher_value():
    assert sorted_by_higher_value([1, 2, 3, 4, 5], 3) == [4, 5]
    assert sorted_by_higher_value([1, 2, 3, 4, 5], 5) == []
    assert sorted_by_higher_value([3, 4, 1, 5, 2], 2) == [3, 4, 5]

def test_min():
    assert min([1, 2, 3, 4, 5], 3, 4) == 4
    assert min([1, 2, 3, 4, 5], 0, 3) == 1
    assert min([1, 2, 3, 4, 5], 1, 4) == 2

def test_avg():
    assert avg([1, 2, 3, 4, 5], 3, 4) == 4.5
    assert avg([1, 2, 3, 4, 5], 0, 3) == 2.5
    assert avg([1, 2, 3, 4, 5], 0, 4) == 3

def test_mul():
    assert mul([1, 2, 3, 4, 5], 3, 4, 4) == []
    assert mul([1, 2, 3, 4, 5], 1, 0, 4) == [1, 2, 3, 4, 5]
    assert mul([1, 2, 3, 4, 5], 2, 0, 4) == [2, 4]


def test_filter_mul():
    assert filter_mul([2, 4, 6, 8, 10], 2) == [2, 4, 6, 8, 10]
    assert filter_mul([3, 6, 9, 12, 15], 3) == [3, 6, 9, 12, 15]
    assert filter_mul([2, -6, 9, -12, 18], 3) == [-6, 9, -12, 18]

def test_filter_greater():
    assert filter_greater([10, 20, 30, 40], 25) == [30, 40]
    assert filter_greater([1, 2, 3, 4, 5], 5) == []
    assert filter_greater([0, 5, 10, 15, 20], 0) == [5, 10, 15, 20]

test_add()
test_insert()
test_remove()
test_remove_multiple()
test_replace()
test_sorted()
test_sorted_by_higher_value()
test_mul()
test_min()
test_avg()
test_filter_mul()
test_filter_greater()

