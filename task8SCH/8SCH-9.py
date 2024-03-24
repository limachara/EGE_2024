from itertools import product

words = [''.join(word) for word in product('БИЛСТВ', repeat=5)]
res = []
for word in words:
    t = word.replace('Л', 'Б').replace('Т', 'С').replace('В', 'С')
    if t.count('Б') == t.count('С'):
        res.append(word)
print(len(res))