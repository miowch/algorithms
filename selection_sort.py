from multipledispatch import dispatch
import unittest
"""
Suppose you have a bunch of music on your computer. For each artist, you have a play count.
You want to sort this list from most to least played, so that you can rank your favorite artists.
How can you do it?
"""


def find_index_max_number(array):
    max_number = array[0]
    index_max_number = 0

    for i in range(1, len(array)):
        if array[i] > max_number:
            max_number = array[i]
            index_max_number = i

    return index_max_number


def find_index_min_number(array):
    min_number = array[0]
    index_min_number = 0

    for i in range(1, len(array)):
        if array[i] < min_number:
            min_number = array[i]
            index_min_number = i

    return index_min_number


@dispatch(list)
def desc_sort(array):
    sorted_list = []

    for i in range(len(array)):
        biggest = find_index_max_number(array)
        sorted_list.append(array.pop(biggest))

    return sorted_list


@dispatch(list)
def asc_sort(array):
    sorted_list = []

    for i in range(len(array)):
        smallest = find_index_min_number(array)
        sorted_list.append(array.pop(smallest))

    return sorted_list


@dispatch(dict)
def desc_sort(dictionary):
    sorted_dict = {}
    sorted_values = desc_sort(list(dictionary.values()))

    for i in sorted_values:
        for entry in dictionary:
            if dictionary[entry] == i:
                sorted_dict[entry] = dictionary[entry]

    return sorted_dict


@dispatch(dict)
def asc_sort(dictionary):
    sorted_dict = {}
    sorted_values = asc_sort(list(dictionary.values()))

    for i in sorted_values:
        for entry in dictionary:
            if dictionary[entry] == i:
                sorted_dict[entry] = dictionary[entry]

    return sorted_dict


class TestSelectionSort(unittest.TestCase):
    music_list = {
        'krovostok': 666,
        'shklovsky': 300,
        'slowdive': 40,
        'marc lavoine': 89,
        'chapelier fou': 78,
        'l\'imperatrice': 59,
        'auktyon': 212}

    def test_desc_sort(self):
        target_list = {
            'krovostok': 666,
            'shklovsky': 300,
            'auktyon': 212,
            'marc lavoine': 89,
            'chapelier fou': 78,
            'l\'imperatrice': 59,
            'slowdive': 40}

        self.assertEqual(target_list, desc_sort(self.music_list))

    def test_asc_sort(self):
        target_list = {
            'slowdive': 40,
            'l\'imperatrice': 59,
            'chapelier fou': 78,
            'marc lavoine': 89,
            'auktyon': 212,
            'shklovsky': 300,
            'krovostok': 666}

        self.assertEqual(target_list, asc_sort(self.music_list))


if __name__ == '__main__':
    unittest.main()
