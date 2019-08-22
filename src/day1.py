# Problem Description
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

import unittest


# This solution runs in O(n)
def array_sum_pairs(arr, k):

    checked = set()

    for val in arr:
        compliment = k-val

        if compliment in checked:
            return True

        checked.add(val)

    return False


class TestSumPairs(unittest.TestCase):
    def test_empty(self):
        given_arrs = [
            []
        ]
        given_k = [
            [1]
        ]
        expected = [
            False
        ]

        for arr, k, exp in zip(given_arrs, given_k, expected):
            self.assertEqual(array_sum_pairs(arr, k), exp)

    def test_length_1(self):
        given_arrs = [
            [1],
            [2],
            [7]
        ]
        given_k = [
            1,
            2,
            3
        ]
        expected = [
            False,
            False,
            False
        ]

        for arr, k, exp in zip(given_arrs, given_k, expected):
            self.assertEqual(array_sum_pairs(arr, k), exp)

    def test_normal(self):
        given_arrs = [
            [1, 2],
            [2, 7],
            [21, 2, 1, 6, 7],
            [10, 15, 3, 7],
            [10, 15, 3, 7]
        ]
        given_k = [
            3,
            8,
            28,
            17,
            20
        ]
        expected = [
            True,
            False,
            True,
            True,
            False
        ]

        for arr, k, exp in zip(given_arrs, given_k, expected):
            self.assertEqual(array_sum_pairs(arr, k), exp)


if __name__ == "__main__":
    unittest.main()
