def f(st, fin):
    if st < fin:
        return 0
    if st == 5 or st == 15:
        return 0
    if st == fin:
        return 1
    return f(st - 1, fin) + f(st - 4, fin) + f(st // 2, fin)


print(f(19, 2))