for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ( (60 >= x) and (20 >= y) or ((2*y + 5*x) > a) ):
                is_a = False
    if is_a:
        print(a)
