for x in range(1, 15):
    for x in range(1, 17):
        a1 = 1*15**4 + 3*15**3 + 1*15**2 + x*15**1 + 1*15**0
        a2 = 1*17**3 + 3*17**2 + x*17**1 + 3*17**0
        n = a1 + a2
        if n % 11 == 0:
            print(x, n // 11)
            break
    break