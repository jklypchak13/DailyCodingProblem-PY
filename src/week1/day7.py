# Problem Description

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

import unittest

# This function runs in O(n) time and uses constant memory


def get_count(data):

    if len(data) < 1:
        return 1

    # memo[0] represents the count at index-2, and memo[1] counts it at index-1
    memo = [1, 1]

    for index in range(1, len(data)):

        prev_char = data[index-1]
        char = data[index]

        # If currently found a 'collision' of a letter > 9
        if prev_char is '1' or (prev_char is '2') and char < '7':
            temp_val = memo[1] + memo[0]
            memo[0] = memo[1]
            memo[1] = temp_val
        else:
            memo[0] = memo[1]

    return memo[1]


class TestDecodeCount(unittest.TestCase):

    def test_empty(self):
        given = ""
        expected = 1

        self.assertEqual(get_count(given), expected)

    def test_length_1(self):
        given = "1"
        expected = 1

        self.assertEqual(get_count(given), expected)

    def test_length_2_1_way(self):
        given = "54"
        expected = 1

        self.assertEqual(get_count(given), expected)

    def test_length_2_2_ways(self):
        given = "23"
        expected = 2

        self.assertEqual(get_count(given), expected)

    def test_length_normal(self):
        givens = [
            "111",
            "121",
            "376",
            "117842911",
            "1111",
            "12121"
        ]
        expecteds = [
            3,
            3,
            1,
            6,
            5,
            8
        ]

        for given, expected in zip(givens, expecteds):
            self.assertEqual(get_count(given), expected)


if __name__ == "__main__":
    unittest.main()
