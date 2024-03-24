def f(st, fin):
    if st > fin:
        return 0
    if st == fin:
        return 1
    res = [f(st + 1, fin), f(st * 2, fin), f(st * 2 + 1, fin)]
    return sum(res)

print(f(int('10', 2), int('10000', 2)))