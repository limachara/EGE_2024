f = open('20.txt')
s = f.readline().strip()
cur_len = 0
max_len = 0
nabor = 'KEGE'
for c in s:
    if c == nabor[cur_len % len(nabor)]:
        cur_len += 1
    elif c == nabor[0]:
        cur_len = 1
    else:
        cur_len = 0
    max_len = max(max_len, cur_len)
print(max_len)