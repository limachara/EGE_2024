def n_to_5(n):
    s = ''
    while n:
        s = str(n % 5) + s
        n //= 5
    return s

k = 0
for n in range(25, 125):
    t = n_to_5(n)
    if t[0] > t[1] > t[2]:
        k += 1
print(k)