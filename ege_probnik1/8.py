from itertools import product

k = 0
for a in product('0123456', repeat=6):
    s = ''.join(a)
    even_c = 0
    if s[0] != '0' and s.count('0') == 1:
        for el in s:
            if int(el) % 2 == 0:
                even_c += 1
        if even_c % 2 != 0:
            k += 1
print(k)
