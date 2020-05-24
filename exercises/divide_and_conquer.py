"""
EXERCISES
4.1 Write out the code for the earlier sum function.
4.2 Write a recursive function to count the number of items in a list.
4.3 Find the maximum number in a list.
4.4 Remember binary search from chapter 1? It’s a divide-and-conquer algorithm, too.
    Can you come up with the base case and recursive case for binary search?
"""


# 4.1 Write out the code for the sum function
def summarise(ab: list):
    if len(ab) == 0:  # base case
        return 0
    for n in ab:  # recursive case
        return ab[0] + summarise(ab[1:])


# Tests
assert summarise([]) == 0
assert summarise([0]) == 0
assert summarise([1, 0]) == 1
assert summarise([1, 1]) == 2
assert summarise([1, 2, 4]) == 7


# 4.2 Write a recursive function to count the number of items in a list
def count_list_elements(ab: list):
    if not ab:  # base case
        return 0
    for n in ab:  # recursive case
        return 1 + count_list_elements(ab[1:])


# Tests
assert count_list_elements([]) == 0
assert count_list_elements([2]) == 1
assert count_list_elements([1, 0]) == 2


# 4.3 Find the maximum number in a list
def max_in(ab: list):
    if len(ab) <= 2:  # base case
        if len(ab) == 0:
            return 0
        elif len(ab) == 1 or ab[0] > ab[1]:
            return ab[0]
        else:
            return ab[1]

    for n in ab:  # recursive case
        if n > max_in(ab[1:]):
            return n
        else:
            return max_in(ab[1:])


# Tests
assert max_in([1, 2]) == 2
assert max_in([3, 5, 1]) == 5
assert max_in([1]) == 1
assert max_in([]) == 0


# 4.4 Remember binary search from chapter 1? It’s a divide-and-conquer algorithm, too.
# Can you come up with the base case and recursive case for binary search?
def binary_search_recursive(array: list, target):
    if len(array) == 1:  # base case
        if array[0] == target:
            return f"{target} is found in the list."
        else:
            return f"{target} is not in the list."
        
    middle_index = len(array) // 2  # recursive case

    if target == array[middle_index]:
        return f"{target} is found in the list."
    if target > array[middle_index]:
        if middle_index + 1 < len(array):
            return binary_search_recursive(array[middle_index+1:], target)
        else:
            return f"{target} is not in the list."
    if target < array[middle_index]:
        return binary_search_recursive(array[:middle_index], target)


# Tests
array = [1, 2, 8, 11, 15]
assert binary_search_recursive(array, 1) == "1 is found in the list."
assert binary_search_recursive(array, 15) == "15 is found in the list."
assert binary_search_recursive(array, 2) == "2 is found in the list."
assert binary_search_recursive(array, 8) == "8 is found in the list."
assert binary_search_recursive(array, 0) == "0 is not in the list."
assert binary_search_recursive(array, 3) == "3 is not in the list."
assert binary_search_recursive(array, 16) == "16 is not in the list."

array = [1, 2, 8, 11]
assert binary_search_recursive(array, 8) == "8 is found in the list."
assert binary_search_recursive(array, 7) == "7 is not in the list."
