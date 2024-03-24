с = 874
for a in range(1000, 2000):
    is_a = True
    for x in range(0, 100):
        for y in range(0, 100):
            if not ( ((x > 10) <= ( (x**3 + 3 * x) >= a)) and (( (y * y + 5 * y) > a) <= (y >= 10)) ):
                is_a = False
    if is_a:
        с += 1
print(с)