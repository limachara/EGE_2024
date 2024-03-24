a = set()
b = set()
for n in range(1, 11):
    s = '7' * 2 + '5' * n + '7' * 2
    while '755' in s or '557' in s:
        s = s.replace('55', '5', 1)
        if '75' in s:
            s = s.replace('75', '57', 1)
        else:
            s = s.replace('57', '5', 1)
    a.add(s)
for n in range(10, 3001):
    s = '7' * 2 + '5' * n + '7' * 2
    while '755' in s or '557' in s:
        s = s.replace('55', '5', 1)
        if '75' in s:
            s = s.replace('75', '57', 1)
        else:
            s = s.replace('57', '5', 1)
    b.add(s)
print(len(a))
print(len(b))