# Problem Description:
# Given a list of integers, write a function that returns the largest sum
# of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5]
#  should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

import unittest


# This function runs in O(n) time and O(1) memory
def get_max_sum(arr):
    # The sum if the previous value in the array was included.
    included = 0

    # The sum if the previous value was excluded
    excluded = 0

    for val in arr:
        current_max = max(included, excluded)

        # If we include the current value, we must exclude the previous
        included = excluded + val

        # If we exclude the current value, then just keep the previous max
        excluded = current_max

    return max(included, excluded)


class TestMaxSum(unittest.TestCase):

    def test_empty(self):
        given = []
        expected = 0
        self.assertEqual(get_max_sum(given), expected)

    def test_length_1(self):
        given = [7]
        expected = 7
        self.assertEqual(get_max_sum(given), expected)

    def test_same_even(self):
        given = [2, 2, 2, 2, 2, 2, 2, 2]
        expected = 8
        self.assertEqual(get_max_sum(given), expected)

    def test_same_odd(self):
        given = [2, 2, 2, 2, 2, 2, 2, 2, 2]
        expected = 10
        self.assertEqual(get_max_sum(given), expected)

    def test_gap(self):
        given = [2, 3, 7, 0, 0, 0, 0, 0, 9]
        expected = 18
        self.assertEqual(get_max_sum(given), expected)

    def test_negatives(self):
        given = [2, 3, -7, 0, 0, 0, 0, 0, 9]
        expected = 12
        self.assertEqual(get_max_sum(given), expected)

    def test_sample_a(self):
        given = [2, 4, 6, 2, 5]
        expected = 13
        self.assertEqual(get_max_sum(given), expected)

    def test_sample_b(self):
        given = [5, 1, 1, 5]
        expected = 10
        self.assertEqual(get_max_sum(given), expected)


if __name__ == "__main__":
    unittest.main()
