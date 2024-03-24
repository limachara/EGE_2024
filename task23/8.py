def f(st, fin):
    if st > fin or st in [7, 12, 17]:
        return 0
    if st == fin:
        return 1
    res = [f(st + 1, fin), f(st + 4, fin), f(st * 3, fin)]
    return sum(res)


print(f(3, 15) * f(15, 30))