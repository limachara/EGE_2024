c_max = 0
for n in range(3, 10000 + 1):
    s = '4' + '0' * n
    while '000' in s or '40' in s or '100' in s:
        if '000' in s:
            s = s.replace('000', '1', 1)
        if '40' in s:
            s = s.replace('40', '0', 1)
        if '100' in s:
            s = s.replace('100', '04', 1)
    c_now = sum(map(int, s))
    if c_now > c_max:
        c_max = c_now
print(c_max)