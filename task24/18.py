f = open('18.txt')
s = f.readline().strip()
cur_len = 0
max_len = 0
find = ('NLO', 'NOL')
for j in range(3):
    for i in range(j, len(s), 3):
        if s[i:i+3] in find:
            cur_len += 1
        else:
            cur_len = 0
        if cur_len > max_len:
            max_len = cur_len
print(max_len)