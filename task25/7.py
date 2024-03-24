def divs(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sum(d)

k = 0
for n in range(131132, 10**10):
    s = divs(n)
    if s != 0 and s % 5 == 0:
        k += 1
        print(n, s, sep='*', end='-')
    if k == 5:
        break