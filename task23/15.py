def f(st, k):
    global a
    if k == 4:
        return st
    a.add(f(st + 1, k + 1))
    a.add(f(st + 3, k + 1))
    a.add(f(st * 3, k + 1))
    return None

a = set()
f(1, 0)
a = a - {None}
print(len(a))
print(a)