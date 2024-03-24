def f(st, fin, k):
    if st > fin or k > 6:
        return 0
    if st == fin and 1 <= k <= 6:
        return 1
    res = [f(st + 1, fin, k + 1),
           f(st * 2, fin, k + 1),
           f(st ** 2, fin, k + 1)]
    return sum(res)


c = 0
for n in range(1, 132):
    if f(n, 131, 0) > 0:
        c += 1
print(c)
