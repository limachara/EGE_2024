import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n < 125:
        return -n
    if n >= 125:
        return f(n-1)+2*g(n-2)
def g(n):
    if n < 123:
        return f(n-1)
    if n >= 123:
        return g(n-1) - 3*f(n-3)
print(f(131)-g(131))