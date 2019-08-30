# Problem Description:

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

import unittest


class Node:

    def __init__(self, word):
        self.val = False
        self.word = word
        self.children = {}


class WordTree:

    def __init__(self, words):
        self.head = Node('')
        for word in words:
            self.add_node(word)

    # Adds a word to the Tree
    def add_node(self, word):
        current = self.head
        for i in range(len(word)):
            c = word[i]
            if c not in current.children.keys():
                current.children[c] = Node(word[0:i + 1])
            current = current.children[c]
        current.val = True

    # Gets all words with the specified prefix
    def query_phrase(self, word):
        current = self.head

        # Traverse the tree, getting to the node of the current string.
        for c in word:
            if c not in current.children.keys():
                return []
            current = current.children[c]

        # Currently at the node representing the current string, so find all children
        def _get_children(node):
            result = []
            if node.val:
                result.append(node.word)
            for value in node.children.values():
                result.extend(_get_children(value))
            return result

        return _get_children(current)


# This is the single function specified to call and check the query. This is
#  inefficient as the tree is created each time, but this could be saved elsewhere,
#  and even passed into the function instead of an array

def get_possible_words(words, str):
    query_tree = WordTree(words)
    return query_tree.query_phrase(str)


class TestAutoComplete(unittest.TestCase):

    def test_empty_string(self):
        given = ['cat', 'dog', 'do', 'stuff', 'all', 'help'], ''
        expected = ['cat', 'do', 'dog', 'stuff', 'all', 'help']

        self.assertEqual(get_possible_words(*given), expected)

    def test_sample(self):
        given = ['dog', 'deer', 'deal'], 'de'
        expected = ['deer', 'deal']

        self.assertEqual(get_possible_words(*given), expected)

    def test_shorter_word(self):
        given = ['do'], 'dog'
        expected = []

        self.assertEqual(get_possible_words(*given), expected)

    def test_normal(self):
        given = (['confess',
                  'step'
                  'retire',
                  'turn',
                  'wrong',
                  'heavy',
                  'stew',
                  'unused',
                  'well-groomed',
                  'cabbage',
                  'last',
                  'complain'],
                 'st')
        expected = ['stepretire', 'stew']

        self.assertEqual(get_possible_words(*given), expected)


if __name__ == "__main__":
    unittest.main()
