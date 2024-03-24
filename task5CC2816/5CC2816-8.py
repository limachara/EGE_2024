def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        t = a[n % p] + t
        n = n // p
    return t
for n in range(1, 1000):
    d1 = int(n_to_p(n, 8)) // 10 % 10
    d2 = int(n_to_p(n, 8)) // 1 % 10
    b = n_to_p(n, 8) + str(d2) + str(d1)
    if int(b, 8) > 1000:
        print(n)
        print(b)
        break