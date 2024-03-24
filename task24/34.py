a = [len(x) for x in open('34.txt').readline().strip().split('VLADIMIR')]
mn = 999999
for i in range(len(a) - 4):
    mn = min(mn, sum(a[i: i + 4]))
print(mn + 40)