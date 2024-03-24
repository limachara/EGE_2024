def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuwxyz'
    while n:
        t = a[n % p] + t
        n = n // p
    return t
def f(n):
    s = n_to_p(n // 2, 16)
    if n % 4 != 0:
        s = 'f' + s + 'a0'
    else:
        s = '15' + s + 'c'
    return int(s, 16)
a = []
for n in range(0, 1000):
    if f(n) < 65536:
        a.append(n)
print(max(a))
