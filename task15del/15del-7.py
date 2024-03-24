for a in range(1, 100):
    is_a = True
    for x in range(1, 5000):
        d56 = x % 56 == 0
        d52 = x % 52 == 0
        da = x % a == 0
        if not ( (da <= d56) or not d52 ):
            is_a = False
    if is_a:
        print(a)