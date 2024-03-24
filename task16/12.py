from functools import lru_cache

@lru_cache(None)
def f(n):
    if n > 5000:
        return n
    if n <= 5000:
        return f(n + 2) + f(n + 4) + 2 * n

for n in range(5000, 2023, -1):
    f(n)
print( (f(2023) + f(2025)) - (3 * f(2027) + 2 * f(2029)) )