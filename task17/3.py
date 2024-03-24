a = [int(x) for x in open('3.txt')]

avg = sum(a[1::2]) / len(a[1::2])

b = []
g = 0
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    if max(p1, p2, p3) % 2 == 0 and (p1 > avg) + (p2 > avg) + (p3 > avg) >= 2:
        b.append(max(p1 - p2, p1 - p3, p2 - p1, p2 - p3, p3 - p1, p3 - p2))
print(len(b), max(b), sep='*')
