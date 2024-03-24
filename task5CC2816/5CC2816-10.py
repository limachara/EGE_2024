def f(n):
    s = f'{n:0>8b}'
    c0 = 0
    c1 = 0
    for el in s:
        if el == '0':
            c0 += 1
        else:
            c1 += 1
    for k in range(3):
        if c0 == c1:
            s = s + s[-1]
            if s[-1] == '0':
                c0 += 1
            else:
                c1 += 1
            break
        if c0 < c1:
            s = s + '0'
            c0 += 1
        if c1 < c0:
            s = s + '1'
            c1 += 1
    return int(s, 2)
def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        t = a[n % p] + t
        n = n // p
    return t
for n in range(132, 1000):
    if n_to_p(f(n), 8)[-1] == '0':
        print(n)
        break