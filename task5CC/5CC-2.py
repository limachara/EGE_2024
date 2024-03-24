def f(n):
    d1, d2, d3, d4, d5 = map(int, str(n))
    s = sorted([d1 + d3 + d5, d2 + d4], reverse=True)
    res = ''.join(map(str, s))
    return res


for i in range(10000, 100000):
    if f(i) == '213':
        print(i)
        break