from re import fullmatch

for n in range(157, 10**10, 157):
    if fullmatch(r'1[13579]*3456[02468]8', str(n)):
        print(n, n // 157, sep='*', end='-')
