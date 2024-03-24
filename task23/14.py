def f(st, fin, k):
    if st > fin or k > 7:
        return 0
    if st == fin:
        return 1
    res = [f(st + 1, fin, k + 1),
           f(st + 2, fin, k + 1),
           f(st * 2, fin, k + 1)]
    return sum(res)


print(f(1, 35, 0))