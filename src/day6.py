# Problem Description:
# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of
# the next node and the previous node.
# Implement an XOR linked list; it has an add(element) which adds the element to the end, and a
# get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer
# and dereference_pointer functions that converts between nodes and memory addresses.

import unittest


# The following are used to simply implement pointer behavior in Python
addrs = {0: 0}


def get_pointer(node):
    return id(node)


def dereference_pointer(addr):
    return addrs[addr]


# Insertion is in O(1) and get is in O(n), though in reality its n/2
class XORList():

    def __init__(self):
        self.value = None
        self.both = 0
        self.length = 0
        self.last = self
        addrs[get_pointer(self)] = self

    def add(self, value):
        prev_addr = 0
        current = self
        if self.length == 0:
            self.value = value
            self.length += 1
            return

        last_node = self.last

        val = XORList()
        val.value = value
        addr = get_pointer(val)

        prev_addr = self._xor(0, last_node.both)
        last_node.both = self._xor(prev_addr, addr)
        self.last = val
        val.both = self._xor(0, get_pointer(last_node))

        self.length += 1

    def get(self, target_idx):
        if target_idx >= self.length or target_idx < 0:
            return None

        idx = 0
        prev_pointer = 0
        change = 1
        current = self

        # If the target index is in the second half, go through backwards
        if(target_idx > self.length/2):
            current = self.last
            idx = self.length - 1
            change = -1

        while target_idx != idx:
            next_val = dereference_pointer(
                self._xor(prev_pointer, current.both))
            prev_pointer = get_pointer(current)
            current = next_val
            idx += change

        return current.value

    @staticmethod
    def _xor(val1, val2):
        return val1 ^ val2


class TestXORList(unittest.TestCase):

    def test_empty(self):
        given = XORList()

        expected = None

        self.assertEqual(given.get(0), expected)
        self.assertEqual(given.get(1), expected)

    def test_length_1(self):
        given = XORList()
        given.add(3)
        expected = 3

        self.assertEqual(given.get(0), expected)

    def test_length_2(self):
        given = XORList()
        vals = [3, 7]
        expected = [3, 7]

        for val in vals:
            given.add(val)

        for i in range(len(expected)):
            self.assertEqual(given.get(i), expected[i])

    def test_length_7(self):
        given = XORList()
        vals = [3, 7, 2, 6, 1, 7, 5]
        expected = [3, 7, 2, 6, 1, 7, 5]

        for val in vals:
            given.add(val)

        for i in range(len(expected)):
            self.assertEqual(given.get(i), expected[i])


if __name__ == "__main__":
    unittest.main()
