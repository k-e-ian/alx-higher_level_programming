#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp = []
    for i in my_list:
        if i % 2 == 0:
            temp.append(True)
        else:
            temp.append(False)
    return (temp)
