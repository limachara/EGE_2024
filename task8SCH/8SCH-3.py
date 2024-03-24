from itertools import product

words = [''.join(word) for word in product('камиль', repeat=6) if word[0] != 'ь' and word.count('м') == 1]
print(len(words))