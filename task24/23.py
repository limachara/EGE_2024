f = open('23.txt')
s = f.readline().strip()
cur_len = 0
max_len = 0
last_s = 0
R_count = 0
T_count = 0
for c in s:
    if c == 'R' and last_s == 'T':
        cur_len = 1
        R_count = 0
        T_count = 0
    elif c == 'R':
        cur_len += 1
        R_count += 1
    elif c == 'T':
        cur_len += 1
        T_count += 1
    elif c == 'R' and last_s == 'T':
        cur_len = 1
        R_count = 0
        T_count = 0
    elif c != 'T' and c != 'R':
        cur_len = 0
        R_count = 0
        T_count = 0
    if cur_len > max_len and R_count > 0 and T_count > 0:
        max_len = cur_len
    last_s = c
print(max_len)