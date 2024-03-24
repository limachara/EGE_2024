f = open('14.txt')
line = f.readline().strip()
cur_len = 1
max_len = 0
for d1, d2 in zip(line, line[1:]):
    if d1 == 'B' and d2 == 'D':
        cur_len = 1
    elif d1 == 'D' and d2 == 'B':
        cur_len = 1
    else:
        cur_len += 1
    if cur_len > max_len:
        max_len = cur_len
print(max_len)