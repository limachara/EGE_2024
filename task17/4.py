a = [int(x) for x in open('4.txt')]

mx = -float('inf')
for el in a:
    if el % 1000 == 131 and el > mx:
        mx = el

b = []
g = []
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    if (1000 <= p1 < 10000) + (1000 <= p2 < 10000) + (1000 <= p3 < 10000) == 1 and (p1 + p2 < mx) + (p1 + p3 < mx) + (p2 + p3 < mx) >= 1:
        if p1 - p2 > 0:
            g.append(p1 - p2)
        if p1 - p3 > 0:
            g.append(p1 - p3)
        if p2 - p1 > 0:
            g.append(p2 - p1)
        if p2 - p3 > 0:
            g.append(p2 - p3)
        if p3 - p1 > 0:
            g.append(p3 - p1)
        if p3 - p2 > 0:
            g.append(p3 - p2)
        b.append(min(g))
print(len(b), min(b), sep='*')
