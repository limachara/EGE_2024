def f(st, fin, k):
    if st > fin or k > 7:
        return 0
    if st == fin:
        return 1
    res = [f(st + 1, fin, k + (st + 1 + 1) % 2), f(st * 2, fin, k + (st * 2 + 1) % 2),
           f(st * 3, fin, k + (st * 3 + 1) % 2)]
    return sum(res)


print(f(1, 131, (1 + 1) % 2))
