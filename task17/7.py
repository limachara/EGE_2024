a = [int(x) for x in open('7.txt')]

h = sorted(a)[-3:]
mx1 = h[2]
mx2 = h[1]
mx3 = h[0]

b = []
for p1, p2, p3, p4 in zip(a, a[1:], a[2:], a[3:]):
    t = sorted([p1, p2, p3, p4])
    if t[1] + t[2] + t[3] > mx1 + mx2 and t[0] < (mx3 / 2):
        b.append(p1 + p2 + p3 + p4)
print(len(b), min(b), sep='*')