def f(st, fin, h):
    if st > fin:
        return 0
    if st == fin:
        if h[-2] == '2':
            return 1
    return f(st + 1, fin, h + '1') + f(st * 2, fin, h + '2') + f(st * 3, fin, h + '2')


print(f(1, 28,''))
