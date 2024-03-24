f = open('24.txt')
s = f.readline().strip()
cur_len = 0
max_len = 0
find = []
for x in range(10):
    find.append(f'1{x}1')
    find.append(f'3{x}3')
for k in range(3):
    for i in range(k, len(s), 3):
        if s[i:i+3] in find:
            cur_len += 1
        else:
            cur_len = 0
        if cur_len > max_len:
            max_len = cur_len
print(max_len)