def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)

def is_prime(n):
    return len(divs(n)) == 2

a = [int(x) for x in open('9.txt')]

mx = -float('inf')
for el in a:
    if el % 3 == 0 and el % 27 != 0 and el > mx:
        mx = el

b = []
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    if (is_prime(p1) + is_prime(p2) + is_prime(p3) == 2) + (p1 > mx or p2 > mx or p3 > mx) == 1:
        b.append(is_prime(p1) + is_prime(p2) + is_prime(p3))
print(len(b), sum(b), sep='*')