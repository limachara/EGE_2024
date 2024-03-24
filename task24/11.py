f = open('11.txt')
line = f.readline().strip()
cur_len = 1
k = 0
for d1, d2 in zip(line, line[1:]):
    if d2 >= d1:
        cur_len += 1
    else:
        if cur_len == 6:
            k += 1
        cur_len = 1
if cur_len == 6:
    k += 1
print(k)