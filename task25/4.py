from fnmatch import fnmatch

k = 0
for n in range(131, 10**8 + 1, 131):
    if fnmatch(str(n), '*13?*?1*'):
        k += 1
        if k % 1131 == 0:
            print(n, n // 131, sep='*', end='-')