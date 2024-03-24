def f(n):
    s1 = f'{n:0>8b}'
    s1 = s1[:-1]
    if n % 2 != 0:
        s1 += '10'
    else:
        s1 += '01'
    return int(s1, 2)
for n in range(1, 10000):
    if f(n) == 2025:
        print(n)
        break
