import sys
sys.setrecursionlimit(10**6)
def f(q, p):
    if p == 0:
        return q
    if p > 0:
        return f(p, q % p)
a = set()
for q in range(50, 251):
    for p in range(50, 251):
        if f(q, p) == 25:
            a.add(q)
print(len(a))
