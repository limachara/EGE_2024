from itertools import product

words = [''.join(word) for word in product('викуля', repeat = 6)]
res = set()
for word in words:
    d1 = word.replace('у', 'и').replace('я', 'и').replace('к', 'в').replace('л', 'в')
    if word.count('в') == 1 and word.count('и') == 1 and word.count('к') == 1 and word.count('у') == 1 and word.count('л') == 1 and word.count('я') == 1  and 'ии' not in d1 and 'вв' not in d1:
        res.add(word)

print(len(res))