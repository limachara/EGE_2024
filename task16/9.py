import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n < 10:
        return n
    if n >= 10:
        return f(g(n))
def g(n):
    if n < 10:
        return n
    if n >= 10:
        return g(n // 10) + n % 10
s = 0
for n in range(1, 101):
    s += f(n)
print(s)