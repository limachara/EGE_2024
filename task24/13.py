from collections import Counter

f = open('13.txt')
s = f.readline().strip()
a = []
for c1, c2, c3 in zip(s, s[1:], s[2:]):
    if c1 == 'S' and c3 == 'S':
        a.append(c2)
print(Counter(a))
print(sorted('biym'))