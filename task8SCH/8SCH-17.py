from itertools import product

words = [''.join(word) for word in product('настя', repeat=5)]
res = set()
for word in words:
    d1 = word.replace('я', 'а')
    if 'аа' not in d1 and word.count('н') == 1 and word.count('а') == 1 and word.count('с') == 1 and word.count(
            'т') == 1 and word.count('я') == 1:
        res.add(word)

print(len(res))