def f(s1, s2, c, m):
    if s1 + s2 >= 98:
        return c % 2 == m % 2
    if c >= m:
        return False
    moves = [f(s1 + 3, s2, c + 1, m), f(s1 * 2, s2, c + 1, m), f(s1, s2 + 3, c + 1, m), f(s1, s2 * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)

for s2 in range(1, 90 + 1):
    for m in range(1, 4 + 1):
        if f(7, s2, 0, m):
            print(s2, m)
            break