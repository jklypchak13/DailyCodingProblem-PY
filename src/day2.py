
# Problem Description:
# Given an array of integers, return a new array such that each element at index i
# of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

import unittest


# This solution runs in O(n)
def array_prod(arr):
    n = len(arr)

    result = [1]*n

    left = [1]*n
    right = [1]*n

    for i in range(1, n):
        left[i] = arr[i-1]*left[i-1]

    for i in range(n-2, -1, -1):
        right[i] = arr[i+1]*right[i+1]

    return [l_val*r_val for l_val, r_val in zip(left, right)]


class TestArrayProduct(unittest.TestCase):

    # Test the Empty Set
    def test_empty(self):
        given = []
        expected = []
        self.assertEqual(array_prod(given), expected)

    # Test Sets of Length 1
    def test_length_1(self):
        given = [
            [0],
            [1],
            [2]
        ]
        expected = [
            [1],
            [1],
            [1]
        ]
        for given_val, expected_val in zip(given, expected):
            self.assertEqual(array_prod(given_val), expected_val)

    # Test Sets with 0's
    def test_zeroes(self):
        given = [
            [5, 0],
            [2, 3, 0, 9],
            [2, 5, 7, 9, 0, 0, 3]
        ]
        expected = [
            [0, 5],
            [0, 0, 54, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        for given_val, expected_val in zip(given, expected):
            self.assertEqual(array_prod(given_val), expected_val)

    # Test General Use Cases
    def test_normal(self):
        given = [
            [1, 2],
            [5, 6],
            [2, 5],
            [9, 6, 12],
            [1, 1, 1, 1, 1],
            [3, 3, 3],
            [1, 2, 3, 4, 5]
        ]
        expected = [
            [2, 1],
            [6, 5],
            [5, 2],
            [72, 108, 54],
            [1, 1, 1, 1, 1],
            [9, 9, 9],
            [120, 60, 40, 30, 24]
        ]
        for given_val, expected_val in zip(given, expected):
            self.assertEqual(array_prod(given_val), expected_val)


if __name__ == "__main__":
    unittest.main()
