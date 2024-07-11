import math
"""
1.1 Suppose you have a sorted list of 128 names, and you’re searching through it using binary search.
What’s the maximum number of steps it would take?
2^x = 128
x = 7

Answer: 7 steps

1.2 Suppose you double the size of the list. What’s the maximum number of steps now?

2^(x+7) = 2*2^7
2^(x+7) = 2^(1+7)
x = 1

Answer: 8 steps
"""


def count_max_steps_binary_search(n):
    return math.log(n, 2)
