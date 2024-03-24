def f(st, fin, h):
    if st > fin:
        return 0
    if st == fin:
        if 'BB' not in h:
            return 1
    return f(st + 1, fin, h + 'A') + f(st * 2, fin, h + 'B') + f(st * 3, fin, h + 'C')


print(f(1, 15,''))
