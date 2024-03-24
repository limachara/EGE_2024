def n_to_p(n, p):
    t = ''
    a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while n:
        t = a[n % p] + t
        n //= p
    return t


r = n_to_p(625 ** 90 + 125 ** 120 - 5 * 25, 25)
print(r)
s = 0
even = [0, 2, 4, 6, 8]
for el in r:
    if int(el) in even:
        s += int(el)
print(s)
