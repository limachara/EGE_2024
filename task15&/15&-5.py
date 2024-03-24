for a in range(1, 1000):
    is_a = True
    for x in range(1, 100000):
        if ( ((x & 15 != 0) <= ((x & a != 0) <= (x & 108 != 0))) <= ((x & 55 == 0) and (x & a != 0) and (x & 15 != 0)) ):
            is_a = False
            break
    if is_a:
        print(a)