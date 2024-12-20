from utils.timing_utils import measure_time
from typing import TypedDict

'''
Problem: Given SORTED array of numbers, find query number with fewest comparisons. Output the index of query.
If no number found, return -1.

Note: if the requirement was to return the index of first or last occurance (in case of repeating numbers) then 
we wull have to edit the standard implementation.
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
        mid: int = (left + right) // 2
        if arr[mid] == query:
            return mid
        elif arr[mid] > query:
            right = mid - 1
        else:
            left = mid + 1
    # if we havent returned index so far then no match was found
    return -1

class Test(TypedDict):
    input: list[int]
    query: int
    output: int

# Test cases
tests: list[Test] = [
    {'input': [1, 2, 3, 4, 5, 6], 'query': 5, 'output': 4},
    {'input': [1], 'query': 1, 'output': 0},
    {'input': [1], 'query': -9, 'output': -1},
    {'input': [], 'query': 5, 'output': -1}
]

def run_tests(test_arr: list[Test]) -> None:
    """
    Runs binary search and linear search tests on a list of test cases.
    Args:
        test_arr (list[Test]): A list of test cases where each test case is a dictionary
                               containing 'input' (list[int]), 'query' (int), and 'output' (int).
    Returns:
        None
    """
    for index, test in enumerate(test_arr):
        input: list[int] = test['input']
        query: int = test['query']
        expected_out: int = test['output']
        
        bs_out: int = binary_search(input, query)
        
        if bs_out == expected_out:
            print(f"Binary Search test {index} passed ✅")
            measure_time(binary_search, input, query)
        else:
            print(f"Binary Search test {index} failed ❌")
            print(f"input = {input}, query = {query}, expected output = {expected_out}")
            print()
            
    print()
    for index, test in enumerate(test_arr):
        input: list[int] = test['input']
        query: int = test['query']
        expected_out: int = test['output']
        
        ls_out: int = linear_search(input, query)
        
        if ls_out == expected_out:
            print(f"Linear Search test {index} passed ✅")
            measure_time(linear_search, input, query)
        else:
            print(f"Linear Search test {index} failed ❌")
            print(f"input = {input}, query = {query}, expected output = {expected_out}")
            print()
            
# Run tests
run_tests(tests)
        
