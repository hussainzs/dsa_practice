from typing import List

'''
Problem: Given SORTED array of numbers, find query number with fewest comparisons. Output the index of query
If no number found return -1
'''
def linearSearch(arr: List[int], query: int) -> int:
    for index in arr:
        if arr[index] == query:
            return index
    
    return -1






tests = []
