for n in range(500, 1001):
    s = '3' * n
    while '111' in s or '3333' in s:
        if '111' in s:
            s = s.replace('111', '33', 1)
        else:
            s = s.replace('333', '1', 1)
    if s == '11333':
        print(n)
        break