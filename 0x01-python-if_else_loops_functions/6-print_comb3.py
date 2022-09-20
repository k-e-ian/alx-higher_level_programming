#!/usr/bin/python3
index = 1
for num in range(0, 9):
    for num2 in range(index, 10):
        if (index != 9):
            print("{:d}{:d}".format(num, num2), end=", ")
        else:
            print("{:d}{:d}".format(num, num2))
    index += 1
