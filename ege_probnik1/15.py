for a in range(1000):
    if all((x & 91 == 0) or (not (x & 77 == 0) or (x & a != 0)) for x in range(-1000, 1000)):
        print(a)
        break