s = '7' * 88 + '5' * 35
while '777' in s:
    s = s.replace('777', '5', 1)
    s = s.replace('55', '7', 1)
print(s)