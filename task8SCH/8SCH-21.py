from itertools import permutations

words = [''.join(word) for word in permutations('перевыборы', r = 10)]
res = set()
for word in words:
    d1 = word.replace('ы', 'е').replace('о', 'е').replace('р', 'п').replace('в', 'п').replace('б', 'п')
    if 'ее' not in d1 and 'пп' not in d1 and word.count('е') == 2 and word.count('п') == 1 and word.count('р') == 2 and word.count('в') == 1 and word.count('б') == 1 and word.count('о') == 1 and word.count('ы') == 2:
        res.add(word)

print(len(res))