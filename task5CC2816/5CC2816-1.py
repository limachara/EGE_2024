def f(n):
    s1 = f'{n:0>8b}'
    c = 0
    t = s1
    for el in t:
        c += int(el)
    c = c % 2
    t = t + str(c)
    c = 0
    for el in t:
        c += int(el)
    c = c % 2
    t = t + str(c)
    return int(t, 2)
for n in range(1, 100):
    if f(n) > 48:
        print(f(n))
        break
