from functools import lru_cache

"""
Implement a function recursively to get the desired Fibonacci sequence value.
Your code should have the same input/output as the iterative code in the instructions.
"""
@lru_cache(max_size = 1000)
def get_fib(position):
    if position == 0:
        return 0
        
    if position == 1 or position == 2:
        return 1
        
    if position > 2:
        return get_fib(position-1) + get_fib(position-2)
        
    if type(position) != int:
        raise TypeError("The input must be an integer")
    
    if position < 0:
        raise ValueError("The input must be an integer")
    
# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(1000))