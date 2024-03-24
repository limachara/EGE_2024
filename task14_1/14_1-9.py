def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        t = a[n % p] + t
        n = n // p
    return t
for n in range(143, 0, -1):
    print(n_to_p(n, 16), n_to_p(n, 5), n)
for x in range(143, 0, -1):
    if x % 16 == 3 and x % 5 == 1:
        print(x)
        break