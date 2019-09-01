# Problem Description:

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number
#  from a set of positive integers X?
#  For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

import unittest


# This problem is solved in O(n) time and O(n) memory
def stair_count(n, steps):
    memo = [1] * (n + 1)
    current_val = 1
    for i in range(n + 1):
        current_val = 0
        for index, step_count in enumerate(steps):
            if i - step_count >= 0:
                current_val += memo[i - step_count]
        if current_val == 0:
            current_val = 1
        memo[i] = current_val
    return current_val


class TestStepCount(unittest.TestCase):

    def test_sample(self):
        expected = 5
        given = (4, [1, 2])

        self.assertEqual(stair_count(*given), expected)

    def test_empty(self):
        expected = 1
        given = (0, [1])

        self.assertEqual(stair_count(*given), expected)

    def test_step_count_3(self):
        expected = 4
        given = (3, [1, 2, 3])

        self.assertEqual(stair_count(*given), expected)

    def test_step_count_normal(self):
        expected = 47
        given = (10, [1, 3, 5])

        self.assertEqual(stair_count(*given), expected)


if __name__ == "__main__":
    unittest.main()
