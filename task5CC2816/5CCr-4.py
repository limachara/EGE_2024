def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuwxyz'
    while n:
        t = a[n % p] + t
        n = n // p
    return t
def f(n):
    s = n_to_p(n, 7)
    c = 0
    for el in s:
        c += int(el)
    s = '10' + s[2:] + n_to_p(c, 7)
    c = 0
    for el in s:
        c += int(el)
    s = '100' + s[3:] + n_to_p(c, 7)
    c = 0
    for el in s:
        c += int(el)
    s = '1000' + s[4:] + n_to_p(c, 7)
    return int(s, 7)
a = []
for n in range(10, 1000):
    if f(n) > 100000:
        a.append(f(n))
print(min(a))