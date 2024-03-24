import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n < 10:
        return n
    if n >= 10:
        return f(n // 10) + n % 10
for n in range(999, 100, -1):
    if f(n) < f(131):
        print(n)
        break