def f(n):
    s = f'{n:b}'
    c1 = 0
    for el in s:
        if el == '1':
            c1 += 1
    for k in range(2):
        if c1 % 2 == 0:
            s = s.replace('1', '', 1)
            s = s.lstrip('0')
            c1 -= 1
        else:
            s = '1' + s + '00'
            c1 += 1
    return int(s, 2)
for n in range(0, 1000):
    if f(n) > 100:
        print(n)
        break