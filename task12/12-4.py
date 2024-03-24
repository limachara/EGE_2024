for n in range(10, 132):
    s = '7' * n + '55'
    while '777' in s or '555' in s:
        if '777' in s:
            s = s.replace('777', '5', 1)
        else:
            s = s.replace('555', '7', 1)
    if s.count('5') >= 4:
        print(n)

