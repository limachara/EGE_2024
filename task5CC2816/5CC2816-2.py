def f(n):
    s1 = f'{n:0>8b}'
    s1 = s1 + s1[7]
    c = 0
    for el in s1:
        c += int(el)
    t = s1 + str(c % 2)
    return int(t, 2)
for n in range(1, 100):
    if f(n) > 167:
        print(f(n))
        break
