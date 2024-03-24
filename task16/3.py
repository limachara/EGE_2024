import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n < 3:
        return 2
    if n >=3 and n % 3 == 0:
        return f(n-1)*3
    if n >=3 and n % 3 == 1:
        return f(n-1)+1
    if n >= 3 and n % 3 == 2:
        return f(n-2)+2
print(f(30))
