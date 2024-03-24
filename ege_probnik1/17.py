a = [int(x) for x in open('17.txt')]

mx4 = 0
for el in a:
    if len(str(el)) == 4 and el > mx4:
        mx4 = el
print(mx4)

b = []

for p1, p2, p3 in zip(a, a[1:], a[2:]):
    if (p1 % 10 == 3 or p1 % 10 == 5) + (p2 % 10 == 3 or p2 % 10 == 5) + (p3 % 10 == 3 or p3 % 10 == 5) > 1 and p1 * p2 * p3 < mx4 ** 3:
        b.append(p1 + p2 + p3)
print(len(b), max(b))