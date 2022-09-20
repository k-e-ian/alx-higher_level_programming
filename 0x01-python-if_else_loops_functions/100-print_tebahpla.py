#!/usr/bin/python3
for aLpHa in range(122, 96, -1):
    if ((aLpHa % 2) != 0):
        print("{}".format(chr(aLpHa - 32)), end="")
    else:
        print("{}".format(chr(aLpHa)), end="")
