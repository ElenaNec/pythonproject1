print('X Y Z W')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ((x or y) and not(y == z) and not(w)):
                    print(x,y,z,w)
