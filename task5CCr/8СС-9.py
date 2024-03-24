from itertools import product

a = list(map(''.join, product(sorted('ластик'), repeat=5)))
k = 0
for i, word in enumerate(a, start=1):
    d1 = word.replace('а','и').replace('с','л').replace('т','л').replace('к','л')
    if 4045 >= i >= int('20421', 6) and 'ии' not in d1 and 'лл' not in d1:
        k += word.count('и')
print(k)