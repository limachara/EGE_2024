a = [int(x) for x in open('5.txt')]

b = []
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    p1, p2, p3 = sorted([p1, p2, p3])
    if (p2 - p1) == (p3 - p2) > 0 and p1 % 10 != p2 % 10 != p3 % 10 != p1 % 10:
        b.append(p2 - p1)
print(len(b), min(b), sep='*')
