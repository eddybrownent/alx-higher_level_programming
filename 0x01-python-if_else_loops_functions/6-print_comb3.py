#!/usr/bin/python3
for int1 in range(0, 10):
    for int2 in range(int1 + 1, 10):
        if int1 == 8 and int2 == 9:
            print("{}{}".format(int1, int2))
        else:
            print("{}{}".format(int1, int2), end=', ')
