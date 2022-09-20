#!/usr/bin/python3
def uppercase(str):
    for lower in str:
        if (str >= 'a' and <= 'z'):
            lower = (lower - 32)
        print("{}".format(lower), end="")
    print("")
