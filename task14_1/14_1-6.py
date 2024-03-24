def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        t = a[n % p] + t
        n = n // p
    return t
s = str(n_to_p(5*49**5 + 3*7**8 - 7*7**4 + 100,7))
c = 0
for el in s:
    c += int(el)
print(c)