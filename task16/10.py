from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return f(n-1) + f(n-2) + f(n-3)

for n in range(1, 132):
    f(n)
print(f(131))