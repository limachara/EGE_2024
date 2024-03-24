from functools import lru_cache
@lru_cache(None)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * f(n - 1) + g(n - 1) - n
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return 3 * f(n - 1) - 2 * g(n - 1) + n
for n in range(1, 33):
    f(n)
    g(n)
k = str(g(33))
print(sum(map(int, k[1:])))