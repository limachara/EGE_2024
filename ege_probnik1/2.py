print('w x y  f')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            f = int( (not x or y) and (w or (not w)) )
            print(w, x, y, '', f)