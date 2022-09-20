#!/usr/bin/python3
def fizzbuzz():
    for fizbuz in range(1, 101):
        if (fizbuz % 3 == 0 and fizbuz % 5 == 0):
            print("FizzBuzz", end=" ")
        elif (fizbuz % 3 == 0):
            print("Fizz", end=" ")
        elif (fizbuz % 5 == 0):
            print("Buzz", end=" ")
        else:
            print("{:d}".format(fizbuz), end=" ")
