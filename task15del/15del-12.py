for a in range(1, 2000):
    is_a = True
    for x in range(1, 10000):
        d36 = x % 36 == 0
        d126= x % 126 == 0
        da = x % a == 0
        if not ( (not da or d36 and d126) and (a > 1000) ):
            is_a = False
    if is_a:
        print(a)
