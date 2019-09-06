# Problem Description:

# Given an array of integers and a number k, where 1 <= k <= length of the array,
#  compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do
# not need to store the results. You can simply print them out as you compute them.

# Note: The values will be stored and returned for testing purposes.
from collections import deque
import unittest


def get_max_subarrays(arr, k):
    n = len(arr)
    vals = deque()
    max_values = []
    if len(arr) < k:
        return []

    for i in range(k):

        while vals and arr[i] >= arr[vals[-1]]:
            vals.pop()

        vals.append(i)

    for i in range(k, n):
        max_values.append(arr[vals[0]])

        while vals and vals[0] <= i - k:
            vals.popleft()

        while vals and arr[i] >= arr[vals[-1]]:
            vals.pop()

        vals.append(i)

    max_values.append(arr[vals[0]])

    return max_values


class TestMaxSub(unittest.TestCase):

    def test_empty(self):
        expected = []
        given = [], 4

        self.assertEqual(get_max_subarrays(*given), expected)

    def test_given_sample(self):
        expected = [10, 7, 8, 8]
        given = [10, 5, 2, 7, 8, 7], 3

        self.assertEqual(get_max_subarrays(*given), expected)

    def test_length(self):
        expected = [10]
        given = [10, 5, 2, 7, 8, 7], 6

        self.assertEqual(get_max_subarrays(*given), expected)

    def test_size_1(self):
        expected = [10, 5, 2, 7, 8, 7]
        given = [10, 5, 2, 7, 8, 7], 1

        self.assertEqual(get_max_subarrays(*given), expected)

    def test_all_the_same(self):
        expected = [5, 5, 5]
        given = [5, 5, 5, 5, 5], 3

        self.assertEqual(get_max_subarrays(*given), expected)

    def test_all_the_same(self):
        expected = [5, 5, 5]
        given = [5, 5, 5, 5, 5], 3

        self.assertEqual(get_max_subarrays(*given), expected)


if __name__ == "__main__":
    unittest.main()
