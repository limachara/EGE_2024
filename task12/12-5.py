def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True

for n in range(1, 100):
    s = '>' + '1' * 14 + '2' * 11 + '3' * n
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '23>', 1)
        elif '>2' in s:
            s = s.replace('>2', '21>', 1)
        elif '>3' in s:
            s = s.replace('>3', '7>', 1)
    s = s.replace('>', '')
    t = sum(map(int, s))
    print(n, t)