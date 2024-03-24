for a in range(1, 100):
    is_a = True
    for x in range(1, 1000):
        d45 = x % 45 == 0
        d30 = x % 30 == 0
        da = x % a == 0
        if not ((d45 or d30) <= da):
            is_a = False
    if is_a:
        print(a)