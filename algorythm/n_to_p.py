def n_to_p(n, p):
    t = ''
    a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while n:
        t = a[n % p] + t
        n = n // p
    return t
print(n_to_p((3*125**6+2*25**9+5**12-625), 5))
print(n_to_p((3*125**6+2*25**9+5**12-625), 5).count('0'))