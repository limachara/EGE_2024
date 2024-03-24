for a in range(-1000, 1000):
    is_a = True
    for x in range(-10000, 10000):
        if not ( ((x*x <= 20) <= a) and (a <= (x*x <= 144)) ):
            is_a = False
            break
    if is_a:
        print(a)