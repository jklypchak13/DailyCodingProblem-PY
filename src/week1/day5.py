# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.

import unittest


# Given Code Snippet
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


# This Solution runs in constant time
def car(pair):
    def _get_first(a, b):
        return a

    return pair(_get_first)


# This Solution runs in constant time
def cdr(pair):
    def _get_second(a, b):
        return b

    return pair(_get_second)


class TestCar(unittest.TestCase):

    def test_basic(self):
        given = cons(1, 2)
        expected = 1

        self.assertEqual(car(given), expected)

    def test_same(self):
        given = cons(10, 10)
        expected = 10

        self.assertEqual(car(given), expected)

    def test_zeros(self):
        given = cons(0, 18)
        expected = 0

        self.assertEqual(car(given), expected)

    def test_none(self):
        given = cons(None, None)
        expected = None

        self.assertEqual(car(given), expected)


class TestCDR(unittest.TestCase):

    def test_basic(self):
        given = cons(1, 2)
        expected = 2

        self.assertEqual(cdr(given), expected)

    def test_same(self):
        given = cons(10, 10)
        expected = 10

        self.assertEqual(cdr(given), expected)

    def test_zeros(self):
        given = cons(18, 0)
        expected = 0

        self.assertEqual(cdr(given), expected)

    def test_none(self):
        given = cons(None, None)
        expected = None

        self.assertEqual(cdr(given), expected)

if __name__ == "__main__":
    unittest.main()
