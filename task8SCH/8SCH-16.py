from itertools import product

words = [''.join(word) for word in product('равиль', repeat = 6) if word[0] != 'ь']
res = set()
for word in words:
    d1 = word.replace('и', 'а')
    if 'аь' not in d1 and word.count('р') == 1 and word.count('а') == 1 and word.count('в') == 1 and word.count('и') == 1 and word.count('л') == 1 and word.count('ь') == 1:
        res.add(word)

print(len(res))