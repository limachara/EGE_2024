import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n < 10:
        return n
    if n >= 10 and n % 3 == 0:
        return f(n - 1) + 3 * n**2
    if n >= 10 and n % 3 != 0:
        return f(n - 1) + n**3
k = 0
for n in range(1, 1000):
    if f(n) < 10**9:
        k += 1
print(k)