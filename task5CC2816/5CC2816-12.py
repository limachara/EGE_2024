def f(n):
    s = f'{n:b}'
    if n % 2 != 0:
        s = '1' + s + '11'
    else:
        s = '11' + s + '00'
    return int(s, 2)
print(f(5))
a = []
for n in range(0, 10000):
    if f(n) < 127:
        a.append(f(n))
print(max(a))
