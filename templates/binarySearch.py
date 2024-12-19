from typing import List
from timing_utils import measure_time

'''
Problem: Given SORTED array of numbers, find query number with fewest comparisons. Output the index of query
If no number found return -1
'''
def linearSearch(arr: List[int], query: int) -> int:
    for index, value in enumerate(arr):
        if value == query:
            return index
    return -1

measure_time(linearSearch, [1,2,3,4,5,6,7,8,9], 9)
