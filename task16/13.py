import sys
sys.setrecursionlimit(10**6)
def f(n, m):
    if m > n:
        return 0
    if m <= n and n % m == 0:
        return f(n, m + 1) + 1
    if m <= n and n % m != 0:
        return f(n, m + 1)

print(f(131131, 77))