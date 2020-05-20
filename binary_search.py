import unittest

"""
Binary search works only when the list is in sorted order.
"""


def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle_element = (low + high) // 2
        guess = array[middle_element]

        if guess < target:
            low = middle_element + 1
        elif guess > target:
            high = middle_element - 1
        else:
            return middle_element

    return None


class TestBinarySearch(unittest.TestCase):
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_target_less_than_guess(self):
        target_index = binary_search(self.array, 2)
        self.assertEqual(2, target_index)

    def test_target_more_than_guess(self):
        target_index = i2 = binary_search(self.array, 8)
        self.assertEqual(8, target_index)

    def test_target_not_in_list(self):
        target_index = binary_search(self.array, 10)
        self.assertEqual(None, target_index)


if __name__ == '__main__':
    unittest.main()
