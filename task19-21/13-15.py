def f(s, c, m, k1, k2, k3):
    if s >= 155:
        return c % 2 == m % 2
    if c >= m:
        return False
    moves = []
    if k1 == 0:
        moves.append(f(s * 3, c + 1, m, 1, 0, 0))
    if k2 == 0:
        moves.append(f(s + 2, c + 1, m, 0, 1, 0))
    if k3 == 0:
        moves.append(f(s + 5, c + 1, m, 0, 0, 1))
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)

for s in range(1, 154 + 1):
    for m in range(1, 4 + 1):
        if f(s, 0, m, 0, 0, 0):
            print(s, m)
            break