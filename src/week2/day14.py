# Problem Description:


import unittest
import random
import math


# This problem samples 10 million times to have a high likelyhood of
#   correctly approximating, and succeeding the test.
def approx_pi():

    n = 10000000
    hits = 0
    for i in range(n):

        # Generate Random Coordinate
        rand_x = random.random()
        rand_y = random.random()

        # Check if it's in the unit circle
        if rand_x * rand_x + rand_y * rand_y <= 1:
            hits += 1
    return hits * 4 / n


class TestPi(unittest.TestCase):

    def test_pi(self):
        expected = 3.142

        self.assertAlmostEqual(approx_pi(), expected, 3)


if __name__ == "__main__":
    unittest.main()
