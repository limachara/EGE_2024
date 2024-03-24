def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)

def c_evendivs(n):
    c = 0
    for el in divs(n):
        if el % 2 == 0:
            c += 1
    return c

t = 0
for k in range(1, 10**6):
    F = 777555 - k
    if c_evendivs(F) % 2 != 0:
        t += 1
        print(k, c_evendivs(F), sep='*', end='-')
    if t == 5:
        break

