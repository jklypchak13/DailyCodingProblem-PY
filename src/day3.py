# Problem Descriptions
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
#  and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
import unittest


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This solution runs in O(n)
def serialize(r):
    val = {}

    def _helper(root, idx):
        max_idx = idx
        if root is None:
            val[idx] = None
            return max_idx

        val[idx] = str(root.val)
        max_idx = max(_helper(root.left, 2*idx+1),
                      _helper(root.right, 2*idx+2), max_idx)

        return max_idx
    count = _helper(r, 0)
    result = ''

    last_i = 0
    for i in range(count):
        if i not in val or val[i] is None:
            result += ','
        else:
            result += val[i] + ','
            last_i = len(result)
    return result[0:last_i-1]


# This solution runs in O(n)
def deserialize(str):
    vals = str.split(',')

    def _process(index):

        if index >= len(vals) or vals[index] == '':
            return None
        value = vals[index]
        left = _process(2*index + 1)
        right = _process(2*index+2)
        return Node(value, left, right)

    return _process(0)


class TestTreeOperations(unittest.TestCase):
    def test_deserialize(self):
        expected = '10'
        given = '4,6,2,10,2,6'

        self.assertEqual(deserialize(given).left.left.val, expected)

    def test_deserialize_empty(self):
        expected = None
        given = ''

        self.assertEqual(deserialize(given), expected)

    def test_deserialize_complete(self):
        expected = '5'
        given = '1,2,3,4,5,6,7'

        self.assertEqual(deserialize(given).left.right.val, expected)

    def test_deserialize_root(self):
        expected = '1'
        given = '1'
        self.assertEqual(deserialize(given).val, expected)

    def test_deserialize_sparse(self):
        expected = '-1'
        given = '1,2,,,3,,,,,4,,,,,,,,,,,5,,,,,,,,,,,,,,,,,,,,,,-1'

        self.assertEqual(deserialize(
            given).left.right.left.right.right.val, expected)

    def test_serialize_normal(self):
        expected = '4,6,2,,10,6'
        given = Node(4,
                     Node(6,
                          None,
                          Node(10)
                          ),
                     Node(2,
                          Node(6),
                          None
                          )
                     )
        self.assertEqual(serialize(given), expected)

    def test_serialize_empty(self):
        expected = ''
        given = None

        self.assertEqual(serialize(given), expected)

    def test_serilize_root(self):
        expected = '10'
        given = Node(10)

        self.assertEqual(serialize(given), expected)

    def test_serilize_complete(self):
        expected = '1,2,3,4,5,6,7'
        given = Node(
            1,
            Node(
                2,
                Node(4),
                Node(5)
            ),
            Node(
                3,
                Node(6),
                Node(7)
            )
        )

        self.assertEqual(serialize(given), expected)

    def test_serilize_sparse(self):
        expected = '1,2,,,3,,,,,4,,,,,,,,,,,5,,,,,,,,,,,,,,,,,,,,,,-1'
        given = Node(
            1,
            left=Node(
                2,
                right=Node(
                    3,
                    left=Node(
                        4,
                        right=Node(
                            5,
                            right=Node(-1)
                        )
                    )
                )
            )
        )
        self.assertEqual(given.left.right.left.right.right.val, -1)

        self.assertEqual(serialize(given), expected)


if __name__ == '__main__':
    unittest.main()
