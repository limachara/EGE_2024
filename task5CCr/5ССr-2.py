def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuwxyz'
    while n:
        t = a[n % p] + t
        n = n // p
    return t
def f(n):
    s = n_to_p(n, 4)
    if n % 2 != 0:
        s = '2' + s + '11'
    else:
        s = '13' + s + '02'
    return int(s, 4)
a = []
for n in range(1, 1000):
    if f(n) > 1000:
        a.append(f(n))
print(min(a))