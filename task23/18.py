def f(st, k):
    global a
    if k == 7:
        return st
    a.add(f(st - 5, k + 1))
    a.add(f(st * (-2), k + 1))
    return None

a = set()
f(131, 0)
a = a - {None}

c = 0
for el in a:
    if el > 0:
        c += 1
print(c)