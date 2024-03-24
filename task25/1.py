from fnmatch import fnmatch

for n in range(2025, 10**9 + 1, 2025):
    if fnmatch(str(n), '1?31*437?'):
        print(n, n // 2025, sep='*', end='-')