a = [int(x) for x in open('6.txt')]

s = 0
c = 0
for el in a:
    if abs(el) % 100 == 19:
        s += el
        c += 1
avg = s / c

b = []
for p1, p2, p3, p4 in zip(a, a[1:], a[2:], a[3:]):
    if (abs(p1) % 15 == 12 or abs(p2) % 15 == 12 or abs(p3) % 15 == 12 or abs(p4) % 15 == 12) and (p1 < avg) + (p2 < avg) + (p3 < avg) + (p4 < avg) >= 2:
        b.append(p1 + p2 + p3 + p4)
print(len(b), max(b), sep='*')