def f(st, fin):
    if st > fin:
        return 0
    if st == 12:
        return 0
    if st == fin:
        return 1
    return f(st + 1, fin) + f(st * 2, fin) + f(st * st, fin)


print(f(3, 20))