from itertools import permutations

words = [''.join(word) for word in permutations('арсений', r = 5) if word[0] != 'й']
res = set()
for word in words:
    if 'рай' not in word and word.count('а') <= 1 and word.count('р') <= 1 and word.count('с') <= 1 and word.count('е') <= 1 and word.count('н') <= 1 and word.count('и') <= 1 and word.count('й') <= 1:
        res.add(word)

print(len(res))