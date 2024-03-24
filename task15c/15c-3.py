for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        d42 = 42 % x == 0
        d35 = 35 % x == 0
        da = a % 4 == 0
        if not ( (d42 <= (not d35)) or (3 * x + a < 131) and da ):
            is_a = False
            break
    if is_a:
        print(a)