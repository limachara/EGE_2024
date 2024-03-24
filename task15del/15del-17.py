for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        d42 = 42 % x == 0
        d35 = 35 % x == 0
        if not ( (d42 <= (not d35)) <= (3 * x + a < 131) ):
            is_a = False
    if is_a:
        print(a)