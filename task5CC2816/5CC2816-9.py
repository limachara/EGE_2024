def f(n):
    s1 = f'{n:o}'
    if len(s1) >= 2:
        d1 = s1[1]
        s1 = s1 + d1
        d2 = s1[-2]
        s1 = d2 + s1
        return int(s1, 8)
    else:
        return n

for i in range(1, 1000):
    if f(i) > 32768:
        print(i)
        break