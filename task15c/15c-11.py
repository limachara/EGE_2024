def f(x, y, a):
    return (5*y + 6*x < 30) or (5*y - 3*x + 40 < 0) or (3*y - x > a)
def is_a(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not f(x, y, a):
                return False
    return True
a = 1000
while not is_a(a):
    a -= 1
print(a)
