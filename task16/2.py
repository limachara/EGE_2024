import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0 and n > 1:
        return n + f(n-1)
    if n % 2 != 0 and n > 1:
        return f(n-2)*2
print(f(20))