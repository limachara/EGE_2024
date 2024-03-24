def f(n):
    s = f'{n:b}'
    c1 = 0
    c0 = 0
    for a in s:
        if a == '1':
            c1 += 1
        else:
            c0 += 1
    if c1 > c0:
        s = s + '1'
    else:
        s = s + '0'
    return int(s, 2)
for n in range(1, 100):
    if f(n) > 100:
        print(f(n))
        print(f'{n:b}')
        break