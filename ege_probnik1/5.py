def n_to_p(n, p):
    t = ''
    a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while n:
        t = a[n % p] + t
        n //= p
    if t == '':
        return '0'
    return t

for n in range(1, 100):
    r1 = n_to_p(n, 3)
    r2 = r1 + n_to_p(r1.count('2'), 3)
    r3 = r2 + n_to_p(r2.count('1'), 3)
    r4 = r3 + n_to_p(r3.count('0'), 3)
    r = int(r4, 3)
    if r < 1000:
        print(n, r)
    if n == 5:
        print(r1, r2, r3, r4, r)