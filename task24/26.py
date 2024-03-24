f = open('26.txt')
s = f.readline().strip()
cur_len = 0
min_len = float('inf')
start_line = False
for c in s:
    if c == 'A':
        start_line = True
        cur_len = 0
    if start_line:
        cur_len += 1
    if c == 'Z' and cur_len > 2:
        start_line = False
        if cur_len < min_len:
            min_len = cur_len
print(min_len)