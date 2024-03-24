def f(s, c, m):
    if s >= 141:
        return c % 2 == m % 2
    if c >= m:
        return False
    moves = [f(s + 1, c + 1, m), f(s * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 140 + 1):
    for m in range(1, 4 + 1):
        if f(s, 0, m):
            print(s, m)
            break

#c - текущий ход
#m - выигрышный ход