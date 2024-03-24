def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        t = a[n % p] + t
        n = n // p
    return t

print(n_to_p(12*32**2 + 16**3 - int(0.5*8**2) + 12, 8))