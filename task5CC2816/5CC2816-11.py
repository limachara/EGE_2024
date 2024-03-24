def f(n):
    s = f'{n:b}'
    c1 = 0
    c0 = 0
    for i in range(len(s)):
        if i % 2 != 0:
            if s[i] == '1':
                c1 += 1
        else:
            if s[i] == '0':
                c0 += 1

    return abs(c1 - c0)
print(f(131))
c = 0
for n in range(1000, 5001):
    if f(n) >= 5:
        c += 1
print(c)