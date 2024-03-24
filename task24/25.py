f = open('25.txt')
s = f.readline().strip()
count = 0
find = [13131, 13231, 13431, 13631, 13731, 13831]
c_1, c_2, c_4, c_6, c_7, c_8 = 0, 0, 0, 0, 0, 0
for i in range(len(s) - 5):
    if s[i:i+5] == '13131':
        count += 1
        c_1 += 1
    if s[i:i+5] == '13231':
        count += 1
        c_2 += 1
    if s[i:i+5] == '13431':
        count += 1
        c_4 += 1
    if s[i:i+5] == '13631':
        count += 1
        c_6 += 1
    if s[i:i+5] == '13731':
        count += 1
        c_7 += 1
    if s[i:i+5] == '13831':
        count += 1
        c_8 += 1
print(count)
print(c_1, c_2, c_4, c_6, c_7, c_8)
