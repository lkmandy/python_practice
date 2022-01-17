
from functools import lru_cache

@lru_cache(maxsize = 5)
def factorial(n):
    if n < 2: return 1
    else:
        return n * factorial(n-1)

print(factorial(5))