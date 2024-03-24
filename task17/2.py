a = [int(x) for x in open('2.txt')]

min7 = float('inf')
for el in a:
    if abs(el) % 10 == 7 and el < min7:
        min7 = el

b = []
for p1, p2 in zip(a, a[1:]):
    if (p1 + p2) % 4 == 0 and ((p1 < min7 and p2 > min7) or (p2 < min7 and p1 > min7)):
        b.append(p1 + p2)

print(len(b), max(b))