from fnmatch import fnmatch

for n in range(143, 10**9 + 1, 143):
    if fnmatch(str(n), '131*131?'):
        print(n, n // 143, sep='*', end='-')