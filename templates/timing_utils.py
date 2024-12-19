from typing import List, Callable, Any
import timeit

def measure_time(func: Callable, *args: Any, **kwargs: Any) -> float:
    """Executes a function 5 times and returns its average execution time.
    Also prints the exection statement.
    
    Args:
        func (Callable): Function to be measured.
        *args (Any): Positional arguments to pass to the function.
        **kwargs (Any): Keyword arguments to pass to the function.

    Returns:
        float: measured execution time
    """
    
    # wrapper function because timeit.timeit expects a function with no arguements
    def wrapper():
        return func(*args, **kwargs)
    
    repeat_count: int = 5
    execution_time: float = timeit.timeit(stmt=wrapper, number=repeat_count)
    average_time: float = execution_time / repeat_count
    
    print(f"Ran {func.__name__} for {repeat_count} times. Average Execution time = {average_time} seconds")   
    return average_time