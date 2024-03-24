for a in range(1, 500):
    is_a = True
    for x in range(1, 100000):
        d45 = x % 45 == 0
        d162 = x % 162 == 0
        da = x % a == 0
        if not ( ( (da and d45) <= d162) and (a > 200)):
            is_a = False
    if is_a:
        print(a)