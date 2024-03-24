from fnmatch import fnmatch

def valid(n):
    b = list(map(int, str(n)))
    for i in range(len(b) - 1):
        if b[i] <= b[i + 1]:
            return False
    return True

for n in range(940, 10**10 + 1, 47):
    if valid(n) and fnmatch(str(n), '9*4*0'):
        print(n, n // 47, sep='*', end='-')