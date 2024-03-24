from fnmatch import fnmatch

def even_divs(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                d.add(i)
            if (n // i) % 2 == 0:
                d.add(n // i)
    if n % 2 == 0:
        d.add(n)
    return sorted(d)


k = 0
for n in range(135001, 10**9):
    if fnmatch(str(n), '1*717*1?') and len(even_divs(n)) > 4:
        k += 1
        print(n, sum(even_divs(n)), sep='*', end='-')
    if k == 6:
        break
