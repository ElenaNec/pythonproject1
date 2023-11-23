for i in range(1, 10000):
    n = bin(i)[2:]
    if i % 3 == 0:
        s = str(n) + str(n)[-3:]
    else:
        s = str(n) + str(bin(3 * (i % 3))[2:])
    a = int(s, 2)
    if a >= 76:
        print(i)
        break
