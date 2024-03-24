print('w x y z  f')
for w in 0, 1:
    for x in 0, 1:
        for y in 0,1:
            for z in 0,1:
                f = int( ( (not x and y) <= w ) and ( (x and y) <= (z and w) ) )
                if f == 0:
                    print(w, x, y, z, '', f)