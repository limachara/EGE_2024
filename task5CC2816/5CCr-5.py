def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuwxyz'
    while n:
        t = a[n % p] + t
        n = n // p
    return t
def f(n):
    s = n_to_p(n, 20)
    t = ''
    for el in s:
        if el != 'j':
            t = t + n_to_p(int(el, 20) + 1, 20)
        else:
            t = t + 'j'
    return int(t, 20)
a = set()
for n in range(1, 10000):
    if 1000 <= f(n) <= 10000:
        a.add(f(n))
print(len(a))