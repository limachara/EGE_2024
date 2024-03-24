def f(n):
    summ1 = sum(filter(lambda x: x % 2 == 0, map(int, str(n))))
    summ2 = sum(map(int, str(n)[1::2]))
    return abs(summ1-summ2)


for i in range(10000, 10000000):
    if f(i) == 17:
        print(i)
        break