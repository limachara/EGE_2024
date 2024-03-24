a = [len(x) for x in open('35.txt').readline().strip().split('W')]
mn = float('inf')
for i in range(len(a) - 99):
    mn = min(mn, sum(a[i: i + 99]))
print(mn + 100)