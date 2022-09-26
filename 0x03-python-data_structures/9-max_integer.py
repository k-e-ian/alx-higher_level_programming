#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return (None)
    my_max = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > my_max:
            my_max = my_list[i]
    return (my_max)
