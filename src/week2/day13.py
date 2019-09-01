# Problem Description:
# Given an integer k and a string s, find the length of the longest
#  substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

import unittest


# This solution runs in 0(n) time and O(k) memory
def find_longest_substring(s, k):
    max_string = ''
    counts = {}
    current_string = ''
    unique_characters = 0

    for c in s:
        if c not in counts.keys():
            counts[c] = 0

        # Add Current Character to String
        if counts[c] == 0:
            unique_characters += 1
        current_string += c
        counts[c] += 1

        # Trim String until down to k characters
        while(unique_characters > k):
            val = current_string[0]
            current_string = current_string[1:]
            counts[val] -= 1
            if counts[val] == 0:
                unique_characters -= 1

        # Check if we have a new max_string
        if len(max_string) < len(current_string):
            max_string = current_string
    return max_string


class TestLongestSubstring(unittest.TestCase):

    def test_given(self):
        given = 'abcba', 2
        expected = 'bcb'

        self.assertEqual(find_longest_substring(*given), expected)

    def test_empty(self):
        given = '', 2
        expected = ''

        self.assertEqual(find_longest_substring(*given), expected)

    def test_whole_string(self):
        given = 'abccbaabccba', 3
        expected = 'abccbaabccba'

        self.assertEqual(find_longest_substring(*given), expected)

    def test_same_length_string(self):
        given = 'abcdef', 3
        expected = 'abc'

        self.assertEqual(find_longest_substring(*given), expected)

    def test_end_string(self):
        given = 'abcdeff', 3
        expected = 'deff'

        self.assertEqual(find_longest_substring(*given), expected)


if __name__ == "__main__":
    unittest.main()
