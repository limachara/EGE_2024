def f(n):
    s = f'{n:b}'
    if n % 2 != 0:
        s = '10' + s + '11'
    else:
        s = '1' + s + '00'
    return int(s, 2)
a = []
for n in range(0, 1000):
    if f(n) > 1023:
        a.append(f(n))
print(min(a))