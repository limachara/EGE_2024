f = open('22.txt')
s = ['A0'[x.isdigit()] for x in f.readline().strip()]
cur_len = 0
max_len = 0
nabor = '0A'
for _ in range(len(nabor)):
    nabor = nabor[1:] + nabor[0]
    for c in s:
        if c == nabor[cur_len % len(nabor)]:
            cur_len += 1
        elif c == nabor[0]:
            cur_len = 1
        else:
            cur_len = 0
        max_len = max(max_len, cur_len)
print(max_len)