from token import ELLIPSIS
from utils.timing_utils import measure_time

'''
Problem: Given SORTED array of numbers, find query number with fewest comparisons. Output the index of query.
If no number found, return -1.
'''


def linear_search(arr: list[int], query: int) -> int:
    for index, value in enumerate(arr):
        if value == query:
            return index
    return -1

def binary_search(arr: list[int], query: int) -> int:
    # empty array -> return -1 right away (small obvious optimization)
    if len(arr) == 0:
        return -1
    
    left: int = 0
    right: int = len(arr) - 1
    
    while left <= right:
        mid: int = int((left + right) / 2)
        if arr[mid] == query:
            return mid
        elif arr[mid] > query:
            right = mid - 1
        else:
            left = mid + 1
    # if we havent returned index so far then no match was found
    return -1


measure_time(linear_search, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
