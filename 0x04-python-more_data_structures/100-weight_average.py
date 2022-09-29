#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    w_a = sum([x * y for x, y in my_list])
    total = w_a / sum([y for x, y in my_list])
    return total
