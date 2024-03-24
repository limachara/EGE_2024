def f(st, fin):
    if st > fin or st == 11:
        return 0
    if st == fin:
        return 1
    res = [f(st + 1, fin),
           f(st + 3, fin),
           f(st * 3, fin)]
    return sum(res)

for n in range(1, 100):
    if f(1, 10) * f(10, n) == 132:
        print(n)
        break