# Problem Description

# Implement a job scheduler which takes in a function f and an integer n,
#  and calls f after n milliseconds.

import unittest
import time


# This function is designed to only handle one job at a time, and could
# be used in a multithreaded sense to schedule multiple jobs. Although this
# solution does meet the requirements of the problem, a further improvement could
# be creating it's own thread of execution.

# Another design note is that kwargs were added, as well as returning the result
# of the specified function. This seemed useful and desired, and the return was also added
# for testing purposes
def schedule_job(f, n, **kwargs):

    desired_time = time.time() + n / 1000

    while desired_time > time.time():
        pass
    return f(*kwargs)


# Function used for testing
def a():
    return time.time()


class TestScheduler(unittest.TestCase):

    def test_one_millisecond(self):
        given = (a, 1)
        expected = time.time() + (1 / 1000)

        self.assertAlmostEqual(schedule_job(*given), expected, 4)

    def test_zero(self):
        given = (a, 0)
        expected = time.time()

        self.assertAlmostEqual(schedule_job(*given), expected, 4)

    def test_negative(self):
        given = (a, -1000)
        expected = time.time()

        self.assertAlmostEqual(schedule_job(*given), expected, 4)

    def test_second(self):
        given = (a, 1000)
        expected = time.time() + 1

        self.assertAlmostEqual(schedule_job(*given), expected, 4)

    def test_10_seconds(self):
        given = (a, 10000)
        expected = time.time() + 10

        self.assertAlmostEqual(schedule_job(*given), expected, 4)

    def test_uneven(self):
        given = (a, 667)
        expected = time.time() + 667 / 1000.0

        self.assertAlmostEqual(schedule_job(*given), expected, 4)


if __name__ == "__main__":
    unittest.main()
