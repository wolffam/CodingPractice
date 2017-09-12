# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
# and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

# Also using the example through a unittest
import unittest


def sum67(li):
    out = 0
    between67 = False
    for num in li:
        if num == 6:
            between67 = True
        if between67 is False:
            out += num
        if num == 7:
            between67 = False
    return out


class TestSum67(unittest.TestCase):

    def test_ins(self):
        self.assertEqual(sum67([1, 2, 2]), 5)
        self.assertEqual(sum67([1, 2, 2, 6, 99, 99, 7]), 5)
        self.assertEqual(sum67([1, 1, 6, 7, 2]),4)


if __name__ == '__main__':
    unittest.main()