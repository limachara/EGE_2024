def f(n):
    a = []
    while n > 0:
        a.append(n % 45)
        n //= 45
    s_even = s_odd = 0
    for i in range(1, len(a) + 1):
        if i % 2 == 0:
            s_even += a[-i]
        else:
            s_odd += a[-i]
    if min(s_even, s_odd) > 0:
        a.append(min(s_even, s_odd))
    a.insert(0, max(s_even, s_odd))
    r = 0
    for i in range(len(a)):
        r += a[i]*45**i
    return r
results = []
for n in range(1001, 20000):
    results.append(f(n))
print(min((results)))