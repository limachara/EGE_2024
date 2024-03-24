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
            s = s.replace('0', '')
            s = s + '1'
            c1 += 1
    return int(s, 2)
c = 0
for n in range(0, 1001):
    if f(n) == 7:
        c += 1
print(c)