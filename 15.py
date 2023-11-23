for a in range(0, 100):
    t = 1
    for x in range(0, 100):
        for y in range(0, 100):
            t *= ((x >= 12) or (3 * x < y) or (x * y < a))
        if t == 1:
            print(a)
            break
