from itertools import product

words = [''.join(word) for word in product('ВИКТОР', repeat=6)]
res = []
for word in words:
    t = word.replace('К', 'В').replace('Т', 'В').replace('Р', 'В')
    if t.count('В') >= 3:
        res.append(word)
print(len(res))