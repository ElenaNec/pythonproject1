for i in range(0, 10**8 - 1):
    for x in range(0, 10):
        for y in range(0, 10):
            s = '12' + str(x) + str(y) + '1' + str(i) + '56'
            if int(s) % 317 == 0:
                print(i, s, int(s) // 317)
