import numpy as np

array = np.load('array.npy')

print('Array shape', array.shape)

print(array)


def test0(ar):
    # has exactly 10 positive values
    # should be 0, 11, 13, 14
    pass


def test1(ar):
    # has exactly 24 none-zeros elements
    # should be 8, 12, 14, 18, 19
    return np.count_nonzero(ar) == 24


def test2(ar):
    # has equal number of positive and negative numbers
    # should be 15, 19
    pass


def test3(ar):
    # has exactly 8 equal elements
    # e.g [1,1,3,4,3] has 4 equal elements
    # should be 0, 7
    pass


def test4(ar):
    # has even number of even elements
    # e.g [0, 1, 2, 35, 46] has 2 even none-zero elements
    # should be 0, 2, 3, 6, 7, 10, 11, 12, 14, 16, 17, 18, 19
    pass


def test5(ar):
    # has a pair of opposite numbers
    # e.g [0, -1, 0, 1, 3, ] has such pair 1 and -1
    # should be 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19
    pass


def test6(ar):
    # is as ascending sequence of elements
    # e.g [-12, -1, 0, 1, 3]
    # should be 17
    pass


def test7(ar):
    # is a descending sequence of elements
    # e.g [12, 1, 0, -1, -3]
    # should be 12
    pass


results = []

for i in range(array.shape[0]):
    row = array[i]
    # it should be N rows (first dimension)

    if test1(row):
        results.append(i)

print('Results:', results)
