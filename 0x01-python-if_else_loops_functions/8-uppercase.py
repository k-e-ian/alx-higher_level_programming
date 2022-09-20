#!/usr/bin/python3
def uppercase(str):
    for lower in str:
        if (lower >= 'a' and lower <= 'z'):
            lower = chr(ord(lower) - 32)
        print("{}".format(lower), end="")
    print("")
