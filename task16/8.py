import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 5 == 0:
        return f(n / 5) + 5
    if n >= 2 and n % 5 != 0:
        return f(n - 3) + 5
a = []
b = {}
for n in range(1, 10**5):
    a.append(f(n))
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
print(b)