def f(n):
    s1 = f'{n:0>8b}'
    s2 = s1[1:]
    return int(s2,2)
a = set()
for n in range(131, 3132):
    a.add(n - f(n))
print(len(a))


