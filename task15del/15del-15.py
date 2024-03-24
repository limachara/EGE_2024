for a in range(1, 1000):
    is_a = True
    for x in range(1, 10000):
        d375 = x % 375 == 0
        d100 = x % 100 == 0
        da = x % a == 0
        if not ( ( (da and d375) <= d100) and (a > 10) ):
            is_a = False
    if is_a:
        print(a)