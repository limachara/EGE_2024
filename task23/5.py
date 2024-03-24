def f(st, fin):
    if st > fin:
        return 0
    if st == fin:
        return 1
    return f(st + 2, fin) + f(st + 3, fin) + f(st * 2, fin)


print(f(1, 9) * f(9, 20))