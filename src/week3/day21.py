# Problem Description:
# Given an array of time intervals(start, end) for classroom lectures(possibly overlapping),
# find the minimum number of rooms required.

# For example, given[(30, 75), (0, 50), (60, 150)], you should return 2.
import unittest


# Run is O(nlog(n)) time and O(n) memory
def get_max_room_count(schedule):
    data = []
    for start, end in schedule:
        data.append((start, 1))
        data.append((end, -1))
    data.sort()

    room_count = 0
    max_count = 0

    for time, resource in data:
        room_count += resource
        max_count = max(max_count, room_count)

    return max_count


class TestRoomCount(unittest.TestCase):

    def test_empty(self):
        expected = 0
        given = []

        self.assertEqual(get_max_room_count(given), expected)

    def test_one_event(self):
        expected = 1
        given = [(30, 130)]

        self.assertEqual(get_max_room_count(given), expected)

    def test_all_overlap(self):
        expected = 4
        given = [(30, 130), (30, 130), (30, 130), (50, 60)]

        self.assertEqual(get_max_room_count(given), expected)

    def test_normal(self):
        expected = 2
        given = [(0, 60), (30, 90), (60, 120), (90, 150)]

        self.assertEqual(get_max_room_count(given), expected)

    def test_sample(self):
        expected = 2
        given = [(30, 75), (0, 50), (60, 150)]

        self.assertEqual(get_max_room_count(given), expected)


if __name__ == "__main__":
    unittest.main()
