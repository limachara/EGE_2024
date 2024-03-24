for p in range(2, 80):
    for x in range(0, p):
        for y in range(1, p):
            for z in range(0, p):
                a1 = 6*p**3 + x*p**2 + 5*p**1 + x*p**0
                a2 = 1*p**3 + x*p**2 + 6*p**1 + 5*p**0
                n = *p**3 + y*p**2 + 8*p**1 + z*p**0
                if a1 + a2 == n:
                    print(x,y,z)
