def f(n):
    s = f'{n:0>8b}'
    s = s[::-1]
    return int(s, 2)
for n in range(1, 201):
    if f(n) == 21:
        print(n)