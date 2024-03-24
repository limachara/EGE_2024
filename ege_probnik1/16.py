from functools import lru_cache
@lru_cache(None)

def f(n):
    if n == 1:
        return 2
    if n > 1 and f(n-1) < 7555444:
        return f(n-1) + 6
    else:
        return f(n-1) - 7555444

mx = 0
for n in range(1, 10**7):
    if f(n) > mx:
        mx = f(n)
print(mx)
