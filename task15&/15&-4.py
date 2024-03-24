for a in range(45, 66):
    is_a = True
    for x in range(1, 100000):
        if (((x & 30 != 0) <= ( x & 10 != 0)) or (x & a != 0)) <= ((x & 10 == 0) and ( x & a == 0) and (x & 21 != 0)):
            is_a = False
            break
    if is_a:
        print(a)