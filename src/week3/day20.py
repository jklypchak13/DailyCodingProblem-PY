# Problem Description:

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_intersection(l1, l2):

    def _get_length(current):
        length = 0
        while current is not None:
            current = current.next
            length += 1
        return length

    first_length = _get_length(l1)
    second_length = _get_length(l2)

    # Figure Out Which is Longer/Shorter
    (longest, shorter) = (l1, l2) if first_length > second_length else (l2, l1)
    diff = abs(first_length - second_length)

    # Set both to same length
    while(diff > 0):
        longest = longest.next
        diff -= 1

    # Keep going until first intersection is found
    while longest is not None and shorter is not None:
        if longest.val == shorter.val:
            return longest.val
        else:
            longest = longest.next
            shorter = shorter.next


def create_linked_list(arr):
    previous = None
    front = None
    for val in arr:
        temp = Node(val)
        if previous is None:
            front = temp
        else:
            previous.next = temp
        previous = temp
    return front


class TestIntersection(unittest.TestCase):

    def test_sample(self):
        given1 = create_linked_list([3, 7, 8, 10])
        given2 = create_linked_list([99, 1, 8, 10])

        expected = 8

        self.assertEqual(get_intersection(given1, given2), expected)

    def test_end(self):
        given1 = create_linked_list([6, 7, 3, 10])
        given2 = create_linked_list([99, 1, 2, 10])

        expected = 10

        self.assertEqual(get_intersection(given1, given2), expected)


if __name__ == "__main__":
    unittest.main()
