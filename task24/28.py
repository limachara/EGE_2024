f = open('28.txt')
s = f.readline()
number = ''
cur_len = 0
max_len = 0
for c in s:
    if c in '0123456789ABCDEFG':
        number += c
        cur_len += 1
    else:
        max_len = max(max_len, cur_len)
        number = ''
        cur_len = 0
print(max_len)