for a in range(1, 100000):
    for x in range(1, 15):
        for y in range(1, 15):
            m = 2*15**5 + y*15**4 + 2*15**3 + 3*15**2 + x*15**1 + 5*15**0
            n = 6*13**4 + 7*13**3 + x*13**2 + 9*13**1 + y*13**0
            if (m + a) % n == 0:
                print(a)
                break
