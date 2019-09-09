# Problem Description:

# A builder is looking to build a row of N houses that can be of K different colors.
#  He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
#  return the minimum cost which achieves this goal.

import unittest


def get_min_cost(n, k, table):

    min_costs = [[0 for i in range(k)] for j in range(n)]
    for i in range(k):
        min_costs[0][i] = table[0][i]
    for i in range(1, n):
        for j in range(0, k):
            previous = min_costs[i - 1][:j] + min_costs[i - 1][j + 1:]
            min_costs[i][j] = table[i][j] + min(previous)
    return min(min_costs[n - 1])


class TestMinCost(unittest.TestCase):

    def test_normal(self):
        table = [
            [5, 7, 10],
            [7, 7, 5],
            [8, 5, 4]
        ]
        expected = 15
        given = (3, 3, table)

        self.assertEqual(get_min_cost(*given), expected)

    def test_one_house(self):
        table = [
            [5, 7, 8]
        ]
        expected = 5
        given = (1, 3, table)

        self.assertEqual(get_min_cost(*given), expected)

    def test_alternating_houses(self):
        table = [
            [5, 7, 8, 8],
            [3, 2, 8, 8],
            [4, 3, 8, 8],
            [3, 5, 8, 8],
            [7, 4, 8, 8]
        ]
        expected = 20
        given = (5, 4, table)

        self.assertEqual(get_min_cost(*given), expected)


if __name__ == "__main__":
    unittest.main()
