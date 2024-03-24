def f(st, fin):
    if st < fin:
        return 0
    if st == fin:
        return 1
    res = [f(st - 1, fin)]
    if st % 2 == 0:
        res.append(f(st // 2, fin))
    if st % 3 == 0:
        res.append(f(st // 3, fin))
    return sum(res)


print(f(30, 1))