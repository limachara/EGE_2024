from itertools import product


words = [''.join(word) for word in product('эмиль', repeat=5) if word[0] != 'ь' ]
res = set()
for word in words:
    if word.count('э') == 1 and word.count('м') == 1 and word.count('и') == 1 and word.count('л') == 1 and word.count('ь') == 1 and 'иэ' not in word:
        res.add(word)
print(len(res))