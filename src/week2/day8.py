# Problem Description:

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
import unittest


class Node:

    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


# This function performs in O(n)
def unival_tree_count(root):
    count = 1
    if root is None:
        count = 0
    elif root.left is not None or root.right is not None:
        if root.left is None:
            count = root.right.val == root.val
        elif root.right is None:
            count = root.left.val == root.val
        elif root.right.val == root.val:
            count = root.left.val == root.right.val

        count += unival_tree_count(root.left)
        count += unival_tree_count(root.right)

    return count


class TestUnivalTree(unittest.TestCase):

    def test_root(self):
        expected = 1
        given = Node(2)

        self.assertEqual(unival_tree_count(given), expected)

    def test_sample(self):
        expected = 5
        given = Node(
            0,
            Node(1),
            Node(
                0,
                Node(
                    1,
                    Node(1),
                    Node(1)
                ),
                Node(0)
            )
        )
        self.assertEqual(unival_tree_count(given), expected)

    def test_line(self):
        expected = 4
        give = Node(
            2,
            Node(
                2,
                Node(
                    2,
                    Node(2)
                )
            )
        )
        self.assertEqual(unival_tree_count(give), expected)

    def test_large(self):
        expected = 10


if __name__ == "__main__":
    unittest.main()
