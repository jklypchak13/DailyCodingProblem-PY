# Problem Description:
# You run an e-commerce website and want to record the last N order ids in a log.
#  Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.
import unittest


# Assumption: ith last I'm assuming means recent. So valid i values will be from 1 to N, where N is the oldest
#   value in the log, and 1 is the most recent. (This could just be reversed if necessary)
class OrderLog:

    def __init__(self, n):
        self.current_index = -1
        self.data = [None] * n

    # Constant Time
    def record(self, order_id):
        self.current_index = (self.current_index + 1) % len(self.data)
        self.data[self.current_index] = order_id

    # Constant Time
    def get_last(self, i):
        if i < 1:
            return None
        idx = self.current_index - i + 1
        if(idx < 0):
            idx += len(self.data)
        return self.data[idx]


def add_orders(log, arr):
    for val in arr:
        log.record(val)


class TestOrderLog(unittest.TestCase):

    def test_one_element(self):
        given = OrderLog(1)
        add_orders(given, [1])
        expected = 1

        self.assertEqual(given.get_last(1), expected)

    def test_normal_case(self):
        given = OrderLog(6)
        add_orders(given, [1, 2, 3, 4, 5, 6, 7, 8])
        expected = 5

        self.assertEqual(given.get_last(4), expected)

    def test_wrap_around(self):
        given = OrderLog(3)
        add_orders(given, [1, 2, 3, 4, 5, 6, 7, 8])
        expected = 7

        self.assertEqual(given.get_last(2), expected)

    def test_zero(self):
        given = OrderLog(20)
        add_orders(given, [1, 2, 3, 4, 5, 6, 7, 8])
        expected = None

        self.assertEqual(given.get_last(0), expected)

    def test_not_added(self):
        given = OrderLog(20)
        add_orders(given, [1, 2, 3, 4, 5, 6, 7, 8])
        expected = None
        self.assertEqual(given.get_last(17), expected)

    def test_last(self):
        given = OrderLog(8)
        add_orders(given, [1, 2, 3, 4, 5, 6, 7, 8])
        expected = 1
        self.assertEqual(given.get_last(8), expected)


if __name__ == "__main__":
    unittest.main()
