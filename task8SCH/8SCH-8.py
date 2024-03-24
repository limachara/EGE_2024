from itertools import product

words = [''.join(word) for word in product('КАРИМ', repeat=5)]
res = []
for word in words:
    t = word.replace('И', 'А')
    if t.count('К') <= 2:
        if t.count('К') == 1 and t.count('КА') == 1:
            res.append(word)
        if t.count('К') == 0:
            res.append(word)
        if t.count('К') == 2 and t.count('КА') == 2:
            res.append(word)
print(len(res))