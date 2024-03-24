def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuwxyz'
    while n:
        t = a[n % p] + t
        n = n // p
    return t
def f(n):
    s = n_to_p(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        s = s + n_to_p(n % 3 * 4, 3)
    return int(s, 3)
a = []
for n in range(1, 1000):
    if f(n) < 1199:
        a.append(n)
print(max(a))