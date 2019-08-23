# Problem Description:

# Given an array of integers, find the first missing positive integer in linear time and constant space.
#  In other words, find the lowest positive integer that does not exist in the array.
#   The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

import unittest


# As specified, this solution operates in O(n) time and
# in constant memory
def get_lowest_missing_val(arr):

    n = len(arr)

    # Move all negative and zero values to the left
    j = 0
    for i in range(0, n):
        if(arr[i] <= 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1

    # Flip Values if non-negative
    for i in range(0, n):
        if(abs(arr[i])-1 < n and arr[abs(arr[i])-1] > 0):
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    # Find Missing Value
    for i in range(0, n):
        if arr[i] > 0:
            return i+1
    return n-j+1


# Unit Tests
class TestArrayLowVal(unittest.TestCase):

    def test_empty(self):
        expected = 1
        arr = []

        self.assertEqual(get_lowest_missing_val(arr), expected)

    def test_length_1(self):
        expected = 1
        arr = [2]

        self.assertEqual(get_lowest_missing_val(arr), expected)

    def test_length_1_b(self):
        expected = 2
        arr = [1]

        self.assertEqual(get_lowest_missing_val(arr), expected)

    def test_non_negative(self):
        arr = [2, 5, 2, 1, 3]
        expected = 4
        self.assertEqual(get_lowest_missing_val(arr), expected)

        arr = [1, 7, 2]
        expected = 3.
        self.assertEqual(get_lowest_missing_val(arr), expected)

    def test_negative(self):
        arr = [3, 4, -1, 1]
        expected = 2
        self.assertEqual(get_lowest_missing_val(arr), expected)

        arr = [1, 2, 0]
        expected = 3
        self.assertEqual(get_lowest_missing_val(arr), expected)


if __name__ == "__main__":
    unittest.main()
