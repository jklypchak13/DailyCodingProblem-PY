# Problem Description:
# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext
#  and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory
#  subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system.
#  For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
# and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute
#  path to a file in the abstracted file system. If there is no file in the system, return 0.

# Note:

# The name of a file contains at least a period and an extension.

# The name of a directory or sub-directory will not contain a period.
import unittest


# This method runs in O(n) time and O(n) memory
def get_longest_path(path):

    # Helper Methods
    def _is_file(s):
        return s.find('.') >= 0

    def _stack_to_string(stack):
        result = ''
        for val in stack:
            result += val + '/'
        return result

    # Clean Up Input to managable data structure
    names = path.split('\n')
    for i in range(len(names)):
        count = names[i].count('\t')
        names[i] = (names[i][count:], count)

    stack = []
    max_path = 0
    for i in range(len(names)):
        name, level = names[i]
        if _is_file(name):
            max_path = max(len(_stack_to_string(stack) + name), max_path)
        if(i < len(names) - 1 and names[i + 1][1] < level):
            stack.pop()
        elif(i < len(names) - 1 and names[i + 1][1] > level):
            stack.append(name)

    return max_path


class TestLongestPath(unittest.TestCase):

    def test_empty(self):
        given = ''
        expected = 0

    def test_sample(self):
        given = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
        expected = 32

        self.assertEqual(get_longest_path(given), expected)

    def test_only_file(self):
        given = 'test.txt'
        expected = 8

        self.assertEqual(get_longest_path(given), expected)

    def test_one_dir(self):
        given = 'dir\n\ttest.txt'
        expected = 12

        self.assertEqual(get_longest_path(given), expected)

    def test_only_dirs(self):
        given = 'dir\n\tdir2\n\tdir3\n\t\tdir4'
        expected = 0

        self.assertEqual(get_longest_path(given), expected)

    def test_middle_result(self):
        given = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsub\n\t\td\n\t\t\tfile2.ext'
        expected = 21

        self.assertEqual(get_longest_path(given), expected)


if __name__ == "__main__":
    unittest.main()
