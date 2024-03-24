for n in range(1, 30):
    s = '@$/' * n
    while '@$' in s or '/@' in s or '/$' in s:
        if '@$' in s:
            s = s.replace('@$', '$@', 1)
        if '/@' in s:
            s = s.replace('/@', '@/', 1)
        if '/$' in s:
            s = s.replace('/$', '$/', 1)
    print(s)