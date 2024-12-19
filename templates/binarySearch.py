from typing import List
from utils.timing_utils import measure_time

'''
Problem: Given SORTED array of numbers, find query number with fewest comparisons. Output the index of query
If no number found return -1
'''

import sys
print(sys.path[0:3])
print("_____________________________")


def linear_search(arr: List[int], query: int) -> int:
    for index, value in enumerate(arr):
        if value == query:
            return index
    return -1


measure_time(linear_search, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
