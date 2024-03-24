def divs(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    if len(d) == 0:
        return 0
    s = sorted(d)
    return s[0] + s[-1]

k = 0
for n in range(777829, 10**10):
    m = divs(n)
    if m % 100 == 16:
        k += 1
        print(n, m, sep='*', end='-')
    if k == 5:
        break




